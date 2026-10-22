import random, string
dic = {
}


def dicadd(text):
    wordlist = text.split()
    count = 0
    for i in wordlist:
        count += 1
        try:
            context = (i, wordlist[count])
            if(context in dic):
                dic.get(context).append(wordlist[count+1])
            else:
                dic[context] = [wordlist[count+1]]
        except:
            print("PROBLEM")
def dicread(start, count):
    outpli = []
    word = start
    next = random.choice(dic.get(word))
    outpli = []
    outpli.append(word[0])
    outpli.append(word[1])
    context= (word[1], next)
    for i in range(count):
        word = next
        if context in dic:
            next = random.choice(dic.get(context))
        else:
            next = random.choice(list(dic))
        context = (word, next)
        outpli.append(context[0])


    return outpli
    


with open("beemovie.txt", 'r') as file:
    content = file.read()
    clean_text = content.translate(str.maketrans('', '', string.punctuation))
    clean_text = clean_text.lower()
    dicadd(clean_text)
passtup = random.choice(list(dic))
sentence = dicread(passtup, 20)
for word in sentence:
    print(f'{word} ', end="")
        

