# Ellaism Diff Plotter

## Dependencies

 * a local [ellaism node](https://ellaism.org/install/)
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

![](https://raw.githubusercontent.com/lexruee/ellaism-stuff/master/plotting/ella-diff1.png)


```
./diff_plotter.py -a http://localhost:8545 -o ella-diff2.png \ 
    --start-block 1 --end-block 500000 --sampling-rate 0.1 --show
```

![](https://raw.githubusercontent.com/lexruee/ellaism-stuff/master/plotting/ella-diff2.png)


```
./diff_plotter.py -a http://localhost:8545 -o ella-diff3.png --end-block -1 --show
```

![](https://raw.githubusercontent.com/lexruee/ellaism-stuff/master/plotting/ella-diff3.png)
