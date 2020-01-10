import json, re, sys, os
import time
from lib.stuff import *

YEARS = [x for x in range(1860, 1900)]
DATAPATH = "../data/"


def nplus_freq_map(n, datatype):

    freq_data = {}
    full_nplus = []

    for year in YEARS:
        t0 = time.time()
        data = open_csv(DATAPATH+datatype+"/"+str(year))
        nplus, freqs = frequency_list(data, n)
        full_nplus = list(set(nplus + full_nplus))
        for f in freqs:
            if f not in freq_data:
                freq_data[f] = {x:0 for x in YEARS}
            freq_data[f][year] = freqs[f]

        print(year, "done")

    print("trimming...")
    freq_data = {x:freq_data[x] for x in full_nplus}
    print("done")
    print("computing row sums")

    for f in freq_data:
        freq_data[f]["tf"] = sum(freq_data[f].values())
    print("done")

    keys = ["tf"]+[x for x in YEARS]
    matrix = []
    
    for f in full_nplus:
        if freq_data[f]["tf"] > 50:
            matrix.append(list([f]+[freq_data[f][x] for x in keys if freq_data[f]["tf"] >= 1]))


    matrix = sorted(matrix, key = lambda x:x[1], reverse=True)
    matrix = ['"'+'","'.join([str(y) for y in x])+'"' for x in matrix]
    matrix = "\n".join(matrix)

    with open(DATAPATH+"resources/"+datatype+"_freqmap.csv", "w", encoding="utf-8") as f:
        f.write(matrix)
    
        









if __name__ == "__main__":

    

    datatype = "words"
    n = 5

    nplus_freq_map(n, datatype)
        

