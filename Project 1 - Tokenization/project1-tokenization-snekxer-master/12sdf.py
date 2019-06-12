import sys
import regex

#inputf = sys.argv[1]
#outputf = sys.argv[2]

inputf = "Wikipedia-LexicalAnalysis.xml"
outputf = "lexical_analysis_stemmed_out.txt"

file = open(inputf, "r", encoding="utf-8").read()

# remove XML tags
file = regex.sub(r"<.+?>|\&lt\;.+?\&gt\;", "", file, flag="UNICODE")
file = file.casefold()

# gets words (after cleanup)
tokens = regex.findall(r"\b(?:[a-zA-Z]+[\.\']?[a-zA-Z]?)+\b", file, flag="UNICODE")

measure = r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*"
has_vowel = r"\w*[aeiou]\w*"


def has_measure(word,suffix):
    return regex.search(r"[^aeiou\W]*(?:[aeiou]+[^aeiou\W]+)+[aeiou]*" % suffix, word, flags="MULTILINE, UNICODE")


def has_vowel(word, suffix):
    return regex.search(r"\w*[aeiou]\w*"+suffix, word, flags="MULTILINE, UNICODE")


for word in tokens:
    if has_measure(word, "*eed$"):
        print('yes')

