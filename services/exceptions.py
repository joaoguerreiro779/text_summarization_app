

class LanguageIdentificationError(ValueError):
    """
        Raised when the language identification output is not reliable

        Attributes
            -------
                status_code: The status code to send for this error.
                name: The name of the error.
                description: The description of the error.
    """
    status_code=400
    name="LanguageIdentificationError"
    description="Error: The language of the input text was not reliably identified as English."
