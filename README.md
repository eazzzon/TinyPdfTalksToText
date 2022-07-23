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

## How to run?

run the modified script in your directory, command line or IDE execution:

```
python pdfToTable.py
```

A built-in function is provided to convert string to float data

Send me [email](yishen.zhang@kuleuven.be) if you ran into any problem.