def dichuyen(fp, tp):
    print("Di chuyển từ cọc",fp, 'tới cọc', tp)
def thapHanoi(n, a, b, c):
    if n > 0:
        thapHanoi(n-1, a, c, b)
        dichuyen(a, c)
        thapHanoi(n-1 ,b, a, c)
n = int(input('Nhập n vào từ bàn phím ='))    
thapHanoi(n, "A", "B", "C")