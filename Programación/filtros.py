import scipy.io.wavfile as wav
import scipy.signal as signal

# Cargar el archivo de audio
fs, audio = wav.read('grabacion.wav')

# Menú de selección de filtro
print("Seleccione el tipo de filtro que desea aplicar: ")
print("1. Pasa bajos")
print("2. Pasa altos")
print("3. Rechaza banda")
print("4. Pasa banda")
opcion = int(input("Opción: "))

if opcion == 1:
    # Filtro pasa bajos
    fc = int(input("Ingrese la frecuencia de corte: "))
    b, a = signal.butter(5, fc/(fs/2), 'low')
    audio_filtrado = signal.filtfilt(b, a, audio)
    wav.write('audio_pasa_bajos.wav', fs, audio_filtrado)
    print("Audio filtrado con éxito.")
    
elif opcion == 2:
    # Filtro pasa altos
    fc = int(input("Ingrese la frecuencia de corte: "))
    b, a = signal.butter(5, fc/(fs/2), 'high')
    audio_filtrado = signal.filtfilt(b, a, audio)
    wav.write('audio_pasa_altos.wav', fs, audio_filtrado)
    print("Audio filtrado con éxito.")
    
elif opcion == 3:
    # Filtro rechaza banda
    f1 = int(input("Ingrese la frecuencia inferior de la banda: "))
    f2 = int(input("Ingrese la frecuencia superior de la banda: "))
    b, a = signal.butter(5, [f1/(fs/2), f2/(fs/2)], 'bandstop')
    audio_filtrado = signal.filtfilt(b, a, audio)
    wav.write('audio_rechaza_banda.wav', fs, audio_filtrado)
    print("Audio filtrado con éxito.")
    
elif opcion == 4:
    # Filtro pasa banda
    f1 = int(input("Ingrese la frecuencia inferior de la banda: "))
    f2 = int(input("Ingrese la frecuencia superior de la banda: "))
    b, a = signal.butter(5, [f1/(fs/2), f2/(fs/2)], 'bandpass')
    audio_filtrado = signal.filtfilt(b, a, audio)
    wav.write('audio_pasa_banda.wav', fs, audio_filtrado)
    print("Audio filtrado con éxito.")
    
else:
    print("Opción inválida.")
