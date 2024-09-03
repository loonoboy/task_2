import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import argparse
import sys

#создание графика
def plot_graph(data, title, lb1, lb2):
    df = pd.read_csv(data, names=['time', 'temp1', 'temp2'], sep=';')
    df['time'] = df['time'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    plt.figure()
    plt.plot(df['time'], df['temp1'], label=lb1)
    plt.plot(df['time'], df['temp2'], label=lb2)
    plt.xlabel('Время')
    plt.ylabel('Температура (°C)')
    plt.title(title)
    plt.legend(loc='best')
    plt.show()
    plt.close()

#парсер строки консоли
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='data1.csv', help='Путь к файлу данных')
    parser.add_argument('--title', type=str, default='Изменение температуры', help='Заголовок графика')
    parser.add_argument('--sensor_1', type=str, default='Датчик 1', help='Наименование 1 датчика')
    parser.add_argument('--sensor_2', type=str, default='Датчик 2', help='Наименование 2 датчика')
 
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
 
    plot_graph(data=namespace.data, title=namespace.title, lb1=namespace.sensor_1, lb2=namespace.sensor_2)
