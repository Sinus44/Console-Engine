# _CONSOLE-ENGINE_
Описание: Описание:
Многосторонний модуль, для разных задач
![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)
![MIT](https://img.shields.io/badge/license-MIT%20License-green)

# Используется в:
- [SnakeCE](https://github.com/Sinus44/SnakeCE)
- [LabGenCE](https://github.com/Sinus44/LabGenCE)
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
## Class Color
Описание:
Работа с цветами для консоли
### Методы:
### rgb\_background(r: int, g: int, b: int)
Возвращает: str
Описание:
Получение символ-кода установки цвета фона

### rgb\_text(r: int, g: int, b: int)
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
Закрытый метод. Переназначение приведет к ошибкам.

### \_get\_()

Описание:
Закрытый метод. Переназначение приведет к ошибкам.

### input\_init()

Описание:
Инициализация ввода

### input\_tick()
Возвращает: tuple
Описание:
Получение ивентов

### print()

Описание:
Вывод в консоль

### set\_size(w: int, h: int)

Описание:
Смена размера консоли

### set\_title(title: str)

Описание:
Смена заголовка

### set\_icon(path: str)

Описание:
Смена иконки

### close()

Описание:
Закрытие окна

### get\_size()

Описание:
Получение размеров окна

### \_\_del\_\_()

Описание:
Закрытый метод. Переназначение приведет к ошибкам.

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



### selected()

Описание:
Выполняется при выборе сцены

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



### set(name: str)

Описание:
Установка сцены по имени

### add(name: str, scene: object)

Описание:
Добавление сцены

### add\_from\_dict(scenes: dict)

Описание:
Импорт сцен из словаря

### \_draw\_()



### \_update\_()



### play()

Описание:
Начинает воспроизведение сцены

### remove(name: str)

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
### \_\_init\_\_(file_path: str)

Описание:
Примает путь к файлу для воспроизведения

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
### \_\_init\_\_(char: str, background_color: str, text_color: str)

Описание:
char - сам символ, background_color - цвет фона, text_color - цвет текста

## Class Window
Описание:
Изображение в консоли
### Методы:
### \_\_init\_\_(w: int, h: int)

Описание:
Принимает ширину и высоту экрана

### input\_tick()

Описание:
Получение ивентов окна

### set\_title()

Описание:
Установка заголовка окна

### set\_icon()

Описание:
Установка иконки окна

### close()

Описание:
Закрытие окна

### set\_size(w: int, h: int)

Описание:
Изменение размеров окна

### print()

Описание:
Вывод буффера в консоль

### clear()

Описание:
Отчистка вывода в консоль

### fill(symbol: object)

Описание:
Заливка всего буффера определенным символом

### point(x: int, y: int, symbol: object)

Описание:
Установка символа в буффер по координатам

### rect\_fill(x: int, y: int, w: int, h: int, symbol: object)

Описание:
Заполненный прямоугольник в буффер

### rect(x: int, y: int, w: int, h: int, symbol: object)

Описание:
Пустотелый прямоугольник в буффер

### circle\_fill(x: int, y: int, r: int, symbol: object)

Описание:
Залитый круг

### circle(x: int, y: int, r: int, symbol: object)

Описание:
Пустотелый круг

### line(x1: int, y1: int, x2: int, y2: int, symbol: object)

Описание:
Линия по координатам

### text(x: int, y: int, text: str, background_color: str, text_color: str)

Описание:
Текст

### table()

Описание:
Таблица данных в консоли

### is\_enable()



