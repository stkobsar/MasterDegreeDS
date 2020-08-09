import matplotlib.pyplot as plt

def get_transaction_hour(times, txs):
    transactions_per_hour = []
    for tx, time in zip(txs, times):
        n_transactions = len(tx)
        time_in_hour = time/3600
        number_transaction_hour = n_transactions/time_in_hour
        transactions_per_hour.append(number_transaction_hour)
    fig, ax = plt.subplots()  # crear una nueva figura de matplotlib para evitar que se sobreecriban los gráficos.
    ax.hist(transactions_per_hour)
    plt.savefig("histogram_transactions_hour.png")
