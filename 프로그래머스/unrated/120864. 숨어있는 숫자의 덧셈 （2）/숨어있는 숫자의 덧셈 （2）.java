class Solution {
    public int solution(String my_string) {
        int answer = 0;
        //문자만 모두 없앤 것을 answer에 더함
        String[] arr = my_string.replaceAll("[a-zA-Z]", " ").split(" ");
        for(String str : arr) {
            if(!str.equals("")) answer += Integer.valueOf(str);
        }
        return answer;
    }
}