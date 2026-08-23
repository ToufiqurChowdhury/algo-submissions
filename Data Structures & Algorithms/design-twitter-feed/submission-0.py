class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_tweets = defaultdict(list)
        self.user_follows = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.user_tweets[userId].append((-self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        heap.extend(self.user_tweets[userId][-10:])
        for followeeId in self.user_follows[userId]:
            heap.extend(self.user_tweets[followeeId][-10:])
        heapq.heapify(heap)

        #return [tweetId for _, tweetId in heapq.nsmallest(10, heap)]
        feed = []
        while heap and len(feed)<10:
            feed.append(heapq.heappop(heap)[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].discard(followeeId)