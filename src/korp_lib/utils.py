import wget

def download_sentences(year, sentence_count):

    corpus_name = "KLK_FI_"+str(year)
    paths = []
    for index in range(0, sentence_count, 1000):

        url = "https://korp.csc.fi/cgi-bin/korp.cgi?command=query&defaultcontext=1+sentence&show=lemma&cache=true&start="+str(index)+"&end="+str(index+999)+"&corpus="+corpus_name+"&incremental=true&cqp=%5Bref+%3D+%221%22%5D&defaultwithin=sentence&sort=random&random_seed=1298753"

        paths.append(wget.download(url))

    return paths


