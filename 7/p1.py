import itertools
from multiprocessing import Pool


def get_calib(args):
    test_val, nums = args
    n = len(nums)

    for num_mults in range(n):
        num_pluses = n - 1 - num_mults
        ops = ["*"] * num_mults + ["+"] * num_pluses
        op_perms = set(itertools.permutations(ops))

        for perm in op_perms:
            res = nums[0]
            for k, op in enumerate(perm):
                if op == "+":
                    res += nums[k + 1]
                else:
                    res *= nums[k + 1]

                if res > test_val:
                    break

            if res == test_val:
                return True
    return False

def process_line(line):
    test_val = int(line.split(":")[0])
    nums = tuple(map(int, line.split(":")[1].strip().split()))
    valid = get_calib((test_val, nums))
    return test_val if valid else 0

def main():
    # still takes forever even with a thread pool
    lines = open("7/i0").read().splitlines()

    with Pool() as pool:
        results = pool.map(process_line, lines)

    total_res = sum(results)
    print(total_res)


if __name__ == "__main__":
    main()
