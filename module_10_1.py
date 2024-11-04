from time import sleep
from time import time
import threading

def write_words(word_count, file_name):
    #print('1', threading.enumerate())
    #print('1', threading.current_thread())

    file = open(file_name,'w')
    for i in range(1,word_count+1):
        file.write(f'Какое-то слово № {str(i)}\n')
        sleep(0.1)
    file.close()

    return print (f'Завершилась запись в файл {file_name}')

start_time_1 = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time_1 = time()

print (f'Работа потоков {end_time_1-start_time_1}')

func_1 = write_words
func_2 = write_words
func_3 = write_words
func_4 = write_words

start_time_2 = time()

thread1 = threading.Thread (target=func_1 (10,'example5.txt'))
thread1.start()
thread1.join()

thread2 = threading.Thread (target=func_2,args=(30,'example6.txt'))
thread2.start()

thread3 = threading.Thread (target=func_3,args=(200,'example7.txt'))
thread3.start()

thread4 = threading.Thread (target=func_4,args=(100,'example8.txt'))
thread4.start()

end_time_2 = time()
print (f'Работа потоков {end_time_2-start_time_2}')
