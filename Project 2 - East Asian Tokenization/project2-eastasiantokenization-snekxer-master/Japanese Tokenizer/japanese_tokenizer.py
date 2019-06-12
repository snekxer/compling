"""
Japanese Tokenization
For the Japanese tokenization project, you will use the MaxMatch algorithm to read in
a file with lines of Japanese text without spaces, find the word boundaries, and output
a file with the same lines of text with spaces added between words.
./japanese_tokenizer.py <input_file> <output_file>

The MaxMatch algorithm uses a dictionary (japanese_wordlist.txt). Starting from the
beginning of the sentence, match the longest consecutive string of characters that
exists in the dictionary. Once you have found that longest string, insert a space and
continue. If no matches exist in the dictionary, consider the character a one character
word, insert a space and continue.

The sample_out.txt file contains the correctly tokenized output of the in.txt file. Please
check your program output against this file.

gold_standard.txt contains the ideal tokenization. The MaxMatch algorithm makes
mistakes, so don't expect your tokenization output to match this. When you're done
implementing MaxMatch, compare the output of your file to the gold_standard. Make
a file (by hand or programmatically) named evaluation.txt that contains the following:

# of sentences tokenized correctly: <# of lines of output that match gold_standard>
# of sentences tokenized incorrectly: <# of lines of output that don't match
gold_standard>
accuracy: <# correct / total # of sentences>
"""
import sys
import regex
infile = sys.argv[1]
outfile = sys.argv[2]

#outfile = "out.txt"
lines = open(infile, "r", encoding='UTF-8').read().split('\n')

eval = open('gold_standard.txt', "r", encoding='UTF-8').read().split('\n')

wordlist = open("japanese_wordlist.txt", "r", encoding='UTF-8').read().split('\n')

allwords = []
words = []

def matchy(line):
    #checks if it's at the end of line so it can finish the lopp
    if line != "。":
        #is the whole line in the wordlist
        if line in wordlist:
            words.append(line)
            return
        else:
            restofline = line
        #decreases rest of the line until whatever is left is in the dictionary or is one character long
        while restofline not in wordlist and len(restofline) != 1:
            restofline = line[0:len(restofline) - 1]
        words.append(restofline)
        #gets the remainder of the line without the word found
        restofline = line[len(restofline):len(line)]
        matchy(restofline)
    else:
        words.append(line)


with open(outfile, 'w', encoding='UTF-8') as output:
    for line in lines:
        matchy(line)
        for word in words:
            output.write(word + " ")
        output.write("\n")
        allwords.append((words[:]))
        words.clear()


#for ev in eval:
#    ev = list(ev.split(" "))
#    print(ev)
#    if ev in allwords:
#        print("found")

matches = 0

for i in range(0, len(eval)):
    eval[i] = list(eval[i].split(" "))
    if eval[i] == allwords[i]:
        matches = matches + 1

evaluation = "# of sentences tokenized correctly: " + str(matches) + '\n' + \
             "# of sentences tokenized incorrectly: " + str((len(eval) - matches)) + '\n' + \
             "accuracy: " + str(matches) + "/" + str(len(eval))
open("evaluation.txt","w", encoding='UTF-8').write(evaluation)







