import datetime
import time
formats = ["%Y-%m-%d-%H-%M-%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H：%M：%S"]
data = []
date = str(int(time.time()))
for i in formats:
    try:
        data.append(datetime.datetime.now().strftime(i))
    except Exception:
        continue
    else:
        data.append(date)