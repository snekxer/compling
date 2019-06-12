"""
In addition to the above file, write a program that uses nltk's word_tokenizer and porter
stemmer after cleaning out the tags, but before counting the tokens. This program
should run using the following command in the terminal:

./nltk_clean_and_count_stems.py <input_file> <output_file>

For more information about NLTK's tokenizing/stemming, check out Chapter 3 of the
NLTK book: http://www.nltk.org/book/ch03.html

Check out sample_stemmed_out.txt for an example output.

You may import: sys, re (or regex), nltk (for this file only)

Your submission should include:
1. clean_and_count_tokens.py
2. nltk_clean_and_count_stems.py
3. lexical_analysis_out.txt
4. lexical_analysis_nltk_stemmed_out.txt

Depending on how you organize your code, you may have more files than this.
"""

# I worked with Will (William Bowers) for a lot of the logic

from nltk import *
import sys
import regex

inputf = sys.argv[1]
outputf = sys.argv[2]

#inputf = "Wikipedia-LexicalAnalysis.xml"
#outputf = "lexical_analysis_nltk_stemmed_out.txt"

file = open(inputf, "r", encoding="utf-8").read()

# remove XML tags
file = regex.sub(r"<.+?>|\&lt\;.+?\&gt\;", "", file, flag="UNICODE")
file = file.casefold()

# gets words (after cleanup)
file = regex.findall(r"\b(?:[a-zA-Z]+[\.\']?[a-zA-Z]?)+\b", file, flag="UNICODE")
words = " ".join(str(i) for i in file)

tokens = word_tokenize(words)

stems = [PorterStemmer().stem(i) for i in tokens]

# makes dictionary out of stems
words = {i: stems.count(i) for i in stems}

wordKey = sorted(words.keys())
ordered = sorted(wordKey, key=lambda x: words[x], reverse=True)

with open(outputf,"w") as output:
    for word in ordered:
        output.write(str(word) + ': ' + str(words[word]) + '\n ')
    output.close()


