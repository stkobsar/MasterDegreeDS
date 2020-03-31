import pandas as pd
import ssl
import numpy as np

ssl._create_default_https_context = ssl._create_unverified_context

json_data = "https://data.nasa.gov/resource/y77d-th95.json"
df_nasa = pd.read_json(json_data)
#print(pd.DataFrame.head(df_nasa))
"""
Cread un diccionario ordenado con los datos del dataset. El diccionario debe de estar indexado y ordenado por el campo id.
La estructura debe de ser {id0: dict_con_datos_de_id0, id1: dict_con_datos_de_id1, ...}
Pista: podéis usar el método .to_dict() de una columna del dataset para convertirla en un diccionario.
"""
dict_nasa = df_nasa.to_dict(orient="index")
#print(dict_nasa)

"""
Definid una función que reciba como parámetro el diccionario del ejercicio anterior y:

Muestre por pantalla las masas de todos los asteroides de clase (recclass) H6 con identificador mayor a 5000.
Devuelva la media de los valores mostrados por pantalla.
La función debe de estar preparada para trabajar con diccionarios muy grandes. Por lo tanto, se debe evitar guardar los valores individuales mostrados por pantalla en una lista.

Llamad a la función definida con el diccionario del ejercicio anterior como parámetro.
"""

def asteroid_mass(dictionary):
    df_nasa = pd.DataFrame(dictionary)
    df_nasa = df_nasa.T
    condition = (df_nasa["recclass"] == "H6") & (df_nasa["id"] > 5000)
    asteroids_H6 = df_nasa[condition]
    print(asteroids_H6["mass"])
    print(asteroids_H6["mass"].mean())

asteroid_mass(dict_nasa)

# the same goal above but using only one line

mass_mean =  np.mean([ mean["mass"] for mean in dict_nasa.values() if mean["id"] > 5000 and not np.isnan(mean["mass"])])

print(mass_mean)





