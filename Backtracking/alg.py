def generate_parentheses(n):
    res = []

    def backtrack(open, close, path):
        if open == close == n:
            res.append(''.join(path))
            return
        if open < n:
            path.append('(')
            backtrack(open+1, close, path)
            # resetting
            path.pop()

        if open > close:
            path.append(')')
            backtrack(open, close+1, path)
            path.pop()
    backtrack(0, 0, [])
    return res


def combination_sum(candidates, target):
    res = []

    def backtrack(start, sum, path):
        if sum == 0:
            res.append(path[:])
            return

        for i in range(start, len(candidates)):
            if sum-candidates[i] >= 0:
                path.append(candidates[i])
                backtrack(i, sum-candidates[i], path)
                path.pop()

    backtrack(0, target, [])
    return res


def subset(arr):
    res = []

    def backtrack(start, path):
        res.append(path[:])

        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return res


def path_sum(root, target):
    def dfs(root, sum):
        if not root:
            return False

        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            return True

        return dfs(root.left, sum) or dfs(root.right, sum)

    return dfs(root, target)


def path_sum_II(root, targetSum):
    res = []

    def backtrack(root, sum, path):
        if not root:
            return
        sum -= root.val
        path.append(root.val)
        if sum == 0 and not root.left and not root.right:
            res.append(path[:])

        backtrack(root.left, sum, path)
        backtrack(root.right, sum, path)
        path.pop()

    backtrack(root, targetSum, [])
    return res
