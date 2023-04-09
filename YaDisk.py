import requests
import os
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
        with open(file_path, 'rb') as f:
            header = self.get_headers()
            param = {"path": f'Загрузки/{os.path.basename(file_path)}', "overwrite": "true"}
            href = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload", headers=header, params=param).json().get("href","")
            resp = requests.put(href, files = {"file":f})
            resp.raise_for_status()
        if resp.status_code == 201:
            print('Successfully')
            return 
        else:
            print('Not successfully')
            return 



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file =r'C:\Users\Home_comp\Documents\PyProjects\README.txt'
    TOKEN = ''
    uploader = YaUploader(TOKEN)
    result = uploader.upload(path_to_file)

    

    
    




            