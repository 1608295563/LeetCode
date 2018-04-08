'''
Created on Apr 8, 2018

@author: zzm
'''
def lengthOfLastWord(s):
    if(s==None):
        return 0;
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
if __name__ == '__main__':
    print lengthOfLastWord('   a   bbb ')