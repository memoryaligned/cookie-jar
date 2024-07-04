# Pandas Window Functions

<!-- toc -->

- [Lag and Lead](#lag-and-lead)
- [Moving Averages](#moving-averages)
- [Rolling Averages](#rolling-averages)
- [Ranking and Percentiles](#ranking-and-percentiles)
- [Expanding Aggregations](#expanding-aggregations)

<!-- tocstop -->

## Lag and Lead

Lag one period

```python
df["lag_1"] = df["price"].shift(1)
```

Lead one period

```python
df["lead_1"] = df["price"].shift(-1)
```

## Moving Averages

## Rolling Averages

Five day rolling average:

```python
df["price_5_rolling_avg"] = df["price"].rolling(5).mean()
```

Five day max/min:

```python
df["price_5_max"] = df["price"].rolling(5).max()
df["price_5_min"] = df["price"].rolling(5).min()
```

## Ranking and Percentiles

Percent change from previous day:

```python
df["price_delta"] = df["price"].pct_change(1) * 100
```

## Expanding Aggregations

This allows us to create a cumulative sum

```python
df["cum_sum"] = df["price"].expanding().sum()
```

To see the lowerest price so far (cumulative min):

```python
df["cum_min"] = df["price"].cummin()
```
