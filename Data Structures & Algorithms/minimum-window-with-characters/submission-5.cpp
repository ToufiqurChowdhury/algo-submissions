class Solution {
public:
    string minWindow(string s, string t) {
        if (t == "") return "";

        unordered_map<char, int> countT, window;
        for (char c:t){
            countT[c]++;
        }

        int have=0, need=countT.size();

        pair<int, int> res(-1, -1);
        int reslen = INT_MAX;

        int l=0;
        for (int r=0; r<s.size(); r++){
            char c = s[r];
            window[c]++;

            if (countT.count(c) && window[c] == countT[c]) { 
                have += 1; 
            }

            while (have==need) {
                // update our result
                if (r-l+1 < reslen){
                    res = {l, r};               // res is min window
                    reslen = r-l+1;             // length of min window
                }

                // pop from left of window
                window[s[l]] -= 1;
                if (countT.count(s[l]) && window[s[l]] < countT[s[l]]) {
                    have -= 1;
                }
                l += 1;
            }
        }

        if (reslen != INT_MAX){
            return s.substr(res.first, reslen);
        }
        else return "";
    }
};
