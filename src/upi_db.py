"""Comprehensive UPI apps database and helper utilities.

This file exports `COMPLETE_UPI_APPS_DATABASE` and helper functions
that the rest of the application can use for genuine-app lookups.
"""
from typing import Dict, Tuple, Optional, List

# Comprehensive UPI Apps Database
COMPLETE_UPI_APPS_DATABASE: Dict[str, Dict] = {
    'phonepe': {
        'package': 'com.phonepe.app',
        'publisher': 'PhonePe Private Limited',
        'name': 'PhonePe',
        'min_installs': 500000000,
        'category': 'major',
        'alternate_packages': []
    },
    'googlepay': {
        'package': 'com.google.android.apps.nbu.paisa.user',
        'publisher': 'Google LLC',
        'name': 'Google Pay',
        'min_installs': 500000000,
        'category': 'major',
        'alternate_packages': []
    },
    'paytm': {
        'package': 'net.one97.paytm',
        'publisher': 'Paytm Mobile Solutions Pvt. Ltd.',
        'name': 'Paytm',
        'min_installs': 500000000,
        'category': 'major',
        'alternate_packages': []
    },
    'bhim': {
        'package': 'in.org.npci.upiapp',
        'publisher': 'National Payments Corporation of India',
        'name': 'BHIM UPI',
        'min_installs': 100000000,
        'category': 'government',
        'alternate_packages': []
    },
    'amazonpay': {
        'package': 'in.amazon.mShop.android.shopping',
        'publisher': 'Amazon Mobile LLC',
        'name': 'Amazon',
        'min_installs': 100000000,
        'category': 'ecommerce',
        'alternate_packages': []
    },
    'flipkart': {
        'package': 'com.phonepe.app',
        'publisher': 'PhonePe Private Limited',
        'name': 'Flipkart (PhonePe)',
        'min_installs': 100000000,
        'category': 'ecommerce',
        'alternate_packages': []
    },
    'mobikwik': {
        'package': 'com.mobikwik_new',
        'publisher': 'MobiKwik',
        'name': 'MobiKwik',
        'min_installs': 50000000,
        'category': 'wallet',
        'alternate_packages': []
    },
    'freecharge': {
        'package': 'com.freecharge.android',
        'publisher': 'Freecharge',
        'name': 'Freecharge',
        'min_installs': 50000000,
        'category': 'wallet',
        'alternate_packages': []
    },
    'airtel': {
        'package': 'com.myairtelapp',
        'publisher': 'Bharti Airtel Ltd.',
        'name': 'Airtel Thanks',
        'min_installs': 100000000,
        'category': 'telecom',
        'alternate_packages': []
    },
    'jio': {
        'package': 'com.jio.myjio',
        'publisher': 'Jio Platforms Limited',
        'name': 'MyJio',
        'min_installs': 500000000,
        'category': 'telecom',
        'alternate_packages': []
    },
    'sbi': {
        'package': 'com.sbi.lotusintouch',
        'publisher': 'State Bank of India',
        'name': 'YONO SBI',
        'min_installs': 100000000,
        'category': 'bank',
        'alternate_packages': ['com.sbi.upi']
    },
    'axis': {
        'package': 'com.axis.mobile',
        'publisher': 'Axis Bank Ltd.',
        'name': 'Axis Mobile',
        'min_installs': 10000000,
        'category': 'bank',
        'alternate_packages': []
    },
    'icici': {
        'package': 'com.csam.icici.bank.imobile',
        'publisher': 'ICICI Bank Ltd.',
        'name': 'iMobile Pay',
        'min_installs': 50000000,
        'category': 'bank',
        'alternate_packages': ['com.icicibank.pockets']
    },
    'hdfc': {
        'package': 'com.snapwork.hdfc',
        'publisher': 'HDFC Bank Ltd',
        'name': 'HDFC Bank MobileBanking',
        'min_installs': 50000000,
        'category': 'bank',
        'alternate_packages': []
    },
    'kotak': {
        'package': 'com.msf.kbank.mobile',
        'publisher': 'Kotak Mahindra Bank',
        'name': 'Kotak Mobile Banking',
        'min_installs': 10000000,
        'category': 'bank',
        'alternate_packages': []
    },
    'pnb': {
        'package': 'com.fss.pnbone',
        'publisher': 'Punjab National Bank',
        'name': 'PNB ONE',
        'min_installs': 10000000,
        'category': 'bank',
        'alternate_packages': []
    },
    'idfc': {
        'package': 'com.idfcfirstbank.optimus',
        'publisher': 'IDFC FIRST Bank',
        'name': 'IDFC FIRST Bank',
        'min_installs': 5000000,
        'category': 'bank',
        'alternate_packages': []
    },
    'indusind': {
        'package': 'com.indusind.mobile',
        'publisher': 'IndusInd Bank',
        'name': 'IndusInd Bank',
        'min_installs': 5000000,
        'category': 'bank',
        'alternate_packages': []
    },
    'yes': {
        'package': 'com.enstage.wibmo.hdfc',
        'publisher': 'YES BANK',
        'name': 'YES BANK',
        'min_installs': 5000000,
        'category': 'bank',
        'alternate_packages': []
    },
    'whatsapp': {
        'package': 'com.whatsapp',
        'publisher': 'WhatsApp LLC',
        'name': 'WhatsApp',
        'min_installs': 5000000000,
        'category': 'messaging',
        'alternate_packages': []
    },
    'cred': {
        'package': 'com.dreamplug.androidapp',
        'publisher': 'Dreamplug Technologies',
        'name': 'CRED',
        'min_installs': 10000000,
        'category': 'fintech',
        'alternate_packages': []
    },
    'bharatpe': {
        'package': 'com.bharatpe.merchantapp',
        'publisher': 'BharatPe Merchant',
        'name': 'BharatPe',
        'min_installs': 10000000,
        'category': 'merchant',
        'alternate_packages': []
    },
    'samsung': {
        'package': 'com.samsung.android.spaymini',
        'publisher': 'Samsung Electronics Co., Ltd.',
        'name': 'Samsung Pay Mini',
        'min_installs': 10000000,
        'category': 'oem',
        'alternate_packages': []
    },
    'zomato': {
        'package': 'com.application.zomato',
        'publisher': 'Zomato',
        'name': 'Zomato',
        'min_installs': 100000000,
        'category': 'food',
        'alternate_packages': []
    },
    'swiggy': {
        'package': 'in.swiggy.android',
        'publisher': 'Bundl Technologies Pvt. Ltd',
        'name': 'Swiggy',
        'min_installs': 100000000,
        'category': 'food',
        'alternate_packages': []
    },
    'bob': {
        'package': 'com.bobibanking.mobile',
        'publisher': 'Bank of Baroda',
        'name': 'bob World',
        'min_installs': 10000000,
        'category': 'bank',
        'alternate_packages': []
    },
    'canara': {
        'package': 'com.canara.mbanking',
        'publisher': 'Canara Bank',
        'name': 'Canara ai1',
        'min_installs': 5000000,
        'category': 'bank',
        'alternate_packages': []
    },
    'union': {
        'package': 'com.unionbank.eportfolio.mobile',
        'publisher': 'Union Bank of India',
        'name': 'Union Bank',
        'min_installs': 5000000,
        'category': 'bank',
        'alternate_packages': []
    },
    'uco': {
        'package': 'uco.mobile.ucopay',
        'publisher': 'UCO Bank',
        'name': 'UCO UPI',
        'min_installs': 1000000,
        'category': 'bank',
        'alternate_packages': []
    },
    'indian': {
        'package': 'com.infrasofttech.indianbank',
        'publisher': 'Indian Bank',
        'name': 'Indian Bank Anywhere',
        'min_installs': 5000000,
        'category': 'bank',
        'alternate_packages': []
    },
}

# Categories mapping (kept for convenience)
UPI_APP_CATEGORIES = {
    'major': ['phonepe', 'googlepay', 'paytm'],
    'government': ['bhim'],
    'bank': ['sbi', 'axis', 'icici', 'hdfc', 'kotak', 'pnb', 'idfc', 'indusind', 'yes', 'bob', 'canara', 'union', 'uco', 'indian'],
    'wallet': ['mobikwik', 'freecharge'],
    'telecom': ['airtel', 'jio'],
    'ecommerce': ['amazonpay', 'flipkart'],
    'fintech': ['cred'],
    'merchant': ['bharatpe'],
    'messaging': ['whatsapp'],
    'food': ['zomato', 'swiggy'],
    'oem': ['samsung']
}

# Known suspicious package patterns for UPI apps (regex strings)
SUSPICIOUS_UPI_PATTERNS: List[str] = [
    r'\.update$',
    r'\.pro$',
    r'\.new$',
    r'\.official$',
    r'\.real$',
    r'\.secure$',
    r'\.fast$',
    r'\.lite$',
    r'\.plus$',
    r'\.premium$',
    r'^com\.app\.',
    r'^com\.free\.',
    r'^com\.download\.',
    r'^com\.install\.',
    r'^com\.get\.',
    r'\.fake',
    r'\.test',
    r'\.demo',
    r'\.copy',
    r'\.clone',
    r'upi.*payment',
    r'payment.*upi',
    r'instant.*pay',
    r'quick.*pay',
]

def get_all_genuine_packages() -> List[str]:
    packages = []
    for app_data in COMPLETE_UPI_APPS_DATABASE.values():
        packages.append(app_data['package'])
        packages.extend(app_data.get('alternate_packages', []))
    return list(set(packages))

def get_apps_by_category(category: str) -> List[str]:
    return [app for app in UPI_APP_CATEGORIES.get(category, [])]

def is_genuine_package(package_name: str) -> bool:
    return package_name in get_all_genuine_packages()

def get_app_by_package(package_name: str) -> Tuple[Optional[str], Optional[Dict]]:
    for app_key, app_data in COMPLETE_UPI_APPS_DATABASE.items():
        if app_data['package'] == package_name:
            return app_key, app_data
        if package_name in app_data.get('alternate_packages', []):
            return app_key, app_data
    return None, None

__all__ = [
    'COMPLETE_UPI_APPS_DATABASE',
    'UPI_APP_CATEGORIES',
    'SUSPICIOUS_UPI_PATTERNS',
    'get_all_genuine_packages',
    'get_apps_by_category',
    'is_genuine_package',
    'get_app_by_package'
]

if __name__ == '__main__':
    print("Total UPI Apps in Database:", len(COMPLETE_UPI_APPS_DATABASE))
    print("\nAll Genuine Package Names:")
    for pkg in get_all_genuine_packages():
        print(f"  - {pkg}")
