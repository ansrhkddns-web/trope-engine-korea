#!/usr/bin/env python3
"""Check a phase-6 reader feedback/fatigue artifact for required signals.

Usage:
  python cliche_feedback_lint.py path/to/feedback.md
  python cliche_feedback_lint.py -
  python cliche_feedback_lint.py --self-test
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
    Check("brief", ("brief", "브리프", "selected portfolio", "선택 포트폴리오", "reader promise"), 2),
    Check("reference families", ("reference families", "레퍼런스 계열", "reader-response", "seriality", "trope"), 2),
    Check("reader cohorts", ("reader cohorts", "독자 코호트", "speed reader", "genre loyalist", "novelty seeker"), 2),
    Check("feedback axes", ("feedback axes", "promise clarity", "first reward visibility", "agency belief", "점수"), 3),
    Check("positive comments", ("positive comments", "좋아할 지점", "긍정 반응", "댓글"), 2),
    Check("complaints", ("complaints", "불만", "이탈", "혼란", "fatigue risk"), 2),
    Check("episode feedback", ("episode feedback", "episodes_1_5", "1-5화", "weak_episode", "반복"), 3),
    Check("paid trust", ("paid trust", "paid-trust", "유료 전환", "payoff", "hook"), 3),
    Check("fatigue repair", ("fatigue_repair", "피로도", "repair_operator", "proof rotation", "witness escalation"), 3),
    Check("copy shadow", ("copy-shadow", "copy risk", "복사 위험", "originality", "signature sequence"), 2),
    Check("revised output", ("revised", "after", "수정 후", "new_proof_object", "new_witness", "new_cost"), 2),
    Check("verdict", ("verdict", "판정", "pass", "revise", "rebuild", "first_repair"), 2),
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
    reader_feedback_calibration:
      brief: hunter support selected portfolio
      selected portfolio: ignored porter analyst, survival report, association auditor
      reader promise: data proves the support class is the real raid brain
      reference families: reader-response theory, seriality, trope catalog, Korean webnovel practice
      reader cohorts:
        speed reader: wants early proof
        genre loyalist: wants clear hunter reward
        novelty seeker: wants new witness and cost
      feedback axes:
        promise clarity: 5
        first reward visibility: 5
        agency belief: 4
      positive comments:
        - 좋아할 지점: 주인공이 직접 생존률을 증명한다
      complaints:
        - fatigue risk: raid report may repeat
        - 이탈: 유료 전환 전에 보상이 없으면 위험
      episode feedback episodes_1_5:
        1화 proof, 2화 repeat, 3화 institution, 4화 weak_episode lawsuit, 5화 paid hook
      paid trust:
        payoff: association recognition
        hook: contract dispute
      fatigue_repair:
        repair_operator: proof rotation and witness escalation
        before: same raid report
        after: public audit hearing
        new_proof_object: casualty audit
        new_witness: association director
        new_cost: guild lawsuit
      copy-shadow risk:
        originality: no named work, no signature sequence
      revised output:
        수정 후: 2화 proof becomes audit hearing
      verdict: pass
      first_repair: strengthen antagonist partial truth
    """
    percentage, _, missing = lint(sample)
    if percentage < 85 or missing:
        print(f"self-test failed: score={percentage}, missing={missing}", file=sys.stderr)
        return 1
    print(f"self-test passed: score={percentage}, verdict={verdict(percentage)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint a phase-6 reader feedback/fatigue output.")
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
