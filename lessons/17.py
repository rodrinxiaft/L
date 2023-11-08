#class class内に属するオブジェクトを作ることができる　メソッドを定義できる
class HelloForEver:
    def readline(self): #readline();fileから行を１つずつ読み取るmethod argは慣例としてmethod(self,arg,arg...)とする
        return 'Hello.\n'
#HelloForEverを型とするオブジェクトを生成、変数fの値となる
f = HelloForEver() #オブジェクトを生成する式をコンストラクタという

print(type(f)) #objectのtypeがHelloForEverになる　生成されたオブジェクトをクラスのインスタンスと呼ぶ
print(f)

print(f.readline()) #class内のreadlineを呼びだす

#初期化method _init_(self,arg) オブジェクトが作られた時に自動的に呼び出される

class HelloFile:
    def __init__(self,n):
        self.n = n
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n - 1
        return 'Hello.'
    
f1 = HelloFile(2) #引数はnにあたる この引数のことをオブジェクトの属性という　オブジェクトの変数と考えれば良い　self.属性名
print(f1.readline())
print(f1.n) #属性を1回消費

print(f1.readline())
print(f1.readline())
print(f1.readline()) #属性の回数だけreturn 'Hello'が実行される 属性の回数を超えると if self.n == 0となり、return ''が実行される

print(f1.n)

#継承 既存のclassをもとにして変更部分だけを与えることにより新たなclassを定義すること
class WorldFile(HelloForEver): #HelloForEverをもとにしてWorldFIleを作成 HelloForEverを親class,WorldFIleを子classと呼ぶ
    def __init__(self,n):
        self.n = n
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n-1
        return super().readline() #super();親classのmethodを呼び出すためのもの　ここでは親classのreadline()が呼び出されている  

f2 = WorldFile(3)
print(f2.readline())
print(f2.readline())
print(f2.readline())


#特殊メソッド __nnn__みたいなやつ、最初から役割が決まっている
class HelloWorldIterator(WorldFile):
    def __iter__(self): #__iter__;objectに対してiter()が呼び出される　引数をiterator化する
        return self
    def __next__(self): #objectに対して関数nextが呼び出される iteratorを進める
        line = self.readline() #文字列の呼び出し
        if line == '':
            raise StopIteration #raise;強制的にエラー文を吐くやつ
        return line
    
f3 = HelloWorldIterator(3)

print(f3 is iter(f3)) #__iter__により、f3がiteratorとなった
for line in f3: #iteratorに対してfor文を実行　属性値を上回るとraise StopIterationが作動して終了 この場合属性値が3なので3回で終わり
    print(line)


class StringFileIterator(HelloWorldIterator):
    def __init__(self, s, n):
        self.s = s
        self.n = n
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n -1
        return self.s
    
f = StringFileIterator('abc', 3)
print(list(f) == ['abc','abc','abc'])

