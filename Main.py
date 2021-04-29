################################################################################
# Will Macxy
# Hot Air Blog Scraper
# Last Updated : 4/28/2021
################################################################################

import os, os.path
import sys
import csv
import numpy
from nltk import word_tokenize
from nltk import sent_tokenize
import nltk


# Loads blogs from /SavedBlogs/ folder and turns them into a list of lists
def loadBlogs():

    blogs = []
    path, dirs, files = os.walk(sys.path[0]+'/Blogs/SavedBlogs/').__next__()


    print(path)
    for file in files:
        file = path + file

        
        with open (os.path.normpath(file), newline='',encoding='utf8') as f:
            reader=csv.reader(f, delimiter=',')
            data = list(reader)

        blogs.append(data)
    
    return(blogs)

blogs = loadBlogs()

# Creates AFINN dictionary of words and sentiment scores
def loadAfinn():

    afinn = {}
    for line in open(sys.path[0]+'/Data/AFINN-111.txt'):
        word, score = line.split('\t')
        afinn[word] = int(score)
        
    return(afinn)

# Seperates blogs into Liberal and Conservative lists
def seperateBlogs(blogs):

    count = 0
    for x in range(len(blogs)):
        if(blogs[x][0][0]) == 'L':
            
            break
        else:
            count=count+1
    return(count, blogs[:649], blogs[650:])

dividingNumber, cBlogs, lBlogs = seperateBlogs(blogs)
# Finds lexical diversity of individual blog
def lexicalDiversity(blog):
	
	sentences = word_tokenize(blog)
	lexDiv = len(set(sentences)) / len(sentences)
	
	return lexDiv


#Finds and outputs top trending PARTS OF SPEACH (POS) within headlines

def listPOS(blog, POS):
    
    occurences = []

    for titles in range(len(blog)):
        tokens = word_tokenize(blog[titles][0][1])
        #print(tokens)
        #print(nltk.pos_tag(tokens))
        for word in nltk.pos_tag(tokens):
            if word[1] == POS:
                occurences.append(word[0])
    
    freq = dict((i, occurences.count(i)) for i in set(occurences))

    freq = (dict(sorted(freq.items(), key=lambda item: item[1], reverse=True)[:40]))
    return freq

#POS tag list:
# CC	coordinating conjunction    CD	cardinal digit  # DT	determiner
# EX	existential there (like: "there is" ... think of it like "there exists")
# FW	foreign word    # IN	preposition/subordinating conjunction
# JJ	adjective	'big'   # JJR	adjective, comparative	'bigger'
# JJS	adjective, superlative	'biggest'   # LS	list marker	1)  # MD	modal	could, will
# NN	noun, singular 'desk'   # NNS	noun plural	'desks'
# NNP	proper noun, singular	'Harrison'  # NNPS	proper noun, plural	'Americans'
# PDT	predeterminer	'all the kids'  # POS	possessive ending	parent\'s
# PRP	personal pronoun	I, he, she  # PRP$	possessive pronoun	my, his, hers
# RB	adverb	very, silently, # RBR	adverb, comparative	better
# RBS	adverb, superlative	best    # RP	particle	give up # TO	to	go 'to' the store.
# UH	interjection	errrrrrrrm  # VB	verb, base form	take
# VBD	verb, past tense	took    # VBG	verb, gerund/present participle	taking
# VBN	verb, past participle	taken   # VBP	verb, sing. present, non-3d	take
# VBZ	verb, 3rd person sing. present	takes   # WDT	wh-determiner	which
# WP	wh-pronoun	who, what   # WP$	possessive wh-pronoun	whose   # WRB	wh-abverb	where, when

# use of listPOS
common = listPOS(blogs, 'NNP')


afinn = loadAfinn()
# Worker class for finding sent score
def sentScore(sentence):
    score = 0
    for word in sentence:
        if afinn.get(word) != None:
            score = score + afinn.get(word)

    return(score)

# Find sentences with biden/trump as NNP and rates their sentiment
def wordSentScore(blog, comparedWord):
    
    
    total = 0
    count = 0

    for titles in range(len(blog)):
        tokens = sent_tokenize(blog[titles][0][4])
        #print(blog[titles][0][1])
        for sentence in tokens:
            word_tokens = word_tokenize(sentence)
            for word in word_tokens:
                if comparedWord == word:
                    
                    score = sentScore(word_tokens)
                    total = total + score
                    count = count + 1

    if count != 0:
        ans = total/count
    else:
        ans = 0
    return ans


def devisiveWords():
    devisive = {}    
    for word in common.keys():
        big = 0
        lil = 0
        
        cScore = wordSentScore(cBlogs, word)
        lScore = wordSentScore(lBlogs, word)
        print('Con: ' + word + '    ' + str(cScore))
        print('Lib: ' + word + '    ' + str(lScore))
        if lScore > cScore:
            big = lScore
            lil = cScore
        else:
            big = cScore
            lil = lScore

        diff = abs(big-lil)
        print("Difference:  " + str(diff))

        devisive[word] = diff

    devisive = (dict(sorted(devisive.items(), key=lambda item: item[1], reverse=True)))
    return devisive


def sentByDate():

    dates = []
    for blog in range(len(blogs)):
        print(dates.append(blogs[blog][0][3]))
    
    print(dates)
    dates = sorted(dates)
    return

sentByDate()

#print(devisiveWords())
#for items in range(len(blogs)):
#    print(lexicalDiversity(blogs[items][0][4]))
#######################
#lexical diversity between lib and con stuff
#totalL = 0
#totalC = 0

#for items in range(len(lBlogs)):
#    totalL = totalL + lexicalDiversity(lBlogs[items][0][4])

#for items in range(len(cBlogs)):
#    totalC = totalC + lexicalDiversity(cBlogs[items][0][4])


#print(totalC/len(cBlogs))
#print(totalL/len(lBlogs))
