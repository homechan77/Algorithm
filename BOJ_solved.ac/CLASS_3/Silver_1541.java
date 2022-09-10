// 잃어버린 괄호

import java.util.*;

public class Main {
    public static int sumall(ArrayList<Integer> forsum) {
        int sum = 0;
        for(int i : forsum) {
            sum += i;
        }
        return sum;
    }

    public static ArrayList solution(String exp) {
        int memory = 0;
        ArrayList<Integer> forsum = new ArrayList<Integer>();
        ArrayList<Integer> result = new ArrayList<Integer>();

        for(int i=0; i<exp.length(); i++) {
            if(exp.charAt(i) == '+' || exp.charAt(i) == '-') {
                forsum.add(Integer.parseInt(exp.substring(memory, i)));
                memory = i+1;
                if(exp.charAt(i) == '-') {
                    int sum = sumall(forsum);
                    result.add(sum);
                    forsum.clear();
                }
            }
            if(i == exp.length()-1) {
                forsum.add(Integer.parseInt(exp.substring(memory, i+1)));
            }
        }
        int sum = sumall(forsum);
        result.add(sum);
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String exp = sc.nextLine();

        ArrayList<Integer> result = solution(exp);

        int answer = result.get(0);
        for(int i = 1; i < result.size(); i++){
            answer -= result.get(i);
        }
        System.out.println(answer);
    }
}
