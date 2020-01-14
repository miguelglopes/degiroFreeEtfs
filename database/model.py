import peewee
from playhouse.shortcuts import dict_to_model
from Common import config

db = peewee.MySQLDatabase(
    config["database"]["db"],
    user=config["database"]["user"],
    password=config["database"]["pwd"],
    host=config["database"]["host"],
    port=config["database"]["port"],
)

class ETF(peewee.Model):
    isin = peewee.CharField(null=False,primary_key = True, max_length=12)
    fiveYearVolatilityCUR= peewee.DoubleField(null=True)
    fiveYearReturnPerRiskCUR= peewee.DoubleField(null=True)
    yearVolatilityCUR= peewee.DoubleField(null=True)
    distributionPolicy= peewee.CharField(null=True, max_length=25)
    fundCurrency= peewee.CharField(null=True, max_length=25)
    threeMonthReturnCUR= peewee.DoubleField(null=True)
    monthReturnCUR= peewee.DoubleField(null=True)
    sixMonthReturnCUR= peewee.DoubleField(null=True)
    inceptionDate= peewee.CharField(null=True, max_length=25)
    threeYearVolatilityCUR= peewee.DoubleField(null=True)
    yearReturnPerRiskCUR= peewee.DoubleField(null=True)
    yearReturn2CUR= peewee.DoubleField(null=True)
    yearReturn4CUR= peewee.DoubleField(null=True)
    groupValue= peewee.CharField(null=True, max_length=25)
    wkn= peewee.CharField(null=True, max_length=25)
    ter= peewee.CharField(null=True, max_length=25)
    replicationMethod= peewee.CharField(null=True, max_length=25)
    hasSecuritiesLending= peewee.CharField(null=True, max_length=25)
    ticker= peewee.CharField(null=True, max_length=25)
    yearReturnCUR= peewee.DoubleField(null=True)
    fundSize= peewee.IntegerField(null=True)
    threeYearReturnPerRiskCUR= peewee.DoubleField(null=True)
    domicileCountry= peewee.CharField(null=True, max_length=25)
    threeYearReturnCUR= peewee.DoubleField(null=True)
    valorNumber= peewee.CharField(null=True, max_length=25)
    name= peewee.CharField(null=True, max_length=25)
    yearReturn3CUR= peewee.DoubleField(null=True)
    fiveYearReturnCUR= peewee.DoubleField(null=True)
    ytdReturnCUR= peewee.DoubleField(null=True)
    weekReturnCUR= peewee.DoubleField(null=True)
    savingsPlanReady= peewee.CharField(null=True, max_length=25)
    yearReturn1CUR= peewee.DoubleField(null=True)

    class Meta:
        db_table = "ETF"
        database = db

def dicToEtf(dic):
    return dict_to_model(ETF, dic, ignore_unknown=True)

tables = [ETF]
db.create_tables(tables, safe=True)