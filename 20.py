'''
Created on Apr 7, 2018

@author: zzm
'''
def isValid(s):
    stack=""
    for i in s:
        if i==')' or i==']' or i=='}':
            if len(stack)==0:
                return False
            else:
                flag=check(stack[len(stack)-1],i)
                if flag==False:
                    return False
                else:
                    stack=stack[:len(stack)-1]
        else:
            stack+=i
    if len(stack)==0:
        return True 
    else:
        return False
def check(x,y):
    if x=='(' and y==')':
        return True
    if x=='[' and y==']':
        return True
    if x=='{' and y=='}':
        return True
    return False
if __name__=='__main__':
    print isValid('(]')
    
