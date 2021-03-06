# -*- coding: utf-8 -*-
# =========================== GDP等级 ===========================

gdpDic = {u"北京市": u"一线城市", u"广州市": u"一线城市", u"上海市": u"一线城市", u"深圳市": u"一线城市", u"成都市": u"新一线城市", u"大连市": u"新一线城市",
          u"东莞市": u"新一线城市", u"杭州市": u"新一线城市", u"南京市": u"新一线城市", u"宁波市": u"新一线城市", u"青岛市": u"新一线城市", u"沈阳市": u"新一线城市",
          u"苏州市": u"新一线城市", u"天津市": u"新一线城市", u"武汉市": u"新一线城市", u"西安市": u"新一线城市", u"长沙市": u"新一线城市", u"郑州市": u"新一线城市",
          u"重庆市": u"新一线城市", u"常州市": u"二线城市", u"佛山市": u"二线城市", u"福州市": u"二线城市", u"贵阳市": u"二线城市", u"哈尔滨市": u"二线城市",
          u"海口市": u"二线城市", u"合肥市": u"二线城市", u"惠州市": u"二线城市", u"济南市": u"二线城市", u"嘉兴市": u"二线城市", u"金华市": u"二线城市",
          u"昆明市": u"二线城市", u"兰州市": u"二线城市", u"南昌市": u"二线城市", u"南宁市": u"二线城市", u"南通市": u"二线城市", u"泉州市": u"二线城市",
          u"厦门市": u"二线城市", u"绍兴市": u"二线城市", u"石家庄市": u"二线城市", u"台州市": u"二线城市", u"太原市": u"二线城市", u"温州市": u"二线城市",
          u"乌鲁木齐市": u"二线城市", u"无锡市": u"二线城市", u"徐州市": u"二线城市", u"烟台市": u"二线城市", u"长春市": u"二线城市", u"中山市": u"二线城市",
          u"珠海市": u"二线城市", u"鞍山市": u"三线城市", u"蚌埠市": u"三线城市", u"包头市": u"三线城市", u"保定市": u"三线城市", u"大庆市": u"三线城市",
          u"丹东市": u"三线城市", u"东营市": u"三线城市", u"抚顺市": u"三线城市", u"赣州市": u"三线城市", u"桂林市": u"三线城市", u"邯郸市": u"三线城市",
          u"衡阳市": u"三线城市", u"呼和浩特市": u"三线城市", u"湖州市": u"三线城市", u"淮安市": u"三线城市", u"吉林市": u"三线城市", u"济宁市": u"三线城市",
          u"江门市": u"三线城市", u"揭阳市": u"三线城市", u"荆州市": u"三线城市", u"九江市": u"三线城市", u"廊坊市": u"三线城市", u"丽江市": u"三线城市",
          u"丽水市": u"三线城市", u"连云港市": u"三线城市", u"临沂市": u"三线城市", u"柳州市": u"三线城市", u"龙岩市": u"三线城市", u"洛阳市": u"三线城市",
          u"马鞍山市": u"三线城市", u"绵阳市": u"三线城市", u"南充市": u"三线城市", u"南平市": u"三线城市", u"南阳市": u"三线城市", u"宁德市": u"三线城市",
          u"盘锦市": u"三线城市", u"莆田市": u"三线城市", u"齐齐哈尔市": u"三线城市", u"秦皇岛市": u"三线城市", u"清远市": u"三线城市", u"衢州市": u"三线城市",
          u"三明市": u"三线城市", u"汕头市": u"三线城市", u"上饶市": u"三线城市", u"泰安市": u"三线城市", u"泰州市": u"三线城市", u"唐山市": u"三线城市",
          u"威海市": u"三线城市", u"潍坊市": u"三线城市", u"芜湖市": u"三线城市", u"西宁市": u"三线城市", u"咸阳市": u"三线城市", u"襄阳市": u"三线城市",
          u"孝感市": u"三线城市", u"延边朝鲜族自治州": u"三线城市", u"盐城市": u"三线城市", u"扬州市": u"三线城市", u"宜昌市": u"三线城市", u"银川市": u"三线城市",
          u"营口市": u"三线城市", u"岳阳市": u"三线城市", u"湛江市": u"三线城市", u"漳州市": u"三线城市", u"肇庆市": u"三线城市", u"镇江市": u"三线城市",
          u"舟山市": u"三线城市", u"株洲市": u"三线城市", u"淄博市": u"三线城市", u"安庆市": u"四线城市", u"安阳市": u"四线城市", u"宝鸡市": u"四线城市",
          u"北海市": u"四线城市", u"本溪市": u"四线城市", u"滨州市": u"四线城市", u"常德市": u"四线城市", u"潮州市": u"四线城市", u"郴州市": u"四线城市",
          u"承德市": u"四线城市", u"赤峰市": u"四线城市", u"滁州市": u"四线城市", u"大同市": u"四线城市", u"德阳市": u"四线城市", u"德州市": u"四线城市",
          u"鄂尔多斯市": u"四线城市", u"恩施土家族苗族自治州": u"四线城市", u"抚州市": u"四线城市", u"阜新市": u"四线城市", u"阜阳市": u"四线城市", u"河源市": u"四线城市",
          u"菏泽市": u"四线城市", u"红河哈尼族彝族自治州": u"四线城市", u"呼伦贝尔市": u"四线城市", u"葫芦岛市": u"四线城市", u"怀化市": u"四线城市",
          u"淮南市": u"四线城市", u"黄冈市": u"四线城市", u"黄山市": u"四线城市", u"黄石市": u"四线城市", u"吉安市": u"四线城市", u"佳木斯市": u"四线城市",
          u"焦作市": u"四线城市", u"锦州市": u"四线城市", u"晋中市": u"四线城市", u"景德镇市": u"四线城市", u"开封市": u"四线城市", u"乐山市": u"四线城市",
          u"辽阳市": u"四线城市", u"聊城市": u"四线城市", u"临汾市": u"四线城市", u"六安市": u"四线城市", u"娄底市": u"四线城市", u"泸州市": u"四线城市",
          u"茂名市": u"四线城市", u"眉山市": u"四线城市", u"梅州市": u"四线城市", u"牡丹江市": u"四线城市", u"内江市": u"四线城市", u"平顶山市": u"四线城市",
          u"黔南布依族苗族自治州": u"四线城市", u"曲靖市": u"四线城市", u"日照市": u"四线城市", u"汕尾市": u"四线城市", u"商丘市": u"四线城市", u"韶关市": u"四线城市",
          u"邵阳市": u"四线城市", u"十堰市": u"四线城市", u"四平市": u"四线城市", u"遂宁市": u"四线城市", u"铁岭市": u"四线城市", u"通化市": u"四线城市",
          u"通辽市": u"四线城市", u"渭南市": u"四线城市", u"梧州市": u"四线城市", u"西双版纳傣族自治州": u"四线城市", u"咸宁市": u"四线城市", u"湘潭市": u"四线城市",
          u"新乡市": u"四线城市", u"信阳市": u"四线城市", u"邢台市": u"四线城市", u"宿迁市": u"四线城市", u"宿州市": u"四线城市", u"许昌市": u"四线城市",
          u"宣城市": u"四线城市", u"雅安市": u"四线城市", u"阳江市": u"四线城市", u"宜宾市": u"四线城市", u"宜春市": u"四线城市", u"榆林市": u"四线城市",
          u"玉林市": u"四线城市", u"玉溪市": u"四线城市", u"运城市": u"四线城市", u"枣庄市": u"四线城市", u"张家口市": u"四线城市", u"周口市": u"四线城市",
          u"驻马店市": u"四线城市", u"遵义市": u"四线城市", u"阿坝藏族羌族自治州": u"五线城市", u"阿克苏地区": u"五线城市", u"阿拉尔市": u"五线城市",
          u"阿拉善盟": u"五线城市", u"阿勒泰地区": u"五线城市", u"阿里地区": u"五线城市", u"安康市": u"五线城市", u"安顺市": u"五线城市", u"巴彦淖尔市": u"五线城市",
          u"巴音郭楞蒙古自治州": u"五线城市", u"巴中市": u"五线城市", u"白城市": u"五线城市", u"白沙黎族自治县": u"五线城市", u"白山市": u"五线城市",
          u"白银市": u"五线城市", u"百色市": u"五线城市", u"保山市": u"五线城市", u"保亭黎族苗族自治县": u"五线城市", u"北屯市": u"五线城市", u"毕节市": u"五线城市",
          u"亳州市": u"五线城市", u"博尔塔拉蒙古自治州": u"五线城市", u"沧州市": u"五线城市", u"昌都市": u"五线城市", u"昌吉回族自治州": u"五线城市",
          u"昌江黎族自治县": u"五线城市", u"朝阳市": u"五线城市", u"澄迈县": u"五线城市", u"池州市": u"五线城市", u"崇左市": u"五线城市", u"楚雄彝族自治州": u"五线城市",
          u"达州市": u"五线城市", u"大理白族自治州": u"五线城市", u"大兴安岭地区": u"五线城市", u"儋州市": u"五线城市", u"德宏傣族景颇族自治州": u"五线城市",
          u"迪庆藏族自治州": u"五线城市", u"定安县": u"五线城市", u"定西市": u"五线城市", u"东方市": u"五线城市", u"鄂州市": u"五线城市", u"防城港市": u"五线城市",
          u"甘南藏族自治州": u"五线城市", u"甘孜藏族自治州": u"五线城市", u"固原市": u"五线城市", u"广安市": u"五线城市", u"广元市": u"五线城市", u"贵港市": u"五线城市",
          u"果洛藏族自治州": u"五线城市", u"哈密市": u"五线城市", u"海北藏族自治州": u"五线城市", u"海东市": u"五线城市", u"海南藏族自治州": u"五线城市",
          u"海西蒙古族藏族自治州": u"五线城市", u"汉中市": u"五线城市", u"和田地区": u"五线城市", u"河池市": u"五线城市", u"贺州市": u"五线城市", u"鹤壁市": u"五线城市",
          u"鹤岗市": u"五线城市", u"黑河市": u"五线城市", u"衡水市": u"五线城市", u"淮北市": u"五线城市", u"黄南藏族自治州": u"五线城市", u"鸡西市": u"五线城市",
          u"济源市": u"五线城市", u"嘉峪关市": u"五线城市", u"金昌市": u"五线城市", u"晋城市": u"五线城市", u"荆门市": u"五线城市", u"酒泉市": u"五线城市",
          u"喀什地区": u"五线城市", u"克拉玛依市": u"五线城市", u"克孜勒苏柯尔克孜自治州": u"五线城市", u"拉萨市": u"五线城市", u"来宾市": u"五线城市",
          u"莱芜市": u"五线城市", u"乐东黎族自治县": u"五线城市", u"凉山彝族自治州": u"五线城市", u"辽源市": u"五线城市", u"林芝市": u"五线城市", u"临沧市": u"五线城市",
          u"临高县": u"五线城市", u"临夏回族自治州": u"五线城市", u"陵水黎族自治县": u"五线城市", u"六盘水市": u"五线城市", u"陇南市": u"五线城市", u"漯河市": u"五线城市",
          u"吕梁市": u"五线城市", u"那曲市": u"五线城市", u"怒江傈僳族自治州": u"五线城市", u"攀枝花市": u"五线城市", u"平凉市": u"五线城市", u"萍乡市": u"五线城市",
          u"濮阳市": u"五线城市", u"普洱市": u"五线城市", u"七台河市": u"五线城市", u"潜江市": u"五线城市", u"黔东南苗族侗族自治州": u"五线城市",
          u"黔西南布依族苗族自治州": u"五线城市", u"钦州市": u"五线城市", u"庆阳市": u"五线城市", u"琼海市": u"五线城市", u"琼中黎族苗族自治县": u"五线城市",
          u"日喀则市": u"五线城市", u"三门峡市": u"五线城市", u"三沙市": u"五线城市", u"三亚市": u"五线城市", u"山南市": u"五线城市", u"商洛市": u"五线城市",
          u"神农架林区": u"五线城市", u"石河子市": u"五线城市", u"石嘴山市": u"五线城市", u"双河市": u"五线城市", u"双鸭山市": u"五线城市", u"朔州市": u"五线城市",
          u"松原市": u"五线城市", u"绥化市": u"五线城市", u"随州市": u"五线城市", u"塔城地区": u"五线城市", u"天门市": u"五线城市", u"天水市": u"五线城市",
          u"铁门关市": u"五线城市", u"铜川市": u"五线城市", u"铜陵市": u"五线城市", u"铜仁市": u"五线城市", u"图木舒克市": u"五线城市", u"吐鲁番市": u"五线城市",
          u"屯昌县": u"五线城市", u"万宁市": u"五线城市", u"文昌市": u"五线城市", u"文山壮族苗族自治州": u"五线城市", u"乌海市": u"五线城市", u"乌兰察布市": u"五线城市",
          u"吴忠市": u"五线城市", u"五家渠市": u"五线城市", u"五指山市": u"五线城市", u"武威市": u"五线城市", u"锡林郭勒盟": u"五线城市", u"仙桃市": u"五线城市",
          u"湘西土家族苗族自治州": u"五线城市", u"忻州市": u"五线城市", u"新余市": u"五线城市", u"兴安盟": u"五线城市", u"延安市": u"五线城市", u"阳泉市": u"五线城市",
          u"伊春市": u"五线城市", u"伊犁哈萨克自治州": u"五线城市", u"益阳市": u"五线城市", u"鹰潭市": u"五线城市", u"永州市": u"五线城市", u"玉树藏族自治州": u"五线城市",
          u"云浮市": u"五线城市", u"张家界市": u"五线城市", u"张掖市": u"五线城市", u"长治市": u"五线城市", u"昭通市": u"五线城市", u"中卫市": u"五线城市",
          u"资阳市": u"五线城市", u"自贡市": u"五线城市"}
