'''
Created on Apr 8, 2018

@author: zzm
'''
def lengthOfLastWord(s):
    if(s==None):
        return 0;
    lenStr=len(s)-1
    length=0
    while lenStr>0:
        if(s[lenStr]!=' '):
            length+=1
        else :
            break
        lenStr-=1
    return length
if __name__ == '__main__':
    print lengthOfLastWord('hello ')