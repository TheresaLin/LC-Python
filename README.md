# Leetcode解題思維

## Recursion
1. if return 最基本的case
2. call function 
3. return 需要的答案
```py
def a(n):
  if (base case): 
    return
  要做什麼事 = a()
  return 需要的答案
```
* [binary tree(preorder + recursion)](https://github.com/TheresaLin/LC-sol/blob/main/Leetcode/104.py)
* [Fibonacci number(滾動數組優化)](https://github.com/TheresaLin/LC-sol/blob/main/Leetcode/509.py)

## Breadth First Search
拿來找最短路徑的演算法 



```py
d = [0]* 8    #d是存到從start到自己的距離 array8個位置從0開始
q = []        #q是存目前要拜訪得節點
visited = set()
q.append(n1)
visited.add(n1)
while q:
    head = q[0]
    print('name: ', head.name)
    if head == n7:
        return d[7]
    len_q = len(q)
    q.pop(0)
    for k in range(len_q):
        for i in head.neighbor:
            if i not in visited:
                q.append(i)
                visited.add(i)
                d[i.name] = d[head.name] +1
```
* [bfs的基本練習](https://github.com/TheresaLin/LC-sol/blob/main/bfs/bfs.ipynb)
