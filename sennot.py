"""
reverses vowels in shakespeare sonnets
"""
import random
import queue
import json

def reverse(word):
    """
    reverse a wrods vowelsefj
    """
    vowels = ["a", "e", "i", "o", "u"]
    word = list(word)
    word_vowels = queue.LifoQueue(maxsize=len(word))
    for i in range(len(word)):
        if word[i] in vowels:
            word_vowels.put(word[i])
            word[i] = ' '
    for i in range(len(word)):
        if word[i] == ' ':
            word[i] = word_vowels.get()
    return ''.join(word)

def main():
    """
    fuck YOU SHAKESPEARe
    """
    with open("shake.json") as file:
        sonnets = json.load(file)
    file.close()
    son = ' '.join(random.choice(sonnets["sonnets"])["lines"])
    son = son.split()

    for i in range(len(son)):
        son[i] = reverse(son[i])
    son = " ".join(son)
    print(son)

if __name__ == '__main__':
    main()
