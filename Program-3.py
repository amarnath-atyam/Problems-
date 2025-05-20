def series(a: int):
    if a % 2 == 0:
        a -= 1
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    return series

a = int(input("Enter a number: "))
result = series(a)
print("Output:", ', '.join(map(str, result)))
