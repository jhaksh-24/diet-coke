"""Configuration for the fake app detector."""

# Known genuine apps database
GENUINE_APPS = {
    "phonepe": {
        "package_id": "com.phonepe.app",
        "publisher": "PhonePe Private Limited",
        "official_icon_url": "https://...",
    },
    "paytm": {
        "package_id": "net.one97.paytm",
        "publisher": "Paytm Mobile Solutions",
        "official_icon_url": "https://...",
    },
    "googlepay": {
        "package_id": "com.google.android.apps.nbu.paisa.user",
        "publisher": "Google LLC",
        "official_icon_url": "https://...",
    }
}

# Risk scoring thresholds
THRESHOLDS = {
    "name_similarity_high": 0.85,
    "name_similarity_medium": 0.70,
    "package_mismatch_penalty": 30,
    "publisher_mismatch_penalty": 40,
    "icon_similarity_suspicious": 0.80,
}
