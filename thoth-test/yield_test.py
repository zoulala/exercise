# 简单例子
def g(n):
    for i in range(n):
        yield i


a = g(5)
print (a)

#print (a.next())

for i in a:
    print(i)


# 用生成器生成一个Fibonacci数列：
def fab(max):
    a,b = 0,1
    while a < max:
        yield a
        a, b = b, a+b

for i in fab(20):
    print (i,end=' ')