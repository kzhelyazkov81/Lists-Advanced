employees = input().split(' ')
happiness_factor = int(input())

employees = list(map(lambda x: int(x) * happiness_factor, employees))
filtered = list(filter(lambda x: x >= sum(employees) / len(employees), employees))

happy_count = len(filtered)
total_count = len(employees)

if happy_count >= total_count / 2:
    print(f'Score: {happy_count}/{total_count}. Employees are happy!')
else:
    print(f'Score: {happy_count}/{total_count}. Employees are not happy!')