from sys import argv
from os import chdir, getcwd, remove
from create_language import Language

def_path:str = getcwd()
chdir("settings")
settings_content = open("st.settings", "r").read().split("\n")
settings_content_language = settings_content[0].replace("LANG=","")
settings_content_mode = settings_content[1].replace("MODE=","")
chdir(def_path)

name:str = argv[1]
try:
    if (settings_content_mode == Language(language=settings_content_language, mode=settings_content_mode, name=name)._save):
        file = open(name, "x")
        file.close()
    elif (settings_content_mode == Language(language=settings_content_language, mode=settings_content_mode, name=name)._del):
        remove(name)
    print(Language(language=settings_content_language, mode=settings_content_mode, name=name).success())
except:
    print(Language(language=settings_content_language, mode=settings_content_mode, name=name).unsuccess())