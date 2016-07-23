package org.java.tdd;

import java.util.Hashtable;

/**
 * Created by mgupta on 7/22/16.
 */
public class Bank {

    private Hashtable rates = new Hashtable();

    public Money reduce(Expression expression, String to) {
        return expression.reduce(this, to);
    }

    public void addRate(String from, String to, int rate) {
        rates.put(new Pair(from, to), new Integer(rate));
    }

    public int rate(String from, String to) {
        if (from.equals(to)) return 1;
        return (int) rates.get(new Pair(from, to));
    }
}
