def max_sub_array(num:list[int])->tuple[int,list[int]]:
    if not num:
        return 0,[]
    max_so_far=num[0]
    current_max=num[0]
    start=end=temp=0
    for i in range(1,len(num)):
        if(num[i]>current_max+num[i]):
            current_max=num[i]
            temp=i
        else:
            current_max+=num[i]
        if current_max>max_so_far:
            max_so_far=current_max
            start=temp
            end=i
    return max_so_far,num[start:end+1]

num=[-2,1,-3,4,-1,2,1,-5,4]
max_sum,subarray=max_sub_array(num)
print(f"Maximum Sum: {max_sum}")
print(f"Subarray: {subarray}")
