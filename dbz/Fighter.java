package dbz;

public interface Fighter {
	void attack(Fighter enemy);
	void takeDamage(int damage);
	boolean isAlive();
}
