"""Configuration for the fake app detector."""

import json
import os
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
EXAMPLES_DIR = BASE_DIR / "examples"

# Load genuine apps database from JSON
def load_genuine_apps():
    """Load genuine apps from JSON file."""
    json_path = DATA_DIR / "genuine_apps.json"
    if json_path.exists():
        with open(json_path, 'r') as f:
            return json.load(f)
    return {}

# Load test apps for validation
def load_test_apps():
    """Load test apps from JSON file."""
    json_path = DATA_DIR / "test_apps.json"
    if json_path.exists():
        with open(json_path, 'r') as f:
            return json.load(f)
    return {}

# Import comprehensive UPI database
try:
    from src.upi_db import (
        COMPLETE_UPI_APPS_DATABASE,
        get_all_genuine_packages,
        is_genuine_package,
        get_app_by_package,
        SUSPICIOUS_UPI_PATTERNS
    )
    UPI_DB_AVAILABLE = True
except ImportError:
    UPI_DB_AVAILABLE = False
    COMPLETE_UPI_APPS_DATABASE = {}
    SUSPICIOUS_UPI_PATTERNS = []

# Load genuine apps (prioritize JSON, fallback to UPI DB)
GENUINE_APPS = load_genuine_apps()

# If JSON is empty, populate from UPI database
if not GENUINE_APPS and UPI_DB_AVAILABLE:
    for app_key, app_data in COMPLETE_UPI_APPS_DATABASE.items():
        GENUINE_APPS[app_key] = {
            "package_id": app_data["package"],
            "publisher": app_data["publisher"],
            "official_name": app_data["name"],
            "category": app_data["category"],
            "min_downloads": f"{app_data['min_installs'] // 1000000}M+",
        }

# Risk scoring thresholds
THRESHOLDS = {
    # Name similarity thresholds (0.0 - 1.0)
    "name_similarity_high": 0.85,      # Very similar name (likely typosquat)
    "name_similarity_medium": 0.70,    # Somewhat similar name
    
    # Package name similarity thresholds
    "package_similarity_high": 0.80,   # Package names very similar
    "package_similarity_medium": 0.60, # Package names somewhat similar
    
    # Risk score penalties
    "package_mismatch_penalty": 30,        # Different package with similar name
    "publisher_mismatch_penalty": 40,      # Publisher doesn't match
    "publisher_partial_mismatch": 24,      # Publisher somewhat similar but not exact
    "suspicious_keyword_penalty": 15,      # Contains suspicious keywords
    "low_downloads_penalty": 10,           # Very low download count vs official
    
    # Icon similarity thresholds
    "icon_similarity_suspicious": 0.80,    # Icon very similar to official
    
    # Download count thresholds (for suspicion)
    "min_legitimate_downloads": 1000000,   # 1M downloads
    "download_ratio_suspicious": 0.001,    # Less than 0.1% of official app downloads
}

# Suspicious keywords in app names/descriptions
SUSPICIOUS_KEYWORDS = [
    "update", "new", "pro", "premium", "official", "real", "secure", 
    "fast", "lite", "plus", "mod", "free", "download", "latest",
    "2024", "2025", "install", "get", "original", "verified"
]

# Suspicious package name patterns (regex patterns)
SUSPICIOUS_PACKAGE_PATTERNS = [
    r'\.update
