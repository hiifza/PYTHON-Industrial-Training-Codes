l1 = [1,2,3,4,5,4]
it = iter(l1)
while True:
    try:
        data = next(it)
        print(data, end=' ')
    except StopIteration as e:
        break
