def count_smileys(arr):
    sum = 0
    valid_eyes = ':;'
    valid_noses = '-~'
    valid_smiles = ')D'
    
    if not arr:
        return 0
    else:
        for i in range(len(arr)):
            if len(arr[i]) == 2:
                if (arr[i][0] in valid_eyes and arr[i][1] in valid_smiles):
                    sum += 1
            if len(arr[i]) == 3:
                if (arr[i][0] in valid_eyes and arr[i][2] in valid_smiles and arr[i][1] in valid_noses):
                    sum += 1
    return sum
