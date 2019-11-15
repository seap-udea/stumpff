# Stumpff series
## Efficient computation of the stumpff series

Computing the value of the [Stumpff
series](https://en.wikipedia.org/wiki/Stumpff_function) is important
in celestial mechanics.  Altough most series might be expressed in
terms of trignometric functions, several singular points way too hard
to create a general function to compute them.

In this package we provide a minimalistic python version of the
stumpff series.

The function is able to compute the Stumpff series in the same time as
a regular trigonometric function, which is really important for
efficient computations in celestial mechanics.

To test the function just run:

```
  make
```

Read the `test.py` source code to see how to use the routines in the
main file `stumpff.py`.

If you find a more shorter and efficient way to compute the Stumpff
series please write to
[jorge.zuluaga@udea.edu.co](mailto:jorge.zuluaga@udea.edu.co).

If you use it please mention this repo.

Happy Stumpff!

Acknowledgements
----------------

Thanks to [Juan Andres Pasos Rua](mailto:japasosr@unal.edu.co) for
suggesting me to use functools to "cache" the function and speed-up it
by a factor of ~20.