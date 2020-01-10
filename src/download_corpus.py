from korp_lib.utils import *
import time
import json, os, sys, re

YEARS = [x for x in range(1862, 1900)]
SENTENCE_COUNT = 150000

def aopen(path):
    return open(path, "a", encoding="utf-8")

if __name__ == "__main__":

    for year in YEARS:
        t0 = time.time()
        kwic_paths= download_sentences(year, SENTENCE_COUNT)
        print(year, "downloaded in:", time.time()-t0)
        for path in kwic_paths:
            with open(path, "r", encoding="utf-8") as f:
                kwic = json.load(f)["kwic"]

            with aopen("../data/lemmas/"+str(year)) as lem, aopen("../data/words/"+str(year)) as wor:

                for line in kwic:
                    words = ",".join(['"'+x["word"]+'"' for x in line["tokens"]])
                    lemmas = ",".join(['"'+x["lemma"]+'"' for x in line["tokens"]])

                    lem.write(lemmas+"\n")
                    wor.write(words+"\n")
            
            os.remove(path)

        print("written in:", time.time()-t0)



