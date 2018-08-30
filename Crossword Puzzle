#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    #print('\n')
    #print('\n'.join([''.join(x) for x in crossword]), words)
    #print('\n')
    '''all the words are filled into the grid.'''
    if len(words) == 0:
        return crossword
    
    #print(words)
    '''iterate words, and find a place to fill each word into the grid'''
    for word in words:
        '''take a word'''
        # Row Traversal
        for r in range(10):
            _len = 0
            _c = 0
            for c in range(10):
                if crossword[r][c] != '+':
                    if _len == 0: #start
                        _len = 1
                        _c = c
                    else: #continue
                        _len += 1
                else: #encounte '+'
                    if _len > 1: #end
                        break
                    else: #reset
                        _len = 0
                        _c = 0
            #print(_len)
            if _len == len(word):
                ix = 0
                _crossword = copy.deepcopy(crossword)
                for i in range(_c, _len + _c):
                    if _crossword[r][i] == '-':
                        _crossword[r][i] = word[ix]
                    else:
                        if _crossword[r][i] != word[ix]:
                            break
                    ix += 1
                if ix == _len:
                    _words = words[:]
                    _words.remove(word)
                    #print('\n'.join([''.join(x) for x in _crossword]))
                    ret = crosswordPuzzle(_crossword, _words)
                    if ret is not None:
                        return ret
                else:
                    _crossword = copy.deepcopy(crossword)
            
        # Column Traversal
        # print('\n'.join([''.join(x) for x in crossword]))
        for c in range(10):
            _len = 0
            _r = 0
            for r in range(10):
                #print(r,c,word)
                if crossword[r][c] != '+':
                    if _len == 0:
                        _len = 1
                        _r = r
                    else:
                        _len += 1
                elif crossword[r][c] == '+':
                    if _len > 1:
                        break
                    else:
                        _len = 0
                        _r = 0
            #print(word,_r,c,_len)
            if _len == len(word):
                ix = 0
                #print(word)
                _crossword = copy.deepcopy(crossword)
                for i in range(_r, _len + _r):
                    if _crossword[i][c] == '-':
                        _crossword[i][c] = word[ix]
                    else:
                        if _crossword[i][c] != word[ix]:
                            break
                    ix += 1
                if ix == _len:
                    _words = words[:]
                    _words.remove(word)
                    #print('\n'.join([''.join(x) for x in _crossword]))
                    ret = crosswordPuzzle(_crossword, _words)
                    if ret is not None:
                        return ret
                else:
                    _crossword = copy.deepcopy(crossword)
                    #print('\n'.join([''.join(x) for x in _crossword]))
    return None          
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []
    flag = False
    for _ in range(10):
        crossword_item = input()
        if 'X' in crossword_item:
            flag = True
        crossword.append(list(crossword_item.replace('X','+')))

    words = input()
    words = words.split(';')
    result = crosswordPuzzle(crossword, words)
    if flag:
        fptr.write('\n'.join([''.join(x) for x in result]).replace('+','X'))
    else:
        fptr.write('\n'.join([''.join(x) for x in result]))
    fptr.write('\n')

    fptr.close()
