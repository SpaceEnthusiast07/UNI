package Past_Exam_Practice.May_2020_Exam;

/**
 * Solution to the Coffee Vending Machine question.
 */
public class CoffeeVendingMachineSolution implements CoffeeVendingMachine {
    short transactionAmount;

    /**
     * Initialises the coffee vending machine's transaction tracker variable to 0p.
     */
    public CoffeeVendingMachineSolution() {
        transactionAmount = 0;

        // Ensures the transaction amount has been initialised to 0
        assert transactionAmount == 0 : "\'transactionAmount\' hasn\'t been initialised correctly!";
    }

    /**
     * Allows the user to insert a coin into the vending machine and updates the transaction tracker variable.
     * @param coin This is the Enum constant representing the coin inserted.
     * @throws CoinRejectedException Thrown if the inserted coin is not a 50p or £1 coin, or by
     * insterting this coin the transaction amount exceeds £1.50.
     */
    @Override
    public void addCoin(CoinValue coin) throws CoinRejectedException {
        // Throw an exception if the coin entered is not a 50p or £1 coin
        if (coin != CoinValue.FIFTY_PENCE && coin != CoinValue.ONE_POUND) {
            throw new CoinRejectedException("Invalid Coin");
        }

        // Convert the enum constant to a short
        short coinAmount;
        if (coin == CoinValue.FIFTY_PENCE) {
            coinAmount = 50;
        }
        else {
            coinAmount = 100;
        }

        // Throw an exception if adding this coin exceeds £1.50
        if ((transactionAmount + coinAmount) > 150) {
            throw new CoinRejectedException("Cannot exceed £1.50");
        }

        // Add the coin value to the transaction
        transactionAmount += coinAmount;

        // Ensure the transaction amount is greater than £0
        assert transactionAmount > 0 : "\'transactionAmount\' shouldn\'t be negative or zero!";

        // Ensure the transaction amount is less than or equal to £1.50
        assert transactionAmount <= 150 : "\'transactionAmount\' shouldn\'t be greater than £1.50!";
    }

    /**
     * Allows the user to cancel the process mid transaction and receive their money back.
     * @return The amount, in pence, the user should receive back.
     */
    @Override
    public short pressClearButton() {
        // Store the current transaction amount
        short currentAmount = transactionAmount;

        // Reset the transaction
        transactionAmount = 0;

        // Ensure transaction amount has been reset
        assert transactionAmount == 0 : "\'transactionAmount\' has not been reset!";

        // Return the transaction amount before the clear button was pressed
        return currentAmount;
    }

    /**
     * Dispenses the newly bought coffee.
     * @return The new Coffee.
     * @throws InsufficientMoneyException When the amount entered is less than £1.50.
     */
    @Override
    public Coffee dispenseCoffee() throws InsufficientMoneyException {
        // The user must enter £1.50 for coffee
        if (transactionAmount != 150) {
            throw new InsufficientMoneyException("Coffee costs £1.50");
        }

        // Ensure the transaction amount is equal to £1.50
        assert transactionAmount == 150 : "\'transactionAmount\' doesn\'t equal £1.50!";

        // Prepare the coffee
        Coffee newCoffee = new Coffee("Latte");

        // Reset the transaction amount
        transactionAmount = 0;

        // Ensure transaction amount has been reset
        assert transactionAmount == 0 : "\'transactionAmount\' has not been reset!";

        // Dispense the coffee
        return newCoffee;
    }
}
