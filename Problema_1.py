total=int(input("Dati numarul de pasari care sunt la ferma: "))
gaini=total//2
rate=gaini//4
gaste=total-gaini-rate
print('La ferma sunt %d gaini, %d rate si %d gaste' % (gaini, rate, gaste))