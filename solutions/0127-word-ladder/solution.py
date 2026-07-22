class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current_word, level = queue.popleft()

            if current_word == endWord:
                return level

            for i in range(len(current_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = current_word[:i] + c + current_word[i + 1 :]

                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))

        return 0

