class Logger:

    def __init__(self):
        self.logMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logMap:
            self.logMap[message] = timestamp
            return True
        
        prevTime = self.logMap[message]

        if timestamp-prevTime >= 10:
            self.logMap[message] = timestamp
            return True
        
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
