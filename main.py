# -*- coding: utf-8 -*-
# Author: Jack Wu & Ason
# Date: 8/9/2017_
import datetime
import time
import os

import pyperclip
from wox import Wox,WoxAPI

class Translate(Wox):
    def query(self, query):
        data = []
        result = []
        formats = ["%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S", "%Y-%m-%d-%H-%M-%S", "%Y-%m-%d %H：%M：%S"]
        if not query:
            return ""
        elif query == "now":
            date = str(int(time.time()))
            data.append(date)
            for i in formats:
                try:
                    timestamp=data.append(datetime.datetime.now().strftime(i))
                except Exception:
                    continue
                else:
                    if timestamp:
                        data.append(timestamp)

        elif len(query) > 10:#非时间戳
            for i in formats:
                try:
                    timestamp = str(int(time.mktime(time.strptime(query, i))))
                except Exception:
                    continue
                else:
                    if timestamp :
                        data = timestamp
                        break

        elif len(query) == 10:#时间戳，需要转化为正常时间
            timeArray = time.localtime(int(query))
            for i in formats:
                try:
                    date = str(time.strftime(i, timeArray))
                except Exception:
                    continue
                else:
                    if date:
                        data.append(date)


        if (isinstance(data, str)):
            result = [{
                "Title": data,
                "SubTitle": '时间戳转换-按下回车复制到粘贴版 ',
                "IcoPath": "Images/timestamp.png",
                "JsonRPCAction": {
                    "method": "copy",
                    "parameters": [data],
                    "dontHideAfterAction": True
                }
            }]
        else:
            for d in data:
                result.append({
                    "Title": d,
                    "SubTitle": '时间戳转换-按下回车复制到粘贴版 ',
                    "IcoPath": "Images/timestamp.png",
                    "JsonRPCAction": {
                        "method": "copy",
                        "parameters": [d],
                        "dontHideAfterAction": True
                    }
                })
        return result

    def copy(self, data):
        # command = 'set /p="' + data + '"<nul echo ' + data + '| clip'
        # os.system(command)
        pyperclip.copy(data)

if __name__ == "__main__":
    Translate()