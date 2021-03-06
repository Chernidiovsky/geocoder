# -*- coding: utf-8 -*-
# =========================== 旧行政区划代码用于身份证 =========================== #

idcardDic = {"652623": u"阿勒泰地区", "652622": u"阿勒泰地区", "362432": u"吉安市", "362433": u"吉安市", "362430": u"吉安市",
             "362431": u"萍乡市", "152601": u"乌兰察布市", "211226": u"沈阳市", "211225": u"沈阳市", "132123": u"邯郸市",
             "132122": u"邯郸市", "132121": u"邯郸市", "132127": u"邯郸市", "132126": u"邯郸市", "132125": u"邯郸市", "132124": u"邯郸市",
             "132129": u"邯郸市", "132128": u"邯郸市", "652627": u"阿勒泰地区", "652626": u"阿勒泰地区", "352104": u"南平市",
             "352101": u"南平市", "652625": u"阿勒泰地区", "352103": u"南平市", "352102": u"南平市", "652624": u"阿勒泰地区",
             "511227": u"重庆市", "532701": u"普洱市", "372330": u"滨州市", "372331": u"淄博市", "422413": u"荆州市", "132801": u"廊坊市",
             "342602": u"合肥市", "342601": u"合肥市", "372925": u"菏泽市", "372924": u"菏泽市", "372927": u"济宁市", "372926": u"菏泽市",
             "372923": u"菏泽市", "372922": u"菏泽市", "372929": u"菏泽市", "372928": u"菏泽市", "152829": u"巴彦淖尔市",
             "513070": u"达州市", "152822": u"巴彦淖尔市", "152823": u"巴彦淖尔市", "612133": u"渭南市", "152825": u"巴彦淖尔市",
             "652401": u"伊犁哈萨克自治州", "612130": u"渭南市", "132321": u"石家庄市", "132323": u"石家庄市", "132322": u"石家庄市",
             "132325": u"石家庄市", "132324": u"石家庄市", "132326": u"石家庄市", "132329": u"石家庄市", "142754": u"运城市",
             "379012": u"威海市", "410426": u"许昌市", "654121": u"伊犁哈萨克自治州", "352127": u"南平市", "352126": u"南平市",
             "352124": u"南平市", "352123": u"南平市", "352122": u"南平市", "352121": u"南平市", "352129": u"南平市", "352128": u"南平市",
             "412372": u"商丘市", "372131": u"烟台市", "452124": u"南宁市", "652457": u"伊犁哈萨克自治州", "512930": u"南充市",
             "512931": u"广元市", "512938": u"南充市", "422432": u"荆门市", "422431": u"荆门市", "422430": u"荆门市", "422434": u"荆州市",
             "452629": u"百色市", "452628": u"百色市", "452621": u"百色市", "452623": u"百色市", "452622": u"百色市", "452625": u"百色市",
             "452624": u"百色市", "452627": u"百色市", "452626": u"百色市", "372901": u"菏泽市", "460022": u"文昌市", "460023": u"琼海市",
             "460021": u"海口市", "460024": u"万宁市", "460025": u"定安县", "460028": u"临高县", "612423": u"安康市", "612422": u"安康市",
             "612425": u"安康市", "612424": u"安康市", "612426": u"安康市", "612428": u"安康市", "342524": u"宣城市", "231026": u"鸡西市",
             "231027": u"鸡西市", "532130": u"昭通市", "532131": u"昭通市", "412926": u"南阳市", "412927": u"南阳市", "412924": u"南阳市",
             "412925": u"南阳市", "412922": u"南阳市", "412923": u"南阳市", "412920": u"南阳市", "412921": u"南阳市", "412928": u"南阳市",
             "412929": u"南阳市", "412315": u"商丘市", "142731": u"运城市", "132302": u"石家庄市", "132301": u"石家庄市",
             "142732": u"运城市", "512329": u"重庆市", "512328": u"重庆市", "512327": u"重庆市", "512326": u"重庆市", "512325": u"重庆市",
             "512324": u"重庆市", "512323": u"重庆市", "512322": u"重庆市", "512321": u"重庆市", "342834": u"安庆市", "342830": u"池州市",
             "342832": u"安庆市", "412718": u"周口市", "412717": u"周口市", "132400": u"保定市", "132401": u"保定市", "512912": u"南充市",
             "512913": u"南充市", "512914": u"南充市", "510202": u"重庆市", "510203": u"重庆市", "510200": u"重庆市", "510201": u"重庆市",
             "510204": u"重庆市", "510205": u"重庆市", "441229": u"云浮市", "441228": u"云浮市", "513826": u"眉山市", "441227": u"云浮市",
             "513824": u"眉山市", "513822": u"眉山市", "142128": u"朔州市", "142129": u"朔州市", "142124": u"大同市", "142125": u"大同市",
             "142126": u"朔州市", "142127": u"朔州市", "142121": u"大同市", "142122": u"大同市", "142123": u"大同市", "432506": u"娄底市",
             "432504": u"娄底市", "432502": u"娄底市", "432503": u"娄底市", "432500": u"娄底市", "432501": u"娄底市", "452601": u"百色市",
             "370981": u"莱芜市", "460004": u"海口市", "460005": u"文昌市", "460006": u"万宁市", "460007": u"东方市",
             "460001": u"五指山市", "460002": u"琼海市", "460003": u"儋州市", "519004": u"乐山市", "519003": u"成都市",
             "519002": u"绵阳市", "519001": u"德阳市", "632128": u"海东市", "632122": u"海东市", "632123": u"海东市", "632121": u"海东市",
             "632126": u"海东市", "412901": u"南阳市", "412902": u"南阳市", "412903": u"南阳市", "412904": u"南阳市", "412906": u"南阳市",
             "513524": u"重庆市", "513525": u"重庆市", "513522": u"重庆市", "513523": u"重庆市", "513521": u"重庆市", "362329": u"上饶市",
             "362326": u"上饶市", "362327": u"鹰潭市", "362324": u"上饶市", "362325": u"上饶市", "362322": u"上饶市", "362323": u"上饶市",
             "362321": u"上饶市", "433022": u"怀化市", "433023": u"怀化市", "433021": u"怀化市", "433026": u"怀化市", "433027": u"怀化市",
             "433024": u"怀化市", "433025": u"怀化市", "433028": u"怀化市", "433029": u"怀化市", "522246": u"铜仁市", "412731": u"周口市",
             "542430": u"那曲市", "510224": u"重庆市", "510225": u"重庆市", "510226": u"重庆市", "510227": u"重庆市", "510221": u"重庆市",
             "510222": u"重庆市", "510223": u"重庆市", "510228": u"重庆市", "510229": u"重庆市", "432520": u"娄底市", "432522": u"娄底市",
             "432523": u"邵阳市", "432524": u"娄底市", "432526": u"娄底市", "512597": u"宜宾市", "452327": u"桂林市", "132428": u"保定市",
             "232602": u"黑河市", "232601": u"黑河市", "132530": u"张家口市", "132531": u"张家口市", "132532": u"张家口市",
             "132533": u"张家口市", "342626": u"合肥市", "132424": u"保定市", "412960": u"南阳市", "362300": u"上饶市",
             "362301": u"上饶市", "362304": u"上饶市", "432201": u"岳阳市", "432202": u"岳阳市", "210719": u"葫芦岛市",
             "232625": u"黑河市", "232623": u"黑河市", "232622": u"黑河市", "533025": u"保山市", "640382": u"银川市", "142263": u"忻州市",
             "433001": u"怀化市", "433002": u"怀化市", "412364": u"商丘市", "412366": u"商丘市", "522229": u"铜仁市", "522228": u"铜仁市",
             "522221": u"铜仁市", "522223": u"铜仁市", "522222": u"铜仁市", "522225": u"铜仁市", "522224": u"铜仁市", "522227": u"铜仁市",
             "522226": u"铜仁市", "511131": u"眉山市", "511130": u"眉山市", "542335": u"日喀则市", "512950": u"南充市",
             "622428": u"定西市", "622422": u"定西市", "622421": u"定西市", "622426": u"定西市", "622427": u"定西市", "622424": u"定西市",
             "542623": u"林芝市", "542622": u"林芝市", "542621": u"林芝市", "542627": u"林芝市", "542626": u"林芝市", "542625": u"林芝市",
             "542624": u"林芝市", "132331": u"石家庄市", "222302": u"白城市", "362528": u"抚州市", "362524": u"抚州市",
             "362526": u"抚州市", "612132": u"渭南市", "432226": u"岳阳市", "232606": u"黑河市", "232604": u"黑河市", "232603": u"黑河市",
             "232600": u"黑河市", "442501": u"惠州市", "452583": u"玉林市", "342401": u"六安市", "342400": u"六安市", "142201": u"忻州市",
             "142202": u"忻州市", "142205": u"忻州市", "142204": u"忻州市", "512310": u"重庆市", "342542": u"宣城市", "412301": u"商丘市",
             "412307": u"商丘市", "452131": u"崇左市", "452130": u"崇左市", "452133": u"崇左市", "452132": u"崇左市",
             "652101": u"吐鲁番市", "422701": u"宜昌市", "422702": u"宜昌市", "612701": u"榆林市", "432560": u"娄底市",
             "442530": u"汕尾市", "442531": u"汕尾市", "513922": u"资阳市", "513923": u"资阳市", "542340": u"日喀则市",
             "542341": u"日喀则市", "542342": u"日喀则市", "362341": u"上饶市", "142223": u"忻州市", "142222": u"忻州市",
             "142220": u"忻州市", "142226": u"忻州市", "142224": u"忻州市", "342427": u"六安市", "342426": u"六安市", "342425": u"六安市",
             "342424": u"六安市", "342423": u"六安市", "342422": u"六安市", "342421": u"六安市", "412324": u"商丘市", "412325": u"商丘市",
             "412326": u"商丘市", "412327": u"商丘市", "412321": u"商丘市", "412322": u"商丘市", "412323": u"商丘市", "342529": u"宣城市",
             "412328": u"商丘市", "452113": u"南宁市", "332512": u"丽水市", "359001": u"三明市", "359002": u"泉州市",
             "652122": u"吐鲁番市", "652123": u"吐鲁番市", "412522": u"洛阳市", "422729": u"宜昌市", "422728": u"宜昌市",
             "422723": u"宜昌市", "422722": u"宜昌市", "422721": u"宜昌市", "422727": u"宜昌市", "422726": u"宜昌市", "422725": u"宜昌市",
             "422724": u"宜昌市", "152701": u"鄂尔多斯市", "510282": u"重庆市", "510283": u"重庆市", "510281": u"重庆市",
             "362133": u"赣州市", "362131": u"赣州市", "362130": u"赣州市", "362137": u"赣州市", "362136": u"赣州市", "362135": u"赣州市",
             "352602": u"龙岩市", "352601": u"龙岩市", "370103": u"济宁市", "513902": u"资阳市", "542228": u"山南市", "542226": u"山南市",
             "542225": u"山南市", "542224": u"山南市", "542222": u"山南市", "542322": u"日喀则市", "542323": u"日喀则市",
             "542321": u"日喀则市", "542326": u"日喀则市", "542327": u"日喀则市", "542324": u"日喀则市", "542325": u"日喀则市",
             "542328": u"日喀则市", "542329": u"日喀则市", "132901": u"沧州市", "132903": u"沧州市", "132902": u"沧州市",
             "132906": u"沧州市", "432627": u"邵阳市", "432626": u"邵阳市", "432625": u"邵阳市", "432624": u"邵阳市", "432623": u"邵阳市",
             "432622": u"邵阳市", "432621": u"邵阳市", "342501": u"宣城市", "342502": u"宣城市", "232131": u"哈尔滨市",
             "232130": u"哈尔滨市", "413076": u"信阳市", "230832": u"双鸭山市", "230830": u"鹤岗市", "412828": u"驻马店市",
             "332527": u"丽水市", "622110": u"酒泉市", "152723": u"鄂尔多斯市", "152722": u"鄂尔多斯市", "152727": u"鄂尔多斯市",
             "152726": u"鄂尔多斯市", "152725": u"鄂尔多斯市", "152724": u"鄂尔多斯市", "152728": u"鄂尔多斯市", "422301": u"咸宁市",
             "422302": u"咸宁市", "362201": u"宜春市", "352624": u"龙岩市", "352625": u"龙岩市", "352626": u"龙岩市", "352627": u"龙岩市",
             "352622": u"龙岩市", "352623": u"龙岩市", "452328": u"桂林市", "452329": u"桂林市", "452322": u"桂林市", "452323": u"桂林市",
             "452325": u"桂林市", "372432": u"德州市", "372431": u"德州市", "372430": u"济南市", "542301": u"日喀则市",
             "432429": u"常德市", "432428": u"张家界市", "432425": u"常德市", "432424": u"常德市", "432427": u"常德市",
             "432426": u"常德市", "432421": u"常德市", "432423": u"常德市", "432422": u"常德市", "452528": u"玉林市", "452526": u"玉林市",
             "452527": u"玉林市", "452524": u"贵港市", "452525": u"玉林市", "452522": u"贵港市", "452523": u"贵港市", "452521": u"玉林市",
             "132929": u"沧州市", "132928": u"沧州市", "132923": u"沧州市", "132927": u"沧州市", "132926": u"沧州市", "132924": u"沧州市",
             "512301": u"重庆市", "512300": u"重庆市", "432640": u"邵阳市", "622630": u"陇南市", "612623": u"延安市", "612622": u"延安市",
             "612621": u"延安市", "612626": u"延安市", "612625": u"延安市", "612624": u"延安市", "612629": u"延安市", "612628": u"延安市",
             "511204": u"重庆市", "511201": u"重庆市", "511203": u"重庆市", "511202": u"重庆市", "413012": u"信阳市", "413016": u"信阳市",
             "342922": u"池州市", "342923": u"池州市", "342921": u"池州市", "440528": u"揭阳市", "440522": u"潮州市", "440525": u"揭阳市",
             "440527": u"揭阳市", "440526": u"揭阳市", "211325": u"葫芦岛市", "533521": u"临沧市", "652521": u"塔城地区",
             "652522": u"塔城地区", "652523": u"塔城地区", "652524": u"塔城地区", "652525": u"塔城地区", "652526": u"塔城地区",
             "652527": u"塔城地区", "652528": u"塔城地区", "422327": u"黄石市", "422326": u"咸宁市", "422325": u"咸宁市",
             "422324": u"咸宁市", "422323": u"咸宁市", "422322": u"咸宁市", "422321": u"咸宁市", "142619": u"临汾市", "132441": u"保定市",
             "132442": u"保定市", "522519": u"安顺市", "132222": u"邢台市", "522511": u"安顺市", "412826": u"驻马店市",
             "352204": u"宁德市", "352202": u"宁德市", "352203": u"宁德市", "352201": u"宁德市", "362502": u"抚州市", "362501": u"抚州市",
             "452501": u"玉林市", "452502": u"贵港市", "452503": u"玉林市", "452504": u"贵港市", "452507": u"玉林市", "442830": u"云浮市",
             "432405": u"常德市", "432402": u"常德市", "432401": u"常德市", "142424": u"晋中市", "142427": u"晋中市", "142421": u"晋中市",
             "142420": u"晋中市", "142423": u"晋中市", "142422": u"晋中市", "142429": u"晋中市", "142428": u"晋中市", "511226": u"重庆市",
             "511225": u"重庆市", "511224": u"重庆市", "511223": u"重庆市", "511222": u"重庆市", "511221": u"重庆市", "511228": u"重庆市",
             "429003": u"襄阳市", "413036": u"信阳市", "429001": u"随州市", "320819": u"宿迁市", "342901": u"池州市",
             "412801": u"驻马店市", "362121": u"赣州市", "422129": u"黄冈市", "422128": u"黄冈市", "422125": u"黄冈市",
             "422124": u"黄冈市", "422127": u"黄冈市", "422126": u"黄冈市", "422121": u"黄冈市", "422123": u"黄冈市", "132404": u"保定市",
             "512222": u"重庆市", "512223": u"重庆市", "512221": u"重庆市", "512226": u"重庆市", "512227": u"重庆市", "512224": u"重庆市",
             "512225": u"重庆市", "512228": u"重庆市", "512229": u"重庆市", "142630": u"临汾市", "142631": u"临汾市", "142632": u"临汾市",
             "142633": u"临汾市", "142634": u"临汾市", "142635": u"临汾市", "142636": u"临汾市", "142227": u"忻州市", "142225": u"忻州市",
             "142228": u"忻州市", "420423": u"荆州市", "132429": u"保定市", "132422": u"保定市", "132423": u"保定市", "132421": u"保定市",
             "132426": u"保定市", "132427": u"保定市", "132425": u"保定市", "372814": u"临沂市", "352220": u"宁德市", "352221": u"宁德市",
             "352222": u"福州市", "352224": u"宁德市", "352225": u"宁德市", "352226": u"宁德市", "352227": u"宁德市", "352228": u"宁德市",
             "352229": u"宁德市", "342522": u"宣城市", "342523": u"宣城市", "342521": u"宣城市", "342527": u"宣城市", "362529": u"抚州市",
             "362522": u"抚州市", "362523": u"抚州市", "152312": u"通辽市", "362525": u"抚州市", "362527": u"抚州市", "342130": u"阜阳市",
             "339010": u"宁波市", "339011": u"绍兴市", "142402": u"晋中市", "142401": u"晋中市", "412823": u"驻马店市",
             "412822": u"驻马店市", "412821": u"驻马店市", "412827": u"驻马店市", "412825": u"驻马店市", "412824": u"驻马店市",
             "412829": u"驻马店市", "362200": u"宜春市", "362203": u"宜春市", "362202": u"宜春市", "362204": u"宜春市",
             "612328": u"汉中市", "612329": u"汉中市", "612322": u"汉中市", "612323": u"汉中市", "612321": u"汉中市", "612326": u"汉中市",
             "612327": u"汉中市", "612324": u"汉中市", "612325": u"汉中市", "422103": u"黄冈市", "422102": u"黄冈市", "422101": u"鄂州市",
             "542133": u"昌都市", "542132": u"昌都市", "512201": u"重庆市", "152125": u"呼伦贝尔市", "152127": u"呼伦贝尔市",
             "152126": u"呼伦贝尔市", "152123": u"呼伦贝尔市", "152122": u"呼伦贝尔市", "152129": u"呼伦贝尔市", "152128": u"呼伦贝尔市",
             "370620": u"威海市", "142729": u"运城市", "522128": u"遵义市", "522129": u"遵义市", "522127": u"遵义市", "522124": u"遵义市",
             "522125": u"遵义市", "522122": u"遵义市", "522123": u"遵义市", "522121": u"遵义市", "533021": u"保山市", "533023": u"保山市",
             "533022": u"保山市", "370729": u"日照市", "533024": u"保山市", "132402": u"保定市", "372833": u"临沂市", "372832": u"临沂市",
             "372831": u"临沂市", "372830": u"临沂市", "420425": u"荆州市", "432930": u"永州市", "232312": u"绥化市", "230228": u"大庆市",
             "230226": u"大庆市", "432330": u"益阳市", "432333": u"益阳市", "432332": u"益阳市", "132233": u"邢台市", "132232": u"邢台市",
             "132231": u"邢台市", "132237": u"邢台市", "132236": u"邢台市", "132235": u"邢台市", "132234": u"邢台市", "532228": u"曲靖市",
             "372533": u"聊城市", "372531": u"聊城市", "362229": u"宜春市", "362228": u"宜春市", "612301": u"汉中市", "362223": u"宜春市",
             "362222": u"宜春市", "362221": u"宜春市", "362227": u"宜春市", "362226": u"宜春市", "532233": u"曲靖市", "532232": u"昆明市",
             "532231": u"昆明市", "432831": u"郴州市", "152106": u"呼伦贝尔市", "152105": u"呼伦贝尔市", "152104": u"呼伦贝尔市",
             "152103": u"呼伦贝尔市", "152102": u"呼伦贝尔市", "152101": u"呼伦贝尔市", "152100": u"巴彦淖尔市", "342223": u"宿州市",
             "452482": u"贺州市", "452731": u"河池市", "452730": u"河池市", "460026": u"屯昌县", "460027": u"澄迈县", "460029": u"儋州市",
             "522100": u"遵义市", "522101": u"遵义市", "522102": u"遵义市", "522103": u"遵义市", "612421": u"安康市", "340224": u"池州市",
             "533001": u"保山市", "533000": u"保山市", "420400": u"荆州市", "622429": u"定西市", "342174": u"阜阳市", "440230": u"清远市",
             "232332": u"绥化市", "232331": u"绥化市", "232330": u"绥化市", "232336": u"绥化市", "142331": u"吕梁市", "142330": u"吕梁市",
             "142333": u"吕梁市", "142332": u"吕梁市", "622425": u"定西市", "452229": u"柳州市", "452228": u"柳州市", "452225": u"来宾市",
             "452224": u"来宾市", "452227": u"柳州市", "452226": u"来宾市", "452223": u"柳州市", "452222": u"柳州市", "370919": u"莱芜市",
             "362132": u"赣州市", "362134": u"赣州市", "612427": u"安康市", "342324": u"滁州市", "342325": u"滁州市", "342326": u"滁州市",
             "342327": u"滁州市", "342321": u"滁州市", "342322": u"滁州市", "342323": u"滁州市", "419004": u"许昌市", "419005": u"新乡市",
             "419006": u"新乡市", "419002": u"平顶山市", "419003": u"焦作市", "513001": u"达州市", "513002": u"达州市",
             "332631": u"台州市", "612429": u"安康市", "372876": u"临沂市", "532730": u"普洱市", "372728": u"济宁市", "372726": u"济宁市",
             "372724": u"济宁市", "422287": u"孝感市", "652425": u"伊犁哈萨克自治州", "652424": u"伊犁哈萨克自治州", "652427": u"伊犁哈萨克自治州",
             "652426": u"伊犁哈萨克自治州", "652423": u"伊犁哈萨克自治州", "652422": u"伊犁哈萨克自治州", "152802": u"巴彦淖尔市",
             "652428": u"伊犁哈萨克自治州", "152801": u"巴彦淖尔市", "512529": u"宜宾市", "512528": u"宜宾市", "512520": u"宜宾市",
             "512523": u"宜宾市", "512525": u"宜宾市", "512527": u"宜宾市", "342637": u"合肥市", "452201": u"来宾市",
             "412882": u"驻马店市", "439004": u"岳阳市", "420619": u"随州市", "532273": u"曲靖市", "152634": u"乌兰察布市",
             "152630": u"乌兰察布市", "152633": u"包头市", "152639": u"巴彦淖尔市", "452445": u"贺州市", "513029": u"达州市",
             "513028": u"巴中市", "513027": u"巴中市", "513026": u"巴中市", "513025": u"巴中市", "513024": u"达州市", "513023": u"达州市",
             "513022": u"达州市", "513021": u"达州市", "142730": u"运城市", "142733": u"运城市", "222328": u"松原市", "222325": u"白城市",
             "222324": u"松原市", "222327": u"白城市", "222326": u"白城市", "222321": u"松原市", "222323": u"松原市", "222322": u"白城市",
             "432123": u"株洲市", "132135": u"邯郸市", "132130": u"邯郸市", "132132": u"邯郸市", "132133": u"邯郸市",
             "652133": u"吐鲁番市", "372301": u"滨州市", "513901": u"资阳市", "152824": u"巴彦淖尔市", "652402": u"伊犁哈萨克自治州",
             "152826": u"巴彦淖尔市", "152827": u"巴彦淖尔市", "654128": u"伊犁哈萨克自治州", "654122": u"伊犁哈萨克自治州",
             "654123": u"伊犁哈萨克自治州", "654126": u"伊犁哈萨克自治州", "654127": u"伊犁哈萨克自治州", "654124": u"伊犁哈萨克自治州",
             "654125": u"伊犁哈萨克自治州", "422403": u"荆州市", "422400": u"荆州市", "422401": u"仙桃市", "422406": u"荆门市",
             "422404": u"天门市", "512501": u"宜宾市", "342611": u"合肥市", "412530": u"洛阳市", "513825": u"眉山市", "412532": u"洛阳市",
             "513823": u"眉山市", "513821": u"眉山市", "612731": u"榆林市", "612730": u"榆林市", "612732": u"榆林市", "372932": u"菏泽市",
             "372930": u"菏泽市", "542229": u"山南市", "542227": u"山南市", "642125": u"银川市", "642124": u"中卫市", "642127": u"吴忠市",
             "642126": u"吴忠市", "642123": u"中卫市", "642122": u"吴忠市", "542223": u"山南市", "642129": u"吴忠市", "542221": u"山南市",
             "362429": u"吉安市", "362428": u"吉安市", "362425": u"吉安市", "362424": u"吉安市", "362427": u"吉安市", "362426": u"吉安市",
             "362421": u"吉安市", "362420": u"吉安市", "362423": u"吉安市", "362422": u"吉安市", "513229": u"阿坝州", "342301": u"滁州市",
             "513041": u"达州市", "432724": u"衡阳市", "132332": u"石家庄市", "132330": u"石家庄市", "132336": u"石家庄市",
             "132337": u"石家庄市", "132335": u"石家庄市", "222304": u"白城市", "222303": u"松原市", "222301": u"白城市",
             "352132": u"南平市", "460034": u"陵水黎族自治县", "440620": u"中山市", "442702": u"江门市", "372328": u"滨州市",
             "372325": u"滨州市", "372324": u"滨州市", "372323": u"滨州市", "372322": u"滨州市", "372321": u"滨州市", "422424": u"荆州市",
             "422425": u"荆州市", "422426": u"荆州市", "422427": u"仙桃市", "422421": u"荆州市", "422422": u"荆州市", "422423": u"荆州市",
             "422428": u"天门市", "422429": u"潜江市", "654101": u"伊犁哈萨克自治州", "452632": u"百色市", "452630": u"百色市",
             "452631": u"百色市", "142326": u"吕梁市", "142325": u"吕梁市", "142322": u"吕梁市", "612430": u"安康市", "642103": u"银川市",
             "642102": u"吴忠市", "642101": u"吴忠市", "532104": u"昭通市", "532101": u"昭通市", "452402": u"贺州市", "362402": u"吉安市",
             "362401": u"吉安市", "640321": u"中卫市", "142728": u"运城市", "142722": u"运城市", "142723": u"运城市", "142726": u"运城市",
             "142727": u"运城市", "142724": u"运城市", "142725": u"运城市", "379007": u"潍坊市", "379006": u"青岛市", "379005": u"泰安市",
             "379004": u"莱芜市", "379002": u"烟台市", "379009": u"烟台市", "379008": u"烟台市", "522272": u"铜仁市", "342802": u"安庆市",
             "412709": u"周口市", "412702": u"周口市", "412701": u"周口市", "422223": u"孝感市", "422226": u"孝感市", "422227": u"孝感市",
             "422224": u"随州市", "422225": u"孝感市", "452427": u"贺州市", "422228": u"孝感市", "422229": u"孝感市", "622241": u"张掖市",
             "512925": u"广安市", "512924": u"南充市", "512927": u"南充市", "512926": u"南充市", "512921": u"南充市", "512923": u"广安市",
             "512922": u"南充市", "512929": u"南充市", "512928": u"广安市", "510277": u"重庆市", "441230": u"云浮市", "342241": u"宿州市",
             "652201": u"哈密市", "460031": u"昌江黎族自治县", "460030": u"白沙黎族自治县", "460033": u"乐东黎族自治县", "460032": u"东方市",
             "460035": u"保亭黎族苗族自治县", "460036": u"琼中黎族苗族自治县", "612601": u"延安市", "532127": u"昭通市", "532126": u"昭通市",
             "532125": u"昭通市", "532124": u"昭通市", "532123": u"昭通市", "532122": u"昭通市", "532129": u"昭通市", "532128": u"昭通市",
             "412937": u"南阳市", "412936": u"南阳市", "412931": u"南阳市", "412930": u"南阳市", "412932": u"南阳市", "452428": u"贺州市",
             "452423": u"梧州市", "452421": u"梧州市", "622242": u"张掖市", "452426": u"贺州市", "452425": u"梧州市", "452424": u"贺州市",
             "142701": u"运城市", "142702": u"运城市", "142703": u"运城市", "142709": u"运城市", "342823": u"安庆市", "342822": u"安庆市",
             "342821": u"安庆市", "342827": u"安庆市", "342826": u"安庆市", "342825": u"安庆市", "342824": u"安庆市", "342829": u"池州市",
             "342828": u"安庆市", "412728": u"周口市", "412729": u"周口市", "412721": u"周口市", "412722": u"周口市", "412723": u"周口市",
             "412724": u"周口市", "412725": u"周口市", "412726": u"周口市", "412727": u"周口市", "422204": u"随州市", "422201": u"孝感市",
             "422202": u"孝感市", "422203": u"孝感市", "512903": u"南充市", "512902": u"广安市", "512901": u"南充市", "522423": u"毕节市",
             "510219": u"重庆市", "510218": u"重庆市", "522421": u"毕节市", "510211": u"重庆市", "510213": u"重庆市", "510212": u"重庆市",
             "510215": u"重庆市", "510214": u"重庆市", "510217": u"重庆市", "510216": u"重庆市", "440231": u"清远市", "342221": u"宿州市",
             "142132": u"大同市", "142130": u"大同市", "342225": u"宿州市", "342224": u"宿州市", "432513": u"娄底市", "219007": u"铁岭市",
             "219004": u"葫芦岛市", "533223": u"丽江市", "533222": u"丽江市", "533221": u"丽江市", "533224": u"丽江市",
             "652223": u"哈密市", "652222": u"哈密市", "652221": u"哈密市", "652227": u"哈密市", "640322": u"中卫市", "632139": u"海东市",
             "632131": u"海东市", "412919": u"南阳市", "412912": u"南阳市", "412911": u"南阳市", "513531": u"重庆市",
             "542330": u"日喀则市", "362334": u"上饶市", "362331": u"上饶市", "362330": u"上饶市", "362333": u"上饶市",
             "362332": u"景德镇市", "542337": u"日喀则市", "542336": u"日喀则市", "210704": u"葫芦岛市", "210705": u"葫芦岛市",
             "232635": u"黑河市", "612401": u"安康市", "612400": u"安康市", "433031": u"怀化市", "433030": u"怀化市", "513011": u"达州市",
             "522230": u"铜仁市", "452147": u"南宁市", "542429": u"那曲市", "542428": u"那曲市", "542421": u"那曲市", "542423": u"那曲市",
             "542422": u"那曲市", "542425": u"那曲市", "542427": u"那曲市", "542426": u"那曲市", "511121": u"眉山市", "511122": u"眉山市",
             "511127": u"眉山市", "511128": u"眉山市", "510232": u"重庆市", "510231": u"重庆市", "510230": u"重庆市", "342203": u"宿州市",
             "342201": u"宿州市", "229001": u"四平市", "229003": u"通化市", "229002": u"通化市", "229005": u"长春市", "229004": u"吉林市",
             "432530": u"娄底市", "132527": u"张家口市", "132526": u"张家口市", "132525": u"张家口市", "132524": u"张家口市",
             "132523": u"张家口市", "132522": u"张家口市", "132521": u"张家口市", "132529": u"张家口市", "469003": u"儋州市",
             "142229": u"忻州市", "652505": u"塔城地区", "652501": u"塔城地区", "452801": u"北海市", "452802": u"钦州市",
             "632113": u"海东市", "632112": u"海东市", "622201": u"张掖市", "210722": u"葫芦岛市", "210723": u"葫芦岛市",
             "632127": u"海东市", "632124": u"西宁市", "632125": u"西宁市", "452122": u"南宁市", "452123": u"南宁市", "452126": u"南宁市",
             "452127": u"南宁市", "522212": u"铜仁市", "452125": u"南宁市", "452128": u"崇左市", "452129": u"崇左市",
             "652172": u"吐鲁番市", "622251": u"张掖市", "512942": u"南充市", "362102": u"赣州市", "362103": u"赣州市",
             "362101": u"赣州市", "513701": u"巴中市", "440128": u"清远市", "222102": u"辽源市", "440124": u"惠州市", "440127": u"清远市",
             "440123": u"韶关市", "522126": u"遵义市", "452827": u"钦州市", "452826": u"钦州市", "452825": u"北海市", "452824": u"钦州市",
             "452823": u"钦州市", "452822": u"防城港市", "452821": u"防城港市", "522201": u"铜仁市", "142133": u"朔州市",
             "142131": u"朔州市", "342222": u"宿州市", "412954": u"南阳市", "422529": u"随州市", "422525": u"襄阳市", "622228": u"张掖市",
             "622224": u"张掖市", "622225": u"张掖市", "622226": u"张掖市", "622227": u"张掖市", "622222": u"张掖市", "622223": u"张掖市",
             "142234": u"忻州市", "142230": u"忻州市", "142231": u"忻州市", "142232": u"忻州市", "142233": u"忻州市", "341223": u"亳州市",
             "341224": u"亳州市", "341227": u"亳州市", "432617": u"邵阳市", "452101": u"崇左市", "332525": u"丽水市", "332524": u"丽水市",
             "332526": u"丽水市", "332521": u"丽水市", "332523": u"丽水市", "332522": u"丽水市", "332529": u"丽水市", "332528": u"丽水市",
             "341422": u"合肥市", "452324": u"桂林市", "513721": u"巴中市", "513722": u"巴中市", "513723": u"巴中市", "222123": u"四平市",
             "362124": u"赣州市", "362125": u"赣州市", "362126": u"赣州市", "362127": u"赣州市", "362122": u"赣州市", "362123": u"赣州市",
             "362128": u"赣州市", "362129": u"赣州市", "522530": u"安顺市", "452841": u"钦州市", "522401": u"毕节市", "442529": u"河源市",
             "442528": u"惠州市", "442527": u"东莞市", "442526": u"惠州市", "442525": u"河源市", "442524": u"河源市", "442523": u"河源市",
             "442522": u"河源市", "442521": u"惠州市", "513931": u"资阳市", "372267": u"潍坊市", "542230": u"林芝市", "542231": u"山南市",
             "542232": u"山南市", "542233": u"山南市", "372402": u"德州市", "372401": u"德州市", "342181": u"阜阳市", "432902": u"永州市",
             "432900": u"永州市", "432901": u"永州市", "432630": u"邵阳市", "432631": u"邵阳市", "342531": u"宣城市", "342530": u"宣城市",
             "232126": u"哈尔滨市", "232127": u"哈尔滨市", "232124": u"哈尔滨市", "232125": u"哈尔滨市", "232122": u"哈尔滨市",
             "232123": u"哈尔滨市", "232128": u"哈尔滨市", "232129": u"哈尔滨市", "512533": u"宜宾市", "332507": u"丽水市",
             "332502": u"丽水市", "332501": u"丽水市", "370633": u"威海市", "370632": u"威海市", "642222": u"固原市", "642223": u"固原市",
             "642221": u"固原市", "642226": u"固原市", "642224": u"固原市", "642225": u"固原市", "412855": u"驻马店市",
             "513122": u"雅安市", "513123": u"雅安市", "513126": u"雅安市", "513127": u"雅安市", "513124": u"雅安市", "513125": u"雅安市",
             "513128": u"雅安市", "422316": u"咸宁市", "522428": u"毕节市", "522427": u"毕节市", "412624": u"许昌市", "522425": u"毕节市",
             "522424": u"毕节市", "452311": u"桂林市", "522422": u"毕节市", "412623": u"许昌市", "522522": u"贵阳市", "522523": u"贵阳市",
             "522520": u"安顺市", "522521": u"安顺市", "522526": u"安顺市", "522527": u"安顺市", "522524": u"贵阳市", "522525": u"贵阳市",
             "522528": u"安顺市", "522529": u"安顺市", "372424": u"德州市", "372425": u"德州市", "372426": u"德州市", "372427": u"德州市",
             "372421": u"德州市", "372422": u"德州市", "372423": u"德州市", "372428": u"德州市", "372429": u"济南市",
             "542332": u"日喀则市", "542338": u"日喀则市", "133031": u"衡水市", "522426": u"毕节市", "132922": u"沧州市",
             "432928": u"永州市", "432929": u"永州市", "432924": u"永州市", "432925": u"永州市", "432926": u"永州市", "432927": u"永州市",
             "432432": u"常德市", "432922": u"永州市", "432923": u"永州市", "132934": u"沧州市", "132930": u"沧州市", "132931": u"沧州市",
             "132932": u"沧州市", "622621": u"陇南市", "622623": u"陇南市", "622624": u"陇南市", "622625": u"陇南市", "622626": u"陇南市",
             "622627": u"陇南市", "622628": u"陇南市", "622629": u"陇南市", "232100": u"哈尔滨市", "232101": u"哈尔滨市",
             "232102": u"哈尔滨市", "232103": u"哈尔滨市", "612630": u"延安市", "612631": u"延安市", "612632": u"延安市",
             "511215": u"重庆市", "413001": u"信阳市", "412876": u"驻马店市", "513101": u"雅安市", "622101": u"酒泉市",
             "622103": u"酒泉市", "622102": u"酒泉市", "132628": u"承德市", "612627": u"延安市", "342700": u"黄山市", "342701": u"黄山市",
             "412602": u"漯河市", "452331": u"桂林市", "452330": u"桂林市", "372223": u"潍坊市", "372227": u"潍坊市", "522507": u"安顺市",
             "522501": u"安顺市", "511027": u"资阳市", "511026": u"资阳市", "511023": u"资阳市", "511022": u"资阳市",
             "422921": u"神农架林区", "622826": u"庆阳市", "622827": u"庆阳市", "622824": u"庆阳市", "622825": u"庆阳市",
             "622822": u"庆阳市", "622823": u"庆阳市", "622821": u"庆阳市", "133029": u"衡水市", "133028": u"衡水市", "133025": u"衡水市",
             "133024": u"衡水市", "133027": u"衡水市", "133026": u"衡水市", "432416": u"常德市", "133022": u"衡水市", "452531": u"玉林市",
             "341281": u"亳州市", "442826": u"肇庆市", "442827": u"云浮市", "442824": u"肇庆市", "442825": u"肇庆市", "442822": u"肇庆市",
             "442823": u"肇庆市", "442821": u"肇庆市", "442828": u"云浮市", "442829": u"云浮市", "321021": u"泰州市", "321024": u"镇江市",
             "321025": u"泰州市", "321028": u"泰州市", "142432": u"晋中市", "142433": u"晋中市", "142430": u"晋中市", "142431": u"晋中市",
             "413024": u"信阳市", "413025": u"信阳市", "413026": u"信阳市", "413027": u"信阳市", "413021": u"信阳市", "413022": u"信阳市",
             "413023": u"信阳市", "413028": u"信阳市", "413029": u"信阳市", "452332": u"桂林市", "239004": u"佳木斯市",
             "239005": u"伊春市", "239006": u"鸡西市", "342932": u"池州市", "422130": u"黄冈市", "210622": u"鞍山市", "622123": u"酒泉市",
             "622122": u"酒泉市", "622120": u"酒泉市", "622127": u"酒泉市", "622126": u"酒泉市", "622125": u"酒泉市", "622124": u"酒泉市",
             "522502": u"贵阳市", "652421": u"伊犁哈萨克自治州", "142601": u"临汾市", "142603": u"临汾市", "142602": u"临汾市",
             "452761": u"河池市", "342728": u"池州市", "342721": u"宣城市", "342722": u"宣城市", "342723": u"黄山市", "342724": u"黄山市",
             "342725": u"黄山市", "342726": u"黄山市", "342727": u"黄山市", "440727": u"阳江市", "440726": u"阳江市", "133030": u"衡水市",
             "372807": u"临沂市", "372802": u"日照市", "372801": u"临沂市", "352215": u"宁德市", "622801": u"庆阳市", "362511": u"抚州市",
             "149001": u"太原市", "342128": u"阜阳市", "342129": u"阜阳市", "342126": u"阜阳市", "342127": u"阜阳市", "342124": u"阜阳市",
             "342125": u"阜阳市", "342122": u"阜阳市", "342123": u"阜阳市", "342121": u"阜阳市", "440520": u"潮州市", "412391": u"商丘市",
             "412392": u"商丘市", "133001": u"衡水市", "132202": u"邢台市", "132201": u"邢台市", "512522": u"宜宾市",
             "433129": u"张家界市", "230834": u"双鸭山市", "412836": u"驻马店市", "412831": u"驻马店市", "533522": u"临沧市",
             "533523": u"临沧市", "533524": u"临沧市", "533525": u"重庆市", "511296": u"重庆市", "533526": u"临沧市", "533527": u"临沧市",
             "533528": u"临沧市", "542424": u"那曲市", "542128": u"昌都市", "542129": u"昌都市", "542121": u"昌都市", "542122": u"昌都市",
             "542123": u"昌都市", "542124": u"昌都市", "542125": u"昌都市", "542126": u"昌都市", "542127": u"昌都市", "622321": u"武威市",
             "622323": u"武威市", "622322": u"武威市", "622326": u"武威市", "652557": u"塔城地区", "512231": u"重庆市",
             "532200": u"曲靖市", "532201": u"曲靖市", "152130": u"呼伦贝尔市", "152131": u"呼伦贝尔市", "142627": u"临汾市",
             "142626": u"临汾市", "142625": u"临汾市", "142624": u"临汾市", "142623": u"临汾市", "142622": u"临汾市", "142621": u"临汾市",
             "142629": u"临汾市", "142628": u"临汾市", "452702": u"河池市", "452700": u"河池市", "452701": u"河池市",
             "542331": u"日喀则市", "542333": u"日喀则市", "533035": u"保山市", "132439": u"保定市", "132438": u"保定市",
             "132430": u"保定市", "132433": u"保定市", "132432": u"保定市", "132435": u"保定市", "132434": u"保定市", "132437": u"保定市",
             "132436": u"保定市", "372821": u"临沂市", "372822": u"临沂市", "372823": u"临沂市", "372824": u"临沂市", "372826": u"日照市",
             "372827": u"临沂市", "372828": u"淄博市", "372829": u"临沂市", "542334": u"日喀则市", "612501": u"商洛市",
             "352236": u"宁德市", "432412": u"常德市", "352231": u"宁德市", "352230": u"宁德市", "420983": u"随州市", "133023": u"衡水市",
             "432417": u"常德市", "652502": u"塔城地区", "152301": u"通辽市", "152303": u"通辽市", "152302": u"通辽市",
             "342100": u"阜阳市", "342101": u"阜阳市", "342102": u"阜阳市", "342103": u"阜阳市", "513621": u"广安市", "513623": u"广安市",
             "513622": u"广安市", "513624": u"广安市", "232302": u"绥化市", "232303": u"绥化市", "232300": u"绥化市", "232301": u"绥化市",
             "232306": u"绥化市", "232304": u"绥化市", "232309": u"绥化市", "362532": u"抚州市", "362531": u"抚州市", "339002": u"嘉兴市",
             "339006": u"衢州市", "339005": u"杭州市", "432328": u"益阳市", "432326": u"益阳市", "432324": u"长沙市", "432325": u"益阳市",
             "432322": u"益阳市", "432323": u"益阳市", "432321": u"益阳市", "132228": u"邢台市", "132229": u"邢台市", "132224": u"邢台市",
             "132225": u"邢台市", "132226": u"邢台市", "132227": u"邢台市", "132223": u"邢台市", "320827": u"宿迁市", "320825": u"宿迁市",
             "320824": u"宿迁市", "320823": u"宿迁市", "320822": u"连云港市", "230823": u"哈尔滨市", "230825": u"双鸭山市",
             "230827": u"双鸭山市", "230829": u"鹤岗市", "362230": u"新余市", "362231": u"南昌市", "362232": u"宜春市",
             "362233": u"宜春市", "612330": u"汉中市", "622302": u"武威市", "622301": u"武威市", "362302": u"上饶市", "532223": u"曲靖市",
             "532224": u"曲靖市", "532225": u"曲靖市", "532226": u"曲靖市", "532227": u"曲靖市", "532229": u"昆明市",
             "152111": u"巴彦淖尔市", "452724": u"河池市", "452725": u"河池市", "452726": u"河池市", "452727": u"河池市",
             "452722": u"河池市", "452723": u"河池市", "452728": u"河池市", "452729": u"河池市", "522135": u"遵义市", "522131": u"遵义市",
             "522130": u"遵义市", "522132": u"遵义市", "533011": u"保山市", "612524": u"商洛市", "612525": u"商洛市", "612526": u"商洛市",
             "612527": u"商洛市", "612521": u"商洛市", "612522": u"商洛市", "612523": u"商洛市", "532426": u"玉溪市", "532427": u"玉溪市",
             "532424": u"玉溪市", "532425": u"玉溪市", "532422": u"玉溪市", "532423": u"玉溪市", "532421": u"玉溪市", "532428": u"玉溪市",
             "532429": u"玉溪市", "513601": u"广安市", "452555": u"玉林市", "440226": u"清远市", "440227": u"清远市", "440228": u"清远市",
             "232328": u"大庆市", "232329": u"大庆市", "232324": u"绥化市", "232325": u"绥化市", "232326": u"绥化市", "232320": u"绥化市",
             "232321": u"绥化市", "152327": u"通辽市", "152326": u"通辽市", "152325": u"通辽市", "152324": u"通辽市", "152323": u"通辽市",
             "152322": u"通辽市", "152321": u"通辽市", "152328": u"通辽市", "432301": u"益阳市", "432302": u"益阳市", "432303": u"益阳市",
             "321086": u"泰州市", "321085": u"泰州市", "321082": u"泰州市", "321083": u"泰州市", "142327": u"吕梁市", "142324": u"吕梁市",
             "142323": u"吕梁市", "142321": u"吕梁市", "142328": u"吕梁市", "142329": u"吕梁市", "232626": u"黑河市", "132440": u"保定市",
             "452230": u"来宾市", "452231": u"来宾市", "372528": u"聊城市", "372523": u"聊城市", "372522": u"聊城市", "372525": u"聊城市",
             "372524": u"聊城市", "372527": u"聊城市", "372526": u"聊城市", "422626": u"十堰市", "422624": u"十堰市", "422625": u"十堰市",
             "422622": u"十堰市", "422623": u"十堰市", "422621": u"十堰市", "432821": u"郴州市", "432823": u"郴州市", "432822": u"郴州市",
             "432825": u"郴州市", "432824": u"郴州市", "432827": u"郴州市", "432826": u"郴州市", "432829": u"郴州市", "432828": u"郴州市",
             "622725": u"平凉市", "622724": u"平凉市", "622727": u"平凉市", "622726": u"平凉市", "622721": u"平凉市", "622723": u"平凉市",
             "622722": u"平凉市", "132528": u"张家口市", "152631": u"乌兰察布市", "152632": u"乌兰察布市", "332622": u"台州市",
             "332623": u"台州市", "332621": u"台州市", "332626": u"台州市", "332627": u"台州市", "332624": u"台州市", "332625": u"台州市",
             "532401": u"玉溪市", "612102": u"渭南市", "612103": u"渭南市", "612101": u"渭南市", "432366": u"益阳市", "432367": u"益阳市",
             "512532": u"宜宾市", "512530": u"宜宾市", "512531": u"宜宾市", "512534": u"宜宾市", "512535": u"宜宾市", "142301": u"吕梁市",
             "142302": u"吕梁市", "142303": u"吕梁市", "142307": u"吕梁市", "412401": u"开封市", "132621": u"秦皇岛市",
             "132622": u"承德市", "132623": u"承德市", "132624": u"承德市", "132626": u"承德市", "132627": u"承德市", "132629": u"承德市",
             "372502": u"聊城市", "372501": u"聊城市", "372500": u"聊城市", "652601": u"阿勒泰地区", "422601": u"十堰市",
             "152626": u"乌兰察布市", "152627": u"乌兰察布市", "152624": u"乌兰察布市", "152625": u"乌兰察布市", "152622": u"呼和浩特市",
             "152623": u"呼和浩特市", "152621": u"呼和浩特市", "432803": u"郴州市", "432802": u"郴州市", "432801": u"郴州市",
             "152628": u"乌兰察布市", "152629": u"乌兰察布市", "452456": u"贺州市", "513030": u"达州市", "513031": u"广安市",
             "513032": u"达州市", "513036": u"达州市", "622701": u"平凉市", "332601": u"台州市", "332602": u"台州市", "332603": u"台州市",
             "132101": u"邯郸市", "511081": u"资阳市", "532721": u"普洱市", "532723": u"普洱市", "532722": u"普洱市", "532725": u"普洱市",
             "532724": u"普洱市", "532727": u"普洱市", "532726": u"普洱市", "532729": u"普洱市", "532728": u"普洱市", "342622": u"合肥市",
             "612122": u"西安市", "612123": u"西安市", "612124": u"渭南市", "612125": u"渭南市", "612126": u"渭南市", "612127": u"渭南市",
             "612128": u"渭南市", "612129": u"渭南市", "441283": u"云浮市", "441282": u"云浮市", "441281": u"云浮市", "412527": u"洛阳市",
             "320881": u"宿迁市", "132828": u"廊坊市", "132829": u"廊坊市", "132826": u"廊坊市", "132827": u"廊坊市", "132825": u"廊坊市",
             "132822": u"廊坊市", "132823": u"廊坊市", "132821": u"廊坊市", "342628": u"合肥市", "342625": u"合肥市", "342627": u"合肥市",
             "412424": u"开封市", "342623": u"合肥市", "612726": u"榆林市", "612727": u"榆林市", "612724": u"榆林市", "612725": u"榆林市",
             "612722": u"榆林市", "612723": u"榆林市", "612721": u"榆林市", "612728": u"榆林市", "612729": u"榆林市", }