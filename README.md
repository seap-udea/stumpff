# Stumpff series
## Efficient computation of the stumpff series

Computing the value of the [Stumpff
series](https://en.wikipedia.org/wiki/Stumpff_function) is important
in celestial mechanics (see for instance [Wisdom and Hernandez,
2015](http://web.mit.edu/wisdom/www/wisdom-hernandez.pdf).)

Altough most of those series might be expressed in terms of
trignometric or hypebolic functions, several singular points make too
hard to create a general routine to compute these series.

In this small package we provide a minimalistic [python routine of the
Stumpff
series](https://github.com/seap-udea/stumpff/blob/master/stumpff.py).
The routine might be easily implemented in any common language.

The function is able to compute the precise value of the any Stumpff
series and for values of the independent variable across four orders
of magnitude, in the same time as a regular trigonometric function.

This improvement is really important for efficient computations in
celestial mechanics.

To test the function just run:

```
  make
```

If you find a shorter and more efficient way to compute the Stumpff
series please write to me
[jorge.zuluaga@udea.edu.co](mailto:jorge.zuluaga@udea.edu.co) or tweet
it mentioning [@zuluagageorge](https://twitter.com/zuluagageorge).

If you find this routine useful, please mention this repo in your
source code.

Happy Stumpff!

Acknowledgements
----------------

Thanks to [Juan Andres Pasos Rua](mailto:japasosr@unal.edu.co) for
suggesting me to use functools to "cache" the function and speed-up it
by a factor of ~20.