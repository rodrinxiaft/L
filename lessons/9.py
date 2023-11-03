#for in　リストの場合要素が順に取り出される

words = ['dog', 'cat', 'mouse']
for w in words:
    print(w, len(w))
print('finish')

str1 = 'aiueo'
for c in str1:
    print(c)

#ord関数は文字をコードにして返す　chr関数はコードを文字にして返す
print(ord('a'))
print(ord('b'))
print(ord('z'))

print(chr(97))

word = 'supercalifragilisticexpialidocious'
height = [0]*26 #0が26個ある空リストを作成
for c in word:
    height[ord(c) - ord('a')] += 1 #ord(取り出した文字) - ord('a')でaからどれだけ離れているかを調べる aなら距離0 cなら距離2 それをindexで表現し、そのindexのところに+1する　繰り返し
print(height)

import matplotlib.pyplot as plt

plt.plot(height)

#for key in dic
dic1 = {'cat': 3, 'dog': 3, 'elephant': 8}
for key in dic1:
    print('key:', key, ', value:', dic1[key]) #keyを参照しkeyに対応するvalueを取り出すのを繰り返す

for value in dic1.values():
    print('value:', value) #valueならvalueのみ取り出せる
    
for key, value in dic1.items():
    print(key) #itemsならkey/valueを同時に出せる
    
list1 = [[0, 10], [1, 20], [2, 30]]
for i, j in list1:
    print(i, j) #list tupleに対しても要素の指定と取り出しが可能
    
def reverse_lookup2(dic1):
    dic2 = {}
    for key,value in dic1.items():
        dic2[value] = key
    return dic2
        
print(reverse_lookup2({'apple': 3, 'pen': 5, 'orange': 7}) == {3: 'apple', 5: 'pen', 7: 'orange'})

#range for in の回数を指定できる for value in range(回数)

for value in range(3):
    print('hi')

#valueとは？→0からの数字
for value in range(5):
    print(value)


ln = ['e', 'd', 'a', 'c', 'f', 'b']
for value in range(len(ln)): #rangeの引数をlistの長さにしている→listの要素を全部出す
    print(ln[value]) #valueは0からの数字→indexに入れることでlistの要素を頭から順番に取り出せる
    
#range の注意点　1.引数を1つ与えると0から引数までの整数列を返す 2.引数２つだと、第一引数が起点、第二引数が終点になる 3.第三引数を与えると刻み方を変えられる　基準値は1で省略可能

s = 0
for i in range(10):
    s += i
print(s)

p = 0
for i in range(1,10,2): #0,1,2,3,4,5,6,7,8,9,から1,3,5,7,9 を取り出す
    p += i
print(p)

def sum_n(x, y):
    sum = 0
    for i in range(x,y+1):
        sum += i
    return sum

print(sum_n(1, 9))

def construct_list(int_size):
    list1 = []
    for value in range(int_size):
        list1.append(value)
    return list1
print(construct_list(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

def construct_list2(int_size):
    ln = int_size * [0] #引数分0をもったlistを作成
    for i in range(int_size):
        ln[i] = i #indexに対応するiを順に格納
    return ln
print(construct_list2(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


#forの入れ子構造
list1 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]

for i in range(4):
    for j in range(3):
        print('list1の', i + 1, '番目の要素（リスト）の', j + 1, '番目の要素 =', list1[i][j])

C = [[1]]  #listを作成
for i in range(100):
    C.append([1]+[0]*i+[1]) #作成したlistに[1]+[0]*i+[1]=[1,0,0,0…0,1]のlistを要素として追加 
    for j in range(i):
        C[i+1][j+1] = C[i][j] + C[i][j+1] #indexを用いてlist内の数字を弄り、追加したlistに代入
print(C[:10])

plt.plot(C[100])

def sum_lists(list1):
    sum = 0
    for list2 in list1:
        for i in range(len(list2)):
            sum += list2[i]
    return sum

print(sum_lists([[20, 5], [6, 16, 14, 5], [16, 8, 16, 17, 14], [1], [5, 3, 5, 7]]) == 158)

def sum_matrix(list1, list2):
    list3 = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            list3[i][j] = list1[i][j] + list2[i][j]
    return list3

print(sum_matrix([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]) == [[2, 6, 10], [6, 10, 14], [10, 14, 18]])

def sum_matrix2(list1, list2):
    list3 = [[0] * 3 for _ in range(3)]
    return [[list1[i][j] + list2[i][j] for j in range(3)] for i in range(3)]
print(sum_matrix2([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]) == [[2, 6, 10], [6, 10, 14], [10, 14, 18]])


some_list = ['dog','cat']
i = 0
for val in some_list:
    print(i, val)
    # 繰り返させたい処理
    i += 1
    
#enumerate関数を使用して簡潔に書ける　index→elementsの順に取得できる
for i, val in enumerate(some_list): #要素の順番を把握する
    # 繰り返させたい処理
    i += 1

words = ['dog','cat','mouse']
mapping = {}
for i,val in enumerate(words):
    mapping[i] = val #indexを把握しその次にvalueを取得、辞書に打ち込む
print(mapping)

#while while後の条件式がFalseを返すまで繰り返す
x = 1
total = 0
while x <= 10: #x = 10 まで足し算
    total += x
    x += 1 #１回やるごとにxを上げていく

print(x, total) #falseになった瞬間に抜けているので、x=11で終了する

#forで書くとこうなる
total1 = 0
for x in range(11):
    total1 += x

print(x, total1)

#break for while文の途中で使用可能　最も内部にある繰り返し操作を中断させる
x = 256
total = 0
while x>0:
    if total > 500:
        break
    total += x
    x = x//2
print(x,total)

def simple_match(str1, str2):
    for i in range(len(str1)-len(str2)):
        judge = str1[i:i+len(str2)]
        if judge == str2:
            return i
    return -1
print(simple_match('location', 'cat') == 2)
print(simple_match('soccer', 'cat') == -1)
print(simple_match('category', 'cat') == 0)
print(simple_match('carpet', 'cat') == -1)

def simple_match1(str1, str2): 
    for i in range(len(str1) - len(str2) + 1): #str2の文字列の長さでstr1の文字列を順に切り分けていくイメージ
        j = 0
        while j < len(str2) and str1[i + j] == str2[j]: #jがlen(str2)以下においてstr[i+j]とstr2[j]が一致していれば先に進める iはstr1の切り分けた時の最初のindexを示す
            j += 1 #次の文字の比較
        if j == len(str2): #無事に全ての一致が確認できたら、j=len(str2)でwhileを抜けてくるので、str2 = jで確認 Trueならreturnでstr1を切り取ったときの最初のindexを返す
            return i
    return -1

#continue　条件に一致した場合、一致したときの繰り返し操作を中断し次の繰り返し操作を行う
colors = ['red', 'green', 'blue', 'black', 'white']
for c in colors:
    if c == 'black': #blackになったらこいつだけ中断して次に進め
           continue
    print(c)
    
#pass文　何もしないで次に進んでくださいの意味　何かしら処理を書かないとエラーになるので、特に処理をしなくてもいいがなにか書かなきゃいけない場合に使う
x = -1
if x < 0:
    print('x is positive')
elif x == 0:
    pass #特になにかやってほしいわけではないのでpass文でお茶を濁す
elif 0 < x < 5:
    print('x is positive and smaller than 5')
else:
    print('x is positive and larger than or equal to 5')


from time import sleep

count = 0
while True:
    print('Yeah!',count)
    count +=1
    if count >= 1:
        break
    sleep(1)


def collect_engwords(str_engsentence):
    list_punctuation = [',','.','!','?',';',';']
    for i in range(len(list_punctuation)):
        str_engsentence = str_engsentence.replace(list_punctuation[i],'')
    print(str_engsentence) #引数に与えられた文字列の記号を全て空白に置き換える
    list1 = str_engsentence.split(' ') #空白で文字列を区切ってリスト化する
    print(list1)
    print(len(list1))
    list2 = []
    for j in range(len(list1)):
        if len(list1[j]) >= 3: #list1のindexを参照　長さが3以上なら空リストに追加
            list2.append(list1[j])
    return list2

print(collect_engwords('Unfortunately no, it requires something with a little more kick, plutonium.') == ['Unfortunately', 'requires','something', 'with', 'little', 'more', 'kick', 'plutonium'])

def swap_lists(ln1, ln2):
    if len(ln1) != len(ln2):
        print('要素の数が異なります')
    result_ln1 = ln1.copy()
    result_ln2 = ln2.copy()
    for i in range(1,len(ln1),2):
        result_ln1[i],result_ln2[i] = result_ln2[i],result_ln1[i]
    return (result_ln1,result_ln2)

print(swap_lists([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']) == ([1, 'b', 3, 'd', 5], ['a', 2, 'c', 4, 'e']))


def count_capitalletters(str1):
    upper_characters=set(chr(i) for i in range(65,91))
    character_count = 0
    for i in str1:
        if i in upper_characters:
            character_count += 1
    return character_count

print(count_capitalletters('Que Será, Será') == 3)

def count_capitalletters1(str1):
    int_count = 0
    for i in range(len(str1)): #str1に対して文字を１個ずつ確認する
        str2 = str1[i].upper() #indexを大文字化した文字列を作成
        str3 = str1[i].lower() #indexを小文字化した文字列を作成 
        if str1[i] == str2 and str2 != str3:#前者の条件で大文字であることを、後者の条件で句読点などでないことを判定する
            int_count += 1
    return int_count
#count_capitalletters('Que Será, Será')

def identify_codons(str_augc):
    augc_list = []
    for i in range(0,len(str_augc),3):
        augc_list.append(str_augc[i:i+3])
    return augc_list

print(identify_codons('CCCCCGGCACCT') == ['CCC', 'CCG', 'GCA', 'CCT'])


def add_commas(int1):
    list1 = list(str(int1))
    str1 = ''
    ccnt = 1
    for i in range(len(list1)-1,-1,-1): #負の数を引数に置くことで後ろから撮ってくる
        str1 =list1[i] + str1 #iは後ろから戻ってくる
        print(str1)
        if ccnt % 3 == 0 and i != 0:
            str1 = ',' + str1
        ccnt += 1
    return str1
print(add_commas(12345))


def sum_strings(list1):
    k = len(list1)
    str1 = ''
    for i in range(k):
        if list1[i] != str:
            list1[i] = str(list1[i])
    for j,item in enumerate(list1):
        if j < k-2:
            str1 += item + ', ' 
        elif j == k-2:
            str1 += item + ' and '
        else:
            str1 += item
    return str1

print(sum_strings(['a', 'b', 'c', 'd']) == 'a, b, c and d')
print(sum_strings(['a']) == 'a')
print(sum_strings([1, 2, 3]) == '1, 2 and 3')

def handle_collision2(dic1, str1):
    n = len(str1)
    for i in range(n,11):
        if dic1.get(i) == None:
            dic1[i] = str1
            return dic1
        
    for i in range(1,n):
        if dic1.get(i) == None:
            dic1[i] = str1
            return dic1

dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd'}
handle_collision2(dic1_orig, 'Big Four')
print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four'})
dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House'}
handle_collision2(dic1_orig, 'Edgware')
print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware'})
dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware', 2: 'Orient', 3: 'Three Act', 5: 'Clouds'}
handle_collision2(dic1_orig, 'ABC')
print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware', 2: 'Orient', 3: 'Three Act', 5: 'Clouds'})


def handle_collision3(dic1, str1):
    n = len(str1)
    if n not in dic1:
        dic1[n] = str1
    else:
        i = n + 1
        while True:
            if i < 10 and i not in dic1:
                dic1[i] = str1
                break
            if i >= 10 or i in dic1:
                i = 1
                i += 1
    return dic1

def handle_collision3(list1):
    dic1 = {}
    for i in range(len(list1)):
        list2 = list1[i]
        if dic1.get(list2[0]) is None:
            dic1[list2[0]] = list2[1]
    return dic1

print(handle_collision3([[3, 'Richard III'], [1, 'Othello'], [2, 'Tempest'], [3, 'King John'], [4, 'Midsummer'], [1, 'Lear']]) == {1: 'Othello', 2: 'Tempest', 3: 'Richard III', 4: 'Midsummer'})