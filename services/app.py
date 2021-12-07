"""
The main flask application which contains the endpoints to call the services

    Endpoints
        -------
            '/summarize', methods=['POST']
                Summarize an input text.
    Host and port
        -------
            host='0.0.0.0', port='3000'
                IP and port where the application is running
    Error Handlers
        -------
            handle_custom_error
                Handles user defined errors

            handle_type_error
                Handles form type errors

            handle_unexpected_error
                Handles unexpected errors

        The port where the application is listening
    Error Handling

"""

import json
from flask import Flask, request
from summarizer import Summarizer
from language_identifier import LanguageIdentifier
from errors import LanguageIdentificationError, ModelNotFoundError


app = Flask(__name__)


@app.route("/summarize", methods=["POST"])
def predict():

    """
    The endpoint for text summarization

        args: {text: <query_text>}

        returns: {
       'summary': <summarized_text>,
        'success': True,
        'status_code': 200
    }

    """

    req = request.get_json(force=True)["text"]

    if not isinstance(req, str):
        raise TypeError("Input is not of type string.")

    lang_code, prob = LanguageIdentifier().get_language(req)

    if lang_code == "en" and prob > 0.98:
        result = Summarizer().summarize(req)
    else:
        raise LanguageIdentificationError()

    response = {"summary": result, "success": True, "status_code": 200}

    return json.dumps(response)


@app.errorhandler(LanguageIdentificationError)
@app.errorhandler(ModelNotFoundError)
def handle_custom_error(err):

    """
    Handles known bad requests

        args: err

        returns:

        {'error':
            {'type': <error name>,
            'message': <error message>},
        'success': False,
        'status_code': <error status_code>
    }

    """

    response = {
        "error": {"type": err.name, "message": err.message},
        "success": False,
        "status_code": err.status_code,
    }
    return json.dumps(response)


@app.errorhandler(TypeError)
def handle_form_type_error(err):

    """
    Handles wrong json form type

        args: err

        returns:

        {'error':
            {'type': <error name>,
            'message': <error message>},
        'success': False,
        'status_code': <error status_code>
    }

    """

    response = {
        "error": {"type": "TypeError", "message": str(err)},
        "success": False,
        "status_code": 400,
    }
    return json.dumps(response)


@app.errorhandler(Exception)
def handle_unexpected_error(err):

    """
    Handles all unexpected errors

        args: err

        returns:

        {'error':
            {'type': <error name>,
            'message': <error message>},
        'success': False,
        'status_code': <error status_code>
    }

    """

    response = {
        "error": {"type": "InternalServerError", "message": str(err)},
        "success": False,
        "status_code": 500,
    }
    return json.dumps(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3000")
