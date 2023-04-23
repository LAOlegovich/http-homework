import requests
import os, json
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

# Код реализации задания №2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        """Метод настраивает заголовок запроса"""
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
   
    def upload(self, file_path: str):
        """Метод загружает файл, расположенный в указанном пути локальной машины, на яндекс диск"""
        header = self.get_headers()
        param = {"path": f'Загрузки/{os.path.basename(file_path)}', "overwrite": "true"}
        link = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload", headers=header, params=param, stream = True)
        href = link.json().get("href","")
        with tqdm.wrapattr(open(file_path, 'rb'),"read", total = os.path.getsize(file_path), desc = f'Загрузка ...{os.path.basename(file_path)}', colour = "green", miniters = 1) as f:
            while True:
                chunk = f.read(40960)
                
                if not chunk:
                    break  
            resp = requests.put(href, files = {"file":f})       
        resp.raise_for_status()
        if resp.status_code == 201:
            print('Successfully')
            return 
        else:
            print('Not successfully')
        return 

def get_settings(key):
    with open(os.getcwd() + '/http_homework/settings.json','r',encoding= 'utf-8') as f_s:
        return json.load(f_s)[key]


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file =r'C:\Users\Home_comp\Documents\PyProjects\1.pdf'
    uploader = YaUploader(get_settings('token'))
    result = uploader.upload(path_to_file)

    

    
    




            