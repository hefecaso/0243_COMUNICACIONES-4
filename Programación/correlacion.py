import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

# Cargar los archivos de audio
fs1, audio1 = wav.read('audio_rechaza_banda.wav')
fs2, audio2 = wav.read('filtromecanico.wav')

# Normalizar los audios
audio1 = audio1 / np.max(np.abs(audio1))
audio2 = audio2 / np.max(np.abs(audio2))

# Obtener la correlación cruzada
corr = signal.correlate(audio1, audio2, mode='full', method='auto')

# Normalizar la correlación cruzada
corr = corr / np.max(np.abs(corr))

# Graficar la correlación cruzada
plt.plot(corr)
plt.title('Correlación cruzada entre audio1 y audio2')
plt.xlabel('Retardo')
plt.ylabel('Correlación')
plt.show()

# Determinar si los audios son similares o no
umbral = 0.9
max_corr = np.max(corr)
if max_corr > umbral:
    print("Los audios son similares (coeficiente de correlación cruzada: %.2f)" % max_corr)
else:
    print("Los audios no son similares (coeficiente de correlación cruzada: %.2f)" % max_corr)
