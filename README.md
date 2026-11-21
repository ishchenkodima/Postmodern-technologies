# Postmodern-technologies

## What

Three study labs in Python. Each lab has code and unit tests.

| Folder | Code | Tests |
|---|---|---|
| `лаб 1` | binary exponentiation | 4 asserts |
| `lab 2` | password validator (length, digits, upper and lower case) | 6 tests: valid password, short password, no digit, no upper case, no lower case, exit codes |
| `lab 3` | thread-safe Singleton for a database connection (fake connection) | 4 tests |

## How to run

You need Python 3.10+. No extra packages.

```bash
cd "lab 2"
python -m unittest -v
```

The same command works in `lab 3`. In `лаб 1` run `python test_dumb_code.py`.

## Results

All tests pass (checked with Python 3.10).

Known issue: in `lab 3` the test `test_missing_connection` always passes.
The Singleton keeps the connection from the earlier tests, so no exception happens,
and the test has no `fail()` after the call. This is a false positive test.
