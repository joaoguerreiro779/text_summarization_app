import json
from flask import Flask, request
from summarizer import Summarizer
from language_identifier import LanguageIdentifier
from exceptions import *


app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def predict():

    req = request.get_json()['text']

    if not isinstance(req,str):
        raise TypeError('Input type is not string')

    lang_code, is_reliable = LanguageIdentifier().get_language(req)

    if lang_code=='en' and is_reliable:
        result = Summarizer().summarize(req)
    else:
        raise LanguageIdentificationError()

    response = {
       'summary': result,
        'success': True,
    }

    return json.dumps(response), 200

@app.errorhandler(LanguageIdentificationError)
@app.errorhandler(ModelConfigLoadError)
@app.errorhandler(TokenizerConfigLoadError)
@app.errorhandler(InvalidModelError)
def handle_custom_error(err):

    response = {
        'error': {
            'type': err.name,
            'message': err.message
        },
        'success': False,
    }
    return json.dumps(response), err.status_code

@app.errorhandler(TypeError)
def handle_form_type_error(err):

    response = {
        'error': {
            'type': 'Type Error',
            'message': str(err)
        },
        'success': False,
    }
    return json.dumps(response), 400

@app.errorhandler(Exception)
def handle_unexpected_error(err):

    response = {
        'error': {
            'type': 'UnexpectedException',
            'message': str(err)
        },
        'success': False,
    }
    return json.dumps(response), 500

if __name__=='__main__':
    app.run(host='0.0.0.0', port='3000')
