# -*- coding: utf-8 -*-
from crawlGeoCodes.crawlUtils import utilsBrowser, openCrawlUrl
import pandas as pd
import re


def sepNameCode(a, b):
    if re.search("[\d]", a) is None:
        name = a
        code = b
    else:
        name = b
        code = a
    return name, code[0:6]


def reformat(row):
    [p, c, d, pc, cc, dc] = row
    if p in [u"北京市", u"天津市", u"上海市", u"重庆市"]:  # 直辖市
        return [p, p, d, pc, pc, dc]
    if c.endswith(u"区划"):  # 省级直辖市
        return [p, d, d, pc, dc, dc]
    return row


def getDistrictCode(interval):
    columns = ["province", "city", "district", "province_code", "city_code", "district_code"]
    urlBasic = "https://xingzhengquhua.51240.com/"
    provinces = openCrawlUrl(chromeBrowser, urlBasic, interval=interval).find("table").find_all('a')[1:]

    data = []
    for i in range(len(provinces) / 2):
        province, provinceCode = sepNameCode(provinces[i * 2].string, provinces[i * 2 + 1].string)
        print("%s %s" % (province, provinceCode))

        urlProv = urlBasic + provinces[i * 2 + 1].get('href')
        cities = openCrawlUrl(chromeBrowser, urlProv, interval=interval).find("table").find_all('a')[2:]

        for j in range(len(cities) / 2):
            city, cityCode = sepNameCode(cities[j * 2].string, cities[j * 2 + 1].string)
            print("%s %s" % (city, cityCode))

            urlCity = urlBasic + cities[j * 2].get('href')
            districts = openCrawlUrl(chromeBrowser, urlCity, interval=interval).find("table").find_all('a')[3:]

            for k in range(len(districts) / 2):
                district, districtCode = sepNameCode(districts[k * 2].string, districts[k * 2 + 1].string)
                print("%s %s" % (district, districtCode))

                values = [province, city, district, provinceCode, cityCode, districtCode]
                values = reformat(values)
                print(", ".join(values))
                data.append(values)
    return pd.DataFrame(data=data, columns=columns)


if __name__ == "__main__":
    chromeBrowser = utilsBrowser("chromedriver")
    df = getDistrictCode(10)
    chromeBrowser.quit()
    df = df.drop_duplicates()
    df.to_csv("geo_code.csv", encoding="utf-8")
