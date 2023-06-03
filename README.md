# _CONSOLE-ENGINE_
Описание библиотеки:
Многосторонний модуль, для разных задач
![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)
![MIT](https://img.shields.io/badge/license-MIT%20License-green)

# Тестировалось на:
- Python 3.10.0
- Windows 10 (22H2)

# ДОКУМЕНТАЦИЯ НЕ АКТУАЛЬНА

# Classes
|[Classes](https://github.com/Sinus44/Console-Engine#Classes)|Описание|
|-|-|
|[Admin](https://github.com/Sinus44/Console-Engine#class-Admin)|Запуск от имени адмнистратора|
|[Byte](https://github.com/Sinus44/Console-Engine#class-Byte)|Работа с данными BYTES-HEX-DEC-STRING|
|[BMP](https://github.com/Sinus44/Console-Engine#class-BMP)|Импорт файлов *.bmp, получение данных из файла и их структуризация|
|[Color](https://github.com/Sinus44/Console-Engine#class-Color)|Работа с цветами для консоли|
|[Config](https://github.com/Sinus44/Console-Engine#class-Config)|Обработка конфигурационных файлов *.cfg, чтение, запись, автосохранение|
|[EBM](https://github.com/Sinus44/Console-Engine#class-EBM)|Импорт файлов *.ebm, получение данных из файла и их структуризация|
|[ImageBMP](https://github.com/Sinus44/Console-Engine#class-ImageBMP)|Импорт картинок пригодных для вставки в Window, из формата *.bmp|
|[ImageEBM](https://github.com/Sinus44/Console-Engine#class-ImageEBM)|Импорт картинок пригодных для вставки в Window, из формата *.ebm|
|[Input](https://github.com/Sinus44/Console-Engine#class-Input)|Обработка входящих событий окна консоли|
|[Interval](https://github.com/Sinus44/Console-Engine#class-Interval)|Цикличный вызов функции в соответветсвии с интервалом|
|[Logging](https://github.com/Sinus44/Console-Engine#class-Logging)|Запись отладочной информации в файл|
|[Mmath](https://github.com/Sinus44/Console-Engine#class-Mmath)|Математические функции|
|[Output](https://github.com/Sinus44/Console-Engine#class-Output)|Настройка выходного буффера окна консоли|
|[Performance](https://github.com/Sinus44/Console-Engine#class-Performance)|Замер времени выполнения кода|
|[Scene](https://github.com/Sinus44/Console-Engine#class-Scene)|Управления отображаемыми сценами|
|[Sound](https://github.com/Sinus44/Console-Engine#class-Sound)|Воспроизведение звуков из WAV файлов|
|[Vector](https://github.com/Sinus44/Console-Engine#class-Vector)|Векторы и математические функции для них|
|[Window](https://github.com/Sinus44/Console-Engine#class-Window)|Изображение в консоли|
|[Events](https://github.com/Sinus44/Console-Engine#class-Events)|[GUI] Шаблоны событий для GUI элементов|
|[Element](https://github.com/Sinus44/Console-Engine#class-Element)|[GUI] База для GUI элементов|
|[Style](https://github.com/Sinus44/Console-Engine#class-Style)|[GUI] Настройка цветов для GUI элементов|
|[Border](https://github.com/Sinus44/Console-Engine#class-Border)|[GUI] Рамка для изображения|
|[Button](https://github.com/Sinus44/Console-Engine#class-Button)|[GUI] Кнопка|
|[Checkbox](https://github.com/Sinus44/Console-Engine#class-Checkbox)|[GUI] Переключатель|
|[Textbox](https://github.com/Sinus44/Console-Engine#class-Textbox)|[GUI] Текстовое поле|
|[Group](https://github.com/Sinus44/Console-Engine#class-Group)|[GUI] Группа GUI элементов|
|[Frame](https://github.com/Sinus44/Console-Engine#class-Frame)|[GUI] Основа кадра и заливка фона|
|[Grid](https://github.com/Sinus44/Console-Engine#class-Grid)|[GUI] Визуальная сетка|
|[Label](https://github.com/Sinus44/Console-Engine#class-Label)|[GUI] Текст|
|[Table](https://github.com/Sinus44/Console-Engine#class-Table)|[GUI] Таблица|
## Class Admin
Запуск от имени адмнистратора
### Методы:

### checkAdmin()
Проверяет запущен ли скрипт с правами администратора
Возвращает: (bool) - True если скрипт запущен с правами администратора

### restartAsAdmin()
Перезапускает скрипт с правами администратора

## Class Byte
Работа с данными BYTES-HEX-DEC-STRING
### Методы:

### stringToBytes()
Преобразует строку в байты
Принимает: (string) string - входная строка
Возвращает: (bytes) - Массив байтов

### hexToFixedHex()
Добавляет нули до определенного кол-ва длины всей строки
Принимает: (string) hex - строка с содержимым формата hex, (int) length - длинна которую необходимо достичь

### bytesToInt()
Преобразует BYTES в INT
Принимает: (bytes) b - Байт
Возвращает: (int) - число

### bytesToHex()
Преобразует BYTES в HEX
Принимает: (bytes) b - Массив байтов
Возвращает: (string) - Строка формата hex

### hexStringToBytes()
Преобразует HEX_STRING в BYTES
Принимает: (string) hex - строка формата hex
Возвращает: (bytes) - массив байт

### hexToBytes()
Преобразует HEX в BYTES
Принимает: (string) hex - hex-байт
Возвращает: (bytes) - байт

### hexToDec()
Преобразует HEX в INT
Принимает: (string) hex - hex-байт
Возвращает: (int) - число

### decToHex()
Преобразует INT в HEX
Принимает: (int) dec - число
Возвращает: (string) hex - строка формата hex

### decToBytes()
Преобразует INT в BYTES
Принимает: (int) dec - число
Возвращает: (bytes) - массив байт

### getHexByte()
Возвращает HEX_BYTE из HEX_STRING по номеру позиции
Принимает: (string) hex - строка формата hex, (int) pos - позиция необходимого байта
Возвращает: (string) hex - hex-байт

### getHexBytesSize()
Возвращает HEX_BYTES из HEX_STRING с начальной позиции указанной длиной
Принимает: (string) hex - строка формата hex, (int) pos - позиция необходимого байта, (int) size - кол-во необходимых байт
Возвращает: (string) - строка формата hex

### getHexBytesNormal()
Возвращает HEX_BYTES из HEX_STRING по номеру позиции начальной и конечной
Принимает: (string) hex - строка формата hex, (int) startPos - начальная позиция, (int) endPos - конечная позиция
Возвращает: (string) - строка формата hex

### getHexBytesReverse()
Возвращает HEX_BYTES из HEX_STRING по номеру позиции начальной и конечной, обратный порядок байт
Принимает: (string) hex - строка формата hex, (int) startPos - начальная позиция, (int) endPos - конечная позиция
Возвращает: (string) - строка формата hex

## Class BMP
Импорт файлов *.bmp, получение данных из файла и их структуризация
### Методы:

### \_\_init\_\_()
Конструктор
Принимает: (string) path - путь к файлу

## Class Color
Работа с цветами для консоли
### Методы:

### rgbBackground()
Возвращает символ-код установки цвета фона
Принимает: (int) r - красная составляющая, (int) g - зеленая составляющая, (int) b - синяя составляющая
Возвращает: (string) - цвет код для консоли

### rgbText()
Возвращает символ-код установки цвета основного текста
Принимает: (int) r - красная составляющая, (int) g - зеленая составляющая, (int) b - синяя составляющая
Возвращает: (string) - цвет код для консоли

## Class Config
Обработка конфигурационных файлов *.cfg, чтение, запись, автосохранение
### Методы:

### \_\_init\_\_()
Конструктор
Принимает: (string) path - путь к cfg файлу, (bool) autosave - автосохранение файла

### setSection()
Установить значение всей секции
Принимает: (string) key - имя секции, (string) value - значение секции

### setParam()
Установить значение в запись секции
Принимает: (string) section - имя секции, (string) key - ключ, (string) value - значение записи

### read()
Чтение файла

### write()
Запись в файл

## Class EBM
Импорт файлов *.ebm, получение данных из файла и их структуризация
### Методы:

### \_\_init\_\_()
Конструктор
Принимает: (string) path - путь к файлу

### convertArrayToEBM()
Преобразует массив в EMB
Принимает: (3_array_int) array - 3х мерный массив int содержащий цвета пикселей

### readFromFile()
Чтение из файла

### readFromHex()
Чтение из hex строки
Принимает: (string) hex - строка формата hex

### saveToFile()
Сохранение в файл
Принимает: (string) fileName - название файла

## Class ImageBMP
Импорт картинок пригодных для вставки в Window, из формата *.bmp
### Методы:

### \_\_init\_\_()
Конструктор
Принимает: (sting) path - путь к файлу, (bool) alpha - использовать прозрачность

### getColor()
Внутренний метод для преобразования кортежа цвета в символ-код
Принимает: (tuple) color - цвет
Возвращает: (string) - символ код цвета OR (int) - 0 если alpha канал

## Class ImageEBM
Импорт картинок пригодных для вставки в Window, из формата *.ebm
### Методы:

### \_\_init\_\_()
Конструктор
Принимает: (sting) path - путь к файлу, (bool) alpha - использовать прозрачность

### getColor()
Внутренний метод для преобразования кортежа цвета в символ-код
Принимает: (tuple) color - цвет
Возвращает: (string) - символ код цвета OR (int) - 0 если alpha канал

## Class Input
Обработка входящих событий окна консоли
### Методы:

### init()
Включает получение событий
Принимает: (bool) useHotkey - использование горячих клавиш, (bool) lineInput - описание отсутствует, (bool) echo - добавление в выходной массив, (bool) resizeEvents - принятие событий изменения размеров окна, (bool) mouseEvents - принятие событий мыши, (bool) insert - включает insert, (bool) quickEdit - выделение мышью, (bool) extended - запрет quickEdit

### reset()
Отчистка входного буффера

### varInit()
Сброс / инициализация переменных

### tick()
Получение и запись событий

## Class Interval
Цикличный вызов функции в соответветсвии с интервалом
### Методы:

### \_\_init\_\_()
Конструктор
Принимает: (function) callback - функция для вызова, (float) t - время в секундах, (bool) daemon - закрытие потока при закрытии главного потока

### start()
Запускает цикл

### stop()
Останавливает цикл

### function()
Метод котоый будет запущен в отдельном потоке

## Class Logging
Запись отладочной информации в файл
### Методы:

### log()
Логирование в файл
Принимает: (*strings) - строки для логгирования

### print()
Логирование в консольnПринимает: (*strings) - строки для логгирования

## Class Mmath
Математические функции
### Методы:

### round()
Правильное математическое округление
Принимает: (float OR int) x - число
Возвращает: (int) x - округленное число

### clamp()
Ограничение значения минимальным и максимальным
Принимает: (float OR int) x - число, (float OR int) maxValue - максимальное значение, (float OR int) minValue - минимальное значение
Возвращает: (float OR int) - число в заданном диапазоне

## Class Output
Настройка выходного буффера окна консоли
### Методы:

### init()
Иницаилизация окна консоли
Принимает: (int) mode - режим работы

### getTitle()
Получение заголовка окна консоли
Возвращает: (string) - текущий заголовок окна консоли

### title()
Установка заголовка окна консоли
Принимает: (string) title - строка заголовок

### resize()
Установка размера буффера окна консоли (в символах)
Принимает: (int) w - ширина окна консоли, (int) h - высота окна консоли

## Class Performance
Замер времени выполнения кода
### Методы:

### start()
Указывает начальное время отсчета

### time()
Возвращает время прошедшее с точки отсчета
Возвращает: (float) - время в секундах

### function()
Возвращает время выполнения функции
Принимает: (function) f - функция для тестирования, (int) repeats - кол-во повторений 1го замера, (int) count - кол-во замеров
Возвращает: (float) - время в секундах

## Class Scene
Управления отображаемыми сценами
### Методы:

### set()
Установка сцены по имени
Принимает: (string) name - имя сцены

### add()
Добавление сцены
Принимает: (string) name - имя сцены, (Scene) scene - сцена

### addFromDict()
Импорт сцен из объекта формата { name:scene }
Принимает: (array_dict_name_scene) scenes - массив сцен для добавления

### play()
Воспроизведение сцены

## Class Sound
Воспроизведение звуков из WAV файлов
### Методы:

### \_\_init\_\_()
Конструктор
Принимает: (string) filePath - Путь к файлу для воспроизведения

### play()
Начинает воспроизведение

### stop()
Остановка воспроизведения

## Class Vector
Векторы и математические функции для них
### Методы:

### \_\_init\_\_()
Коструктор
Принимает: (float) x - координата x, (float) y - координата y

### length()
Длина вектора
Возвращает: (float) - длина вектора

### \_\_add\_\_()
Сложение векторов
Принимает: (Vector or float or int) y - второй член
Возвращает: (Vector) - сам себя

## Class Window
Изображение в консоли
### Методы:

### \_\_init\_\_()
Конструктор
Принимает: (int) w - ширина, (int) h - высота

### print()
Описание отсутсвует

### draw()
Вывод буффера в консоль

### clear()
Отчистка вывода в консоль
Принимает: (bool) fast - если True - сдвиг изображения вверх

### fill()
Заливка всего буффера
Принимает: (string) symbol - символ для заливки

### point()
Установка символа в буффер по координатам
Принимает: (int) x - координата x, (int) y - координата y, (string) symbol - символ для заливки

### rectFill()
Заполненный прямоугольник в буффер
Принимает: (int) x - координата x, (int) y - координата y, (int) w - ширина, (int) h - высота, (string) symbol - символ для заливки

### rect()
Пустотелый прямоугольник в буффер
Принимает: (int) x - координата x, (int) y - координата y, (int) w - ширина, (int) h - высота, (string) symbol - символ для заливки

### circleFill()
Залитый круг в буффер
Принимает: (int) x - координата x, (int) y - координата y, (int) r - радиус, (string) symbol - символ для заливки

### circle()
Пустотелый круг в буффер
Принимает: (int) x - координата x, (int) y - координата y, (int) r - радиус, (string) symbol - символ для заливки

### line()
Линия по координатам
Принимает: (int) x1 - координата x1, (int) y1 - координата y1, (int) x2 - координата x2, (int) y2 - координата y2, (string) symbol - символ для заливки

### paste()
Вставка буффера другого объекта в текущий
Принимает: (Window) - Окно из которого копировать, (int) x - кооридната x, (int) y - коорината y

### text()
Текст
Принимает: (string) text - текст, (int) x - кооридната x, (int) y - коорината y, (string) wordPrefix - префикс перед текстом, (string) symbolPrefix - префикс перед символом, (string) wordPostfix - постфикс после текста, (string) symbolPostfix - постфикс после символа

## Class Events
[GUI] Шаблоны событий для GUI элементов
### Методы:

### click()
Нажатие
Принимает: (object) obj - инициатор события

### change()
Изменение состояние
Принимает: (object) obj - инициатор события

### focus()
Наведение мышью на элемент
Принимает: (object) obj - инициатор события

### select()
Выбор элемента
Принимает: (object) obj - инициатор события

## Class Element
[GUI] База для GUI элементов
### Методы:

### \_\_init\_\_()
Коснтруктор
Принимает: (Window) screen - окно в котором необходимо рисовать, (Style) style - стиль, (int) x - коорината x, (int) y - координата y, (string) text - текст, (bool) enable - состояние, (bool) visible - отрисовывать ли элемент

### block()
Блокировка элемента

### intersectionFromEvent()
Проверка на пересечение с мышью из события
(Event) - событие

### intersection()
Проверка на пересечение по координатам
Принимает: (int) x - координата x, (int) y - координата y

## Class Style
[GUI] Настройка цветов для GUI элементов
### Методы:

### \_\_init\_\_()
конструктор

### importFromConfig()
Иморт стилей из файла конфигураций
Принимает: (Config) cfg - файл конфигурации

## Class Border
[GUI] Рамка для изображения
### Методы:

### \_\_init\_\_()
Конструктор
Принимает: (Window) screen - окно в котором необдимо рисовать, (Style) style - стиль, (string) symbol - символ

### draw()
Отрисовка

## Class Button
[GUI] Кнопка
### Методы:

### draw()
Отрисовка

## Class Checkbox
[GUI] Переключатель
### Методы:

### \_\_init\_\_()
Коснтруктор
Принимает: (Window) screen - окно в котором необходимо рисовать, (Style) style - стиль, (int) x - коорината x, (int) y - координата y, (string) text - текст, (bool) enable - состояние, (bool) checked - отмечен ли чекбокс

### \_\_bool\_\_()
Возвращает состояние переключателя
Возвращает: (bool) - отмечена ли чекбокс

### click()
Событие нажатия
Принимает: (object) obj - инициатор события

### draw()
Отрисовка

## Class Textbox
[GUI] Текстовое поле
### Методы:

### \_\_init\_\_()
Коснтруктор
Принимает: (Window) screen - окно в котором необходимо рисовать, (Style) style - стиль, (int) x - коорината x, (int) y - координата y, (string) text - текст, (bool) enable - состояние, (int) maxLength - максимальная длина текста, (string) alphabet - алфавит доступных для ввода символов

### \_\_str\_\_()
Возвращает текст из текствого поля
Возвращает: (string) - текст из текствого поля

### click()
Событие нажатия

### block()
Блокировка текстового поля

### inputFromEvent()
Обработка нажатий клавиатуры
Принимает: (Event) event - событие

### draw()
Отрисовка

## Class Group
[GUI] Группа GUI элементов
### Методы:

### \_\_init\_\_()
Конструктор
Принимает: (Winow) screen - окно для отрисовки, (int) x - кооридната x, (int) y - координата y, (int) interval - интервал между элементами, (int) maxElements - максимальное кол-во элеметов для отрисовки

### append()
Добавление элементов в группу
Принимает: (Element or any [GUI]) element - элемент для добавления в группу

### eventHandler()
Обработка событий для всех элементов в группе
Принимает: (Event) - событие

### click()
Обработка событий для всех элементов в группе

### sort()
Автопозиционирование элементов группы

### draw()
Отрисовка всех элементов группы

## Class Frame
[GUI] Основа кадра и заливка фона
### Методы:

### \_\_init\_\_()
[GUI] База кадра и фона
Принимает: (Window) screen - окно для отрисовки, (Style) style - стиль

### draw()
Отрисовка

## Class Grid
[GUI] Визуальная сетка
### Методы:

### \_\_init\_\_()
Коструктор
Принимает: (Window) screen - окно для отрисовки, (int) x - координата x, (int) y - координата y, (int) w - ширина, (int) h - высота, (int) columns - кол-во столбцов, (int) strings - кол-во строк, (Style) style - стиль

### intersection()
Вовзращает координаты в сетке
Принимает: (int) x - координата x, (int) y - координата y
Возвращает: (tuple_int) - координаты ячейки по которой нажали

### draw()
Отрисовка

## Class Label
[GUI] Текст
### Методы:

### \_\_init\_\_()
Коснтруктор
Принимает: (Window) screen - окно в котором необходимо рисовать, (Style) style - стиль, (int) x - коорината x, (int) y - координата y, (string) text - текст, (int) maxLength - максимальная длинна текста в символах, (bool) enable - состояние, (bool) visible - отрисовывать ли элемент

### draw()
Отрисовка

## Class Table
[GUI] Таблица
### Методы:

### \_\_init\_\_()
Конструктор
Принимает: (Window) screen - окно для отрисовки, (Style) - стиль, (int) x - x координата, (int) y - y координата, (int) w - ширина, (int) h - высота

### resize()
Перерасчет размеров таблицы

### click()
Нажатие
Принимает: (object) obj - инициатор события

### block()
Блокировка текстового поля

### inputFromEvent()
Обработка нажатий клавиатуры
Принимает: (Event) event - событие

### draw()
Отрисовка

