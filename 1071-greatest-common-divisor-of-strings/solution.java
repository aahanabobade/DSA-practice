// Greatest Common Divisor of Strings
// Difficulty: Easy
// Runtime: 0 ms
// Memory: 42.3 MB
// https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution {
    public String gcdOfStrings(String str1, String str2) {
        // Check if concatenations are equal
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }

        // Find GCD of lengths
        int gcdLength = gcd(str1.length(), str2.length());

        // Return prefix of that length from str1
        return str1.substring(0, gcdLength);
    }

    // Euclidean algorithm for GCD of two integers
    private int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
}
