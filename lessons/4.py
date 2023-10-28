#assert文 デバッグの際に有効 assertのあとに書いたものを真だと宣言するもの　偽の場合プログラムが中断される

def squre(x):
    return x*x

x = -2
assert squre(x) >= 0 #平方数なので必ず真になるはず

def wrong_squre(y):
    return y+y

y = -2
assert wrong_squre(y) >= 0 #関数の書き方をミスっているので停止される

def median(x, y, z):
    #xとyを入れ替えるため x = yだと複製されてしまう
    if x > y:
        w = x
        x = y
        y = w
    if z < x: #前の段階でxとyを入れ替えたので y>xの状態 x>zが証明できれば中央値がxと求まる
        return x
    if z < y: # z>xが成立しているので、y>zが証明できれば中央値がzと定まる
        return z
    return y

print(median(3,1,2))