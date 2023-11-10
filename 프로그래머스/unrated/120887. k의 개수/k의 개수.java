class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String str = "";
        for(int q = i;  q <= j; q++) {
            str += String.valueOf(q);
        }
        for(int r = 0; r < str.length(); r++) {
            if(str.charAt(r) == (char) (k+'0')) answer++;
        }
        return answer;
    }
}