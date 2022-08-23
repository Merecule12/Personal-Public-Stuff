# Coded by Nvidia and Merecule! Not the corporation itself, but the user. Merecule had the idea!

from random import random
import threading, re, time
import requests, random
import time
import json

threadc = 5

itemid = 1

startUserId = 1
endUserId = 2

s = requests.session()
proxy = set()

with open("./proxies.txt", "r") as f:
    file_lines1 = f.readlines()
    for line1 in file_lines1:
        proxy.add(line1.strip())
        
proxies = {
    'http': 'https://'+random.choice(list(proxy))
}

def thread():
    while True:
        try:
            for i in range(startUserId, endUserId):

                r = requests.get(f'https://inventory.roproxy.com/v1/users/{i}/items/Asset/{itemid}/is-owned',proxies=proxies)
                rtext = r.text

                print(i)
                print(r.text)

                if rtext == 'true':
                    with open('id.txt', 'a') as f:
                        f.writelines(f"User ID: {i}\n")
                        if i == startUserId:
                            f.write(f"User ID: {i}\n")
                if rtext == '{"errors":[{"code":0,"message":"TooManyRequests"}]}':
                    time.sleep(75)
                if i == endUserId:
                    print("Finished!")
                    f.close()
        except Exception as e:
            print("Error ->", e)

for i in range(threadc):
    threading.Thread(target=thread).start()
    time.sleep(1.5)