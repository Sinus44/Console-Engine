# _CONSOLE-ENGINE_
Описание: Описание:
Многосторонний модуль, для разных задач
![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)
![MIT](https://img.shields.io/badge/license-MIT%20License-green)

# Тестировалось на:
- Python 3.10.0
- Windows 10 (22H2)

# Classes
|[Classes](https://github.com/Sinus44/Console-Engine#Classes)|Описание|
|-|-|
|[Color](https://github.com/Sinus44/Console-Engine#class-Color)|Работа с цветами для консоли|
|[Console](https://github.com/Sinus44/Console-Engine#class-Console)|Работа с отдельным окном консоли|
|[Input](https://github.com/Sinus44/Console-Engine#class-Input)|Обработка входящих событий окна консоли|
|[Logging](https://github.com/Sinus44/Console-Engine#class-Logging)|Запись отладочной информации в файл|
|[Performance](https://github.com/Sinus44/Console-Engine#class-Performance)|Замер времени выполнения кода|
|[Scene](https://github.com/Sinus44/Console-Engine#class-Scene)|Экземпляр сцены|
|[Scene_Control](https://github.com/Sinus44/Console-Engine#class-Scene_Control)|Управления отображаемыми сценами|
|[Sound](https://github.com/Sinus44/Console-Engine#class-Sound)|Воспроизведение звуков из WAV файлов|
|[Window](https://github.com/Sinus44/Console-Engine#class-Window)|Основной класс для работы с графикой в консоли|
|[Events](https://github.com/Sinus44/Console-Engine#class-Events)|[GUI] Шаблоны событий для GUI элементов|
|[Element](https://github.com/Sinus44/Console-Engine#class-Element)|[GUI] База для GUI элементов|
|[Border](https://github.com/Sinus44/Console-Engine#class-Border)|[GUI] Рамка для изображения|
|[Button](https://github.com/Sinus44/Console-Engine#class-Button)|[GUI] Кнопка|
|[Checkbox](https://github.com/Sinus44/Console-Engine#class-Checkbox)|[GUI] Переключатель|
|[Textbox](https://github.com/Sinus44/Console-Engine#class-Textbox)|[GUI] Текстовое поле|
|[Group](https://github.com/Sinus44/Console-Engine#class-Group)|[GUI] Группа GUI элементов|
|[Frame](https://github.com/Sinus44/Console-Engine#class-Frame)|[GUI] Фона|
|[Grid](https://github.com/Sinus44/Console-Engine#class-Grid)|[GUI] Визуальная сетка|
|[Style](https://github.com/Sinus44/Console-Engine#class-Style)|[GUI] Настройка цветов для GUI элементов|
|[Label](https://github.com/Sinus44/Console-Engine#class-Label)|[GUI] Текст|
|[Table](https://github.com/Sinus44/Console-Engine#class-Table)|[GUI] Таблица|
## Class Color
Описание:
Работа с цветами для консоли
### Методы:

### rgb\_background(r:int, g:int, b:int)
Возвращает: str
Описание:
Возвращает символ-код цвета фона

### rgb\_text(r:int, g:int, b:int)
Возвращает: str
Описание:
Возвращает символ-код цвета основного текста

## Class Console
Описание:
Работа с отдельным окном консоли
### Методы:

### \_\_init\_\_()



### \_send\_()



### \_get\_()



### input\_init()



### input\_tick()



### print()



### set\_size(w:int, h:int)



### set\_title(title:str)



### set\_icon(path:str)



### close()



### get\_size()



### \_\_del\_\_()



## Class Input
Описание:
Обработка входящих событий окна консоли
### Методы:

### init()

Описание:
Включает получение событий

### tick()

Описание:
Получение и запись событий

## Class Logging
Описание:
Запись отладочной информации в файл
### Методы:

### log(text:str)

Описание:
Логирование в файл

### print(text:str, end:str)

Описание:
Логирование в консоль

## Class Performance
Описание:
Замер времени выполнения кода
### Методы:

### start()

Описание:
Указывает начальное время отсчета

### time()
Возвращает: float
Описание:
Возвращает время прошедшее с точки отсчета

### function(repeats:int, count:int)
Возвращает: float
Описание:
Возвращает время выполнения функции

## Class Scene
Описание:
Экземпляр сцены
### Методы:

### \_\_init\_\_()



### remove()



### play()



### select()



## Class Scene_Control
Описание:
Управления отображаемыми сценами
### Методы:

### \_\_init\_\_()



### set(name:str)

Описание:
Установка сцены по имени

### add(name:str, scene:object)

Описание:
Добавление сцены

### addFromDict(scenes:dict)

Описание:
Импорт сцен из словаря

### play()

Описание:
Воспроизведение сцены

## Class Sound
Описание:
Воспроизведение звуков из WAV файлов
### Методы:

### \_\_init\_\_(filePath:str)



### play()

Описание:
Начинает воспроизведение

### stop()

Описание:
Остановка воспроизведения

## Class Window
Описание:
Основной класс для работы с графикой в консоли
### Методы:

### \_\_init\_\_(w:int, h:int)

Описание:
Принимает консоль с которой необходимо взаимодействовать

### set\_size()



### print()

Описание:
Вывод буффера в консоль

### clear()

Описание:
Отчистка вывода в консоль

### fill(symbol:str)

Описание:
Заливка всего буффера определенным символом

### point(x:int, y:int, symbol:int)

Описание:
Установка символа в буффер по координатам

### rectFill(x:int, y:int, w:int, h:int, symbol:str)

Описание:
Заполненный прямоугольник в буффер

### rect(x:int, y:int, w:int, h:int, symbol:str)

Описание:
Пустотелый прямоугольник в буффер

### circleFill(x:int, y:int, r:int, symbol:str)

Описание:
Залитый круг в буффер

### circle()

Описание:
Пустотелый круг в буффер

### line()

Описание:
Линия по координатам

### paste()

Описание:
Вставка буффера другого объекта в текущий

### text(x:int, y:int, text:str, text_prefix:str, symbol_prefix:str, text_postfix:str, symbol_postfix:str)

Описание:
Текст

## Class Events
Описание:
[GUI] Шаблоны событий для GUI элементов
### Методы:

### click()

Описание:
Нажатие
Принимает: (object) obj - инициатор события

### change()

Описание:
Изменение состояние
Принимает: (object) obj - инициатор события

### focus()

Описание:
Наведение мышью на элемент
Принимает: (object) obj - инициатор события

### select()

Описание:
Выбор элемента
Принимает: (object) obj - инициатор события

## Class Element
Описание:
[GUI] База для GUI элементов
### Методы:

### \_\_init\_\_()

Описание:
Коснтруктор
Принимает: (Window) screen - окно в котором необходимо рисовать, (Style) style - стиль, (int) x - коорината x, (int) y - координата y, (string) text - текст, (bool) enable - состояние, (bool) visible - отрисовывать ли элемент

### block()

Описание:
Блокировка элемента

### intersectionFromEvent()

Описание:
Проверка на пересечение с мышью из события
(Event) - событие

### intersection()

Описание:
Проверка на пересечение по координатам
Принимает: (int) x - координата x, (int) y - координата y

## Class Border
Описание:
[GUI] Рамка для изображения
### Методы:

### \_\_init\_\_()

Описание:
Конструктор
Принимает: (Window) screen - окно в котором необдимо рисовать, (Style) style - стиль, (string) symbol - символ

### draw()

Описание:
Отрисовка

## Class Button
Описание:
[GUI] Кнопка
### Методы:

### draw()

Описание:
Отрисовка

## Class Checkbox
Описание:
[GUI] Переключатель
### Методы:

### \_\_init\_\_()

Описание:
Коснтруктор
Принимает: (Window) screen - окно в котором необходимо рисовать, (Style) style - стиль, (int) x - коорината x, (int) y - координата y, (string) text - текст, (bool) enable - состояние, (bool) checked - отмечен ли чекбокс

### \_\_bool\_\_()

Описание:
Возвращает состояние переключателя
Возвращает: (bool) - отмечена ли чекбокс

### click()

Описание:
Событие нажатия
Принимает: (object) obj - инициатор события

### draw()

Описание:
Отрисовка

## Class Textbox
Описание:
[GUI] Текстовое поле
### Методы:

### \_\_init\_\_()

Описание:
Коснтруктор
Принимает: (Window) screen - окно в котором необходимо рисовать, (Style) style - стиль, (int) x - коорината x, (int) y - координата y, (string) text - текст, (bool) enable - состояние, (int) maxLength - максимальная длина текста, (string) alphabet - алфавит доступных для ввода символов

### \_\_str\_\_()

Описание:
Возвращает текст из текствого поля
Возвращает: (string) - текст из текствого поля

### click()

Описание:
Событие нажатия

### block()

Описание:
Блокировка текстового поля

### inputFromEvent()

Описание:
Обработка нажатий клавиатуры
Принимает: (Event) event - событие

### draw()

Описание:
Отрисовка

## Class Group
Описание:
[GUI] Группа GUI элементов
### Методы:

### \_\_init\_\_()

Описание:
Конструктор
Принимает: (Winow) screen - окно для отрисовки, (int) x - кооридната x, (int) y - координата y, (int) interval - интервал между элементами, (int) maxElements - максимальное кол-во элеметов для отрисовки

### append()

Описание:
Добавление элементов в группу
Принимает: (Element or any [GUI]) element - элемент для добавления в группу

### eventHandler()

Описание:
Обработка событий для всех элементов в группе
Принимает: (Event) - событие

### click()

Описание:
Обработка событий для всех элементов в группе

### sort()

Описание:
Автопозиционирование элементов группы

### draw()

Описание:
Отрисовка всех элементов группы

## Class Frame
Описание:
[GUI] Фона
### Методы:

### \_\_init\_\_()

Описание:
[GUI] Фон 

### draw()

Описание:
Отрисовка

## Class Grid
Описание:
[GUI] Визуальная сетка
### Методы:

### \_\_init\_\_()

Описание:
Коструктор
Принимает: (Window) screen - окно для отрисовки, (int) x - координата x, (int) y - координата y, (int) w - ширина, (int) h - высота, (int) columns - кол-во столбцов, (int) strings - кол-во строк, (Style) style - стиль

### intersection()

Описание:
Вовзращает координаты в сетке
Принимает: (int) x - координата x, (int) y - координата y
Возвращает: (tuple_int) - координаты ячейки по которой нажали

### draw()

Описание:
Отрисовка

## Class Style
Описание:
[GUI] Настройка цветов для GUI элементов
### Методы:

### \_\_init\_\_()

Описание:
конструктор

### importFromConfig()

Описание:
Иморт стилей из файла конфигураций
Принимает: (Config) cfg - файл конфигурации

## Class Label
Описание:
[GUI] Текст
### Методы:

### \_\_init\_\_()

Описание:
Коснтруктор
Принимает: (Window) screen - окно в котором необходимо рисовать, (Style) style - стиль, (int) x - коорината x, (int) y - координата y, (string) text - текст, (int) maxLength - максимальная длинна текста в символах, (bool) enable - состояние, (bool) visible - отрисовывать ли элемент

### draw()

Описание:
Отрисовка

## Class Table
Описание:
[GUI] Таблица
### Методы:

### \_\_init\_\_()

Описание:
Конструктор
Принимает: (Window) screen - окно для отрисовки, (Style) - стиль, (int) x - x координата, (int) y - y координата, (int) w - ширина, (int) h - высота

### resize()

Описание:
Перерасчет размеров таблицы

### click()

Описание:
Нажатие
Принимает: (object) obj - инициатор события

### block()

Описание:
Блокировка текстового поля

### inputFromEvent()

Описание:
Обработка нажатий клавиатуры
Принимает: (Event) event - событие

### draw()

Описание:
Отрисовка

