import shlex

def dictify(s: str):
    if len(s) == 0:
        return "String can't be empty"

    s = shlex.split(s, posix = True)
    itc_ini = []
    itc = []
    flags_ini = [x for x in s if x.startswith('-')]
    flags = []
    for flag in flags_ini:
        if flag not in flags:
            flags.append(flag)
    dict = {}
    dict["binflags"] = []
    for flag in flags:
        flag_indexes =  [f"{i}" for i, x in enumerate(s) if x == flag]
        itc_ini.extend(flag_indexes)
        try:
            if (int(flag_indexes[0]) + 1) <= (len(s) - 1):
                if s[int(flag_indexes[0]) + 1] in ["True", "False"]:
                    dict["binflags"].append(flag)
                dict[f"{flag}"] = []
                for flag_index in flag_indexes:
                    dict[f"{flag}"].append(s[int(flag_index) + 1])
                continue
        except IndexError:
            continue
        try:
            if len(flag_indexes) == 1 and not s[int(flag_indexes[0]) + 1].startswith('-'):
                dict["binflags"].append(flag)
        except IndexError:
            dict["binflags"].append(flag)

    itc = [x for x in itc_ini if x not in itc]
    for i in itc:
        s[int(i)] = ''
        s[int(i) + 1] = ''
    for flag in flags:
        if flag in s:
            s[s.index(flag)] = ''
    dict["noflag"] = [x for x in s if x]

    return dict
