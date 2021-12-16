import shlex

def dictify(s: str):
    if len(s) == 0:
        return "String can't be empty"

    s = shlex.split(s, posix = True)
    itc = []
    flags = [x[1:] for x in s if x.startswith('-')]
    dict = {}
    dict["binflags"] = []
    for flag in flags:
        flag_indexes =  [f"{i}" for i, x in enumerate(s) if x == flag]
        itc.extend(flag_indexes)
        if (int(flag_indexes[0]) + 1) <= (len(s) - 1):
            if s[int(flag_indexes[0]) + 1] in ["True", "False"]:
                dict["binflags"].append(flag)
            dict[f"{flag}"] = []
            for flag_index in flag_indexes:
                dict[f"{flag}"].append(s[int(flag_indexes[0]) + 1])
            continue
        try:
            if len(flag_indexes) == 1 and not s[int(flag_indexes[0]) + 1].startswith('-'):
                dict["binflags"].append(flag)
        except IndexError:
            dict["binflags"].append(flag)

    itc = [itc.append(x) for x in itc if x not in itc]
    for i in itc:
        s[int(i)] = ''
    for flag in flags:
        if flag in s:
            s[s.index(flag)] = ''
    dict["noflag"] = [x for x in s if x]

    return dict
