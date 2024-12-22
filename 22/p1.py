def get_nth_secret_num(secret_num, n):
    for _ in range(n):
        secret_num ^= secret_num * 64
        secret_num %= 16777216
        secret_num ^= secret_num // 32
        secret_num %= 16777216
        secret_num ^= secret_num * 2048
        secret_num %= 16777216

    return secret_num

if __name__ == "__main__":
    res = 0
    lines = open("22/i1").read().splitlines()

    for num in lines:
        res += get_nth_secret_num(int(num), 2000)

    print(res)
