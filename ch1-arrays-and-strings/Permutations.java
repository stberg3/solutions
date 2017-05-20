// permutations.java
// problem 1.2
// Given two strings, check if they are permutations of each other

import java.util.HashMap;
import java.util.HashSet;

public class Permutations {
	public static boolean isPermutation(String a, String b){
		HashMap<Character, Integer> A = new HashMap<Character, Integer>();
		HashMap<Character, Integer> B = new HashMap<Character, Integer>();
		HashSet<Character> setA = new HashSet<Character>();
		HashSet<Character> setB = new HashSet<Character>();


		if(a.length() != b.length()) return false;

		for(int i=0; i<a.length(); i++){
			Character c = new Character(a.charAt(i));
			setA.add(c);
			if(A.containsKey(c)){
				Integer val = A.get(c);
				A.put(c, val + 1);
			} else{
				A.put(a.charAt(i), 1);
			}
		}

		for(int i=0; i<b.length(); i++){
			Character c = b.charAt(i);
			setB.add(c);
			if(B.containsKey(c)){
				Integer val = B.get(c);
				B.put(c, val + 1);
			} else{
				B.put(b.charAt(i), 1);
			}
		}

		if(!setA.equals(setB)) return false;

		for(Character c : setA){
			if(A.get(c) != B.get(c)){
				return false;
			}
		}

		return true;
	}

	public static void main(String[] args){
		if(args.length == 2){
			// System.out.println("args[0] ="+args[0]+" \n"+
			// 									 "args[1] ="+args[1]+" \n");
			System.out.println(isPermutation(args[0], args[1]));
		}
	}
}
