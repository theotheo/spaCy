# coding: utf8
from __future__ import unicode_literals

# import the symbols for the attrs you want to overwrite
from ...attrs import LIKE_NUM


# Overwriting functions for lexical attributes
# Documentation: https://localhost:1234/docs/usage/adding-languages#lex-attrs
# Most of these functions, like is_lower or like_url should be language-
# independent. Others, like like_num (which includes both digits and number
# words), requires customisation.


# Example: check if token resembles a number

_num_words = ['ноль', 'нуль', 'нол', 'нул'
              'один', 'одн'
              'два', 'дву',
              'три', 'тре',
              'четыре', 'четырь',
              'пять', 'пят',
              'шесть', 'шест'
              'семь', 'сем',
              'восемь', 'восьм', 'восьмь',
              'девять', 'девят',
              'десять', 'десят',
              'одинадцать', 'одинадцат',
              'двенадцать', 'двенадцат',
              'тринадцать', 'тринадцат', 
              'четырнадцать', 'четырнадцат',
              'пятнадцать', 'пятнадцат', 
              'шестнадцать', 'шестнадцат', 
              'семнадцать', 'семнадцат', 
              'восемнадцать', 'восемнадцат', 
              'девятнадцать', 'девятнадцат', 
              'двадцать', 'двадцат',
              'тридцать', 'тридцат', 
              'сорок',
              'пятьдесят', 'пятидесять', 'пятидесят',
              'шестьдесят', 'шестидесять', 'шестидесят',
              'семьдесят', 'семидесять', 'семидесят',
              'восемьдесят', 'восьмидесять', 'восьмидесят',
              'девяносто', 'девяност',
              'сто', 'ст',
              'двести', 'двухсот', 'двухстам', 'двухстами', 'двухстах', 
              'триста', 'трехсот', 'трехстам', 'трехстами', 'трехстах', 
              'четыреста', 'четырехсот', 'четырехстам', 'четырехстами', 'четырехстах',
              'пятьсот', 
              'шестьсот', 
              'семьсот', 
              'восемьсот', 
              'девятьсот', 
              'тысяча', 'тысяче', 'тысячь',
              'миллион', 
              'миллиард',
              'биллион',
              'триллион',
              'триллиард', 
              'квадриллион']

_endings = ['', 'я', 'ого', 'и', 'х', 'а', 'ю', 'у', 'ому', 'е', 'м', 'ем', 'им', 'ми', 'мя', 'й', 'е', 'ом']

_num_words_forms = []
for i in _num_words:
  for j in _endings:
    _num_words_forms.append(i + j)

def like_num(text):
    text = text.replace(',', '').replace('.', '')
    if text.isdigit():
        return True
    if text.count('/') == 1:
        num, denom = text.split('/')
        if num.isdigit() and denom.isdigit():
            return True
    if text in _num_words_forms:
        return True
    return False


# Create dictionary of functions to overwrite. The default lex_attr_getters are
# updated with this one, so only the functions defined here are overwritten.

LEX_ATTRS = {
    LIKE_NUM: like_num
}
