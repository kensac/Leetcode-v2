class Twitter:

    def __init__(self):
        self.follower_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        self.follower_map[userId].add(userId)
        for follower in self.follower_map[userId]:
            for meta in self.tweet_map[follower]:
                heappush(tweets, meta)
                if len(tweets) > 10:
                    heappop(tweets)
        res = []
        while tweets:
            time, tweet = heappop(tweets)
            res.append(tweet)

        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
