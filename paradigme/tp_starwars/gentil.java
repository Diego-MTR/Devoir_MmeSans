class Gentil extends Personnage {
    private boolean force;

    public Gentil(String nom, String prenom, boolean force) {
        super(nom, prenom);
        this.force = force;
    }

    @Override
    public String toString() {
        return super.toString() + ", Force=" + force;
    }
}