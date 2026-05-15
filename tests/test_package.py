"""Smoke tests for newtest-1."""

import importlib


def test_package_version() -> None:
    pkg = importlib.import_module("newtest_1")
    assert pkg.__version__ == "0.1.0"


def test_main_runs(capsys) -> None:
    from newtest_1.main import main

    main()
    out = capsys.readouterr().out
    assert "newtest-1" in out
