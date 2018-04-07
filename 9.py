'''
Created on Apr 7, 2018

@author: zzm
'''
def  isPalindrome(x):
    y=str(x)
    i=0
    j=len(y)-1
    while i<j:
        if y[i]!=y[j]:
            return False
        i+=1
        j-=1
    return True   
if __name__=='__main__':
    print isPalindrome(-2147483648)