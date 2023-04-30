import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal

# Cargar archivo de audio
fs, audio = wavfile.read('filtromecanico.wav')

# Aplicar transformada de Fourier
f, Pxx = signal.periodogram(audio, fs)

# Obtener función de transferencia del filtro
H = np.sqrt(Pxx)

# Graficar respuesta en frecuencia del filtro
plt.figure()
plt.plot(f, H)

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid()


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
