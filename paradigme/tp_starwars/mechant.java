class mechant extends Personnage {
    private boolean coteObscur;

    public mechant(String nom, String prenom, boolean coteObscur) {
        super(nom, prenom);
        this.coteObscur = coteObscur;
    }

    @Override
    public String toString() {
        return super.toString() + ", Côté obscur=" + coteObscur;
    }
}