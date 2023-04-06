#____________________________ [ && ]
from time import sleep as slp
from subprocess import *
from threading import *
import requests as rq
import socket
import os
#____________________________ [ && ]
dir = os.path.dirname(os.path.abspath(__file__))
banner = dir + "/files/banner/b.txt"
with open(banner,"r") as line:
    for i in line:
        print(i,end="")
        slp(0.5)
#____________________________ [ && ]
lt = False
while not lt:
    os.chdir(dir)
    cmd = input("\033[1;4;37m\x54\x6f\x6f\x6c\x73\033[0m > ")
    if cmd == "exit":
        print("Logout")
        slp(0.5)
        lt = True
    elif cmd == "ip":
        print("\033[1;34m[*]\033[0m\texec: %s\n"%(cmd))
        slp(0.5)
        ip_int = socket.gethostbyname(socket.gethostname())
        print("\033[1;34m[*]\033[0m\tIp Interno: %s"%(ip_int))
        try:
            ip_ext = rq.get("https://icanhazip.com").text
            print("\033[1;34m[*]\033[0m\tIp Externo: %s"%(ip_ext))
        except:
            print("\033[1;31m[-]\033[0m\tNão foi possivel buscar seu Ip Externo!!")
    elif cmd == "chat":
        lt = True
        print("\033[1;34m[*]\033[0m\texec: %s\n"%(cmd))
        slp(0.5)
        user = input("\033[1;34m[*]\033[0m\tUser: ")
        host = input("\033[1;34m[*]\033[0m\tHost: ")
        port = int(input("\033[1;34m[*]\033[0m\tPort: "))
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            client.connect((host,port))
            client.send(user.encode())
            print("\033[1;34m[*]\033[0m\tConectado!!\n")
            def send(client):
                while True:
                    data = (f"{user} : "+input(""))
                    client.send(data.encode())
            def recive(client):
                while True:
                    try:
                        data = client.recv(1024).decode()
                        print(data)
                    except:
                        client.close()
                        break
            thread1 = Thread(target=send,args=(client,))
            thread1.start()
            thread2 = Thread(target=recive,args=(client,))
            thread2.start()
        except:
            print("\033[1;31m[-]\033[0m\tNão conectado!")
    elif cmd == "help":
        print("\033[1;34m[*]\033[0m\texec: %s\n"%(cmd))
        slp(0.5)
        with open(".help.txt","r") as line:
            for i in line:
                print(i,end="")
                slp(0.5)
    elif cmd == "start":
        cmds = input("\033[1;4;37m\x54\x6f\x6f\x6c\x73\033[0m exploit(\033[1;31m%s\033[0m) > "%(cmd))
        if cmds == "seeker":
            exc = input("\033[1;4;37m\x54\x6f\x6f\x6c\x73\033[0m exploit(\033[1;31m%s/%s\033[0m) > "%(cmd,cmds))
            if exc == "run" or exc == "exploit":
                os.chdir(dir+"/files/commands/seeker")
                run("python seeker.py",shell=True)
            else:
                pass
        elif cmds == "pyphisher":
            exc = input("\033[1;4;37m\x54\x6f\x6f\x6c\x73\033[0m exploit(\033[1;31m%s/%s\033[0m) > "%(cmd,cmds))
            if exc == "run" or exc == "exploit":
                os.chdir(dir+"/files/commands/PyPhisher")
                run("python pyphisher.py",shell=True)
            else:
                pass
        elif cmds == "toolsig":
            exc = input("\033[1;4;37m\x54\x6f\x6f\x6c\x73\033[0m exploit(\033[1;31m%s/%s\033[0m) > "%(cmd,cmds))
            if exc == "run" or exc == "exploit":
                os.chdir(dir+"/files/commands/ToolsIG")
                run("node index.js",shell=True)
            else:
                pass
        elif cmds == "tracer":
            exc = input("\033[1;4;37m\x54\x6f\x6f\x7c\x73\033[0m exploit(\033[1;31m%s/%s\033[0m) > "%(cmd,cmds))
            if exc == "run" or exc == "exploit":
                ip = input("\033[1;34m[*]\033[0m\tDigite o endereço IP: ")
                try:
                    with rq.session() as s:
                        r = s.get("http://ip-api.com/json/%s"%(ip)).json()
                        print("""
        \033[1;34m[*]\033[0m\tIP:\t%s
        \033[1;34m[*]\033[0m\tPais:\t%s - %s
        \033[1;34m[*]\033[0m\tEstado:\t%s - %s
        \033[1;34m[*]\033[0m\tCidade:\t%s
        \033[1;34m[*]\033[0m\tORG:\t%s
"""%(r["query"],r["country"],r["countryCode"],r["regionName"],r["region"],r["city"],r["org"]))
                except:
                    print("\033[1;31m[-]\033[0m\tError!")
            else:
                pass
        else:
            print("\033[1;31m[-]\033[0m\tError! A função \033[1;4;37m%s\033[0m não existe!"%(cmds))
    else:
        print("\033[1;34m[*]\033[0m\texec: %s\n"%(cmd))
        slp(0.5)
        run(cmd,shell=True)
        os.chdir(dir+"/files/logs")
        if "logs.txt" in os.listdir():
            with open("logs.txt","a") as log:
                log.write("\t%s"%(cmd))
        else:
            with open("logs.txt","w") as log:
                log.write("""
        #____Logs____#

        %s
"""%(cmd))
#____________________________ [ && ]
