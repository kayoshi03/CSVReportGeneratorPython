from read import read_files

def test_read_files(tmp_path):
    file = tmp_path / "data.csv"
    file.write_text(
        "country,gdp\nUSA,100\nChina,200\n",
        encoding="utf-8"
    )

    rows = read_files([str(file)])

    assert len(rows) == 2
    assert rows[0]["country"] == "USA"
    assert rows[1]["gdp"] == "200"

