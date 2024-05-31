n = int(input(“please give input for no. of stars”))
def m():
    print(" ")
    for i in range(1, n+1):
        if i == 1 or i == n: print(f"{'*'* n}")
        else:
            for _ in range(1, n+1):
                if _ ==1 or _ == n:
                    print("*", end="")
                    if _==n:
    m()
else:
    print(" ", end="")z