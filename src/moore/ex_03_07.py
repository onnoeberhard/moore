from math import inf

def edit(s, t): # (action values)
    x = d(s[1:], t) + 1 if len(s) > 0 else inf
    y = d(s, t[1:]) + 1 if len(t) > 0 else inf
    z = d(s[1:], t[1:]) + (0 if s[0] == t[0] else 1) \
        if len(s) > 0 and len(t) > 0 else inf
    return x, y, z

def d(s, t, known={('', ''): 0}): # (state values)
    if (s, t) in known: return known[(s, t)]
    dist = min(*edit(s, t))
    known[(s, t)] = dist
    return dist

def align(s, t):
    x, y, z = edit(s, t)

    best, cost = -1, inf
    for i, dist in enumerate([x, y, z]):
        if dist < cost: best, cost = i, dist

    match best:
        case 0: return [(s[0], ' ')] + align(s[1:], t)
        case 1: return [(' ', t[0])] + align(s, t[1:])
        case 2: return [(s[0], t[0])] + align(s[1:], t[1:])
        case _: return []

if __name__ == "__main__":
    s, t = "pastrycook", "astronomer"
    dist = d(s, t)
    sol = align(s, t)
    print(f"Levenshtein distance: {dist}")
    print("".join(x[0] for x in sol))
    print("".join(x[1] for x in sol))
