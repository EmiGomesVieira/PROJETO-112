import os
import shutil

from_dir = "C:/Users/eg200/Downloads"
to_dir = "C:/Users/eg200/Downloads/Imagens, aula 112"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    # Verificar se a extensão está em branco
    if extension == '':
        continue

    # Verificar se a extensão é uma das extensões de documentos
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Arquivos_Documentos"
        path3 = to_dir + '/' + "Arquivos_Documentos" + '/' + file_name

        # Verificar se o diretório de destino existe
        if os.path.exists(path2):
            print("Movendo " + file_name + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo " + file_name + "...")
            shutil.move(path1, path3)
