train_length = int(input())

train = list(0 for i in range(train_length))

command = input()
while command != 'End':
    command = command.split(' ')
    if command[0] == 'add':
        train[-1] += int(command[1])
    elif command[0] == 'insert':
        index = int(command[1])
        train[index] += int(command[2])
    elif command[0] == 'leave':
        index = int(command[1])
        train[index] -= int(command[2])
    command = input()

print(train)
