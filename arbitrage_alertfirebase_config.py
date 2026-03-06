"""Firebase initialization with proper error handling and singleton pattern."""
import os
import logging
from typing import Optional, Dict, Any
from firebase_admin import firestore, credentials, initialize_app
from firebase_admin.exceptions import FirebaseError

logger = logging.getLogger(__name__)

class FirebaseManager:
    """Singleton Firebase manager with robust error handling."""
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FirebaseManager, cls).__new__(cls)
        return cls._instance
    
    def initialize(self, credential_path: Optional[str] = None) -> None:
        """Initialize Firebase with comprehensive error handling."""
        if self._initialized:
            logger.info("Firebase already initialized")
            return
            
        try:
            # Validate credential file exists
            if credential_path and not os.path.exists(credential_path):
                raise FileNotFoundError(f"Firebase credential file not found: {credential_path}")
            
            # Initialize with explicit options
            cred = credentials.Certificate(credential_path) if credential_path else credentials.ApplicationDefault()
            app = initialize_app(