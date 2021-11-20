import json
from flask import Flask, request
from summarizer import Summarizer
from language_identifier import LanguageIdentifier
from errors import *


app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def predict():

    try:
        req = request.get_json()['text']
    except:
        raise TypeError("Error in request format. Ensure request is of the form text:<query_text>")

    if not isinstance(req,str):
        raise TypeError("Request input type is not string.")

    lang_code, prob = LanguageIdentifier().get_language(req)

    if lang_code=='en' and prob>0.98:
        result = Summarizer().summarize(req)
    else:
        raise LanguageIdentificationError()

    response = {
       'summary': result,
        'success': True,
        'status_code': 200
    }

    return json.dumps(response)

@app.errorhandler(LanguageIdentificationError)
@app.errorhandler(ModelNotFoundError)
def handle_custom_error(err):

    response = {
        'error': {
            'type': err.name,
            'message': err.message
        },
        'success': False,
        'status_code': err.status_code
    }
    return json.dumps(response)

@app.errorhandler(TypeError)
def handle_form_type_error(err):

    response = {
        'error': {
            'type': 'TypeError',
            'message': str(err)
        },
        'success': False,
        'status_code': 400
    }
    return json.dumps(response)

@app.errorhandler(Exception)
def handle_unexpected_error(err):

    response = {
        'error': {
            'type': 'UnexpectedException',
            'message': str(err)
        },
        'success': False,
        'status_code': 500
    }
    return json.dumps(response)

if __name__=='__main__':
    app.run(host='0.0.0.0', port='3000')
