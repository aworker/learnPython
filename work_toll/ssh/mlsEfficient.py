import os
import time
token = input("token: ")
iprdHost = [
     "10.200.18.145"
    ,"10.200.18.146"
    ,"10.200.18.210"
    ,"10.200.18.211"
    ,"10.200.18.212"
    ,"10.200.18.213"
    ,"10.200.18.214"
    ,"10.200.18.215"
]
password = "445566" + token
tabStr = "    "
scriptDir = "D:\limingyuan001\\vbsScript"
xshDir = "D:\limingyuan001\AppData\Roaming\\NetSarang\Xshell\Sessions"
os.chdir(scriptDir)

# generate vbScript for Xshell
for host in iprdHost:
    with open(host+'.vbs','w') as file:
        file.write("Sub Main")
        file.write("\n")
        file.write(tabStr+"xsh.Screen.Send(\""+password+"\")")
        file.write("\n")
        file.write(tabStr+"xsh.Screen.Send(VbCr)")
        file.write("\n")
        file.write(tabStr+"xsh.Screen.WaitForString \"# \"")
        file.write("\n")
        file.write(tabStr+"xsh.Screen.Send(\""+host+"\")")
        file.write("\n")
        file.write(tabStr+"xsh.Screen.Send(VbCr)")
        file.write("\n")
        file.write("End Sub")


# open the session file for Xshell
for host in iprdHost:
    xshFile = "start Xshell "+xshDir+"\\" +host+".xsh"
    time.sleep(2)
    os.popen(xshFile)




