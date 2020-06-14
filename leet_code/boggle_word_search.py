'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" 
cells are those horizontally or vertically neighboring. The same letter cell may not be 
used more than once in a word.

Notes:
* runtime - k words, n rows, n columns
  * brute force = O(m^2 n^2 k)
    * mnk invocations of contains_word_at_position each doing a DFS (each of O(V)). Since V = (m-1)*n + (n-1)*m = 2mn - (m+n).
  * trie = O(m^2 n^2)
* what went right
  * got brute force / DFS solution right except for subtle visited flag bug
  * defensive coding in contains_word_at_position
  * got the Trie class implementation right
  * got the Trie word search implementation right except for subtle visited flag bug
* what went wrong
  * subtle bug with DFS - need to set visited to False after exploring all 4 directions since character can be revisited along a separate route
  * brute force
    * didn't check that index counters were being incremented
    * didn't set inner loop counter to zero inside the loop
  * trie implementation
    * wrong index for node.children
    * forgot to set visited flag

'''
from copy import copy 

class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.match = False
        self.children = {}
    
def print_trie(node, prefix):
    prefix += node.val
    if node.match == True:
        print(prefix)
    for c in node.children.values():
        print_trie(c, prefix)


def insert_trie(node, s, i, n):
    if s[i] not in node.children:
        node.children[s[i]] = TrieNode(s[i])
    if i == n - 1:
        node.children[s[i]].match = True
    else:
        insert_trie(node.children[s[i]], s, i+1, n)
        
def word_search_trie(board, words):
    def find_matches(board, node, i, j, visited, matches, prefix):
        if i < 0 or i >= n or j < 0 or j >= m:
            return
        c = board[i][j]
        if visited[i][j] == False and c in node.children:
            visited[i][j] = True
            prefix += c
            if node.children[c].match == True:
                matches.append(copy(prefix))
            find_matches(board, node.children[c], i-1, j, visited, matches, prefix)
            find_matches(board, node.children[c], i+1, j, visited, matches, prefix)
            find_matches(board, node.children[c], i, j-1, visited, matches, prefix)
            find_matches(board, node.children[c], i, j+1, visited, matches, prefix)
            visited[i][j] = False


    root = TrieNode('')
    for w in words:
        insert_trie(root, w, 0, len(w))
    #print_trie(root, '')

    n = len(board)
    m = len(board[0])
    i = 0
    matches = []
    while i < n:
        j = 0
        while j < m:
            visited = [[False] * m for _ in range(n)]
            find_matches(board, root, i, j, visited, matches, '')
            j += 1
        i += 1
    return list(set(matches)) 


def word_search_brute(board, words):
    n = len(board)
    m = len(board[0])

    def contains_word_at_position(board, word, offset, i, j, visited):
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        if offset >= len(word):
            return True
        if visited[i][j] == False and board[i][j] == word[offset]:
            visited[i][j] = True
            if contains_word_at_position(board, word, offset+1, i+1, j, visited):
                return True
            if contains_word_at_position(board, word, offset+1, i-1, j, visited):
                return True
            if contains_word_at_position(board, word, offset+1, i, j-1, visited):
                return True
            if contains_word_at_position(board, word, offset+1, i, j+1, visited):
                return True
            visited[i][j] = False
        return False

    i = 0
    matches = []
    while i < n:
        j = 0
        while j < m:
            for word in words:
                visited = [[False] * m for _ in range(n)]
                if contains_word_at_position(board, word, 0, i, j, visited):
                    matches.append(word)
            j += 1
        i += 1
    return list(set(matches))



if __name__ == '__main__':
    test_cases = [
        ([
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
        ], ["oath","pea","eat","rain"]),
        ([
            ["b","a","a","b","a","b"],
            ["a","b","a","a","a","a"],
            ["a","b","a","a","a","b"],
            ["a","b","a","b","b","a"],
            ["a","a","b","b","a","b"],
            ["a","a","b","b","b","a"],
            ["a","a","b","a","a","b"]],
        ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa",
        "bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa",
        "babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa",
        "aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab",
        "aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa",
        "aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb",
        "aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab",
        "bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab",
        "aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa",
        "abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]),
    ]
    for t in test_cases:
        board, words = t[0], t[1]
        print(word_search_brute(board, words))
        print(word_search_trie(board, words))

        

