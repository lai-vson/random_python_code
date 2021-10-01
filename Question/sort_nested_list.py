# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.


if __name__ == '__main__':
    records = []
    scores = set()
    second_name = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.add(score)

    second = sorted(scores)[1]

    for name, score in records:
        if score == second:
            second_name.append(name)

    second_name.sort()

    for name in second_name:
        print(name, end='\n')