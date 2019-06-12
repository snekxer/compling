"""
In addition to both of the above files, write your own Porter Stemmer. See https://
tartarus.org/martin/PorterStemmer/def.txt for the original paper that describes the
algorithm in detail. Your program should remove the tags, tokenize the text, and run it
through your porter stemmer before counting the tokens. It should run using the
following command in the terminal:

./my_clean_and_count_stems.py <input_file> <output_file>

You may import: sys, re (or regex). You may not use NLTK for any of these steps.

Your full submission should include:
1. clean_and_count_tokens.py
2. nltk_clean_and_count_stems.py
3. my_clean_and_count_stems.py
4. lexical_analysis_out.txt
5. lexical_analysis_nltk_stemmed_out.txt
6. lexical_analysis_stemmed_out.txt

Depending on how you organize your code, you may have more files than this.
"""

# I worked with Will (William Bowers) for a lot of the logic

import sys
import regex

inputf = sys.argv[1]
outputf = sys.argv[2]

#inputf = "Wikipedia-LexicalAnalysis.xml"
#outputf = "lexical_analysis_stemmed_out.txt"

file = open(inputf, "r", encoding="utf-8").read()

# remove XML tags
file = regex.sub(r"<.+?>|\&lt\;.+?\&gt\;", "", file, flag="UNICODE")
file = file.casefold()

# gets words (after cleanup)
tokens = regex.findall(r"\b(?:[a-zA-Z]+[\.\']?[a-zA-Z]?)+\b", file, flag="UNICODE")

measure = r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*"
has_vowel = r"\w*[aeiou]\w*ed$"


def step1b2(word):
    word = regex.sub(r"at$", "ate", word, regex.MULTILINE)
    word = regex.sub(r"bl$", "ble", word, regex.MULTILINE)
    word = regex.sub(r"iz$", "ize", word, regex.MULTILINE)
    if regex.search(r"\w+[^aeiou][^aeiou](?:ed|ing)$", word, regex.MULTILINE):
        word = regex.sub(r"(ing|ed)$", "", word, regex.MULTILINE)
    if regex.search(r"\w+[^aeiou][aeiou][^aeiou](?:ed|ing)$", word, regex.MULTILINE):
        word = regex.sub(r"(ing|ed)$", "", word, regex.MULTILINE)
    return word


def step1(word):
    # step 1a
    word = regex.sub(r"sses$", "ss", word, regex.MULTILINE)
    word = regex.sub(r"ies$", "i", word, regex.MULTILINE)
    word = regex.sub(r"ss$", "ss", word, regex.MULTILINE)
    word = regex.sub(r"s$", "", word, regex.MULTILINE)

    # step 1b - first case
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*eed$", word, regex.MULTILINE):
        word = regex.sub(r"eed$", "ee", word, regex.MULTILINE)

    # step 1b - second and third cases
    if regex.search(r"\w*[aeiou]\w*ed$", word, regex.MULTILINE):
        word = regex.sub(r"ed$", "", word, regex.MULTILINE)
        word = step1b2(word)
    if regex.search(r"\w*[aeiou]\w*ing$", word, regex.MULTILINE):
        word = regex.sub(r"ing$", "", word, regex.MULTILINE)
        word = step1b2(word)

    # step 1c
    if regex.search(r"\w*[aeiou]\w*y$", word, regex.MULTILINE):
        word = regex.sub(r"y$", "i", word, regex.MULTILINE)
    return word


def step2(word):
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*ational$", word, regex.MULTILINE):
        word = regex.sub(r"ational$", "ate", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*[^a]tional$", word, regex.MULTILINE):
        word = regex.sub(r"tional$", "tion", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*enci$", word, regex.MULTILINE):
        word = regex.sub(r"enci$", "ence", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*anci$", word, regex.MULTILINE):
        word = regex.sub(r"anci$", "ance", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*(izer|ization)$", word, regex.MULTILINE):
        word = regex.sub(r"(izer|ization)$", "ize", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*abli$", word, regex.MULTILINE):
        word = regex.sub(r"abli$", "able", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*(alli|alism)$", word, regex.MULTILINE):
        word = regex.sub(r"(alli|alism)$", "al", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*entli$", word, regex.MULTILINE):
        word = regex.sub(r"entli$", "ent", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*eli$", word, regex.MULTILINE):
        word = regex.sub(r"eli$", "e", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*(ousli|ousness)$", word, regex.MULTILINE):
        word = regex.sub(r"(ousli|ousness)$", "ous", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*(ation|ator)$", word, regex.MULTILINE):
        word = regex.sub(r"(ation|ator)$", "ate", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*(iveness|iviti)$", word, regex.MULTILINE):
        word = regex.sub(r"(iveness|iviti)$", "ive", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*fulness$", word, regex.MULTILINE):
        word = regex.sub(r"fulness$", "ful", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*biliti$", word, regex.MULTILINE):
        word = regex.sub(r"biliti", "ble", word, regex.MULTILINE)
    return word


def step3(word):
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*(icate|iciti|ical)$", word, regex.MULTILINE):
        word = regex.sub(r"(icate|iciti|ical)$", "ic", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*alize$", word, regex.MULTILINE):
        word = regex.sub(r"alize$", "al", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*(ative|ful|ness)$", word, regex.MULTILINE):
        word = regex.sub(r"(ative|ful|ness)$", "", word, regex.MULTILINE)
    return word


def step4(word):
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+){1,}[aeiou]*(al|ance|ence|er|ic|able|ible|ant|ement|[^e]ment|[^m]ent|ou|ism|ate|iti|ous|ive|ize)$", word, regex.MULTILINE):
        word = regex.sub(r"(al|ance|ence|er|ic|able|ible|ant|ement|[^e]ment|[^m]ent|ou|ism|ate|iti|ous|ive|ize)$", "", word, regex.MULTILINE)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+){2,}[aeiou]*[st]ion$", word, regex.MULTILINE):
        word = regex.sub(r"ion$", "", word, regex.MULTILINE)
    return word


def step5(word):
    # step 5a
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+){1,}[aeiou]*e$", word, regex.MULTILINE):
        word = regex.sub(r"e$", "", word, regex.MULTILINE)
    if regex.search(r"\w+(?<![^aeiou][aeiou][^aeiou])e$", word, regex.MULTILINE):
        word = regex.sub(r"e$", "", word, regex.MULTILINE)

    # step 5b
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+){1,}[aeiou]*[^aeiou][^aeiou][a-z]$", word, regex.MULTILINE):
        word = regex.sub(r"\w$", "", word, regex.MULTILINE)
    return word


def stemmer(word):
    word = step1(word)
    word = step2(word)
    word = step3(word)
    word = step4(word)
    word = step5(word)

    return word


stems = []

for token in tokens:
    print(token)
    if regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*", token, regex.MULTILINE):
        stem = stemmer(token)
        stems.append(stem)
        print(stem + ' ' + token)

words = {i: stems.count(i) for i in stems}

wordKey = sorted(words.keys())
ordered = sorted(wordKey, key=lambda x: words[x], reverse=True)

with open(outputf, "w") as output:
    for word in ordered:
        output.write(str(word) + ': ' + str(words[word]) + '\n ')
    output.close()


