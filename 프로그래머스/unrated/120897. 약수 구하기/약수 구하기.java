import java.util.*;

class Solution {
    public int[] solution(int n) {
        int cnt = 0;
        for(int i = n; i > 0; i--){
            if(n % i == 0) {
                cnt++;
            }
        }
        int[] answer = new int[cnt];
        int index = 0;
        for(int j = n; j > 0; j--) {
            if(n % j == 0) {
                answer[index] = n / j;
                index++;
            }
        }
        return answer;
    }
}