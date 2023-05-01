from jinja2 import Environment, FileSystemLoader
import re, os, inflect
from datetime import datetime
from core.BaseClass import BaseClass

class Factory(BaseClass):
    __name: str = ''
    __path: str = ''
    __content: str = ''


    def __init__(self, name: str, project_path: str = os.getcwd(), path: str = 'database/factories/', template: str = 'Factory.stub') -> None:
        self.__name = name.title()
        self.__path = f"{project_path}/{path}/{self.__name}Factory.php"


        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template(template)

        self.__content = template.render(model=self.__name)


    
    def make(self) -> str:
        with open(self.__path, mode="w", encoding="utf-8") as file:
            file.write(self.__content)

        return self.__path

    def remove(self):
        if os.path.exists(self.__path):
            os.remove(self.__path)
            return True
        
        return False