def get_prices_and_diffs(secret_num, n):
    prices_and_diffs = [(secret_num % 10, None)]
    for i in range(1, n):
        secret_num ^= secret_num * 64
        secret_num %= 16777216
        secret_num ^= secret_num // 32
        secret_num %= 16777216
        secret_num ^= secret_num * 2048
        secret_num %= 16777216
        price = secret_num % 10

        prices_and_diffs.append((price, price - prices_and_diffs[i-1][0]))

    return prices_and_diffs

if __name__ == "__main__":
    res = 0
    lines = open("22/i1").read().splitlines()
    all_prices = {}

    for num in lines:
        price_tups = get_prices_and_diffs(int(num), 2001)
        price_dict = {}
        for i in range(4, len(price_tups)):

            diff_tup = (price_tups[i-3][1], price_tups[i-2][1], price_tups[i-1][1], price_tups[i][1])
            if diff_tup not in price_dict:
                price_dict[diff_tup] = price_tups[i][0]
        
        for k, v in price_dict.items():
            if k not in all_prices:
                all_prices[k] = []
            all_prices[k].append(v)

    for k, v in all_prices.items():
        res = max(res, sum(v))
    
    print(res)
    