# Coverage on Python 3.12

Reproducible example for coverage + pytest not running on Python 3.12, narrowed down to an import
of a chunky asset.

## Steps to Reproduce

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

2. Check tat pytest runs normally on Python 3.11 and Python 3.12:

    ```bash
    uv run --python 3.11 pytest tests/
    ```

    ```bash
    uv run --python 3.12 pytest tests/
    ```

3. Check that coverage runs normally on Python 3.11:

    ```bash
    uv run --python 3.11 coverage run -m pytest tests/
    ```

4. Check that coverage fails on Python 3.12:

    ```bash
    uv run --python 3.12 coverage run -m pytest tests/
    ```

    Note that smaller assets work fine:

    ```bash
    uv run --python 3.12 coverage run -m pytest smaller_mapping_tests/
    ```
