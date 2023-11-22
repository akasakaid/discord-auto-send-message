import time
import requests


headers = {

}

def sendMessage(text):
    data = {"mobile_network_type":"unknown","content":text,"nonce":str(int(time.time())),"tts":False,"flags":0}
    headers['Content-Length'] = str(len(str(data)))
    urlMessage = ""
    res = requests.post(urlMessage,json=data,headers=headers)
    if res.text.find("id") >= 0:
        print("[+] pesan berhasil dikirim",text)
    else:
        print("[x] pesan gagal dikirim",text)

def countdown(detik):
    while detik:
        print(f"[!] tunggu sampai {detik} detik ",flush=True,end="\r")
        detik -= 1
        time.sleep(1)
    print("                              ",flush=True,end="\r")

def main():
    msg = "-work"
    while True:
        sendMessage(msg)
        countdown(60 * 60) # 3600

try:
    main()
except KeyboardInterrupt:
    exit()