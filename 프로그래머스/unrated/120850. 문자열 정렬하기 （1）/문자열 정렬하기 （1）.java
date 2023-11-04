import java.util.*;

class Solution {
    public int[] solution(String my_string) {        
        String[] strArr = my_string.replaceAll("[a-z]", "").split("");
        int[] intArr = new int[strArr.length];
        for (int i = 0; i < strArr.length; i++) {
        	intArr[i] = Integer.parseInt(strArr[i]);
		}
        Arrays.sort(intArr);
    	return intArr;
    }
}