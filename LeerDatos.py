from sys import stderr, argv


with open(argv[1], 'r', encoding='utf-8') as file:
    file.readline()
    alumnos = []
    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        fields = line.split(';')
        alumno = (fields[0], int(fields[1]), float(fields[2]))
        alumnos.append(alumno)

print(alumnos)