package rpg.decorator;

import rpg.core.Character;

public class FireResistance extends CharacterDecorator {
    public FireResistance(Character decoratedCharacter) {
        super(decoratedCharacter);
    }

    @Override
    public int getPowerLevel() {
        // La résistance au feu augmente la puissance
        return super.getPowerLevel() + 10;
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " + Résistance au feu";
    }
}