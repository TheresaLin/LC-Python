# 607. Two Sum III - Data structure design

class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """

    # store add value
    twoSum_list = []
    def add(self, number):
        # write your code here
        self.twoSum_list.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        if not self.twoSum_list or len(self.twoSum_list) < 2:
            return False
        # twoSum_set is to store target value - number in twoSum_list
        twoSum_set = set()
        for i in self.twoSum_list:
            if i not in twoSum_set:
                twoSum_set.add(value - i)
            else:
                return True
        return False
