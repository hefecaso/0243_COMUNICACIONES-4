import numpy as np
import wave
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal

# Abrir archivo WAV
with wave.open('filtromecanico.wav', 'r') as audio_file:
    # Obtener los datos de audio
    audio_data = audio_file.readframes(-1)
    # Obtener la tasa de muestreo del audio
    sample_rate = audio_file.getframerate()

audio_data = np.frombuffer(audio_data, dtype=np.int16)
window = np.hanning(len(audio_data))
audio_data = audio_data * window

# Calculamos la transformada de Fourier
fourier = np.fft.fft(audio_data)

# Obtenemos la magnitud y la fase de la transformada
magnitud = np.abs(fourier)
fase = np.angle(fourier)

# Obtenemos la respuesta en frecuencia
freq = np.fft.fftfreq(len(audio_data), 1/sample_rate)[:len(audio_data)//2]
response = magnitud[:len(audio_data)//2] * np.exp(1j*fase[:len(audio_data)//2])
transfer_function = np.abs(response)

# Cargar archivo de audio para el analisis de la funcion de transferencia
fs, audio = wavfile.read('filtromecanico.wav')

# Aplicar transformada de Fourier
f, Pxx = signal.periodogram(audio, fs)

# Obtener función de transferencia del filtro
H = np.sqrt(Pxx)



plt.figure()
plt.plot(freq, transfer_function)

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')


# Determinar tipo de filtro
if np.max(H) == 1.0:
    plt.title('El filtro es un filtro pasabajos')
    plt.show()
elif np.min(H) == 0.0:
    plt.title('El filtro es un filtro pasaltos')
    plt.show()
elif np.max(H) < 1.0:
    print('El filtro es un filtro pasa banda')
    plt.show()
else:
    plt.title('El filtro es un filtro rechaza banda')
    plt.show()