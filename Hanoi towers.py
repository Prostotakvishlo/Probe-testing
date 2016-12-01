def k(n, s, f):
    if n > 0:
        t = 6-s-f
        k(n-1, s, t)
        print(n,s,f)
        k(n-1, t, f)
k(int(input()),1,3)