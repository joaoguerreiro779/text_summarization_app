from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from config import Config


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
        print("Downloading a model")
        self.model = AutoModelForSeq2SeqLM.from_pretrained(Config.MODEL_NAME)



    def summarize(self, query_text: str) -> str:

        '''
            Summarize an input text.

                Parameters:
                        query_text (str): Input text to be summarized

                Returns:
                        decoded (str): The summarized text
        '''
        tokenizer = AutoTokenizer.from_pretrained(Config.TOKENIZER_NAME)
        inputs = tokenizer(query_text, return_tensors="pt")
        prediction = self.model.generate(**inputs)
        decoded = tokenizer.batch_decode(prediction)
        return decoded
