import configparser

config = configparser.RawConfigParser()
config.read(".\\Config\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','loginURL')
        return url

    @staticmethod
    def getemail():
        username = config.get('common info','email')
        return username

    @staticmethod
    def getpassword():
        username = config.get('common info', 'password')
        return password