import java.util.HashMap;

public class HashTest {
	public static void main(String[] args){
		if(args.length != 2) return;

		HashMap<Character, Integer> countA = new HashMap<Character, Integer>();
		HashMap<Character, Integer> countB = new HashMap<Character, Integer>();

		String a = args[0];
		String b = args[1];

		for(int i=0; i<a.length(); i++){
			Character c = a.charAt(i);
			if(countA.containsKey(c))
				countA.put(c, countA.get(c)+1);
			else
				countA.put(c,1);
		}

		for(int i=0; i<b.length(); i++){
			Character c = b.charAt(i);
			if(countB.containsKey(c))
				countB.put(c, countB.get(c)+1);
			else
				countB.put(c,1);
		}

		for(Character c : countA.keySet())
			System.out.println("A: "+c+"'s "+countA.get(c));

		for(Character c : countB.keySet())
			System.out.println("B: "+c+"'s "+countB.get(c));
	}
}
