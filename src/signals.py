"""Signal extraction functions for fake app detection."""

from fuzzywuzzy import fuzz
import imagehash
from PIL import Image
import requests
from io import BytesIO

class SignalExtractor:
    
    @staticmethod
    def name_similarity(app_name, official_name):
        """
        Calculate name similarity using fuzzy matching.
        
        Returns:
            Float between 0-1 (1 = identical)
        """
        return fuzz.ratio(app_name.lower(), official_name.lower()) / 100.0
    
    @staticmethod
    def package_name_check(package_id, official_package):
        """
        Check if package name is suspicious.
        
        Returns:
            dict with 'is_suspicious' and 'reason'
        """
        if package_id == official_package:
            return {"is_suspicious": False, "reason": "Exact match"}
        
        if official_package in package_id:
            return {
                "is_suspicious": True, 
                "reason": f"Contains official package but has extra parts: {package_id}"
            }
        
        similarity = fuzz.ratio(package_id, official_package) / 100.0
        if similarity > 0.7:
            return {
                "is_suspicious": True,
                "reason": f"Very similar package name (similarity: {similarity:.2f})"
            }
        
        return {"is_suspicious": False, "reason": "Different package"}
    
    @staticmethod
    def publisher_check(app_publisher, official_publisher):
        """
        Check if publisher matches official publisher.
        
        Returns:
            dict with 'matches' and 'similarity'
        """
        similarity = fuzz.ratio(app_publisher.lower(), official_publisher.lower()) / 100.0
        
        return {
            "matches": similarity > 0.9,
            "similarity": similarity,
            "reason": "Exact match" if similarity > 0.9 else "Publisher mismatch"
        }
    
    @staticmethod
    def icon_similarity(icon_url_1, icon_url_2):
        """
        Compare two app icons using perceptual hashing.
        
        Returns:
            Float between 0-1 (1 = identical)
        """
        try:
            # Download icons
            img1 = Image.open(BytesIO(requests.get(icon_url_1).content))
            img2 = Image.open(BytesIO(requests.get(icon_url_2).content))
            
            # Calculate perceptual hash
            hash1 = imagehash.average_hash(img1)
            hash2 = imagehash.average_hash(img2)
            
            # Calculate similarity (lower hash difference = more similar)
            hash_diff = hash1 - hash2
            similarity = 1 - (hash_diff / 64.0)  # Normalize to 0-1
            
            return similarity
        except:
            return 0.0  # If images can't be compared
