# **はべき乗を表す
print(7**2)

#//で整数除算、小数点切り捨ての商の値をもってくる
print(7//2) #3.5なので表示は3になる
print(7**2//3) #49/3で16を表示

# % であまりを求める
print(7**2%5) #49/5であまりは4

# 整数と実数が厳密に定められる
print(7/1) #実数表示
print(7//1) #整数表示　//は整数除算

#値が同じならtrueを返す 整数と実数が混ざったら実数値を返す
print(7/1==7//1)

#実数を整数に変換するときには　int 関数を使用　実数→整数
print(int(2.9))
print(int(-2.9))
#整数を実数に変換するときは float 関数を使用 整数→実数
print(float(2))
print(float(3))

#演算子の順序
print(17-17//3*3) #整数除算で17/3=5 5*3=15 17-15=2
print(2**2**3)
print(2**8) #先に右側のべき乗が計算される　右に結合　数式と同じ

#数学関数 import mathで数学関数を召喚　sin cos tan sqrt(平方根) pi(π)　など
import math
print(math.sqrt(2))
print(math.sqrt(3))
print(math.sin(0))

#黄金比を求める
print((math.sqrt(5)+1)/2)

