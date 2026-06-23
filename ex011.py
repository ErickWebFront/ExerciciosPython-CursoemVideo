l = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura da parede: '))
area = l * a
print('esta parede possui uma dimensao de {}x{} e a area possui {}m2'.format(l, a, area))
tinta = area / 2
print('para pintar uma parede de {}m2 voce precisara de {}L de tinta'.format(area, tinta))