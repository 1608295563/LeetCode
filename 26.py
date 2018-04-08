'''
Created on Apr 8, 2018

@author: zzm
'''
def removeDuplicates(nums):
    index=1
    dupIndex=0
    if len(nums)==1:
        return 1;
    if len(nums)==0:
        return 0;
    while index<len(nums):
        if(nums[index]!=nums[dupIndex]):
            dupIndex+=1;
            nums[dupIndex]=nums[index]
        index+=1
    return dupIndex+1
if __name__ == '__main__':
    num=[1,1,3,3]
    a=removeDuplicates(num)
    print a
    print num[:a]