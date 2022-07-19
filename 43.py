def doctep(tentep):
    with open(tentep, mode= 'r' ) as f:
        n, m = f.readline().split()
        n = int(n)
        m = int(m)
        a = []
        for i in range(n):
            k = f.readline().split()
            for j in range(m):
                k[j] = float(k[j])
        a.append(k)
        return a,n,m

a, n, m = doctep('D:/Iris.TXT')
print(n, ' ', m)
print(a)