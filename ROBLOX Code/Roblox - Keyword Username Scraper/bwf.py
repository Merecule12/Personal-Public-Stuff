import threading, re, time
import requests

userId = 1
output_file = open("usernames.txt", "a", encoding="UTF-8")
amount = 50
threadc = 25
keywords = ["penis", "dildo", "asshole", "bitch", "fuck", "nigg", "vagina", "slut", "shit", "fag", "kcuf", "pussy", "fuk", "hitler", "blowjob", "fuc", "sex", "69", "88", "18", "fap", "azzhole", "aszhole", "kkk", "toggaf", "horny", "pedo", "cum"]

def api(params):
    req = requests.get(url="https://www.roblox.com/avatar-thumbnails?params="+params, allow_redirects=False)
    if req.status_code == 200:
        return req.text
    return ""

def thread():
    global userId
    while True:
        try:
            params = "["
            for i in range(userId+1, userId+amount+1):
                params += "{userId:"+str(i)+"},"
            userId += amount
            params = params[:-1]+"]"
            resp = api(params)
            users = re.findall(r"\"id\":(\d+?),\"name\":\"(.+?)\",", resp)
            for user in users:
                    for k in keywords:
                        uId, uName = user
                        if k.lower() in uName.lower():
                            print(k)
                            print(uId, uName)
                            output_file.write(uId+":"+uName+"\n")
            output_file.flush()
        except Exception as e:
            print("Error ->", e)

for i in range(threadc):
    threading.Thread(target=thread).start()
    time.sleep(0.01)