import numpy as np
import matplotlib.pyplot as plt


def get_mean_size(sizes, times):
    sizes_per_hour = []
    for time, size in zip(times, sizes):
        time_in_hour = time/3600
        size_per_hour = size/time_in_hour
        sizes_per_hour.append(size_per_hour)
    meanblock_per_hour = np.mean(sizes_per_hour)

    print(meanblock_per_hour)

    fig, ax = plt.subplots() #crear una nueva figura de matplotlib para evitar que se sobreecriban los gráficos.
    ax.boxplot(sizes_per_hour)
    plt.savefig("barplot_sizes_hour.png")