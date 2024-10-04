import java.util.*;

public class TreeMap2Test {
    public static int Num_element = 10000000;
    public static void main(String args[]) {
        TreeMap<Integer,String> map = new TreeMap<Integer,String>();

        InsertElement(map);
        AccessElement(map);
        RemoveElement(map);
    }
    
    public static void InsertElement(TreeMap<Integer,String> map) {
        for (int i = 0; i < Num_element; i++) {
            map.put(i,"Number is " + i);
        }
    }

    public static void RemoveElement(TreeMap<Integer,String> map) {
        for (int i = 0; i < Num_element; i++) {
            map.remove(i);
        }
    }

    public static void AccessElement(TreeMap<Integer,String> map) {
        for (Map.Entry m : map.entrySet()) {
            m.getKey();
            m.getValue();
        }
    }
}
