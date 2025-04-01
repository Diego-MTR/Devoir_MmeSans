package rpg.decorator;

import rpg.core.Character;

public class Telepathy extends CharacterDecorator {
    public Telepathy(Character decoratedCharacter) {
        super(decoratedCharacter);
    }

    @Override
    public int getPowerLevel() {
        // La télépathie augmente la puissance
        return super.getPowerLevel() + 20;
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " + Télépathie";
    }
}