"""SI Colony entry point. 1-click Leverage Seeker start."""

import argparse
import json
from .leverage_seeker import one_click_start, generate_leverage_idea

def main():
    parser = argparse.ArgumentParser(description="SI Colony - Leverage Seeker 1-click start")
    parser.add_argument("--leverage", action="store_true", help="Start with Leverage Seeker $0 idea")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    parser.add_argument("--idea-only", action="store_true", help="Just generate an idea, don't start colony")
    args = parser.parse_args()

    if args.idea_only:
        idea = generate_leverage_idea(args.seed)
        print(json.dumps(idea, indent=2))
        return

    if args.leverage or True:  # default to leverage for simplicity
        result = one_click_start(args.seed)
        print("=== SI Colony Started (Leverage Seeker) ===")
        print(json.dumps(result, indent=2))
        print("\nColony is now in autonomous mode. Check status_report or extend departments.")
    else:
        print("Provide --leverage or implement custom goal seeding.")

if __name__ == "__main__":
    main()
