import itertools
import copy


def get_calib(test_val, nums):
    for i in range(len(nums) - 1):
        curr_ops = ["+" for _ in range(len(nums) - 1)]
        curr_ops[:i] = ["*" for _ in range(i)]
        for j in range(i-1, len(curr_ops)):
            new_ops = copy.deepcopy(curr_ops)
            if j >= i:
                new_ops[j] = "*"
            
            res = nums[0] 
            for k, op in enumerate(new_ops):
                if op == "+":
                    res += nums[k+1]
                else:
                    res *= nums[k+1]
            if res == test_val:
                return True
    return False
            
            

    return res

lines = open("i1").read().splitlines()
res = 0

for l in lines:
    test_val = int(l.split(":")[0])
    nums = l.split(":")[1]
    nums = tuple(int(n) for n in nums.strip().split(" "))
    
    valid = get_calib(test_val, nums)
    if valid:
        res += test_val

print(res) 

