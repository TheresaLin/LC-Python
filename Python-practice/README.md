## `sort_dictionary.py`
**Description**: Sort the existing dictionary in defined order.

## `two_cnt_sum.py`
**Description**: It is similar to the problem in Leetcode, which is two sum. However, this problem find two sum which is not the number itself, but the count of the number. For example, the sum defined in the problem for A and B is 5. Then the list is `[A, B, A, A, B]`. The reason is that A shows up three times and B shows up two times, and sum up with five times. If I give you A and the sum is 5, then you should give me B as the answer.

## `wiki_preprocessing.py`
**Description**: From [page of wiki](https://en.wikipedia.org/wiki/Data_pre-processing), you need to list out the words without duplication in the page and remove the punctuations. Each of the results need to be stored as one line in the file of the new directory. The path would be `/sample_res/wikiwords.txt`.

## `word_classification.py`
**Description**: Still remember the output file of `wiki_preprocessing.py` which was `sample_res/wikiwords.txt`? Now, let's make a simply classification on each line of words. The simple classification separate all words to three types: one is numeric, another one is plain text, and the other one is alphanumerical. To make it clear, I would give some samples here. E.g. `-100` would be numeric, `apple` would be plain text, and `bio2` would be alphanumerical because it is the combination of number and text. Please help me to show classification result with json format. Json format would be `{"word": "numeric/plaintxt/alphanum"}`. The output should stored in `sample_res/wordclassify.json`. Good luck :)
