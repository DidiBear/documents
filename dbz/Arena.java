package dbz;

public final class Arena {
	private Arena() {}

	/**
	 * Start a battle !
	 */
	public static void battle(Fighter fighter1, Fighter fighter2) {
		
		// Choose randomly the first one to attack
		if (Math.random() > 0.5) {
			Fighter tmp = fighter1;
			fighter1 = fighter2;
			fighter2 = tmp;
		}
	
		System.out.println("FIGHT : " + fighter1 + " VS " + fighter2);
		
		Fighter winner = fight(fighter1, fighter2);
		
		System.out.println(winner + " wins !" + System.lineSeparator());
	}

	/** 
	 * They are fighting ! return the winner 
	 */
	private static Fighter fight(Fighter fighter1, Fighter fighter2) {
		do {
			
			fighter1.attack(fighter2);
			fighter2.attack(fighter1);
			
		} while (fighter1.isAlive() && fighter2.isAlive());
		
		// Return the winner
		
		if (fighter1.isAlive()) {
			return fighter1;
		} 
		return fighter2;
	}
}
