import java.util.*;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        //배열을 string으로 만들어 다 붙이고, 그 안에서 "7"문자열의 수를 세기
        String str = "";
        for(int i=0; i<array.length; i++) {
            str += String.valueOf(array[i]);
        }
        for(int j=0; j<str.length(); j++) {
            if(str.charAt(j) == '7') {
                answer++;
            }
        }
        return answer;
    }
}