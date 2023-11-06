class Solution {
    public int solution(int num, int k) {
        int answer = 0;
        String strNum = String.valueOf(num);
        String strK = String.valueOf(k);
        if(strNum.indexOf(strK) > -1 ) {
            answer = strNum.indexOf(strK)+1;
        }else {
            answer = -1;
        }
        return answer;
    }
}