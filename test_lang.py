LANGUAGES = [
    {
        'name': 'Spanish',
        'common_words': [
            'el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'ser', 'se',
            'no', 'haber', 'por', 'con', 'su', 'para', 'como', 'estar',
            'tener', 'le', 'lo', 'lo', 'todo', 'pero', 'más', 'hacer',
            'o', 'poder', 'decir', 'este', 'ir', 'otro', 'ese', 'la',
            'si', 'me', 'ya', 'ver', 'porque', 'dar', 'cuando', 'él',
            'muy', 'sin', 'vez', 'mucho', 'saber', 'qué', 'sobre',
            'mi', 'alguno', 'mismo', 'yo', 'también', 'hasta'
        ]
    },
    {
        'name': 'German',
        'common_words': [
            'das', 'ist', 'du', 'ich', 'nicht', 'die', 'es', 'und',
            'der', 'was', 'wir', 'zu', 'ein', 'er', 'in', 'sie', 'mir',
            'mit', 'ja', 'wie', 'den', 'auf', 'mich', 'dass', 'so',
            'hier', 'eine', 'wenn', 'hat', 'all', 'sind', 'von',
            'dich', 'war', 'haben', 'für', 'an', 'habe', 'da', 'nein',
            'bin', 'noch', 'dir', 'uns', 'sich', 'nur',
            'einen', 'kann', 'dem'
        ]
    },
    
    {
        'name':'English',
        'common_words':['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I',
        'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his',
        'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all',
        'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go'
        'people','into','year','your','good','some','could','them','see','other','than','then','now',
        'look','only','come','its','over','think','also','back','after','use','two','how','our','work',
        'first','well','way','even','new','want','because','any','these','give','day','most','us','when',
        'make','can','like','time','no','just','him','know','take'
        ]
    }
]


def get_word_count(text, list_of_words):
    
    count = 0
    text_l = text.split()
    for word in text_l:
        if word in list_of_words:
            count += 1
            
    return count

def detect_language(text, LANGUAGES):
    """Returns the detected language of given text."""
    lang = None
    word_count = None
    our_test = []
    
    for language in LANGUAGES:
        
        result = get_word_count(text, language['common_words'])
        if word_count is None or result > word_count:
            lang = language['name']
            
    return lang

print(detect_language('ich bin du bist', LANGUAGES))
