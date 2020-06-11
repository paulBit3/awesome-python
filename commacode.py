"""Write a function that takes a list value as an argument and returns a string
with all the items separated by a comma and space, with and inserted before
the last item. example: 'apples', 'bananas', 'tofu', and 'cats'"""

def get_list(wordslist):
    # giving an empty value
    value = ''
    wordlen = len(wordslist)
    for i in range(wordlen):
        if i == wordlen - 1:
            value += ' and ' + str(wordslist[i])
            return value
        else:
            value += str(wordslist[i]) + ','


my_list = ['apples', 'bananas', 'tofu', 'cats']
word_list = get_list(my_list)
print(word_list)
# apples,bananas,tofu, and cats