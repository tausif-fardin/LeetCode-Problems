class Solution {
public:
    string addStrings(string num1, string num2) {
         int n1 = num1.length(), n2 = num2.length();
        if (n1 < n2) return addStrings(num2, num1);
        int carry = 0;
        string res;
        for (int i = 0; i < n1; i++) {
            int a = num1[n1-1-i] - '0';
            int b = i < n2 ? num2[n2-1-i] - '0' : 0;
            int sum = a + b + carry;
            res = to_string(sum % 10) + res;
            carry = sum / 10;
        }
        return carry ? to_string(carry) + res : res;
    }
};