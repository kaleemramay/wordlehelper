
f = open("words.txt", "r")
words = f.read()

words_list = words.split("\n")

exclude = list("wetcrfm")
#exclude = ["w", "a", "t", "e", "r", "h", "l", "p", "k", "i", "n", "d"]

yellows = list("")

greens = {
    '0': "s",
    '1': "",
    '2': "a",
    '3': "l",
    '4': "l"
}

pruned_list = []
included_list = []
positional_list = []

for word in words_list:
    if not any(char in exclude for char in word):
        pruned_list.append(word)

# a loop to iterate through pruned_list
for word in pruned_list:
    include = True
    for char in yellows:
        if char not in word:
            include = False
        else:
            print(word)
    if include:
        included_list.append(word)
# print(included_list)

for word in included_list:
    addWord = True 
    for i in greens:
        if greens[i] != "":
            if  not list(word)[int(i)] == greens[i]:
                addWord = False
    if addWord == True:
        positional_list.append(word)

print(positional_list)