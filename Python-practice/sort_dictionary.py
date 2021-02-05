def sort_dict(dictionary):
    # Please sort dictionary with the second value in list in ascending order
    # {'key1': [..., a], 'key2': [..., b]}
    # a needs to be smaller than b
    # please finish this function
    
    #use items()to flatten the list
    dictionary = sorted(d.items(), key=lambda e:e[1][1])

    return dictionary

if __name__ == '__main__':
    d = {'k1': [2, 3], 'k2': [3, 2], 'k3': [5, 4], 'k4': [6, 1]}
    print(sort_dict(d))