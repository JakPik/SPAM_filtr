#импорт модуля, который предоставляет фун-и для работы с операционкой
import os
class Corpus:
    def __init__(self, directory_path):
        self.directory_path = directory_path
#Это метод emails, который будет генератором. 
# Генератор позволяет проходить по email-ам по мере необходимости, не загружая их все сразу в память.     
    def emails(self):
        #проходится по всем фаулам директории и возвращает список их имён
        for filename in os.listdir(self.directory_path):
            #пропускает всё, что начинается !
            if filename.startswith('!'):
                continue
            #создаёт путь к текущему файлу
            file_path = os.path.join(self.directory_path, filename)
            with open(file_path, 'rt', encoding='utf-8') as f:
                # Возвращает из генератора кортеж с именем файла и его содержимым. 
                # yield используется для создания генератора, 
                # который возвращает данные по мере необходимости, а не загружает их все сразу.
                yield filename, f.read()
                