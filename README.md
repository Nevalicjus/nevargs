# nevargs

It's a simple package that using shlex formats your cli-like argument strings and format them into a dict

```py
>>> import nevargs
>>> s = "this is -f True fun -c command"
>>> nevargs.dictify(s)
{'args': ['this', 'is', 'fun'], '-f': ['True'], '-c': ['command']}
```
Arguments with no value are returned under `args` and for each flag found, it's arguments are under `{flag}`
