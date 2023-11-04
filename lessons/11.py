#file ファイルから文字列を取得、書き込みが可能　opne(file)でファイルを開ける
path = '/Users/nishikata/Desktop/python_practice/lessons/a.txt'
f = open(path,'r',encoding='utf-8') #open(開きたいファイルのパス指定,mode) modeはr;読み取り w;書き込み a;追記


#readline() でファイルから１行読んで文字列で返す 返す文字列がなくなった場合、空文字列を返す
print(f.readline())
f.close()

#read() ファイル全体を読み込んで１つの文字列を取得したい時に使う
f = open(path)
print(f.read())

path2 = '/Users/nishikata/Desktop/python_practice/examples/sample.txt'
#with ファイルオブジェクト as 変数: withの後にopenしたいfileを指定、asの後に格納したいところを指定 with文は処理完了後に自動的にcloseを行ってくれる
with open(path2, 'r') as f:
    print(f.read())
#printを用いてファイルに書き込みができる　modeをwに設定すると完全に書き換える
path3 = '/Users/nishikata/Desktop/python_practice/examples/sample2.txt'
with open(path3, 'w') as f:
    print('hello\nworld', file=f)
    
#aを使うと既存の文章に追加して編集できる
with open(path3, 'a') as f:
    print('hello', 'world\n', end='', file=f) #末尾に加える文字はend引数を指定する
    
#区切りの文字はsepで指定できる
with open('print-test.txt', 'a') as f:
    print('hello', 'world', sep=', ', file=f) # 'hello, world'が印字される
    

def file_upper(infile,outfile):
    with open(infile,'r') as f:
        with open(outfile,'w') as g:
            g.write(f.read().upper())

testpath = '/Users/nishikata/Desktop/python_practice/examples/print_test.txt'
testpath2 = '/Users/nishikata/Desktop/python_practice/examples/print_test_upper.txt'

with open(testpath, 'w') as f:
    print('hello', 'world', file=f)
file_upper(testpath, testpath2)
with open(testpath2, 'r') as f:
    print(f.read() == 'HELLO WORLD\n')
    
#with文を一つにまとめることも可能
def file_upper2(infile,outfile):
    with open(infile,'r') as f , open(outfile,'w') as g:
        g.write(f.read().upper())