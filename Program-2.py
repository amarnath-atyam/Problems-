def odd_series(a: int):
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    return series

a = int(input("Enter a number: "))
result = odd_series(a)
print("Output:", ', '.join(map(str, result)))
