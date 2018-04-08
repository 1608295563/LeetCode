'''
Created on Apr 8, 2018

@author: zzm
'''
def plusOne(digits):
    carry=1
    result=[]
    i=len(digits)-1
    while i>=0:
        add=digits[i]+carry
        digits[i]=add%10
        carry=add/10
        i-=1
    if carry==1:
        return [1]+digits
    return digits  
if __name__ == '__main__':
    m=[9,9,9]
    print plusOne(m)