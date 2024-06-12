from abc import ABC, abstractmethod
import os
from config import ROOT_DIR

#from pathlib import Path
#проверка наличия директории
#if Path("ROOT_DIR/data").exists():
#    self.path = os.path.join('data', file_name)
#else:
#    print("Directory does not exist")

class SaveFile(ABC):

    @abstractmethod
    def write_file(self):
        pass


class JSONWorker(SaveFile):
    def __init__(self, file_name: str):
        self.path = os.path.join('data', file_name)

    def read_file(self):
        with open(self.path) as file:
            return json.load(file)

    def write_file(self, data):
        with open(self.path, 'w') as file:
            return json.dump(data, file, indent=4, ensure_ascii=False)

    #def add_vacancy(self, vacanc: Vacancy):
        vac_info = vacancy.to_json()
        file_content: list[dict] = self.read_file()
        file_content.append(vac_info)
        self.write_file(file_content)
