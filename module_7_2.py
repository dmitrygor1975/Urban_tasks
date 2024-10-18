
def custom_write(file_name, strings):
    strings_positions = {}

    #file = open (file_name,'a', encoding="utf-8")
    file = open (file_name,'a')

    for i in range(len(strings)):
        str_number = i+1
        position = file.tell()
        file.write(f'{strings[i]}\n')
        elem = {(str_number,position):strings[i]}
        strings_positions.update(elem)

    file.close()

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
        ]

result = custom_write('text.txt',info)


for elem in result.items():
  print(elem)

#print(result)