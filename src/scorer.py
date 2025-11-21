"""Risk scoring logic for detected apps."""

from src.signals import SignalExtractor
from config import THRESHOLDS, GENUINE_APPS

class RiskScorer:
    def __init__(self):
        self.signal_extractor = SignalExtractor()
    
    def calculate_risk_score(self, app, brand_key):
        """
        Calculate risk score for an app.
        
        Args:
            app: App dictionary with name, package_id, publisher
            brand_key: Key in GENUINE_APPS config
        
        Returns:
            dict with risk_score (0-100), signals, and verdict
        """
        if brand_key not in GENUINE_APPS:
            return {"error": "Unknown brand"}
        
        official_app = GENUINE_APPS[brand_key]
        risk_score = 0
        signals = {}
        flags = []

        # Use the configured official display name if available
        official_name = official_app.get("official_name", brand_key.title())

        # Signal 1: Name similarity (0-1)
        name_sim = self.signal_extractor.name_similarity(app["name"], official_name)
        signals["name_similarity"] = name_sim

        # Weight name similarity more clearly: higher similarity with mismatched package -> stronger signal
        if name_sim >= THRESHOLDS["name_similarity_high"] and app["package_id"] != official_app["package_id"]:
            risk_score += 40
            flags.append("High name similarity but different package")
        elif name_sim >= THRESHOLDS["name_similarity_medium"] and app["package_id"] != official_app["package_id"]:
            risk_score += 20
            flags.append("Moderate name similarity but different package")

        # Signal 2: Package name check
        package_check = self.signal_extractor.package_name_check(app["package_id"], official_app["package_id"])
        signals["package_check"] = package_check

        if package_check["is_suspicious"]:
            risk_score += THRESHOLDS["package_mismatch_penalty"]
            flags.append(package_check["reason"])

        # Signal 3: Publisher check
        publisher_check = self.signal_extractor.publisher_check(app["publisher"], official_app["publisher"])
        signals["publisher_check"] = publisher_check

        if not publisher_check["matches"]:
            # If publisher totally differs it's a strong signal; if it's somewhat similar, penalize less
            if publisher_check["similarity"] < 0.7:
                risk_score += THRESHOLDS["publisher_mismatch_penalty"]
            else:
                risk_score += int(THRESHOLDS["publisher_mismatch_penalty"] * 0.6)
            flags.append(f"Publisher mismatch: '{app['publisher']}'")
        
        # Determine verdict
        if risk_score >= 70:
            verdict = "HIGH RISK - Likely fake"
        elif risk_score >= 40:
            verdict = "MEDIUM RISK - Suspicious"
        else:
            verdict = "LOW RISK - Appears legitimate"
        
        return {
            "app_name": app["name"],
            "package_id": app["package_id"],
            "publisher": app["publisher"],
            "risk_score": min(risk_score, 100),
            "verdict": verdict,
            "signals": signals,
            "flags": flags
        }
