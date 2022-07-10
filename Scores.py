scores_of_students = [int(x) for x in input('Enter the scores of students by space after each input ').split()]
runners_up_students = []
count = 0
new_count = 0
print(f'Number of students is {len(scores_of_students)}')
for i in scores_of_students:
    if i == max(scores_of_students):
        count += 1
    else:
        runners_up_students.append(i)    
scores_of_students.sort()
for i in runners_up_students:
    if i == max(runners_up_students):
        new_count += 1
runners_up_students.sort()
if count > 1:
    print(f'Number of Students with Highest Score is {count}')
    print(f'The Winners Score is {scores_of_students[-1]}')
else:
    print(f'The Winner Score is {scores_of_students[-1]}')
if new_count > 1:
    print(f'Number of Students with Runner-up Score is {new_count}')
    print(f'The Runner-ups Score is {runners_up_students[-1]}')
else:
    print(f'The Runner-up Score is {runners_up_students[-1]}')
print(f'The Third Score is {runners_up_students[len(runners_up_students) - new_count - 1]}')