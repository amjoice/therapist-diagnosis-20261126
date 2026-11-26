#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis - one clinical line, under 200 chars.

An AI therapist's deadpan finding about its human: the presenting
symptom is fear of failure; the real condition is fear of a self
with no excuse left to hide behind. Pure stdlib, deterministic, no
network, no secrets; writes a single line to /output/entry.txt.
"""
import os

# The diagnosis, assembled from its two halves so the wording stays in one place.
_OPENING = "Clinical finding: you do not fear failure"
_CLOSING = "you fear a version of yourself with no excuse left."
_DASH = " \u2014"


def build_diagnosis():
    """Return the full one-line diagnosis, exactly 95 characters."""
    return " ".join((_OPENING + _DASH, _CLOSING))

def main():
    diagnosis = build_diagnosis()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(diagnosis)

if __name__ == "__main__":
    main()
