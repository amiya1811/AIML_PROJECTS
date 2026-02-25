facts = {"A", "B"}

rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"D"}, "E")
]

goal = "E"

derived = set(facts)

changed = True
while changed:
    changed = False
    for cond, res in rules:
        if cond.issubset(derived) and res not in derived:
            derived.add(res)
            changed = True

if goal in derived:
    print("Goal Reached")
else:
    print("Goal Not Reached")


def backward(g):
    if g in facts:
        return True
    for cond, res in rules:
        if res == g:
            return all(backward(c) for c in cond)
    return False

if backward(goal):
    print("Goal Reached")
else:
    print("Goal Not Reached")


def resolve(c1, c2):
    result = []
    for lit in c1:
        if ("~" + lit) in c2:
            result.append((c1 - {lit}) | (c2 - {"~" + lit}))
        elif lit.startswith("~") and lit[1:] in c2:
            result.append((c1 - {lit}) | (c2 - {lit[1:]}))
    return result


KB = [
    {"A", "B"},
    {"~A"},
    {"~B"}
]

found = False

while True:
    new = []
    for i in range(len(KB)):
        for j in range(i + 1, len(KB)):
            resolvents = resolve(KB[i], KB[j])

            for r in resolvents:
                if len(r) == 0:
                    found = True
                    break
                new.append(r)

        if found:
            break

    if found:
        print("Contradiction Found")
        break

    if all(r in KB for r in new):
        print("No Contradiction")
        break

    KB.extend([r for r in new if r not in KB])