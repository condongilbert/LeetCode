def combinationSum(candidates, target):
    def backtrack(start, target, path, result):
        # If we reach the target, add the path to results
        if target == 0:
            result.append(path[:])
            return
        # If the target is negative, stop exploring
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            # Include the current number and recurse
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path, result)
            # Backtrack by removing the last element
            path.pop()
    
    result = []
    backtrack(0, target, [], result)
    return result

# Example
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))  # Output: [[2, 2, 3], [7]]