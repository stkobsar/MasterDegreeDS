import matplotlib.pyplot as plt

def get_time_block(times):
    tiempo_entre_bloques = []
    for i, time in enumerate(times):
        try:
            resta = abs(times[i+1] - time)
        except IndexError:
            continue
        tiempo_entre_bloques.append(resta)
    fig, ax = plt.subplots()  # crear una nueva figura de matplotlib para evitar que se sobreecriban los gráficos.
    ax.hist(tiempo_entre_bloques)
    plt.savefig("histogram_timeblocks.png")