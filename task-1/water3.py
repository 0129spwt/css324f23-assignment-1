def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return (s[0]==4, s[1]==4)

def successors(s):
    x, y, z = s
    if x > 0:
        if y < 5:
            actions.append((0, 1))
        if z < 3:
            actions.append((0, 2))
    if y > 0:
        if x < 8:
            actions.append((1, 0))
        if y < 3:
            actions.append((1, 2))
    if y > 0:
        if x < 8:
            actions.append((2, 0))
        if y < 5:
            actions.append((2, 1))

    return []
