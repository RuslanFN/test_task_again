def read_files(file_names):
    files = {}
    for file_name in file_names:
        try:
            with open(file_name, 'r') as f:
                try:
                    files[file_name] = f.readlines()
                except IOError:
                    print(f'Ошибка чтения файла "{file_name}"')
        except:
            print(f'File "{file_name}" not found')
    return files