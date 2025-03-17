import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class film {
    private String titre;
    private int anneeSortie;
    private int numeroEpisode;
    private double cout;
    private double recette;
    private List<acteur> acteurs;
    private List<Personnage> personnages;

    public film(String titre, int anneeSortie, int numeroEpisode, double cout, double recette) {
        this.titre = titre;
        this.anneeSortie = anneeSortie;
        this.numeroEpisode = numeroEpisode;
        this.cout = cout;
        this.recette = recette;
        this.acteurs = new ArrayList<>();
        this.personnages = new ArrayList<>();
    }

    public void ajouterActeur(acteur acteur) {
        acteurs.add(acteur);
    }

    public void ajouterPersonnage(Personnage personnage) {
        personnages.add(personnage);
    }

    public int nbActeurs() {
        return acteurs.size();
    }

    public int nbPersonnages() {
        return personnages.size();
    }

    public double calculBenefice() {
        return recette - cout;
    }

    public boolean isBeneficiaire() {
        return calculBenefice() > 0;
    }

    public boolean isBefore(int annee) {
        return this.anneeSortie < annee;
    }

    public void trierActeurs() {
        acteurs.sort(Comparator.comparing(acteur::getNom));
    }

    @Override
    public String toString() {
        return "Film{" +
                "titre='" + titre + '\'' +
                ", anneeSortie=" + anneeSortie +
                ", numeroEpisode=" + numeroEpisode +
                ", cout=" + cout +
                ", recette=" + recette +
                ", benefice=" + calculBenefice() +
                '}';
    }

    public String getTitre() {
        return titre;
    }
}