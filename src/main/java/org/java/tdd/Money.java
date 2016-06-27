package org.java.tdd;

/**
 * Created by mgupta on 6/27/16.
 */
public class Money implements Expression {

    protected int    amount;
    protected String currency;

    public Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    static Money dollar(int amount) {
        return new Money(amount, "USD");
    }

    static Money franc(int amount) {
        return new Money(amount, "CHF");
    }

    public Money times(int multiplier) {
        return new Money(amount * multiplier, currency);
    }

    public boolean equals(Object object) {
        Money money = (Money) object;
        return money.amount == amount && currency().equals(money.currency());
    }

    public String currency() {
        return currency;
    }

    public String toString() {
        return amount + " " + currency;
    }

    @Override
    public Expression plus(Money added) {
        return new Money(amount + added.amount, currency);
    }
}