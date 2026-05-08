#!/usr/bin/env python3
"""Check a phase-9 quality regression/coherence artifact for required signals.

Usage:
  python cliche_quality_lint.py path/to/quality-audit.md
  python cliche_quality_lint.py -
  python cliche_quality_lint.py --self-test
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
    Check("artifact scope", ("artifact", "artifact under test", "검사 대상", "scope"), 2),
    Check("source families", ("source_families", "소스 계열", "레퍼런스 계열", "narrative coherence", "story-generation", "serial fiction"), 2),
    Check("gate scores", ("gate score", "gate_scores", "release score", "source gate", "promise gate", "게이트"), 3),
    Check("severity", ("severity", "p0", "p1", "p2", "p3", "심각도"), 2),
    Check("cross phase", ("cross-phase", "크로스 페이즈", "phase 2", "phase 3", "phase 4", "phase 5", "phase 6", "phase 7"), 2),
    Check("coherence", ("coherence", "temporal", "causal", "institutional", "reward", "reader_memory", "서사 일관성"), 3),
    Check("inference gaps", ("inference_gaps", "inference gap", "missing_edges", "gap", "추론", "추론 공백"), 2),
    Check("reward debt", ("reward debt", "보상 부채", "open promises", "paid boundary", "debt"), 2),
    Check("originality", ("originality", "copy-shadow", "copy risk", "signature scene", "복사"), 2),
    Check("patch list", ("patch list", "quality_regression_patch", "repair", "expected_effect", "verify_with", "패치 리스트"), 3),
    Check("verdict", ("verdict", "release verdict", "pass", "revise", "rebuild", "판정"), 2),
    Check("next artifact", ("next_artifact", "다음 산출물", "production artifact", "handoff"), 1),
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
    quality_regression_audit:
      artifact under test: serial deployment plan
      source_families: narrative coherence, story-generation evaluation, serial fiction, Korean webnovel research
      gate_scores:
        source gate: 5
        promise gate: 5
        proof gate: 4
        graph gate: 4
      severity:
        - P2 hook rotation is thin
      cross-phase:
        phase 2 synthesis preserved
        phase 3 graph preserved
        phase 4 compiler handoff preserved
        phase 5 portfolio role balance preserved
        phase 6 feedback complaint preserved
        phase 7 deployment reward debt preserved
      narrative_coherence_audit:
        coherence_scores:
          temporal: 5
          causal: 4
          institutional: 4
          reward: 5
          reader_memory: 4
        inference_gaps:
          - gap: institution gap
            repair: define why association audit triggers guild lawsuit
        missing_edges: none
      reward debt:
        open promises: guild lawsuit
        paid boundary: association recognition before lawsuit hook
      originality:
        copy-shadow risk: no named work or signature scene
      patch list:
        quality_regression_patch:
          issue_id: Q9-01
          severity: P2
          gate: serial gate
          repair: rotate episode 3 hook from danger to authority ruling
          expected_effect: less hook monotony
          verify_with: cliche_serial_lint.py
      release verdict: pass
      next_artifact: revised episode brief
    """
    percentage, _, missing = lint(sample)
    if percentage < 85 or missing:
        print(f"self-test failed: score={percentage}, missing={missing}", file=sys.stderr)
        return 1
    print(f"self-test passed: score={percentage}, verdict={verdict(percentage)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint a phase-9 quality regression output.")
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
