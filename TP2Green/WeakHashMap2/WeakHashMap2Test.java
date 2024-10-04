import java.util.*;

public class WeakHashMap2Test {
    public static int Num_element = 100000000;

    public static void main(String args[]) {
        WeakHashMap2Test map = new WeakHashMap2Test();
        map.InsertElement();
        map.AccessElement();
        map.RemoveElement();
    }

    public void InsertElement() {
        WeakHashMap<Integer,String> map = new WeakHashMap<Integer,String>();
        for (int i = 0; i < Num_element; i++) {
            map.put(i,"Number is " + i);
        }
    }

    public void RemoveElement() {
        WeakHashMap<Integer,String> map = new WeakHashMap<Integer,String>();
        for (int i = 0; i < Num_element; i++) {
            map.remove(i);
        }
    }

    public void AccessElement() {
        WeakHashMap<Integer,String> map = new WeakHashMap<Integer,String>();
        for (Map.Entry<Integer, String> m : map.entrySet()) {
            m.getKey();
            m.getValue();
        }
    }
}
