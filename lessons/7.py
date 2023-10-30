#条件分岐　elif elifより上に記述した式が偽でelif内に書いた式が真である時、などを表すのに使う　elseを楽に書けるようにしたもの

# if 式1:
#     ここのグループは「式1」が真のときにのみ実行される
# elif 式2:
#     ここのグループは「式1」が偽 かつ「式2」が真のときにのみ実行される
# elif 式3:
#     ここのグループは「式1」「式2」が偽 かつ「式3」が真のときにのみ実行される
# else:
#     ここのグループは「式1」「式2」「式3」がいずれも偽のときにのみ実行される

def exception3(x,y,z):
    if x == y:
        return z
    elif x == z:
        return y
    else:
        return x
print(exception3(1,2,2))
print(exception3(4,2,4))
print(exception3(9,9,3))

def exception9(a):
    x = a[0] + a[1] + a[2]
    y = a[3] + a[4] + a[5]
    z = a[6] + a[7] + a[8]
    if x==y:
        return exception3(a[6], a[7], a[8])
    elif x==z:
        return exception3(a[3], a[4], a[5])
    else:
        return exception3(a[0], a[1], a[2]) #与えられたリストを三分割　分割したものの和を求めて比較　比較して異なる値をもっているものに対して先に書いた関数を適用
    
print(exception9([1,2,2,2,2,2,2,2,2]))
print(exception9([4,4,4,4,4,2,4,4,4]))
print(exception9([9,9,9,9,9,9,9,9,3]))

def exception10(a):
    unique_element = None
    for element in a:
        if a.count(element) == 1:
            unique_element = element
            break
    return unique_element

print(exception10([1,2,2,2,2,2,2,2,2]))
print(exception10([4,4,4,4,4,2,4,4,4]))
print(exception10([9,9,9,9,9,9,9,9,3]))

x = -1  # example: 3, 0, -4

if x > 0:
    print('x is greater than zero.')
elif x < 0:
    print('x is less than zero, but x will be 0') #if elifに続く式がTrueを帰す場合　それ以降の式は実行されない
    x = 0
else:
    print('x is zero.')
    
x = 1
if 2<= x < 3:
    print('x is larger than or equal to 2, and less than 3')
elif 1<= x < 2:
    print('x is larger than or equal to 1, and less than 2')
elif x < 1:
    print('x is less than 1')
else:
    print('x is larger or equal to 3')
    
    x = -1
if x < 1:
    print('x is less than 1')
elif x < 2: #ここに来た時点で1<= が前提になっている
    print('x is larger or equal to 1, and less than 2')
elif x < 3: #2<= xが前提になっている
    print('x is larger or equal to 2, and less than 3')
else: #3<= x が前提になっている
    print('x is larger or equal to 3')
    
#三項演算子　if else は一行に収めることもできる
x = -1 
sign = 'positive or zero' if x >= 0 else 'negative'
print(sign)