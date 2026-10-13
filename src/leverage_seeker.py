"""Leverage Seeker: $0-capital idea generator and 1-click Colony seeder.

Uses combinatorial recombination + controlled randomness to produce executable,
high-leverage startup ideas that fit the SI Colony structure and bootstrap
without paid capital.
"""

import random
from typing import Dict, List
from .colony.kernel import ColonyKernel

# Pattern library for zero-capital leverage
DOMAINS = [
    "niche AI tools", "public data research", "open-source developer utilities",
    "content automation for X/Twitter", "GitHub-based distribution",
    "email newsletter on emerging tech", "community building in Discord/Reddit",
    "automated lead magnets", "micro-SaaS on free tiers", "viral thread generators"
]

CHANNELS = [
    "GitHub + stars", "X/Twitter daily posts", "Reddit niche subreddits",
    "Hacker News / Indie Hackers", "email list (free tier)", "YouTube Shorts / Reels",
    "product hunt style launches", "open-source contribution graphs"
]

MONETIZATION_LATER = [
    "sponsorships", "paid tier later", "affiliate", "premium module",
    "consulting from audience", "SaaS conversion", "data product"
]

COLONY_FIT = [
    "Engineering builds the tool, Marketing distributes daily",
    "Governor tracks signals, Meta proposes pivots",
    "Finance tracks non-monetary value (stars, followers, emails) first",
    "Full modular departments scale the flywheel"
]

def generate_leverage_idea(seed: int = None) -> Dict:
    """Generate a concrete $0-capital idea via combinatorial sampling."""
    if seed is not None:
        random.seed(seed)
    domain = random.choice(DOMAINS)
    channel = random.choice(CHANNELS)
    later = random.choice(MONETIZATION_LATER)
    fit = random.choice(COLONY_FIT)

    idea = {
        "title": f"{domain.title()} via {channel}",
        "description": (
            f"Build a {domain} that bootstraps through {channel}. "
            f"Start at $0 using free tiers, public data, and open distribution. "
            f"Later path: {later}. Colony structure: {fit}."
        ),
        "goal": f"Create and distribute a {domain} primarily via {channel}, measuring traction at zero capital.",
        "constraints": {"budget": 0.0, "paid_ads": False, "priority": "distribution_and_signals"},
        "flywheel": "content/tool → distribution → audience → more content/tools → compounding reach",
        "random_seed": random.randint(1000, 9999)
    }
    return idea

def seed_colony_from_leverage(seed: int = None) -> ColonyKernel:
    """1-click: generate idea and instantiate a ready Colony."""
    idea = generate_leverage_idea(seed)
    colony = ColonyKernel(
        goal=idea["goal"],
        budget=0.0,
        constraints=idea["constraints"]
    )
    # Seed default modular departments (stubs)
    colony.add_department("Governor", {"role": "strategy_and_allocation"})
    colony.add_department("Engineering", {"role": "build_and_ship"})
    colony.add_department("Marketing", {"role": "distribute_and_amplify"})
    colony.add_department("Meta", {"role": "evolve_and_improve"})
    colony.memory["seed_idea"] = idea
    colony._log(f"Leverage Seeker seeded colony with: {idea['title']}")
    return colony

def one_click_start(seed: int = None) -> Dict:
    """Public 1-click entry point. Returns colony status + idea."""
    colony = seed_colony_from_leverage(seed)
    # Immediate first cycle
    cycle = colony.execute_cycle()
    return {
        "idea": colony.memory["seed_idea"],
        "colony_status": colony.status_report(),
        "first_cycle": cycle,
        "message": "Colony started at $0 capital. Running autonomous loops."
    }
