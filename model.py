## 快速幂运算

def fun(a :int ,b: int)-> int:
    res :int = 1
    while(b > 0):
        if (b&1):
            res *= a
        a *= a
        b >>= 1
    return res

if __name__ == "__main__":
    a :int = 2
    b :int = 10
    res :int = fun(a,b)
    print(f"a^b = {res}")
    

        