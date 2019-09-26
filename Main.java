class Main {
    public static void main(String[] args) {
        DLL d = new DLL();
        d.insert_after(1);
        d.insert_after(2);
        d.insert_after(3);
        d.insert_after(4);
        d.insert_after(5);
        d.insert_after(6);
        d.insert_after(7);
        System.out.println(d.get_length());
        System.out.println(d.contain(5));

        for (LT item : d) {
            System.out.println(item.get_item_value());            
        }
    }
}