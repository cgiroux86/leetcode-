def getPermutations(array):
    if len(array) == 1:
        return [array]
    permutations = []
    for i in range(len(array)):
        # get all perm's of subarray w/o current item
        perms = getPermutations(array[:i] + array[i + 1:])
        for p in perms:
            permutations.append([array[i], *p])
    return permutations


getPermutations([1, 2, 3])
