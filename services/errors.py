class LanguageIdentificationError(ValueError):
    """
    Raised when the language identification output is not reliable

    Attributes
        -------
            status_code: The status code to send for this error.
            name: The name of the error.
            message: The description of the error.
    """

    status_code = 400
    name = "LanguageIdentificationError"
    message = "Error: Language of input text was not reliably identified as English."


class ModelNotFoundError(ValueError):
    """
    Raised when the service was unable to find the model files.

    Attributes
        -------
            status_code: The status code to send for this error.
            name: The name of the error.
            message: The description of the error.
    """

    status_code = 500
    name = "ModelNotFoundError"

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
