package dbz;

public class Character implements Fighter {

	private final String name;
	private int health;
	private final int attack;
	
	public Character(String name, int health, int attack) {
		this.name = name;
		this.health = health;
		this.attack = attack;
	}

	// Fighting methods 
	
	@Override
	public void attack(Fighter enemy) {
		dealDamage(enemy, attack);
	}
	
	void dealDamage(Fighter enemy, int damage) {
		System.out.println(name + " deals " + damage + " damages to " + enemy + " !");
		enemy.takeDamage(damage);
	}

	@Override
	public void takeDamage(int damage) {
		health -= damage;		
	}

	public boolean isAlive() {
		return health > 0;
	}

	// Getters
	
	public String getName() {
		return name;
	}
	
	public int getHealth() {
		return health;
	}
	
	public int getAttack() {
		return attack;
	}
	
	@Override
	public String toString() {
		return name;
	}
}
