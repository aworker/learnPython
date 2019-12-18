import os
from datetime import  datetime


def openXshFile(fileName):
    xshDir = "D:\limingyuan001\AppData\Roaming\\NetSarang\Xshell\Sessions"
    os.chdir(xshDir)
    xshFile = "start Xshell " + xshDir + "\\" + fileName + ".xsh"
    os.popen(xshFile)

def generateXsh(fileName) :
    xshDir = "D:\limingyuan001\AppData\Roaming\\NetSarang\Xshell\Sessions"
    xsh_common = "ScriptPath=D:\limingyuan001\\vbsScript\\"

    os.chdir(xshDir)

    template = "template"

    with open(template + '.xsh', 'r') as template_file:
        with open(fileName + '.xsh','w') as target_file:
            for line in template_file.readlines():
                if line.find("ScriptPath")  >= 0 :
                    line = xsh_common + fileName + ".vbs\n"
                target_file.write(line)



def generateVbs(host,password):
    vbsDir = "D:\limingyuan001\\vbsScript"
    os.chdir(vbsDir)
    tabStr = "    "
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