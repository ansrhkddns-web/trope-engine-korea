# Mode Playbooks

Use this file when deciding how to run the skill for a specific user request. It keeps the skill from loading too many references or producing a mismatched output.

## Mode Selection

| User request | Primary mode | Load first | Optional add-ons |
| --- | --- | --- | --- |
| "헌터+회귀 클리셰 팩" | trope pack | `default-genre-settings.md`, `trope-card-library.md` | `reader-reward-model.md`, `variation-engine.md` |
| "익숙하지만 새롭게" | freshness pass | `variation-engine.md` | `scene-proof-bank.md`, `failure-patterns.md` |
| "이 아이디어 진단" | diagnosis | `diagnostics-rubric.md` | `failure-patterns.md`, `reader-response-simulation.md` |
| "제목/소개글/태그" | product package | `product-packaging.md` | `scene-proof-bank.md`, `reader-reward-model.md` |
| "1화 장면" | proof scene | `scene-proof-bank.md` | `reader-reward-model.md`, `episode-hook-designer` if episode hooks dominate |
| "50화까지" | escalation map | `escalation-ladders.md` | `trope-engine-schema.md`, `production-handoff.md` |
| "바이블로 정리" | structured spec | `trope-engine-schema.md` | `production-handoff.md`, `output-templates.md` |
| "독자 반응" | reader response | `reader-response-simulation.md` | `diagnostics-rubric.md`, `product-packaging.md` |
| "유명작 느낌" | originality safety | `originality-safety.md` | `variation-engine.md`, `scene-proof-bank.md` |
| "요즘 잘 먹히는" | market reference | `market-research-protocol.md` | current web research, then stable references |
| "장르 조사값/장르별 100종 클리셰 등록" | genre reference registration | `webnovel-genre-survey-values.md`, `genre-cliche-bank-100-a.md`, `genre-cliche-bank-100-b.md` | `cliche-structure-assembly-rules.md`, `external-cliche-reference-map.md` |
| "클리셰 레퍼런스 참고 고도화 진행2" | reference synthesis upgrade | `reference-synthesis-engine-2.md`, `cliche-remix-operators.md`, `reference-derived-card-bank-3.md` | `external-cliche-reference-map.md`, `cliche-taxonomy-engine.md`, `scene-proof-bank.md` |
| "클리셰 레퍼런스 참고 고도화 진행3" | reference triangulation upgrade | `reference-triangulation-protocol-3.md`, `cliche-graph-stress-tests.md` | `reference-synthesis-engine-2.md`, `cliche-remix-operators.md`, `reference-derived-card-bank-3.md` |
| "클리셰 레퍼런스 참고 고도화 진행4" | reference routing compile | `reference-routing-matrix-4.md`, `trope-engine-compiler-4.md` | routed references, `acceptance-tests.md`, `production-handoff.md` |
| "클리셰 레퍼런스 참고 고도화 진행5" | reference selection optimize | `cliche-selection-optimizer-5.md`, `trope-portfolio-builder-5.md` | `reference-routing-matrix-4.md`, `trope-engine-compiler-4.md`, `acceptance-tests.md` |
| "클리셰 레퍼런스 참고 고도화 진행6" | reader feedback calibrate | `reader-feedback-calibrator-6.md`, `cliche-fatigue-repair-loop-6.md` | `reader-response-simulation.md`, `acceptance-tests.md`, `failure-patterns.md` |
| "많이 쓰이는/성공한 클리셰" | successful cliche upgrade | `successful-webnovel-cliche-patterns.md`, `successful-cliche-card-bank-2.md` | `reader-reward-model.md`, `scene-proof-bank.md`, `variation-engine.md` |
| "다양한 클리셰 레퍼런스 참고" | reference-backed upgrade | `external-cliche-reference-map.md`, `cliche-taxonomy-engine.md` | `reference-backed-card-bank-1.md`, `originality-safety.md` |

## Output Size Rules

- For quick ideation, use 5-8 sections, not a full bible.
- For a complete concept, include first proof, reward loop, cliche stack, and 1-5 episode path.
- For a bible or long-running plan, include the standard schema and production handoff.
- For diagnosis, lead with judgment and fixes, then details.
- For packaging, do not overload with lore; show title promise, logline, tags, and first 5 episodes.

## Reference Loading Rules

- Do not read every reference for normal requests.
- Load `output-templates.md` only when the final structure matters.
- Load `trope-engine-schema.md` only when continuity or reuse matters.
- Load `market-research-protocol.md` only for current trends or platform-specific requests.
- Load `webnovel-genre-survey-values.md` before the 100-item banks when the user asks for genre-wide research values.
- Load only the relevant half of the 100-item bank when the user names a genre: A for fantasy/hunter/tower/regression/finance, B for martial arts/academy/possession/support/romance.
- Load `cliche-structure-assembly-rules.md` whenever the user asks to structure or combine cliches from the banks.
- Load `reference-synthesis-engine-2.md`, `cliche-remix-operators.md`, and `reference-derived-card-bank-3.md` for a second or deeper upgrade based on diverse trope/motif/story references.
- Load `reference-triangulation-protocol-3.md` and `cliche-graph-stress-tests.md` when the user asks for phase 3, graph verification, stress testing, or deeper engine validation.
- Load `reference-routing-matrix-4.md` and `trope-engine-compiler-4.md` when the user asks for phase 4, compiled engines, routing, reusable packaging, or end-to-end reference selection.
- Load `cliche-selection-optimizer-5.md` and `trope-portfolio-builder-5.md` when the user asks for phase 5, candidate ranking, best cliche selection, portfolio balance, score-based repair, or reducing redundant cliche stacks.
- Load `reader-feedback-calibrator-6.md` and `cliche-fatigue-repair-loop-6.md` when the user asks for phase 6, reader comments, retention risk, fatigue repair, paid-trust risk, or episode-level response calibration.
- Load `successful-webnovel-cliche-patterns.md` and `successful-cliche-card-bank-2.md` when the user asks for common, successful, proven, widely used, or commercially reliable webnovel cliches without needing live rankings.
- Load `originality-safety.md` whenever a named reference work appears.
- Load `failure-patterns.md` when the result feels generic, bloated, too easy, or not serializable.

## Mode Playbooks

### Quick Trope Pack

Use when the user wants ideas fast.

Steps:

1. Pick primary and support genre.
2. State reader promise.
3. Select 5 cliche cards.
4. Give one fresh variation for each.
5. Build one first proof scene.
6. Add repeatable reward loop and risk/fix.

Avoid:

- long market explanation;
- 50-episode roadmap unless requested;
- too many named institutions.

### Reference-Backed Upgrade

Use when the user asks to improve the engine using many cliche references.

Steps:

1. Identify reference families: trope catalog, motif index, plot function, dramatic situation, Korean webnovel practice.
2. Extract functions, not names.
3. Convert each function into cliche taxonomy fields.
4. Add or select cards from the reference-backed card bank.
5. Connect cards to proof scenes and reward loops.
6. Record source-inspired principles without copying examples.

Avoid:

- quoting or reproducing external trope page content;
- adding cards that cannot be staged;
- using external references without Korean webnovel localization.

### Reference Synthesis Upgrade

Use when the user asks for a continued or second upgrade from diverse cliche references.

Steps:

1. Identify the reference families being used: trope catalog, motif index, Propp-like function, dramatic situation, kishotenketsu/giseungjeongyeol, progression fantasy, Korean regression/reincarnation/possession, and trope-graph research.
2. Extract each reference through the seven-step schema in `reference-synthesis-engine-2.md`.
3. Select 6-10 cards from `reference-derived-card-bank-3.md`.
4. Apply 1-3 operators from `cliche-remix-operators.md` to make familiar cards less stale.
5. Connect selected cards as a graph: reward -> witness -> institution -> cost -> antagonist -> hook.
6. Convert the strongest graph path into a first proof scene.
7. Add copy-risk blocks: no named settings, no signature scene order, no unique rule system.

Avoid:

- treating reference names as output material;
- applying too many twists until the genre promise disappears;
- ending with abstract theory instead of cards, scenes, and loops.

### Reference Triangulation Upgrade

Use when the user asks for phase 3, deeper validation, or more reliable reference-backed cliche engineering.

Steps:

1. Use `reference-triangulation-protocol-3.md` to score candidate cliches across recognition, story function, reward clarity, Korean localization, serial durability, originality safety, and remixability.
2. Require three supports for stable cards: recognition support, structure support, and Korean webnovel localization support.
3. Use `cliche-graph-stress-tests.md` to check required nodes and causal edges.
4. Repair weak cards by changing proof object, witness, institution, cost, or edge cause.
5. Run `scripts/cliche_graph_lint.py --self-test` after editing the script, and use it on saved cliche graph artifacts when available.
6. End with a graph verdict: pass, revise, or rebuild.

Avoid:

- accepting cards because they are familiar only;
- building graphs where events happen without causal edges;
- calling a graph durable when proof, witness, cost, or long-term ladder is missing.

### Reference Routing Compile

Use when the user asks for phase 4, routing, compiled trope engines, or a reusable end-to-end engine.

Steps:

1. Use `reference-routing-matrix-4.md` to identify intent, genre scope, reference depth, output artifact, and verification need.
2. Load only the routed reference packet.
3. Use `trope-engine-compiler-4.md` to compile route, source packet, genre core, reader contract, card pool, normalized cards, cliche graph, first proof scene, 1-5 episode loop, escalation, package, validation, and handoff.
4. If the output is saved or requested as a stable artifact, run `scripts/cliche_engine_compile_lint.py <path>` or pipe the output through it.
5. End with a validation verdict and the next production artifact.

Avoid:

- loading every reference file by default;
- producing a theory-only routing plan without a compiled engine;
- skipping validation after claiming the engine is reusable.

### Reference Selection Optimize

Use when the user asks for phase 5, ranked cliche selection, portfolio balancing, or a stronger decision layer over many candidate cliches.

Steps:

1. Use `cliche-selection-optimizer-5.md` to normalize candidate cards into role, reward, proof object, witness, protagonist action, cost, repeat method, freshness lever, and copy risk.
2. Score candidates by recognition, genre fit, reward fit, proof visibility, protagonist agency, cost integrity, serial durability, freshness pressure, originality safety, and package alignment.
3. Use `trope-portfolio-builder-5.md` to choose a balanced 6-card, 8-card, or 12-card portfolio instead of blindly taking the highest scores.
4. Remove redundant cards that repeat the same proof object, witness, reward, or cost.
5. Convert the selected portfolio into a first proof scene, 1-5 episode loop, 50+ hook, and first repair.
6. If the output is saved or requested as a stable artifact, run `scripts/cliche_portfolio_lint.py <path>` or pipe the output through it.

Avoid:

- choosing only the top-scoring cards when they do the same job;
- fixing a weak engine by adding more cards instead of repairing the missing slot;
- letting novelty outrank first-scene proof;
- selecting cards that cannot show reward through proof object and witness.

### Reader Feedback Calibrate

Use when the user asks for phase 6, reader-response calibration, fatigue repair, likely comments, retention risk, or whether the selected portfolio will keep readers paying attention.

Steps:

1. Use `reader-feedback-calibrator-6.md` to simulate click, first proof, repeat, and paid-trust reader responses.
2. Simulate at least three reader cohorts when the output is substantial: speed reader, genre loyalist, novelty seeker, power fantasy reader, strategy reader, relationship/status reader, or paid-boundary reader.
3. Score promise clarity, first reward visibility, agency belief, reaction pleasure, repeat curiosity, freshness credibility, fatigue risk, paid-trust safety, confusion control, and copy-shadow safety.
4. Use `cliche-fatigue-repair-loop-6.md` to repair the weakest episode or cliche role through proof rotation, witness escalation, cost causality, competence injection, reward diversification, debt payoff, institution turn, or copy-shadow break.
5. End with likely praise, likely complaints, 1-5 episode feedback map, paid-trust verdict, first repair, and revised proof/loop/hook.
6. If the output is saved or requested as a stable artifact, run `scripts/cliche_feedback_lint.py <path>` or pipe the output through it.

Avoid:

- repairing weak reader response by adding lore;
- removing the familiar reward just to look fresh;
- predicting only praise without naming the first complaint;
- opening a paid hook before paying one visible promise;
- treating fatigue as a reason to discard the portfolio before trying proof, witness, cost, or payoff-order repair.

### Genre Reference Registration

Use when the user asks to research/register genre defaults, build genre-specific cliche reference values, or create 100 cliches per genre.

Steps:

1. Use `webnovel-genre-survey-values.md` to select the genre coverage set.
2. If current platform trend accuracy is requested, run live research first with `market-research-protocol.md`; otherwise use the registered survey values as stable defaults.
3. Use `genre-cliche-bank-100-a.md` and `genre-cliche-bank-100-b.md` as the registered cliche seed banks.
4. Verify each requested genre has 100 items with `scripts/genre_bank_count.py` when editing the banks.
5. Use `cliche-structure-assembly-rules.md` to convert lists into role stacks, episode loops, and cross-genre engines.
6. When producing output, do not print all 100 items unless the user explicitly asks; summarize coverage and sample the most useful cliches.

Avoid:

- presenting a raw 100-item list as a finished trope engine;
- mixing live rankings with stable defaults without saying which is which;
- creating exact work-alike plots from reference sources.

### Successful Cliche Upgrade

Use when the user asks to keep improving common, successful, or commercially reliable webnovel cliches.

Steps:

1. Pick the primary genre preset from `successful-cliche-card-bank-2.md`.
2. Select 6 success-loop roles: identity, advantage, proof, social reaction, renewal, and long-term.
3. For each selected cliche, name the reader reward, visible proof, witness, and cost.
4. Convert the strongest cliche into a first proof scene.
5. Build a 3-5 episode repetition loop that pays one reward each episode.
6. Add anti-staleness rules from `successful-webnovel-cliche-patterns.md`.
7. Add one freshness lever without breaking the familiar promise.

Avoid:

- treating popular cliches as raw lists without scene proof;
- giving the protagonist free advantages with no cost or uncertainty;
- using face-slap scenes with incompetent opposition;
- copying named works, unique rules, or signature scenes.

### Full Concept Engine

Use when the user wants a usable premise.

Steps:

1. Use input assembly if vague.
2. Pick genre stack.
3. Build protagonist engine.
4. Define world/institution engine.
5. Select trope stack.
6. Build first proof scene.
7. Add reward ledger.
8. Add 1-5 episode proof path.
9. Add package direction.

Avoid:

- ending without a proof scene;
- listing tropes without jobs;
- adding novelty that removes the core reward.

### Diagnosis

Use when the user provides an idea, outline, or existing plan.

Steps:

1. Score critical axes.
2. Identify the first failure pattern.
3. Name the biggest drop-off risk.
4. Preserve one strong part.
5. Give a concrete repair.
6. Rewrite the first proof scene if needed.
7. End with a work order.

Avoid:

- vague praise;
- rewriting everything when one repair will work;
- diagnosing style before engine.

### Product Package

Use when the user asks for title, intro, tags, sales copy, or first-screen promise.

Steps:

1. Identify title promise.
2. Align logline and tags to the same reward.
3. Confirm opening scene proves the promise.
4. Build first 5 episode package path.
5. Flag mismatch.

Avoid:

- poetic titles that hide the genre;
- tags that the first 5 episodes do not support;
- intro copy that depends on unexplained lore.

### Production Handoff

Use when the user wants to continue into writing.

Steps:

1. Preserve stable decisions in schema.
2. Name the next artifact.
3. List non-negotiable promise.
4. List approved/restricted cliche cards.
5. List first proof and reward ledger.
6. Give next 3 tasks.

Avoid:

- reopening already-set decisions without reason;
- handing off only vibes;
- omitting must-avoid items.

## Default Final Section

For substantial outputs, end with:

- **다음 작업**: the next artifact or edit.
- **잃으면 안 되는 것**: the core reader promise.
- **주의할 것**: the highest risk.
