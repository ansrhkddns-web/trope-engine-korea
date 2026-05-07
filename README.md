# Trope Engine Korea

한국형 상업 웹소설의 장르 문법과 클리셰를 **익숙하지만 새롭게** 조립하기 위한 Codex 스킬입니다.

`trope-engine-korea`는 헌터 협회, 게이트, 탑, 시스템, 성좌, 회귀, 재벌, 주식, 부동산, 기업 인수, 사문, 마교, 정파, 기연, 아카데미, 빙의, 지원직, 복수 같은 장르 장치를 단순 아이디어 목록이 아니라 **독자 보상, 성공 클리셰 루프, 1화 증명 장면, 상품 패키지, 장기 연재 엔진**으로 바꿔 줍니다.

## 핵심 기능

- 한국형 웹소설 장르 기본값 설계
- 웹소설 장르 조사값 등록: 판타지, 헌터, 탑/시스템, 회귀, 재벌/현판, 무협, 아카데미, 빙의, 제작/지원직, 로맨스/로판
- 장르별 100종 클리셰 레퍼런스 뱅크 제공
- 다양한 클리셰/모티프/서사 레퍼런스를 기능, 압박, 증거물, 목격자, 비용으로 변환하는 2차 합성 엔진
- 레퍼런스 기반 클리셰를 인식/구조/한국형 웹소설 적합성으로 삼각검증하는 3차 검증 프로토콜
- 클리셰 카드가 실제 연재 그래프로 작동하는지 검사하는 그래프 스트레스 테스트
- 요청별로 필요한 레퍼런스를 고르고 최종 클리셰 엔진으로 조립하는 4차 라우팅/컴파일 파이프라인
- 후보 클리셰를 점수화하고 중복 없는 포트폴리오로 고르는 5차 선택 최적화 엔진
- 익숙한 클리셰를 metric swap, witness swap, cost injection 같은 연산자로 변주
- 헌터/게이트/탑/시스템/성좌/회귀/재벌/무협/아카데미/빙의 계열 클리셰 조합
- 많이 쓰이는 성공 클리셰를 정체성, 우위, 증명, 사회 반응, 갱신, 장기 훅으로 조립
- 익숙한 클리셰를 새롭게 보이게 하는 변주 설계
- TV Tropes식 장치 분류, 민담 모티프/타입 인덱스, Propp/Polti식 서사 기능을 참고한 레퍼런스 기반 클리셰 분해
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
$trope-engine-korea로 웹소설에서 많이 쓰이는 성공 클리셰 6개를 골라 헌터물 콘셉트로 고도화해줘.
```

```text
$trope-engine-korea로 장르별 100종 클리셰 뱅크를 참고해서 회귀+재벌물을 구조화해줘.
```

```text
$trope-engine-korea로 다양한 클리셰 레퍼런스를 참고해서 2차 고도화 카드 그래프를 만들어줘.
```

```text
$trope-engine-korea로 클리셰 레퍼런스 참고 고도화 진행3. 삼각검증과 그래프 스트레스 테스트까지 붙여줘.
```

```text
$trope-engine-korea로 클리셰 레퍼런스 참고 고도화 진행4. 레퍼런스 라우팅과 컴파일 검증까지 붙여줘.
```

```text
$trope-engine-korea로 클리셰 레퍼런스 참고 고도화 진행5. 후보 클리셰 점수화와 포트폴리오 선택까지 해줘.
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
│   ├── cliche-taxonomy-engine.md
│   ├── cliche-remix-operators.md
│   ├── cliche-graph-stress-tests.md
│   ├── cliche-structure-assembly-rules.md
│   ├── default-genre-settings.md
│   ├── diagnostics-rubric.md
│   ├── escalation-ladders.md
│   ├── external-cliche-reference-map.md
│   ├── failure-patterns.md
│   ├── genre-cliche-bank-100-a.md
│   ├── genre-cliche-bank-100-b.md
│   ├── input-assembly-protocol.md
│   ├── market-research-protocol.md
│   ├── mode-playbooks.md
│   ├── originality-safety.md
│   ├── output-templates.md
│   ├── production-handoff.md
│   ├── product-packaging.md
│   ├── reader-response-simulation.md
│   ├── reader-reward-model.md
│   ├── reference-derived-card-bank-3.md
│   ├── reference-backed-card-bank-1.md
│   ├── reference-synthesis-engine-2.md
│   ├── reference-triangulation-protocol-3.md
│   ├── reference-routing-matrix-4.md
│   ├── cliche-selection-optimizer-5.md
│   ├── trope-portfolio-builder-5.md
│   ├── scene-proof-bank.md
│   ├── self-audit-prompts.md
│   ├── successful-cliche-card-bank-2.md
│   ├── successful-webnovel-cliche-patterns.md
│   ├── trope-card-library.md
│   ├── trope-combination-matrix.md
│   ├── trope-engine-schema.md
│   ├── trope-engine-compiler-4.md
│   ├── variation-engine.md
│   └── webnovel-genre-survey-values.md
└── scripts/
    ├── cliche_graph_lint.py
    ├── cliche_engine_compile_lint.py
    ├── cliche_portfolio_lint.py
    ├── genre_bank_count.py
    └── trope_pack_lint.py
```

## 주요 파일 설명

| 파일 | 역할 |
| --- | --- |
| `SKILL.md` | Codex가 실제로 읽는 스킬 본문과 작업 흐름 |
| `references/default-genre-settings.md` | 장르별 기본 설정값과 독자 약속 |
| `references/webnovel-genre-survey-values.md` | 웹소설 장르별 플랫폼/태그 신호, 독자 보상, 세계 엔진, 첫 증명 장면 조사값 |
| `references/genre-cliche-bank-100-a.md` | 판타지, 헌터/게이트, 탑/시스템, 회귀, 재벌/현판 장르별 100종 클리셰 뱅크 |
| `references/genre-cliche-bank-100-b.md` | 무협, 아카데미, 빙의/악역/엑스트라, 제작/지원직, 로맨스/로판 장르별 100종 클리셰 뱅크 |
| `references/cliche-structure-assembly-rules.md` | 100종 리스트를 10카드 엔진, 6역할 성공 스택, 에피소드 루프로 구조화하는 규칙 |
| `references/reference-synthesis-engine-2.md` | 다양한 클리셰/모티프/서사 레퍼런스를 한국형 웹소설 카드로 변환하는 2차 합성 엔진 |
| `references/reference-triangulation-protocol-3.md` | 레퍼런스 파생 클리셰를 인식, 구조, 한국형 웹소설 적합성 기준으로 삼각검증 |
| `references/cliche-graph-stress-tests.md` | 클리셰 그래프의 필수 노드, 인과 엣지, 증거물, 비용, 장기 사다리 점검 |
| `references/reference-routing-matrix-4.md` | 요청 의도, 장르 범위, 레퍼런스 깊이, 산출물, 검증 방식에 따라 읽을 자료를 라우팅 |
| `references/trope-engine-compiler-4.md` | 라우팅된 레퍼런스를 소스 패킷, 카드 풀, 그래프, 1화, 1-5화, 패키지, 검증, 인계까지 컴파일 |
| `references/cliche-selection-optimizer-5.md` | 후보 클리셰를 인식도, 장르 적합도, 보상, 증명성, 주인공 행동성, 비용, 장기성, 고유성으로 점수화 |
| `references/trope-portfolio-builder-5.md` | 점수화한 후보를 6카드, 8카드, 12카드 포트폴리오로 균형 있게 조립 |
| `references/cliche-remix-operators.md` | 익숙한 클리셰를 증거물, 목격자, 비용, 기관, 소유권 등으로 변주하는 연산자 모음 |
| `references/reference-derived-card-bank-3.md` | 기능 카드, 모티프 카드, 그래프 카드로 구성된 3차 레퍼런스 파생 카드 은행 |
| `references/external-cliche-reference-map.md` | 외부 클리셰/모티프/서사 기능 레퍼런스를 스킬용 원칙으로 정리 |
| `references/cliche-taxonomy-engine.md` | 클리셰를 압박, 기능, 모티프, 보상, 목격자, 비용 축으로 분해 |
| `references/reference-backed-card-bank-1.md` | 레퍼런스 기반 1차 클리셰 카드 은행 |
| `references/successful-webnovel-cliche-patterns.md` | 성공한 웹소설에서 자주 쓰이는 클리셰 루프와 진부화 방지 규칙 |
| `references/successful-cliche-card-bank-2.md` | 헌터, 탑/시스템, 회귀/재벌, 무협, 아카데미, 빙의 계열 성공 클리셰 카드 은행 |
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
| `scripts/genre_bank_count.py` | 장르별 클리셰 뱅크가 장르당 100종씩 들어 있는지 검사 |
| `scripts/cliche_graph_lint.py` | 레퍼런스 합성/클리셰 그래프 산출물의 삼각검증, 노드, 엣지, 증거물, 비용 누락 검사 |
| `scripts/cliche_engine_compile_lint.py` | 컴파일된 클리셰 엔진 산출물의 라우팅, 소스 패킷, 카드 풀, 그래프, 검증, 인계 누락 검사 |
| `scripts/cliche_portfolio_lint.py` | 5차 클리셰 포트폴리오 산출물의 후보군, 점수축, 선택 슬롯, 균형, 증명 장면, 수리 지점 누락 검사 |

## 작업 모드

스킬은 요청에 따라 자동으로 작업 모드를 고릅니다.

| 모드 | 하는 일 |
| --- | --- |
| `input assembly` | 애매한 키워드나 거친 아이디어를 장르 엔진으로 조립 |
| `reference synthesis upgrade` | 다양한 외부 레퍼런스를 기능/모티프/그래프 카드로 변환해 스킬 엔진 고도화 |
| `reference triangulation upgrade` | 레퍼런스 파생 클리셰를 삼각검증하고 그래프 스트레스 테스트로 내구성 점검 |
| `reference routing compile` | 요청별 레퍼런스 묶음을 라우팅하고 재사용 가능한 클리셰 엔진으로 컴파일 |
| `reference selection optimize` | 후보 클리셰를 점수화하고 역할 중복 없는 포트폴리오로 선택 |
| `genre reference registration` | 웹소설 장르 조사값과 장르별 100종 클리셰 뱅크를 등록/참조 |
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
| `successful cliche upgrade` | 많이 쓰이고 성공하기 쉬운 클리셰를 6개 역할로 조립해 상업성을 강화 |
| `reference-backed upgrade` | 다양한 클리셰 레퍼런스를 기능 단위로 추출해 카드/엔진을 확장 |

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
- 성공 클리셰가 단순 복제가 아니라 증거물, 목격자, 비용을 가진 루프로 작동하는가?
- 신선한 변주가 이름 바꾸기가 아니라 장면 변화를 만드는가?
- 제목, 로그라인, 태그, 1화가 같은 약속을 파는가?
- 1-5화에서 반복 재미가 증명되는가?
- 50화 이상 확장 가능한 적대 사다리가 있는가?
- 유명작의 고유 설정, 이름, 장면 순서, 규칙을 베끼지 않았는가?

## 성공 클리셰 고도화

많이 쓰이는 클리셰는 그대로 베끼면 낡아 보이지만, **역할**을 나누면 안정적인 연재 엔진이 됩니다.

이 스킬은 성공 클리셰를 다음 6개 역할로 조립합니다.

| 역할 | 기능 |
| --- | --- |
| 정체성 클리셰 | 약자, 지원직, 망한 엑스트라, 숨겨진 후계자처럼 클릭 즉시 알아보이는 출발점 |
| 우위 클리셰 | 회귀, 시스템, 감정, 미래 지식, 숨겨진 클래스처럼 행동을 만드는 힘 |
| 증명 클리셰 | 랭크 테스트, 경매, 구조, 결투, 계약처럼 1화에서 보이는 결과 |
| 사회 반응 클리셰 | 길드 스카우트, 라이벌 인정, 공개 사과, 군중 반전처럼 보상을 키우는 목격자 |
| 갱신 클리셰 | 계약 함정, 숨은 소유권, 타임라인 변화, 기관의 통제처럼 다음 문제를 여는 장치 |
| 장기 클리셰 | 두 번째 회귀자, 후원자 전쟁, 가짜 영웅, 독점 자원처럼 50화 이상 끌고 가는 축 |

핵심 규칙은 간단합니다. **익숙한 약속, 행동 가능한 우위, 눈에 보이는 증명, 새 압박**이 모두 있어야 성공 클리셰가 반복 가능한 엔진이 됩니다.

## 장르별 100종 클리셰 뱅크

이번 버전에는 장르별로 100종씩, 총 1,000개의 클리셰 참조값을 등록했습니다.

| 파일 | 포함 장르 |
| --- | --- |
| `genre-cliche-bank-100-a.md` | 판타지/성장형, 헌터/게이트, 탑/시스템/성좌, 회귀/미래지식, 현판/재벌/금융 |
| `genre-cliche-bank-100-b.md` | 무협/사문/마교, 아카데미/랭킹, 빙의/악역/엑스트라, 제작/지원직/전문직, 로맨스/로판 |

각 항목은 단순 소재가 아니라 `identity`, `advantage`, `proof`, `reaction`, `cost`, `episode`, `antagonist`, `long-term`, `variation`, `hook` 역할로 태그되어 있습니다. 그래서 스킬은 100개를 그대로 나열하는 대신, 필요한 카드만 뽑아 1화 증명 장면과 3-5화 반복 루프로 조립할 수 있습니다.

## 레퍼런스 합성 2차 고도화

이번 버전은 다양한 레퍼런스를 다음 순서로 변환합니다.

```text
레퍼런스 신호 → 서사 기능 → 압박 원천 → 한국형 기관 → 증거물 → 독자 보상 → 갱신 비용
```

예를 들어 외부 레퍼런스의 “금기”, “시험”, “조력자”, “인정 표식”, “추격”, “귀환” 같은 기능은 그대로 쓰지 않고, 헌터 협회, 탑 관리자, 재벌 이사회, 문파 장문인, 아카데미 교수진, 사교계 평판 같은 한국형 웹소설 기관으로 옮겨 씁니다.

새 리믹스 연산자는 이런 문제를 고치기 위해 들어갔습니다.

| 문제 | 쓰는 연산자 예시 |
| --- | --- |
| 너무 익숙함 | metric swap, witness swap, ownership reveal |
| 너무 쉬움 | cost injection, anti-free-power constraint |
| 악역이 멍청함 | competent opposition, antagonist mirror |
| 보상이 사적임 | public procedure, hidden audience |
| 장기 엔진이 약함 | consequence ladder, motif relay |

## 레퍼런스 삼각검증 3차 고도화

3차 고도화는 “좋아 보이는 클리셰”를 바로 채택하지 않고, 다음 세 가지 근거가 모두 있는지 봅니다.

| 검증 축 | 확인하는 것 |
| --- | --- |
| 인식 근거 | 독자가 한 줄만 봐도 어떤 재미인지 알아보는가 |
| 구조 근거 | 시험, 조력, 금기, 추격, 인정, 귀환처럼 반복 가능한 서사 기능이 있는가 |
| 한국형 웹소설 근거 | 협회, 길드, 탑, 시스템, 재벌가, 문파, 아카데미, 사교계 같은 기관에서 장면화되는가 |

또한 클리셰를 카드 목록으로 끝내지 않고 그래프로 점검합니다.

```text
독자 약속 → 압박 → 주인공 행동 → 증거물 → 목격자 반응 → 보상 → 비용 → 다음 압박
```

이 경로에서 빠지는 노드가 있거나, 다음 사건이 앞 사건 때문에 생기지 않으면 `revise` 또는 `rebuild`로 판단합니다.

## 레퍼런스 라우팅 컴파일 4차 고도화

4차 고도화는 스킬이 무조건 모든 레퍼런스를 읽지 않도록, 요청에 맞는 자료 묶음을 먼저 고르게 합니다.

```text
요청 의도 → 장르 범위 → 레퍼런스 깊이 → 산출물 형태 → 검증 방식
```

그다음 선택된 자료만 사용해 다음 구조로 컴파일합니다.

```text
소스 패킷 → 장르 코어 → 독자 계약 → 카드 풀 → 클리셰 그래프 → 1화 증명 → 1-5화 루프 → 장기 확장 → 상품 패키지 → 검증 → 생산 인계
```

이 레이어의 목적은 답변을 더 길게 만드는 것이 아니라, 같은 프로젝트를 여러 번 이어가도 스킬이 “무엇을 근거로, 어떤 카드로, 어떤 검증을 거쳐” 엔진을 만들었는지 잃어버리지 않게 하는 것입니다.

## 클리셰 선택 최적화 5차 고도화

5차 고도화는 후보 클리셰를 많이 뽑은 뒤, 그중 어떤 카드를 실제 기획에 써야 하는지 고르는 선택 엔진입니다.

```text
후보 카드 정규화 → 10개 축 점수화 → 역할 슬롯 선택 → 중복 제거 → 1화/1-5화/50화 훅 검증
```

점수화 기준은 다음처럼 작동합니다.

| 점수축 | 확인하는 것 |
| --- | --- |
| 인식도 | 독자가 한 줄만 봐도 어떤 재미인지 알아보는가 |
| 장르 적합도 | 메인 장르의 클릭 약속을 강화하는가 |
| 보상 적합도 | 힘, 돈, 지위, 복수, 지식, 안전, 관계, 인정 중 하나를 지급하는가 |
| 증명성 | 보상이 숫자, 계약, 랭크, 장면 결과, 목격자로 보이는가 |
| 주인공 행동성 | 우위가 행동과 선택을 만드는가 |
| 비용 무결성 | 성공이 다음 압박을 만드는가 |
| 연재 내구성 | 1-5화 반복과 50화 이상 확장에 쓸 수 있는가 |
| 신선한 압박 | 이름 바꾸기가 아니라 장면 압박을 바꾸는가 |
| 고유성 안전 | 특정 작품의 설정, 규칙, 장면 순서를 베끼지 않는가 |
| 패키지 정렬 | 제목, 로그라인, 태그, 1화가 같은 약속을 파는가 |

최종 결과는 단순 상위 점수표가 아니라 6카드, 8카드, 12카드 포트폴리오로 나옵니다. 예를 들어 8카드 포트폴리오는 `정체성`, `우위`, `1화 증명`, `사회 반응`, `기관 반응`, `비용/적대`, `갱신/반복`, `장기 훅`을 모두 채워야 합니다. 그래서 같은 종류의 랭크 테스트만 여러 개 고르는 문제를 줄이고, 실제 연재에 필요한 역할 균형을 맞춥니다.

## 레퍼런스 기반 업그레이드

이 스킬은 클리셰를 단순히 많이 나열하지 않고, 다음 레퍼런스 계열을 **기능 단위**로 추상화해 사용합니다.

| 레퍼런스 계열 | 스킬에서 쓰는 방식 |
| --- | --- |
| TV Tropes식 장치/관습 분류 | 반복되는 서사 장치를 기능과 독자 인식 신호로 분류 |
| ATU/모티프 인덱스 계열 | 큰 이야기 타입과 작은 모티프를 분리해 카드화 |
| Propp식 민담 기능 | 테스트, 금기, 원조, 투쟁, 인정 같은 순차 기능을 보상 루프로 변환 |
| Polti식 극적 상황 | 복수, 구원, 추격, 반란, 대담한 시도 같은 압박 관계를 장면 갈등으로 변환 |
| 현대 한국형 웹소설 관습 | 회귀, 빙의, 시스템, 탑, 헌터, 무협, 재벌, 지원직 문법으로 현지화 |
| Trope-based story ideation 연구 | 클리셰 카드를 그래프처럼 연결해 반복 가능한 엔진으로 구성 |

참고한 공개 레퍼런스:

- [TV Tropes - Narrative Devices](https://tvtropes.org/pmwiki/pmwiki.php/Main/NarrativeDevices)
- [Harvard Library - Tale-Type and Motif Indices](https://guides.library.harvard.edu/folk_and_myth/indices)
- [University of Washington Libraries - Tale Type & Motif Indexes](https://guides.lib.uw.edu/research/folklore/motif)
- [Propp's Morphology of the Folk Tale](https://www.changingminds.org/disciplines/storytelling/plots/propp/propp.htm)
- [The Thirty-Six Dramatic Situations](https://en.wikipedia.org/wiki/The_Thirty-Six_Dramatic_Situations)
- [TropeTwist: Trope-based Narrative Structure Generation](https://arxiv.org/abs/2204.09672)
- [TaleStream: Supporting Story Ideation with Trope Knowledge](https://arxiv.org/abs/2309.03790)
- [Kishotenketsu / 기승전결 개요](https://en.wikipedia.org/wiki/Kish%C5%8Dtenketsu)
- [웹소설에 나타난 회귀와 환생의 욕망코드](https://scholar.kyobobook.co.kr/article/detail/4010027519081)

성공 클리셰 고도화에서 보조적으로 참고한 공개 장르/태그 자료:

- [WebNovel - Academy Stories](https://www.webnovel.com/tags/academy-novel)
- [LitRPG Vault - LitRPG & Progression Fantasy tags](https://litrpgvault.com/)
- [Royal Road Tracker - genres and popular tags](https://rrtrack.app/genres)
- [Progression fantasy overview](https://en.wikipedia.org/wiki/Progression_fantasy)

이 레퍼런스들은 스킬의 구조를 넓히기 위한 참고 자료입니다. 특정 문장, 장면, 설정, 이름을 복제하지 않고, 기능과 구조만 일반화합니다.

## Lint 스크립트

`scripts/trope_pack_lint.py`는 저장된 마크다운 클리셰 팩에 필수 신호가 들어 있는지 검사합니다. 이번 버전부터 성공 클리셰 루프가 실제로 들어갔는지도 함께 확인합니다.

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

장르별 100종 뱅크 개수 검증:

```bash
python scripts/genre_bank_count.py references/genre-cliche-bank-100-a.md references/genre-cliche-bank-100-b.md
```

클리셰 그래프 검증:

```bash
python scripts/cliche_graph_lint.py --self-test
python scripts/cliche_graph_lint.py path/to/cliche-graph.md
```

컴파일 엔진 검증:

```bash
python scripts/cliche_engine_compile_lint.py --self-test
python scripts/cliche_engine_compile_lint.py path/to/compiled-engine.md
```

클리셰 포트폴리오 검증:

```bash
python scripts/cliche_portfolio_lint.py --self-test
python scripts/cliche_portfolio_lint.py path/to/cliche-portfolio.md
```

이 저장소는 외부 런타임 의존성이 거의 없습니다. `trope_pack_lint.py`, `genre_bank_count.py`, `cliche_graph_lint.py`, `cliche_engine_compile_lint.py`, `cliche_portfolio_lint.py`는 Python 표준 라이브러리만 사용합니다.

## 라이선스

MIT License. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
