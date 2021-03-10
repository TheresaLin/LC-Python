def two_cnt_sum(l, target):
    # please return a list of two nums which have count sum up as target
    # the list should be sorted in ascending order
    # e.g. [1, 2, 1, 2, 1]
    # then you should return [1, 2] because 1 shows up 3 times and 2 shows up 2 times
    # also you cannot return [2, 1]
    
        
    res = []
    count = {}
    n = 0
    for i in l:
        if i in count: 
            count[i] += 1
        else:
            count[i] = n+1
    
    for i in count:
        for j in count:
            if count[i]+count[j] == target:
                if j > i:
                    res.append([i,j])

    return res

if __name__ == '__main__':
    ipt = [2,2,3,4,3,3,4,4,1,1,5,5]
    target = 5
    res = two_cnt_sum(ipt, target)
    print(res)
