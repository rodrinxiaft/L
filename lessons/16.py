#高階関数;引数に関数を持つことができる関数のこと
ls = [3,-8,1,0,7,-5]
print(max(ls))
print(max(ls,key=abs)) #argにfnを渡す時は、key=fnとする　abs()は絶対値を求める関数なので、maxと合わせることで絶対値が最大となる要素を返す関数になる

#sortedも高階関数
print(sorted(ls, key=abs)) #key=absで絶対値の昇順に並び替える
#自分で関数を設定してそれを引数に渡すこともできる　invertという関数を作成して、並び替えて降順になるようにした
def invert(x):
    return -x
print(sorted(ls, key=invert))
print(sorted(ls,reverse=True)) #reverse = Trueでも同じことができる

#ラムダ式 lambda;無名関数を定義する時に使える　上のinvertのようにいちいち定義するのが面倒な場合、key=lmaba 引数:処理 とやればいちいち関数を定義しなくても一行で作成できる
print(sorted(ls,key=lambda x:-x))

#max/sortedはliterableを引数に持つ
print(max((3,-8,1,0,7,-5)))
print(sorted((3,-8,1,0,7,-5)))
print(max('hello world'))
print(sorted('hello world'))

with open('/Users/nishikata/Desktop/python_practice/examples/jugem.txt','r',encoding='utf-8') as f:
    print(max(f,key=len)) #key=lenでfile内で列の長さが最大の列を返す
    

def max_value_key(d):
    return max(d,key=lambda k:d[k])
print(max_value_key({3:10, 5:2, 9:1}) == 3)


print([abs(x) for x in [3,-8,1,0,7,-5]]) 
#map これと同様のことをmapを使って表現できる map(fn,iterable)
print(map(abs,[3,-8,1,0,7,-5])) 
for x in map(abs,[3,-8,1,0,7,-5]): #mapによりiteratorが生成される
    print(x)
print([x for x in map(abs,[3,-8,1,0,7,-5])])

def abs1(x):
    print('abs called on', x)
    return abs(x)
it = map(abs1, [3,-8,1,0,7,-5])

print(next(it)) #iteratorよりnextにより進められる

#iteratorはiterableより、mapの結果を別のmapに渡せる
print(list(map(lambda x: x+1,map(abs,[3,-8,1,0,7,-5])))) #map(abs,[3,-8,1,0,7,-5])の各要素に1を足すラムダ式関数を引数に渡す

def max_abs(ln):
    return max(map(abs,ln))
print(max_abs([3,-8,1,0,7,-5]) == 8)

#filter;高階関数でiterableをiteratorで返す
def pos(x): #正の数ならTrue,負の数ならFalseを返す関数posを定義
    if x>0:
        return True
    else:
        return False
    
print(list(filter(pos, [3,-8,1,0,7,-5]))) #filter(fn,iterable) iterableに対してfnを適用し、条件にあったものをfilterで抽出、それをlistにして返す
print([x for x in [3,-8,1,0,7,-5] if pos(x)]) #内包表現

def number_of_big_numbers(ln, n):
    return sum(map(lambda x:1,filter(lambda x:x>n,ln)))
print(number_of_big_numbers([10, 0, 7, 1, 5, 2, 9], 5) == 3)

def number_of_long_lines(file, n):
    with open(file,'r',encoding='utf-8') as f:
        return sum(map(lambda x:1,filter(lambda x:len(x)>n,f)))
    
print(number_of_long_lines('/Users/nishikata/Desktop/python_practice/examples/jugem.txt', 10) == 6)