package rpg.dao;

import rpg.core.Character;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CharacterDAO implements DAO<Character> {
    // Utilisation d'une HashMap pour stocker les personnages (simulation de persistance)
    private Map<String, Character> characters = new HashMap<>();

    @Override
    public void save(Character character) {
        characters.put(character.getName(), character);
    }

    @Override
    public Character findByName(String name) {
        return characters.get(name);
    }

    @Override
    public List<Character> findAll() {
        return new ArrayList<>(characters.values());
    }
}