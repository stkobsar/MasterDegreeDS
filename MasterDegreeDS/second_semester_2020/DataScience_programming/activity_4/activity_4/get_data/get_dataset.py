import json
import os

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_blocks = os.path.join(root_dir, "dataset/blocks.json")
file_txs = os.path.join(root_dir, "dataset/txs.json")

def open_dataset(file_blocks=file_blocks, file_txs=file_txs):
    times = []
    txs = []
    sizes = []
    for line in open(file_blocks, 'r'):
        data_linea = json.loads(line)
        time = data_linea["time"]
        times.append(time)
        tx = data_linea["tx"]
        txs.append(tx)
        size = data_linea["size"]
        sizes.append(size)
    txids = []
    suma_vouts = {}
    for line in open(file_txs, 'r'):
        data_linea = json.loads(line)
        txid = data_linea["txid"]
        txids.append(txid)
        vout = data_linea["vout"]

        counter = 0
        for dic in vout:
            num = dic["value"]
            counter += num #sobreescribir el counter por counter + num
        suma_vouts[txid] = counter

    return times, txs, sizes, txids, suma_vouts
