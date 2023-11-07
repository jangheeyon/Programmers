import java.util.*;

class Solution {
    public int solution(String before, String after) {
        int answer = 0;
        char[] char1 = before.toCharArray();
        char[] char2 = after.toCharArray();
        
        Arrays.sort(char1);
        Arrays.sort(char2);
        
        String str1 = new String(char1);
        String str2 = new String(char2);
        
        if(str1.equals(str2)) {
            answer = 1;
        } else {
            answer = 0;
        }
        return answer;
    }
}