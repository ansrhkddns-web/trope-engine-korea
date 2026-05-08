#!/usr/bin/env python3
"""Check a phase-10 trope memory/transfer artifact for required signals.

Usage:
  python cliche_memory_lint.py path/to/trope-memory.md
  python cliche_memory_lint.py -
  python cliche_memory_lint.py --self-test
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Check:
    name: str
    terms: tuple[str, ...]
    weight: int = 1


CHECKS = (
    Check("source cases", ("source cases", "source_family", "source_abstraction", "소스", "레퍼런스"), 2),
    Check("memory card", ("trope_memory_card", "memory card", "메모리 카드", "id:", "label:"), 3),
    Check("trope dna", ("trope_dna", "pressure", "proof_object", "witness", "reward", "cost", "institution", "hook_object"), 3),
    Check("preconditions", ("preconditions", "전제", "must exist", "ranking system", "public metric"), 2),
    Check("causal edges", ("causal_edges", "because", "therefore", "but", "인과"), 2),
    Check("retrieval cues", ("retrieval_cues", "retrieval", "cue", "검색 단서", "태그"), 2),
    Check("protected core", ("protected_core", "protected core", "보존 코어", "reusable_promise"), 3),
    Check("flexible shell", ("flexible_shell", "flexible shell", "전이 껍질", "transfer_axes"), 2),
    Check("transfer", ("cliche_transfer", "target_genre", "translated_shell", "transfer", "전이"), 2),
    Check("anti copy", ("anti_copy", "anti-copy", "copy-shadow", "signature scene", "복사"), 2),
    Check("validation", ("validation", "verdict", "pass", "revise", "rebuild", "검증", "판정"), 2),
    Check("next artifact", ("next_artifact", "다음 산출물", "handoff", "production artifact"), 1),
)


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def lint(text: str) -> tuple[int, list[str], list[str]]:
    normalized = text.lower()
    max_score = sum(check.weight for check in CHECKS)
    score = 0
    present: list[str] = []
    missing: list[str] = []

    for check in CHECKS:
        found = any(term.lower() in normalized for term in check.terms)
        if found:
            score += check.weight
            present.append(check.name)
        else:
            missing.append(check.name)

    percentage = round(score / max_score * 100) if max_score else 0
    return percentage, present, missing


def verdict(percentage: int) -> str:
    if percentage >= 85:
        return "pass"
    if percentage >= 65:
        return "revise"
    return "rebuild"


def run_self_test() -> int:
    sample = """
    trope_memory_card:
      id: TM-001
      label: public proof creates institutional cost
      source_family: trope ideation systems, narrative graph research, Korean webnovel practice
      source_abstraction: public proof becomes social recognition and legal pressure
      reusable_promise: rank recognition through visible proof
      trope_dna:
        pressure: association deadline
        protagonist_method: uses hidden gate memory under audit
        proof_object: raid survival ledger
        witness: association auditor
        reward: rank and raid rights
        cost: guild monopoly lawsuit
        institution: hunter association
        hook_object: emergency gate summons
      preconditions:
        - ranking system must exist
        - public metric must control status
      causal_edges:
        - because public proof exposes value
        - therefore guild monopoly reacts
        - but the lawsuit opens paid pressure
      retrieval_cues: hunter, rank, public metric, audit, guild lawsuit
      transfer_axes: institution, proof object, cost, hook object
      protected_core: public proof creates status and institutional pressure
      flexible_shell: hunter association can become academy, sect, board, or court
      anti_copy_rules: no named work, no signature scene order
      validation: pass with cliche_memory_lint.py and quality regression
      next_artifact: target genre transfer card
    cliche_transfer:
      source_memory_id: TM-001
      target_genre: murim
      translated_shell:
        institution: martial alliance
        proof_object: duel tablet
        witness: alliance envoy
        cost: blood debt
        hook_object: duel letter
      preserved_reward: recognition through public proof
      changed_axes: institution, proof object, witness, cost, hook object
      anti_copy_check: no source rule or scene order remains
      verdict: pass
    """
    percentage, _, missing = lint(sample)
    if percentage < 85 or missing:
        print(f"self-test failed: score={percentage}, missing={missing}", file=sys.stderr)
        return 1
    print(f"self-test passed: score={percentage}, verdict={verdict(percentage)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint a phase-10 trope memory or transfer output.")
    parser.add_argument("path", nargs="?", help="Markdown/YAML-ish file to lint, or '-' for stdin.")
    parser.add_argument("--self-test", action="store_true", help="Run built-in smoke test.")
    args = parser.parse_args(argv)

    if args.self_test:
        return run_self_test()
    if not args.path:
        parser.error("path is required unless --self-test is used")

    text = read_text(args.path)
    percentage, present, missing = lint(text)
    print(f"score: {percentage}")
    print(f"verdict: {verdict(percentage)}")
    if present:
        print("present:")
        for item in present:
            print(f"  - {item}")
    if missing:
        print("missing:")
        for item in missing:
            print(f"  - {item}")
    return 0 if percentage >= 65 else 2


if __name__ == "__main__":
    raise SystemExit(main())
