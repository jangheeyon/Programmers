import java.util.*;

class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int tmp = 100;
        for(int i=0; i<array.length; i++) {
            if(Math.abs(array[i] - n) < tmp) {
                tmp = Math.abs(array[i] - n);
                answer = array[i];
            }else if(Math.abs(array[i] - n) == tmp && array[i] < answer) {
                answer = array[i];
            }
        }
        return answer;
    }
}