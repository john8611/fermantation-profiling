#!/usr/bin/env python

g = open("CSV.inp","r")
list_3D = g.readlines()

for csv_3D in list_3D :
    csv_3D = csv_3D.replace("\n","")
    tip3D = csv_3D.split("/")
    # list the path as its factor


    Class_3D = tip3D[-2][:-1]
    Type_3D = tip3D[-3]
    sample = tip3D[-2]
    sample_num = tip3D[-1].replace("-OUT.CSV","")

    f = open(csv_3D,"r")
    file_3D =  f.readlines()

    for i in file_3D[5:] :
        i = i.split(",")
        scan = int(i[0])
        for mz,intensity in enumerate(i[1:]):
            try :
                intensity = int(intensity)
                print Class_3D + "\t" + Type_3D + "\t"+ sample+ "\t" + sample_num + "\t" + str(scan) + "\t" + str(mz+50) + "\t" + str(intensity)
            except ValueError :
                continue
    # print Class_3D,Type_3D,sample,sample_num

    f.close()
g.close()
