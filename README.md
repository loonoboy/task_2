# Программа для построения графиков на основе данных из CSV-файла
Эта программа предназначена для построения графика на основе данных, содержащихся в файле формата CSV.

# Установка
Для запуска программы необходимо установить Python и необходимые модули: pandas, matplotlib и argparse.

# Использование
Программа принимает следующие аргументы командной строки:

--data — путь к файлу данных; -обязательный аргумент
--title — заголовок графика;
--sensor_1 — наименование первого датчика;
--sensor_2 — наименование второго датчика.
Пример использования:
```
python task_2.py --title "Изменение температуры"
```
# Ограничения
Программа может работать только с данными, содержащимися в CSV-файле. Данные должны содержать столбцы «time», «temp1» и «temp2».
