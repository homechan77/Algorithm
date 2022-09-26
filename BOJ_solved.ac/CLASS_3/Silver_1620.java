import java.util.*;
import java.io.*;

public class s1620 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> pbook = new HashMap<String, Integer>();
        String[] key_pbook = new String[n+1];

        for(int i=1; i<n+1; i++) {
            String name = br.readLine();
            pbook.put(name, i);
            key_pbook[i] = name;
        }

        for(int i=0; i<m; i++) {
            String question = br.readLine();
            int verifi = question.charAt(0);
            if(65<=verifi && verifi <= 90) {
                System.out.println(pbook.get(question));
            } else {
                System.out.println(key_pbook[Integer.parseInt(question)]);
            }
        }
    }
}
