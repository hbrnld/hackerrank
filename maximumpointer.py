# Maximum pointer with bad integer
# Starting with i = 0, and j = 1, for each step you have two choices
# 1. The pointer i stays
# 2. The pointer moves to i + j
# j is always incremented by one
# Find the maximum integer that can be reached in n steps, when needing to avoid the integer badIndex.

def maxPointer(n, badIndex):
    maxList = [int(i*(i+1)/2) for i in range(1, n+1)]
    print(maxList)

    if badIndex in maxList:
        return maxList[-1]-1
    else:
        return maxList[-1]

def main():
    max_steps = 5
    badIndex = 1
    print(maxPointer(max_steps, badIndex))

if __name__ == '__main__':
    main()

    

    