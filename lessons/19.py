#set;集合のこと
set1= {2, 1, 2, 3, 2, 3, 1, 3, 3, 1}
print(set1) #listと異なり要素の重複がない listの重複をなくしたいとき、setに変換して重複を無くした後に再度listに戻すことで重複なしlistを作成できる

set2 = set() #setメソッドでsetを作成できる
setwrong = {} #これは辞書になる
print(set2)

print(set([1,1,2,4,2,1,2,3,1]))
print(set((1,2,3,2,1,4)))
print(set('aabdceabdae'))
print(set({'apple': 1,'banana':2})) #dicをsetにした時はkeyのみ帰ってくる

#演算子も通常通りに使える
print(len(set1))
x,y,z = set1 #set1{1,2,3} よりx=1,y=2,z=3と代入した
print(x)
print(2 in set1)

def check_characters(str1):
    set_characters = set(str1)
    return len(set_characters)
print(check_characters('Onde a terra acaba e o mar começa') == 13)

def check_dicsize(dic1):
    set_characters = set(dic1)
    return len(set_characters)
print(check_dicsize({'apple': 0, 'orange': 2, 'pen': 1}) == 3)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1|set2) #set|set ; 和集合 set.union(set)も可能
print(set1.union(set2))

print(set1&set2)#set&set ; 積集合 set.intersection()も可能
print(set1.intersection(set2))

print(set1-set2) #set-set ; 差集合 set.diffetence(set)も可能
print(set1.difference(set2))

print(set1^set2) #set^set ; 対象差　どちらか一方に属している要素 set.symetric_difference(set)も可能
print(set1.symmetric_difference(set2))


print({1, 2, 3} == {1, 2, 3})
print({1, 2} != {1, 2, 3})
#<=;部分集合を調べる　>=;上位集合かを調べる　<;1つ目の集合が2つ目の集合より小さい時True
print({1, 2, 3} <= {1, 2, 3})
print({1, 2, 3} < {1, 2, 3})
print({1, 2} < {1, 2, 3})

s1 = {1,2,3,5,6,7}
s1.add(4) #add(n);nをsetに追加できる 引数は1つまで
print(s1)

s1.remove(1) #remove(n);nをsetから削除できる　要素が含まれていない場合errorとなる
print(s1)

s1.discard(2) #discard(n);nをsetから削除できる 要素が含まれていなくても普通に動く
print(s1)

s1.clear() #clear();setの要素をすべて削除できる
print(s1) 

s2 = {1,2,3,4,5}
print(s2.pop()) #pop();ランダムにsetから一つ要素を取り出す
print(s2)

def count_words2(str_engsentences):
    str1 = str_engsentences.replace(',',' ')
    str1 = str1.replace('.',' ')
    str1 = str1.replace(':',' ')
    str1 = str1.replace(';',' ')
    str1 = str1.replace('!','  ')
    str1 = str1.replace('?',' ')
    str1 = str1.split(' ')
    list1 = list(str1)
    set1 = set(list1)
    return len(set1)
print(count_words2('From Stettin in the Baltic to Trieste in the Adriatic an iron curtain has descended across the Continent.') == 15)