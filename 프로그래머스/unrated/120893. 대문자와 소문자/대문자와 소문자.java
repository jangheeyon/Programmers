//toUpperClass(), toLowerCase()                    
class Solution {
    public String solution(String my_string) {
        String answer = "";
        for(int i=0; i<my_string.length(); i++) {
          String str = String.valueOf(my_string.charAt(i));
          if(str.equals(str.toUpperCase())) {
              answer += str.toLowerCase();
          }else {
             answer += str.toUpperCase(); 
          }
        }
        return answer;
    }
}