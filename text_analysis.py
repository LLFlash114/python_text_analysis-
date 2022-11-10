# Importing passages and string modules 

from data.passage01 import text as passage0
from data.passage02 import text as passage1
import string 

text1 = passage0.text.lower()
text2 = passage1.text.lower()

# This function turns punctuations into spaces 

def list_punc(text):
    punctuation = string.punctuation

    for i in text:
        if i in punctuation:
            text = text.replace(i, ' ')
    return text

# Function that finds the common words between two strings

def common_words(text1,text2):
    text1 = list_punc(text1).split()
    text2 = list_punc(text2).split()
    common_words = []
    common_words1 = []
    for i in text1:
        if i in text2:
            if i not in common_words1:
                common_words.append(i)
    common_sorted_list = sorted(common_words)
    return common_sorted_list
# For loop that removes duplicates
    # for i in common_words:
    #     if i not in common_words1:
    #         common_words1.append(i) 
    # common_sorted_list = sorted(common_words1)
    # return common_sorted_list

# Function that outputs the number of times a user inputted word appears in the passages  

def count_word(word):
    text1 = list_punc(passage0.text).split()
    test2 = list_punc(passage1.text).split()
    passage1_count = passage0.text.count(word)
    passage2_count = passage1.text.count(word)
    return f"'{word}' appears {passage1_count} times in passage 0" and f"'{word}' appears {passage1_count} times in passage 0"

# Function that converts list into dictionary of frequent values 
def frequent_words_dict(text):
    text = list_punc(text).split()
    freq = {}
    for i in text:
        freq.setdefault(i, 0)
        freq[i] = freq[i] + 1
    return freq

def dict_count_first(text):
    words_first = frequent_words_dict(text)
    freq_words_dict = {}
    for i, freq in words_first.items():
        if freq in freq_words_dict:
            freq_words_dict[freq].append(i)
        else:
            freq_words_dict[freq] = [i]

    return freq_words_dict

    

def dict_to_sorted_tuple(text):
    text = dict_count_first(text)
    sorted_tuple = sorted(text.items(), reverse = True)
    return sorted_tuple

def most_frequent_slice(text):
    frequent_words = dict_to_sorted_tuple(text)
    frequent_words = frequent_words[0:5]
    return frequent_words

def frequent_letters_dict(text):
    text = list_punc(text)
    freq = {}
    for i in text:
        freq.setdefault(i, 0)
        freq[i] = freq[i] + 1
    return freq

def dict_count_letters_first(text):
    letters_first = frequent_letters_dict(text)
    freq_letters_dict = {}
    for i, freq in letters_first.items():
        if freq in freq_letters_dict:
            freq_letters_dict[freq].append(i)
        else:
            freq_letters_dict[freq] = [i]

    return freq_letters_dict

def letter_dict_tuple(text):
    text = dict_count_letters_first(text)
    sorted_letter_tuple = sorted(text.items(), reverse = True)
    return sorted_letter_tuple

def frequent_letters_slice(text):
    text = letter_dict_tuple(text)
    text = text[0:5]
    return text

print(frequent_letters_slice(text1))











# print(common_words(text1,text2))
# word = input('Enter a word to find the frequency of: ')
# print(count_word(word))








        
