
f = open("words.txt", "r")
words = f.read()

words_list = words.split("\n")

exclude = ["w", "a", "t", "e", "r", "h", "l", "p", "k", "i", "n", "d"]

greens = {
    '0': "",
    '1': "",
    '2': "",
    '3': "",
    '4': "s"
}

pruned_list = []
positional_list = []

#check words list and remove words that contain exclude and save to pruned_list
for word in words_list:
    if not any(char in exclude for char in word):
        pruned_list.append(word)

for i in greens:
    for word in pruned_list:
        #print(list(word)[int(i)])
        # print(word)
        # print(list(word)[int(i)])
        
        if list(word)[int(i)] == greens[i]:
            positional_list.append(word)

print(positional_list)