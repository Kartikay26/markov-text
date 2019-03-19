import random
from collections import Counter, defaultdict

raw_text = open("sherlock1.txt").read()

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
punctuation = ".,!&"
allow_punct = True
filtered_text = ""

for c in raw_text:
    if c in alphabets:
        filtered_text += c.lower()
    elif c in punctuation and allow_punct:
        filtered_text += " " + c
    elif c.isspace():
        filtered_text += " "

words_seq = filtered_text.split()
unique_words = Counter(words_seq)

print("Total words in text:", len(words_seq))
print("Unique words in text:", len(unique_words))
print()
N = 10
print("Top %d most common words:"%N)
for x in unique_words.most_common(N):
    print(x)
print()

chain_len = 3

next_words = defaultdict(list)

for i in range(len(words_seq) - chain_len):
    cur_chain = tuple(words_seq[i:i+chain_len])
    next_word = words_seq[i+chain_len]
    next_words[cur_chain].append(next_word)

# simulate chain

def get_next_tuple(old_tuple, new_word):
    l = list(old_tuple)
    l.append(new_word)
    return tuple(l[1:])

starting_words = tuple(x.lower() for x in input("Enter %d starting words:\t"%chain_len).split())
full_text = list(starting_words)
cur_words = starting_words

for i in range(200):
    next_word = random.choice(next_words[cur_words])
    cur_words = get_next_tuple(cur_words, next_word)
    full_text.append(next_word)

full_text[0] = full_text[0].capitalize()

for i in range(len(full_text) - 1):
    if full_text[i] == ".":
        full_text[i+1] = full_text[i+1].capitalize()

result = ""

for x in full_text:
    if x in punctuation:
        result += x
    else:
        result += " "+x

print("\nGenerated text: \n")

c = 0
for x in result:
    print(x,end="")
    c += 1
    if c == 70:
        c = 0
        print()

print("\n"+"="*75)
