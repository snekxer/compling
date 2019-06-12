"""
I'm providing hmm.txt, which is in the following format (italics are replaced with values in the file):

state_num=number of states
sym_num=number of POS tags
\init
tag P(tag | BOS) log10(P(tag | BOS))
...
\transition
tag1 tag2 P(tag2 | tag1) log10(P(tag2 | tag1))
...
\emission
tag word P(word | tag) log10(P(word | tag))
...

* If there is no transition probability from tag1 to tag2, then it is impossible to go from
tag1 to tag2.
* If there is no transition probability from tag to word, then it is impossible for that tag
to generate that word.

Each line of the test_file contains a single sentence.
The format of the output_file should be, one sentence per line:
word1/tag1 word2/tag2 word3/tag3...

"""
import sys

#hmm = sys.argv[1]
#testf = sys.argv[1]
#outputf = sys.argv[1]

inputf = "hmm.txt"
testf = "test_file.txt"
outputf = "markov_output.txt"

hmm = open(inputf, "r", encoding="UTF-8").read()

hmm_array_prob_matrix = hmm[hmm.find('\\transition'):hmm.find('\\emission')].strip().splitlines()
hmm_array_prob_matrix.pop(0)
matrix = []
for line in hmm_array_prob_matrix:
    matrix.append(line.split('\t'))
print(matrix)

hmm_observation = hmm[hmm.find('\\emission'):].strip().splitlines()
hmm_observation.pop(0)
matrix_ob = []
for line in hmm_observation:
    matrix_ob.append(line.split('\t'))
print(matrix_ob)

input_lines = open(testf, "r", encoding="UTF-8").read().strip().splitlines()
lines_words = []
for line in input_lines:
    temp_line = line.split(' ')
    temp_line.insert(0, '<s>')
    temp_line.append('</s>')
    lines_words.append(temp_line)
print(lines_words)

viterbi = []
for line in lines_words:
    for state in line:
        matches = []
        for obs in matrix_ob:
            if state == obs[1]:
                # get the observation entry for the word
                matches.append(obs)
        if state == '<s>':
            # if it's the BOS, ignore transition and go to the next word
            temp_array = [state, matches[0][0], float(matches[0][2])]
            viterbi.append(temp_array)
            continue
        else:
            calcs = []
            for tag in matches:
                for trans in matrix:
                    # BOS will never get here, so it will always be the first entry,
                    # so this will always compare to the domain
                    if viterbi[len(viterbi)-1][1] == trans[0] and tag[1] == trans[1]:
                        print(viterbi[len(viterbi)-1][1] +" "+ trans[0] +" & "+ tag[1] +" "+ trans[1])
                        # calculates the prob where the transition matches the backpointer with the new word
                        calc = viterbi[len(viterbi)-1][2] * float(trans[2])
                        print(calc)
                        calcs.append([calc, tag, trans])
                calcs.sort()
                #print(calcs)












