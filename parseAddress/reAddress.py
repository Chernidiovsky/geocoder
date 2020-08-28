# -*- coding: utf-8 -*-
from reProvCityName import *
from codesProvCity import *
import re


def kickFullWidth(string, fillExcept):
    """全角转半角:
    全角字符unicode编码65281~65374 （十六进制 0xFF01 ~ 0xFF5E）
    半角字符unicode编码从33~126 （十六进制 0x21~ 0x7E）
    空格全角为 12288（0x3000），半角为 32（0x20）
    除空格外，按unicode编码排序半角 + 0x7e= 全角"""
    result = re.sub(u"，", u",", string)
    result = re.sub(u"。", u".", result)
    result = re.sub(u"、", u",", result)
    result = re.sub(u"“", u'"', result)
    result = re.sub(u"”", u'"', result)
    result = re.sub(u"‘", u"'", result)
    result = re.sub(u"’", u"'", result)
    result = re.sub(u"【", u"[", result)
    result = re.sub(u"】", u"]", result)
    result = re.sub(u"《", u"<", result)
    result = re.sub(u"》", u">", result)
    result = re.sub(u"『", u"[", result)
    result = re.sub(u"』", u"]", result)
    result = re.sub(u"「", u"[", result)
    result = re.sub(u"」", u"]", result)
    result = re.sub(u"﹃", u"[", result)
    result = re.sub(u"﹄", u"]", result)
    result = re.sub(u"〔", u"{", result)
    result = re.sub(u"〕", u"}", result)
    result = re.sub(u"—", u"-", result)
    result = re.sub(u"·", u"-", result)
    resultStr = u""
    for i in result:
        try:
            inside_code = ord(i)  # 返回字符对应的ASCII或Unicode数值
            if inside_code == 12288:
                inside_code = 32
            if 65281 <= inside_code <= 65374:
                inside_code -= 65248
            resultStr += chr(inside_code)  # 用一个范围在0~255的整数作参数，返回一个对应的字符
        except:
            if fillExcept is None:
                resultStr += i
            else:
                resultStr += fillExcept
    return resultStr


def reAddressCity(address, city):
    if re.search(u"[\u4e00-\u9fa5]+", address) is None or len(address) < 5:
        return ""
    address = kickFullWidth(address, None)
    address = re.sub(u"（", u"_", address)
    address = re.sub(u"）", u"_", address)
    address = re.sub(u"\(", u"_", address)
    address = re.sub(u"\)", u"_", address)
    address = re.sub(u"【", u"_", address)
    address = re.sub(u"】", u"_", address)
    address = re.sub(u"\[", u"_", address)
    address = re.sub(u"]", u"_", address)
    address = re.sub(u"-", u"_", address)
    address = re.sub(u"[^\u4e00-\u9fa5|\w]+", u"", address)
    address = re.sub(u"_", u" ", address)

    def geoFromAddress(oa):
        p, c, ph, ch = "", "", "", ""
        for x in provRe:
            pIdx = oa.find(x[1])
            if pIdx == 0:
                p, ph = x[0], x[1]
                for y in cityRe:
                    cIdx = oa.find(y[1])
                    if cIdx >= 0:
                        c, ch = y[0], y[1]
                        break
                break
        return p, c, ph, ch

    def geoFromCity(oc):
        p, c, ph, ch = "", "", "", ""
        if oc != "":
            for c in cityRe:
                if oc.find(c[1]) >= 0:
                    c, ch = c[0], c[1]
                    break
            p = provRevDic.get(cityDic.get(c, "")[:2], "")
            ph = [x[1] for x in provRe if x[0] == p][0]
        return p, c, ph, ch

    p1, c1, ph1, ch1 = geoFromAddress(address)
    p2, c2, ph2, ch2 = geoFromCity(city)
    if p1 != "" or c1 != "":
        province, city, provinceHead, cityHead = p1, c1, ph1, ch1
    else:
        province, city, provinceHead, cityHead = p2, c2, ph2, ch2

    address = address.replace(province, "", 1)
    address = address.replace(provinceHead, "", 1)
    address = address.replace(city, "", 1)
    for w in [u"区", u"县", u"镇", u"乡", u"村"]:  # 已升级为城市的区县镇乡村，名称改为市来匹配一遍
        address = address.replace(cityHead + w, "", 1)
    address = address.replace(cityHead, "", 1)
    if province in [u"北京市", u"天津市", u"上海市", u"重庆市"]:
        return city + address
    return province + city + address