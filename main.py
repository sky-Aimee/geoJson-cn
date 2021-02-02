# -*- coding: UTF-8 -*-

import json
import urllib.request
import urllib.parse
import ssl
import os


def write_json_to_file(item, text, level):
    if not os.path.isdir(level):
        os.mkdir(level)
    with open(level + "/" + item + ".json", "w", encoding='utf-8') as json_file:
        json.dump(text, json_file, ensure_ascii=False)


def write_full_jso_to_file(item, text, level):
    with open(level + "_full/" + item + ".json", "w", encoding='utf-8') as json_file:
        json.dump(text, json_file, ensure_ascii=False)


if not os.path.isdir("country_full"):
    os.mkdir("country_full")
if not os.path.isdir("country"):
    os.mkdir("country")

if not os.path.isdir("province_full"):
    os.mkdir("province_full")
if not os.path.isdir("province"):
    os.mkdir("province")

if not os.path.isdir("city_full"):
    os.mkdir("city_full")
if not os.path.isdir("city"):
    os.mkdir("city")

if not os.path.isdir("district"):
    os.mkdir("district")

context = ssl._create_unverified_context()
url = "https://geo.datav.aliyun.com/areas_v2/bound/infos.json"
with urllib.request.urlopen(url, context=context) as response:
    html = json.loads(response.read().decode("UTF-8"))
    with open("location.json", "w", encoding='utf-8') as json_file:
        json.dump(html, json_file, ensure_ascii=False)

    for item in list(html.keys()):
        level = html[item]['level']
        try:
            with urllib.request.urlopen(
                    "https://geo.datav.aliyun.com/areas_v2/bound/" + item + ".json",
                    context=context,
            ) as res:
                text = json.loads(res.read().decode("UTF-8"))
                write_json_to_file(item, text, level)
        except Exception as e:
            print(item, '报错', e)

        try:
            if level != "district":
                with urllib.request.urlopen(
                        "https://geo.datav.aliyun.com/areas_v2/bound/" + item + "_full.json",
                        context=context,
                ) as res:
                    text = json.loads(res.read().decode("UTF-8"))
                    write_full_jso_to_file(item, text, level)
        except Exception as e:
            print(item, '报错', e)
    print("写入完成")
