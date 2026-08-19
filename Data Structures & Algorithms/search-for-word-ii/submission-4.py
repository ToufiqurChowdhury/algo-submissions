class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.word = None

        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w

        res = []
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None

            board[r][c] = "#"
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    dfs(nr, nc, next_node)
            board[r][c] = char

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        return res