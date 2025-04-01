package rpg.decorator;

import rpg.core.Character;

public class Invisibility extends CharacterDecorator {
    public Invisibility(Character decoratedCharacter) {
        super(decoratedCharacter);
    }

    @Override
    public int getPowerLevel() {
        // L'invisibilité augmente la puissance
        return super.getPowerLevel() + 15;
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " + Invisibilité";
    }
}