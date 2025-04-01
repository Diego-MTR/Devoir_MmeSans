package rpg.core;

public class Character {
    private String name;
    private int strength;
    private int agility;
    private int intelligence;

    public Character(String name, int strength, int agility, int intelligence) {
        this.name = name;
        this.strength = strength;
        this.agility = agility;
        this.intelligence = intelligence;
    }

    public String getName() {
        return name;
    }

    public int getStrength() {
        return strength;
    }

    public int getAgility() {
        return agility;
    }

    public int getIntelligence() {
        return intelligence;
    }

    public int getPowerLevel() {
        // Calcul simple du niveau de puissance basé sur les caractéristiques
        return strength * 2 + agility * 1 + intelligence * 3;
    }

    public String getDescription() {
        return "Personnage " + name + " [Force: " + strength +
                ", Agilité: " + agility +
                ", Intelligence: " + intelligence +
                ", Puissance: " + getPowerLevel() + "]";
    }
}