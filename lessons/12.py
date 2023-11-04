#for文のinの後にfileを設定できる

lines = []
with open('/Users/nishikata/Desktop/python_practice/examples/sample3.txt', 'r') as f: #with文でfileを開いてfに格納
    for line in f: #fに対してfor文を実行
        lines.append(line)
print(lines)

#fileから行の取り出しを行うとファイルオブジェクトを消費するため、２回はできない
with open('/Users/nishikata/Desktop/python_practice/examples/sample3.txt', 'r') as f:
    print('---- 最初 ----')
    for line in f:
        print(line)
    print('---- もう一度 ----') #なにも表示されない ２回開きたい場合はもう一回openでfileを開きfileオブジェクトを生成する必要がある
    for line in f:
        print(line)
        
def last_line(name):
    with open(name,'r',encoding='utf-8') as f:
        for line in f:
            pass
    return line
print(last_line('/Users/nishikata/Desktop/python_practice/examples/sample3.txt') == 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

#for文によって参照できるデータをiterableと呼ぶ for文が繰り返し処理ができるのは、iteratorを経由するため　for文を通じなくても、iteratorを設定すれば繰り返し処理を可能にする
it = iter([1,2,3]) #iterableからiteratorを生成　iterに渡されるオブジェクトに対応したiteratorになる

#next関数でiteratorを進めることができる
print(next(it)) #1
print(next(it)) #2
print(next(it)) #3
#print(next(it))　iteratorが終了しているのにnextで進めようとするとstopiterationが作動しエラーになる

for x in [0,1,2]:
    print(x)

#これをfor文を使用しないでも書くことができる
try: #try;例外やエラーが発生する可能性のある処理を書く時に使う
    it = iter([1,2,3])
    while True:
        x = next(it) #nextでiteratorが終了しているのに進めるとerrorが発生する可能性があるためtry-exceptを使用している
        print(x)
except StopIteration: #except;例外が発生したときの処理について書く この場合Stopterationが発生したときにpassするようにしている
    pass
#for文にiteratorを繰り返すことが可能
this =iter(['aa','ii','uu'])
for x in this:
    print(x)
#ただし一回使い切りなので、一回使った場合は下のように実行されない
for x in this:
    print('これは実行されない')
    
def but_first(ls):
    it = iter(ls)
    next(it)
    return it

that = but_first([0,2,4,6,8])
print(type(that) == type(iter([]))) # type(it) では it は消費されない
print(list(that) == [2,4,6,8])
        
#iterable!=iterator 辞書やリスト、rangeはfor inで使えるのでiterableであるが、一回使い切りのiteratorではない
xs = [1,2,3] #iterableなのでforに使えるがiteratorではないので二回目のforでも使える
for x in xs:
    print(x)
for x in xs:
    print(x)

#enumerateはiteratorを返す
t = enumerate([10,20,30])
print(next(t))
for x in t:
    print(x)

for i,c in enumerate('ABCD'):
    print(i+1,'番目の文字=',c)

#enumerateはiterableを引数として受け取る　またiteratorもiterableなのでenumerateの引数にfile(iterator)を渡せる
with open('/Users/nishikata/Desktop/python_practice/examples/sample3.txt','r') as f:
    for i,s in enumerate(f):
        print(i+1,'行目')
        print(f)
