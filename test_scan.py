"""Quick test runner to print scanner results for mock data."""
import json
from src.scraper import AppScraper
from src.scorer import RiskScorer

def run():
    scraper = AppScraper()
    scorer = RiskScorer()

    brand = "phonepe"
    apps = scraper.search_apps(brand, mock=True)

    results = []
    for app in apps:
        score = scorer.calculate_risk_score(app, brand)
        results.append(score)

    # sort and print
    results.sort(key=lambda x: x.get("risk_score", 0), reverse=True)
    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    run()
