import os
import pec4_ds_skobsar.get_data.get_dataset as gd
import pec4_ds_skobsar.analysis.get_transaction_block as gt
import pec4_ds_skobsar.analysis.get_value_transaction as vt
import pec4_ds_skobsar.analysis.mean_size_hour as mz
import pec4_ds_skobsar.analysis.time_blocks as tb
import pec4_ds_skobsar.analysis.transactions_hour as th

absolute_path_every_machine = os.path.abspath(__file__)
test_dir = os.path.dirname(absolute_path_every_machine)
file_blocks = os.path.join(test_dir, "blocks_test.json")
file_txs = os.path.join(test_dir, "txs_test.json")

txs = [["deda", "deda"],  ["dedae", "dedd", "dedae"]]
txs_2 = [["059c99edf8ed1b3301cf0c24e2a291017071d635eb9fa20819cfa880345bf929", "059c99edf8ed1b3301cf0c24e2a291017071d635eb9fa20819cfa880345bf928"]]
suma_vouts = {"059c99edf8ed1b3301cf0c24e2a291017071d635eb9fa20819cfa880345bf929": 4, "059c99edf8ed1b3301cf0c24e2a291017071d635eb9fa20819cfa880345bf928": 6}
times = [3600, 7200]
sizes = [10, 20]


print(file_txs)
print(file_blocks)
def test_get_data(block_test=file_blocks, txs_test=file_txs):
    times, txs, sizes, txids, suma_vouts = gd.open_dataset(block_test, txs_test)
    assert txids[0] == "059c99edf8ed1b3301cf0c24e2a291017071d635eb9fa20819cfa880345bf929"
    assert suma_vouts["059c99edf8ed1b3301cf0c24e2a291017071d635eb9fa20819cfa880345bf929"] == 7.46675786
    assert times[0] == 1591021468
    assert "059c99edf8ed1b3301cf0c24e2a291017071d635eb9fa20819cfa880345bf929" in txs[0]
    assert "cbffdaba9ceaa9e34bc415f68f77d072dedbe7eecee52caf13d8f3e0293b5934" in txs[0]
    assert "9a8c010365cf7dfbd8807a85a8c0009d1866897f14480d9d01f4ae2ccac83464" in txs[0]
    assert sizes[0] == 1340282

def test_get_transaction_block(txs=txs):
    transactions = gt.get_transaction(txs)
    assert transactions == [2, 3]

def test_get_value_transaction(txs=txs, suma_vouts=suma_vouts):
    value_transaction_test = vt.get_value(txs_2, suma_vouts)
    assert value_transaction_test == [10]

def test_mean_size_hour(sizes=sizes, times=times):
    size_hour_test = mz.get_mean_size(sizes, times)
    assert size_hour_test == 10

def test_time_block(times=times):
    test_times = tb.get_time_block(times)
    assert test_times == [3600]

def test_transaction_hour(times=times, txs=txs):
    test_trans_time = th.get_transaction_hour(times, txs)
    assert test_trans_time == [2, 1.5]






