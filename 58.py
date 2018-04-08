'''
Created on Apr 8, 2018

@author: zzm
'''
def lengthOfLastWord(s):
    if(s==None):
        return 0
    lenStr=len(s)-1
    length=0
    flag=False
    while lenStr>=0:
        if(s[lenStr]!=' '):
            flag=True
            length+=1
        elif  flag:
            break
        lenStr-=1
    return length
def lengthOfLastWord1(s):
    split=s.split()
    if len(split)==0:
        return 0
    return len(split[-1])
if __name__ == '__main__':
    print lengthOfLastWord1(' ')