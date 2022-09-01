
/*
 * coin height problem solved in a very easy manner .
 */
import java.util.*;

public class CoinHeightProblem {

    public static void findheight(int no_of_coins) {
        int num = no_of_coins;
        int count = 0;
        int height = 0;
        for (int i = 0; i <= num; i++) {
            count = count + i;
            if (num - count > i) {
                height++;
            }
        }
        System.out.println(height++);
    }

    public static void main(String[] args) {
        Scanner Sc = new Scanner(System.in);
        int num = Sc.nextInt();
        findheight(num);
    }

}
