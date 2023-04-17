#Instalar requirements con "pip install -r requirements.txt"

import RPi.GPIO as GPIO
from scipy.signal import firwin, lfilter
import numpy as np

# Configura los parámetros del filtro FIR
fs = 44100   # frecuencia de muestreo
fc = 1000    # frecuencia de corte
numtaps = 1000  # número de taps en el filtro

# Crea un filtro FIR con los parámetros dados
nyquist_rate = fs / 2.0
cutoff_norm = fc / nyquist_rate
taps = firwin(numtaps, cutoff_norm)

# Configura los pines GPIO
mic_pin = 7   # número físico del pin de entrada del micrófono
GPIO.setmode(GPIO.BOARD)
GPIO.setup(mic_pin, GPIO.IN)

# Configura el búfer de entrada y la salida
buf_len = numtaps
in_buf = np.zeros(buf_len)
out_buf = np.zeros(buf_len)

# Loop de procesamiento de señal
while True:
    # Lee la entrada del micrófono en el búfer de entrada
    in_buf[:-1] = in_buf[1:]
    in_buf[-1] = GPIO.input(mic_pin)

    # Aplica el filtro FIR al búfer de entrada
    out_buf[:-1] = out_buf[1:]
    out_buf[-1] = np.dot(taps, in_buf)

    # Envía la salida a través de una interfaz de salida
    # (por ejemplo, un altavoz o una conexión de red)
    # en este ejemplo, simplemente imprimimos la salida en la consola
    print(out_buf[-1])
