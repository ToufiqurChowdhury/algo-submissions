class Solution {
public:

    string encode(vector<string>& strs) {
        string encStr = "";
        for (string& s:strs){
            encStr += to_string(s.size()) + "#" + s;  
        }

        return encStr;
    }


    vector<string> decode(string s) {
        vector<string> res;

        int i = 0;
        while(i < s.size()){
            int hasPos = s.find('#', i);            
            int len = stoi(s.substr(i, hasPos-i));
            res.push_back(s.substr(hasPos+1, len));
            i = hasPos + 1 + len;
        }

        return res;
    }
};
