#moduleのimport　JavaScriptと同じ moduleの中で複数のmethodを持つものが存在するがその時はfrom module import methodと記述する
from math import sqrt #この方法では関数ごとにimportを設定する必要がある　global valuableやclassもimportの対象になる
print(sqrt(2)) 
#import * を使うことで関数内のすべてのmethodをimportできる
#ただし、methodと同じ変数名を定義した場合、methodと変数が衝突してmethod側の処理が優先されるため非推奨
pi = 'パイ'
print(pi)
from math import *
print(pi)

#module名が長いときasを使って省略形を命名できる
import numpy
print(numpy.ones((3, 5))) # 3×5の行列を表示

import numpy as np
print(np.ones((3, 5)))

#moduleを自作してimportすることが可能
import factorial as fac
print(fac.fact(6))

from factorial import fact
print(fact(6))

from ..examples import aaa

print(aaa.sample(3))