import re
def applyByteStuffing(flagbyte, escapebyte, payload):

    #flagbyte = ("@")
    #escapebyte = ("A")


    x = payload.replace (escapebyte, escapebyte*2)
    y = x.replace (flagbyte, escapebyte+flagbyte)
    result=flagbyte + y + flagbyte
    print (flagbyte + y + flagbyte+" bytestuffing")
    return result;

def removebutestuffing(flagbyte,escapebyte,payload):
    y = payload.replace (escapebyte,"")
    res1=y[1:]
    result=res1[:-1]
    print(result+" unstuffed string after bytestuffing")

def applybitstuffing(payload):
    a_list = payload.split()
    map_object = map(int, a_list)
    bits = list(map_object)
    
    stuffed=[]
    count=0
    ones=max(map(len,payload.split('0')))

    flag="0"
    for j in range(ones-1):
        flag=flag+"1"
    for i in range(len(bits)):
        if bits[i]==1:
            count=count+1
            stuffed.append(bits[i])
        elif bits[i]!=1:
            count=0
            stuffed.append(bits[i])
        if count==5:
            stuffed.insert(i+1,0)
        if bits[i]==0:
            stuffed.append(bits[i])
    str1 = ''.join(str(e) for e in stuffed)
    print (flag+" "+str1+" "+flag+"bitstuffing")
    result=flag+str1+flag
    #removebitsstuffing(flag,payload)
    return(result)


def removebitstuffing(payload):
    ones=max(map(len,payload.split('0')))
    flag="0"
    count=1
    for j in range(ones-1):
        flag=flag+"1"
        count=count+1
    count=count-3
    res1=payload[count:-count]
    print(res1+" this is unstuffed")
    #x = payload.replace(flag," ")
    #print(x)



        
output1=applyByteStuffing("@", "$", "mayuri.mane18@st.niituniversity.in")
removebutestuffing("@","$",output1)
output2=applybitstuffing("0111101111")
removebitstuffing(output2)