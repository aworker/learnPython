import os
token = input("token: ")
iprdHost = ["10.200.17.11","10.200.17.12","10.200.17.13","10.200.17.75","10.200.17.76","10.200.17.77","10.200.18.71","10.200.18.72","10.200.18.73"]
password = "445566" + token
tabStr = "    "
os.chdir("D:\limingyuan001\pythonScript")
for host in iprdHost:
    with open(host+'.py','w') as file:
        file.write("def Main():")
        file.write("\n")
        file.write(tabStr+"xsh.Screen.Send(\""+password+"\")")
        file.write("\n")
        file.write(tabStr + "host =\""+host+"\"")
        file.write("\n")
        file.write(tabStr+"xsh.Screen.Send('\\r')")
        file.write("\n")
        file.write(tabStr+"xsh.Screen.WaitForString(\"#\")")
        file.write("\n")
        file.write(tabStr+"xsh.Screen.Send(host)")
        file.write("\n")
        file.write(tabStr+"xsh.Screen.Send('\\r')")


