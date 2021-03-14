import ast
import yaml

def loadNicknames():
    file = open("nicknames.config", "r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()
    return dictionary

def initialize():
    with open("config.yaml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)
    nicknames = loadNicknames()
    return cfg, nicknames