import scipy.signal as signal
import numpy as np
import wave
import matplotlib.pyplot as plt
import librosa

# Abrir archivo WAV
with wave.open('grabacion.wav', 'r') as audio_file:
    # Obtener los datos de audio
    audio_data = audio_file.readframes(-1)
    # Obtener la tasa de muestreo del audio
    sample_rate = audio_file.getframerate()




audio_data = np.frombuffer(audio_data, dtype=np.int16)
window = signal.hann(441000)
audio_data = audio_data * window

fft_audio = np.fft.fft(audio_data)
freq, response = signal.freqz(fft_audio)
transfer_function = np.abs(response)

plt.figure()
plt.plot(freq, transfer_function)
plt.title('Función de transferencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.show()

x = int(input('Ingrese la opcion: '))
if x == 1:
    # Cargar el archivo de audio WAV grabado en el microcofono debidamente filtrado 
    audio_data, sample_rate = librosa.load('grabacion.wav', sr=None, mono=True)

    # Reemplazar esta parte para abrir el archivo de audio wav capturado en el filtro mecanico
    inv_audio_data = np.flip(audio_data)

    # Calcular la correlación cruzada
    corr = np.correlate(audio_data, inv_audio_data, mode='full')

    # Normalizar la correlación cruzada
    corr_norm = corr / np.max(corr)

    # Graficar la correlación cruzada
    
    plt.plot(corr_norm)
    plt.xlabel('Desplazamiento')
    plt.ylabel('Coeficiente de correlación')
    plt.show()

    #Este código cargará un archivo de audio WAV, invertirá la señal de audio 
    # y calculará los coeficientes de correlación cruzada entre la señal de audio original 
    # y la señal invertida. Luego, normalizará los valores de correlación para que el valor máximo sea 1 
    # y graficará los coeficientes de correlación cruzada en función del desplazamiento.
    # Los coeficientes de correlación cruzada indican el grado de similitud entre dos señales de audio en función del desplazamiento.
    #  Si los coeficientes son altos para un desplazamiento dado, significa que las dos señales son muy similares en ese punto. 
    # Si los coeficientes son bajos o negativos, significa que las dos señales son muy diferentes en ese punto.