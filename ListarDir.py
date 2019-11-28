from os import scandir

with scandir() as dir:
    for file in dir:
        print('Nombre del archivo:', file.name)
        print('Ruta al archivo:', file.path)
        print('¿Es un directorio?', 'Sí' if file.is_dir() else 'No')
        print('¿Es un archivo?', 'Sí' if file.is_file() else 'No')
        print()
