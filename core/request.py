import os
from jinja2 import Environment, FileSystemLoader
from core.BaseClass import BaseClass

class Request(BaseClass):
    __name: str = ''
    __path: str = ''
    __filename: str = ''
    __content: str = ''

    def __init__(self, name: str, project_path: str = os.getcwd(), path: str = 'app/Http/Requests/V1', class_name: str = 'StoreRequest', template: str = 'request.stub') -> None:
        self.__name = name.title()
        self.__filename = f"{class_name}.php"
        self.__path = f"{project_path}/{path}/{self.__name}/"

        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template(template)

        self.__content = template.render(model=self.__name, class_name=class_name)


    
    def make(self) -> str:
        if not(os.path.exists(self.__path)):
            os.mkdir(self.__path)


        with open(self.__path + self.__filename, mode="w", encoding="utf-8") as file:
            file.write(self.__content)

        return self.__path + self.__filename

    def remove(self):
        if os.path.exists(self.__path + self.__filename):
            os.remove(self.__path + self.__filename)
            return True
        
        return False