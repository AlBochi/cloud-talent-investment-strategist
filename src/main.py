#!/usr/bin/env python3
"""
Cloud Talent Investment Strategist - Main Application
Executive decision-support platform for cloud talent investments.
"""

import argparse
from .models.roi_engine import CloudTalentROIEngine

def main():
    parser = argparse.ArgumentParser(description="Cloud Talent Investment Strategist")
    parser.add_argument("--role", help="Cloud role to analyze")
    parser.add_argument("--team-size", type=int, help="Team size to model")
    parser.add_argument("--cloud-spend", type=float, help="Annual cloud spend in USD")
    parser.add_argument("--report", action="store_true", help="Generate executive report")
    
    args = parser.parse_args()
    
    # Initialize the ROI engine
    engine = CloudTalentROIEngine()
    
    if args.role and args.team_size and args.cloud_spend:
        # Run analysis
        results = engine.monte_carlo_simulation(args.role, args.team_size, args.cloud_spend)
        print(f"Analysis results for {args.team_size} {args.role}s:")
        for key, value in results.items():
            print(f"{key}: {value}")
    
    if args.report:
        # Generate executive report
        report = engine.generate_investment_memo({
            "analysis_id": "CTIS-2024-08-23-001",
            "role": args.role,
            "risk_adjusted_roi": 42.5,
            "payback_period": 8.2,
            "npv": 1200000,
            "irr": 0.42,
            "annualized_return": 0.38,
            "var_95": 250000,
            "expected_shortfall": 0.12,
            "sharpe_ratio": 3.2
        })
        print(report)

if __name__ == "__main__":
    main()
