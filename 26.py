'''
Created on Apr 8, 2018

@author: zzm
'''
def removeDuplicates(nums):
    num=0
    index=1
    dupIndex=0
    if len(nums)==1:
        return 1;
    if len(nums)==0:
        return 0;
    while index<len(nums):
        if(nums[index]==nums[dupIndex]):
            index+=1
        else:
            num+=1
            dupIndex=index
            index+=1
    return num+1
if __name__ == '__main__':
    print removeDuplicates([])