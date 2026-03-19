import re
import random

def getWordList(filename):
    inFile = open(filename)
    lines = inFile.readlines()
    words = []
    pattern = re.compile(r"\b\w+\b")
    for line in lines:
        line = line.lower()
        words.extend(pattern.findall(line))
    return words

def mapWordToFollower(words):
    followers = {}
    for i in range(len(words)-1):
        followers[words[i]] = words[i+1]
    return followers

def generateTextFromFollowers(followers,n=100,initial=""):
    if not initial:
        initial = random.choice(list(followers.keys()))
    curr = initial.lower()
    text = curr + " "
    for i in range(n):
        curr = followers[curr]
        text += curr + " "
    return text

def mapWordToFollowers(words):
    followers = {}
    for i in range(len(words)-1):
        if words[i] in followers: # is the word already in the dictionary
            if not words[i+1] in followers[words[i]]: # is the following word not in the list of following words?
                followers[words[i]].append(words[i+1]) # add it to the list
        else:
            followers[words[i]] = [words[i+1]] # word is not already in dictionay - add first entry
    return followers

def generateTextFromFollowerList(followers,n=100,initial=""):
    if not initial: # create an initial word if not specified
        initial = random.choice(list(followers.keys()))
    curr = initial.lower()
    text = curr + " "
    for i in range(n):
        curr = random.choice(followers[curr]) # get a random following word
        text += curr + " "
    return text

def mapWordToFollowersWithFrequency(words):
    followers = {}
    for i in range(len(words)-1):
        if words[i] in followers: # is the word already in the dictionary
            followers[words[i]].append(words[i+1]) # add the following word again, even if it was there before, to achieve a simply indication of frequency
        else:
            followers[words[i]] = [words[i+1]] # word is not already in dictionay - add first entry
    return followers


if __name__=="__main__":
    data = "data/1Nephi.txt"
    words = getWordList(data)
    print(len(words),'\n')

    followers = mapWordToFollower(words)
    text = generateTextFromFollowers(followers,initial="Nephi")
    print(text,'\n')

    followerList = mapWordToFollowers(words)
    text = generateTextFromFollowerList(followerList,initial="Nephi")
    print(text,'\n')

    followerFrequency = mapWordToFollowersWithFrequency(words)
    text = generateTextFromFollowerList(followerFrequency,initial="Nephi")
    print(text,'\n')

    data = "data/SorcerersStone.txt"
    words = getWordList(data)
    followerFrequency = mapWordToFollowersWithFrequency(words)
    text = generateTextFromFollowerList(followerFrequency,initial="Harry")
    print(text,'\n')



