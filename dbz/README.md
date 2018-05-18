> _Dans tous les exercices, vous n'avez pas le droit de modifier les classes des exercices précedents (hormis la classe Main)_

Dans le projet se trouve de quoi faire des combat, avec des `Fighter` et une `Arena`. Le but du sujet est de simuler les combat de DBZ. \
Voici par exemple le combat entre Goku et Yamsha !

```java
Fighter goku = new Character("Goku", 16, 4);
Fighter yamsha = new Character("Yamsha", 20, 3);

Arena.battle(goku, yamsha);
```

## Exercice 1 : Hero

Les combats sont un peu lassant. Rajoutons une interface `PowerAttack` pour les super attaques :

```java
public interface PowerAttack {

    /** return damage dealt */
    int superPowerAttack();
}
```	
Avec on peut ajouter nos attaques favorites ! 

- Ajoutez une classe `Hero` qui possède en plus des attaques normales, une super attaque. \
Un hero a 20% de chance de la réaliser une super attaque à la place d'une attaque normal. \
Attention : pas le droit d'utiliser d'héritage.

Avec cela, Goku a des chances de vaincre le vilain Picolo !

```java
PowerAttack kamehameha = () -> 30;
Fighter goku = new Hero("Goku", 50, 15, kamehameha);

Fighter picolo = new Character("Picolo", 70, 20);

Arena.battle(goku, picolo);
```
## Exercice 2 : Power

Malheureusement, Goku n'arrive pas à vaincre Picolo, ceci parce qu'il ne crie pas sa super attaque !  
Faites en sorte que goku crie son attaque juste avant de l'effectuer :

```java
PowerAttack kamehameha = PowerAttack.shout("KAMEHAMEHAAA !!!!", () -> 60);
Fighter goku = new Hero("Goku", 50, 15, kamehameha);
```

- Ajoutez la method `shout()`

## Exercice 3 : DBZ Heros

Avec son périple, Goku a grandi rencontré plusieurs alliés. 

- Rajoutez les personnages dans une classe `DBZ`

| Perso       | PV    | ATK   | SUPER ATK - DMG         |
|-------------|-------|-------|:-----------------------:|
| Goku        | 500   | 50    | KAMEHAMEHAAA !!!! - 200 |
| Gohan       | 200   | 30    | MASEEENNKO ! - 100      |
| Krilin      | 200   | 20    | KIEN-ZAN ! - 70         |
| Yamcha      | 150   | 20    | SO-KIDAN ! - 60         |
| Tenshinhan  | 300   | 40    | KI-KO-HOOO ! - 100      |

On pourra les recupérer comme cela :
```java
Fighter goku = DBZ.GOKU 
// ou bien 
Fighter goku = DBZ.getGoku()
```

## Exercice 4 : Tournoi des arts martiaux

C'est le tournoi des arts martiaux !

```java
Tournament tournament = new Tournament("Tournoi des arts martiaux");

Fighter winner = tournament
    .addParticipant(DBZ.GOKU)
    .addParticipant(DBZ.YAMSHA)
    .addParticipant(DBZ.TENSHINHAN)
    .addParticipant(DBZ.KRILIN)
    .addParticipant(new Character("Chiatzu", 1, 100))
    .addParticipant(new Character("Orc", 50, 20))
    .addParticipant(new Character("Sumo", 100, 5))
    .addParticipant(new Character("Shaman", 40, 15))
    .start();

System.out.println(winner + " wins the tournament !");
```

Un tournoi ne doit pas pouvoir être lancer s'il n'y a aucun participant (la méthode `start()` ne doit pas être visible).

- Ajoutez la classe `Tournament` (les combats sont tirés au sort et on suppose qu'il y a toujours un nombre de participant qui est une puissance de 2)


## Exercice 5 : KAIOKEN !

Ah ! les saiyen arrivent ! Raddits est vaincue mais Nappa est la ! Goku doit protégé Krilin et Gohan ! 
Pour ca il doit utilisé le `Kaioken` x2. Ce qui lui donne 50% de chance d'attaquer 2 fois d'affilés, en revanche, il subit 1.5 fois plus de dégats des attaques.

| Nappa  | 700   | 50     | Break Cannoooon !!! - 150 |
|--------|-------|--------|:-------------------------:|

```java
Arena.battle(new Kaioken(DBZ.GOKU, 2), DBZ.NAPPA);
```

- Ajoutez le `Kaioken` (attention à ne pas oublier le `toString()`)


## Exercice 6 : Combat contre Vegeta

C'est le combat final contre Vegeta !

| Vegeta  | 2000   | 90     | FINAAAAL FLAAAASHHHH !!! - 200 |
|---------|--------|--------|:------------------------------:|

Goku, Krilin et Gohan le combattent ensemble. 
```java
Fighter heros = Fighter.together(new Kaioken(DBZ.GOKU, 3), DBZ.KRILIN, DBZ.GOHAN)
Arena.battle(heros, DBZ.VEGETA);
```

- Faites en pour qu'ils puissent combattre ensemble. \
Un seul des 3 peut attaquer à la fois, et les dégats ne sont ingligés qu'à un seul. \
(attention à ne pas oublier le `toString()`)



## Exercice 7 : Tournoi de Cell

Nos heros s'unissent pour combattre Cell, mais comme c'est un tournois, ils decides de le combattre 1 à 1.

| Cell    | 2000   | 150    | Ultimate Blitz - 300         |
|---------|--------|--------|:----------------------------:|
| Trunks  | 350    | 50     | BUSTER ATTAAAAAACK !!! - 200 |
| Gohan SSJ2  | 650    | 100     | Kamehameha père-fils ! - 1000 |

L'ordre des combattants est le suivant : Trunks, Krilin, Goku, Gohan

```java
Fighter heros = DBZ.TRUNKS.then(DBZ.KRILIN).then(DBZ.GOKU).then(DBZ.GOHAN_SSJ2)
Arena.battle(heros, DBZ.CELL);
```

## Exercice 8 : Changement de comportement !

Les combats sont trop monotone. Rajoutons un comportement durant les combats.

```java
interface Behaviour {
    void attack(int health, Runnable normalAttack, Consumer<Integer> dealDamage, Consumer<Integer> takeDamage);
}
```

- `health` = vie restante du héro
- `normalAttack` = la fonction fait une attaque normal à l'enemie
- `dealDamage` = la fonction qui inglige des dégats à l'enemie
- `takeDamage` = la fonction qui inflige des dégats au héro

Voici par exemple le comportement de Chiatzu :

```java
PowerAttack suicide = PowerAttack.shout("Farewell, Mr. Tien !", () -> 500);

Behaviour kamikaze = (health, normalAttack, dealDamage, takeDamage) -> {
    if (health < 50){
        dealDamage.accept(suicide.superPowerAttack());
        takeDamage.accept(health); // prend ses pv restants en dégat
    } else {
        normalAttack();
    }
}

Hero("Chiatzu", 150, 5, kamikaze);
// Hero ne prend plus superAttack mais behaviour à la place.
```

- Changez la methode `attack()` de `Hero` pour implémenter ce comportement. \
Pour gerer les `PowerAttack`, il serait judicieux de les ajouter dans une classe `Techniques` (de la même façon que `DBZ` pour les héros)

## Exercice 9 : Freezer

Freezer, le plus grand méchant !!! Il est la pour combattre nos héros !

- Implementer Freezer et avec ses différentes formes ([Design Pattern State](https://refactoring.guru/design-patterns/state))

```java
Hero("Freezer", 2000, 50, new FreezerBehaviour());
```

Ici, `FreezerBehaviour` contient toutes les formes de Freezer

| Freezer    | Changement quand |  ATK    | SUPER ATK - DMG           |
|------------|------------------|---------|:-------------------------:|
| BaseForm   | hp < 1600        | 50      | FINGER BEAM ! - 100 |
| SecondForm | hp < 1200        | 75      | DEATH STORM ! - 150 |
| ThridForm  | hp < 800         | 100     | CRAZY FINGER BEAM !!! - 200 |
| FinalForm  |                  | 200     | Dark Death Ball - 400 |

```java
Fighter heros = Fighter.together(DBZ.GOKU, DBZ.VEGETA, DBZ.KRILIN, DBZ.GOHAN)
Arena.battle(heros, DBZ.FREEZER);
```
