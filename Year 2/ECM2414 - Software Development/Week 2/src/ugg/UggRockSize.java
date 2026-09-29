package src.ugg;

enum UggRockSize {
    BIGUN((short) 5), QUITE_BIGUN((short) 3), NOT_SO_BIGUN((short) 1);

    private short multiplierValue;

    private UggRockSize(short multiplierValue) {
        this.multiplierValue = multiplierValue;
    }

    // Getter
    public short getMultiplierValue() {
        return this.multiplierValue;
    }
}