# _CONSOLE-ENGINE_
Описание: Модуль для пользовательских приложений в консоли
![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)

## Import
```python
import Core
```

## Classes
|[Classes](https://github.com/Sinus44/console-engine#Classes)|Описание|
|-|-|
|[Byte](https://github.com/Sinus44/console-engine#Byte)|Класс для работы с данными BYTES HEX DEC|
|[BMP](https://github.com/Sinus44/console-engine#BMP)|Импорт файлов *.bmp и получение большенства данных из файла и их структуризация|
|[EBM](https://github.com/Sinus44/console-engine#EBM)|Импорт файлов *.ebm и получение большенства данных из файла и их структуризация|
|[Color](https://github.com/Sinus44/console-engine#Color)|Класс цветов|
|[Config](https://github.com/Sinus44/console-engine#Config)|Класс для обработки конфигурационных файлов .cfg с возможностью чтения, записи, автосохранения|
|[ImageBMP](https://github.com/Sinus44/console-engine#ImageBMP)|Импорт картинок пригодных для вставки в Window|
|[ImageEBM](https://github.com/Sinus44/console-engine#ImageEBM)|Импорт картинок пригодных для вставки в Window|
|[Logging](https://github.com/Sinus44/console-engine#Logging)|Класс вывода отладочной информации / записи логов в файл|
|[Input](https://github.com/Sinus44/console-engine#Input)|Класс для получения входных ивентов консоли|
|[Interval](https://github.com/Sinus44/console-engine#Interval)|Класс цикличного вызова функции в соответветсвии с интервалом|
|[Mmath](https://github.com/Sinus44/console-engine#Mmath)|Некоторые математические формулы|
|[Output](https://github.com/Sinus44/console-engine#Output)|Класс для настройки выходного буффера окна консоли|
|[Performance](https://github.com/Sinus44/console-engine#Performance)|Класс оценки производительности, замеров времени выполнения кода, по точкам или функции|
|[Scene](https://github.com/Sinus44/console-engine#Scene)|Класс для управления отображаемыми сценами|
|[Sound](https://github.com/Sinus44/console-engine#Sound)|Класс звуков, импорт из файла воспроизведение ускорение замедление, остановка|
|[Vector](https://github.com/Sinus44/console-engine#Vector)|Класс векторов|
|[Window](https://github.com/Sinus44/console-engine#Window)|Окно - Класс окна для отрисовки ИЗО в консоли|
|[Events](https://github.com/Sinus44/console-engine#Events)|Шаблоны Event'ов для GUI элементов|
|[Element](https://github.com/Sinus44/console-engine#Element)|Мульти класс для большенства GUI элементов|
|[Style](https://github.com/Sinus44/console-engine#Style)|Стиль - настройки цветов и прочего для GUI элементов|
|[Border](https://github.com/Sinus44/console-engine#Border)|Рамка для окна|
|[Button](https://github.com/Sinus44/console-engine#Button)|GUI - элемент Кнопка|
|[Checkbox](https://github.com/Sinus44/console-engine#Checkbox)|GUI - элемент чек бокс|
|[Textbox](https://github.com/Sinus44/console-engine#Textbox)|GUI элемент для ввода текста пользователем|
|[Group](https://github.com/Sinus44/console-engine#Group)|Группа GUI элементов, авто позиционнирование элементов в соответсвии с интервалом и координатами группы|
|[Frame](https://github.com/Sinus44/console-engine#Frame)|Основа кадра и заливка фона|
|[Grid](https://github.com/Sinus44/console-engine#Grid)|Визуальный разделитель окна в соответсвии с кол-вом столбцов и строк|
|[Label](https://github.com/Sinus44/console-engine#Label)|GUI - элемент текст|

## Class Byte
|Метод|Описание|
|-|-|
|bytesToHex | Преобразует BYTES в строку с HEX|
|getHexByte | Возвращает байт в виде HEX из HEX строки по номеру позиции|
|getHexBytesSize | Возвращает байты в виде HEX из HEX строки по номеру позиции и кол-ва|
|getHexBytesNormal | Возвращает байты в виде HEX из HEX строки по номеру позиции начальной и конечной|
|getHexBytesReverse | Возвращает байты в виде HEX из HEX строки по номеру позиции начальной и конечной обратный порядок байт|
|hexToDec | Преобразует HEX в INT|
|decToHex | Преобразует INT в HEX|

## Class BMP
|Метод|Описание|
|-|-|
|__init__ | Импорт файлов *.bmp и получение большенства данных из файла и их структуризация|

## Class EBM
|Метод|Описание|
|-|-|
|__init__ | Импорт файлов *.ebm и получение большенства данных из файла и их структуризация|

## Class Color
|Метод|Описание|
|-|-|
|rgb | Возвращает символ-код установки цвета основного текста|

## Class Config
|Метод|Описание|
|-|-|
|__init__ | Класс для обработки конфигурационных файлов .cfg с возможностью чтения, записи, автосохранения|
|setSection | Установить значение всей секции|
|setParam | Установить значение в запись секции|
|read | Чтение файла|
|write | Запись в файл|

## Class ImageBMP
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|getColor | Описание отсутсвует|

## Class ImageEBM
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|getColor | Описание отсутсвует|

## Class Logging
|Метод|Описание|
|-|-|
|log | Логирование в файл|

## Class Input
|Метод|Описание|
|-|-|
|init | Описание отсутсвует|
|start | Описание отсутсвует|
|stop | Описание отсутсвует|
|mode | Описание отсутсвует|
|tick | Описание отсутсвует|
|clearEvents | Описание отсутсвует|
|getEvents | Описание отсутсвует|

## Class Interval
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|start | Запускает цикл|
|stop | Останавливает цикл|
|function | Описание отсутсвует|

## Class Mmath
|Метод|Описание|
|-|-|
|round | Правильное математическое округление|
|clamp | Ограничение значения минимальным и максимальным|

## Class Output
|Метод|Описание|
|-|-|
|init | Описание отсутсвует|
|mode | Описание отсутсвует|
|getTitle | Описание отсутсвует|
|title | Описание отсутсвует|
|resize | Описание отсутсвует|

## Class Performance
|Метод|Описание|
|-|-|
|start | Описание отсутсвует|
|time | Описание отсутсвует|
|function | Описание отсутсвует|

## Class Scene
|Метод|Описание|
|-|-|
|set | Установка сцены по имени|
|add | Добавление сцены|
|addFromDict | Импорт сцен из объекта формата { name:scene }|
|play | Воспроизведение сцены|

## Class Sound
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|p | Описание отсутсвует|
|speed | Описание отсутсвует|
|play | Описание отсутсвует|
|volume | Описание отсутсвует|
|stop | Описание отсутсвует|

## Class Vector
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|length | Длина вектора|
|__add__ | Сложение векторов|

## Class Window
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|draw | Вывод буффера в консоль|
|clear | Отчистка вывода в консоль|
|fill | Заливка всего буффера|
|point | Установка символа в буффер по координатам|
|rectFill | Заполненный прямоугольник в буффер|
|rect | Пустотелый прямоугольник в буффер|
|circleFill | Залитый круг в буффер|
|circle | Пустотелый круг в буффер|
|line | Линия по координатам|
|paste | Вставка буффера другого объекта в текущий|
|text | Текст|

## Class Events
|Метод|Описание|
|-|-|
|click | Описание отсутсвует|
|change | Описание отсутсвует|
|focus | Описание отсутсвует|
|select | Описание отсутсвует|

## Class Element
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|block | Описание отсутсвует|
|intersectionFromEvent | Описание отсутсвует|
|intersection | Описание отсутсвует|

## Class Style
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|importFromConfig | Иморт стилей из файла конфигураций|

## Class Border
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|draw | Описание отсутсвует|

## Class Button
|Метод|Описание|
|-|-|
|draw | Описание отсутсвует|

## Class Checkbox
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|__bool__ | Описание отсутсвует|
|click | Описание отсутсвует|
|draw | Описание отсутсвует|

## Class Textbox
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|__str__ | Описание отсутсвует|
|click | Описание отсутсвует|
|block | Описание отсутсвует|
|inputFromEvent | Описание отсутсвует|
|draw | Описание отсутсвует|

## Class Group
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|append | Описание отсутсвует|
|eventHandler | Описание отсутсвует|
|click | Описание отсутсвует|
|sort | Описание отсутсвует|
|draw | Описание отсутсвует|

## Class Frame
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|draw | Описание отсутсвует|

## Class Grid
|Метод|Описание|
|-|-|
|__init__ | Описание отсутсвует|
|intersection | Описание отсутсвует|
|draw | Описание отсутсвует|

## Class Label
|Метод|Описание|
|-|-|
|draw | Описание отсутсвует|

## License
![MIT](https://img.shields.io/badge/license-MIT%20License-green)
