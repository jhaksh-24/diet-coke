"""Configuration for the fake app detector.

This module builds a compact `GENUINE_APPS` mapping used by the scorer
from the more comprehensive `src.upi_db.COMPLETE_UPI_APPS_DATABASE`.
"""

from src.upi_db import COMPLETE_UPI_APPS_DATABASE

# Build a minimal GENUINE_APPS mapping expected by scorer and other components.
# Each entry includes: package_id, publisher, official_name, and optional icon URL.
GENUINE_APPS = {}
for key, data in COMPLETE_UPI_APPS_DATABASE.items():
    GENUINE_APPS[key] = {
        "package_id": data.get("package"),
        "publisher": data.get("publisher"),
        "official_name": data.get("name"),
        "official_icon_url": data.get("official_icon_url", "")
    }

# Risk scoring thresholds
THRESHOLDS = {
    "name_similarity_high": 0.85,
    "name_similarity_medium": 0.70,
    "package_mismatch_penalty": 30,
    "publisher_mismatch_penalty": 40,
    "icon_similarity_suspicious": 0.80,
}
