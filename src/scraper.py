"""Scraper to fetch app data from Play Store or mock data."""

import requests
from bs4 import BeautifulSoup

class AppScraper:
    def __init__(self):
        self.base_url = "https://play.google.com/store/search"
    
    def search_apps(self, brand_name, mock=True):
        """
        Search for apps by brand name.
        
        Args:
            brand_name: Brand to search for
            mock: If True, returns mock data for demo
        
        Returns:
            List of app dictionaries
        """
        if mock:
            return self._get_mock_data(brand_name)
        
        # Real scraping implementation (optional)
        return self._scrape_play_store(brand_name)
    
    def _get_mock_data(self, brand_name):
        """Generate mock app data for demonstration."""
        bn = (brand_name or "").lower()

        if "phone" in bn or bn == "phonepe":
            return [
                {
                    "name": "PhonePe",
                    "package_id": "com.phonepe.app",
                    "publisher": "PhonePe Private Limited",
                    "downloads": "500M+",
                    "rating": 4.5,
                    "description": "Official PhonePe app for payments"
                },
                {
                    "name": "PhonPe - UPI Payments",
                    "package_id": "com.phonepe.app.update",
                    "publisher": "PhonePe Services",
                    "downloads": "100K+",
                    "rating": 4.2,
                    "description": "Fast UPI payments and recharges"
                },
                {
                    "name": "PhonePe Secure",
                    "package_id": "com.phonepe.secure.app",
                    "publisher": "Mobile Payment Solutions",
                    "downloads": "50K+",
                    "rating": 3.8,
                    "description": "Secure payment app for PhonePe users"
                }
            ]

        if "paytm" in bn:
            return [
                {
                    "name": "Paytm",
                    "package_id": "net.one97.paytm",
                    "publisher": "Paytm Mobile Solutions",
                    "downloads": "100M+",
                    "rating": 4.3,
                    "description": "Official Paytm app for payments"
                },
                {
                    "name": "Paytm Wallet - Easy Payments",
                    "package_id": "net.one97.paytm.wallet.fake",
                    "publisher": "Paytm Services",
                    "downloads": "200K+",
                    "rating": 3.5,
                    "description": "Wallet and UPI"
                },
                {
                    "name": "Paytm Recharge",
                    "package_id": "com.paytm.recharge",
                    "publisher": "QuickPay Solutions",
                    "downloads": "10K+",
                    "rating": 3.0,
                    "description": "Recharge and bill payments"
                }
            ]

        if "google" in bn or "googlepay" in bn or "gpay" in bn:
            return [
                {
                    "name": "Google Pay",
                    "package_id": "com.google.android.apps.nbu.paisa.user",
                    "publisher": "Google LLC",
                    "downloads": "1B+",
                    "rating": 4.4,
                    "description": "Official Google Pay app"
                },
                {
                    "name": "GPay - Money Transfer",
                    "package_id": "com.gpay.app.fake",
                    "publisher": "GPay Services",
                    "downloads": "500K+",
                    "rating": 3.6,
                    "description": "Fast transfers and UPI"
                }
            ]

        # Generic fallback: return apps that contain the brand name in title
        return [
            {
                "name": f"{brand_name.title()} Official",
                "package_id": f"com.{bn}.official",
                "publisher": f"{brand_name.title()} Pvt Ltd",
                "downloads": "1M+",
                "rating": 4.0,
                "description": f"Official {brand_name.title()} app"
            },
            {
                "name": f"{brand_name.title()} - Payments",
                "package_id": f"com.{bn}.payments",
                "publisher": f"{brand_name.title()} Services",
                "downloads": "50K+",
                "rating": 3.2,
                "description": "Payments and recharge"
            }
        ]
    
    def _scrape_play_store(self, brand_name):
        """Actual Play Store scraping (implement if needed)."""
        # TODO: Implement real scraping
        # Note: Respect rate limits and ToS
        pass
