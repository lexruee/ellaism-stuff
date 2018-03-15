# Ellaism Diff Plotter

## Dependencies

 * a local ellaism node
 * python3 
 * [matplotlib](https://github.com/matplotlib/matplotlib)
 * [web3.py](https://github.com/ethereum/web3.py)

You can install the Python deps via `pip`:

```
pip install matplotlib web3
```


## Usage
```
./diff_plotter.py -h
usage: diff_plotter.py [-h] [-V] [-a JSONRPC] [-s START_BLOCK] [-e END_BLOCK]
                       [-r SAMPLING_RATE] [-o OUTPUT] [-S]

ellap - Simple tool to plot ella difficulty

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         Print version number.
  -a JSONRPC, --jsonrpc JSONRPC
                        Set JSONRPC URL address.
  -s START_BLOCK, --start-block START_BLOCK
                        Set start block.
  -e END_BLOCK, --end-block END_BLOCK
                        Set end block.
  -r SAMPLING_RATE, --sampling-rate SAMPLING_RATE
                        Set sampling rate.
  -o OUTPUT, --output OUTPUT
                        Output file.
  -S, --show            Show plot.

```

## Example Usage

```
./diff_plot.py -a http://localhost:8545 --show
```

```
./diff_plotter.py -a http://localhost:8545 -o ella-diff-1.png --start-block 1 --end-block 500000 --sampling-rate 0.1 --show
```
