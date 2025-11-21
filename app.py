"""Main Flask application for fake app detection."""

from flask import Flask, render_template_string, request, jsonify
from src.scraper import AppScraper
from src.scorer import RiskScorer

app = Flask(__name__)
scraper = AppScraper()
scorer = RiskScorer()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Fake App Detector</title>
    <style>
        body { font-family: Arial; max-width: 1200px; margin: 50px auto; padding: 20px; }
        h1 { color: #333; }
        .search-box { margin: 20px 0; }
        input { padding: 10px; width: 300px; font-size: 16px; }
        button { padding: 10px 20px; font-size: 16px; background: #007bff; color: white; border: none; cursor: pointer; }
        button:hover { background: #0056b3; }
        .results { margin-top: 30px; }
        .app-card { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .high-risk { border-left: 5px solid #dc3545; background: #fff5f5; }
        .medium-risk { border-left: 5px solid #ffc107; background: #fffef5; }
        .low-risk { border-left: 5px solid #28a745; background: #f5fff5; }
        .risk-score { font-size: 24px; font-weight: bold; }
        .flags { margin-top: 10px; }
        .flag { background: #f8d7da; padding: 5px 10px; margin: 5px 0; border-radius: 3px; }
    </style>
</head>
<body>
    <h1>🔍 Fake App Detector</h1>
    <p>Enter a brand name to scan for fake/suspicious apps</p>
    
    <div class="search-box">
        <input type="text" id="brand" placeholder="e.g., phonepe, paytm" />
        <button onclick="scanApps()">Scan Apps</button>
    </div>
    
    <div id="results" class="results"></div>
    
    <script>
        function scanApps() {
            const brand = document.getElementById('brand').value;
            fetch('/scan?brand=' + brand)
                .then(r => r.json())
                .then(data => {
                    let html = '<h2>Scan Results</h2>';
                    data.forEach(app => {
                        let riskClass = app.risk_score >= 70 ? 'high-risk' : 
                                       app.risk_score >= 40 ? 'medium-risk' : 'low-risk';
                        html += `
                            <div class="app-card ${riskClass}">
                                <h3>${app.app_name}</h3>
                                <p><strong>Package:</strong> ${app.package_id}</p>
                                <p><strong>Publisher:</strong> ${app.publisher}</p>
                                <p class="risk-score">Risk Score: ${app.risk_score}/100</p>
                                <p><strong>Verdict:</strong> ${app.verdict}</p>
                                <div class="flags">
                                    ${app.flags.map(f => `<div class="flag">⚠️ ${f}</div>`).join('')}
                                </div>
                            </div>
                        `;
                    });
                    document.getElementById('results').innerHTML = html;
                });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/scan')
def scan():
    brand = request.args.get('brand', 'phonepe')
    
    # Fetch candidate apps
    apps = scraper.search_apps(brand, mock=True)
    
    # Score each app
    results = []
    for app in apps:
        score = scorer.calculate_risk_score(app, brand.lower())
        results.append(score)
    
    # Sort by risk score (highest first)
    results.sort(key=lambda x: x['risk_score'], reverse=True)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
