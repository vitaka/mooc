nombres = ['José', 'Miguel', 'Luis', 'María', 'Manuel', 'Ricardo', 'Dolores']
# Para mí, estos son los nombres que considero que no podrían existir
excluir = ['María Miguel', 'María Luis', 'María Manuel', 'María Ricardo', 'Manuel José', 'Dolores José',
           'Dolores Miguel', 'Dolores María', 'Dolores Manuell', 'Dolores Ricardo']

for i in nombres:
    for j in nombres:
        # Evito que tenga los dos nombres iguales o que componiendo ese nombre no esté en mis nombres a excluir
        if i != j and not i + ' ' + j in excluir:
            print('{0} {1}'.format(i, j))
