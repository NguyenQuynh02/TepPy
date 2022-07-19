#ghi dl từ tiệp
def ghitep(tentiep):
    with open(tentiep, mode='w', encoding= 'utf-8' ) as f:
        f.write('3 5\n')
        f.write('1 3 2 5 4\n')
        f.write('3 2 5 3 6\n')
        f.write('2 3 5 4 7\n')

ghitep('D:/BAI42.TXT')