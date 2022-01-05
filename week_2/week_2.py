def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    sum=0
    for n in range(min,max+1):
        sum=sum+n
    return sum

result=calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
print(result)
result=calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30
print(result)


def avg(data):
    # 請用你的程式補完這個函式的區塊
    x=data["count"]
    y=data["employees"]
    sum=0
    for n in y:
        z=n["salary"]
        sum=sum+z
    average=sum/x
    return average   

result=avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
    }) # 呼叫 avg 函式
print(result)



def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    m1 = max(nums)#m1是最大元素
    x2 = nums.copy()#複製一個列表，同時不破壞原來的列表
    x2.remove(m1)#把列表里最大的元素刪除
    m2 = max(x2)#再次取列表里最大的元素，這時取到的就是列表里第二大的元素
    #m1是第二大的值,m2是最大值
    m3 = min(nums)
    x2 = nums.copy()
    x2.remove(m3)
    m4 = min(x2)
    #m4是第二小的值,m3是最小值
    x=m1*m2
    y=m3*m4
    if x>=y:
        return x
    else: return y
    
    
result=maxProduct([5, 20, 2, 6]) # 得到 120
print(result)
result=maxProduct([10, -20, 0, 3]) # 得到 30
print(result)
result=maxProduct([-1, 2]) # 得到 -2
print(result)
result=result=maxProduct([-1, 0, 2]) # 得到 0
print(result)
result=maxProduct([-1, -2, 0]) # 得到 2
print(result)


def twoSum(nums, target):
    # your code here
    for x in (nums):
        y=target-x
        if y in (nums):
            return [(nums.index(x)),(nums.index(y))]    

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

