from collections import defaultdict

lines = list(open("input/01.txt"))

left = []
right = []
left_count = defaultdict(int)
right_count = defaultdict(int)
for line in lines:
    a, b = map(int, line.split())
    left.append(a)
    right.append(b)
    left_count[a] += 1
    right_count[b] += 1

left.sort()
right.sort()

distance = 0
for i in range(len(lines)):
    distance += abs(left[i] - right[i])
print(distance)

similarity_score = 0
for key, val in left_count.items():
    similarity_score += val * key * right_count[key]

print(similarity_score)
