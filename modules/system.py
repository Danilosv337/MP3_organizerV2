from os import walk
import eyed3


def get_files(way: str) -> list:
    lista = []
    for root,_, files in walk(way):
        if files == []:
            continue
        else:
            for file in files:
                ext = file[-4:]
                if ext == ".mp3":
                    lista.append((f"{root}/{file}",file))
    return lista
