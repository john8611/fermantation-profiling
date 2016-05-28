#!/share/anaconda/bin/python
import os, sys, time
data_file = "compressed_fungi.dat"

class FG:
    def __init__(self, line):
        self.name = line[1:].strip()
        self.lst_comps = []

    def Info(self):
        print "#FG_Info>%s" % self.name
        for c in self.lst_comps:
            print "#\t%s" % c.name
        print "### has %d comps" % len(self.lst_comps)


class Comp:
    def __init__(self, line):
        self.name = line.strip()


def get_lst():
    lst_fg = []
    fp = open(data_file, 'r')
    line, line1 = None, None
    fg = None
    while 1:
        line1 = line
        line = fp.readline()

        if not line:
            break

        if line[0] == "#":
            fg = FG(line)
            lst_fg.append(fg)

        if fg is not None:
            if "Synonymous names" in line:
                comp = Comp(line1)
                fg.lst_comps.append(comp)
            

    fp.close()
    return lst_fg

def doit():
    lst_fg = get_lst()

    n_cpds = 0
    dic_cpds = {}
    for f in lst_fg:
        f.Info()
        n_cpds += len(f.lst_comps)
        for c in f.lst_comps:
            dic_cpds[c.name] = dic_cpds.get(c.name, 0) + 1

    print "#Total %d fungi..." % len(lst_fg)
    print "#Total %d cmpds..." % n_cpds
    print "#Unique %d cmpds..." % len(dic_cpds)

    for k,v in dic_cpds.items():
        print k

if __name__ == '__main__':
    doit()

