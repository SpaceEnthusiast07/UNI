package src.ugg;

enum UggRockType {
    SPECKILY((short) 7), OUCHY_BLACK((short) 20), FLOATY((short) 2), HOT_HOT_HOT((short) 15);
    
    private short multiplierValue;

    private UggRockType(short multiplierValue) {
        this.multiplierValue = multiplierValue;
    }

    // Getter
    public short getMultiplierValue() {
        return this.multiplierValue;
    }
}