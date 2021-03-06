#Synonym recognition using WordNet
#author: Joshua Kranabetter

#Synonyms can be used to improve upon the accuracy of the FAQ part of the chatbot.
#By adding the synonyms one can answer the questions asked by the user that don’t really match the questions fed by you.
#This way, your bot can identify the intent and provide the right answer even when the question asked is not an exact match.

#-----INTSTALLATION-----
# run the following two commands to import the nltk dataset
#import nltk
#nltk.download()


from nltk.corpus import wordnet

def findSynonyms(input):
    #create array of strings for our result
    synonimousSentences = []
    wordList = input.split()
    #for each word in the sentence
    for word in wordList:
        s1 = wordList
        ind = s1.index(word)
        wordMem = word
        #for each synonym generated by wordnet
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                #remove the word we will replace with a synonym
                s1.remove(word)
                #instert the gerenated synontm
                s1.insert(ind, l.name())
                #replace the word so it can be replaced next time
                word = l.name()
                #convert back into a string
                sentence = " ".join(s1)
                #add to array of synonimous sentences
                synonimousSentences.append(sentence)
        #reset to original array
        s1.remove(word)
        s1.insert(ind, wordMem)
    #print(synonimousSentences)
    return synonimousSentences

