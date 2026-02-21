from reports.base import Base
from statistics import mean

class AverageGDP(Base):
    name = "average-gdp"
    title = ["Country", "Average GDP"]

    def generate(self, rows):
        data = {}

        for row in rows:
            country = row["country"]
            gdp = float(row["gdp"])
            data.setdefault(country, []).append(gdp)

        result = [
            [country, round(mean(values), 2)]
            for country, values in data.items()
        ]

        result.sort(key = lambda x: x[1], reverse=True)
        return result