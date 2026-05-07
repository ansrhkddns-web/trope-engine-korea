#!/usr/bin/env python3
"""Check a phase-7 serial arc deployment artifact for required signals.

Usage:
  python cliche_serial_lint.py path/to/serial-plan.md
  python cliche_serial_lint.py -
  python cliche_serial_lint.py --self-test
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
    Check("brief and engine", ("brief", "브리프", "selected_engine", "선택 엔진", "core_reader_promise"), 2),
    Check("source families", ("source_families", "소스 계열", "serial fiction", "narrative planning", "cliffhanger"), 2),
    Check("deployment horizon", ("deployment_horizon", "배치 범위", "1-5", "6-25", "26-50"), 2),
    Check("episode jobs", ("episode_jobs", "에피소드 job", "episode", "pressure", "protagonist_method"), 3),
    Check("cliche cards", ("cliche_cards", "클리셰 카드", "proof_object", "witness", "reward_paid"), 3),
    Check("reward debt", ("reward_debt", "보상 부채", "open_debts", "paid_debts", "next_debt_to_pay"), 3),
    Check("hook cadence", ("hook_cadence", "훅", "payoff_before_hook", "hook_rotation", "paid boundary"), 3),
    Check("arc segments", ("arc_segments", "아크", "6-25", "26-50", "institution_shift", "antagonist_move"), 2),
    Check("causal continuity", ("because", "therefore", "causal", "인과", "continuity_anchors"), 2),
    Check("feedback checkpoints", ("feedback_checkpoints", "피드백 체크포인트", "repair_if_weak", "fatigue_guard"), 2),
    Check("restricted cards", ("restricted_cards", "금지", "copy", "copy-shadow", "복사"), 1),
    Check("validation", ("validation", "verdict", "판정", "first_repair", "next_artifact"), 2),
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
    serial_arc_deployment:
      brief: hunter support 1-50 deployment
      selected_engine: ignored porter analyst engine
      core_reader_promise: support class proves raid value through survival data
      source_families: serial fiction, cliffhanger research, narrative planning, Korean webnovel form
      deployment_horizon: 1-5, 6-25, 26-50
      episode_jobs:
        - episode: 1
          job: promise proof
          cliche_cards: identity, advantage, first proof
          pressure: gate accident
          protagonist_method: survival route analysis
          proof_object: casualty report
          witness: association auditor
          reward_paid: public recognition
          reward_debt_opened: guild lawsuit
          hook_type: consequence hook
          fatigue_guard: no repeated rank test
      arc_segments:
        - range: 6-25
          institution_shift: association adopts audit metric
          antagonist_move: guild counters with partial truth
        - range: 26-50
          institution_shift: national disaster board
          antagonist_move: illegal gate cartel
      reward_debt_ledger:
        open_debts:
          - id: D1
            type: justice
            next_debt_to_pay: guild lawsuit
        paid_debts:
          - id: P1
            visible_payoff: association recognition
        reward_debt_summary:
          next_debt_to_pay: contract dispute
      hook_cadence:
        payoff_before_hook: yes
        hook_rotation: consequence, authority, metric
        paid boundary: recognition before lawsuit
      continuity_anchors:
        because: proof causes audit
        therefore: audit causes lawsuit
        restricted_cards: named work copy
      feedback_checkpoints:
        - episode: 5
          repair_if_weak: pay one more proof debt
      validation:
        verdict: pass
        first_repair: rotate episode 2 proof object
        next_artifact: 1-25 episode brief
    """
    percentage, _, missing = lint(sample)
    if percentage < 85 or missing:
        print(f"self-test failed: score={percentage}, missing={missing}", file=sys.stderr)
        return 1
    print(f"self-test passed: score={percentage}, verdict={verdict(percentage)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint a phase-7 serial deployment output.")
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
