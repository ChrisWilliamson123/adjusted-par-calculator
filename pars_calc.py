import sys

# (hole, par, SI, new par)
course_filename = sys.argv[1]
f = open(f'courses/{course_filename}', 'r')
hole_number = 1
holes = []
for line in f:
    [par, si] = map(lambda x: int(x), line.rstrip().split(','))
    holes.append([hole_number, par, si, par])
    hole_number += 1

target_strokes = int(sys.argv[2])

par_for_course = sum(x[1] for x in holes)
print(f'Scratch par for course: {par_for_course}')
print(f'Adjusted par for course: {target_strokes}')

sorted_by_si = sorted(holes, key=lambda x: x[2])

strokes_given = 0
while (target_strokes - strokes_given > par_for_course):
    sorted_by_si[strokes_given % len(sorted_by_si)][3] += 1
    strokes_given += 1

sorted_by_hole = sorted(sorted_by_si, key=lambda x: x[0])
print('\n')
print('|----------|')
print('|Hole\tPar|')
print('|----------|')
for hole in sorted_by_hole:
    print(f'|{hole[0]}\t{hole[3]}  |')
print('|----------|')
