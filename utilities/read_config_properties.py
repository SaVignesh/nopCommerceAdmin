import configparser
import os

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_base_url():
        url = config.get("common info","base_url")
        return url.strip('/"')

    @staticmethod
    def get_email():
        username = config.get("common info", "email")
        return username

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password


