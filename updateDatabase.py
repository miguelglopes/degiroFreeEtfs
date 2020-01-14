import requests
import json
from tika import parser
import os
from database import model
from Common import config
from peewee import IntegrityError

def getIsinInfo(isin):

    data = {
        'draw' : '1',
        'start' : '0',
        'length' : '25',
        'search[value]' : '',
        'search[regex]' : 'false',
        'lang' : 'en',
        'country' : config["countries"][isin[0:2]],
        'universeType' : 'private',
        'etfsParams' : 'query='+isin+'&tab=volatility&groupField=index'
    }
    headers = {
                'Accept-Encoding': 'gzip, deflate, br',
            }
    session = requests.Session()


    r = session.get("https://www.justetf.com/en/etf-profile.html?tab=overview&isin="+isin, headers=headers)

    r = session.post("https://www.justetf.com/servlet/etfs-table", data=data, headers=headers)
    try:
        r = json.loads(r.text.replace('%','').replace("<br />", " "))['data'][0]
    except IndexError as error:
        print(isin)
        return None
    r["fundSize"]=r["fundSize"].replace(",","")

    return model.dicToEtf(r)

def getFreeIsinsList():
    isins=[]
    freeEtfs = "https://www.degiro.pt/data/pdf/pt/lista-etfs-sem-comissao.pdf"
    path = 'freeEtfs.pdf'
    r = requests.get(freeEtfs)
    with open(path, 'wb') as f:
        f.write(r.content)
    raw = parser.from_file(path)
    os.remove(path)
    for row in raw['content'].split("ISIN Produto Divisa Bolsa")[1].split("\n\n"):
        columns=row.split(" ")
        if len(columns[0])==12:
            isins.append(columns[0])
    return isins

def updateDatabase():
    isins = set(getFreeIsinsList())
    for isin in isins:
        etf = getIsinInfo(isin)
        if etf is not None:
            try:
                etf.save(force_insert=True) #first time
            except IntegrityError:
                etf.save() #updateDB

