def wlasne_csv(separator,lokalizacja):
    count = -1
    for count, wiersz in enumerate(open(lokalizacja, 'rU')):
        pass
    count += 1
    plik_csv = open(lokalizacja, 'r')
    lista = []
    for i in range(0, count):
        zaczytanie_linii = plik_csv.readline()
        lista.append(zaczytanie_linii.split(separator))
    lista.pop(0)
    duration = []
    for j in lista:
        duration.append(int(j[3]))
    p = len(duration)
    for d in range(0, p):
        yield(duration[d])


x = input()
y = input()
print(sum(wlasne_csv(x,y)))

def operacja(x,y):
return(x+y)