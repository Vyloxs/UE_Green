import java.util.*;

public class ArrayList2Test {
    public static int Num_element = 1000000;
       public static void main(String args[]) {
        ArrayList<String> list = new ArrayList<String>();

        InsertElement(list, Num_element);
        AccessElement(list);
        RemoveElement(list, Num_element);
    }

    public static void InsertElement(ArrayList<String> list, int Num_element) {
        for (int i = 0; i < Num_element; i++) {
            list.add("Number is " + i);
        }
    }

    public static void RemoveElement(ArrayList<String> list, int Num_element) {
        for (int i = 0; i < Num_element; i++) {
            list.remove(i);
        }
    }

    public static void AccessElement(ArrayList<String> list) {
        Iterator itr = list.iterator();
        while (itr.hasNext()) {
            itr.next();
        }
    }
}
