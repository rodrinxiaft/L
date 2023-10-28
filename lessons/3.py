#if文について　if もしならば　eles それ以外ならば
def bmax(a,b):
    if a>b:
        return a
    else:
        return b
#必ず:を書いて区切る　インデントによって関数が働かないので注意
print(bmax(3,5))

#関数の中でreturnが実行されたとき、その時点で関数が即座に返り値を出すので、その後の関数定義は使用されない

def bmac(a,b):
    if a>b:
        return a 
    return b
print(bmac(3,5)) #bのほうがでかいので後続のreturnが作動
print(bmac(6,3)) #aのほうがでかいので前のreturnが作動

#演算子
x =1
y =1
x == y #xとyが等しいことを示す　= だけだと代入を意味するので注意
x != y #xとyが等しくないことを示す

i = 1
j =2 
i >= 0 and j > 0   #iは0以上でかつ、jは0より大きい
i < 0 or j > 0     #iは0より小さいか、または、jは0より大きい
i == 1 or i == 2 or i ==3 #i== 1 or 2 or 3は不可能

#######################################################################################################################################
#練習  引数の絶対値を求める関数を定義する

def absolute(x):
    if x > 0:
        return x
    else:
        return -x

print(absolute(5))
print(absolute(-5))
print(absolute(0))

#練習 xが正ならば 1、負ならば -1、ゼロならば0を返す関数を定義する

def sign(x):
    if x > 0:
        return 1
    if x<0:
        return -1
    return 0

print(sign(2))
print(sign(-2))
print(sign(0))
########################################################################################################################################

#真偽値　True False

z= 3
print(z>1) #trueを返す
print(z>4) #falseを返す

def is_even(x):
    return x%2 == 0

print(is_even(3)) #関数に使用可能

def is_odd(y):
    if is_even(y): #もしis_evenが成立するならis_oddは不成立
        return False
    else:
        return True

print(is_odd(3)) #奇数なのでtrueを返す
print(is_odd(4)) #偶数なのでfalseを返す

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(10))
print(fib(2))