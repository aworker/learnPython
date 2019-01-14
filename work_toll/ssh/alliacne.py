import os
import time

token = input("token: ")
iprdHost = ["10.200.20.16"
    , "10.200.20.17"
    , "10.200.20.18"
    , "10.200.19.202"
    , "10.200.19.203"
    , "10.200.19.204"
    , "10.200.20.131"
    , "10.200.20.132"
    , "10.200.20.133"
    , "10.200.19.219"
    , "10.200.20.139"
    , "10.200.20.22"
            ]
password = "445566" + token
tabStr = "    "
scriptDir = "D:\limingyuan001\\vbsScript"
xshDir = "D:\limingyuan001\AppData\Roaming\\NetSarang\Xshell\Sessions"
os.chdir(scriptDir)

# generate vbScript for Xshell
for host in iprdHost:
    with open(host + '.vbs', 'w') as file:
        file.write("Sub Main")
        file.write("\n")
        file.write(tabStr + "xsh.Screen.Send(\"" + password + "\")")
        file.write("\n")
        file.write(tabStr + "xsh.Screen.Send(VbCr)")
        file.write("\n")
        file.write(tabStr + "xsh.Screen.WaitForString \"# \"")
        file.write("\n")
        file.write(tabStr + "xsh.Screen.Send(\"" + host + "\")")
        file.write("\n")
        file.write(tabStr + "xsh.Screen.Send(VbCr)")
        file.write("\n")
        file.write("End Sub")

# open the session file for Xshell
count = 0;
for host in iprdHost:
    xshFile = "start Xshell " + xshDir + "\\" + host + ".xsh"
    if count == 1:
        time.sleep(3)
    else:
        time.sleep(1)
    count = count + 1
    os.popen(xshFile)
