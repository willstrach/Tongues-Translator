import json
import os


class ConfigManager:
    ''' Manages the configuration file for the application. The configuration file can be found in the location defined in install_variables.

    If no configuration file exists, one will be created

    '''

    def __init__(self):
        install_variables = json.loads(open('config/install_variables.json').read())
        self.config_path = install_variables['config_location']
        self.config_files = {
            'providers':'providers.json'
        }


        if not os.path.isfile(os.path.join(self.config_path, self.config_files['providers'])):
            self.write_providers([])

    def get_providers(self):
        ''' gets the api providers from the config files

        Returns:
            (list(dict)): A list of dictionaries, in the form "name":NAME, "service":SERVICE, "token":TOKEN
        ''' 
        with open(os.path.join(self.config_path, self.config_files['providers']), 'r') as f:
            return json.loads(f.read())

    def write_providers(self, providers_list):
        ''' Writes a list of providers to file

        Args:
            providers_list (list(dict)): A list of provider definitions
        '''
        with open(os.path.join(self.config_path, self.config_files['providers']), 'w') as f:
            write_string = json.dumps({'api_providers':providers_list})
            f.write(write_string)