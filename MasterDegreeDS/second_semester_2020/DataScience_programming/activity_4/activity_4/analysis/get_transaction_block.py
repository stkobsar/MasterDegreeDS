import matplotlib.pyplot as plt

def get_transaction(txs):
    transactions = []
    for tx in txs:
        transaction = len(tx)
        transactions.append(transaction)
    fig, ax = plt.subplots() #crear una nueva figura de matplotlib para evitar que se sobreecriban los gráficos.
    ax.hist(transactions)
    plt.savefig("histogram_transactions.png")