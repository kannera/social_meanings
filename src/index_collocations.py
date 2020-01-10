import json, re, sys, os
import numpy as np
import time
from lib.stuff import *

YEARS = [i for i in range(1860, 1900)]
DATA_PATH = "../data/"

if __name__ == "__main__":

    datatype = "lemmas"

    data_path = DATA_PATH + datatype + "/"
    
    freq_map = frequency_index(datatype)


    for year in YEARS:
        res = {x:[] for x in freq_map}
        res_path = DATA_PATH + datatype + "_indices/" + str(year)
        t0 = time.time()
        data = open_csv(data_path + str(year))
        
        for i,row in enumerate(data):
            for x in row:
                if x in res.keys():
                    res[x].append(i)

        res_matrix = [res[x] for x in freq_map]
        write_csv(res_matrix, res_path)







        





