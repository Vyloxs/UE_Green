import java.util.*;

public class LinkedList2Test {
    public static int Num_element = 250000;
    public static void main(String args[]) {
        LinkedList<String> list = new LinkedList<String>();

        InsertElement(list, Num_element);
        AccessElement(list);
        RemoveElement(list, Num_element);
    }

    public static void InsertElement(LinkedList<String> list, int Num_element) {
        for (int i = 0; i < Num_element; i++) {
            list.add("Number is " + i);
        }
    }

    public static void RemoveElement(LinkedList<String> list, int Num_element) {
        for (int i = 0; i < Num_element; i++) {
            list.remove(i);
        }
    }

    public static void AccessElement(LinkedList<String> list) {
        Iterator itr = list.iterator();
        while (itr.hasNext()) {
            itr.next();
        }
    }
}
