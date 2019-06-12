"""
Write a script, generate_from_ngram.py, that takes an ngram language model (output
from the previous part, written to a file as described above), and outputs to a file 5
sentences generated from the unigram, bigram, and trigram models.
The script should run with the following command:

./generate_from_ngram.py <input_file> <output_file>

You will need to import random for this script.

"""

import sys
import random

input = sys.argv[1]
output = sys.argv[2]

#input = "dickens_model.txt"
#output = "generated_sentences.txt"

ngram_model = open(input, 'r', encoding='UTF-8').read()
random.seed()

punctuation_signs = (".", "!", "?", "...")

"""
Unigram:
Generate a random number from 0.0 to 1.0, and begin to count up the
probabilities for the unigrams. When you reach the unigram whose probability sends
the probability total above the random number, add that unigram to the sentence.
Repeat.
Sentences should begin with <s> and end with </s>, and not have any <s>s or
</s>s between the start and end.
"""
unigram_model = ngram_model[ngram_model.find('\\1-gram'):ngram_model.find('\\2-gram')].strip().splitlines()
unigram_model.pop(0)
unigram_model.reverse()


def select_word(pos, model, rand_num, sentence):
    original = sentence
    added_word = False
    print("original sentence:" + str(original))
    for unigram in model:
        prob = float(unigram.split(" ")[1])
        key = unigram.split(" ")[pos]
        # makes sure the word is not beginning of a sentence
        if prob > rand_num and key != '<s>':
            sentence.append(key)
            if sentence[len(sentence) - 1] in punctuation_signs:
                sentence.append('</s>')
            print("added word " + key)
            added_word = True
            break
        if sentence[len(sentence) - 1] == '</s>':
            break
    print("    new sentence: " + str(sentence))
    if not added_word:
        print("sentences are equal")
        rand = random.uniform(0.0, 1.0)
        select_word(pos, model, rand, sentence)


uni_sentences = []
for i in range(0, 5):
    print("unigrams")
    uni_sentence = []
    uni_sentence.append('<s>')
    while '</s>' not in uni_sentence:
        uni_rand = random.uniform(0.0, 1.0)
        select_word(3, unigram_model, uni_rand, uni_sentence)
    uni_sentences.append(uni_sentence)

"""
Bigram:
Start with <s>. Generate a random number from 0.0 to 1.0, and begin to count
up the probabilities of the second word, given <s>. When you reach the word whose
probability sends the probability total above the random number, add that word to the
sentence, and repeat with the bigrams that start with the word you generated.
Sentences should begin with <s> and end with </s>, and not have any <s>s or
</s>s between the start and end.
"""

bigram_model = ngram_model[ngram_model.find('\\2-gram'):ngram_model.find('\\3-gram')].strip().splitlines()
bigram_model.pop(0)
bigram_model.reverse()


def filter_ngrams(nmodel, word):
    filtered = []
    for model in nmodel:
        if model.split(" ")[3] == word:
            filtered.append(model)
    return filtered


bi_sentences = []

for i in range(0, 5):
    print("bigrams")
    bi_sentence = []
    bi_sentence.append('<s>')

    while '</s>' not in bi_sentence:
        bi_rand = random.uniform(0.0, 1.0)
        select_word(4, filter_ngrams(bigram_model, bi_sentence[len(bi_sentence) - 1]), bi_rand, bi_sentence)

    bi_sentences.append(bi_sentence)

"""
Trigram:
Same idea as above, adapted to trigrams. Use the bigram generator to find the
first word after the <s> of the sentence.
"""

trigram_model = ngram_model[ngram_model.find('\\3-gram'):len(ngram_model)].strip().splitlines()
trigram_model.pop(0)
trigram_model.reverse()

tri_sentences = []

for i in range(0, 5):
    tri_sentence = []
    tri_sentence.append('<s>')

    while '</s>' not in tri_sentence:
        tri_rand = random.uniform(0.0, 1.0)
        select_word(4, filter_ngrams(trigram_model, tri_sentence[len(tri_sentence) - 1]), tri_rand, tri_sentence)
        select_word(5, filter_ngrams(trigram_model, tri_sentence[len(tri_sentence) - 1]), tri_rand, tri_sentence)

    tri_sentences.append(tri_sentence)

with open(output, "w", encoding='UTF-8') as output:
    output.write("Sentences generated from unigrams: \n")
    for sentence in uni_sentences:
        for word in sentence:
            output.write(word + " ")
        output.write("\n")

    output.write("\nSentences generated from bigrams: \n")
    for sentence in bi_sentences:
        for word in sentence:
            output.write(word + " ")
        output.write("\n")

    output.write("\nSentences generated from trigrams: \n")
    for sentence in tri_sentences:
        for word in sentence:
            output.write(word + " ")
        output.write("\n")

    output.close()
