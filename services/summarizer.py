'''
The language identifier module which contains the class to
define language identification objects

    Classes
        -------
            Summarizer
                A class to create a text summarizer.

                Methods
                    -------
                        def __init__(self):
                            Constructor for the summarizer class.

                            summarize(query_text: str)-> str:
                                Summarize an input text.
'''


import re
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from errors import ModelNotFoundError


class Summarizer:

    """
        A class to create a text summarizer.

        Methods
            -------
            summarize(query_text: str):
                Summarize an input text.
    """

    def __init__(self):
        """
        Constructor for the summarizer class.
        """
        try:
            print("Downloading a model")
            self.model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
        except ValueError as error:
            raise ModelNotFoundError(message=str(error)) from error

    def summarize(self, query_text: str) -> str:

        '''
            Summarize an input text.

                Parameters:
                        query_text (str): Input text to be summarized

                Returns:
                        result (str): The summarized text
        '''
        try:
            tokenizer = AutoTokenizer.from_pretrained("philschmid/bart-large-cnn-samsum")
        except ValueError as error:
            raise ModelNotFoundError(message=str(error)) from error

        inputs = tokenizer(str(query_text), return_tensors=self.model.framework)
        prediction = self.model.generate(**inputs)
        decoded = tokenizer.batch_decode(prediction)

        result = re.sub(r'(\W^<)?\<[^>]*\>(\W^>)?', '', decoded[0])

        return result
