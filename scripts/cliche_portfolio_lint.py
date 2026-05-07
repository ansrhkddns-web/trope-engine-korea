#!/usr/bin/env python3
"""Check a phase-5 cliche selection portfolio for required ranking signals.

Usage:
  python cliche_portfolio_lint.py path/to/portfolio.md
  python cliche_portfolio_lint.py -
  python cliche_portfolio_lint.py --self-test
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
    Check("brief", ("brief", "브리프", "요청", "primary_genre", "메인 장르"), 2),
    Check("source families", ("source_families", "소스 계열", "reference family", "레퍼런스 계열"), 2),
    Check("candidate pool", ("candidate_count", "후보", "candidate_card", "candidate pool"), 2),
    Check("scoring axes", ("scoring", "점수", "recognition", "genre_fit", "reward_fit", "proof_visibility"), 3),
    Check("weighted verdict", ("percentage", "verdict", "select", "support", "repair", "reject", "판정"), 2),
    Check("portfolio slots", ("portfolio", "포트폴리오", "identity", "advantage", "proof", "witness"), 3),
    Check("cost and renewal", ("cost", "비용", "pressure", "압박", "renewal", "repeat_method", "반복"), 2),
    Check("long term", ("long-term", "long_term", "장기", "50+", "escalation"), 2),
    Check("balance", ("balance", "균형", "missing_roles", "duplicate", "redundancy", "중복"), 2),
    Check("rejected cards", ("rejected", "deferred", "reject", "보류", "탈락"), 1),
    Check("first proof scene", ("first_proof_scene", "1화 증명", "proof_object", "witness", "cost_or_hook"), 3),
    Check("episode loop", ("episodes_1_5", "1-5화", "3-5화", "episode loop", "반복 루프"), 2),
    Check("copy risk", ("copy_risk", "originality", "복사 위험", "고유성", "restricted"), 2),
    Check("repair", ("first_repair", "repair", "수정", "보완", "next_artifact"), 2),
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
    cliche_selection_optimizer:
      brief: hunter support profession portfolio
      primary_genre: hunter/gate
      source_families: trope catalog, motif index, Propp function, progression fantasy
      candidate_count: 18
      scoring:
        recognition: 5
        genre_fit: 5
        reward_fit: 5
        proof_visibility: 5
      selected_portfolio:
        - id: H-01
          role: identity
          cliche: ignored porter analyst
          percentage: 91
          verdict: select
          proof_object: survival report
          witness: association auditor
          cost_or_pressure: guild lawsuit
          repeat_method: audit a new gate
        - id: H-02
          role: advantage
          cliche: monster-route data
          percentage: 88
          verdict: select
        - id: H-03
          role: proof
          cliche: casualty reduction broadcast
          percentage: 90
          verdict: select
      rejected:
        - id: H-09
          reason: duplicate proof
      balance:
        missing_roles: none
        duplicate_risks: rank-test overlap repaired
      first_proof_scene:
        pressure: gate accident
        proof_object: survival report
        witness: association auditor
        cost_or_hook: contract violation notice
      episodes_1_5: 1화 proof, 2화 repeat, 3화 institution, 4화 pressure, 5화 paid hook
      long_term: 50+ national gate logistics escalation
      copy_risk: no named work, no signature sequence
      first_repair: strengthen rival witness
      next_artifact: 1-5 episode brief
    """
    percentage, _, missing = lint(sample)
    if percentage < 85 or missing:
        print(f"self-test failed: score={percentage}, missing={missing}", file=sys.stderr)
        return 1
    print(f"self-test passed: score={percentage}, verdict={verdict(percentage)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint a phase-5 cliche portfolio output.")
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
