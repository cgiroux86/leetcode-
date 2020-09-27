def groupPeople(people):
    groups = {}
    results = []
    for i in range(len(people)):
        print(people[i], groups)
        if people[i] in groups:
            groups[people[i]].append(i)
        else:
            groups[people[i]] = [i]
        if(len(groups[people[i]]) == people[i]):
            results.append(groups[people[i]])
            groups.pop(people[i])

    return results


print(groupPeople([2, 2, 1, 1, 1, 1, 1, 1]))
