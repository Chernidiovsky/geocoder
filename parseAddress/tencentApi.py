# -*- coding: utf-8 -*-
from hashlib import md5
import urllib
import urllib2
import json
import time
from math import sqrt, sin, cos, atan2


tencentAcc = "BXBBZ-YUK6O-IQ7WR-SEWKG-EACS5-N6BJN"
tencentKey = "whZPOEmnEUpj98z4IOlMWMGttYMgE8xh"


def gcj2bdString(lng, lat):
    """高德地图坐标系 -> 百度地图坐标系"""
    x_pi = 3.14159265358979324 * 3000.0 / 180.0
    z = sqrt(lng * lng + lat * lat) + 0.00002 * sin(lat * x_pi)
    theta = atan2(lat, lng) + 0.000003 * cos(lng * x_pi)
    lng = z * cos(theta) + 0.0065
    lat = z * sin(theta) + 0.006
    return lng, lat


def openUrlAddress(address):  # 查询地址，获取经纬度
    head = "https://apis.map.qq.com"
    encodedUrl = "/ws/geocoder/v1?address=%s&key=%s" % (address.encode("utf-8"), tencentAcc)
    suffix = "&sig=" + md5(encodedUrl + tencentKey).hexdigest()
    encodedUrl = head + encodedUrl + suffix
    encodedUrl = urllib.quote(encodedUrl, safe="/:=&?#+!$,;'@()*[]")
    time.sleep(0.5)
    res = urllib2.urlopen(encodedUrl).read()
    js = json.loads(res, encoding="utf-8")
    return js


def openUrlCoordinate(lng, lat):
    head = "https://apis.map.qq.com"
    encodedUrl = "/ws/geocoder/v1?key=%s&location=%s,%s" % (tencentAcc, lat, lng)
    suffix = "&sig=" + md5(encodedUrl + tencentKey).hexdigest()
    encodedUrl = head + encodedUrl + suffix
    time.sleep(0.5)
    res = urllib2.urlopen(encodedUrl).read()
    js = json.loads(res, encoding="utf-8")
    return js


if __name__ == "__main__":
    dic = openUrlAddress(u"北京市海淀区彩和坊路海淀西大街74号")
    print(dic)