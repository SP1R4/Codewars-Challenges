def permutations(input):
    
    if len(input) == 1:
        return input if isinstance(input, list) else [input]

    result = []
    for i in range(len(input)):
        first = input[i]
        rest = input[:i] + input[i + 1:]
        rest_permutation = permutations(rest)
        for p in rest_permutation:
            result.append(first + p)
    return list(dict.fromkeys(result))
