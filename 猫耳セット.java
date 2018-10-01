// Hint from https://stackoverflow.com/questions/767759/occurrences-of-substring-in-a-string

import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String findStr = "cat";
        System.out.println(str.split(findStr, -1).length-1);
    }
}