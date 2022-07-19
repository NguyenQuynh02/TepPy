#ghi dl từ tiệp
def ghitep(tentep):
    with open(tentep, mode='w', encoding= 'utf-8' ) as f:
        f.write('3 5\n')
        f.write('1 3 2 5 4\n')
        f.write('3 2 5 3 6\n')
        f.write('2 3 5 4 7\n')

ghitep('D:/BAI42.TXT')


def doctep(tentep):
    with open(tentep, mode= 'r' ) as f:
        n, m = f.readline().split()
        n = int(n)
        m = int(m)
        a = []
        for i in range(n):
            k = f.readline().split()
            for j in range(m):
                k[j] = int(k[j])
        a.append(k)
        return a,n,m

ghitep('D:/BAI42.TXT')
a, n, m = doctep('D:/BAI42.TXT')
print(n, ' ', m)
print(a)
