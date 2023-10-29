 #文字列　"""か''でくくる
word1 = "hello"
print(word1)
#type 関数によってデータ型を確認できる
print(type(word1)) #文字列なので型はstrと表示される

#str関数を用いれば、あるデータ（数字など）を文字列に変換することができる
word2 = str(123)
print(word2)
print(type(word2))#str関数によって123の整数が文字列として認識された

#int float関数を用いれば文字列を数字に変換できる
word3 = int('123')
print(word3)
print(type(word3))#int関数によって'123'という文字列が整数に変換された

word4 = float('123.4')
print(word4)
print(type(word4))#float関数によって'123,4'という文字列が実数に変換された

print(len(word1)) #lenによって文字列の長さを確認できる

#文字列とインデックス インデックスとは[]の中の数字のこと　文字列は変更不可能なので文字列を書き換えたい場合は新たに設定する必要
print("hello"[1])#文字列から任意の位置にある文字を取り出すとき　文字列+[取り出したい文字-1]　で取り出せる h だったら h[0]で取り出せる

print("hello"[-1])#インデックスに負の数を設定することで後ろから引っ張ってくる　この場合後ろから1番目のoが取られる

#スライスを用いることで文字列の任意の区間を引っ張り出すことができる
digits1='0123456789'
print(digits1[1:4]) #インデックス1から4の範囲の文字を引っ張り出した　この場合123
print(digits1[:3]) #先頭からインデックス3までの文字を引っ張り出した　先頭は省略可
print(digits1[3:]) #インデックス3から末尾までの文字を引っ張り出した　末尾も省略可

print(digits1[-4:-1]) #負の数を設定することも可能　後ろからのインデックス4から後ろからのインデックス1より小さいものを取り出した

#スライスに3番めの数字を設定することで飛び飛びに抽出することが可能
print(digits1[3:9:2]) #インデックス3からインデックス9までの数字を2おきに取り出す
print(digits1[8:4:-1]) #3番目に負の数を設定することも可能　後ろから順番に取り出す

#空文字列　文字列中からある部分の文字列を除去するときとかに使う
blank = ''
price = '2,980円'
print(price.replace(',',blank))

#in演算子　文字列がある文字列を含んでいるかどうかを調べる　返り値はtrue/false
print('lo' in 'hello') #hello に lo が含まれているかどうかを調べた　含まれているのでtrueを返す
print('z' in "hello") #hello に z が含まれているかどうか　含まれていないのでfalseを返す

substir1 = 'lo'
substir2 = 'z'
print(substir1 in word1)
print(substir2 in word1) #実際は変数を定義して使用する場合が多いかも

#not in　演算子を用いることで逆を調べられる
print(substir1 not in word1)
print(substir2 not in word1) #さっきと逆の返り値を示した

#エスケープシーケンス　文字列内で''を使用すると、文字列を作成する際の''に干渉してしまいエラーを起こす

# not_escaped = 'This is 'MINE'' エラーを吐く
# print(not_escaped)

#解消のために ''の前に\を入れる
escaped = 'This is \'MINE\''
print(escaped) 
escaped2 = '時は金なり\"Time is money\"\nTime is money\\' #\" も可能　\n は改行 \\　は \ を表示する
print(escaped2)

triple_quote_escaped = '''時は金なり
'Time is money' 
Time is money \\'''

print(triple_quote_escaped) #''' 三連続のクオートで挟むことで \n \' を使わずに表示が可能になる

#文字列の連結　文字列をくっつける・繰り返すときには演算子を用いることが可能
text1 = word1 + word2
print(text1)

text2 = word1 * 3 
print(text2) #word1を3回繰り返す

#replace 指定した文字列を別の文字に置き換える　文字列.replace(元の文字列で置き換えたい部分,置き換える文字)
print(word1.replace('l','123')) #hello の l を　123 という文字列に置き換えた

#############################################################################################################################################
#練習
def remove_punctuations(str_engsentences):
    str1 = str_engsentences.replace('.','')
    str1 = str1.replace(',', '')
    str1 = str1.replace(';','')
    str1 = str1.replace(':','')
    str1 = str1.replace('!','')
    str1 = str1.replace('?','')
    return str1

print(remove_punctuations('Quiet, uh, donations, you want me to make a donation to the coast guard youth auxiliary?') == 'Quiet uh donations you want me to make a donation to the coast guard youth auxiliary')

#練習
def atgc_bppair(str_atgc):
    str_pair = str_atgc.replace('A','t') #一旦全部小文字に変換する　最初から大文字に変換するとループみたいになってしまう
    str_pair = str_pair.replace('T','a') #AをTに変換したあとにTをAに変換することになるから、一度小文字にして避難
    str_pair = str_pair.replace('C','g')
    str_pair = str_pair.replace('G','c')
    str_pair = str_pair.upper() #最後に大文字に変換するupper関数を使用
    return str_pair

print(atgc_bppair('AAGCCCCATGGTAA') == 'TTCGGGGTACCATT')

#############################################################################################################################################
#index　指定した部分文字列が、元の文字列のどこにあるのかを検索する 文字列A.index(文字列B)　で文字列Bは文字列Aのどこにあるのかを調べることを意味する

print(word1.index('lo')) #hello の lo がどこにあるのかを調べる　lo の l　がインデックス3なので3が表示される
print(word1.index('l')) #同じ文字が複数個ある場合、最初の文字を検索する

#find も同じ使い方が可能　ただし、エラーの際にはプログラムが停止するのではなく、-1 を返り値として返す
print(word1.find('a')) #hello に a　は含まれないので -1を返した

#############################################################################################################################################
#練習
def swap_colon(str1):
    str_colon = str1.index(':') #; のインデックスを取得
    str2 = str1[:str_colon] 
    str3 = str1[str_colon + 1:] #:より前の文字列とあとの文字列を抽出　
    str4 = str3 + ':' + str2 #くっつけて完成
    return str4

print(swap_colon('hello:world') == 'world:hello')
#############################################################################################################################################

#count 文字列の中に指定した文字列がいくつ含まれているかを数え上げる
print(word1.count('l')) #hello の中に l　は２個含まれるので２を返す
print('aaaaaaaa'.count('aa'))

#############################################################################################################################################
#練習
def atgc_count(str_atgc, str_bpname):
    return str_atgc.count(str_bpname)

print(atgc_count('AAGCCCCATGGTAA', 'A') == 5)

#############################################################################################################################################

upper_dna = 'DNA'
print(upper_dna.lower()) #lower 全ての文字を小文字にする

lower_text = 'hello world!'
print(lower_text.capitalize()) #capitalize 先頭文字を大文字にする
print(lower_text.upper()) #upper 全ての文字を大文字にする

#文字列比較　辞書式で比較しているらしい　よくわからない
print('abc' <= 'abc')
print('abc' < 'abc')
print('abc' < 'abd')
print('ab' < 'abc')

#############################################################################################################################################
#練習

def check_lower(str_engsentences):
     str_judge = str_engsentences
     if str_engsentences == str_judge.lower(): 
         return True
     else:
         return False
print(check_lower('down down down') == True)
print(check_lower('There were doors all round the hall, but they were all locked') == False)


def remove_clause(str_engsentences):
    clause_index = str_engsentences.index(',')
    str_removed = str_engsentences[clause_index+2:]
    str_res = str_removed.capitalize()
    return str_res

print(remove_clause("It's being seen, but you aren't observing.") == "But you aren't observing.")