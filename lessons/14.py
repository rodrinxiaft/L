#Numpy

import numpy as np
#array np.array(list,tuple)でarrayを作れる
a = np.array([1,2,3])
b = np.array((1,2,3))
print(a)
print(b) #arrayの場合listとは違い、空白で要素が区切られる

print(type(a)) #typeはnumpy.ndarrayになる

#要素型 array(arrayにしたいlist,要素型)で指定された要素型の配列を作れる

print(np.array([-1,0,1], dtype=np.int32)) #int32　整数で返す
print(np.array([-1,0,1], dtype=np.float64)) #float64　実数で返す
print(np.array([-1,0,1], dtype=np.complex128)) #complex128　複素数で返す
print(np.array([-1,0,1], dtype=np.bool_)) #bool_　0をFalseで、0以外をTrueで返す

#多次元配列　配列の中に配列がある入れ子の配列
print(np.array([[1,2],[3,4]])) #22行列
print(np.array([[1,2],[3,4],[5,6],[7,8]])) #23行列

a1 = np.array([0, 1, 2, 3, 4, 5])
a2 = a1.reshape(2,3) #15行列を23行列にする
print(a2)

a1[1] = 6 #元のarrayを変更するとreshape後の配列も変更される
print(a2)

a3 = np.array([0,1,2,3,4,5]).reshape(2,3)
print(a3)
print(a3.ravel()) #ravelで多次元配列を１次元配列に戻せる

#arange rangeのnumpy版 arange(開始値、終了値、刻み値)デフォルトの開始地は0
print(np.arange(3))
print(np.arange(0,1,0.2)) #0を開始地として0.2刻みで1までの配列を作成

#linspace 範囲を等分割した値からなる配列を生成する linspace(開始値、終了値、分割数)
print(np.linspace(0,1,3)) #3分割

#zeros;0のみからなる配列を生成する　ones;1のみからなる配列を生成する
print(np.zeros(4))
print(np.zeros((2,3))) #23行列を生成
print(np.ones(3))
print(np.ones((2,3))) #23行列を生成

#ramdom.rand;0以上1未満の乱数からなる配列を生成する
print(np.random.rand(4))
print(np.random.rand(2,3))

print(np.random.randn(5)) #randn;正規分布を調べられる
print(np.random.binomial(100,0.5,5)) #binominal;二項分布を調べられる 

def arange_square_matrix(n):
    return np.array([np.arange(i,n+i) for i in range(n)])
print(all(map(all,(arange_square_matrix(3) == np.array([[0,1,2],[1,2,3],[2,3,4]])))))

#arrayもindex参照できる　index指定した後にその要素を変更することもできる
a4 = np.arange(5)
print(a4)
print(a4[2])
a4[1] = 5
print(a4)

a5 = np.arange(6).reshape(2,3)
print(a5)
print(a5[1,2]) #多次元配列もindex指定できる　array[行index,列index]

#arrayもindexスライスできる　やり方はlistと同じ
print(a4[1:4])
print(a4[1:])
print(a4[::2])
print(a4[::-1])
#スライス代入も可能　右辺の数値をスライスで取り出したところに代入する
a4[1:4] = 6
print(a4)
#多次元配列のスライスは第一行、第二行...とスライスを指定する
print(a5)
print(a5[:2,:2])

#for文を使用することも可能
for v in np.arange(3):
    print(v)
    
for row in np.arange(8).reshape(2,4):
    print(row)

#numpy.ndeenumerate();enumerateの多次元配列版　indexと要素の組み合わせを列挙する
for idx,e in np.ndenumerate(np.arange(6).reshape(2,3)):
    print(idx,e) #(n行目,n列目)の要素 を返り値にもつ
    
#arrayの演算 array全体に演算子を用いることが可能　array+演算子で書く要素に対して処理を行える
n1 = np.arange(6)
print(n1)

print(n1 + 1)
print(n1 - 1)
print(n1 * 3)
print(n1 / 2)
print(n1 // 2)
print(n1 ** 2)

n2 = np.arange(4).reshape(2,2)
n3 = np.arange(1,5).reshape(2,2)

#多次元配列でも同様　多次元配列間の演算もできる
print(n2)
print(n3)

print(n2 + n3)
print(n2*n3)

#numpy.dot;２つのarrayをargに取り、その行列積を求める
print(np.dot(np.arange(4),np.arange(1,5))) #ベクトル内積
print(np.dot(np.arange(4).reshape(2,2),np.arange(1,5).reshape(2,2))) #行列積

#numpy.sort;arrayを昇順に並び替える sortedのarray版
a6 = np.array([3,4,1,0,-1])
print(a6)
print(np.sort(a6))

a = np.arange(6).reshape(2,3)
print(a)
print(a.sum()) #sum;要素の合計値　引数にnを設定することで、n-1行目の要素の合計値を調べられる
print(a.sum(0)) 
print(a.sum(1))

#numpy.savetxt;与えられた配列をtxtファイルにして保存する savetxt(file名,array)
np.savetxt('arange3.txt', np.arange(3))
np.savetxt('arange2x3.txt', np.arange(6).reshape(2,3)) 

#numpy.loadtxt;txtファイルにして保存した配列を呼び出せる
a = np.loadtxt('arange2x3.txt') #大規模な配列を呼び出す時はめっちゃ重くなるので、保存時に拡張子を.gzとすることで圧縮ファイルで保存できる　またloadtxtも.gzを自動的に回答してarrayを返す
print(a)
hugeArray = np.savetxt('hugeArray.gz',np.random.randint(1,1000,(100,100)))
openArray = np.loadtxt('hugeArray.gz')
print(openArray)

#真偽値配列　要素ごとに真偽値のチェックがはいる
a = np.arange(6)
print(a)
print(a < 3)

#真偽値配列はindex指定などを利用できる
a = np.array([0,1,2,-3,-4,5,-6,-7])
print(a)
print(a[a < 0]) # 負の要素を取り出し
print(a[(a < 0) & (a % 2 == 0)]) # 負で偶数の要素を取り出し
a[a < 0] = 8 # 負の要素を8に上書き
print(a)

#numpy.matmul;引数に与えた行列の行列積を求める関数
I = np.identity(3) #numpy.identity(n);nn単位行列を生成できる
print(I)
a = np.arange(9).reshape(3,3)
print(a)
print(np.matmul(a, I))