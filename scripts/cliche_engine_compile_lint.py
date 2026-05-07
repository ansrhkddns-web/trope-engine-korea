#!/usr/bin/env python3
"""Check a compiled trope engine markdown/YAML-ish output for required signals.

Usage:
  python cliche_engine_compile_lint.py path/to/compiled-engine.md
  python cliche_engine_compile_lint.py -
  python cliche_engine_compile_lint.py --self-test
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
    Check("route", ("라우팅", "route", "user_intent", "reference_depth", "output_artifact"), 2),
    Check("source packet", ("소스 패킷", "source_packet", "stable_structure", "stable_genre", "research_signal"), 2),
    Check("genre core", ("장르 코어", "genre_core", "primary", "support", "first_click_owner"), 2),
    Check("reader contract", ("독자 약속", "reader_contract", "one_line_promise", "reward_channels"), 3),
    Check("card pool", ("카드 풀", "card_pool", "identity", "advantage", "proof", "witness"), 2),
    Check("normalized cards", ("정규화", "normalized_cards", "recognition_signal", "proof_object", "cost_or_pressure"), 2),
    Check("cliche graph", ("클리셰 그래프", "cliche_graph", "nodes", "edges", "weakest_edge"), 3),
    Check("first proof scene", ("1화 증명", "first_proof_scene", "pressure", "proof_object", "cost_or_hook"), 3),
    Check("episode loop", ("1-5화", "episodes_1_5", "3-5화", "반복 루프"), 2),
    Check("escalation", ("장기 확장", "escalation", "institution", "region_or_nation", "hidden_world_or_system"), 2),
    Check("package", ("상품 패키지", "package", "title_direction", "logline", "paid_boundary"), 2),
    Check("validation", ("검증 판정", "validation", "acceptance_verdict", "graph_verdict", "first_repair"), 3),
    Check("handoff", ("생산 인계", "handoff", "next_artifact", "non_negotiable_promise"), 2),
    Check("copy risk", ("복사 위험", "copy_risk", "originality", "restricted_cards"), 1),
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
    라우팅 결과 route:
      user_intent: phase-4 compiled engine
      reference_depth: compiled
      output_artifact: trope engine
    소스 패킷 source_packet:
      stable_structure: Propp, motif, graph stress
      stable_genre: hunter gate
      research_signal: Korean webnovel motif research
      copy_risk: no named works
    장르 코어 genre_core:
      primary: hunter
      support: finance
      first_click_owner: gate proof
    독자 약속 reader_contract:
      one_line_promise: F급 포터가 생존 데이터로 게이트 산업을 뒤집는다
      reward_channels: status, money, recognition
    카드 풀 card_pool:
      identity: F급 포터
      advantage: 생존 데이터
      proof: 구조 성공률 보고서
      witness: 협회 감사관
    정규화 normalized_cards:
      recognition_signal: F급 underdog
      proof_object: 보고서와 영상
      cost_or_pressure: 기존 길드의 소송
    클리셰 그래프 cliche_graph:
      nodes: promise, advantage, proof object, witness, cost
      edges: proof measures witness, reward causes cost
      weakest_edge: market reaction
    1화 증명 first_proof_scene:
      pressure: 게이트 사고
      proof_object: 구조 영상
      cost_or_hook: 계약 위반 소송
    1-5화 episodes_1_5 반복 루프:
      1화 proof, 2화 audit, 3화 scout, 4화 lawsuit, 5화 paid boundary
    장기 확장 escalation:
      institution: 협회
      region_or_nation: 국가 재난청
      hidden_world_or_system: 게이트 원인
    상품 패키지 package:
      title_direction: F급 포터는 생존률을 감정한다
      logline: 생존 데이터로 게이트 산업을 재평가한다
      paid_boundary: 스카우트 제안 후 소송장
    검증 판정 validation:
      acceptance_verdict: pass
      graph_verdict: pass
      first_repair: market reaction 강화
    생산 인계 handoff:
      next_artifact: 1-5화 상세 시드
      non_negotiable_promise: 데이터로 인정받는 지원직
      restricted_cards: named work copy
    """
    percentage, _, missing = lint(sample)
    if percentage < 85 or missing:
        print(f"self-test failed: score={percentage}, missing={missing}", file=sys.stderr)
        return 1
    print(f"self-test passed: score={percentage}, verdict={verdict(percentage)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint a compiled trope engine output.")
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
