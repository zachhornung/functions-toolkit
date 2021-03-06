import functools
from math import sqrt

# Iterative way to do Fibonacci sequence. returns Fibonacci number at the given index
def fib_iter(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
    return a


# Recursive way to do Fibonacci sequence. Returns Fibonacci number at the given index.
def fib_rec(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib_rec(num-1) + fib_rec(num-2)


# General way to generate a sequence of numbers recursively. takes 1 positional argument, and 2 keyword arguments
def sum_series_recursive(num, a=0, b=1):
    if num == a:
        return a
    if num == b:
        return b
    return sum_series_recursive(num-1, a, b) + sum_series_recursive(num-2, a, b)


# General way to generate a sequence of numbers, iteratively. takes 1 positional argument and 2 optional keyword arguments. 
def sum_series_iterative(num, starting1=0, starting2=1):
    a,b = starting1,starting2
    for _ in range(num):
        a,b = b, a+b
    return a


def tower_of_hanoi(num, current, destination, aux_rod):
    if num == 1:
        print(f'\nMove disk 1 from rod {current} to rod {destination}')
        return
    tower_of_hanoi(num-1, current, aux_rod, destination)
    print(f'\nMove disk {num} from rod {current} to rod {destination}')
    tower_of_hanoi(num-1, aux_rod, destination, current)

#Looks to see if there are two numbers in the given array that add up to the given target number. Optimal solution because sets lookup has O(1) time.
def find_two_sum(arr, target_sum):
    compliment = set()
    for num in arr:
        if target_sum-num in compliment:
            return f'{target_sum-num}, {num}, sum to {target_sum}'
        compliment.add(num) 


def find_three_sum(arr, target_sum):
    compliment = set()
    for i in range(len(arr)):
        looking_for = target_sum - arr[i] # Looking_for will be the other two numbers we need to compliment num in order to add to get the target_sum
        j, k = i+1, len(arr)-1
        while j < k:
            if arr[i]+arr[j]+arr[k] == target_sum:
                return f'solution is {arr[i]}, {arr[j]}, {arr[k]}'
            compliment.add(arr[i])
            compliment.add(arr[j])
            compliment.add(arr[k])
            if looking_for-arr[j] in compliment:
                return 'got it'
            if looking_for-arr[k] in compliment:
                return 'also got it'
        set.add(arr[i])


# memoization really speeds up recursive functions. The memo in this takes this from O(2^N) to O(N).
# The memo will be passed to each recursive call and updated by each unique number that has not been calculated yet
# If the number has been calculated, then the function call will just return the stored value in the memo.
def memoized_fib_recursive(num, memo={}):
    if num < 2:
        return num
    if num in memo:
        return memo[num]
    memo[num] = memoized_fib_recursive(num-1, memo) + memoized_fib_recursive(num-2, memo)
    return memo[num]

# this is the more pythonic way to memoize recursive functions, using the functools library.
@functools.lru_cache(maxsize=None)
def fib_with_cache(num):
    if num < 2:
        return num
    return fib_with_cache(num-1) + fib_with_cache(num-2)

def fib_formula(n):
    p = ((1+sqrt(5))/2)**n
    q = ((1-sqrt(5))/2)**n
    fib = (p-q)/sqrt(5)
    return int(fib)

#checks for brackets with elemination based approach
def bracket_checker(string):
    string = ''.join([char for char in string if char in '(){}[]']) # all non bracket characters are removed from the string
    while any(char in string for char in ['()', '{}', '[]']): # while there are any pairs of brackets in the string
        string = string.replace('()', '').replace('{}', '').replace('[]', '') # remove any current pairs of brackets from the string
    return not string #this will return false if there are orphan brackets remaining in the string, and true if the string is empty.

def most_consecutive_nums(arr):
    hash_map = {num:0 for num in arr}
    l = r = 0
    for num in arr:
        if hash_map.get(num):
            continue
        i = num-1
        j = num+1
        while True:
            if i in hash_map:
                hash_map[i] += 1
                i -= 1
                continue
            if j in hash_map:
                hash_map[j] += 1
                j += 1
                continue
            tl = i
            tr = j
            if (tr - tl) > r - l:
                l = tl
                r = tr
            break
    return r - l -1

def diameterOfBinaryTree(root):
    res = 0
    def walk(root):
        nonlocal res
        if root is None:
            return 0 
        left = walk(root.left)
        right = walk(root.right)
    
        res = max(res, 1 + left + right)
        return 1 + max(left, right)
    walk(root)  
    return res-1

from collections import Counter

def find_clusters(mat):
    clusters = {}
    for y, row in enumerate(mat):
        for x, col_val in enumerate(row):
            if col_val == 1:
                left = (x-1,y)
                above = (x,y-1)
            if left in clusters:
                origin = clusters[left]
            elif above in clusters:
                origin = clusters[above]
            else:
                origin = (x,y)
        clusters[(x,y)] = origin

    return Counter(clusters.values()).values()

def simplifyPath(path):
    s1 = []
    i = j = 0
    while i < len(path):
        if path[i] == '/':
            i += 1
            j += 1
            continue
        while (j < len(path)) and (path[j] != '/'):
            j += 1
        if path[i:j] == '..':
            if not s1:
                j += 1
                i = j
                continue
            s1.pop()
            j += 1
            i = j
            continue
        if path[i:j] == '.':
            j += 1
            i = j
            continue
        s1.append(f'/{path[i:j]}')
        j += 1
        i = j
    if not s1:
        s1.append('/')
    return ''.join(s1)


def preorder(root):
    ans = []
    def dive(root):
        nonlocal ans
        if not root:
            return
        ans.append(root.val)
        for child in root.children:
            dive(child)
    dive(root)
    return ans

def preorder(root):
    def dive(root):
        if root:
            ans = [root.val]
            for child in root.children:
                ans.extend(dive(child))
            return ans
        return []
    return dive(root)

def postorderTraversal(root):
    ans = []
    def dive(root):
        nonlocal ans
        if not root:
            return 
        dive(root.left)
        dive(root.right)
        ans.append(root.val)
    dive(root)
    return ans

def checkValidString(s):
    count = 0
    for char in s:
        if char == ')':
            count -= 1
        else:
            count += 1
        if count < 0:
            return False
    if not count:
        return True
    count = 0
    for char in reversed(s):
        if char == '(':
            count -= 1
        else:
            count += 1
        if count < 0:
            return False
    return True

def reverseParentheses(s):
    loc = []
    og = s
    for i, char in enumerate(og):
        if char == '(':
            loc.append(i)
        if char == ')':
            start = loc.pop()
            end = i
            s = s[0:start+1]+s[start+1:end][::-1]+s[end:]
    return ''.join([c for c in s if c not in '()'])

def scoreOfParentheses(s):
    st = [0]
    for c in s:
        if c == '(':
            st.append(0)
            continue
        close = st.pop()
        if close == 0:
            score = 1
            st[-1] += score
            continue
        score = close * 2
        st[-1] += score
    return st[0]

def maximumGain(s, x, y):
    a, b = "a", "b"
    if x < y: 
        x, y = y, x
        a, b = b, a
    ans = cnt0 = cnt1 = 0
    for c in s: 
        if c not in "ab": 
            ans += min(cnt0, cnt1) * y
            cnt0 = cnt1 = 0 
            continue
        if c == b:
            if cnt0: 
                cnt0 -= 1
                ans += x
                continue
            cnt1 += 1
            continue
        cnt0 += 1
    return ans + min(cnt0, cnt1) * y

if __name__ == '__main__':
    tower_of_hanoi(3, 'a', 'b', 'c',)
    