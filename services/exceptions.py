

class LanguageIdentificationError(ValueError):
    """
        Raised when the language identification output is not reliable

        Attributes
            -------
                status_code: The status code to send for this error.
                name: The name of the error.
                message: The description of the error.
    """
    status_code=400
    name="LanguageIdentificationError"
    message="Error: The language of the input text was not reliably identified as English."

class ModelConfigLoadError(OSError):
    """
        Raised when summarizer was unable to load the model config

        Attributes
            -------
                status_code: The status code to send for this error.
                name: The name of the error.
                message: The description of the error.
    """

    status_code=500
    name="ModelConfigLoadError"

    def __init__(self, message: str):
        self.message=message
        super().__init__(self.message)

class TokenizerConfigLoadError(OSError):
    """
        Raised when summarizer was unable to load the tokenizer config

        Attributes
            -------
                status_code: The status code to send for this error.
                name: The name of the error.
                message: The description of the error.
    """

    status_code=500
    name="TokenizerConfigLoadError"

    def __init__(self, message: str):
        self.message=message
        super().__init__(self.message)

class InvalidModelError(ValueError):
    """
        Raised when selected model is not appropriate for summarization.

        Attributes
            -------
                status_code: The status code to send for this error.
                name: The name of the error.
                message: The description of the error.
    """

    status_code=500
    name="InvalidModelError"

    def __init__(self, message: str):
        self.message=message
        super().__init__(self.message)
