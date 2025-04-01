package rpg.settings;

import rpg.core.Character;

public class GameSettings {
    private static GameSettings instance;
    private final int maxStatPoints;

    private GameSettings() {
        // Valeur maximale pour la somme des stats (force + agilité + intelligence)
        this.maxStatPoints = 100;
    }

    public static synchronized GameSettings getInstance() {
        if (instance == null) {
            instance = new GameSettings();
        }
        return instance;
    }

    public int getMaxStatPoints() {
        return maxStatPoints;
    }

    public boolean isValid(Character character) {
        return isValid(character.getStrength(), character.getAgility(), character.getIntelligence());
    }

    public boolean isValid(int strength, int agility, int intelligence) {
        int totalStats = strength + agility + intelligence;
        return totalStats <= maxStatPoints;
    }
}