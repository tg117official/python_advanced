def fibonacci():
    count = 0
    while True :
        yield count
        count = count + 1

val = fibonacci()

for _ in range(10):
    print(next(val))
