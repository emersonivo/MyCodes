stocks = {
    "abc": 10,
    "def": 15,
    "ghi": 9,
    "jkl": 12
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))