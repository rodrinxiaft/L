#変数の定義→　文字＝なにか　だけ

height = 188.0
weight = 60.0
bmi = weight/(height/100.0)**2 #**のほうが/より先に処理される

print(bmi)

#代入文　左辺に登場する変数が右辺に来ても良い
w = 60
w = w-10
h = 180

print(w/(h/100.0)**2)

#累積代入文　w=w-10は書き方がキモいので簡潔に書く方法がある
w -=10 # w = w-10と同義
h +=10 # h = h+10と同義

print(w/(h/100.0)**2)

#関数定義 :以降が関数の本体　引数とかはJSと同じ　returnが関数の終了を表す
def Bmi(Height, Weight):
    return Weight / (Height/100.0) ** 2 #returnの前には必ずインデントを入れておく

print(Bmi(188.0,60.0)) #呼び出しには　関数名() 引数(数字入れる)で終わり　最初に定義したbmiの値と同じ値を返している

def felt_air_temperature(temperature,humidity):
    return temperature - 1/2.3*(temperature-10)*(0.8-humidity/100)

print(felt_air_temperature(28,50))

#練習　fフィートiインチをcmに変換する関数を書く
def ft_to_cm (f,i):
    return (f + i/12)*30.48

print(ft_to_cm(5,2))

#二次関数の数値を求める関数を定義する
def quadratic(a,b,c,x):
    return a*x**2 + b*x + c

print(quadratic(1,2,1,3))
print(quadratic(1,-5,-2,7))

#ローカル変数　関数内で定義した変数は関数の外では使えない

import math

def heron(a,b,c): #ヘロンの公式
    s = (a+b+c)*0.5 #ローカル変数 関数内でsに右辺を代入してるのでこの関数内でのみ使用可能　この関数の外でsを使用しても全く別のものとして扱う
    print("The value of s is",s) #printを関数内で召喚することでローカル変数を確認できる　デバッグに便利
    return math.sqrt(s *(s-a)*(s-b)*(s-c))

print(heron(3,4,5)) #6.0を表示
# print(s) #sを定義していないのでエラー

s= 100 #関数外でsを再定義
print(heron(3,4,5))#関数内のsを使っているのでそのまま6.0を表示
print(s) #100を表示

#練習　2次方程式について
import math
#1 判別式を求める
def qe_disc(a,b,c):
    return b**2 - 4*a*c
#小さい解を求める
def qe_solution1(a,b,c):
    return  (-b - math.sqrt(b**2 - 4*a*c))/2*a
#大きい解を求める
def qe_solution2(a,b,c):
    return(-b+math.sqrt(b**2 - 4*a*c))/2*a

print(qe_solution1(1, -2, 1))
print(qe_solution2(1, -2, 1))
print(qe_solution1(1, -5, 6))
print(qe_solution2(1, -5, 6))

#グローバル変数　関数内で定義されない変数のこと（関数外で定義される変数のこと）　自由度が高く関数の内外で使用可能　便利だが扱い注意？
g=9.8 #グローバル変数 関数の外で定義している

def force(m):
    return m*g

g = g/6
print(force(104))

a = 10 #グローバル変数
def foo():
    return a
def bar():
    a = 3 #ローカル変数
    return a

print(foo()) #ここでのreturnはグローバル変数aを参照
print(a) 
print(bar()) #ここでのreturnはローカル変数aを参照