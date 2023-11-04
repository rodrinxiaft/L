#関数とスコープ　ローカル変数は関数の外から参照できないが、グローバル変数ならどこでも参照できる

#グローバル変数greeting_globalの定義
greeting_global = 'Hello'

#グローバル変数greeting_globalの値を表示する関数greeting
def greeting():
    print(greeting_global)

greeting()

#グローバル変数greeting_globalを参照
print(greeting_global)

#グーローバル変数と同じ名前の変数を関数内で定義すると、関数内でのみ使用可能なローカル変数として扱われる が、混乱するのでローカル変数はちゃんと定義する
#グローバル変数greeting_globalと同じ名前の変数に値を代入する関数greeting
def greeting():
    greeting_global = 'Bonjour'
    print(greeting_global)

greeting()

#変数greeting_globalを参照
print(greeting_global)

#global 基本的に関数内ではグローバル変数は更新されないが、どうしても更新したい時に使う

#グローバル変数greeting_globalに値を代入する関数greeting
def greeting():
    global greeting_global #global宣言でglobal変数を変化
    greeting_global = 'Bonjour' #helloからbonjourに変化
    print(greeting_global)

greeting()

##変数greeting_globalを参照
print(greeting_global)

#keyword引数 実引数に何かしらの値を代入して記述することで、事前に定義した引数の順番を無視して引数を設定できる　事前に定義した引数を位置引数と言う
#文字列と数値を引数として受け取る関数greeting
def greeting(en, number, name):
    print(en*number+','+name)

#関数greetingに引数の変数名とその値の組みを渡して呼び出し
greeting(en='Hello', name='Japan', number=2)

#位置引数とキーワード引数を組み合わせた関数greetingの呼び出し　もし位置引数とkeyword引数を併用する場合、位置引数は関数で定義された通りの位置に記述する必要がある
greeting('Hello', name='Japan', number=2)

#可変長引数　仮引数の前にg*をつけて関数を定義すると、複数の引数をタプルとして受け取ることができる

def greeting(*args):
    print(args)

#可変長の引数を受け取る関数greetingに複数の引数を渡して呼び出し
greeting('Hello','Bonjour','Guten Tag')

#辞書型の場合**を仮引数の前に記述することで、辞書型引数を受け取れる
def greeting(**kwargs):
    print(kwargs)

#可変長のキーワード引数を受け取る関数greetingに複数の引数を渡して呼び出し
greeting(en='Hello', fr='Bonjour', de='Guten Tag')

#def 関数名(位置引数, 初期値を持つ引数, 可変長引数, 辞書型の可変長引数) の順番で引数を設定する必要がある
def greeting(greet, en='Hello', *args, **kwargs):
    print(greet)
    print(en)
    print(args)
    print(kwargs)
    
greeting_list = ['Bonjour']
greeting_dict = {'de': 'Guten Tag'}

greeting('Hi', 'Hello', *greeting_list, **greeting_dict)

