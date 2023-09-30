import sys
import math
import os
import re
import string
from math import e


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt', encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt', encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=dict()
    X= dict.fromkeys(string.ascii_uppercase, 0)

    with open(filename, encoding='utf-8') as f:
       text=f.read()
       text=text.replace(" ", "")
       text=re.findall('[A-Za-z]*', text)
       text=str(text)
       text=text.upper()
       for a in text:
           if a in X:
               X[a]=X.get(a)+1
    return X


def main():
    print("Q1")
    X=shred('letter.txt')
    for i in X:
        print(i+" "+str(X[i]))

    print("Q2")
    P = get_parameter_vectors()
    A = X.get('A')


    Q2E = A*math.log(P[0][0])
    Q2S = A*math.log(P[1][0])
    print(format(Q2E,'.4f'))
    print(format(Q2S, '.4f'))

    print("Q3")
    m=0
    n=0

    count = 0

    for v in X:
        index = P[0][count]
        m += X[v]*math.log(index)
        count = count+1

    FE= math.log(0.6)+m

    count1 = 0


    for v in X:
        index = P[1][count1]
        n += X[v] * math.log(index)
        count1 = count1 + 1

    FS = math.log(0.4) + n

    print(format(FE,'.4f'))
    print(format(FS,'.4f'))

    print("Q4")
    q4a = 1/(1+(e**(FS-FE)))
    if FS-FE >= 100:
        print("0")
    elif FS-FE<=-100:
        print("1")
    else:
        print('%.4f' % q4a)


main()

# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!
