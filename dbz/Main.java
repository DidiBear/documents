package dbz;

public class Main {

	public static void main(String[] args) {
		battle1();
	}

	private static void battle1() {
		Fighter goku = new Character("Goku", 16, 4);
		Fighter yamsha = new Character("Yamsha", 20, 3);
		
		Arena.battle(goku, yamsha);
	}

}