with open('данные.txt', 'r') as file:
    data = file.readlines()

    students = {}

    for line in data:
        info = line.strip().split()

        if len(info) >= 3:
            name = info[0] + ' ' + info[1]
            grade = info[2]
            students[name] = grade

user_input = input("Введите имя и фамилию ученика: ")

if user_input in students:
    print(f"Оценка ученика {user_input}: {students[user_input]}")
else:
    print("Данные об этом ученике отсутствуют")