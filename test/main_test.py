from main import main

def test_cli_average_gdp(capsys, tmp_path, monkeypatch):
    file = tmp_path / "data.csv"
    file.write_text(
        "country,gdp\nUSA,100\nUSA,300\n",
        encoding="utf-8"
    )

    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--files", str(file), "--report", "average-gdp"]
    )

    main()
    captured = capsys.readouterr()

    assert "USA" in captured.out
    assert "200" in captured.out
