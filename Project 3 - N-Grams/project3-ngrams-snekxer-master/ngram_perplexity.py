"""
Calculating the perplexity on a test set is one way of evaluating the effectiveness of the
language model. Write a script called ngram_perplexity.py, that takes in an ngram
language model as input (output of Part 1), lambda values, a test file and and output
file and calculates the perplexity of the test file.
The script should run with the following command:
./ngram_perplexity.py <input_file> <lambda1> <lambda2> <lambda3>
<test_file> <output_file>
"""

import sys
import math

inputf = sys.argv[1]
lambda1 = sys.argv[2]
lambda2 = sys.argv[3]
lambda3 = sys.argv[4]
testf = sys.argv[5]
outputf = sys.argv[6]

ngram_model = open(inputf, 'r', encoding='utf-8').read()
#lambda1 = 1
#lambda2 = 0
#lambda3 = 0
#testf = "dickens_test.txt"
#outputf = "lambda_out.txt"

"""
Perplexity can be calculated like this:
    for each sentence in the test data file:
    add the number of words in the sentence (excluding <s> and </s>) to the total
    number of words
    for each word(i) in the sentence (excluding <s>, but including </s>:
    if the word(i) is unknown, increment an unknown word counter and
    continue
    Calculate the interpolated log-probability of the trigram as below:
    log( P(word(i) | word(i-2) word (i-1)) )
    #Justin clarified this as: log( lambda1*P(unigram) + lambda2*P(bigram) + lambda3*P(trigram))
    Add this log-prob to a running total
    divide the negative sum of the log-probs by the total number of words added to the
    number of sentences minus the number of unknown words.
    Raise this value to the power of 10
"""
unigram_model_raw = ngram_model[ngram_model.find('\\1-gram'):ngram_model.find('\\2-gram')].strip().splitlines()
unigram_model_raw.pop(0)
unigram_model = []
for line in unigram_model_raw:
    unigram_model.append(line.split(" "))
unigram_dict = {}
model_words = []
for line in unigram_model:
    model_words.append(line[3])
    unigram_dict[line[3]] = line[1]

bigram_model_raw = ngram_model[ngram_model.find('\\2-gram'):ngram_model.find('\\3-gram')].strip().splitlines()
bigram_model_raw.pop(0)
bigram_model = []
for line in bigram_model_raw:
    bigram_model.append(line.split(" "))
bigram_dict = {}
for line in bigram_model:
    bigram_dict[(line[3], line[4])] = line[1]

trigram_model_raw = ngram_model[ngram_model.find('\\3-gram'):len(ngram_model)].strip().splitlines()
trigram_model_raw.pop(0)
trigram_model = []
for line in trigram_model_raw:
    trigram_model.append(line.split(" "))
trigram_dict = {}
for line in trigram_model:
    trigram_dict[line[3], line[4], line[5]] = line[1]

data = [lines.split(" ") for lines in open(testf, "r", encoding="UTF-8").readlines()]
known_words = 0

perplexity_model = []
for line in data:
    i = 0
    for word in line:
        if word not in model_words:
            print("not here")
            i += 1
            continue
        else:
            known_words += 1
            if word is '<s>':
                print("begining of sentence -- skiping")
                i += 1
                continue
            else:
                unigram = word
                bigram = (line[i-1], word)
                if i-2 < 0:
                    trigram = bigram
                else:
                    trigram = (line[i-2], line[i-1], word)
        calc = 0
        print(unigram)
        print(bigram)
        print(trigram)
        if bigram not in bigram_dict.keys():
            bigram_value = 0
        else:
            bigram_value = float(bigram_dict[bigram])
        if trigram not in trigram_dict.keys():
            trigram_value = 0
        else:
            trigram_value = float(trigram_dict[trigram])
        prob = ((lambda1 * float(unigram_dict[unigram])) + (lambda2 * bigram_value) + (lambda3 * trigram_value))
        print(prob)
        calc = math.log10(prob)
        print(calc)
        perplexity_model.append(calc)
        if word is '</s>':
            break
        i += 1
print("sum of log probs = " + str(sum(perplexity_model)))
neg_prob_sum = sum(perplexity_model) * (-1)
print("sum of negative log probs = " + str(neg_prob_sum))
print("known words = " + str(known_words))
print("divided neg prob over known words = " + str(neg_prob_sum / known_words))
perplexity = pow((neg_prob_sum / known_words), 10)
print("perplexity = " + str(perplexity))


with open(outputf, 'a+', encoding='UTF-8') as output:
    output.write("lambda 1 (unigram weight): " + str(lambda1) + '\t')
    output.write("lambda 2 (bigram weight): " + str(lambda2) + '\t')
    output.write("lambda 3 (trigram weight): " + str(lambda3) + '\t\t')
    output.write("perplexity: " + str(perplexity) + "\n")
output.close()



"""
Build a model using dickens_training.txt. Calculate the perplexity for the following
lambda values on dickens_test.txt:

------------------------------------------------------------
|     lambda 1      |     lambda 2     |     lambda 3      |
| (unigram weight)  | (bigram weight)  | (trigram weight)  |
|----------------------------------------------------------|
|        0.1        |      0.1          |       0.8        |
|----------------------------------------------------------|
|        0.2        |      0.5          |       0.3        |
|----------------------------------------------------------|
|        0.2        |      0.7          |       0.1        |
|----------------------------------------------------------|
|        0.2        |      0.8          |        0         |
|----------------------------------------------------------|
|        1.0        |       0           |        0         |
|----------------------------------------------------------|

"""
