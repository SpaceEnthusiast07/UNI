package src.ugg;

public class UggRock {
    private UggRockSize rockSize;
    private UggRockType rockType;

    public UggRock(UggRockSize rockSize, UggRockType rockType) {
        this.rockSize = rockSize;
        this.rockType = rockType;
    }

    // Getters
    public UggRockSize getUggRockSize() {
        return this.rockSize;
    }
    public UggRockType getUggRockType() {
        return this.rockType;
    }

    // Returns the value of the rock
    public short rockValue() {
        return (short)(this.rockSize.getMultiplierValue() * this.rockType.getMultiplierValue());
    }

    // Used to output this rock's state in a human readable format
    @Override
    public String toString() {
        return String.format("%s, %s", rockSize.toString(), rockType.toString());
    }
}