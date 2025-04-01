package rpg.builder;

import rpg.core.Character;

public class CharacterBuilder {
    private String name;
    private int strength;
    private int agility;
    private int intelligence;

    public CharacterBuilder() {
        // Valeurs par défaut
        this.name = "Sans nom";
        this.strength = 10;
        this.agility = 10;
        this.intelligence = 10;
    }

    public CharacterBuilder setName(String name) {
        this.name = name;
        return this;
    }

    public CharacterBuilder setStrength(int strength) {
        this.strength = strength;
        return this;
    }

    public CharacterBuilder setAgility(int agility) {
        this.agility = agility;
        return this;
    }

    public CharacterBuilder setIntelligence(int intelligence) {
        this.intelligence = intelligence;
        return this;
    }

    public Character build() {
        // Vérification de la validité du personnage
        if (!rpg.settings.GameSettings.getInstance().isValid(this.strength, this.agility, this.intelligence)) {
            throw new IllegalStateException("Le personnage ne respecte pas les règles du jeu.");
        }
        return new Character(name, strength, agility, intelligence);
    }
}