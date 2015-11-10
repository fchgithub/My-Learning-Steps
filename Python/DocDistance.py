'''
Created on Nov 10, 2015

@author: Fatemeh
'''
from __future__ import print_function

import sys 
import math

def read_file(filename):
    """ 
        Read the text file with the given filename;
        return a list of the lines of text in the file.
    """
    try:
        file = open(filename, 'r')
        text = file.read()
    except IOError:
        print ("Error opening or reading input file: {c:10s}".format(c=filename))
        sys.exit()
    return text

def getKey(item):
    return item[0].lower()

def get_word_frequency(filename):
    count = dict()
    text = read_file(filename)
    words = text.split() 
    for word in words:
        # count[word] = count.get(word, 0) + 1
        if word.lower() not in count:
            count[word.lower()] = 1
        else:
            count[word.lower()] += 1
    return count
def doc_distance(doc1_lst_of_wrd, doc2_lst_of_wrd):
    
    numerator = inner_product(doc1_lst_of_wrd, doc2_lst_of_wrd)
    denumerator = math.sqrt(inner_product(doc1_lst_of_wrd, doc1_lst_of_wrd)) * \
          math.sqrt(inner_product(doc2_lst_of_wrd, doc2_lst_of_wrd))
    
    return math.acos(numerator / denumerator)
def inner_product(l1, l2):
    """
    Inner product between two vectors, where vectors
    are represented as alphabetically sorted (word,freq) pairs.

    Example: inner_product([["and",3],["of",2],["the",5]],
                           [["and",4],["in",1],["of",1],["this",2]]) = 14.0 
    """
    shorter_list = l1 if len(l1)<len(l2) else l2
    inner_product_result = 0
    for key, val in shorter_list.items():
        if key in l2:
            inner_product_result += l2[key] * val
    print (inner_product_result)
    return inner_product_result
    
def main():
    sorted_word_list_file_1 = get_word_frequency('testFile1.txt') 
    print(sorted_word_list_file_1)
    sorted_word_list_file_2 = get_word_frequency('testFile1.txt')
    print(type(sorted_word_list_file_2))
    distance = doc_distance(sorted_word_list_file_1, sorted_word_list_file_2)
    print ('distance:  ', distance)
    
    
    
if __name__ == '__main__':
    main()
    import profile
    profile.run("main()")