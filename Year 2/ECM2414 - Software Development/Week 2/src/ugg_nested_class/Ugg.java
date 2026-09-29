package src.ugg_nested_class;

// Used within drawRock()
import java.util.Random;

public class Ugg {
    // Nested UggRockSize ENUM
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

    // Nested UggRockType ENUM
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

    // Static nested UggRock class
    public static class UggRock {
        private UggRockSize rockSize;
        private UggRockType rockType;

        public UggRock(UggRockSize rockSize, UggRockType rockType) {
            this.rockSize = rockSize;
            this.rockType = rockType;
        }

        /**
         * Gives the client access to this rock's size.
         * @return This rock's size as a UggRockSize ENUM constant.
         */
        public UggRockSize getUggRockSize() {
            return this.rockSize;
        }

        /**
         * Gives the client access to this rock's type.
         * @return This rock's type as a UggRockType ENUM constant.
         */
        public UggRockType getUggRockType() {
            return this.rockType;
        }

        /**
         * Determines this rock value by multiplying the size and type multipliers.
         * @return This rock's value.
         */
        public short rockValue() {
            return (short)(this.rockSize.getMultiplierValue() * this.rockType.getMultiplierValue());
        }

        /**
         * Formats this rock's state in a human readable string.
         * @return This rock's state as a human readable String object.
         */
        @Override
        public String toString() {
            return String.format("%s, %s", rockSize.toString(), rockType.toString());
        }
    }

    /**
     * Generates a rock at random.
     * Size: Quite-bigun is twice as likely as Bigun, and No-so-bigun is three times as likely as Quite-bigun.
     * So:        No-so-bigun        Quite-bigun     Bigun
     *      |---------6/9---------|------2/9------|---1/9---|
     * Type: each type is equally as likely.
     * @return The randomly generated rock.
     */
    public UggRock drawRock() {
        // Create a new Random object
        Random random = new Random();

        // Generate the rock's random size from Bigun, Quite-bigun, and Not-so-bigun
        int randomSizeValue = (int) (random.nextDouble()*100);
        UggRockSize rockSize;
        // Decide which type this random decimal translates to
        if (randomSizeValue < 67) rockSize = UggRockSize.NOT_SO_BIGUN;
        else if (randomSizeValue < 89) rockSize = UggRockSize.QUITE_BIGUN;
        else rockSize = UggRockSize.BIGUN;

        // Generate the rock's random type from Speckily, Ouchy-black, Floaty, and Hot-hot-hot
        int randomTypeValue = (int) (random.nextDouble()*100);
        UggRockType rockType;
        // Decide which type this random decimal translates to
        if (randomTypeValue < 25) rockType = UggRockType.SPECKILY;
        else if (randomTypeValue < 50) rockType = UggRockType.OUCHY_BLACK;
        else if (randomTypeValue < 75) rockType = UggRockType.FLOATY;
        else rockType = UggRockType.HOT_HOT_HOT;

        // Create the new random rock
        return new UggRock(rockSize, rockType);
    }

    /**
     * Testing that my logic works.
     * @param args
     */
    public static void main(String[] args) {
        // Create a new Ugg game object
        Ugg ugg = new Ugg();

        // Output program title
        System.out.println("-- Ugg Game --\n10 randomly generated rocks:");

        // Generate 10 random rocks and output their state
        UggRock rock;
        for (int i = 0; i < 10; i++) {
            rock = ugg.drawRock();
            System.out.printf("Rock %d: size=%s type=%s\n", i, rock.getUggRockSize().toString(), rock.getUggRockType().toString());
        }
    }
}
