def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    sum=0
    max0=0
    for i in nums:
        if i==0:
            sum=sum+1
        else:
            if max0<sum:
                max0=sum
                sum=0

    if sum>max0:
        return sum
    else:    
        return max0
        
result=maxZeros([0, 1, 0, 0]) # 得到 2
print(result)
result=maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
print(result)
result=maxZeros([1, 1, 1, 1, 1]) # 得到 0
print(result)
result=maxZeros([0, 0, 0, 1, 1]) # 得到 3
print(result)