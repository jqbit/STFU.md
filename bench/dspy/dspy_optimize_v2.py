"""DSPy optimization v2 — uses expanded 10x probe corpus + bigger search.
Run: python3 dspy_optimize_v2.py {stfu|blunt}
"""
import sys
sys.path.insert(0, "/tmp/stfu-test/scripts")
from dspy_optimize import score_stfu_probe, score_blunt_probe, optimize
from pathlib import Path
import json


def main(variant: str):
    splits = json.loads(Path("/tmp/stfu-test/dspy/probe_splits_10x.json").read_text())
    train = splits[variant]["train"]
    if variant == "stfu":
        seed = Path("/tmp/stfu-test/prompts/old-stfu-v016.md").read_text()
        scorer = score_stfu_probe
    else:
        # Use the v0.17.0 DSPy-optimized BLUNT as the new seed (warm start)
        seed = Path("/tmp/stfu-repo/STFU.blunt.md").read_text()
        scorer = score_blunt_probe
    optimize(seed, train, scorer, variant, breadth=6, depth=4,
             out_dir="/tmp/stfu-test/dspy/v2")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 dspy_optimize_v2.py {stfu|blunt}")
        sys.exit(1)
    main(sys.argv[1])
