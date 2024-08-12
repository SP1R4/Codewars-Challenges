def combos(num):
    memo = {}

    def generate_combinations(target):
        if target in memo:
            return memo[target]

        if target == 0:
            return [[]]

        if target < 0:
            return None

        result = []
        for i in range(1, target + 1):
            sub_combos = generate_combinations(target - i)
            if sub_combos is not None:
                for combo in sub_combos:
                    new_combo = [i] + combo
                    new_combo.sort()
                    if new_combo not in result:
                        result.append(new_combo)

        memo[target] = result
        return result

    return generate_combinations(num)