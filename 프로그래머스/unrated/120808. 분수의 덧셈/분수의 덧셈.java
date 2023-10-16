class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = {};
        int son = (numer1*denom2)+(numer2*denom1);
        int mom = denom1*denom2;
        //최대공약수(유클리드 호제법)
        int mcn = ucl(son, mom);
        answer = new int[]{son/mcn, mom/mcn};
        return answer;
    }
    int ucl(int a, int b) {
        if(a%b==0) return b;
        return ucl(b, a%b);
    }
}