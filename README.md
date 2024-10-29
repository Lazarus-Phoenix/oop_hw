# Проект OOP Homework
![Image alt](htmlcov/Screenshot 2024-10-29 at 19-55-41 Coverage report.png)

Этот проект представляет собой домашнюю работу базовый пример использования объектно-ориентированного программирования (OOP) в Python.

## Структура проекта

### Основные классы

1. `Product`:
   - Представляет товар со свойствами: имя, описание, цена, количество.
   - Имеет метод `__init__()` для инициализации объекта.
   - Для класса Product переопределен метод str, который возвращает строку: Название продукта, X руб. Остаток: X шт.
   - Для класса Product создан класс-метод new_product который 
   будет принимать на вход параметры товара в словаре и возвращать созданный объект класса Product
   - Для класса Product сделаны атрибут цены приватным и описаны геттеры и сеттеры.

2. `Category`:
   - Представляет категорию товаров со свойствами: имя, описание, список продуктов.
   - Имеет статические переменные для подсчета количества категорий и продуктов.
   - Имеет метод `__init__()` для инициализации объекта.
   - Функциональность для добавления продуктов в категорию.
   - Реализована проверка: в случае если цена равна или ниже нуля, выводится сообщение в консоль “Цена не должна быть нулевая или отрицательная” 
   - Реализована логика подтверждения пользователем согласия понизить цену. В случае если пользователь вручную вводит y (значит yes) цена товара понижается, если n (значит no) происходит отмена действия. 
   - Для класса Category переопределен метод str, который возвращает строку: Название категории, количество продуктов: X шт. 
   - Метод str рассчитывает общее количество товаров на складе (quantity) для каждого продукта в приватном атрибуте products

## Использование

Пример создания и использования объектов:
Запустите модуль crs.main.py с примерами ввода и получения обработанных данных.