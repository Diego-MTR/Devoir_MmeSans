import java.util.Scanner;
import java.util.Map;
import java.util.List;

public class main {
    public static void main(String[] args) {
        film film1 = new film("Un nouvel espoir", 1977, 4, 11000000, 775000000);
        film film2 = creerFilmInteractif();

        acteur markHamill = new acteur("Hamill", "Mark");
        Personnage luke = new Gentil("Skywalker", "Luke", true);
        markHamill.ajouterPersonnage(luke);
        film1.ajouterActeur(markHamill);
        film1.ajouterPersonnage(luke);

        acteur harrisonFord = new acteur("Ford", "Harrison");
        Personnage hanSolo = new Personnage("Solo", "Han");
        Personnage indianaJones = new Personnage("Jones", "Indiana");
        harrisonFord.ajouterPersonnage(hanSolo);
        harrisonFord.ajouterPersonnage(indianaJones);
        film1.ajouterActeur(harrisonFord);
        film1.ajouterPersonnage(hanSolo);
        film1.ajouterPersonnage(indianaJones);

        System.out.println(film1);
        System.out.println(film2);
    }

    public static film creerFilmInteractif() {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        System.out.print("Titre du film : ");
        String titre = scanner.nextLine();
        System.out.print("Année de sortie : ");
        int anneeSortie = scanner.nextInt();
        System.out.print("Numéro de l’épisode : ");
        int numeroEpisode = scanner.nextInt();
        System.out.print("Coût du film : ");
        double cout = scanner.nextDouble();
        System.out.print("Recette du film : ");
        double recette = scanner.nextDouble();
        return new film(titre, anneeSortie, numeroEpisode, cout, recette);
    }

    // 13
    public static void makeBackUp(Map<Integer, film> films) {
        for (Map.Entry<Integer, film> entry : films.entrySet()) {
            int annee = entry.getKey();
            film film = entry.getValue();
            System.out.println(annee + " - " + film.getTitre() + " - " + film.calculBenefice());
        }
    }

    // 5
    public static void afficherPersonnages(List<Personnage> personnages) {
        for (Personnage personnage : personnages) {
            System.out.println(personnage);
        }
    }
}
