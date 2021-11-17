from abc import ABC
from typing import Tuple
import gcld3

class LanguageIdentifier(ABC):

    """
        A class to create a text summarizer.

        Methods
        -------
            get_language(query_text: str)-> Optional[str]:
                Detect the language of an input text.
            get_freq_languages(self, query_text: str, num_langs: int)-> Optional[list]:
                Detect the n most frequent languages of an input text.
    """

    def get_language(self, query_text: str)-> Tuple[str,bool]:

        '''
            Get the language of an input text.

                Parameters:
                        query_text (str): Input text whose language is to be detected.

                Returns:
                        result.language (str): The language code of the text.
        '''

        model = gcld3.NNetLanguageIdentifier(min_num_bytes=0, max_num_bytes=1000)
        result = model.FindLanguage(text=query_text)

        return result.language, result.is_reliable


    def get_freq_languages(self, query_text: str, num_langs: int)-> list:

        '''
            Get the language of an input text.

                Parameters:
                        query_text (str): Input text whose language is to be detected.
                        num_langs (int): The number of languages in the text.

                Returns:
                        languages_list (list): A list of all the language codes detected.
        '''

        model = gcld3.NNetLanguageIdentifier(min_num_bytes=0, max_num_bytes=1000)
        result = model.FindTopNMostFreqLangs(text=query_text, num_langs=num_langs)

        languages_list = []
        for res in result:
            if res.is_reliable:
                languages_list.append(res.language)
        if languages_list == []:
            return languages_list
