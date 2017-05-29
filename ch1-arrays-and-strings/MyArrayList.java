public class MyArrayList<T> {
	private final int INITIAL_SIZE = 8;
	private Object[] array;
	private int length = 0;

	@SuppressWarnings("unchecked")
	public MyArrayList(){
		array = (T[]) new Object[INITIAL_SIZE];
	}

	@SuppressWarnings("unchecked")
	public T get(int index){
		if(index > length - 1 || index < 0){
			return null;
		} else{
			return (T) array[index];
		}
	}

	@SuppressWarnings("unchecked")
	public void add(T item){
		array[length] = item;
		length++;

		if(length == array.length){
			T new_array[] = (T[]) new Object[length*2];
			for(int i=0; i<length; i++){
				new_array[i] = (T) array[i];
			}
			array = new_array;
		}


	}

	public void add(int index, T element){
		if(index < 0 || index > length - 1){
			throw new IndexOutOfBoundsException("Invali array index "+index);
		} else{
			array[index] = element;
		}
	}

	public int size(){
		return length;
	}

	public static void main(String args[]){
		MyArrayList<Integer> test = new MyArrayList<Integer>();
		int size = 166;
		for(int i=0; i<size; i++){
			test.add(i);
		}

		for(int i=0; i<size; i++){
			System.out.println(test.get(i));
		}
	}
}
