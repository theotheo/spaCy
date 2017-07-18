# encoding: utf8
from __future__ import unicode_literals


# Add stop words
# Documentation: https://spacy.io/docs/usage/adding-languages#stop-words
# To improve readability, words should be ordered alphabetically and separated
# by spaces and newlines. When adding stop words from an online source, always
# include the link in a comment. Make sure to proofread and double-check the
# words – lists available online are often known to contain mistakes.

STOP_WORDS = set("""
а

без более бы был была были было будет будем будете буду будут

в вам вами вас ведь во вот все всего всем всеми всему всех вы

да даже для до

ее ей его ему если есть еще

же

за

и из или им именно ими их

к как когда которого котором которому которые который которым

ли лишь

между меня мне мной мы

на над нам нами нас не ней нем нет ни них но ну

о об однако он они от

перед по под пока после при про просто

с со

так тем то того только том тому

у уж уже

хотя чего чем чему через что чтобы

это этим этого этом этому

я
""".split())
