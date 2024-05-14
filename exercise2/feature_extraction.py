'''
author: Merilin Sousa SIlva
studentID: 23-726-086
'''

##### YOU CAN ADD IMPORTS HERE #####
import re
import spacy
####################################

class Document:
    """
    Represents a document, storing a text.
    """

    def __init__(self, file_path: str):
        """
        Initializes a new instance of Document.

        Args:
            file_path (str): The path to the document file.
        """
        
        self.file_path = file_path
        self.text = self.extract_text_from_file() # Text extracted from the file -- TODO: implement its extraction
        
    # TODO: Implement loading text from file, and other functionalities as required
    def extract_text_from_file(self) -> None:
        """
        Extracts text from a file and returns it
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read() # reads the contents of the file and returns it

    def __repr__(self) -> str:
        """
        Returns a string representation of the class instance

        Returns:
            str: string representation of the class instance
        """
        return f"Document('{self.file_path}')" # Returns a string representation with the use of a f-string
    
    def __len__(self) -> int:
        """
        Returns the length of the file content

        Returns:
            int: length of self.text
        """
        return len(self.text)
    
    def __lt__(self, other: 'Document') -> bool: 
        """
        Enables the comparison of different documents, thus through sorting
        the documents are sorted by their length. Thus sorted() can then be used.

        Args:
            other (Document): another instance of the class Document

        Returns:
            bool: a boolean that decides if self.text is smaller than other.text
        """
        if not isinstance(other, Document):
            return NotImplemented # This checks if the other value is also an instance of Document, if not, it acts accordingly
        return len(self.text) < len(other.text) # Through this implementation, documents are ordered by their length


####################################

class FeatureExtractor:
    """
    Base class for extracting features from a document.
    
    This class should be subclassed to create specific feature extractors for different languages or requirements.
    """

    def extract_features(self, document: Document) -> dict[str, float]:
        """
        Extracts features from a document. This method should be overridden in subclasses.

        Args:
            document (Document): The document from which to extract features.

        Returns:
            Dict[str, float]: A dictionary containing the extracted features.
        """
        # Placeholder for base feature extraction logic. Implement feature extraction methods below.
        features = {
            'char_count': self._char_count(document.text),
            'alpha_ratio': self._alpha_ratio(document.text),
            'unique_chars_count': self._unique_chars_count(document.text),
        }
        return features

    # Methods for feature extraction:

    @staticmethod
    def _char_count(text: str) -> int:
        """
        Counts the number of characters in the specified text.
        
        Args:
            text (str): The text from which to count characters.

        Returns:
            int: The number of characters in the text.
        """
        # TODO: Implement this method to count characters in the text
        return len(text)

    @staticmethod
    def _alpha_ratio(text: str) -> float:
        """
        Calculates the ratio of characters that are alphabetic in the specified text.
        Alphabetic characters include letters (including umlauts etc.) but not numbers or punctuation.
        
        Args:
            text (str): The text from which to calculate alphabetic ratio.

        Returns:
            float: The ratio of alphabetic characters in the text.
        """
        # TODO: Implement this method to calculate the alphanumeric ratio
        alpha = [character for character in text if character.isalpha()] # Counts the characters in the text that are alphabetic

        # Sorts the characters depending if they are alphabetic and then divides them by the number of all the characters
        return len(alpha) / len(text)

    @staticmethod
    def _unique_chars_count(text: str) -> int:
        """
        Counts the number of unique characters in the specified text.
        
        Args:
            text (str): The text from which to count the unique characters.

        Returns:
            int: The number of unique characters in the text.
        """
        # TODO: Implement this method to count unique characters

        return len(set(list(text))) # first a list is created of the characters and then a set, to only retain the unique characters and finally they are counted

###### TODO: YOUR FEATURE EXTRACTOR IMPLEMENTATIONS HERE ######

class PortugueseFeatureExtraction(FeatureExtractor):
    # There isn't a constructor since the class doesn't create any instance, and just works with a given document. One could implement one, but it isn't needed here
    def extract_features(self, document: Document) -> dict[str, float]: # This function is the only one that isn't private (since it should be accessible from the outside) and that isn't a static method (since it uses the self parameter, so an instance of the class)
        """
        This function extracts general language features and also some language specific features related to Portugese

        Args:
            document (Document): instance of the class Document that incorportates the content being in Portuguese

        Returns:
            dict[str, float]: dictionary with language features
        """
        features = {
            'char_count': self._char_count(document.text),
            'alpha_ratio': self._alpha_ratio(document.text),
            'unique_chars_count': self._unique_chars_count(document.text),
            'clitic_pronoun_count': self._count_clitic_pronouns(document.text),
            'nasal_vowel_words_count': self._count_nasal_vowel_words(document.text),
            'cedilla_words_count': self._count_cedilla_words(document.text)
        }
        return features
    
    @staticmethod
    def _count_clitic_pronouns(text: str) -> int:
        """
        Counts the number of portuguese pronouns in the text

        Args:
            text (str): string in portuguese

        Returns:
            int: number of pronouns
        """
        pronoun_list = []
        cleaned_text = re.sub(r'[^\w\s]', '', text).lower() # removes punctuation and makes the text lower case
        word_list = cleaned_text.split() # splits the text into a word list

        for word in word_list:
            if word in ['eu', 'tu', 'ele', 'ela', 'nós', 'vós', 'eles', 'elas', 'mim', 'ti', 'me', 'te', 'o', 'a', 'nos', 'vos', 'os', 'as', 'lhe', 'lhes']:
                pronoun_list.append(word) # finds pronouns and adds them to a list
        
        return len(pronoun_list) #returns the count of pronouns in the text

    @staticmethod
    def _count_nasal_vowel_words(text: str) -> dict:
        """
        Finds all the words that have nasal vowels and increases the count of that
        nasal vowel in a created dictionary, which is then returned.

        Args:
            text (str): string with a portuguese text

        Returns:
            dict: dictionary that counts the occurence of words with nasal vowels
        """
        nasal_vowels_dict = {'ã': 0, 'õ':0, 'ũ': 0}

        for word in text.split():
            search_nasal_vowel = re.match(r'.*((ã)|(õ)|(ũ)).*', word.lower())
            if search_nasal_vowel:
                nasal_vowels_dict[search_nasal_vowel.group(1)] += 1
        
        return nasal_vowels_dict

    @staticmethod
    def _count_cedilla_words(text: str) -> int:
        """
        Counts the words that have a cedilla in them (ç)

        Args:
            text (str): string with portuguese text

        Returns:
            int: number of words in the text that contain a cedilla
        """
        return len([word for word in text.split() if 'ç' in word])
        
class EnglishFeatureExtraction(FeatureExtractor):

    def extract_features(self, document: Document) -> dict[str, float]:
        """
        This function extracts general language features and also some language specific features related to English

        Args:
            document (Document): instance of the class Document that incorportates the content being in English

        Returns:
            dict[str, float]: dictionary with language features
        """
        features = {
            'char_count': self._char_count(document.text),
            'alpha_ratio': self._alpha_ratio(document.text),
            'unique_chars_count': self._unique_chars_count(document.text),
            'article_frequency': self._article_frequency(document.text),
            'count_regular_pastform_verbs': self._count_regular_pastform_verbs(document.text),
            'named_entities_frequency': self._named_entities_frequency(document.text)
        }
        return features
    
    @staticmethod
    def _article_frequency(text:str) -> int:
        """
        Counts the number of articles in the text

        Args:
            text (str): string with English text

        Returns:
            int: number of articles in a text
        """
        nlp = spacy.load("en_core_web_md") # load the English language model
        doc = nlp(text) # Put the text through the Language pipeline

        return len([token for token in doc if token.pos_ == 'DET'])
    
    @staticmethod
    def _count_regular_pastform_verbs(text: str) -> int:
        """
        Counts the regular verbs that are in past simple

        Args:
            text (str): string with English text

        Returns:
            int: count of regular verbs in past simple
        """
        nlp = spacy.load("en_core_web_md") # load the English language model
        doc = nlp(text)

        return len([token for token in doc if token.pos_ == 'VERB' and token.text.endswith('ed')])
    
    @staticmethod
    def _named_entities_frequency(text: str) -> int:
        """
        Counts the named entities

        Args:
            text (str): String of text in English

        Returns:
            int: Count of Named Entities in the text
        """
        nlp = spacy.load("en_core_web_md") # load the English language model
        doc = nlp(text)
        return len(doc.ents) # returns the number of Named Entities in the text
