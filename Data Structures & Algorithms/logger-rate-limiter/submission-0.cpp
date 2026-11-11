class Logger {
private:
    map<string, int> logmap;
public:
    Logger() {
        
        
    }
    
    bool shouldPrintMessage(int timestamp, string message) {
        if (!logmap.count(message)){
            logmap[message] = timestamp;
            return true;
        }

        int prevlogtime = logmap[message];

        if (timestamp-prevlogtime >= 10) {
            logmap[message] = timestamp;

            return true;
        }

        return false;
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */
