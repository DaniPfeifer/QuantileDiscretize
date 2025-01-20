# QuantileDiscretize
Python quantile discretize function

# Inputs:
- `df`: A pandas database.<br>
- `numOfIntervals`: An integer, the number of intervals to discretize to.<br>
- `printPartitions` (optional): `True` or `False`. If `True`, the interval boundaries of each column are printed. Default: `False`. If the printed list is `[a,b,c]`, then the first interval is `]-∞,a[`, the second interval is `[a,b[`, the third interval is `[b,c[`, and the last interval is `[c,∞[`.

# Outputs:
A pandas database of the same shape and columns, but values discretized to the given number of intervals.

# Examples
`discretized_df = quantileDiscretize(df, 5)`<br>
`discretized_df = quantileDiscretize(df, 7, printPartitions=True)`
