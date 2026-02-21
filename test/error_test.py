import pytest
from main import main

def test_unknown_report(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--files", "x.csv", "--report", "unknown"]
    )

    with pytest.raises(ValueError):
        main()

def test_no_files(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--report", "average-gdp"]
    )

    with pytest.raises(SystemExit):
        main()
