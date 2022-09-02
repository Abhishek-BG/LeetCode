import java.util.regex.Pattern;

public class swapwords {

    public static void findwords(String s) {
        Pattern pattern = Pattern.compile("\\s");
        String[] tmp = pattern.split(s);
        String res = "";
        for (int i = 0; i < tmp.length; i++) {
            if (i == tmp.length - 1) {
                res = tmp[i] + res;

            } else {
                res = " " + tmp[i] + res;
            }

        }
        System.out.println(res);
    }

    public static void main(String[] arg) {
        findwords("My name is raj");
    }

}
