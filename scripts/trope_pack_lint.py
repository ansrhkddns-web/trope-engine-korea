#!/usr/bin/env python3
"""Check a Korean webnovel trope-pack markdown for missing planning signals.

Usage:
  python trope_pack_lint.py path/to/pack.md
  python trope_pack_lint.py -
  python trope_pack_lint.py --self-test
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
    Check("reader promise", ("독자 약속", "핵심 약속", "one_line_promise", "Reader promise"), 2),
    Check("genre stack", ("메인 장르", "보조 장르", "genre_stack", "primary", "support"), 1),
    Check("protagonist advantage", ("주인공 우위", "unfair_advantage", "advantage", "우위"), 2),
    Check("first proof scene", ("첫 증명", "1화 증명", "first_proof_scene", "proof scene"), 3),
    Check("proof object", ("증거물", "proof_object", "visible proof", "눈에 보이는 증거"), 2),
    Check("witness reaction", ("목격자", "witness", "주변 반응", "대중 반응"), 2),
    Check("trope cards", ("클리셰 카드", "trope_stack", "approved_cards", "Trope cards"), 1),
    Check("reward loop", ("반복 보상", "reward loop", "reward_ledger", "보상 루프"), 3),
    Check("cost or pressure", ("비용", "압박", "cost", "pressure", "새 압박"), 2),
    Check("escalation", ("1-50", "확장", "escalation", "적대 사다리"), 2),
    Check("product package", ("제목", "로그라인", "태그", "product_package"), 1),
    Check("originality safety", ("고유성", "복사 위험", "originality", "copy_risk"), 1),
    Check("risk and fix", ("위험", "보완", "수정", "risk", "fix"), 1),
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
    missing: list[str] = []
    present: list[str] = []

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
    독자 약속: F급 포터가 감정 능력으로 게이트 물류를 장악한다.
    메인 장르: 헌터
    보조 장르: 지원직/제작
    주인공 우위: 몬스터 부산물의 진짜 용도를 본다.
    1화 증명 장면: 협회 감사 중 폐급 재료가 구조 장비임을 증명한다.
    증거물: 구조 성공률 데이터와 길드 계약서.
    목격자: 협회 감사관과 경쟁 길드 스카우트.
    클리셰 카드: 저평가 지원직, 불가능한 감정, 길드 스카우트.
    반복 보상 루프: 감정 -> 제작/물류 개선 -> 생존률 상승 -> 계약/랭크 상승.
    새 압박: 대형 길드가 증거를 숨기려 한다.
    1-50화 확장: 팀 생존, 길드 의존, 시장 독점, 협회 규제.
    제목 후보: F급 포터는 게이트 물류를 감정한다.
    고유성: 특정 작품 설정을 쓰지 않고 기관과 증거물을 새로 구성한다.
    위험과 보완: 전투 만능화를 늦추고 지원직 보상을 유지한다.
    """
    percentage, _, missing = lint(sample)
    if percentage < 85 or missing:
        print(f"self-test failed: score={percentage}, missing={missing}", file=sys.stderr)
        return 1
    print(f"self-test passed: score={percentage}, verdict={verdict(percentage)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint a trope-engine-korea markdown output.")
    parser.add_argument("path", nargs="?", help="Markdown file to lint, or '-' for stdin.")
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
