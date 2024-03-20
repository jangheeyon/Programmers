max_num=0;
row=0; col=0;
 
for i in range(9):
    nums=list(map(int,input().split()));
 
    if(max_num<max(nums)):
        max_num=max(nums);
        row=i;
        col=nums.index(max(nums));
 
# 출력부
print(max_num);
print(row+1,col+1);