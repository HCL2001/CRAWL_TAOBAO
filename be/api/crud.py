import urllib.parse
from datetime import datetime
import random
import time
import re
import json
import aiohttp
import requests
from bs4 import BeautifulSoup
from sqlalchemy import desc
from sqlalchemy.orm import Session

import config
import models
import schemas


async def crawl_taobao(keyWord: str):
    product_list = []
    cookie_parameters = {
        'JSESSIONID': 'A3F2A600D89A337421C303832ED25962',
        'alitrackid': 'world.taobao.com',
        'lastalitrackid': 'world.taobao.com',
        'isg': 'BC8v81Y-l2QRlpMlcbENsWFcvkM51IP2ll2ewEG8yx6lkE-SSaQTRi1BFpiu6Ftu',
        'tfstk': 'dLbMHJ2S6G-_6Yf0nVL_WuKAbMEp5ATXft3vHEp4YpJIWnJYftxcH9tVWFCOKKWRnIQOkZjIo_1fW5TY1F16lEy8ezBc11TXNVe8yAfw5f84e8U-vX-_BE7YaZkAU5GSIMGPW5xkEjV_pPwrMHvP_dWAHwJneL5wKqu2ICXaBDoyqqgXTSQEcmtwOBvJwZGT-',
        '_uetvid': 'dc870040ea5911ed8305a55f0f12c1b7',
        'cookie17': 'UUpgQEvyiTEr4C708g%3D%3D',
        '_ga_YFVFB9JLVB': 'GS1.1.1690442168.15.1.1690445459.0.0.0',
        'isg': 'BPv7j7ggG8DR6CflrlfL6pzEit9lUA9SghHKLO24w_oRTBsudSJQotaOYvQC7GdK',
        '_tb_token_': '3e3868656177',
        '_ga': 'GA1.1.1534418803.1689924886',
        '_uetsid': '5f099c3029d611ee8c3217cd68bb6b41',
        'l': 'fBIQOzNINiq0KVKsBOfZPurza7797IRAguPzaNbMi9fPOB5p5lvVW1O2bET9CnMNFs_MR38PiVPBBeYBqIv4n5U62j-latkmnmOk-Wf..',
        '_samesite_flag_': 'sssssssssssssssssss',
        'uc3': 'vt3=F8dCsGChughbL6o4QIw%3D&id2=UUpgQEvyiTEr4C708g%3D%3D&nk2=F5RDLjqWCLCCNe6Q0ac%3D&lg2=VT5L2FSpMGV7TQ%3D%3D',
        '_nk_': 'tb627551502528',
        '_cc_': 'VFC%2FuZ9ajQ%3D%3D',
        'tracknick': 'tb627551502528',
        'csg': 'eb0ab3d9',
        'existShop': 'MTY5MDQ0MzYyNQ%3D%3D',
        'skt': '0b8c3b7ac48f8278',
        'cookie1': 'AimSwy6Hu0cjkXBiNAEvUR5yUCjEb50QirZe9OQR8JM%3D',
        'dnk': 'tb627551502528',
        'cancelledSubSites': 'empty',
        'uc1': 'existShop=false&pas=0&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=VT5L2FSpdiBh&cookie14=Uoe9bflJcYfchg%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D',
        'unb': '2216209135380',
        'tbsa': '1ff46cdd849b0540a0e8d98a_1690445950_36',
        'thw': 'cn',
        'cna': 'v2HaHKidsAcCAQ6hEtJmGx5y',
        '_m_h5_tk_enc': '10703d311e9d054fbfdbfaca52d84fb1',
        '_m_h5_tk': '30ad0693ddd4c45a3bfbc3b6f628c9bf_1690452610419',
        'hng': 'VN%7Czh-CN%7CVNM%7C704',
        '_ga_JBTWV3NHSY': 'GS1.1.1690442168.15.1.1690445459.51.0.0',
        'sgcookie': 'E100KEWfBiTccF1aMmqLD7jiJ%2FRsFEDSRl658T1FF%2BoHAe2Celm%2FuAvxWb3umYcD13IJVPAmRjyYqTrK10o52Dbi%2BCJFP8GNkq8b9RLV3MpwZY0%3D',
        'sca': '98c4abf4',
        'OVS_HIGH_VALUE_INVITATION_CODE': 'WDPNQP',
        '_fbp': 'fb.1.1690192635997.267978015',
        't': '2ce80f22b49a2767d846dd2bc50b2942',
        '_gcl_au': '1.1.1475640338.1690192636',
        'xlly_s': '1',
        'atpsida': 'bf784225a9ab65bdcfd4e6ea_1690445950_30',
        'uc4': 'id4=0%40U2gqz6QY%2B2LU45CVgCnTHhyjgPQ5L46G&nk4=0%40FY4I7WSY2SzxeSCD9wJSplBYHJ0a6CrQJg%3D%3D',
        'cookie2': '1246ef28b2614d40a0ce34c00ec9cdef',
        'sg': '807',
        'lgc': 'tb627551502528',
        'mt': 'ci=0_0',
        'aui': '2216209135380',
        '_gid': 'GA1.2.1903367849.1690171119',
        'cnaui': '2216209135380',
        'cna': 'v2HaHKidsAcCAQ6hEtJmGx5y',
        'xlly_s': '1',
        'cna': 'v2HaHKidsAcCAQ6hEtJmGx5y'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    url = f"https://s.taobao.com/search?q={urllib.parse.quote(keyWord)}"
    counter = 1
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, cookies=cookie_parameters) as resp:
            content = await resp.text()
            soup = BeautifulSoup(content, "html.parser")
            script_tags = soup.find_all("script")
        for script_tag in script_tags:
            script_content = script_tag.string
            if script_content and "g_page_config" in script_content:
                start_index = script_content.find("g_page_config =")
                end_index = script_content.find("}};")
                json_content = script_content[start_index + 15 : end_index +2]
                try:
                    g_page_config_json = json.loads(json_content)
                    data = g_page_config_json['mods']['itemlist']['data']['auctions']
                    print(len(data))
                    for item in data:
                        objectDto = {
                            'id': counter,
                            'name': item['raw_title'],
                            'link': item['detail_url'],
                            'price': item['view_price'],
                            'shopName': item['shopName'],
                            # 'crawl_time': object.crawl_time
                        }
                        counter +=1
                        product_list.append(objectDto)
                except json.JSONDecodeError as e:
                    print(e)
    return product_list