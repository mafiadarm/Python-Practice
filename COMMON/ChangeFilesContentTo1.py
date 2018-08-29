import hashlib
import os
import random
from multiprocessing.dummy import Pool
from tqdm import tqdm

def createNewFile(file, size):
    count = 0
    with open(file, "w") as cc:
        cc.truncate() 
        while count < size:
            cc.write("\\x" + "".join(random.sample(ll, 2)))
            count = os.path.getsize(file)
            

def changeTo1(file):
    mm = hashlib.md5(file.encode()).hexdigest()
    with open(file, "a") as cc:
        cc.seek(random.randint(10000, 50000))
        cc.write(mm)

    # os.remove(file)  # delete files


if __name__ == '__main__':
    folder = input("The folder path: ")
    p = Pool()

    for folder, _, files in os.walk(folder):
        for file in tqdm(files):
            path = os.path.join(folder, file)
            p.apply_async(changeTo1, args=(path,))

    p.close()
    p.join()
