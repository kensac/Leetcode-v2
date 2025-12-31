class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # Create graph
        graph = defaultdict(set)

        for word in wordList:
            for idx, char in enumerate(word):
                graph[word[:idx] + "*" + word[idx + 1:]].add(word)

        seen = set()
        queue = Deque([[beginWord]])
        distance = 1

        while queue:
            #print(queue)
            cur_level = queue.popleft()
            new_level = []
            for cur_word in cur_level:
                if cur_word == endWord:
                    return distance
                seen.add(cur_word)
                for idx, char in enumerate(cur_word):
                    generic_to_check = cur_word[:idx] + "*" + cur_word[idx + 1:]

                    #print(cur_word, generic_to_check)
                    for word in graph[generic_to_check]:
                        #print(word, endWord)
                        if word not in seen:
                            new_level.append(word)
            if new_level:
                queue.append(new_level)
            distance += 1

        return 0
