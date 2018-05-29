import os
import datx
##import requests
import datetime
import time

test_list = [
    "cbsw-test.fs.ap1.oraclecloud.com",
    "cbsw.fs.ap1.oraclecloud.com",
]


def get_city(addr):
    aa = os.popen(f"ping {addr}").readlines()
    for a in aa:
        print(a)
    ip = ""

    if "来自" in (aa[2][:2], aa[3][:2], aa[4][:2], aa[5][:2]):
        ip = aa[7][:13]

        cc = datx.City("ipdb.datx")  # 在数据库查（更稳定）
        try:
            res = cc.find(ip)
        except ValueError as VE:
            print(VE)
            res = ["未知", "未知", "", ""]
        ##        url = f"http://freeapi.ipip.net/{ip}"  # 在接口查，需要sleep
        ##        res = requests.get(url).text

        if "香港" in res:
            print("获得香港ip：", addr, ip)
            print()
            dd = os.popen(f"nslookup -qt=A cbsw-test.fs.ap1.oraclecloud.com {ip}")
            for d in dd:
                print(d)

        else:
            print("以上ip来自：", "-".join(res), ip, addr)

    with open("address_get.txt", "a") as ww:
        ww.write(f"{res[1]}\t")
        ww.write(f"{addr}\t")
        ww.write(f"{ip}\t")
        ww.write(f"{str(datetime.datetime.now())}\n")


while 1:
    for i in os.popen("ipconfig/flushdns").readlines():
        print(i)

    for t in test_list:
        get_city(t)

    ee = os.popen(f"nslookup -qt=A cbsw.fs.ap1.oraclecloud.com").readlines()
    print("-" * 60)
    print("\nnslookup -qt=A cbsw.fs.ap1.oraclecloud.com")
    for i in ee:
        print(i)
    time.sleep(60 * 20)
