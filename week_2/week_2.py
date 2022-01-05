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
    count=data["count"]
    employees_data=data["employees"]
    sum=0
    for n in employees_data:
        salary_list=n["salary"]
        sum=sum+salary_list
    average=sum/count
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
    max_num = max(nums)#m1是最大元素
    list_copy = nums.copy()#複製一個列表，同時不破壞原來的列表
    list_copy.remove(max_num)#把列表里最大的元素刪除
    secondmax_num = max(list_copy)#再次取列表里最大的元素，這時取到的就是列表里第二大的元素
    #m1是第二大的值,m2是最大值
    min_num = min(nums)
    list_copy = nums.copy()
    list_copy.remove(min_num)
    secondmmin_num = min(list_copy)
    #m4是第二小的值,m3是最小值
    max_sum=max_num*secondmax_num
    min_sum=min_num*secondmmin_num
    if max_sum>=min_sum:
        return max_sum
    else: return min_sum
    
    
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
    for n in (nums):
        i=target-n
        if i in (nums):
            return [(nums.index(n)),(nums.index(i))]    

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

