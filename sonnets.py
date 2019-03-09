'''This programs checks to see what words in Shakespears Sonnet are not in the dicitionary. In other words,
words that did not exists at the time or have become extinct

Additionally, it provides the opporunity to investigate how lists and dictionaries are implmented and
which is more effective'''
sonnet_words = open("sonnet_words.txt", "r")
my_words = [line.strip() for line in sonnet_words.readlines()]

dictionary_words = open("sowpods.txt", "r")
word_list = [line.strip() for line in dictionary_words.readlines()]

#a dictionary is created
word_dict = dict((line, 1) for line in word_list)


#As part of this program, I wanted to determine how long it takes for the program to complete execution in the loop
import time
counter = 0
#Start time recorded before the execution of the loop
start_time = time.time()
#for word in my_words:
#Initially, the search was done in a list. Now I am searching in a dictinioray to determine the cost of using either
for word in my_words:
    if word not in word_dict:
        print(word)
        counter += 1
#End time recorded at the end of the completion of the loop
end_time = time.time()
time_of_completion = end_time - start_time
print("Total Number of words: %d" % counter)
print("Time taken to complete loop: %.1f Seconds" % time_of_completion)

'''the length of items in a dictiionary has no effect on how long it takes a program to search
the dictionary compared to a list'''
