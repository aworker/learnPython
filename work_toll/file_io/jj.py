import os

getcwd = os.getcwd()
print(getcwd)
commenStr = 'truncate table mls_pc_relation_'
with open("1.txt","w") as file:
    for i in  range(128):
        zfill = str(i).zfill(3)+";"
        file.write(commenStr + zfill)
        file.write("\n")




