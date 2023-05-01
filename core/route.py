from jinja2 import Environment, FileSystemLoader
import re, os, inflect
from datetime import datetime
from core.BaseClass import BaseClass

class Route(BaseClass):
    __name: str = ''
    __path: str = ''
    __content: str = ''
    __search: str = ''


    def __init__(self, name: str, project_path: str = os.getcwd(), path: str = 'routes/v1/', template: str = 'api.php', search: str = 'Route::apiResources([') -> None:
        self.__name = name.title()
        self.__search = search
        self.__path = f"{project_path}/{path}/"


        environment = Environment(loader=FileSystemLoader(self.__path))
        template = environment.get_template(template)

        self.__content = template.render(model=self.__name)

    
    def add(self) -> str:
        name = inflect.engine().plural(self.__name.lower())
        content = f"'{name}' => \App\Http\Controllers\Api\V1\{self.__name}Controller::class,"


        if self.__content.find(self.__search) >= 0 and self.__content.find(content) == -1:
            self.__content = self.__content.replace(self.__search, f"{self.__search}\n\t\t{content}")
        else:
            i = self.__content.rindex('use ')
            j = self.__content.index('\n', i)

            search = f"{self.__content[i:j]}\n\n" 

            if self.__content.find(content) == -1:
                self.__content = self.__content.replace(search, f"{search}{self.__search}\n\t\t{content}\n" + "});\n")

        with open(self.__path + 'api.php', mode="w", encoding="utf-8") as file:
            file.write(self.__content)

        return self.__path

    def remove(self):
        name = inflect.engine().plural(self.__name.lower())
        content = f"'{name}' => \App\Http\Controllers\V1\{self.__name}Controller::class,"
        res = self.__content.find(content) >= 0

        self.__content = self.__content.replace(content, '')

        with open(self.__path + "api.php", mode="w", encoding="utf-8") as file:
            file.write(self.__content)

        return res
