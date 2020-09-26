from math import log, ceil 
import collections 
def flip(c): 

    return '1' if (c == '0') else '0'
def printOneAndTwosComplement(bin): 
  
    n = len(bin)  
    ones = "" 
    twos = "" 

    for i in range(n): 
        ones += flip(bin[i])  

    ones = list(ones.strip("")) 
    twos = list(ones) 
    for i in range(n - 1, -1, -1): 
      
        if (ones[i] == '1'): 
            twos[i] = '0'
        else:          
            twos[i] = '1'
            break
  
    i -= 1    
    if (i == -1): 
        twos.insert(0, '1')  
    print("Checksum: ", *ones, sep = "") 
    return(ones)

def bin_checksum(a,b,c,d):
    integer_sum = int(a, 2) + int(b, 2)
    sum=bin(integer_sum)
    #sum_check(sum,a)
    if len(sum)>len(a):
        extra=str(sum[2])
        #sum=list(sum)
        #sum.pop[2]
        sum=int(sum,2)+int(extra,2)
        sum=bin(sum)
        sum=sum[3:]
        sum="0b"+str(sum)
        sum=int(sum,2)+int(c,2)
        sum=bin(sum)
        extra=str(sum[2])
        #sum=list(sum)
        #sum.pop[2]
        sum=int(sum,2)+int(extra,2)
        sum=bin(sum)
        sum=sum[3:]
        sum="0b"+str(sum)
        sum=int(sum,2)+int(d,2)
        sum=bin(sum)
        extra=str(sum[2])
        #sum=list(sum)
        #sum.pop[2]
        sum=int(sum,2)+int(extra,2)
        sum=bin(sum)
        sum=sum[3:]
        sum="0b"+str(sum)
        #print("Checksum",sum)
        sum=str(sum[2:])
        com=printOneAndTwosComplement(sum.strip("")) 
        print("complement checksum",com)
        comple=""
        for i in com:
            comple=comple+i
        com=str(com)
        return(a[2:]+b[2:]+c[2:]+d[2:]+str(comple))

        
def received(code):
    codeword = [int(x) for x in str(code)]
    print("Codeword  is",codeword)
 
    data=int(input("Enter the received binary sequency"))
    rec_data= [int(x) for x in str(data)]

    print("received seuqnce",rec_data)
    if collections.Counter(codeword) == collections.Counter(rec_data):
        print ("The information is correct") 
        print("Code received is",code)
        return True
    else: 
        print ("discarded information") 
        return False
def hexa_checksum():
    # Sender site
    text = input('Enter the text')
    data = []
    l = len(text)

    if l % 2 == 0:
        for i in range(0, l, 2):
            app = hex(ord(text[i])).lstrip("0x").rstrip("L") + hex(ord(text[i + 1])).lstrip("0x").rstrip("L")
            data.append(app)
    else:
        a = '00' + hex(ord(text[0])).lstrip("0x").rstrip("L")
        data.append(a)
        for i in range(1, l, 2):
            app = hex(ord(text[i])).lstrip("0x").rstrip("L") + hex(ord(text[i + 1])).lstrip("0x").rstrip("L")
            data.append(app)
    su = bin(sum(int(x, 16) for x in data))[2:]
    while len(su) > 16:
        su = bin(int(su[len(su) - 16:], 2) + int(su[:len(su) - 16], 2))[2:]
    checksum = hex(65535 - int(su, 2)).lstrip("0x").rstrip("L")

    print('checksum:', checksum)
    ed = []
    for x in data:
        ed.append(x)
    ed.append(checksum)
    print('sender side:', ed)

    # Receiver site
    print('Enter the received data in sequency')
    rd = []
    for i in range(len(ed)):
        a = input()
        if len(a) != 4:
            print('Error in received data')
            return
        rd.append(a)
    su = bin(sum(int(x, 16) for x in rd))[2:]
    while len(su) > 16:
        su = bin(int(su[len(su) - 16:], 2) + int(su[:len(su) - 16], 2))[2:]
    checksum = hex(65535 - int(su, 2)).lstrip("0x").rstrip("L")
    rdd = ''
    cordata = ''
    if len(checksum) == 0:
        print('Correct data received:')
        for x in range(len(rd)-1):
            rdd += rd[x]
        for i in range(0, len(rdd), 2):
            cordata += chr(int(rdd[i] + rdd[i + 1], 16))
        print(cordata)

    else:
        print('Error in received data')

print('1. 4 bit data\n2. Text data')
inp = int(input('Enter your choice: '))
if inp == 1:
    sender=bin_checksum("0b11001100","0b10101010","0b11110000","0b11000011")
    print("Sender side",sender)
    receiver=("1100110010101010111100001100001111010011")
    received(sender)
elif inp == 2:
    hexa_checksum()
else:
    print('Wrong choice')
