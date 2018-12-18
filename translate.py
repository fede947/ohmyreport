from mtranslate import translate as trans


def translate(text, lang):
    if(lang == 'en'):
        return text
    return trans(text, lang)
