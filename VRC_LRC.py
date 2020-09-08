import collections 
from collections import Counter
import shlex

def VRC():
    sen_data=list(input("Enter the sender binary sequency"))
    ch2=int(input("1. EVEN PARITY 2.ODD PARITY"))
    if ch2==1:
        sen_data=vrc_even_parity(sen_data)
        print("even parity encoded")
        print(sen_data)

    if ch2==2:
        sen_data=vrc_odd_parity(sen_data)
        print("odd parity encoded")
        print(sen_data)
def LRC():
    k = int(input("enter the number of squences you will input"))
    sen_data = [[1,0,1,1,0,0,1,1],[1,0,1,0,1,0,1,1],[0,1,0,1,1,0,1,0],[1,1,0,1,0,1,0,1]]

    ch2=int(input("1. EVEN PARITY 2.ODD PARITY"))
    #sen_data=sen_data1+sen_data2+sen_data3+sen_data4
    print(sen_data)
    if ch2==1:
        sen_data=lrc_even_parity(sen_data)
        print("even parity encoded")
        print(sen_data)

    if ch2==2:
        sen_data=lrc_odd_parity(sen_data)
        print("odd parity encoded")
        print(sen_data)

def checker(sen_data):
    rec_data=list(input("Enter the received binary sequency"))
    print("received seuqnce",rec_data)

    if collections.Counter(sen_data) == collections.Counter(rec_data):
        print ("The information is correct") 
        return True
    else: 
        print ("discarded information") 
        return False 
def lrc_checker(horizontal,vertical):
    row_data=list(input("Enter the received row binary sequency"))
    col_data=list(input("Enter the received column binary sequency"))

    print("received row seuqnce",row_data)
    print("received column seuqnce",col_data)


    if collections.Counter(horizontal) == collections.Counter(row_data) and collections.Counter(vertical) == collections.Counter(col_data) :
        print ("The information is correct") 
        return True
    else: 
        print ("discarded information") 
        return False
    
def hammingWeight( n):
      n = str((n))
      print(n)
      one_count = 0
      for i in n:
         if i == "1":
            one_count+=1
      return one_count

def lrc_even_parity(sen_data):
    vertical1=[]
    count1=0
    horizontal=[]
    new=[]
    print("lenggth",len(sen_data))
    #first list 
    for i in range(len(sen_data)):
        count1=hammingWeight(sen_data[i])
        if count1%2==1:
            vertical1=vertical1+["1"]
        if count1%2==0:
            vertical1=vertical1+["0"]
    print("vertical1",vertical1)

    num=len(sen_data[0])
    for i in range(num):
        new=[item[i] for item in sen_data]
        new_len=len(new)
        count1=hammingWeight(new)
        if count1%2==1:
            horizontal=horizontal+["1"]
        if count1%2==0:
            horizontal=horizontal+["0"]
    print("prininting the horizontal elements",horizontal)
    print("checking recieved sequence")
    print(lrc_checker(horizontal,vertical1))

def lrc_odd_parity(sen_data):
    vertical1=[]
    count1=0
    horizontal=[]
    new=[]
    print("lenggth",len(sen_data))
    #first list 
    for i in range(len(sen_data)):
        count1=hammingWeight(sen_data[i])
        if count1%2==1:
            vertical1=vertical1+["0"]
        if count1%2==0:
            vertical1=vertical1+["1"]
    print("vertical1",vertical1)

    num=len(sen_data[0])
    for i in range(num):
        new=[item[i] for item in sen_data]
        new_len=len(new)
        count1=hammingWeight(new)
        if count1%2==1:
            horizontal=horizontal+["0"]
        if count1%2==0:
            horizontal=horizontal+["1"]
    print("prininting the horizontal elements",horizontal)
    print("checking recieved sequence")
    print(lrc_checker(horizontal,vertical1))



def vrc_even_parity(sen_data):
    cout=0
    print("sender sequence",sen_data)
    print("lenggth",len(sen_data))
    for i in range(len(sen_data)):
        if sen_data[i]=='1':
            cout=cout+1

    if cout%2==1:
        sen_data=sen_data+["1"]
    if cout%2==0:
        sen_data=sen_data+["0"]
    print("checking recieved sequence")
    print(checker(sen_data))
    return (sen_data)
    
def vrc_odd_parity(sen_data):
    count1=0
    sen_data=list(input("Enter the sender binary sequency"))
    print("sender seuqnce",sen_data)
    num=len(sen_data[0])
    for i in range(len(sen_data)):
        if sen_data[i]=='1':
            count1=count1+1
    if count1%2==1:
        sen_data=sen_data+["0"]
    if count1%2==0:
        sen_data=sen_data+["1"]
    print("checking recieved sequence")
    print(checker(sen_data))
    return (sen_data)





print("1. VRC 2.LRC")
ch1=int(input())

str1=""
if ch1==1:
    VRC()
if ch1==2:
    LRC()
    