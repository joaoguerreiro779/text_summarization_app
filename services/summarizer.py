from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from config import Config
from exceptions import ModelConfigLoadError, TokenizerConfigLoadError, InvalidModelError


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
        Construct all the necessary attributes for the summarizer object.
        """
        try:
            print("Downloading a model")
            self.model = AutoModelForSeq2SeqLM.from_pretrained(Config.MODEL_NAME)
        except OSError as error:
            raise ModelConfigLoadError(message=str(error)) from error
        except ValueError as error:
            raise InvalidModelError(message=str(error)) from error

    def summarize(self, query_text: str) -> str:

        '''
            Summarize an input text.

                Parameters:
                        query_text (str): Input text to be summarized

                Returns:
                        result (str): The summarized text
        '''
        try:
            tokenizer = AutoTokenizer.from_pretrained(Config.TOKENIZER_NAME)
        except OSError as error:
            raise TokenizerConfigLoadError(message=str(error)) from error

        inputs = tokenizer(query_text, return_tensors=self.model.framework)
        prediction = self.model.generate(**inputs)
        decoded = tokenizer.batch_decode(prediction)

        result = decoded[0].replace('</s>','').replace('<s>','')

        return result
