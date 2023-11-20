class Solution {
    public int solution(int n) {
        int answer = 1;
        int cnt = 0;
        for(int i=1; i<=n; i++) {
            answer *= i;
            if(answer == n) {
                cnt = i;
                break;
            }else if(answer > n) {
                cnt = i-1;
                break;
            }
        }
        return cnt;
    }
}