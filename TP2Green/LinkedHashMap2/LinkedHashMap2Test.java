import java.util.*;

public class LinkedHashMap2Test {
    public static int Num_element = 10000000;
    public static void main(String args[]) {
        LinkedHashMap<Integer,String> map = new LinkedHashMap<Integer,String>();

        InsertElement(map, Num_element);
        AccessElement(map);
        RemoveElement(map, Num_element);
    }
    
    public static void InsertElement(LinkedHashMap<Integer,String> map, int Num_element) {
        for (int i = 0; i < Num_element; i++) {
            map.put(i,"Number is " + i);
        }
    }

    public static void RemoveElement(LinkedHashMap<Integer,String> map, int Num_element) {
        for (int i = 0; i < Num_element; i++) {
            map.remove(i);
        }
    }

    public static void AccessElement(LinkedHashMap<Integer,String> map) {
        for (Map.Entry m : map.entrySet()) {
            m.getKey();
            m.getValue();
        }
    }

}
