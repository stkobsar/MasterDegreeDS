import matplotlib.pyplot as plt

def get_value(txids, bloques, suma_vouts):
    suma_por_bloque = []
    for bloque in bloques:
        suma_valores_bloque = 0
        for transaction in bloque:
            valor_transaction = suma_vouts[transaction] #sacar el value de cada key "transaction"
            suma_valores_bloque += valor_transaction
        suma_por_bloque.append(suma_valores_bloque)
    fig, ax = plt.subplots()  # crear una nueva figura de matplotlib para evitar que se sobreecriban los gráficos.
    ax.hist(suma_por_bloque)
    plt.savefig("histogram_valores_por_bloque.png")