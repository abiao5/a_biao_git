def fun(a:int, b:int) -> int :
    num : int = 0
    for i in range(a):
        num += b
    return num


if __name__ == "__main__":
    a: int = 10
    b: int = 5
    res:int = fun(a,b)

    print(f"a x b = {res}")

