from jinja2 import Environment, FileSystemLoader
import os
from core.BaseClass import BaseClass
from datetime import datetime

class Migration(BaseClass):
    __name: str = ''
    __path: str = ''
    __content: str = ''


    def __init__(self, name: str, project_path: str = os.getcwd(), path: str = 'database/migrations/', template: str = 'Migration.stub') -> None:
        self.__name = name.title()
        self.__path = f"{project_path}/{path}/{self.__get_table_name(self.__name)}.php"


        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template(template)

        self.__content = template.render(model=f"{self._get_plural_name(self._snake_case(self.__name))}")


    
    def make(self) -> str:
        with open(self.__path, mode="w", encoding="utf-8") as file:
            file.write(self.__content)

        return self.__path

    def remove(self):
        if os.path.exists(self.__path):
            os.remove(self.__path)
            return True
        
        return False


    def __get_table_name(self, name: str):
        return f"{datetime.now().strftime('%Y_%m_%d_%H%M%S')}_create_{self._get_plural_name(self._snake_case(self.__name))}_table.php"