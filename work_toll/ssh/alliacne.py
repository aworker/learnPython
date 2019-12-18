import os
import time
from sshTool import generateXsh
from sshTool import generateVbs
from sshTool import openXshFile

token = input("token: ")
iprdHost = ["10.200.19.144","10.200.16.137","10.200.20.103","10.200.19.49","10.200.18.32","10.200.17.53","10.200.19.202","10.200.20.104","10.200.16.138","10.200.19.246","10.200.20.22","10.200.20.139","10.200.20.16","10.200.20.132","10.200.20.82","10.200.20.18","10.200.19.219","10.200.17.18","10.200.19.223","10.200.20.133","10.200.17.19","10.200.17.16","10.200.19.203","10.200.20.131","10.200.19.235","10.200.19.244","10.200.16.217","10.200.18.111","10.200.19.89","10.200.19.90","10.200.19.101","10.200.19.102","10.200.19.103","10.200.19.176","10.200.21.43","10.200.19.213"]
# iprdHost = ["10.200.19.144","10.200.16.137","10.200.20.103"]
password = "445566" + token
tabStr = "    "


# generate vbScript for Xshell
count = 0;
for host in iprdHost:
    generateVbs(host,password)
    generateXsh(host)
    if count == 1:
        time.sleep(3)
    else :
        time.sleep(1)
    openXshFile(host)
    count = count + 1


# open the session file for Xshell
# count = 0;
# for host in iprdHost:
#     xshFile = "start Xshell " + xshDir + "\\" + host + ".xsh"
#     if count == 1:
#         time.sleep(3)
#     else:
#         time.sleep(1)
#     count = count + 1
#     os.popen(xshFile)
