import java.util.Iterator;
public class DLL implements Iterable<LT>{
    private LT first_item;
    private LT last_item;
    private int length = 0;

    public DLL(){}

    public LT get_first_item(){
        return this.first_item;
    }

    public LT get_last_item(){
        return this.last_item;
    }

    public int get_length(){
        return this.length;
    }

    private void push_lenght(){
        this.length = this.length + 1;
    }

    private void bump_lenght(){
        this.length = this.length - 1;
    }

    public void insert_after(Object value){
        LT l = new LT(value);

        if (this.first_item == null) {
            this.first_item = l;
            this.last_item = l;
            this.push_lenght();
        } else {
            this.last_item.set_next_item(l);
            l.set_previous_item(this.last_item);
            this.last_item = l;
            this.push_lenght();
        }
        return;
    }

    public void insert_before(Object value){
        LT l = new LT(value);

        if (this.first_item == null) {
            this.first_item = l;
            this.last_item = l;
            this.push_lenght();
        } else {
            this.first_item.set_previous_item(l);
            l.set_next_item(this.first_item);
            this.first_item = l;
            this.push_lenght();
        }
        return;
    }

    public boolean contain(Object value){
        var l = this.first_item;
        while(l != null){
            if(l.get_item_value() == value) {
                return true;
            } else {
                l = l.get_next_item();
            }
        }
        return false;
    }

    public Iterator<LT> iterator() {
        return new LTIterator();
    }

    class LTIterator implements Iterator<LT> {
        private LT current;

        public boolean hasNext() {
            if (current == null){
                current = first_item;
            } else {
                current = current.get_next_item();
            }

            if (current == null) {
                return false;
            } else {
                return true;
            }
        }

        public LT next() {
            return current;
        }

        public void remove() {
            throw new UnsupportedOperationException("not supported yet");

        }
   }
}

class LT{
    private LT next_item;
    private LT previous_item;
    private Object item_value;

    public LT(){};

    public LT(LT next_item, LT previous_item, Object item_value){
        this.next_item = next_item;
        this.previous_item = previous_item;
        this.item_value = item_value;
    };

    public LT(Object item_value){
        this.next_item = null;
        this.previous_item = null;
        this.item_value = item_value;
    };

    public void set_next_item(LT item){
        this.next_item = item;
    }
    public void set_previous_item(LT item){
        this.previous_item = item;
    }
    public void set_item_value(Object value){
        this.item_value = value;
    }

    public LT get_next_item(){
        return this.next_item;
    }

    public LT get_previous_item(){
        return this.previous_item;
    }

    public Object get_item_value(){
        return this.item_value;
    }
}