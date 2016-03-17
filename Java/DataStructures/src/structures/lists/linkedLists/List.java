package lists.linkedLists;

public interface List {
	public void clear(); // Remove all objects from the list
	public void insert(Object item); //Insert object at the current position
	public void append(Object item); //Insert object at the tail
	public Object remove();          //Remove and return the current object
	public void setFirst();	//Set current to first position
	public void next();    //Move current to the next position
	public void prev();    //Move current to the previous position
	public int length();	//Return current length of the list
	public void setPos(int pos);   //Set current to specified pos
	public void setValue(Object val); //Set current object's value
	public Object currVal();    //Return value of current object
	public boolean isEmpty();	//Return true if list is empty
	public boolean isInList(Object item);  //True if current is within list
	public void print();		//Print the all the elements
}
