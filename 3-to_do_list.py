to_do_list = ['' for x in range(11)]
command = input()

while command != 'End':
    command = command.split('-')
    index = int(command[0])
    task = command[1]
    to_do_list[index] = task
    command = input()

final_todo = [task for task in to_do_list if task != '']

print(final_todo)
