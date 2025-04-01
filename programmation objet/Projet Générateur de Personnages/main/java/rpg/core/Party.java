package rpg.core;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Party {
    private List<Character> members = new ArrayList<>();
    private String partyName;

    public Party(String partyName) {
        this.partyName = partyName;
    }

    public String getPartyName() {
        return partyName;
    }

    public void addCharacter(Character character) {
        members.add(character);
    }

    public void removeCharacter(Character character) {
        members.remove(character);
    }

    public void removeCharacterByName(String name) {
        members.removeIf(character -> character.getName().equals(name));
    }

    public int getTotalPowerLevel() {
        int totalPower = 0;
        for (Character character : members) {
            totalPower += character.getPowerLevel();
        }
        return totalPower;
    }

    public List<Character> getMembers() {
        return members;
    }

    // Méthode pour trier les personnages par puissance
    public void sortByPowerLevel() {
        Collections.sort(members, Comparator.comparing(Character::getPowerLevel).reversed());
    }

    // Méthode pour trier les personnages par nom
    public void sortByName() {
        Collections.sort(members, Comparator.comparing(Character::getName));
    }

    // Simulation simple d'un combat entre deux personnages
    public static String simulateCombat(Character character1, Character character2) {
        StringBuilder result = new StringBuilder();
        result.append("Combat entre ").append(character1.getName())
                .append(" (").append(character1.getPowerLevel()).append(" points de puissance) et ")
                .append(character2.getName())
                .append(" (").append(character2.getPowerLevel()).append(" points de puissance)\n");

        if (character1.getPowerLevel() > character2.getPowerLevel()) {
            result.append(character1.getName()).append(" gagne le combat!");
        } else if (character2.getPowerLevel() > character1.getPowerLevel()) {
            result.append(character2.getName()).append(" gagne le combat!");
        } else {
            result.append("Match nul! Les deux personnages sont de force égale.");
        }

        return result.toString();
    }
}