# _CONSOLE-ENGINE_
Описание: Модуль для пользовательских приложений в консоли

![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)

## Import
```python
import Engine
```

## Classes
|[Classes](https://github.com/Sinus44/console-engine#Classes)|Описание|
|-|-|
|[Admin](https://github.com/Sinus44/console-engine#class-Admin)|Запуск от имени адмнистратора|
|[Byte](https://github.com/Sinus44/console-engine#class-Byte)|Работа с данными BYTES-HEX-DEC-STRING|
|[BMP](https://github.com/Sinus44/console-engine#class-BMP)|Импорт файлов *.bmp, получение данных из файла и их структуризация|
|[EBM](https://github.com/Sinus44/console-engine#class-EBM)|Импорт файлов *.ebm, получение данных из файла и их структуризация|
|[Color](https://github.com/Sinus44/console-engine#class-Color)|Работа с цветами для консоли|
|[Config](https://github.com/Sinus44/console-engine#class-Config)|Обработка конфигурационных файлов *.cfg, чтение, запись, автосохранение|
|[ImageBMP](https://github.com/Sinus44/console-engine#class-ImageBMP)|Импорт картинок пригодных для вставки в Window, из формата *.bmp|
|[ImageEBM](https://github.com/Sinus44/console-engine#class-ImageEBM)|Импорт картинок пригодных для вставки в Window, из формата *.ebm|
|[Input](https://github.com/Sinus44/console-engine#class-Input)|Обработка входящих событий окна консоли|
|[Interval](https://github.com/Sinus44/console-engine#class-Interval)|Цикличный вызов функции в соответветсвии с интервалом|
|[Logging](https://github.com/Sinus44/console-engine#class-Logging)|Запись отладочной информации в файл|
|[Mmath](https://github.com/Sinus44/console-engine#class-Mmath)|Математические функции|
|[Output](https://github.com/Sinus44/console-engine#class-Output)|Настройка выходного буффера окна консоли|
|[Perceptron](https://github.com/Sinus44/console-engine#class-Perceptron)|Простой нейрон|
|[Performance](https://github.com/Sinus44/console-engine#class-Performance)|Замер времени выполнения кода|
|[Scene](https://github.com/Sinus44/console-engine#class-Scene)|Управления отображаемыми сценами|
|[Sound](https://github.com/Sinus44/console-engine#class-Sound)|Воспроизведение звуков из WAV файлов|
|[Vector](https://github.com/Sinus44/console-engine#class-Vector)|Векторы и математические функции для них|
|[Window](https://github.com/Sinus44/console-engine#class-Window)|Изображение в консоли|
|[Events](https://github.com/Sinus44/console-engine#class-Events)|[GUI] Шаблоны событий для GUI элементов|
|[Element](https://github.com/Sinus44/console-engine#class-Element)|[GUI] База для GUI элементов|
|[Style](https://github.com/Sinus44/console-engine#class-Style)|[GUI] Настройка цветов для GUI элементов|
|[Border](https://github.com/Sinus44/console-engine#class-Border)|[GUI] Рамка для изображения|
|[Button](https://github.com/Sinus44/console-engine#class-Button)|[GUI] Кнопка|
|[Checkbox](https://github.com/Sinus44/console-engine#class-Checkbox)|[GUI] Переключатель|
|[Textbox](https://github.com/Sinus44/console-engine#class-Textbox)|[GUI] Текстовое поле|
|[Group](https://github.com/Sinus44/console-engine#class-Group)|[GUI] Группа GUI элементов|
|[Frame](https://github.com/Sinus44/console-engine#class-Frame)|[GUI] Основа кадра и заливка фона|
|[Grid](https://github.com/Sinus44/console-engine#class-Grid)|[GUI] Визуальная сетка|
|[Label](https://github.com/Sinus44/console-engine#class-Label)|[GUI] Текст|
|[Table](https://github.com/Sinus44/console-engine#class-Table)|[GUI] Таблица|

## Class Admin
Запуск от имени адмнистратора
|Метод|Описание|
|-|-|
|checkAdmin|Возвращает True если скрипт запущен от имени администратора|
|restartAsAdmin|Перезапускает скрипт с правами администратора|

## Class Byte
Работа с данными BYTES-HEX-DEC-STRING
|Метод|Описание|
|-|-|
|stringToBytes|Описание отсутсвует|
|hexToFixedHex|Добавляет нули до определенного кол-ва длины всей строки|
|bytesToInt|Преобразует BYTES в INT|
|bytesToHex|Преобразует BYTES в HEX|
|hexStringToBytes|Преобразует HEX_STRING в BYTES|
|hexToBytes|Преобразует HEX в BYTES|
|hexToDec|Преобразует HEX в INT|
|decToHex|Преобразует INT в HEX|
|decToBytes|Преобразует INT в BYTES|
|getHexByte|Возвращает HEX_BYTE из HEX_STRING по номеру позиции|
|getHexBytesSize|Возвращает HEX_BYTES из HEX_STRING с начальной позиции указанной длиной|
|getHexBytesNormal|Возвращает HEX_BYTES из HEX_STRING по номеру позиции начальной и конечной|
|getHexBytesReverse|Возвращает HEX_BYTES из HEX_STRING по номеру позиции начальной и конечной, обратный порядок байт|

## Class BMP
Импорт файлов *.bmp, получение данных из файла и их структуризация
|Метод|Описание|
|-|-|
|__init__|Импорт файлов *.bmp, получение данных из файла и их структуризация|

## Class EBM
Импорт файлов *.ebm, получение данных из файла и их структуризация
|Метод|Описание|
|-|-|
|__init__|Импорт файлов *.ebm, получение данных из файла и их структуризация
		EBM(str path) - path-путь к файлу для чтения
		EBM(list path OR tuple path) - дву мерный массив кортежей цветов пикселей для конвертации в файл
		|
|convertArrayToEBM|Описание отсутсвует|
|readFromFile|Описание отсутсвует|
|readFromHex|Описание отсутсвует|
|saveToFile|Описание отсутсвует|

## Class Color
Работа с цветами для консоли
|Метод|Описание|
|-|-|
|rgbBackground|Возвращает символ-код установки цвета фона|
|rgbText|Возвращает символ-код установки цвета основного текста|

## Class Config
Обработка конфигурационных файлов *.cfg, чтение, запись, автосохранение
|Метод|Описание|
|-|-|
|__init__|Обработка конфигурационных файлов *.cfg, чтение, запись, автосохранение|
|setSection|Установить значение всей секции|
|setParam|Установить значение в запись секции|
|read|Чтение файла|
|write|Запись в файл|

## Class ImageBMP
Импорт картинок пригодных для вставки в Window, из формата *.bmp
|Метод|Описание|
|-|-|
|__init__|Импорт картинок пригодных для вставки в Window, из формата *.bmp|
|getColor|Внутренний метод для преобразования кортежа цвета в символ-код|

## Class ImageEBM
Импорт картинок пригодных для вставки в Window, из формата *.ebm
|Метод|Описание|
|-|-|
|__init__|Импорт картинок пригодных для вставки в Window, из формата *.ebm|
|getColor|Внутренний метод для преобразования кортежа цвета в символ-код|

## Class Input
Обработка входящих событий окна консоли
|Метод|Описание|
|-|-|
|init|Включает получение событий|
|tick|Получение событий, обработка и их запись в массив|
|clearEvents|Очистка массива событий|
|getEvents|Возвращает события|

## Class Interval
Цикличный вызов функции в соответветсвии с интервалом
|Метод|Описание|
|-|-|
|__init__|Цикличный вызов функции в соответветсвии с интервалом|
|start|Запускает цикл|
|stop|Останавливает цикл|
|function|Метод котоый будет запущен в отдельном потоке|

## Class Logging
Запись отладочной информации в файл
|Метод|Описание|
|-|-|
|log|Логирование в файл|
|print|Логирование в консоль|

## Class Mmath
Математические функции
|Метод|Описание|
|-|-|
|round|Правильное математическое округление|
|clamp|Ограничение значения минимальным и максимальным|

## Class Output
Настройка выходного буффера окна консоли
|Метод|Описание|
|-|-|
|init|Иницаилизация окна консоли|
|getTitle|Получение заголовка окна консоли|
|title|Установка заголовка окна консоли|
|resize|Установка размера буффера окна консоли (в символах)|

## Class Perceptron
Простой нейрон
|Метод|Описание|
|-|-|
|__init__|Описание отсутсвует|
|exp|Возвращает экспоненту числа|
|derivative|Производная функции активации|
|activation|Функция активации|
|predict|Предсказывает выхоное значение исходя из входных данных|
|learn|Обучение нейрона с учителем|
|learnNoLearer|Обучение нейрона с без учителя|

## Class Performance
Замер времени выполнения кода
|Метод|Описание|
|-|-|
|start|Указывает начальное время отсчета|
|time|Возвращает время прошедшее с точки отсчета|
|function|Возвращает время выполнения функции|

## Class Scene
Управления отображаемыми сценами
|Метод|Описание|
|-|-|
|set|Установка сцены по имени|
|add|Добавление сцены|
|addFromDict|Импорт сцен из объекта формата { name:scene }|
|play|Воспроизведение сцены|

## Class Sound
Воспроизведение звуков из WAV файлов
|Метод|Описание|
|-|-|
|__init__|
        desc: Воспроизведение звуков из WAV файлов
        in: (str) filePath - Путь к файлу для воспроизведения
        |
|play|Начинает воспроизведение|
|stop|Остановка воспроизведения|

## Class Vector
Векторы и математические функции для них
|Метод|Описание|
|-|-|
|__init__|Векторы и математические функции для них|
|length|Длина вектора|
|__add__|Сложение векторов|

## Class Window
Изображение в консоли
|Метод|Описание|
|-|-|
|__init__|Изображение в консоли|
|print|Описание отсутсвует|
|draw|Вывод буффера в консоль|
|clear|Отчистка вывода в консоль|
|fill|Заливка всего буффера|
|point|Установка символа в буффер по координатам|
|rectFill|Заполненный прямоугольник в буффер|
|rect|Пустотелый прямоугольник в буффер|
|circleFill|Залитый круг в буффер|
|circle|Пустотелый круг в буффер|
|line|Линия по координатам|
|paste|Вставка буффера другого объекта в текущий|
|text|Текст|

## Class Events
[GUI] Шаблоны событий для GUI элементов
|Метод|Описание|
|-|-|
|click|Нажатия|
|change|Изменение состояние (Textbox, Checkbox)|
|focus|Наведение мышью на элемент|
|select|Выбор элемента (Textbox)|

## Class Element
[GUI] База для GUI элементов
|Метод|Описание|
|-|-|
|__init__|[GUI] База для GUI элементов|
|block|Блокировка элемента|
|intersectionFromEvent|Проверка на пересечение с мышью из события|
|intersection|Проверка на пересечение по координатам|

## Class Style
[GUI] Настройка цветов для GUI элементов
|Метод|Описание|
|-|-|
|__init__|[GUI] Настройка цветов для GUI элементов|
|importFromConfig|Иморт стилей из файла конфигураций|

## Class Border
[GUI] Рамка для изображения
|Метод|Описание|
|-|-|
|__init__|[GUI] Рамка для изображения|
|draw|Отрисовка|

## Class Button
[GUI] Кнопка
|Метод|Описание|
|-|-|
|draw|Отрисовка|

## Class Checkbox
[GUI] Переключатель
|Метод|Описание|
|-|-|
|__init__|[GUI] Переключатель|
|__bool__|Возвращает состояние переключателя|
|click|Событие нажатия|
|draw|Отрисовка|

## Class Textbox
[GUI] Текстовое поле
|Метод|Описание|
|-|-|
|__init__|[GUI] Текстовое поле|
|__str__|Возвращает текст из текствого поля|
|click|Событие нажатия|
|block|Блокировка текстового поля|
|inputFromEvent|Обработка нажатий клавиатуры|
|draw|Отрисовка|

## Class Group
[GUI] Группа GUI элементов
|Метод|Описание|
|-|-|
|__init__|[GUI] Группа GUI элементов|
|append|Добавление элементов в группу|
|eventHandler|Обработка событий для всех элементов в группе|
|click|Обработка событий для всех элементов в группе|
|sort|Автопозиционирование элементов группы|
|draw|Отрисовка всех элементов группы|

## Class Frame
[GUI] Основа кадра и заливка фона
|Метод|Описание|
|-|-|
|__init__|[GUI] База кадра и фона|
|draw|Отрисовка|

## Class Grid
[GUI] Визуальная сетка
|Метод|Описание|
|-|-|
|__init__|[GUI] Визуальная сетка|
|intersection|Вовзращает координаты в сетке|
|draw|Отрисовка|

## Class Label
[GUI] Текст
|Метод|Описание|
|-|-|
|__init__|[GUI] Текст|
|draw|Отрисовка|

## Class Table
[GUI] Таблица
|Метод|Описание|
|-|-|
|__init__|[GUI] Таблица|
|resize|Описание отсутсвует|
|click|Событие нажатия|
|block|Блокировка текстового поля|
|inputFromEvent|Обработка нажатий клавиатуры|
|draw|Отрисовка|

## License
![MIT](https://img.shields.io/badge/license-MIT%20License-green)