#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从各省份简称中返回全称

def get_full_province_name(name):
    name_kv = {
        '皖': '安徽', '京': '北京', '渝': '重庆',
        '闽': '福建', '甘': '甘肃', '粤': '广东',
        '桂': '广西', '黔': '贵州', '琼': '海南',
        '冀': '河北', '豫': '河南', '黑': '黑龙江',
        '鄂': '湖北', '湘': '湖南', '吉': '吉林',
        '苏': '江苏', '赣': '江西', '辽': '辽宁',
        '蒙': '内蒙古', '宁': '宁夏', '青': '青海',
        '鲁': '山东', '晋': '山西', '陕': '陕西',
        '沪': '上海', '川': '四川', '津': '天津',
        '藏': '西藏', '新': '新疆', '滇': '云南',
        '浙': '浙江', '港': '香港', '澳': '澳门',
        '台': '台湾'
    }
    if name in name_kv.keys():
        return name_kv[name]
    else:
        return name
