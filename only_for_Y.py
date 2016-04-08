Y = ["/home/madbunny/test/GC-MS/actual/Y/1117Y7E.D/RESULTS.CSV","/home/madbunny/test/GC-MS/actual/Y/1117Y8E.D/RESULTS.CSV","/home/madbunny/test/GC-MS/actual/Y/1117Y9E.D/RESULTS.CSV"]
g = open("2D_CSV_list.inp","r")
k = g.readlines()
Y = [x.replace("\n","") for x in k]

print Y


for name in Y :
    path_list = name.split("/")
    sample_info = path_list[-2].replace(".D","")
    date_info = sample_info[:4]
    mon = date_info[:2]
    day = date_info[2:]
    date = "2015/"+mon+"/"+day
    sample = sample_info[4:]
    #class_sample = sample[:-1]
    # only for Y
    class_sample = sample[:-2]

    f = open(name,"r")
    a = f.read()

    # spliter all
    spl_1 = '''Header=,"Peak","R.T.","First","Max","Last","PK  TY","Height","Area","Pct Max","Pct Total"\r\n'''
    spl_2 = '''Header=,"PK","RT","Area Pct","Library/ID","Ref","CAS","Qual"\r\n'''

    b = a.split(spl_1)
    c = b[1].split(spl_2)

    ori_PK_dat = c[0].split("\r\n")[:-3]
    comp_PK_dat = c[1].split("\r\n")

    for index,ori in enumerate(ori_PK_dat):
        d = ori.split(",")
        e = comp_PK_dat[index].split(",")
        Peak = int(d[1])
        RT = d[2]
        scan_num = int(d[4])
        intensity = d[8]
        compoud = e[4].split("$$")[0].replace('"','')
        Qual = int(e[-1])
        print class_sample+"\t"+sample+"\t"+date+"\t"+str(Peak)+"\t"+RT+"\t"+str(scan_num)+"\t"+str(intensity)+"\t"+compoud+"\t"+str(Qual)
