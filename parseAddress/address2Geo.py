# -*- coding: utf-8 -*-
from parseAddress.reAddress import reAddressCity
from parseAddress.tencentApi import openUrlAddress, gcj2bdString
from codesProvCity import cityDic, cityRevDic, provRevDic
import Levenshtein


def addressToGeo(row):
    """
    输入: [cust_code, addresses list, origCity]
    输出: ["cust_code", "status", "lng", "lat", "source_address", "province", "city", "district", "street",
          "street_number", "reliability", "level", "has_error", "error_message"]
    """
    [custCode, addresses, origCity] = row
    if custCode == "" or custCode is None:
        return ["", -10, 0.0, 0.0, "", "", "", "", "", "", 0, "", "y", u"cust_code为空"]
    if addresses is None:
        addresses = []
    elif isinstance(addresses, unicode):
        addresses = addresses.split("|")
    elif not isinstance(addresses, list):
        try:
            addresses = list(addresses)
        except:
            return ["", -10, 0.0, 0.0, "", "", "", "", "", "", 0, "", "y", u"地址无效"]
    origCity = "" if origCity is None else origCity

    custProv = getProvince(custCode)
    custCity = getCity(custCode)
    if cityDic.get(origCity, "00")[:2] != custCode[:2]:  # origCity和cust_code在省份上不一致
        origCity = custCity

    try:
        results, oops = [], []
        for address in addresses:
            addressRe = reAddressCity(address, origCity)
            if addressRe == "":
                oops.append("null")
                continue
            dic = openUrlAddress(addressRe)
            status = dic["status"]
            if status != 0:
                oops.append(str(status))
                continue
            dic = dic["result"]
            reliability = int(dic["reliability"])
            level = levelDict(dic["level"])
            lng = dic["location"]["lng"]
            lat = dic["location"]["lat"]
            lng, lat = gcj2bdString(lng, lat)
            dic = dic["address_components"]
            province = dic["province"]
            city = dic["city"]
            district = dic["district"]
            street = dic["street"]
            streetNumber = dic["street_number"]
            results.append([lng, lat, province, city, district, street, streetNumber, address, reliability, level])
        if not results:
            return [custCode, -10, 0.0, 0.0, "", "", "", "", "", "", 0, "", "y", "|".join(oops)]

        results2 = []
        for result in results:
            # 省份匹配
            if result[2] == custProv:
                # 解析结果、疑似城市、cust_code解析城市 完美一致
                if result[3] == custCity == origCity:
                    results2.append([custCode, 0] + result + ["n", ""])
                # 解析结果、疑似城市一致，cust_code解析城市不同，权重-1
                elif result[3] == origCity != custCity:
                    results2.append([custCode, -1] + result + ["n", ""])
                # 解析结果、cust_code解析城市一致，疑似城市不同
                elif result[3] == custCity != origCity:
                    results2.append([custCode, 0] + result + ["n", ""])
                # 城市完全不匹配，权重-5
                else:
                    results2.append([custCode, -5] + result + ["y", origCity])
            # 省市都不匹配，权重-9
            else:
                results2.append([custCode, -9] + results[0] + ["y", custProv])

        results2 = sorted(results2, key=lambda x: x[1] + x[10], reverse=True)  # 按省市匹配评分
        maxScr = results2[0][1] + results2[0][10]
        results2 = [result for result in results2 if result[1] + result[10] == maxScr]
        score, finalResult = 0., results2[0]
        for result in results2:  # 按解析结果与原地址相似度再评分
            geoInfo = "".join(result[5:9])
            tmp = Levenshtein.ratio(geoInfo, result[4])
            if tmp > score:
                score = tmp
                finalResult = result
        return finalResult

    except Exception as e:
        return [custCode, -10, 0.0, 0.0, "", "", "", "", "", "", 0, "", "y", e]


def getProvince(ass):
    return provRevDic.get(ass[0:2], "")


def getCity(ass):
    codeCity = cityRevDic.get(ass[0:2], "")
    codeCity = cityRevDic.get(ass[0:4], "") if codeCity == "" else codeCity
    codeCity = cityRevDic.get(ass[0:6], "") if codeCity == "" else codeCity
    return codeCity


def levelDict(num):
    dic = {1: u"城市", 2: u"区、县", 3: u"乡镇、街道", 4: u"村、社区", 5: u"开发区", 6: u"热点区域、商圈", 7: u"道路", 8: u"道路附属点：交叉口、收费站、出入口等",
           9: u"门址", 10: u"小区、大厦", 11: u"POI点"}
    return dic.get(int(num), "UNKNOWN")


if __name__ == "__main__":
    inputs = [u"620503100991", u"甘肃省天水市天水办事处", u"天水市"]
    outputs = [unicode(x) if x != "" else "..." for x in addressToGeo(inputs)]
    print("\n".join(outputs))