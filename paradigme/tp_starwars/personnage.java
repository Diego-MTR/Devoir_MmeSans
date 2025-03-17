class Personnage {
    private String nom;
    private String prenom;

    public Personnage(String nom, String prenom) {
        this.nom = nom;
        this.prenom = prenom;
    }

    @Override
    public String toString() {
        return "Personnage{" + "nom='" + nom + '\'' + ", prenom='" + prenom + '\'' + '}';
    }
}
