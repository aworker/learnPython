with open("mls_pc_relations.txt","w") as wfile:
    for i in range(0, 128):
        ll = "CREATE TABLE `mls_pc_relation_"+str(i).zfill(3)+"` ("
        with open("module", "r") as file:
            for line in file:
                if "mls_pc_relation_" in line:
                    line = ll;
                wfile.write(line)
        wfile.write('\n')
