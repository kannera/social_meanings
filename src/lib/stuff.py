import json, os, re, sys

def open_csv(path):

    with open(path, "r", encoding="utf-8") as f:
        data = [x.replace("\n", "")[1:-1].split('","') for x in f]

    return data


def write_csv(data, path):

    

    res = ['"'+'","'.join([str(y) for y in x])+'"' for x in data]
    res = "\n".join(res)

    with open(path, "w", encoding="utf-8") as f:
        f.write(res)


def frequency_list(data, n):

    freqs = {}

    for row in data:
        for word in row:
            freqs[word] = freqs.get(word, 0) + 1

    return [x for x in freqs if freqs[x] >= n], freqs

def frequency_index(datatype):

    data = open_csv("../data/resources/"+datatype+"_freqmap.csv")

    index = [x[0] for x in data]
    return index

def frequency_table(datatype):
    data = open_csv("../data/resources/"+datatype+"_freqmap.csv")
    return [[int(y) for y in x[2:]] for x in data]

def list_to_fdict(A):
    return {i:A.count(i) for i in set(A)}
