def two_cnt_sum(l, target):
    # please return a list of two nums which have count sum up as target
    # the list should be sorted in ascending order
    # e.g. [1, 2, 1, 2, 1]
    # then you should return [1, 2] because 1 shows up 3 times and 2 shows up 2 times
    # also you cannot return [2, 1]
    
        
    res = []
    
    for i in l:
        for j in l:
            if i+j == target:
                if i>j:
                    res.append(j)
                    res.append(i)
                else:
                    res.append(i)
                    res.append(j)
                    return res
            else:
                continue

if __name__ == '__main__':
    ipt = [1, 2, 3, 2, 5, 1, 7, 2, 1, 9, 6, 3]
    target = 5
    res = two_cnt_sum(ipt, target)
    print(res)
