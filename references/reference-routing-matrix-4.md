# Reference Routing Matrix 4

Use this file for phase-4 upgrades and for any request where the skill must decide which reference resources to load before building a trope engine.

The goal is to stop overloading every answer with every reference. Route the request to the smallest useful reference packet, then compile the result with `trope-engine-compiler-4.md`.

## Routing Principle

Every request should be routed by:

1. **Intent**: what the user wants done.
2. **Genre scope**: one genre, cross-genre, or genre-wide.
3. **Reference depth**: default, 100-bank, synthesis, triangulation, or market-current.
4. **Output artifact**: trope pack, graph, bible insert, episode ladder, package, diagnosis, compiled engine, ranked portfolio, reader feedback calibration, serial deployment plan, or quality regression audit.
5. **Verification need**: none, lint, triangulation, graph stress test, portfolio lint, feedback lint, serial lint, quality lint, or market check.

## Intent Router

| User signal | Route | Load first | Add if needed | Verify with |
| --- | --- | --- | --- | --- |
| "빠르게 아이디어" | quick pack | `default-genre-settings.md`, `trope-card-library.md` | `reader-reward-model.md` | none |
| "장르 기본값" | genre defaults | `webnovel-genre-survey-values.md`, `default-genre-settings.md` | `output-templates.md` | none |
| "장르별 100종" | 100-bank selection | `genre-cliche-bank-100-a.md` or `genre-cliche-bank-100-b.md` | `cliche-structure-assembly-rules.md` | `genre_bank_count.py` when editing banks |
| "다양한 레퍼런스" | reference-backed | `external-cliche-reference-map.md`, `cliche-taxonomy-engine.md` | `reference-backed-card-bank-1.md` | originality check |
| "고도화 진행2" | synthesis | `reference-synthesis-engine-2.md`, `cliche-remix-operators.md` | `reference-derived-card-bank-3.md` | reference synthesis test |
| "고도화 진행3" | triangulation | `reference-triangulation-protocol-3.md`, `cliche-graph-stress-tests.md` | `cliche_graph_lint.py` | graph lint |
| "고도화 진행4" | routed compiler | `reference-routing-matrix-4.md`, `trope-engine-compiler-4.md` | all routed files | `cliche_engine_compile_lint.py` |
| "고도화 진행5" | selection optimizer | `cliche-selection-optimizer-5.md`, `trope-portfolio-builder-5.md` | routed genre banks, `trope-engine-compiler-4.md` | `cliche_portfolio_lint.py` |
| "고도화 진행6" | feedback calibrator | `reader-feedback-calibrator-6.md`, `cliche-fatigue-repair-loop-6.md` | selected portfolio, `reader-response-simulation.md`, `acceptance-tests.md` | `cliche_feedback_lint.py` |
| "고도화 진행7" | serial deployment | `serial-arc-deployment-planner-7.md`, `reward-debt-ledger-7.md` | selected engine, feedback calibration, `production-handoff.md` | `cliche_serial_lint.py` |
| "고도화 진행9" | quality regression | `cliche-quality-regression-suite-9.md`, `narrative-coherence-audit-9.md` | previous phase artifact, `acceptance-tests.md` | `cliche_quality_lint.py` |
| "성공한/잘 먹히는" | success cliche | `successful-webnovel-cliche-patterns.md`, `successful-cliche-card-bank-2.md` | `scene-proof-bank.md` | acceptance tests |
| "1화 장면" | proof scene | `scene-proof-bank.md` | `reader-reward-model.md` | first-scene test |
| "50화/장기연재" | escalation | `escalation-ladders.md` | `cliche-graph-stress-tests.md` | 50-episode test |
| "제목/태그/소개글" | product package | `product-packaging.md` | `reader-reward-model.md`, `scene-proof-bank.md` | package alignment |
| "진단" | diagnosis | `diagnostics-rubric.md`, `failure-patterns.md` | `acceptance-tests.md` | pass/revise/rebuild |
| "최신/요즘/랭킹" | market-current | `market-research-protocol.md` | web research, then stable references | cite dated sources |

## Genre-to-Bank Router

| Genre signal | Load |
| --- | --- |
| fantasy, progression, 판타지, 성장형 | `genre-cliche-bank-100-a.md` G01 |
| hunter, gate, raid, 헌터, 게이트, 던전 | `genre-cliche-bank-100-a.md` G02 |
| tower, system, constellation, 탑, 시스템, 성좌 | `genre-cliche-bank-100-a.md` G03 |
| regression, future knowledge, 회귀, 미래지식 | `genre-cliche-bank-100-a.md` G04 |
| chaebol, stocks, finance, real estate, 재벌, 주식, 부동산 | `genre-cliche-bank-100-a.md` G05 |
| martial arts, murim, sect, 무협, 사문, 마교, 정파 | `genre-cliche-bank-100-b.md` G06 |
| academy, ranking, school, 아카데미, 랭킹 | `genre-cliche-bank-100-b.md` G07 |
| possession, reincarnation, villain, extra, 빙의, 환생, 악역, 엑스트라 | `genre-cliche-bank-100-b.md` G08 |
| production, support, profession, 제작, 지원직, 전문직 | `genre-cliche-bank-100-b.md` G09 |
| romance, rofan, BL-adjacent, 로맨스, 로판, 관계 | `genre-cliche-bank-100-b.md` G10 |

## Reference Depth Levels

### Level 0: Direct Answer

Use for tiny requests. No extra reference unless needed.

### Level 1: Genre Defaults

Use when the request needs recognizable genre grammar.

Load:

- `default-genre-settings.md`
- `webnovel-genre-survey-values.md`

### Level 2: Bank Selection

Use when the request needs many cliche options or genre-specific card variety.

Load:

- relevant 100-bank file;
- `cliche-structure-assembly-rules.md`.

### Level 3: Reference Synthesis

Use when the user asks for broad references, freshness, or phase 2.

Load:

- `reference-synthesis-engine-2.md`;
- `cliche-remix-operators.md`;
- `reference-derived-card-bank-3.md`.

### Level 4: Triangulated Graph

Use when reliability, durability, or phase 3 is requested.

Load:

- `reference-triangulation-protocol-3.md`;
- `cliche-graph-stress-tests.md`.

### Level 5: Compiled Engine

Use when phase 4, reusable project work, bible-ready outputs, or end-to-end packaging is requested.

Load:

- this file;
- `trope-engine-compiler-4.md`;
- the routed genre/reference files;
- `acceptance-tests.md`;
- `production-handoff.md`.

### Level 6: Ranked Portfolio

Use when phase 5, best-card selection, ranked candidates, portfolio balance, or redundancy reduction is requested.

Load:

- `cliche-selection-optimizer-5.md`;
- `trope-portfolio-builder-5.md`;
- routed genre/reference banks;
- `acceptance-tests.md`.

### Level 7: Reader Feedback Calibration

Use when phase 6, reader comments, retention risk, fatigue, paid-trust, or response repair is requested.

Load:

- `reader-feedback-calibrator-6.md`;
- `cliche-fatigue-repair-loop-6.md`;
- selected portfolio or compiled engine reference;
- `acceptance-tests.md`;
- `reader-response-simulation.md` when the user wants more comment detail.

### Level 8: Serial Deployment

Use when phase 7, episode operation, arc deployment, reward debt, hook cadence, or 1-50 cliche placement is requested.

Load:

- `serial-arc-deployment-planner-7.md`;
- `reward-debt-ledger-7.md`;
- selected compiled engine, portfolio, or feedback artifact when available;
- `production-handoff.md`;
- `acceptance-tests.md`.

### Level 9: Quality Regression

Use when phase 9, release gate, post-deployment audit, narrative coherence, cross-phase preservation, or output QA is requested.

Load:

- `cliche-quality-regression-suite-9.md`;
- `narrative-coherence-audit-9.md`;
- previous compiled engine, portfolio, feedback, or deployment artifact when available;
- `acceptance-tests.md`;
- `cliche_quality_lint.py` when validating a saved artifact.

## Source Reliability Tags

Use these tags when explaining source status:

- **stable-structure**: Propp, motif, dramatic situations, story structure, cliche graph logic.
- **stable-genre**: recurring webnovel genre grammar and long-lived platform categories.
- **platform-current**: live rankings, newest tags, current market claims; browse first.
- **research-signal**: academic or semi-academic analysis; useful but must be localized.
- **community-signal**: forum/tag discussions; useful for reader vocabulary, not proof of quality.
- **copy-risk**: a named work, proprietary rule, or distinctive scene sequence; abstract before use.

## Routing Output

When phase-4 routing is visible to the user, show:

- **요청 의도**:
- **장르 범위**:
- **레퍼런스 깊이**:
- **읽을 파일 묶음**:
- **산출물 형태**:
- **검증 방식**:
- **주의할 복사 위험**:

Do not expose this routing for short creative requests unless it helps the user understand the work.
