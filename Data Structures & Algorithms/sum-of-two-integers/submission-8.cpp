class Solution {
public:
    int getSum(int a, int b) {

        if (a>0 && b>0 && a>INT_MAX-b)
            return -1;
        if (a<0 && b<0 && b<INT_MIN-b)
            return -1;
        
        int sum = a+b;

        return sum;
    }
};
