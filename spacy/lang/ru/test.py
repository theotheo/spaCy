@pytest.fixture
def ru_tokenizer():
    return util.get_lang_class('ru').Defaults.create_tokenizer()
    
@pytest.mark.parametrize('text,length', [
    ("Я пью, т.к. не могу не пить.", 9),
    ("Нет документации - нет токенизатора!", 6),
    ("Мы все учились понемногу: чему-нибудь и как-нибудь...", 9)])  
def test_ru_tokenizer_handles_punct_abbrev(ru_tokenizer, text, length):
    tokens = ru_tokenizer(text)
    assert len(tokens) == length
