# -*- coding: utf-8 -*-
import pandas as pd


# 根据geo_code.csv更新cityDic、cityRevDic
def updateCityDict():
    df = pd.read_csv("geo_code.csv")
    cityAndCodes = df[["city", "city_code"]].drop_duplicates().values.tolist()
    cityAndCodes = sorted(cityAndCodes, key=lambda r: r[1])

    print("cityDic = {")

    for row in cityAndCodes:
        print('u"%s": "%s",' % (row[0], row[1]))

    print("}\n\ncityRevDic = {")

    for row in cityAndCodes:
        if row[1].endswith("0000"):
            cityCodeShort = row[1][:2]
        elif row[1].endswith("00"):
            cityCodeShort = row[1][:4]
        else:
            cityCodeShort = row[1]
        print('"%s": u"%s",' % (cityCodeShort, row[0]))

    print("}")


# 根据geo_code.csv更新provRe、cityRe
def updateShortName():
    df = pd.read_csv("geo_code.csv")
    provinces = df["province"].drop_duplicates().tolist()
    cities = df["city"].drop_duplicates().tolist()

    print("provRe = [")

    for i in sorted(provinces):
        if i.endswith(u"省") or i.endswith(u"市"):
            print(u'[u"%s", u"%s"],' % (i, i[:-1]))
        elif i.endswith(u"自治区") and i != u'内蒙古自治区':
            print(u'[u"%s", u"%s"],' % (i, i[:2]))
        else:
            print(u'[u"%s", u"%s"],' % (i, i[:3]))

    print("]\n\ncityRe = [")

    for i in sorted(cities):
        if i.endswith(u"市") or i.endswith(u"县") or i.endswith(u"盟"):
            print(u'[u"%s", u"%s"],' % (i, i[:-1]))
        elif i.endswith(u"地区") or i.endswith(u"林区"):
            print(u'[u"%s", u"%s"],' % (i, i[:-2]))
        elif i in [u"西双版纳傣族自治州", u"巴音郭楞蒙古自治州", u"博尔塔拉蒙古自治州", u"克孜勒苏柯尔克孜自治州"]:
            print(u'[u"%s", u"%s"],' % (i, i[:4]))
        elif i in [u"黔西南布依族苗族自治州", u"黔东南苗族侗族自治州"]:
            print(u'[u"%s", u"%s"],' % (i, i[:3]))
        elif i in [u"海南藏族自治州"]:
            print(u'[u"%s", u"%s"],' % (i, i))
        else:
            print(u'[u"%s", u"%s"],' % (i, i[:2]))

    print("]")