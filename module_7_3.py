import pprint
word = 'tExt'

class WordsFinder:
    res = {}
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation = ',.=!?;:-'
        for filename in self.file_names:
            words = []
            clear_line = ''
            with open(filename, "r", encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    while line.find(' — ') != -1:
                        line = line.replace(' — ', " ")
                        continue
                    for char in line:
                        if not char in punctuation:
                            clear_line += char
                words = clear_line.split()
            all_words[filename] = words
            self.res.clear()
        return all_words

    def find(self, word):
        # f_dict = {}
        for names, words in self.get_all_words().items():
            place = 0
            if word.lower() in words:
                place = words.index(word.lower())+1
                self.res[names] = place
        return self.res

    def count(self, word):
        for names, words in self.get_all_words().items():
            counter = 0
            if word.lower() in words:
                counter = words.count(word.lower())
                self.res[names] = counter
        return self.res

myfinder = WordsFinder('test_file.txt')
print(myfinder.get_all_words())
print(myfinder.find(word))
print(myfinder.count(word))

#
# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'), '\n')
#
# finder2 = WordsFinder('Rudyard Kipling - If.txt',)
# print(finder2.get_all_words())
# print(finder2.find('if'))
# print(finder2.count('if'), '\n')
#
# finder3 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder3.get_all_words())
# print(finder3.find('captain'))
# print(finder3.count('captain'), '\n')
#
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# pprint.pprint(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))
