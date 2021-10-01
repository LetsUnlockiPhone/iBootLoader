# iBootLoader

IDA Loader

## Disassembler Support:

| Disassembler | Supported |
|--------------|-----------|
| IDA 7.0-7.6  | ✓         |

# Filetype Support 

| File type                | Supported |
|--------------------------|-----------|
| arm32/64 SecureROM       | ✓         |
| arm32/64 iBoot/iBEC/iBSS | ✓         |
| Encrypted arm32/64 iBoot/iBEC/iBSS | ✓         |
| SEPROM                   | ✗        |


## Installation

### On Windows:

```
python3 -m pip install --upgrade ilstrap
python3 -m ilstrap.installer --gh KritantaDev/iBootLoader
```

### On MacOS/Linux

```
pip3 install --upgrade ilstrap
ilstrap --gh KritantaDev/iBootLoader
```
---



---

###### Credits:

this project was originally inspired by https://github.com/argp/iBoot64helper

