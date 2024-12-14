"""Sample file."""


def rule_engine(inp: dict) -> dict:
    """Sample function."""
    if "foo" in inp:
        return {"bar": inp["foo"]}
    return {"bar": "baz"}
