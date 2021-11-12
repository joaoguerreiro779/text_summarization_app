from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained("philschmid/bart-large-cnn-samsum")




class Summarizer:
    def __init__(self):
        print("Downloading a model")
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)



    def AwesomeFunction(self, QueryText: str) -> "something":
        inputs = tokenizer(QueryText, return_tensors="pt")
        prediction = self.model.generate(**inputs)
        decoded = tokenizer.batch_decode(prediction)
        return decoded  

