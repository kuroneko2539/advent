with open("day6input.txt", "r") as f:
	lines = [x.strip() for x in f.readlines()]

answers = []
answer = ""
answer_count = 0
for line in lines:
	if line == "":
		answers.append([answer, answer_count])
		answer = ""
		answer_count = 0
	else:
		answer += line
		answer_count += 1
answers.append([answer, answer_count])

total_yes = 0

for answer in answers:
	total_yes += len(set(answer[0]))
	
print(total_yes)

total_all_yes = 0

for answer in answers:
	for c in set(answer[0]):
		if answer.count(c) == answer[1]:
			total_all_yes += 1
			
print(total_all_yes)