#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:00:53 2019

@author: solorzaj

La idea es modelar . En este modelo:
    Las celulas tienen un tamaño despreciable frente a las droplets. Son puntuales. Su distribucion viene modelada por el conjunto de puntos distribuidos de forma estadisticamente uniforme entre 0 y el valor que representa el volumen que contiene las celulas.
    

"""



#%%
#    #  Ruta Linux
#inroute = '/home/solorzaj/Documentos/Master/TFM/tfmjavier/'
outroute = '/home/solorzaj/Documentos/Master/TFM/tfmjavier/'

#   # Nombre de los ficheros
#infile_name = 'datapresion en contra.csv'

#%% Paquetes importados:

import datetime

import numpy as np
#from sympy.physics import units

#   Soporte de unidades físicas.
#from astropy import units as u 

#import random
np.random.seed(7)

#import math

#%% Delcaración de funciones

def encapsulados(vol_muestra, vol_droplet, distribucion_muestra):
    """
    Primera idea, quizás mas facil de entender pero exageradamente poco eficiente en comparación con el siguiente.
    
    np.random.seed(7)
    Para vol_droplet=1 vol_muestra=1E4 n_celulas=20000 , 0:00:52.920673 [0 1 2 3 4 5 6 7 8] [1351 2712 2691 1823  896  362  119   39    7]
    Para vol_droplet=1 vol_muestra=1E5 n_celulas=2000 , 0:00:59.481928
    Para vol_droplet=1 vol_muestra=1E5 n_celulas=20000 , 0:09:48.699224
[0 1 2 3 4] [81811 16502  1571   108     8]
    
    """
    n_droplets=int(vol_muestra/vol_droplet)
    
    for e in range(0,n_droplets,1):
        droplet=[]
        vol_inicio=e*vol_droplet
        vol_final=(e+1)*vol_droplet
        for i in range(0,n_celulas,1):
            if (distribucion_muestra[i]>=vol_inicio) and (distribucion_muestra[i]<vol_final):
                droplet.append(distribucion_muestra[i])
        droplets.append(droplet)
    
    return droplets



def encapsuladosss(vol_muestra, vol_droplet, distribucion_muestra):
    """
    np.random.seed(7)
    Para vol_droplet=1 vol_muestra=1E4 n_celulas=20000 , 0:00:00.090168
[0 1 2 3 4 5 6 7 8] [1351 2712 2691 1823  896  362  119   39    7]
    Para vol_droplet=1 vol_muestra=1E5 n_celulas=20000 , 0:00:00.344325 [0 1 2 3 4] [81806 16507  1571   108     8]
    Para vol_droplet=1 vol_muestra=3E6 n_celulas=2000000 ,0:00:18.111172 [0 1 2 3 4 5 6 7 8] [1539910 1027525  341993   75974   12652    1737     190      18       1]
    """
    
    n_droplets=int(vol_muestra/vol_droplet)
    distribucion_muestra.sort()
    pos_cel_siguiente_droplet=0
    
    for e in range(0,n_droplets,1):
        droplet=[]
        vol_final=(e+1)*vol_droplet
        for i in range(pos_cel_siguiente_droplet,n_celulas,1):
            if (distribucion_muestra[i]<vol_final):
                droplet.append(distribucion_muestra[i])
            else:
                pos_cel_siguiente_droplet=i
                break
                
        droplets.append(droplet)
    
    return droplets

#https://stackoverflow.com/questions/3410976/how-to-round-a-number-to-significant-figures-in-python
        
from math import log10, floor  
     
def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)

def vol_esfera_radio(r):
    return (4/3)*(np.pi)*(r**3)

def vol_esfera_diametro(d):
    return (1/6)*(np.pi)*(d**3)

#%%
#   Soporte de unidades físicas.
        
from astropy import units as u     

# Α α, Β β, Γ γ, Δ δ, Ε ε, Ζ ζ, Η η, Θ θ, Ι ι, Κ κ, Λ λ, Μ μ, Ν ν, Ξ ξ, Ο ο, Π π, Ρ ρ, Σ σ[ς], Τ τ, Υ υ, Φ φ, Χ χ, Ψ ψ, Ω ω

# Input
        
# Unidades: 1mm³=1μl => 1000 mm³=1ml

# Volumen de la muestra:
vol_muestra=50*u.mm**3 # volumen en ml de la muestra agarosa+cultivo_celulas
vol_muestra.to(u.mm**3)
#vol_muestra=vol_muestra.value

# Densidad de celulas:
#rho_celulas=1467*u.mm**(-3) # celulas/mm³ optimo para diametro_droplet=50 μm 4.998423131410721 %
#rho_celulas=445*u.mm**(-3) # celulas/mm³ optimo para diametro_droplet=75 μm 5.0073506481935235 %
#rho_celulas=190*u.mm**(-3) # celulas/mm³ optimo para diametro_droplet=100 μm 5.030155416376711 %
#rho_celulas=95*u.mm**(-3) # celulas/mm³ optimo para diametro_droplet=125 μm 4.993864746602459 %
#rho_celulas=64*u.mm**(-3) # celulas/mm³ optimo para diametro_droplet=143 μm 5.052206902084837 %
#rho_celulas=55*u.mm**(-3) # celulas/mm³ optimo para diametro_droplet=150 μm 5.041053529537214 %
#rho_celulas=23*u.mm**(-3) # celulas/mm³ optimo para diametro_droplet=200 μm 4.94176846635863 %


rho_celulas=23.2*u.mm**(-3) # celulas/mm³ optimo para diametro_droplet=75 μm

rho_celulas.to(u.mm**-3)
#rho_celulas=rho_celulas.value

# Radio de las droplets:
#radio_droplet=25*u.micron

# Diámetro de las droplets:
diametro_droplet=200*u.micron

# Genera un volumen equivalente a una droplet con el tamaño que esperamos obtener.
vol_droplet=vol_esfera_diametro(diametro_droplet)
vol_droplet.to(u.mm**3)
#vol_droplet=vol_droplet.value

# Redondea al número de células entero mas próximo.
n_celulas=int(round((vol_muestra.value)*(rho_celulas.value)))

n_simulaciones=60


#flujo_continua=5*(u.micron**3*u.min**-1)
#flujo_continua.to(u.micron**3*u.min**-1)
#flujo_continua=flujo_continua.value

flujo_dispersa=2*(u.mm**3*u.min**-1)
#flujo_dispersa.to(u.micron**3*u.min**-1)
#flujo_dispersa=flujo_dispersa.value



# Output
duracion_experimento=vol_muestra.to(u.mm**3)/(flujo_dispersa.to(u.mm**3*u.min**-1)) # min
tasa_formacion=flujo_dispersa.to(u.mm**3*u.s**-1)/vol_droplet.to(u.mm**3) 

print('ρ = ',rho_celulas,'\nVol_muestra: ',vol_muestra,'\nDiametro droplet: ',diametro_droplet,'\nFlujo fase dispersa: ',flujo_dispersa.to(u.mm**3*u.min**-1),'\nNúmero de simulaciones: ',n_simulaciones,'\n\nVolumen droplet: ',vol_droplet.to(u.mm**3),'\nDuración experimento: ',duracion_experimento,'\nTasa de formación: ',tasa_formacion,'\n')

vol_muestra=(vol_muestra.to(u.mm**3)).value
vol_droplet=(vol_droplet.to(u.mm**3)).value
rho_celulas=(rho_celulas.to(u.mm**-3)).value


# Para las pruebas:
#vol_muestra=1E3
#n_celulas=10000
#vol_droplet=1


#%% Genera un conjunto de números aleatorios entre 0 y un valor "volumen" muestra. Esto simula la distribución de las celulas contenidas en la muestra en un volumen.

a=datetime.datetime.now()

array_elementos=[]
array_repeticiones=[]

# Comienzan las "simulaciones".
for n in range(0,n_simulaciones,1):
    
    distribucion_muestra=[] # len(distribucion_muestra)=n_celulas.

    # Generamos una distribución de puntos estadísticamente uniforme.
    for i in range(0,n_celulas,1):
        distribucion_muestra.append(np.random.uniform(0,vol_muestra))

    # Formacion de las droplets
    droplets=[] # droplets es un array de droplet con "celulas en su interior" a partir de distribución muestra.
    droplets=encapsuladosss(vol_muestra, vol_droplet, distribucion_muestra)
      
    # Recuento del número de "celulas" en cada droplet.
    n_encapsulamientos=[]
    for i in range(0,len(droplets),1):
        n_encapsulamientos.append(len(droplets[i]))
    
    
# Número de encapsulados que se han producido. Se realiza un conteo de qué elementos se encuentran en el array (elementos) y que número de veces se han repetido (repetidos).
    [elementos,repeticiones]=np.unique(n_encapsulamientos,return_counts = True)
    
    array_elementos.append(elementos)
    array_repeticiones.append(repeticiones)
    
    t=datetime.datetime.now()
    print(t-a, elementos, repeticiones)

# Queremos estudiar estadísticamente los resultados de las simulaciones.
# https://stackoverflow.com/questions/43146266/convert-list-of-lists-with-different-lengths-to-a-numpy-array
a=array_repeticiones
    
b = np.zeros([len(a),len(max(a,key = lambda x: len(x)))])
for i,j in enumerate(a):
    b[i][0:len(j)] = j

# Obtiene una matrix de enteros.
c=b.astype(int)

medias=[] 
std_medias=[]
for k in range(1,len(max(a,key = lambda x: len(x)))+1,1):
    medias.append(np.mean(c[:,k-1:k])) # Medias de la columna k de la matriz c.
    std_medias.append(np.std(c[:,k-1:k])) # Desviación estándar de la columna k de la matriz c.

# Transforma la lista en array.  
medias=np.array(medias)
std_medias=np.array(std_medias)

# Redondea los valores contenidos en el array al entero más próximo.  
print('\n\nCélulas/droplet  Nª droplets  Desviación estándar \n')
# Imprime los valores enteros de los arrays medias y std_medias.
for s in range(0,len(max(a,key = lambda x: len(x))),1):
    print(s,'',medias.astype(int)[s],'±',std_medias.astype(int)[s],'(±',round_sig((std_medias[s]/medias[s])*100),'% )')

# Ratio entre número de repeticiones que se ha producido un tipo de encapsulado (entiendo por tipo de encapsulado la distición que hago en función del número de encapsulados que se han producido en cada droplet) y el siguiente.   MEJORAR REDACCION
cociente=[]
for p in range(0,len(repeticiones)-1,1):
    cociente.append(medias[p]/medias[p+1])

print(cociente)


porcentaje=[]
encapsulados_multiples=0

for p in range(0,len(medias)-1,1):
    porcentaje.append(medias[p]/len(droplets)*100)
    if p==(len(medias)-1):
        print('algo')
        encapsulados_multiples=encapsulados_multiples+medias[p]+medias[p+1]
    elif p>1:
        encapsulados_multiples=encapsulados_multiples+medias[p]
    
f=datetime.datetime.now()

# Queremos que el 95% de los encapsulados (se entiende por encapsulado, todas las droplets que tienen al menos 1 célula en su interior) tengan 1 célula, es decir, encapsulados multiples ~5% del total de encapsulados.
print('Queremos que se encuentre ~5%... y el valor resultante es',(encapsulados_multiples/medias[1])*100,'%')
len(droplets)-medias[0]
print(porcentaje)




#%% Histograma para ver la distribución que muestra cuantas gotas contienen tantas "celulas"
    
from astropy.visualization import hist as hist_astropy
import matplotlib.pyplot as plt

figura=plt.figure(num = None, figsize = (9, 6), dpi = 80, facecolor = 'w', edgecolor = 'k')

# "knuth" "scott" "freedman" "blocks"
#hist_astropy(z_spec12_amg, bins=100, range=(0,0.6), normed=False, alpha=0.6, color='#2e7d32', histtype='stepfilled', label='$z_{g}$ Q=2')

hist_astropy(n_encapsulamientos, bins=len(elementos), density=False, alpha=0.6,color='#9e9d24', histtype='stepfilled', label='$z_{g}$ Q=3')
             
plt.xlabel('$\mathrm{N_{celulas}}$', fontsize = 16)
plt.ylabel('$\mathrm{N_{droplets}}$', fontsize = 16)
plt.legend(loc='best')
figura.savefig(outroute + 'histograma.png', dpi=150, transparent=True)
