from g2p_en import G2p
from functools import reduce
import eng_to_ipa as ipa
import pyphen

class Splitword():
    # def split_word(self,word:str):
    #     list_of_words = word.lower().split()
    #     return list_of_words

    def list_of_word(self, name:str):
        full_words = []
        lst_final_word = []
        lst_word = name.lower().split()
        g2p = G2p()
        for text in lst_word:
            out = g2p(text)
            without_digits = [reduce(lambda x, y: x+y, filter(lambda x: not x.isdigit(), s), '') for s in out]
            full_words.append(without_digits)
        for full_word in full_words:
            final_word = '-'.join(full_word)
            lst_final_word.append(final_word)
        return lst_final_word

    
    def pronouncing_word(self, first_name:str, last_name:str) ->str:

        p_first_name = self.list_of_word(name=first_name)
        p_last_name = self.list_of_word(name=last_name)

        return p_first_name, p_last_name
        # full_words_first = []
        # full_words_last = []
        # final_word = ''
        # lst_final_word = []
        # list_of_words_first = first_name.lower().split()
        # list_of_words_last = last_name.lower().split()
        # g2p = G2p()
        # for text in list_of_words_first:
        #     out = g2p(text)
        #     without_digits = [reduce(lambda x, y: x+y, filter(lambda x: not x.isdigit(), s), '') for s in out]
        #     full_words_first.append(without_digits)

        # for text in list_of_words_last:
        #     out = g2p(text)
        #     without_digits = [reduce(lambda x, y: x+y, filter(lambda x: not x.isdigit(), s), '') for s in out]
        #     full_words_last.append(without_digits)

        # for full_word in full_words:
        #     final_word = '-'.join(full_word)
        #     lst_final_word.append(final_word)
        # return lst_final_word

    def Phonetics_eng_words(self, first_name:str, last_name:str):
            first_name_lst = first_name.lower().split()
            last_name_lst = last_name.lower().split()
            legit_word_first = []
            legit_word_last = []

            for word in first_name_lst:
                first_name_ip = ipa.convert(word)
                first_name_special = first_name_ip.replace("*", "")
                if word != first_name_special:
                     legit_word_first.append(first_name_ip)
                else:
                     legit_word_first.append([])
                
            for word in last_name_lst:
                last_name_ip = ipa.convert(word)
                last_name_special=last_name_ip.replace("*", "")
                if word != last_name_special:
                     legit_word_last.append(last_name_ip)
                else:
                     legit_word_first.append([])
            
            return legit_word_first, legit_word_last

# fir, last_ = Splitword().Phonetics_eng_words(first_name="vijay jane", last_name="tomato")
# print(Splitword().pronouncing_word(first_name="vijay jane", last_name="tomato"))

# print(fir)
# print(last_)

    def split_syllables(self, word):
        dic = pyphen.Pyphen(lang='en_US')
        syllables = dic.inserted(word).split("-")
        return syllables
    
    def seperating_name(self, first_name:str, last_name:str):
         f_name = first_name.lower().strip().split()
         l_name = last_name.lower().strip().split()

         first_name_split = []
         last_name_split = []
         for first in f_name:
              split_name = self.split_syllables(first)
              split_name = "-".join(split_name)
              first_name_split.append(split_name)
         for last in l_name:
              split_name = self.split_syllables(last)
              split_name = "-".join(split_name)
              last_name_split.append(split_name)
         return first_name_split, last_name_split
         



def word_split(word:str):
     
     # Define vowels and diphthongs
    vowels = 'aeiouy'
    diphthongs = ['ai', 'au', 'ay', 'ea', 'ee', 'ei', 'ey', 'oa', 'oe', 'oi', 'ou', 'oy', 'ae']

    # Define digraphs (consonant pairs that make only one sound)
    digraphs = ['ch', 'sh', 'ph', 'th', 'wh', 'gh']

    # Define exceptions for two vowels making one sound
    one_sound_exceptions = ['oa', 'oe', 'oo', 'ou', 'ei', 'ie', 'ay', 'ey']

#     # Flag to keep track of whether we're in a diphthong
#     in_diphthong = False

    # Remove trailing silent 'e'
    if word.endswith('e'):
        word = word[:-1]

    length_of_word = len(word)
    index = 0
    while index < length_of_word:
        if length_of_word <= 5:
            print(word[index])
            print(vowels[index])
            # for letter in word:
            #     for vowel in vowels:
            #         if letter.lower() == vowel.lower():
            #                 letter_index = word.index(letter)
            #                 current_letter = letter
            #                 next_letter = word[letter_index + 1]
            #                 word_check = current_letter + next_letter
            #                 if word_check in diphthongs:
            #                     letter_index+2

#                         if word_check in digraphs:
                             
                        

                   
                   


# print(word_split(word='vijay'))
    
    
