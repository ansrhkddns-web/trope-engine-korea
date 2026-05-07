# Trope Engine Korea

한국형 상업 웹소설의 장르 문법과 클리셰를 **익숙하지만 새롭게** 조립하기 위한 Codex 스킬입니다.

`trope-engine-korea`는 헌터 협회, 게이트, 탑, 시스템, 성좌, 회귀, 재벌, 주식, 부동산, 기업 인수, 사문, 마교, 정파, 기연, 아카데미, 빙의, 지원직, 복수 같은 장르 장치를 단순 아이디어 목록이 아니라 **독자 보상, 1화 증명 장면, 상품 패키지, 장기 연재 엔진**으로 바꿔 줍니다.

## 핵심 기능

- 한국형 웹소설 장르 기본값 설계
- 헌터/게이트/탑/시스템/성좌/회귀/재벌/무협/아카데미/빙의 계열 클리셰 조합
- 익숙한 클리셰를 새롭게 보이게 하는 변주 설계
- 1화에서 장르 재미를 증명하는 장면 설계
- 제목, 로그라인, 태그, 소개글, 1-5화 패키지 정렬
- 독자 보상 루프와 보상 부채 관리
- 1-50화 이상 버틸 수 있는 확장 사다리 설계
- 기존 기획안 진단과 수정 처방
- 유명작의 감각을 안전하게 일반화하는 고유성 점검
- 저장된 클리셰 팩의 누락 요소를 검사하는 lint 스크립트 제공

## 이런 요청에 사용합니다

```text
$trope-engine-korea로 헌터+재벌 회귀물 클리셰 팩 만들어줘.
```

```text
$trope-engine-korea로 사문/마교/정파/기연 장치를 익숙하지만 새롭게 변주해줘.
```

```text
$trope-engine-korea로 이 아이디어가 50화 이상 버틸 수 있는지 진단해줘.
```

```text
$trope-engine-korea로 제목, 소개글, 태그, 1-5화 패키지까지 만들어줘.
```

```text
$trope-engine-korea로 유명 헌터물의 쾌감만 일반화해서 복사 위험 없이 새 콘셉트로 바꿔줘.
```

## 설치 방법

Codex가 스킬을 자동으로 발견하려면 이 저장소 폴더를 Codex 스킬 경로에 둡니다.

### Windows PowerShell

```powershell
git clone https://github.com/ansrhkddns-web/trope-engine-korea.git "$env:USERPROFILE\.codex\skills\trope-engine-korea"
```

### macOS / Linux

```bash
git clone https://github.com/ansrhkddns-web/trope-engine-korea.git ~/.codex/skills/trope-engine-korea
```

이미 같은 폴더가 있다면 기존 폴더를 백업하거나 삭제한 뒤 다시 clone하세요.

## 저장소 구조

```text
trope-engine-korea/
├── SKILL.md
├── README.md
├── LICENSE
├── agents/
│   └── openai.yaml
├── references/
│   ├── acceptance-tests.md
│   ├── default-genre-settings.md
│   ├── diagnostics-rubric.md
│   ├── escalation-ladders.md
│   ├── failure-patterns.md
│   ├── input-assembly-protocol.md
│   ├── market-research-protocol.md
│   ├── mode-playbooks.md
│   ├── originality-safety.md
│   ├── output-templates.md
│   ├── production-handoff.md
│   ├── product-packaging.md
│   ├── reader-response-simulation.md
│   ├── reader-reward-model.md
│   ├── scene-proof-bank.md
│   ├── self-audit-prompts.md
│   ├── trope-card-library.md
│   ├── trope-combination-matrix.md
│   ├── trope-engine-schema.md
│   └── variation-engine.md
└── scripts/
    └── trope_pack_lint.py
```

## 주요 파일 설명

| 파일 | 역할 |
| --- | --- |
| `SKILL.md` | Codex가 실제로 읽는 스킬 본문과 작업 흐름 |
| `references/default-genre-settings.md` | 장르별 기본 설정값과 독자 약속 |
| `references/trope-card-library.md` | 클리셰 카드 모음 |
| `references/variation-engine.md` | 익숙한 장치를 새롭게 바꾸는 변주 규칙 |
| `references/reader-reward-model.md` | 독자 보상, 보상 부채, 유료 전환 신뢰 |
| `references/scene-proof-bank.md` | 1화 증명 장면 설계 |
| `references/product-packaging.md` | 제목, 로그라인, 태그, 소개글, 1-5화 패키지 |
| `references/escalation-ladders.md` | 1화부터 50화 이후까지 확장 사다리 |
| `references/trope-engine-schema.md` | 계속 이어 쓸 수 있는 표준 기획 스키마 |
| `references/diagnostics-rubric.md` | 기획안 점수화와 수정 처방 |
| `references/acceptance-tests.md` | 10초 이해, 첫 장면, 1-5화, 유료 전환, 고유성 테스트 |
| `references/originality-safety.md` | 유명작 참고 시 복사 위험을 피하는 일반화 규칙 |
| `references/production-handoff.md` | 작품 바이블, 로드맵, 에피소드 브리프로 넘기는 인계 규칙 |
| `scripts/trope_pack_lint.py` | 저장된 결과물의 필수 요소 누락 검사 |

## 작업 모드

스킬은 요청에 따라 자동으로 작업 모드를 고릅니다.

| 모드 | 하는 일 |
| --- | --- |
| `input assembly` | 애매한 키워드나 거친 아이디어를 장르 엔진으로 조립 |
| `trope pack` | 클리셰 카드, 보상, 변주, 첫 증명 장면 생성 |
| `familiar-but-fresh premise` | 익숙한 장르 장치를 새 콘셉트로 변주 |
| `proof scene` | 추상적인 클리셰를 1화 장면으로 변환 |
| `product package` | 제목, 로그라인, 태그, 소개글, 1-5화 흐름 정렬 |
| `escalation map` | 1-50화 이상 확장 가능한 연재 구조 설계 |
| `diagnosis` | 기존 기획안의 약점 진단과 수정 처방 |
| `reader response` | 독자 반응, 댓글 포인트, 이탈 위험 예측 |
| `originality safety` | 유명작 참고 요소를 복사 위험 없이 일반화 |
| `production handoff` | 다음 산출물로 넘길 작업 지시서 생성 |
| `acceptance test` | 기획이 실제로 준비됐는지 테스트 |

## 결과물 예시

요청:

```text
$trope-engine-korea로 헌터+지원직+회귀 조합을 익숙하지만 새롭게 만들어줘.
```

예상 출력 범위:

- 독자 약속
- 메인 장르와 보조 장르
- 주인공 우위
- 첫 증명 장면
- 사용할 클리셰 카드
- 신선한 변주
- 반복 보상 루프
- 1-5화 보상 흐름
- 50화 이상 확장 방향
- 제목/로그라인 방향
- 위험과 보완

## 품질 기준

이 스킬은 결과물을 만들 때 다음 질문을 통과해야 합니다.

- 장르가 첫 장면 또는 한 줄 콘셉트에서 바로 보이는가?
- 주인공의 우위가 행동을 만드는가?
- 첫 보상이 다른 인물에게도 보이는가?
- 클리셰가 독자 보상을 실제로 지급하는가?
- 신선한 변주가 이름 바꾸기가 아니라 장면 변화를 만드는가?
- 제목, 로그라인, 태그, 1화가 같은 약속을 파는가?
- 1-5화에서 반복 재미가 증명되는가?
- 50화 이상 확장 가능한 적대 사다리가 있는가?
- 유명작의 고유 설정, 이름, 장면 순서, 규칙을 베끼지 않았는가?

## Lint 스크립트

`scripts/trope_pack_lint.py`는 저장된 마크다운 클리셰 팩에 필수 신호가 들어 있는지 검사합니다.

자체 테스트:

```bash
python scripts/trope_pack_lint.py --self-test
```

파일 검사:

```bash
python scripts/trope_pack_lint.py path/to/trope-pack.md
```

표준 입력 검사:

```bash
cat trope-pack.md | python scripts/trope_pack_lint.py -
```

검사 결과는 `pass`, `revise`, `rebuild`로 나옵니다. 이 검사는 문학적 완성도를 평가하는 도구가 아니라, **필수 기획 요소가 빠졌는지 확인하는 보조 도구**입니다.

## 최신 시장 조사 주의

플랫폼 랭킹, 최신 유행, 현재 공모전 경향처럼 시간이 지나면 바뀌는 정보는 스킬 내부 지식만으로 단정하지 않습니다.

그런 요청이 들어오면 `references/market-research-protocol.md`에 따라 현재 자료를 조사한 뒤, 관찰된 패턴을 장르 문법으로 일반화해야 합니다.

## 고유성 안전 원칙

이 스킬은 특정 작품의 고유한 설정, 이름, 장면, 규칙을 복제하기 위한 도구가 아닙니다.

허용되는 것:

- 장르 문법 일반화
- 독자 보상 구조 분석
- 익숙한 클리셰의 기능 추출
- 새로운 기관, 증거물, 장면 순서, 비용으로 재구성

피해야 하는 것:

- 유명작 고유 명칭 재사용
- 특정 작품의 튜토리얼/게이트/탑 규칙 복제
- 같은 오프닝 사건 순서 반복
- 캐릭터 관계와 역할 배치 복사

## 개발 및 검증

스킬 기본 검증:

```bash
python path/to/skill-creator/scripts/quick_validate.py .
```

lint 스크립트 자체 검증:

```bash
python scripts/trope_pack_lint.py --self-test
```

이 저장소는 외부 런타임 의존성이 거의 없습니다. `trope_pack_lint.py`는 Python 표준 라이브러리만 사용합니다.

## 라이선스

MIT License. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
