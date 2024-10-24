import os, time

# Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize
# и использование модуля time для корректного отображения времени.


print ('текущий путь:',os.getcwd())


directory="."

#os.chdir(dir)
#print ('текущий путь:',os.getcwd())
#print (os.walk(dir))

#print (os.listdir(directory))

#file=[f for f in os.listdir() if os.path.isfile(f)]
#dirs=[d for d in os.listdir() if os.path.isdir(d)]
#print(dirs)
#print(file)

#os.startfile(file[0]) # применимо только для Windows

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.getcwd()
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.stat(file).st_size
    print(filesize)
    parent_dir = os.path.dirname(filepath)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
    #print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория:')