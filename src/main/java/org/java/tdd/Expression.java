package org.java.tdd;

/**
 * Created by mgupta on 7/22/16.
 */
public interface Expression {
    Money reduce(Bank bank, String to);

    Expression plus(Expression addend);

    Expression times(int i);

}
