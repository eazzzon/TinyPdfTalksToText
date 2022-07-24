# Night talks of Pdf to Text
Have you ever got nightmare from converting tables in old literature pdf files to excel files? Yes? Here is a tiny script you can simply convert these nightmare tables to excels with few efforts.

## Requirements 

1. Python > 3.7 (tested with python 3.10 but should work with the latest `tabula` and `tabulate` pkgs)
2. `tabula` packages, can be installed in conda env via:

```
conda install -c conda-forge tabula-py
```

3. `tabulate` package, install via:

```
conda install -c conda-forge tabulate
```

4. `pandas` and `numpy`

## How to run?

Run from the example notebook or run the modified script in your directory, with command line or IDE execution:

```
python pdfToTable.py
```

A built-in function is provided to convert string to float data, also extract standard errors in the tabula (if given)

A breif example notebook is given in the example folder. with output files for benchmark, example test pdf can be download from [here](https://www.sciencedirect.com/science/article/pii/S0024493717303948?casa_token=mvW4EmhgSxIAAAAA:NHo12hBnV-pl1ZMfynRm4xNlIxdhe_HQangT1AcQZRco7twgzD9Z3ozIUqkkxky9aiNd7ZdPUz_p) or Zhang et al. 2018 Lithos: 300–301 (2018) 20–32. 

Send me [email](yishen.zhang@kuleuven.be) if you ran into any problem.