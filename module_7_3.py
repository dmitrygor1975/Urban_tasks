# Домашнее задание по теме "Оператор "with".

class WordsFinder:

    def __init__(self, *file_names):
        self.file_name = file_names

    def get_all_words (self):
        all_words = {}
        str_2=str()
        for i in range (len(self.file_name)):

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


finder_1 = WordsFinder ('test_file.txt')

print(finder_1.get_all_words())