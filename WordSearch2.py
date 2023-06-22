from collections import defaultdict
class solution:

    #https://leetcode.com/problems/word-search-ii/description/
    #20.60% time complexity, 32.88% space complexity solution for LeetCode 212
    
    def findWords(self, board, words):
        prefixes = defaultdict(list)
        word_set = set(words)

        for word in words:
            for i in range(1, len(word)+1):
                prefixes[word[:i]].append(word)

        result = set()

        def traverse(string, row, col, visited):
            if string not in prefixes or (row, col) in visited:
                return

            visited.add((row, col))
            
            if string in word_set:
                result.add(string)

            if row > 0:
                traverse(string+board[row-1][col], row-1, col, set(visited))

            if col > 0:
                traverse(string+board[row][col-1], row, col-1, set(visited))
            
            if row < len(board)-1:
                traverse(string+board[row+1][col], row+1, col, set(visited))

            if col < len(board[0])-1:
                traverse(string+board[row][col+1], row, col+1, set(visited))
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in prefixes and not set(prefixes[board[row][col]]).issubset(result):
                    traverse(board[row][col], row, col, set())

        return list(result)