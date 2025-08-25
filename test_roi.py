#!/usr/bin/env python3
"""
Simple test script for the ROI engine
"""

import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from models.roi_engine import CloudTalentROIEngine

def test_engine():
    try:
        engine = CloudTalentROIEngine("config/parameters.yaml")
        print("✅ ROI Engine initialized successfully!")
        
        # Test Monte Carlo simulation
        results = engine.monte_carlo_simulation("cloud_architect", 3, 2000000)
        print("📊 Simulation results:", results)
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_engine()
