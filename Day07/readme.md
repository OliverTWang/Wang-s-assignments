# Numerical Methods with SciPy

Chris Seymour

June 18, 2019

---

# Review

1. Trapezoid rule
2. Simpson's rule
3. Newton's Method
4. Secant Method

---

# Main Topics in Computational Methods

1. Integration
1. Linear Algebra
1. Root Finding
1. Differential Equations

---
## helpful `matplotlib` features
subplots `plt.subplots()`
```python
f, ax = plt.subplots() # create a single subplot

fig, axs = plt.subplots(2, 1, sharex=True) #horizontal stack of two
fig, axs = plt.subplots(1, 2, sharey=True) #verticle pair of two
axs[1].plot( xs, ys ) #access the plots in axs like a 1-D list

fig, axs = plt.subplots( cols, rows, sharex=True, sharey=True) # "cols" by "rows" grid of subplots
axs[0, 1].plot( xs, ys ) #access the plots in axs like a 2-D list

axs.shape  # can check the shape to make sure...
```
plot a second y-axis on the right side of the plot with `.twinx()`
```pyhton
f, ax = plt.subplots() #create a figure "f", and a subplot "ax"
ax.plot( xs, ys )
ax2 = ax.twinx() #create a second y-axis with the same x-units
ax2.plot( xs, ys2 )
```
Matplotlib useful "[Favorite Recipies](https://matplotlib.org/1.3.1/users/recipes.html)"

---
## line formatting

format string: optiona, third argument of `plt.plot()`
```python
plt.plot(x, y, 'go--', linewidth=2, markersize=12)
plt.plot(x, y, color='green', marker='o', linestyle='dashed',
...      linewidth=2, markersize=12)
```

legend
```python
plt.plot( xs, ys0, label='line 0' )
plt.plot( xs, ys1, label='line {}'.format(1) )
plt.plot( xs, ys2, label='line {}'.format( $\\beta$ ) )
plt.plot( xs, ys3, label='line {}'.format(1+2) )
plt.legend()
```
error bars
```python
plt.errorbar( xs, ys, yerr ) # yerr can be a single value, or a list of the same length as 'xs' and 'ys'
```
`matplotlib.plyplot.plot` [Documentation](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.plot.html)

---

## `scipy`

what we did last class...
- Worth it to program things yourself to understand them.
 
`scipy` has *most* things implemented already

You will often import a submodule via `from scipy import <something_else>`

---
## integration

- Integration methods are in `scipy.integrate`:
  - [Documentation](http://docs.scipy.org/doc/scipy/reference/integrate.html)

---
### quad

```python
from scipy import integrate

# func is the function to integrate, a and b are lower and upper integration limits
I, err = integrate.quad( func=f, a=low, b=up ) # returns a tuple of the integral value, and the estimated error

integrate.quad_explain() #call this to see how quad works...
```
---
### `trapz` and `simps`

- Simpson's method and the trapezoid method take sequences, not functions
```python
>>> np.trapz([1,2,3])
4.0
>>> np.trapz([1,2,3], x=[4,6,8])
8.0
>>> integrate.simps( [1,2,3], x=[4,6,8] )
8.0
```

---

## root finding

- Root finding methods are in `scipy.optimize`:
  - [Documentation](http://docs.scipy.org/doc/scipy/reference/optimize.html)

`bisect` and `newton` methods

`newton` defaults to Secant Method is no derivative `fprime` is given
```python
newton(f, x0, fprime=None) #defaults to secant
```


---

## more...

*FYI:* Linear Algebra: 

- `scipy.linalg` (use arrays for matrices)

other useful non-`scipy` packages:
```python
scikit-learn # machine learning
scikit-image # image analysis
flask, django # web development
socket, serial # serial communication
sqlite3 #SQL  databases
requests # html requests
BeautifulSoup # html parsing
```

---
## What we can do now...

Curve fitting:

- still in `scipy.optimize`... -> `scipy.optimize.curve_fit`

`curve_fit()` [documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)

---

## Let's Practice Together

- Example fitting code
- Fit the double Gaussian by modifying `fitting.py`
- Bring some research data on Thursday if you want.
