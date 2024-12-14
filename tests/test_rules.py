"""Tests for the rules module."""

import coverage_pytest.assets.mapping
import coverage_pytest.rules


def test_simple_rule_engine_with_foo():
    inp = {"foo": "test_value"}
    expected_output = {"bar": "test_value"}
    assert coverage_pytest.rules.rule_engine(inp) == expected_output


def test_simple_rule_engine_without_foo():
    inp = {"not_foo": "test_value"}
    expected_output = {"bar": "baz"}
    assert coverage_pytest.rules.rule_engine(inp) == expected_output
