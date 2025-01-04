import os, time
from time import time, localtime
import multiprocessing
from multiprocessing import Pool

def read_info(name):
    all_data=[]
    file = open(name,'r')
    #print(f'открыт файл{file}')
    all_data=file.readlines()
    file.close()
    #print(f'закрыт файл{file}')


files_names = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

#start_time_1 = time()
#
#for file_name in files_names:
#    read_info (file_name)
#
#end_time_1 = time()
#print(f'Линейный вызов {(end_time_1)-(start_time_1)}')

# Многопроцессный

if __name__ == '__main__':
    start_time_2 = time()

    with Pool(4) as pool:
       pool.map (read_info,files_names)

    end_time_2 = time()
    print(f'Многопроцессный вызов {(end_time_2) - (start_time_2)}')
