#pandas asの後はpdが通例
import pandas as pd
import numpy as np

#pandasはlist,dicをSeries,DataFrameとしてオブジェクトにできる Seriesは単数の列、DataFrameは複数の列からなる indexで管理できる
#pd.Series(iterable);indexとiterableの要素をセットにして返す
s1 = pd.Series([0,1,2])
print(s1)

s2 = pd.Series(np.random.rand(3))
print(s2)

s3 = pd.Series({0:'boo',1:'hoo',2:'woo'})
print(s3)

#pd.DataFrame(iterable,index,colums); tableを作成できる　index引数を書かなかった場合は0,1,2...と自動的に振られる columsは横のラベルを指定する
d1 = pd.DataFrame([[0,1,2],[3,4,5],[6,7,8],[9,10,11]], index=[10,11,12,13], columns=['c1','c2','c3'])
print(d1)

d2 = pd.DataFrame(np.random.rand(12).reshape(4,3),columns=['c1','c2','c3'])
print(d2)
#dicの場合columsで列の順番を指定する
d3 = pd.DataFrame({'Initial':['B','F','W'], 'Name':['boo', 'foo', 'woo']},columns=['Initial','Name'])
print(d3)
d4 = pd.DataFrame({'Initial':['B','F','W'], 'Name':['boo', 'foo', 'woo']},columns=['Name','Initial']) #d3とcolumsのラベルを変えると、変えた順番にdicの取り出し方も変わる
print(d4)

#csvの処理 read_csv()でcsvを読み込みDataFrameを作成できる
iris_d = pd.read_csv('/Users/nishikata/Desktop/python_practice/examples/iris.csv')
print(iris_d)