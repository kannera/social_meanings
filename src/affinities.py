import re, sys, os, json
import time
import numpy as np
from lib.stuff import *

YEARS = [y for y in range(1860, 1900)]
WINDOW = 10
ROLLING = 5
CAP = 100
COLLOCATION_CAP = 5
DATA_PATH = "../data/"

def compute_pmi(i, j, co, window, farr):

    fi = farr[i,window].sum()
    fj = farr[j,window].sum()
    tf = farr[:,window].sum()

    pco = co/tf
    ecp = (fi/tf)*(fj/tf)

    return np.log(pco/ecp)
    
def get_affinities(i, window, sentence_path, index_path, freqmap):

    res = []
    for j in window:
        year = j + 1860
        print(year)
        sentences = open_csv(sentence_path + str(year))
        indices = open_csv(index_path + str(year))
        i_word_sentences = [int(x) for x in indices[i]]
        for s in i_word_sentences:
            res.extend([freqmap.index(w) for w in sentences[s] if w in freqmap and freqmap.index(w) > 100])
         
    collocations = list_to_fdict(res)
    affinities = {x:compute_pmi(start_i, x, collocations[x], window, farray) for x in collocations if collocations[x] >= COLLOCATION_CAP}
    return affinities

if __name__ == "__main__":

    datatype = "lemmas"
    test_word = "waiwainen"

    data_path_index = DATA_PATH + datatype + "_indices/"
    data_path_sents = DATA_PATH + datatype + "/"

    freqtable = open_csv(DATA_PATH + "resources/" + datatype + "_freqmap.csv")
    farray = np.array([x[2:] for x in freqtable], dtype='int64')
    freqmap = [x[0] for x in freqtable]
    
    start_i = freqmap.index(test_word)

    res = dict()
    for i in range(0, len(YEARS)-ROLLING, ROLLING):
        window = [j for j in range(i, i+WINDOW)]
        res[i] = {}

        first_orders = get_affinities(start_i, window, data_path_sents, data_path_index, freqmap)
        res[i][start_i] = first_orders
        print(i, "first done")
        with open(DATA_PATH + "resources/affinities_" + test_word + ".json", "w", encoding="utf-8") as f:
            json.dump(res, f)
        for k in first_orders:
            res[i][k] = get_affinities(k, window, data_path_sents, data_path_index, freqmap)
            with open(DATA_PATH + "resources/affinities_" + test_word + ".json", "w", encoding="utf-8") as f:
                json.dump(res, f)
            print(k, "done")

        print(i, "second done")


        sys.exit()



