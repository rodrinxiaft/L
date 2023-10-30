#リスト　配列のこと　JSと書き方はだいたい同じ
number = [1,2,3,4,5]
print(type(number))#リスト型として表示される
fruits = ['apple', 'banana','chelly',1,4,7]
print(fruits) #文字列をリストに格納することもできる 数字が混在していても問題ない
empty = [] #空リスト　プログラムの途中記録を記録するときとかに使う

#スライス・インデックス指定も可能
print(fruits[2]) #インデックス2のchellyが取り出された
print(fruits[1:3])
print(fruits[0:6:2])

#文字列と違いリストは代入可能
alphabet = ['a','b','c','d','e','f']
alphabet[3] = 'hello'
print(alphabet) #インデックス3にhelloが代入された

fruits[0:3] = 'x','y','z'
print(fruits) #スライスして代入も可能

#############################################################################################################################################
#練習

def remove_evenindex(ln):
    ln2 = ln[1::2]
    return ln2
print(remove_evenindex(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ['b', 'd', 'f'] )
print(remove_evenindex([1, 2, 3, 4, 5]) == [2, 4])
#############################################################################################################################################

#多重リスト　リストの要素としてリストを入れることができる 複数のインデックスを用いて多重リスト内のリストの要素を引っ張る

lns = [[1,2,3],['apple','lemmon','chelly'],[10,20,30]]
print(lns[1][0]) #多重リスト内のインデックス1のリストから、インデックス0の要素を引っ張る
print(lns[1]) #リストをそのまま取りたい時はインデックスを1個指定すればok

lns2 = [lns,[1,2,3],['x',[10,20,30]],['y',[1,2,3]]]
print(lns2)
print(lns2[0]) 

#リストに対する演算子

numbers =[0,10,20,30,40,50]
print(len(numbers)) #len len関数でリストの要素の個数を調べられる
print(max(numbers)) 
print(min(numbers))
print(sum(numbers)) #max min で最大最小を調べる　sum で合計値を調べる

#リストは演算子によって連結ができる
print(numbers + [1,2,3])
print(numbers * 3)

x = [[0.1],[2,3]]
y = x * 3
print(y) #多重リストの繰り返しの場合も同様

print(10 in numbers) #inでリスト内にその要素があるかを調べる
print(10 not in numbers) #not in も同様の扱い
a1 = 1
print(a1 == 1 or a1 == 3 or a1 == 5)
print(a1 in [1,3,7]) #or演算子が長いときに in+リストで簡潔に記述可能

print(numbers.index(10)) 
all20 = [20]*3
print(all20.count(20))

randam_numbers = [30,20,50,60,10,0,70]
randam_numbers.sort()
print(randam_numbers) #sort 並べ替えられる　引数になにも指定しないと昇順になる

numbers2 = [40,20,30,50,60,70,0,10,]
numbers2.sort(reverse = True) # 引数に reverse = True を入れることで降順になる
print(numbers2)

characters = ['e', 'd', 'a', 'c', 'f', 'b']
characters.sort()
print(characters) #文字列の場合辞書式に並べ替えられる

print(sorted(numbers)) #sortedも同じ

#sort は元のリストを変更する破壊的メソッド　sorted は新しいリストを作成し元のリストはそのままになる　sorted後のリストは変数として代入可能
numbers1 = sorted(numbers)
print('sorted関数の返値:', numbers1)

numbers2 = numbers.sort()
print('sortメソッドの返値:', numbers2) #破壊しているのでnoneが表示される

numbers.append(100)
print(numbers) #append でリストの末尾に引数を追加できる

numbers5 = [10, -10, 20, 30, -20, 40, -30]
positives = [] # 空のリストを作成する
positives.append(numbers5[0])
positives.append(numbers5[2])
positives.append(numbers5[3])
positives.append(numbers5[5]) 
print(positives) #appendで追加して条件を満たしたもののみ抽出したリストを作成する　空リストの使い方

b1 = [10,20,30,40,30]
b1.extend([100,200,300])
print(b1) #extend リストを結合する　b1 += [100,200,300] と同じ意味

b1.insert(1,1000)
print(b1) #insert で指定のインデックスに要素を挿入できる

b1.remove(10)
print(b1) #remove で引数の文字列を消去できる
b1.remove(30)
print(b1) #複数個存在する場合最初のものが消される

print(b1.pop(2))
print(b1) #popで指定したインデックスの要素を取り出すことができる
print(b1.pop()) #引数を指定しないと末尾の要素を取り出す

b2 = [10,20,30,40,50,60,]
del b2[2]
print(b2)

del b2[0:2]
print(b2) #del関数で指定したインデックスの要素を削除できる　スライス用いることも可

characters = ['e', 'd', 'a', 'c', 'f', 'b']
characters.reverse()
print(characters) 

#文字列は変更不可能だがリストは変更可能
print(list('abc123')) #ｌistで文字列をリスト化する

print('banana'.split('n'))
print('A and B and C'.split(' and ')) #split で引数に入れた文字列で区切ってリストにする
print('A   B\nC  '.split()) #引数なしの場合、連続した空白文字で区切る

#join リスト内で独立した文字を文字列にする場合はjoinを用いる　接合点に挿入する文字列.join(文字列のリスト)
print(''.join(['a', 'b', 'c', '1', '2', '3'])) #特になにも入れなくていい場合、空文字列を用いる
print('n'.join(['ba', 'a', 'a'])) 

#############################################################################################################################################
#練習
def change_domain(email, domain):
    at_index = email.index('@')
    domain_removed = email[:at_index]
    return domain_removed + '@' + domain

print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp') == 'spam@ipp.u-tokyo.ac.jp')

def change_domain1(email, domain):
    return '@'.join([email.split('@')[0], domain]) #emailを@で区切りリスト化する（本体部分とドメイン部分に分ける）→joinでバラされたものをくっつける
#index指定　email.split('@')で[本体,@以降]のリストが作成される
print('spam@utokyo-ipp.org'.split('@')) #['spam', 'utokyo-ipp.org'] このリストのインデックス0+@+domain をjoinによって実装
print(change_domain1('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp'))
#############################################################################################################################################
#タプル　変更不可能なリスト　特に変更する必要のないようなリストはタプルで設定するのが望ましい
x = 3
y = 5
point = (x, y) #()で囲むとタプルになる
print(point)
numbers3 = 1,2,3
print(numbers3) #が、囲まなくてもタプルになる

onlyone = (1,) #要素が一つの場合は(要素,) とすることでタプルにできる
onllyone1 = (1)
print(onlyone)
print(onllyone1) #これやらないと、onlyone1 = 1　と同じことになってしまう

numbers3 = (1, 2, 3)
print(numbers3[1]) # インデックスの指定による値の取得
print(len(numbers3)) # lenはタプルを構成する要素の数
print(numbers3[1:3]) # スライス

numbers3 = (1, 2, 3)
print(list(numbers3))
numbers4 = [1,2,3]
print(tuple(numbers4)) #list tupleを使うことでリストをタプルに、タプルをリストにできる
#############################################################################################################################################
#練習

def reverse_totuple(ln):
    ln.reverse()
    return tuple(ln)
print(reverse_totuple([1, 2, 3, 4, 5]) == (5, 4, 3, 2, 1))

#############################################################################################################################################
#多重代入 左辺に複数の要素を指定して、一度にタプル・リストのすべての要素に代入できる

numbersa = [0, 10, 20, 30, 40]
[a, b, c, d, e] = numbersa #a=0 b=10 c=20 d=30 e=40になる
print(b) 

a, b, c, d, e = 'hello'
print(d) #文字列に対しても使用可能　a=h b=e c=l d=l e=o
print(e)

x = 'apple'
y = 'pen'
x, y = y, x
print(x, y) #w = x; x = y; y = w と同じ結果が得られる

#for 変数 in 対象　で繰り返しを表現できる
ls = [0,1,2]

for value in ls:
    print('For loop:', value) #ls[0]がvalueに代入されて処理が実行→ls[1]がvalueに代入…→len(ls)回同じ処理をやって終了

for value in [0,1,2,3]: #リストをそのまま置いても良い　タプルを書いても良い
    print('For loop:',value)

numberArray = [0,1,2,3,4,5]
squares1 = [] #空リストを作成
for x in numberArray: #与えられたリストの要素を[0]から順に取っていく
    squares1.append(x**2) #取った要素を二乗して空リストに入れる
    
print(squares1)

#############################################################################################################################################
#練習
def sum_list(ln):
    int_sum = 0 #代入可能なように適当な数字を設定
    for x in ln: 
        int_sum += x #lnの要素を順に取り0に足していく
    return int_sum

print(sum_list([10, 20, 30]) == 60)
print(sum_list([-1, 2, -3, 4, -5]) == -3)

#############################################################################################################################################
#文字列を順に取ることも可能
str1 = 'Apple and pen'
for c in str1:
    print(c.upper())
    
def atgc_countlist(str_atgc):
    list_count = [] 
    for value in 'ATGC': #A T G Cを順番に取り出す
        int_bpcnt = str_atgc.count(value) #引数内でA,T,G,Cが何個あるか数える それを変数に格納
        list_count.append([int_bpcnt, value]) #それを空リストに格納+valueで何の文字かを表記
        #例えば一周目なら、Aを取り出す→引数内にAが何個あるか数える→リストに格納　以下繰り返し
    return list_count
print(sorted(atgc_countlist('AAGCCCCATGGTAA')) == sorted([[5, 'A'], [2, 'T'], [3, 'G'], [4, 'C']]))

#内包表記

a2 = [0,1,2,3,4,5]
a3 = []
for x in a2:
    a3.append(x**2)
print(a3)

a4 =[x**2 for x in a2]#この形で簡潔に記述できる　[x を含む式 for x in リストを返す式]
print(a4)

# == はオブジェクトの等価性を示すが、同一性は示さない
#is を用いることで同一性を確かめられる
a = []
b = []
print(a == b) #等価であるためTrueを返す []で囲まれた式を評価すると新たにオブジェクトを生成するので必ずしも同一ではない

p = [1, 2, 3]
q = p #qはpをそのまま参照しているので同じ
r = p[:]#rはｐをコピーしているので実際は異なるもの

print(a is b)

