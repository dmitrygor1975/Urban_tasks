# Домашнее задание по теме "Оператор "with".

class WordsFinder:

    def __init__(self, *file_names):
        self.file_name = file_names

    def get_all_words (self):
        all_words = {}

        for i in range (len(self.file_name)):
            str_2 = str()
            with open (self.file_name[i]) as file:

                for line in file:
                    str_1 = line.lower() # все буквы в строке переводим в нижний регистр

                    chars_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - '] # убираем знаки пунктуации в строке
                    for char in chars_to_remove:
                        str_1=str_1.replace(char,'')

                    str_2+= str_1

                str_3 = str_2.split()
                all_words[self.file_name[i]]=str_3

        return all_words

    def find (self, txt):

        dict_of_words = self.get_all_words()
        result = {}

        for name, words in dict_of_words.items():
            ind=words.index(txt.lower())+1
            result.update({name: ind})
        return result

    def count(self, txt):

        dict_of_words = self.get_all_words()
        result = {}

        for name, words in dict_of_words.items():
            result.update({name:words.count(txt.lower())})
        return result

finder_1 = WordsFinder ('test_file.txt','test_file_2.txt')
#finder_1 = WordsFinder ('test_file.txt')
#finder_1 = WordsFinder ('test_file_2.txt')


print(finder_1.get_all_words()) # Все слова
print(finder_1.find('TEXT'))    # 3 слово по счёту
print(finder_1.count('teXT'))   # 4 слова teXT в тексте всего