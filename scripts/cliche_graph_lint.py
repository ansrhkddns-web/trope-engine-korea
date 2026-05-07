#!/usr/bin/env python3
"""Check a cliche graph markdown output for required engine signals.

Usage:
  python cliche_graph_lint.py path/to/graph.md
  python cliche_graph_lint.py -
  python cliche_graph_lint.py --self-test
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
    Check("reference triangulation", ("삼각검증", "triangulation", "recognition support", "structure support", "localization support"), 3),
    Check("graph nodes", ("노드", "node", "promise node", "proof object node", "witness node"), 2),
    Check("graph edges", ("엣지", "edge", "causes", "reveals", "measures", "escalates"), 2),
    Check("reader promise", ("독자 약속", "핵심 약속", "promise"), 2),
    Check("protagonist agency", ("주인공 행동", "protagonist action", "agency", "선택"), 2),
    Check("proof object", ("증거물", "proof object", "visible proof", "눈에 보이는 증거"), 3),
    Check("witness or institution", ("목격자", "witness", "기관", "institution"), 3),
    Check("reward", ("보상", "reward", "payoff"), 2),
    Check("cost or pressure", ("비용", "압박", "cost", "pressure", "새 압박"), 3),
    Check("antagonist or mirror", ("적대자", "antagonist", "mirror", "라이벌"), 1),
    Check("episode loop", ("3-5화", "episode loop", "반복 루프", "5-beat"), 2),
    Check("remix operator", ("연산자", "operator", "metric swap", "cost injection", "witness swap"), 1),
    Check("copy risk", ("복사 위험", "copy risk", "originality", "고유성"), 2),
    Check("graph verdict", ("graph verdict", "그래프 판정", "pass", "revise", "rebuild"), 1),
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
    그래프 판정: pass
    삼각검증: recognition support는 헌터/게이트 태그, structure support는 donor test,
    localization support는 헌터 협회 재검정이다.
    독자 약속: F급 포터가 생존 데이터를 증명해 랭크와 지위를 올린다.
    노드: promise node, advantage node, proof object node, witness node, institution node, cost node.
    엣지: proof object measures witness reaction, reward causes cost, cost escalates next pressure.
    주인공 행동: 계약을 거절하고 구조 데이터를 제출한다.
    증거물: 구조 성공률 보고서와 게이트 영상.
    목격자/기관: 협회 감사관과 경쟁 길드 스카우트.
    보상: 재검정과 스카우트 제안.
    비용/새 압박: 기존 길드가 계약 위반 소송을 건다.
    적대자: 구식 전투 기여도만 믿는 길드장이 mirror 역할을 한다.
    적용 연산자: metric swap, cost injection.
    3-5화 반복 루프: 감사 -> 구조 -> 보고서 -> 스카우트 -> 소송.
    복사 위험: 특정 작품의 게이트 규칙과 장면 순서를 쓰지 않는다.
    """
    percentage, _, missing = lint(sample)
    if percentage < 85 or missing:
        print(f"self-test failed: score={percentage}, missing={missing}", file=sys.stderr)
        return 1
    print(f"self-test passed: score={percentage}, verdict={verdict(percentage)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint a cliche graph markdown output.")
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
