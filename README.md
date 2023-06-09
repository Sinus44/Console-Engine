# _CONSOLE-ENGINE_
Описание: Описание:
Многосторонний модуль, для разных задач
![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)
![MIT](https://img.shields.io/badge/license-MIT%20License-green)

# Используется в:
- [SnakeCE](https://github.com/Sinus44/SnakeCE)
- [LabGenCE](https://github.com/Sinus44/SnakeCE)
- [FractalCE](https://github.com/Sinus44/FractalCE)
- [Console-TicTacToe](https://github.com/Sinus44/Console-TicTacToe)
- [EBMConsoleViewer](https://github.com/Sinus44/EBMConsoleViewer)


# Тестировалось на:
- Python 3.10.0
- Windows 10 (22H2)

# Classes
|[Classes](https://github.com/Sinus44/Console-Engine#Classes)|Описание|
|-|-|
|[Color](https://github.com/Sinus44/Console-Engine#class-Color)|Работа с цветами для консоли|
|[Console](https://github.com/Sinus44/Console-Engine#class-Console)|Создание дополнительного отдельного окна консоли|
|[Input](https://github.com/Sinus44/Console-Engine#class-Input)|Обработка входящих событий окна консоли|
|[Logging](https://github.com/Sinus44/Console-Engine#class-Logging)|Запись отладочной информации в файл|
|[Scene](https://github.com/Sinus44/Console-Engine#class-Scene)|Экземпляр сцены|
|[Scene_Control](https://github.com/Sinus44/Console-Engine#class-Scene_Control)|Управления отображаемыми сценами|
|[Sound](https://github.com/Sinus44/Console-Engine#class-Sound)|Воспроизведение звуков из WAV файлов|
|[Symbol](https://github.com/Sinus44/Console-Engine#class-Symbol)|Описывает символ в консоли|
|[Window](https://github.com/Sinus44/Console-Engine#class-Window)|Изображение в консоли|
|[Element](https://github.com/Sinus44/Console-Engine#class-Element)|[GUI] База для GUI элементов|
|[Border](https://github.com/Sinus44/Console-Engine#class-Border)|[GUI] Рамка для изображения|
|[Button](https://github.com/Sinus44/Console-Engine#class-Button)|[GUI] Кнопка|
|[Checkbox](https://github.com/Sinus44/Console-Engine#class-Checkbox)|[GUI] Чекбокс - Переключатель|
|[Textbox](https://github.com/Sinus44/Console-Engine#class-Textbox)|[GUI] Текстовое поле|
|[Group](https://github.com/Sinus44/Console-Engine#class-Group)|[GUI] Группа GUI элементов|
|[Frame](https://github.com/Sinus44/Console-Engine#class-Frame)|[GUI] Фон|
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
Получение символ-кода установки цвета фона

### rgb\_text(r:int, g:int, b:int)
Возвращает: str
Описание:
Получение символ-кода установки цвета основного текста

## Class Console
Описание:
Создание дополнительного отдельного окна консоли
### Методы:

### \_\_init\_\_()



### \_send\_()

Описание:
Байтовая отправка команд

### \_get\_()

Описание:
Байтовое принятие команд

### input\_init()

Описание:
Инициализация ввода

### input\_tick()

Описание:
Получение ивентов

### print()

Описание:
Вывод в консоль

### set\_size(w:int, h:int)

Описание:
Смена размера консоли

### set\_title(title:str)

Описание:
Смена заголовка

### set\_icon(path:str)

Описание:
Смена иконки

### close()

Описание:
Закрытие окна

### get\_size()

Описание:
Получение размеров окна

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
Получение событий

## Class Logging
Описание:
Запись отладочной информации в файл
### Методы:

### log()

Описание:
Логирование в файл

### print()

Описание:
Логирование в консоль

## Class Scene
Описание:
Экземпляр сцены
### Методы:

### \_\_init\_\_()



### start()

Описание:
Выполняется при запуске сцены

### update()

Описание:
Метод для обновления логики прилоежния

### draw()

Описание:
Метод для обновления отрисовки приложения

### remove()

Описание:
Вызывается при смене сцены

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

### add\_from\_dict(scenes:dict)

Описание:
Импорт сцен из словаря

### \_draw\_()



### \_update\_()



### play()

Описание:
Начинает воспроизведение сцены

### remove(name:str)

Описание:
Удаление сцены из списка

### remove\_all()

Описание:
Удаление всех сцен из списка

### stop()

Описание:
Остановка воспроизведения сцены

## Class Sound
Описание:
Воспроизведение звуков из WAV файлов
### Методы:

### \_\_init\_\_(file_path:str)



### play()

Описание:
Начинает воспроизведение

### stop()

Описание:
Остановка воспроизведения

## Class Symbol
Описание:
Описывает символ в консоли
### Методы:

### \_\_init\_\_(char:str, background_color:str, text_color:str)



## Class Window
Описание:
Изображение в консоли
### Методы:

### \_\_init\_\_(w:int, h:int)



### set\_size(w:int, h:int)

Описание:
Изменение размеров окна

### print()

Описание:
Вывод буффера в консоль

### clear()

Описание:
Отчистка вывода в консоль

### fill(symbol:object)

Описание:
Заливка всего буффера определенным символом

### point(x:int, y:int, symbol:object)



### rect\_fill(x:int, y:int, w:int, h:int, symbol:object)

Описание:
Заполненный прямоугольник в буффер

### rect(x:int, y:int, w:int, h:int, symbol:object)

Описание:
Пустотелый прямоугольник в буффер

### circle\_fill(x:int, y:int, r:int, symbol:object)

Описание:
Залитый круг в буффер

### circle(x:int, y:int, r:int, symbol:object)

Описание:
Пустотелый круг в буффер

### line(x1:int, y1:int, x2:int, y2:int, symbol:object)

Описание:
Линия по координатам

### text(x:int, y:int, text:str, background_color:str, text_color:str)

Описание:
Текст

### table()



## Class Element
Описание:
[GUI] База для GUI элементов
### Методы:

### \_\_init\_\_()



### block()

Описание:
Блокировка элемента

### intersection()

Описание:
Проверка на пересечение по координатам

### event()

Описание:
Передайте ивент для выполнения биндов

### on\_hover()

Описание:
Наведение мышью на элемент

### no\_hover()

Описание:
Ивент если мышь более не наведена на элемент

### on\_mouse\_up()

Описание:
Ивент отпускания кнопки мыши

### on\_left\_click()

Описание:
Ивент нажатия ЛКМ

### on\_right\_click()

Описание:
Ивент нажатия ЛКМ

### on\_change()

Описание:
Изменение состояние

### on\_select()

Описание:
Выбор элемента

## Class Border
Описание:
[GUI] Рамка для изображения
### Методы:

### \_\_init\_\_(window:object, style:object, symbol:str)



### draw()

Описание:
Отрисовка

## Class Button
Описание:
[GUI] Кнопка
### Методы:

### on\_hover()

Описание:
Мышь наведена

### no\_hover()

Описание:
Более мышь не наведена

### format()

Описание:
Формат кнопки

### draw()

Описание:
Отрисовка

## Class Checkbox
Описание:
[GUI] Чекбокс - Переключатель
### Методы:

### \_\_bool\_\_()

Описание:
Возвращает состояние переключателя

### on\_left\_click()

Описание:
Событие нажатия

### draw()

Описание:
Отрисовка

## Class Textbox
Описание:
[GUI] Текстовое поле
### Методы:

### \_\_init\_\_()



### \_\_str\_\_()

Описание:
Возвращает текст из текствого поля

### click()

Описание:
Событие нажатия

### block()

Описание:
Блокировка текстового поля

### inputFromEvent()

Описание:
Обработка нажатий клавиатуры

### draw()

Описание:
Отрисовка

## Class Group
Описание:
[GUI] Группа GUI элементов
### Методы:

### \_\_init\_\_(window:object, x:int, y:int, interval:int)



### append(element:object)

Описание:
Добавление элементов в группу

### eventHandler()

Описание:
Обработка событий для всех элементов в группе

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
[GUI] Фон
### Методы:

### \_\_init\_\_(window:object, style:object)



### draw()

Описание:
Отрисовка

## Class Grid
Описание:
[GUI] Визуальная сетка
### Методы:

### \_\_init\_\_(window:object, x:int, y:int, w:int, h:int, columns:int, strings:int, style:object)



### intersection(x:int, y:int)

Описание:
Вовзращает координаты в сетке

### draw()

Описание:
Отрисовка

## Class Style
Описание:
[GUI] Настройка цветов для GUI элементов
### Методы:

### \_\_init\_\_(text:str, text_fill:str, background:str, background_fill:str, disable:str)



## Class Label
Описание:
[GUI] Текст
### Методы:

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

