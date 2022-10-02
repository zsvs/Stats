[![Pylint](https://github.com/zsvs/Stats/actions/workflows/pylint.yml/badge.svg)](https://github.com/zsvs/Stats/actions/workflows/pylint.yml)

# Stats processing for telegram

This program takes 2 `CSV` files and creates them in the right way(with headers). Main purpose is to compare `CSV` files and find user who have more messages in specific range of time

## Example Usage:
```powershell
    C:\<Path>\<To>\stats.py `
    -s "C:\\<Path>\\<To>\\<Older_Source_CSV_Files>.csv" `
    -r "C:\\<Path>\\<To>\\<Older_Result_CSV_Files>.csv" `
    -sn "C:\\<Path>\\<To>\\<Newer_Source_CSV_Files>.csv" `
    -rn "C:\\<Path>\\<To>\\<Older_Result_CSV_Files>.csv" `
    -f "C:\\<Path>\\<To>\\<Result_Files>.csv" `
    -v True
```

## Inputs

* `--source-file` - Path to CSV file with start time values. For example, this must be the file from the begining of the week
    - Short version: `-s`
    - Required: True
    - Type: str

* `--result-file` - Path to result CSV file with correct headers formed from `--source-file`. This files needs for comparasion between start and end of the period.
    - Short version: `-r`
    - Required: True
    - Type: str

* `--new-source-file` - Path to new CSV file with start time values. For example, this must be the file from the begining of the week
    - Short version: `-sn`
    - Required: True
    - Type: str

* `--new-result-file` -Path to new result CSV file with correct headers formed from `--new-source-file`. This files needs for comparasion between start and end of the period.
    - Short version: `-rn`
    - Required: True
    - Type: str

* `--file` - Save result to csv file. You must provide path to file
    - Short version: `-f`
    - Required: True
    - Type: str

* `--verbose` - Enable verbose. Print all difference between old and new entries
    - Short version: `-v`
    - Required: False
    - Type: bool
