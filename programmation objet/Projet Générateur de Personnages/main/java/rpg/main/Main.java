import rpg.core.Character;
import rpg.builder.CharacterBuilder;
import rpg.decorator.FireResistance;
import rpg.decorator.Invisibility;
import rpg.decorator.Telepathy;
import rpg.core.Party;

public class Main {
    public static void main(String[] args) {
        // Exemple d'utilisation des différentes fonctionnalités
        Character thief = createCharacter("Voleur", 20, 40, 30);
        Character warrior = createCharacter("Guerrier", 40, 30, 20);
        Character mage = createCharacter("Mage", 10, 20, 70);

        Character enhancedThief = addAbilities(thief, new FireResistance(thief), new Invisibility(thief));
        Character enhancedMage = addAbilities(mage, new Telepathy(mage));

        Party party = createParty("Aventuriers", enhancedThief, warrior, enhancedMage);
        displayPartyDetails(party);

        System.out.println(Party.simulateCombat(enhancedThief, warrior));
    }

    private static Character createCharacter(String name, int strength, int agility, int intelligence) {
        return new CharacterBuilder()
                .setName(name)
                .setStrength(strength)
                .setAgility(agility)
                .setIntelligence(intelligence)
                .build();
    }

    private static Character addAbilities(Character baseCharacter, Character... abilities) {
        Character enhancedCharacter = baseCharacter;
        for (Character ability : abilities) {
            enhancedCharacter = ability;
        }
        return enhancedCharacter;
    }

    private static Party createParty(String name, Character... members) {
        Party party = new Party(name);
        for (Character member : members) {
            party.addCharacter(member);
        }
        return party;
    }

    private static void displayPartyDetails(Party party) {
        System.out.println("Équipe: " + party.getPartyName());
        for (Character member : party.getMembers()) {
            System.out.println(member.getDescription());
        }
        System.out.println("Puissance totale de l'équipe: " + party.getTotalPowerLevel());
    }
}