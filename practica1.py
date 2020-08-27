import sys
sys.path.insert (1, 'dsp-modulo')
from thinkdsp import SinSignal
from thinkdsp import CosSignal
from thinkdsp import decorate

#modulo para mostrar graficas
import matplotlib.pyplot as plt

#Crear senoidal signal
seno = SinSignal(freq=400, amp=0.7, offset=0)
cos = SinSignal (freq=800, amp=1.1, offset=0)


#Crear grafica en memoria, asignamos propiedades
seno.plot()
decorate(xlabel='Tiempo (s)')
decorate(ylabel='Amplitud')

cos.plot()


#muestra grafica
plt.show()



