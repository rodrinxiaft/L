#内包表記　for分やwith文を簡潔に書ける
squares1 = []
for x in range(6):
    squares1.append(x**2)
print(squares1)
#内包表記ver
squares2 = [x**2 for x in range(6)] #実行したい処理+for文
print(squares2)

strings = ['The', 'quick', 'brown']
print([len(x) for x in strings])

str1 = '123,45,-3'
print([int(x) for x in str1.split(',')])

def var(lst):
    n = len(lst)
    ave = sum(lst)/n
    return sum([(x-ave)*(x-ave) for x in lst])/n

print(var([3,4,1,2]) == 1.25)

#内包表記をネスト化することができる
print([[x*y for y in range(x+1)] for x in range(4)]) #外側から考えるとわかりやすい　xに数値を入れた後にyに数値を入れる
print([x*y for x in range(4) for y in range(x+1)]) #x=0 y=0/x=1 y=0 x=1 y=1...

def allsubstrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
print(allsubstrings('abc'))

def sum_lists(list1):
    return sum([sum(i) for i in list1])
print(sum_lists([[20, 5], [6, 16, 14, 5], [16, 8, 16, 17, 14], [1], [5, 3, 5, 7]]) == 158)

def sum_matrix(list1,list2):
    return [[list1[i][j]+list2[i][j] for j in range(3)]for i in range(3)]
print(sum_matrix([[1,5,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]])==[[2, 9, 10], [6, 10, 14], [10, 14, 18]])

#ifも内包表記に使える
words = ['cat','dog','elephant',None,'matplotlib']
length = [len(i) for i in words if i != None]
print(length)
#dicにも使える
length_dic = {w:len(w) for w in words if w != None}
print(length_dic)

#ジェネレータ式　[]を()に書き換えればジェネレータ式になる　iteratorを構築する
it = (x*3 for x in 'abc')
for x in it:
    print(x)

print(list(x*3 for x in range(4)))
print(tuple(x*2 for x in range(4)))
print(sum(x**2 for x in range(5)))
    
    