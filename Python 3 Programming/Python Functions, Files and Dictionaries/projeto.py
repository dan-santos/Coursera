punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    for c in word:
        if c in punctuation_chars:
            word = word.replace(c, '')
    return word

#---------------------------------------

# list of positive words to use

positive_words = ['happy', 'smile', 'beautiful', 'calm', 'generous',
                 'handsome', 'healing', 'wonderful', 'incredible']

def get_pos(s):
    count = 0
    words = s.split()
    for word in words:
        word = strip_punctuation(word)
        if word.lower() in positive_words:
            count += 1
    return count

with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

#----------------------------------------------

negative_words = ['bad', 'wrong', 'incorrect', 'no', 'anger', 'ungry']

def get_neg(s):
    count = 0
    words = s.split()
    for word in words:
        word = strip_punctuation(word)
        if word.lower() in negative_words:
            count += 1
    return count

with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#-------------------------------------------------------
pos = list()
neg = list()
retw = list()
repl = list()
net = list()

with open('project_twitter_data.csv', 'r') as file:
    tweets = file.readlines()
    for l in tweets[1:]:
        data = l.split(',')
        p = get_pos(data[0])
        n = -get_neg(data[0])

        pos.append(p)
        neg.append(n)

        net.append(p + n)
        retw.append(int(data[1]))
        repl.append(int(data[2]))

with open('resulting_data.csv', 'w') as f:
    f.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
    for i in range(len(net)):
        row = ','.join([str(retw[i]), str(repl[i]), str(pos[i]), str(neg[i]), str(net[i])])
        f.write(row + '\n')