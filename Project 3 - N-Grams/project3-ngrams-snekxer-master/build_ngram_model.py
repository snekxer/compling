"""
Write a script called build_ngram_model.py, that takes in an input file and outputs a
file with the probabilities for each unigram, bigram, and trigram of the input text.
The script should run with the following command:

./build_ngram_model.py <input_file> <output_file>

The input file format is 1 sentence per line, with spaces between every word. (The files
are pre-tokenized).
Add beginning of sentence (<s>) and end of sentence tags (</s>) and make everything
lowercase.
For example, if a sentence is:

Hello , my cat !

You will count as if the sentence is written:

<s> hello , my cat ! </s>
"""


import sys
import math

input = sys.argv[1]
output = sys.argv[2]

#input = "dickens_training.txt"
#output = "dickens_model.txt"

file = open(input, 'r', encoding='UTF-8').read().splitlines()

words_count = 0

#lowercase and beginning/end of sentence
mod_file = ['<s> ' + line.lower() + ' </s>' for line in file]

unigrams = []
bigrams = []
trigrams = []

#splits words in each line and formats them into uni/bi/trigrams by using relative position
for line in mod_file:
    i = 0
    split_line = line.split(" ")
    words_count += len(split_line)
    for word in split_line:
        unigrams.append(word)
        if i+1 < len(split_line):
            bigrams.append((word, split_line[i+1]))
        if i+2 < len(split_line):
            trigrams.append((word, split_line[i+1], split_line[i+2]))
        i += 1

#Makes dictionary of uni/bi/trigrams, sorts them, and makes dictionary of the sorted elements.
#Will helped me with the ngram loop for the dictionary after my beautiful one liner failed :(
uni_count = {}
for unigram in unigrams:
    if unigram in uni_count:
        uni_count[unigram] += 1
    else:
        uni_count[unigram] = 1
#uni_count = {i: unigrams.count(i) for i in unigrams}
uni_keys = sorted(sorted(uni_count.keys()), key=lambda x: uni_count[x], reverse=True)
uni_ordered = {}
[uni_ordered.update({word: uni_count[word]}) for word in uni_keys]

bi_count = {}
for bigram in bigrams:
    if bigram in bi_count:
        bi_count[bigram] += 1
    else:
        bi_count[bigram] = 1

#bi_count = {i: bigrams.count(i) for i in bigrams}
bi_keys = sorted(sorted(bi_count.keys()), key=lambda x: bi_count[x], reverse=True)
bi_ordered = {}
[bi_ordered.update({word: bi_count[word]}) for word in bi_keys]

tri_count = {}
for trigram in trigrams:
    if trigram in tri_count:
        tri_count[trigram] += 1
    else:
        tri_count[trigram] = 1
#tri_count = {i: trigrams.count(i) for i in trigrams}
tri_keys = sorted(sorted(tri_count.keys()), key=lambda x: tri_count[x], reverse=True)
tri_ordered = {}
[tri_ordered.update({word: tri_count[word]}) for word in tri_keys]

"""
The output file should have the following format: (see sample file: dickens_model.txt)

\data\
ngram 1: types=<# of unique unigram types> tokens=<total # of unigram tokens>
ngram 2: types=<# of unique bigram types> tokens=<total # of bigram tokens>
ngram 3: types=<# of unique trigram types> tokens=<total # of trigram tokens>

\1-grams:
<list of unigrams>

\2-grams:
<list of bigrams>

\3-grams:
<list of trigrams>

The lists should include the following, in order, separated by spaces:

Count of n-gram

Probability of n-gram (P(wn | wn-1) for bigram and P(wn | wn-2 wn-1) for trigram)

Log-prob of n-gram (take the log base 10 of the probability above)

n-gram

Do not use smoothing for this! Only include n-grams that exist in the training text.
"""

with open(output, "w", encoding='UTF-8') as output:
    output.write(
        "\\data\\\n" +
        "ngram 1: types=" + str(len(uni_ordered.keys())) + " tokens=" + str(sum(uni_ordered.values())) + "\n" +
        "ngram 2: types=" + str(len(bi_ordered.keys())) + " tokens=" + str(sum(bi_ordered.values())) + "\n" +
        "ngram 3: types=" + str(len(tri_ordered.keys())) + " tokens=" + str(sum(tri_ordered.values())) + "\n"
    )

    output.write("\n \\1-gram: \n")
    for key, value in uni_ordered.items():
        prob = value / words_count
        log = math.log10(prob)
        output.write(str(value) + " " + str(prob) + " " + str(log) + " " + key + "\n")

    output.write("\n \\2-gram: \n")
    for key, value in bi_ordered.items():
        prob = value / uni_ordered[key[0]]
        log = math.log10(prob)
        output.write(str(value) + " " + str(prob) + " " + str(log) + " " + str(key[0] + " " + key[1]) + "\n")

    output.write("\n \\3-gram: \n")
    for key, value in tri_ordered.items():
        prob = value / bi_ordered[(key[0], key[1])]
        log = math.log10(prob)
        output.write(str(value) + " " + str(prob) + " " + str(log) + " " + str(key[0] + " " + key[1] + " " + key[2]) + "\n")

    output.close()
