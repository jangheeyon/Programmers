class Solution {
    public String solution(String my_string) {
        String answer = "";
        //answer에 하나씩 넣는데, answer에 없으면 넣음
        for(int i=0; i<my_string.length(); i++) {
            if(!answer.contains(String.valueOf(my_string.charAt(i)))) {
                answer += my_string.charAt(i);
            }
        }
        return answer;
    }
}