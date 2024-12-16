def get_calib(target, nums):
    n = len(nums)

    dp = [set() for _ in range(n)]

    dp[0].add(nums[0])

    for i in range(1, n):
        for val in dp[i-1]:
            new_val = val + nums[i]
            dp[i].add(new_val)

            new_val = val * nums[i]
            dp[i].add(new_val)

            new_val = int(str(val) + str(nums[i]))
            dp[i].add(new_val)
    
    return target in dp[-1]

def process_line(line):
    test_val = int(line.split(":")[0])
    nums = tuple(map(int, line.split(":")[1].strip().split()))
    valid = get_calib(test_val, nums)
    return test_val if valid else 0

lines = open("7/i1").read().splitlines()

results = [process_line(line) for line in lines]
total_res = sum(results)
print(total_res)
