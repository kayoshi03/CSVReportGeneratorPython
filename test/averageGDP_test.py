from reports.average_gdp import AverageGDP

def test_average_gdp_report_test():
    rows = [
        {"country": "USA", "gdp": "100"},
        {"country": "USA", "gdp": "300"},
        {"country": "RUSSIA", "gdp": "150"},
    ]

    report = AverageGDP()
    result = report.generate(rows)

    assert result == [
        ["USA", 200.0],
        ["RUSSIA", 150.0]
    ]