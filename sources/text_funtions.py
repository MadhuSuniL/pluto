from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from .translate import translate
# # Download the required NLTK data
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


def total_words(text):
    return len(text.split(' '))

def total_different_words(text):
    return len(set(text.split(' ')))
    
def length(text):
    return len(text)



def get_pos_explanation(pos):
    """
    Get an explanation for a given part of speech tag.
    """
    pos_explanations = {
        'CC': 'Coordinating conjunction',
        'CD': 'Cardinal number',
        'DT': 'Determiner',
        'EX': 'Existential there',
        'FW': 'Foreign word',
        'IN': 'Preposition or subordinating conjunction',
        'JJ': 'Adjective',
        'JJR': 'Adjective, comparative',
        'JJS': 'Adjective, superlative',
        'LS': 'List item marker',
        'MD': 'Modal',
        'NN': 'Noun, singular or mass',
        'NNS': 'Noun, plural',
        'NNP': 'Proper noun, singular',
        'NNPS': 'Proper noun, plural',
        'PDT': 'Predeterminer',
        'POS': 'Possessive ending',
        'PRP': 'Personal pronoun',
        'PRP$': 'Possessive pronoun',
        'RB': 'Adverb',
        'RBR': 'Adverb, comparative',
        'RBS': 'Adverb, superlative',
        'RP': 'Particle',
        'SYM': 'Symbol',
        'TO': 'to',
        'UH': 'Interjection',
        'VB': 'Verb, base form',
        'VBD': 'Verb, past tense',
        'VBG': 'Verb, gerund or present participle',
        'VBN': 'Verb, past participle',
        'VBP': 'Verb, non-3rd person singular present',
        'VBZ': 'Verb, 3rd person singular present',
        'WDT': 'Wh-determiner',
        'WP': 'Wh-pronoun',
        'WP$': 'Possessive wh-pronoun',
        'WRB': 'Wh-adverb'
    }

    return pos_explanations.get(pos, 'Unknown')

def extract_pos_word_dict(text):

    sentences = sent_tokenize(text)

    pos_word_dict = {}

    for sentence in sentences:
        words = word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)

        for word, pos in tagged_words:
            explanation = get_pos_explanation(pos)
            if explanation in pos_word_dict:
                pos_word_dict[explanation].append(word)
            else:
                pos_word_dict[explanation] = [word]

    return pos_word_dict

def text_info(text):    
    result = extract_pos_word_dict(text)
    res = ''
    for pos, words in result.items():
        res += f"<b>{pos + ':'}</b><br> <ol> {''.join(['<li>'+word+'/<li>' for word in words ])}</ol>+<br>"
    return res


def language_convert(text,language):
    language_dict = {
    'Afrikaans': 'af',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Azerbaijani': 'az',
    'Belarusian': 'be',
    'Bulgarian': 'bg',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Czech': 'cs',
    'Welsh': 'cy',
    'Danish': 'da',
    'German': 'de',
    'Greek': 'el',
    'English': 'en',
    'Esperanto': 'eo',
    'Spanish': 'es',
    'Estonian': 'et',
    'Basque': 'eu',
    'Persian': 'fa',
    'Finnish': 'fi',
    'French': 'fr',
    'Irish': 'ga',
    'Scottish Gaelic': 'gd',
    'Galician': 'gl',
    'Gujarati': 'gu',
    'Hausa': 'ha',
    'Hawaiian': 'haw',
    'Hindi': 'hi',
    'Hmong': 'hmn',
    'Croatian': 'hr',
    'Haitian Creole': 'ht',
    'Hungarian': 'hu',
    'Armenian': 'hy',
    'Indonesian': 'id',
    'Igbo': 'ig',
    'Icelandic': 'is',
    'Italian': 'it',
    'Hebrew': 'iw',
    'Japanese': 'ja',
    'Javanese': 'jv',
    'Georgian': 'ka',
    'Kazakh': 'kk',
    'Khmer': 'km',
    'Kannada': 'kn',
    'Korean': 'ko',
    'Kurdish': 'ku',
    'Kyrgyz': 'ky',
    'Latin': 'la',
    'Luxembourgish': 'lb',
    'Lao': 'lo',
    'Lithuanian': 'lt',
    'Latvian': 'lv',
    'Malagasy': 'mg',
    'Maori': 'mi',
    'Macedonian': 'mk',
    'Malayalam': 'ml',
    'Mongolian': 'mn',
    'Marathi': 'mr',
    'Malay': 'ms',
    'Maltese': 'mt',
    'Burmese': 'my',
    'Nepali': 'ne',
    'Dutch': 'nl',
    'Norwegian': 'no',
    'Chichewa': 'ny',
    'Punjabi': 'pa',
    'Polish': 'pl',
    'Pashto': 'ps',
    'Portuguese': 'pt',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Kinyarwanda': 'rw',
    'Sindhi': 'sd',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Samoan': 'sm',
    'Shona': 'sn',
    'Somali': 'so',
    'Albanian': 'sq',
    'Serbian': 'sr',
    'Sesotho': 'st',
    'Sundanese': 'su',
    'Swedish': 'sv',
    'Swahili': 'sw',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Tajik': 'tg',
    'Thai': 'th',
    'Filipino': 'tl',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Uzbek': 'uz',
    'Vietnamese': 'vi',
    'Xhosa': 'xh',
    'Yiddish': 'yi',
    'Yoruba': 'yo',
    'Chinese': 'zh',
    'Chinese (Traditional)': 'zh-TW',
    'Zulu': 'zu'
}
    
    try:
        return translate(text,language_dict[language.title()])
    except:
        return 'Please provide text between \' or "'


def correct_text(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()
    return str(corrected_text)


    