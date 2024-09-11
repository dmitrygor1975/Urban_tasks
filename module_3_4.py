 # Модуль 3.4 СР Произвольное число параметров

def single_root_words (root_word, *other_words):
    same_words=[]

    root_word_low = root_word.lower()
   
    for i in range(len(other_words)):
        if root_word_low in other_words[i].lower(): # перебираем и приводим каждое слово из списка к нижнему регистру и ищем соответствие
            same_words.append(other_words[i])
        elif other_words[i].lower() in root_word_low: # тоже что и в пред условии, но меняем проверяемые слова местами
            same_words.append(other_words[i])
        else: continue

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print (result1)
print (result2)
