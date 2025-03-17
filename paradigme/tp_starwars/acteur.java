import java.util.ArrayList;
import java.util.List;

class acteur {
    private String nom;
    private String prenom;
    private List<Personnage> personnages;

    public acteur(String nom, String prenom) {
        this.nom = nom;
        this.prenom = prenom;
        this.personnages = new ArrayList<>();
    }

    public void ajouterPersonnage(Personnage personnage) {
        personnages.add(personnage);
    }

    public int nbPersonnages() {
        return personnages.size();
    }

    public String getNom() {
        return nom;
    }

    @Override
    public String toString() {
        return "Acteur{" + "nom='" + nom + '\'' + ", prenom='" + prenom + '\'' + '}';
    }
}