import pec4_ds_skobsar.get_data.get_dataset as gd
import pec4_ds_skobsar.analysis.get_transaction_block as gt
import pec4_ds_skobsar.analysis.get_value_transaction as gv
import pec4_ds_skobsar.analysis.time_blocks as tb
import pec4_ds_skobsar.analysis.mean_size_hour as ms
import pec4_ds_skobsar.analysis.transactions_hour as th

def main():
    print("Get values from dataset")
    times, txs, sizes, txids, suma_vouts = gd.open_dataset()
    gt.get_transaction(txs)
    gv.get_value(txids, txs, suma_vouts)
    tb.get_time_block(times)
    ms.get_mean_size(sizes, times)
    th.get_transaction_hour(times, txs)


#Print para que el usuario sepa que hace
#README donde se diga como correrlo
#setup.py (image formatter)
#   git clone ....
#   cd pec4....
#   python setup.py install



if __name__ == "__main__":
    main()