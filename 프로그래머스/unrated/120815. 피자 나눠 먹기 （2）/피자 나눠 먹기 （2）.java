class Solution {
    public int solution(int n) {
        int pizza = (n%6 != 0) ?  ((6*n)/gcd(6, n))/6 : n/6;
        return pizza;
    }
    public int gcd(int num1, int num2) {
        if (num1 % num2 == 0) {
            return num2;
        }
        return gcd(num2, num1%num2);
    }
}