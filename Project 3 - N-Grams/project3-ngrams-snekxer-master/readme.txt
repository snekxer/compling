Part 1:

I had a one-liner for counting all the elements in the list of words in the file, but since its a recursive function, the huge size of lines, words & resulting calculations made it impossible to use.
Just the counting of the unigrams took more than 10 minutes to execute -- it didn't even finish, I stopped it. So I set to do it with primitive functions after talking with Will about it.
On one hand, it makes sense that primitive functions make everything more efficient; on the other, it annoys me a bit that the better way to do it turned out to be longer, which is usually the way around:
short lines of code that can accomplish that of a longer amount. If it works it works, so I can't complain much.

Part II:
I spent about 4h trying to do the bigram generator because I misunderstood the calculation (it took me like 10 minutes to complete it once I understood it).
I had to toy around with the punctuation signs indicator, as it would give false positives or not generate sentences.
The trigram generator can get into a weird loop of ' " after' ad infinitum, just as the sentences tend to start with
" -out what youthful; youths offered". In general, trigram and bigram generators are more accurate, but also require more tuning I think.
Sentences generated from bigrams make more sense than the ones from trigrams.

Part III:
Once the algorithm for perplexity was clear, implementing it was easier. It was a bit tricky seeing where the mapping had gone wrong when I got some issues with the dictionaries,
the source problem being the formatting of the model; I was using an incomplete version, and once the complete one was uploaded, it performed seamlessly (note that this is based on the
model I created, meaning that words in the n-grams are separated only by spaces and dont have the tuple structure in them). I preferred to append to the file
instead of rewriting because it allows for easy comparision between the results.

