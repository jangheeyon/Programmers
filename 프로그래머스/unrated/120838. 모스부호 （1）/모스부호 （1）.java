class Solution {
    public String solution(String letter) {
        String answer = "";
        String[] morse = { 
            ".-","-...","-.-.","-..",".","..-.",
            "--.","....","..",".---","-.-",".-..",
            "--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-",
            "-.--","--.."
        };
        String[] strArr = letter.split(" ");
        for(String str : strArr) {
            for(int i = 0; i<morse.length; i++) {
                if(str.equals(morse[i])) {
                    answer += Character.toString(i+'a');
                }
            }
        }
        return answer;
    }
}