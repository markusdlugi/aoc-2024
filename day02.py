lines = list(open("input/02.txt"))


def is_safe(levels):
    increasing = levels[1] > levels[0]
    for i, level in enumerate(levels[1:]):
        prev_level = levels[i]
        if level > prev_level and not increasing:
            break
        elif level < prev_level and increasing:
            break
        diff = abs(level - prev_level)
        if diff < 1 or diff > 3:
            break
    else:
        return True
    return False


result = 0
for line in lines:
    levels = list(map(int, line.split(' ')))
    if is_safe(levels):
        result += 1

print(result)

result = 0
for line in lines:
    levels = list(map(int, line.split(' ')))
    for removed in range(0, len(levels)):
        dampened_levels = levels.copy()
        del dampened_levels[removed]
        if is_safe(dampened_levels):
            result += 1
            break

print(result)
