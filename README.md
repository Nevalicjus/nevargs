# nevargs

Nevargs is a simple package that formats cli-like argument strings into a dictionary

Arguments with no value are returned under `args` and for each flag found, it's arguments are under `{flag}`

## Installation

```bash
python3 -m pip install nevargs
```

## Example

```py
>>> import nevargs
>>> s = "this is -f True fun -c command"
>>> nevargs.dictify(s)
{'args': ['this', 'is', 'fun'], '-f': ['True'], '-c': ['command']}
```
