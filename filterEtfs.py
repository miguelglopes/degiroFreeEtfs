import pandas
from database import model
from Common import config

def filterEtf(minimumEtfs, positiveColumns = config["positiveColumns"], negativeColumns=config["negativeColumns"], positiveWeight=1.03, negativeWeight = 1):
    etfs=pandas.DataFrame(list(model.ETF.select().dicts()))

    for i in range(0,100):
        netfs = etfs
        for column in negativeColumns:
            netfs = netfs[netfs[column] <= float(etfs[column].quantile([i/100]))*negativeWeight]
        for column in positiveColumns:
            netfs = netfs[netfs[column] >= float(etfs[column].quantile([(1-i/100)]))*positiveWeight]
        if len(netfs)>=minimumEtfs:
            print(i)
            break

    return netfs

def getAllEtfs():
    return pandas.DataFrame(list(model.ETF.select().dicts()))
