# Ближайшие бары

После запуска скрипт запросит ввести GPS координаты (широту и долготу), на их основании
будет произведен расчет и поиск ближайшего бара в .json файле с даными о московских барах
так же в нём будут найдены самый большой и самый маленький бар.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
а так же .json файл содержащий информацию о московских барах
(скачать файл можно по ссылке https://devman.org/fshare/1503831681/4/)
в параметрах при запуске скрипта необходимо передать путь и имя .json файла с барами
Запуск на Linux:

```bash

$ python bars.py bars.json # possibly requires call of python3 executive instead of just python
# пример ответа скрипта
Укажите долготу(longitude) вашего местоположения (например 37.35805): 37.358059205668638
Укажите широту(latitude) вашего местоположения (например: 55.846144): 55.846144758987947

Самый большой бар носит название: Спорт бар «Красная машина»
Самый маленький бар носит название: БАР. СОКИ
Ближайший бар носит название: Staropramen
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
