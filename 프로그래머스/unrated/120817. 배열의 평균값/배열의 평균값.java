class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int cnt = 0;
        for(double nums : numbers) {
            answer= answer+nums;
            cnt++;
        }
        return answer/cnt;
    }
}