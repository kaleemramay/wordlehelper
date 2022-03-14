
f = open("words.txt", "r")
words = f.read()

words_list = words.split("\n")

exclude = list("frakon")
#exclude = ["w", "a", "t", "e", "r", "h", "l", "p", "k", "i", "n", "d"]

greens = {
    '0': "",
    '1': "m",
    '2': "e",
    '3': "",
    '4': ""
}

pruned_list = []
positional_list = []

for word in words_list:
    if not any(char in exclude for char in word):
        pruned_list.append(word)

for word in pruned_list:
    addWord = True 
    for i in greens:
        if greens[i] != "":
            if  not list(word)[int(i)] == greens[i]:
                addWord = False
    if addWord == True:
        positional_list.append(word)

print(positional_list)