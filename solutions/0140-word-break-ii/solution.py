class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            valid_sentences = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    rest_of_sentences = dfs(end)

                    for sentence in rest_of_sentences:
                        if sentence == "":
                            valid_sentences.append(word)
                        else:
                            valid_sentences.append(word + " " + sentence)

            memo[start] = valid_sentences
            return valid_sentences

        return dfs(0)

