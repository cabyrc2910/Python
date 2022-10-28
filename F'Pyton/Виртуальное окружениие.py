
from ctypes import pythonapi
from gc import freeze
from gettext import install
from multiprocessing import Pipe
from os import pipe, pipe2
import pipes
from pydoc import pipepager
from urllib import request
import venv


python -m venv new_venv #- создать виртуальное окружение
# source venv/bin/activate #- активация ВО для линукс
venv\Scripts\activate  #- активация в виндоус (обязательно \ - обратный слэш)
deactivate #- деактивация виртуального окружения
Pipe freeze #- распечатает установленные пакеты(библиотеки) (создаёт файл зависимостей)
pipe install #-U pip setuptools - U-сокращенно upgrade, далее следуют имя или имена модулей, которые требуется обновить, в данном случае setuptools
pythonapi.exe #-m pip install -U pip setuptools #- тоже самое
pipepager install request lxml #- установка библиотек requests и lxml - если нужно установить несколько библиотек, то командой  pip uninstall lxml #- можно перечислить их через пробел, - lxml - удаление библиотеки
pipes freeze > requirements.txt #- создаёт файл с зависимостями (в нём прописываются все библиотеки и версии нашего проекта)
pipe2 install -r requirements.txt #- устанавливаем все библиотеки с зависимостями

cd #- перейти в нужную папку
cd.. #- на уровень выше

#Что делать если pycharm не видит библиотеку
https://www.youtube.com/watch?v=3SvmrzqVmXo
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment