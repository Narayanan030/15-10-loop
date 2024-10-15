def func(n):
    while True:
        num=int(input("enter 0 to stop:"))
        if num==0:
            break
        n +=num
    print(f"The total sum is: {n}")

func(0)