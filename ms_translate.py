import requests
import json
import uuid

class MicrosoftTranslate():
    ''' A class to handle interactions with the MS Translator Text API

    Args:
        api_key (str): The API Key for your instance of MS 
    
    Raises:
        HTTPError: If a HTTP request fails
    '''


    def __init__(self, api_key):
        self._base_url = 'https://api.cognitive.microsofttranslator.com/'
        self._api_key = api_key
        self._headers = {
            'Ocp-Apim-Subscription-Key': api_key,
            'Content-type': 'application/json'
        }
        self._supported_languages = self._get_supported_languages()

    def _get_supported_languages(self):
        request_url = self._base_url + 'languages?api-version=3.0&scope=translation'
        response = requests.get(request_url, headers=self._headers)
        if not response.ok:
            raise requests.exceptions.HTTPError(f'\n\nFailed to contact MS Translator Text API:\n\tResponse returned error:\n\t\t{response.text}')
        returnDict = {}
        for language in response.json()['translation'].keys():
            returnDict[language] = response.json()['translation'][language]['name']
        return returnDict

    def get_supported_languages(self):
        ''' A method to get the languages supported by the MS Translator Text API

        Returns:
            dict: A dictionary of supported languages in the form language_tag:name, language tags follow the BCP 47 standard
        '''
        return self._supported_languages

    def translate(self, inputString, translate_from=None, translate_to=['en'], html=False):
        ''' A method to translate an input string to one or more languages

        Args:
            inputString (str): A string containing the source text to be translated
            translate_from (:obj:'str',: optional): A string denoting the language tag of the source language (a list of supported languages and their tags can be found here: https://docs.microsoft.com/en-gb/azure/cognitive-services/Translator/language-support).
                Defaults to None, if none, MS Translate will attempt to automatically recognise the language
            translate_to (list(str)): A list of strings dentoting target language tags (a list of supported languages and their tags can be found here: https://docs.microsoft.com/en-gb/azure/cognitive-services/Translator/language-support)
            html (:obj:'bool', optional): Does the source text contain HTML? Defaults to False

        Returns:
            dict: A dictionary containing the output of the request in the format language_tag:text 
        
        Raises:
            ValueError: If translate_from or translate_to are not valid
            HTTPError: If the HTTP request fails
        '''

        # Is translate_from valid?
        if translate_from is not None:
            if not translate_from in list(self._supported_languages.keys()):
                raise ValueError(f'"{translate_from}" is not a recognised language')

        # Is translate_to valid?
        for language in translate_to:
            if not language in self._supported_languages.keys():
                raise ValueError(f'"{language}" is not a recognised language')

        identifier = str(uuid.uuid4())

        request_url = self._base_url + f'translate?api-version=3.0&ClientTraceId={identifier}' 
        
        if translate_from:
            request_url += f'&from={translate_from}'

        for language in translate_to:
            request_url += f'&to={language}'

        request_url += '&textType=html' if html else '&textType=plain'

        data = json.dumps([{'text':inputString}])

        response = requests.post(request_url, headers=self._headers, data=data)

        if not response.ok:
            raise requests.exceptions.HTTPError(f'\n\nFailed to contact MS Translator Text API:\n\tResponse returned error:\n\t\t{response.text}')

        returnDict = {'request_id':identifier}
        for translation in response.json()[0]['translations']:
            returnDict[translation['to']] = translation['text']
        
        return returnDict