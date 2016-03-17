package lists.linkedLists;

/*
 * An array-based implementation of list
 * **/
public class AList implements List{

	private static final int defaultSize = 10;	
	private int curr;
	private int listSize;
	private int length;     //number of all elements in the current list
	private Object [] listArray;

	public AList()	{ initialize(defaultSize);	}
	
	public AList(int size){ initialize(size); }
	
	private void initialize(int size){
		listArray = new Object[size];
		curr = 0;
		length = 0;
		listSize = size;
	}//Always find common statements and encapsulate them in a method
	
	@Override
	public void clear() {
		curr = 0;
		length = 0;
	}

	@Override
	public void insert(Object item) {
		
		// use assert more than if/else when judging values		
		assert(listSize < length):"List is full";
		
		for (int i = length; i < curr; i--)
			listArray[i] = listArray[i - 1];
		listArray[curr] = item;
		length++;
	}

	@Override
	public void append(Object item) {
		
		assert(listSize < length):"List is full";
		listArray[length++] = item;
		//Shorten statements as you can
	}

	@Override
	public Object remove() {
		assert(length == 0): "The list is empty";
		Object currItem = listArray[curr];
		
		for (int i = curr; i < length-1; i++)
			listArray[i] = listArray[i + 1];
		length--;
		return currItem;
	}

	@Override
	public void setFirst() {
		// TODO Auto-generated method stub
		assert(!isEmpty()): "The list is empty";
		curr = 1;
	}

	@Override
	public void next() {
		
		assert(curr < length): "No next item after the current position";
		curr++;		
	}

	@Override
	public void prev() {
		
		assert(curr !=  0): "No previous item before the current position";
		curr++;
	}

	@Override
	public int length() {
		
		return length;
	}

	@Override
	public void setPos(int pos) {
		assert(pos >=0 && pos < length ):"invalid pos value";
		curr = pos;
	}

	@Override
	public void setValue(Object val) {
		
		listArray[curr] = val;
	}

	@Override
	public Object currVal() {
		// TODO Auto-generated method stub
		return listArray[curr];
	}

	@Override
	public boolean isEmpty() {
		
		return (length == 0)?  true: false;
	}

	@Override
	public boolean isInList(Object item) {
		for(int i = 0; i < length; i++){
			if (listArray[i] == item)
				return true;
		}
		return false;
	}

	@Override
	public void print() {
		if(isEmpty())
			System.out.println("The list is empty");
		else{
			System.out.println("The list contains: ");
			for (int i = 0; i < length; i++)
				System.out.println(listArray[i]);
		}
		
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
