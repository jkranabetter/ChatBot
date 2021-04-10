# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:47:07 2021

@author: jkran
"""

#import the library
import wikipedia

# set language to english
wikipedia.set_lang("en")

#this function spits the user input and finds the keyword to search for, and uses 'queryword()' to return the answer
def getDefinition(input):
    wordList = input.split()
    answer = ""
    #find index of "what" and "is"
    for i in wordList:
        if i == "what":
            if (wordList[wordList.index("what") + 1] == "is"):
                #if there and an "a" in front of the definition "what is a ______"
                if ( wordList[wordList.index("what") + 2] == "a" ):
                    keyword = wordList[wordList.index("what") + 3]
                    answer = queryWord(keyword)
                    #there is no "a", its "what is _____"
                else:
                    keyword = wordList[wordList.index("what") + 2]
                    answer = queryWord(keyword)
    return answer

#this function takes a word and queries the result from wiki with error handling and disambiguation handling
def queryWord(input):
    queryResult = ""
    try:
        #query the keyword
        queryResult = wikipedia.summary(input, sentences=1)
    except wikipedia.exceptions.DisambiguationError as e:
        #if there are multiple answers to our query we choose the first one since it is usually right
        queryResult = wikipedia.summary(e.options[0], sentences=1)
    except wikipedia.exceptions.PageError:
        #return nothing if error
        return ""
    return queryResult


print(getDefinition("what is a depression?"))