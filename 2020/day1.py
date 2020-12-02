with open("day1input.txt", "r") as f:
    expenses = [int(x.strip()) for x in f.readlines()]


for i in range(len(expenses)):
    for j in range(i, len(expenses)):
        if expenses[i] + expenses[j] == 2020:
            print(expenses[i]*expenses[j])
        for k in range(j, len(expenses)):
            if expenses[i] + expenses[j] + expenses[k] == 2020:
                print(expenses[i]*expenses[j]*expenses[k])