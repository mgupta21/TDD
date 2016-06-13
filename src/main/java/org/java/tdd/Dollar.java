package org.java.tdd;

/**
 * Created by mgupta on 6/13/16.
 */
public class Dollar {

    private int amount;

    public Dollar(int amount) {
        this.amount = amount;
    }

    public Dollar times(int multiplier) {
        return new Dollar(amount * multiplier);
    }

    public boolean equals(Object object) {
        Dollar dollar = (Dollar) object;
        return dollar.amount == amount;
    }

}
