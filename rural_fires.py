with open("rural_fires.csv", "r") as f:
    with open("table_rural_fires.csv", "w") as fw:
        for line in f:
            if line[0]=="1" or line[0]=="2" or line[0]=="3":
                fw.write(line)
