lines = list(open("input/02.txt"))

result = 0
for line in lines:
    levels = list(map(int, line.split(' ')))
    prev_level = 0
    inc = True
    safe = True
    for i, level in enumerate(levels):
        if i == 0:
            if levels[1] > level:
                inc = True
            else:
                inc = False
            prev_level = level
            continue
        if level > prev_level and not inc:
            safe = False
            break
        elif level < prev_level and inc:
            safe = False
            break
        if 1 <= abs(level - prev_level) <= 3:
            prev_level = level
            continue
        else:
            safe = False
            break
    if safe:
        result += 1

print(result)

result = 0
for line in lines:
    levels = list(map(int, line.split(' ')))
    for removed in range(0, len(levels)):
        levels = list(map(int, line.split(' ')))
        del levels[removed]
        prev_level = 0
        inc = True
        safe = True
        for i, level in enumerate(levels):
            if i == 0:
                if levels[1] > level:
                    inc = True
                else:
                    inc = False
                prev_level = level
                continue
            if level > prev_level and not inc:
                safe = False
                break
            elif level < prev_level and inc:
                safe = False
                break
            if 1 <= abs(level - prev_level) <= 3:
                prev_level = level
                continue
            else:
                safe = False
                break
        if safe:
            result += 1
            break

print(result)
