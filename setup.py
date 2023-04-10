from subprocess import *
import os
run("apt-get install figlet -y",shell=True)
print("*"*88,"\n\033[1;34m[*]\033[0m\tBaixando banner...")
dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)
run("mkdir files",shell=True)
os.chdir(dir+"/files")
run("mkdir commands logs banner",shell=True)
os.chdir(dir+"/files/banner")
run("figlet -c -t 'Tools-H4X' >> b.txt",shell=True)
print("*"*88,"\n\033[1;34m[*]\033[0m\tBaixando exploits...")
os.chdir(dir+"/files/commands")
run("apt-get install git -y",shell=True)
links = ["https://github.com/thewhiteh4t/seeker","https://github.com/KasRoudra/PyPhisher","https://github.com/ZheHacK/ToolsIG"]
for i in links:
    run("git clone %s"%(i),shell=True)
if "seeker" in os.listdir():
    os.chdir(dir+"/files/commands/seeker")
    run("bash install.sh",shell=True)
os.chdir(dir+"/files/commands")
run("apt-get install nodejs -y",shell=True)
os.chdir(dir+"/files/commands/ToolsIG")
run("npm install",shell=True)
os.chdir(dir)
print("*"*88,"\n\033[1;34m[*]\033[0m\tBaixando pacotes do python...")
run("python3 -m pip install requests",shell=True)
print("*"*88,"\n\033[1;34m[*]\033[0m\tUse: python3 main.py")

