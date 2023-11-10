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

print(iris_d.head(10)) #head(n);最初のn行だけを表示する
print(iris_d.index)
print(len(iris_d.index)) #.indexでindexの情報や長さを取得できる

#index指定でsliceもできる
print(iris_d[:5])
print(iris_d[-5:])

#DataFrame.列名/DataFrame['列名’]で指定した列のみを取り出せる　またこれに対してindex指定やhead指定も可能
print(iris_d['species'].head(10))
print(iris_d[['sepal_length','species']].head(10)) #列名をlistにして渡すことで複数個の列を取り出せる

#iloc[index];指定indexのcsv要素を抽出できる 行列と似ている
print(iris_d.iloc[1])
print(iris_d.iloc[1,2]) #第1indexの行の中の第2indexの要素を出した
print(iris_d.iloc[0:5, 0:2]) #1-5行の1-2列を取り出した

#loc[index,列名];指定indecの行と、指定列のデータを返す
print(iris_d.loc[5])
print(iris_d.loc[5,'sepal_length'])
print(iris_d.loc[1:5,['sepal_length','species']])

#列指定と合わせて条件を指定することで、条件にあった行からなるデータを抽出できる　条件式の演算子は and→& or→| not→~
print(iris_d[(iris_d['sepal_length'] > 7.0) & (iris_d['sepal_width'] < 3.0)]) #lengthが7以上かつwidthが3以下のデータを抽出した

#列名指定して代入すると列を追加できる
iris_d['mycolumn']=np.random.rand(len(iris_d.index)) #randomで生成された数字を列に持つmycolumn追加する
print(iris_d.head(10))

del iris_d['mycolumn'] #delで消去できる
print(iris_d.head(10))
#assignで新たなcolumnを追加したデータフレームを作成できる これは元データとは別に新たに作成されるので元データには影響はない
myiris1 = iris_d.assign(mycolumn=np.random.rand(len(iris_d.index)))
print(myiris1)
#dropでcolumnを消せる　ただし、元のデータフレームは変更されない
myiris2 = myiris1.drop('mycolumn',axis=1)
print(myiris2.head(2))

#pandas.concat([DataFrame1,DataFrame2...],keys = [arg_df1,arg_df2...]);第一引数に入れたdfを新たに行で追加できる　keysで対応する文字列を指定できる
row = pd.DataFrame([[1,1,1,1, 'setosa']], columns=iris_d.columns) #追加する行
myiris4 = pd.concat([row],keys = ['setosa'])
print(myiris4[-2:]) #appendは現在使うことができない

#sort_index();indexに基づくソートができる sort_values();任意の列の値に対するsortができる sort_index(iterable,inplace = True/False)となっていて、inplace引数にFalseを与えると新たにdfを作成してそれをsortする Trueだと元のdfをsortする
sorted_iris = iris_d.sort_values(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
print(sorted_iris) #引数に与えたlistの要素のみを表示させた
indsorted_iris = iris_d.sort_index()
print(indsorted_iris)
#降順に表示させる場合、ascending＝Falseを設定する
sorted_iris = iris_d.sort_values(['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],ascending=False)
print(sorted_iris) 

print(iris_d.describe())
