def minimize_loss(prices):
    n = len(prices)
    min_loss = float('inf')
    buy_year = -1
    sell_year = -1

    for i in range(n - 1):
        for j in range(i + 1, n):
            if prices[i] > prices[j]:
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year = i + 1
                    sell_year = j + 1

    if buy_year == -1:
        return "No valid buy and sell years for a loss."
    else:
        return f"Buy in year {buy_year}, sell in year {sell_year}, loss: {min_loss}"

if _name_ == "_main_":
    n = int(input("Enter number of years: "))
    prices = list(map(int, input("Enter prices separated by spaces: ").split()))
    result = minimize_loss(prices)
    print(result)
