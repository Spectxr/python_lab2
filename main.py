# 50% кода сгенерировано ИИ.

filename = "C:/Users/User/Documents/Audacity/16.wav"

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import dst
from scipy.io import wavfile


def load_wav_file(file_name):
    """Загрузка wav файла"""

    # Чтение частоты дискретизации и массива отсчетов
    sample_rate, data = wavfile.read(file_name)

    # Если файл стерео, оставляем только левый канал
    if data.ndim > 1:
        data = data[:, 0]
    return sample_rate, data


def get_number_of_samples(max_samples):
    """Ввод количества отображаемых отсчётов"""

    while True:
        try:
            value = int(input(f"Введите количество отсчетов " f"(от 1 до {max_samples}): "))
            if 1 <= value <= max_samples:
                return value
            print("Число вне допустимого диапазона.")

        except ValueError:
            print("Введите целое число.")


def plot_samples(samples):
    """Линейный график с закрашенной областью"""

    # Номера отсчётов по оси x
    x = np.arange(len(samples))

    plt.figure(figsize=(10, 5))
    plt.plot(x, samples, label="Сигнал")
    plt.fill_between(x, samples, alpha=0.3)
    plt.title(f"Дискретные отсчеты звукового сигнала ({len(samples)} отсчётов)")
    plt.xlabel("Номер отсчета")
    plt.ylabel("Амплитуда, отн. ед.")
    plt.grid(True)
    plt.legend()


def plot_oscillogram(data, sample_rate):
    """Осциллограмма сигнала"""

    # Перевод номеров отсчётов во время
    time = np.arange(len(data)) / sample_rate

    plt.figure(figsize=(10, 5))
    plt.plot(time, data)
    plt.title("Осциллограмма звукового сигнала")
    plt.xlabel("Время, с")
    plt.ylabel("Амплитуда, отн. ед.")
    plt.grid(True)


def plot_dst_spectrum(data, sample_rate):
    """Спектральный анализ методом DST"""

    # Преобразование отсчётов в вещественный тип
    signal = data.astype(float)

    # Дискретное синусное преобразование
    spectrum = dst(signal, type=2, norm="ortho")

    n = len(signal)

    # Формирование частотной шкалы
    frequencies = np.arange(n) * sample_rate / (2 * n)

    plt.figure(figsize=(10, 5))
    plt.plot(frequencies, np.abs(spectrum))
    plt.title("Спектр сигнала")
    plt.xlabel("Частота, Гц")
    plt.ylabel("Амплитуда, отн. ед.")
    plt.grid(True)


def plot_histogram(data):
    """Гистограмма отсчетов сигнала"""

    plt.figure(figsize=(10, 5))

    # Разбиение диапазона значений на 50 интервалов
    plt.hist(data, bins=50)

    plt.title("Гистограмма отсчетов сигнала")
    plt.xlabel("Амплитуда, отн. ед.")
    plt.ylabel("Количество отсчетов")
    plt.grid(True)


def main():

    # Проверка существования файла
    if not Path(filename).exists():
        print("Ошибка: файл не найден.")
        return

    try:
        sample_rate, data = load_wav_file(filename)

        print(f"Частота дискретизации: {sample_rate} Гц")
        print(f"Количество отсчетов: {len(data)}")

        # Ввод количества отображаемых отсчётов
        number_of_samples = get_number_of_samples(len(data))

        selected_samples = data[:number_of_samples]

        plot_samples(selected_samples)
        plot_oscillogram(data, sample_rate)
        plot_dst_spectrum(data, sample_rate)
        plot_histogram(data)
        plt.show()

    except Exception as error:
        print(f"Ошибка при обработке файла: {error}")


if __name__ == "__main__":
    main()
