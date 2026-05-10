package Past_Exam_Practice.May_2020_Exam;

public interface CoffeeVendingMachine { 
    void addCoin(CoinValue coin) throws CoinRejectedException;
    short pressClearButton();
    Coffee dispenseCoffee() throws InsufficientMoneyException;
}