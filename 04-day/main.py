from itertools import groupby

nmin = 256310
nmax = 732736

def has_adj(n):
    n_str = str(n)
    grps = [len(list(g)) > 1 for k, g in groupby(n_str)]
    return any(grps)

def even_groups(n):
    n_str = str(n)
    grps = [len(list(g)) == 2 for k, g in groupby(n_str)]
    return any(grps)

def is_asc(n):
    n_str = str(n)
    old_digit = "-1"
    for digit in n_str:
        if int(digit) < int(old_digit):
            return False
        old_digit = digit
    return True

print("=== A ===")
print(sum([has_adj(n) and is_asc(n) for n in range(nmin, nmax + 1)]))

print("=== B ===")
print(sum([has_adj(n) and even_groups(n) and is_asc(n) for n in range(nmin, nmax + 1)]))
