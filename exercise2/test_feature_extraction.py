'''
author: Merilin Sousa SIlva
studentID: 23-726-086
'''

from feature_extraction import Document, FeatureExtractor, PortugueseFeatureExtraction, EnglishFeatureExtraction 

# Document class tests

def test_document_loading():
    doc = Document('test.txt')
    assert doc.file_path == 'test.txt'
    assert doc.text == """In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. The latter may allow its elements to be mutated and the length changed, or it may be fixed (after creation). A string is generally considered as a data type and is often implemented as an array data structure of bytes (or words) that stores a sequence of elements, typically characters, using some character encoding. String may also denote more general arrays or other sequence (or list) data types and structures.

Depending on the programming language and precise data type used, a variable declared to be a string may either cause storage in memory to be statically allocated for a predetermined maximum length or employ dynamic allocation to allow it to hold a variable number of elements.

When a string appears literally in source code, it is known as a string literal or an anonymous string.[1]

In formal languages, which are used in mathematical logic and theoretical computer science, a string is a finite sequence of symbols that are chosen from a set called an alphabet."""

def test_document_repr():
    doc = Document('test.txt')
    assert repr(doc) == "Document('test.txt')"

def test_document_length():
    # The length of the document should be the number of characters in the text
    doc = Document('test.txt')
    assert len(doc) == 1118

def test_document_sorting():
    # Documents should be sorted based on their length
    doc1 = Document('test.txt')
    doc1.text = 'short text'
    doc2 = Document('test.txt')
    doc2.text = 'longer text'
    doc3 = Document('test.txt')
    doc3.text = 'longest text'
    assert sorted([doc2, doc1, doc3]) == [doc1, doc2, doc3]

# FeatureExtractor class tests

def test_feature_extractor():
    doc = Document('test.txt')
    extractor = FeatureExtractor()
    features = extractor.extract_features(doc)
    assert features == {
        'char_count': 1118,
        'alpha_ratio': 904 / 1118,
        'unique_chars_count': 39,
    }

# PortugueseFeatureExtractor class tests

def test_portuguese_feature_extractor():
    doc = Document('test_port.txt')
    extractor = PortugueseFeatureExtraction()
    features = extractor.extract_features(doc)
    assert features == {
        'char_count': 1917,
        'alpha_ratio': 0.8085550339071466,
        'unique_chars_count': 56,
        'clitic_pronoun_count': 25,
        'nasal_vowel_words_count': {'ã': 8, 'õ': 5, 'ũ': 0},
        'cedilla_words_count': 9
    }

def test_portuguese_feature_extractor_on_engl_text():
    doc = Document('test_eng.txt')
    extractor = PortugueseFeatureExtraction()
    features = extractor.extract_features(doc)
    assert features == {
        'char_count': 1647,
        'alpha_ratio': 0.8014571948998178,
        'unique_chars_count': 46,
        'clitic_pronoun_count': 8, # Since some pronouns in Portuguese are also some articles in English (a etc.), the function will count those in the English text
        'nasal_vowel_words_count': {'ã': 0, 'õ': 0, 'ũ': 0},
        'cedilla_words_count': 0
    }

# EnglishFeatureExtraction class tests
    
def test_english_feature_extractor():
    doc = Document('test_eng.txt')
    extractor = EnglishFeatureExtraction()
    features = extractor.extract_features(doc)
    assert features == {
        'char_count': 1647,
        'alpha_ratio': 0.8014571948998178,
        'unique_chars_count': 46,
        'article_frequency': 24,
        'count_regular_pastform_verbs': 14,
        'named_entities_frequency': 14 
    }

def test_english_feature_on_portuguese_text():
    doc = Document('test_port.txt')
    extractor = EnglishFeatureExtraction()
    features = extractor.extract_features(doc)
    assert features == {
        'char_count': 1917,
        'alpha_ratio': 0.8085550339071466,
        'unique_chars_count': 56,
        'article_frequency': 9, # Since the SpaCy model is in English, the number of articles found will be innacurate, here it found nine
        'count_regular_pastform_verbs': 0,
        'named_entities_frequency': 66 # Even though the text is in English, the capialization in portuguese has the same rules as in English, yet Time entities etc. are different, so the SpaCy pipeline will find different ones that may not be Named Entities
    }