from api_interfaces.ms_translate import MicrosoftTranslate


class TranslatorManager():
    ''' A class for managing multiple translation services. This is a mostly aspirational feature, where in the future I may add more API providers
    '''

    def __init__(self):
        self.translation_services = {}
        self._translator = None
        self.current_service = None
        self.supported_services = {
            'MS':'Microsoft Translator Text API'
        }


    def add_translation_service(self, name, service, token):
        ''' Add a translation service. If no translation services currently exist, this will set up the service as the current translator.

        Args:
            name (str): The name of the translator, this name will appear in menus
            service (str): The name of the service, supported services are contained within the "supported_services" attribute of this object
            token (str): The API token used to authenticate requests

        Raises:
            ValueError: If an unrecognised service name is passed
            ValueError: If the name passed already exists
        '''
        if service not in list(self.supported_services.keys()):
            raise ValueError(f'{service} is not a recognised service provider. Valid services are contained within the "supported_services" attribute of this object')            

        if name in list(self.translation_services.keys()):
            raise ValueError(f'{name} already exists!')

        self.translation_services[name] = {}
        self.translation_services[name]['service'] = service
        self.translation_services[name]['token'] = token

        if len(list(self.translation_services.keys())) == 1:
            self.change_translation_service(name)
        

    def change_translation_service(self, name):
        ''' Change the translation service in use.

        Args:
            name (str): The name of the translator
        
        Raises:
            KeyError: If the translator name does not exist
        '''
        if self.translation_services[name]['service'] == 'MS':
            self._translator = MicrosoftTranslate(self.translation_services[name]['token'])
            self.current_service = name
        

    def translate(self, inputString, translate_from=None, translate_to=['en'], html=False):
        ''' A method to translate an input string to one or more languages. Calls the translate method of the "_translator" attribute

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
        return self._translator.translate(inputString, translate_from, translate_to, html)

    
    def get_supported_languages(self):
        ''' A method to get the languages supported by the current translation service. Calls the get_supported_languages method of the "_translator" attribute

        Returns:
            dict: A dictionary of supported languages in the form language_tag:name, language tags follow the BCP 47 standard
        '''
        return self._translator.get_supported_languages()