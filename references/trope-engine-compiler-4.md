# Trope Engine Compiler 4

Use this file for phase-4 upgrades and for end-to-end compilation of a Korean webnovel cliche engine from routed references.

A compiled engine is stronger than a trope pack. It contains the source packet, selected cards, graph, proof scene, episode loop, escalation ladder, packaging direction, validation, and handoff.

## Compiler Pipeline

Run the pipeline in this order:

1. **Intake**: identify user intent, genre stack, desired output, and whether live market data is needed.
2. **Route**: use `reference-routing-matrix-4.md` to pick the smallest useful reference packet.
3. **Source packet**: list the files or source families used and tag reliability.
4. **Genre core**: choose the primary genre that owns the first proof.
5. **Card pool**: collect candidate cards from genre banks, success cards, synthesis cards, or user-provided ideas.
6. **Card normalization**: convert cards to role, reward, proof, witness, cost, repeat method, and copy-risk fields.
7. **Graph assembly**: connect cards with causal edge labels.
8. **Proof scene**: compile the strongest path into a first proof scene.
9. **Episode loop**: build 3-5 episode repeatability.
10. **Escalation ladder**: scale personal -> institution -> market/faction -> region/nation/world while preserving the same reward.
11. **Packaging**: align title direction, logline, tags, and paid boundary.
12. **Validation**: run acceptance tests, triangulation if used, graph stress tests if used, and lint when a saved artifact exists.
13. **Production handoff**: state next artifact and non-negotiable promise.

## Compiled Engine Schema

Use this schema for stable outputs:

```yaml
compiled_trope_engine:
  route:
    user_intent:
    genre_scope:
    reference_depth:
    output_artifact:
    verification:
  source_packet:
    stable_structure:
    stable_genre:
    research_signal:
    platform_current:
    community_signal:
    copy_risk:
  genre_core:
    primary:
    support:
    delayed_flavors:
    first_click_owner:
  reader_contract:
    one_line_promise:
    reward_channels:
    visible_rewards:
    reward_debt:
  card_pool:
    identity:
    advantage:
    pressure:
    proof:
    witness:
    cost:
    antagonist:
    long_term:
    hook:
  normalized_cards:
    - id:
      source:
      role:
      recognition_signal:
      reader_reward:
      protagonist_action:
      proof_object:
      witness:
      institution:
      cost_or_pressure:
      repeat_method:
      remix_operator:
      copy_risk_block:
  cliche_graph:
    nodes:
    edges:
    required_node_coverage:
    weakest_edge:
    strongest_loop:
  first_proof_scene:
    pressure:
    action:
    proof_object:
    witness:
    reward:
    cost_or_hook:
  episodes_1_5:
    - episode:
      pressure:
      card_used:
      proof:
      reward:
      cost_or_hook:
  escalation:
    personal:
    team_or_household:
    institution:
    market_or_faction:
    region_or_nation:
    hidden_world_or_system:
  package:
    title_direction:
    logline:
    tags:
    paid_boundary:
  validation:
    acceptance_verdict:
    triangulation_verdict:
    graph_verdict:
    lint_verdict:
    first_repair:
  handoff:
    next_artifact:
    non_negotiable_promise:
    approved_cards:
    restricted_cards:
```

## Compilation Rules

- The first proof must be owned by the primary genre.
- A support genre may provide cost, witness, institution, or escalation, but should not steal the first click.
- Every normalized card needs a proof object and a cost.
- Every graph edge needs a causal verb: causes, reveals, measures, claims, prices, punishes, recruits, mirrors, escalates, or debts.
- Every 3-5 episode loop must pay at least one reward before a larger hook.
- Packaging cannot promise a reward that the first proof scene does not show.
- Validation must produce `pass`, `revise`, or `rebuild`.

## Reference Packet Presets

### Familiar But Fresh Concept

Load:

- `default-genre-settings.md`
- `trope-card-library.md`
- `variation-engine.md`
- `scene-proof-bank.md`

Compile:

- 5-8 cards;
- one proof scene;
- 1-5 episode loop.

### Success Cliche Concept

Load:

- `successful-webnovel-cliche-patterns.md`
- `successful-cliche-card-bank-2.md`
- `reader-reward-model.md`
- `scene-proof-bank.md`

Compile:

- 6-role success stack;
- reward-then-cost loop;
- paid-trust hook.

### 100-Bank Concept

Load:

- `webnovel-genre-survey-values.md`
- relevant `genre-cliche-bank-100-a.md` or `genre-cliche-bank-100-b.md`
- `cliche-structure-assembly-rules.md`

Compile:

- 10-card trope engine;
- graph stress test;
- long-term ladder.

### Reference Synthesis Concept

Load:

- `reference-synthesis-engine-2.md`
- `cliche-remix-operators.md`
- `reference-derived-card-bank-3.md`
- `cliche-graph-stress-tests.md`

Compile:

- reference-derived cards;
- remix operators;
- card graph;
- first proof scene.

### Triangulated Compiled Engine

Load:

- `reference-routing-matrix-4.md`
- `reference-triangulation-protocol-3.md`
- `cliche-graph-stress-tests.md`
- `acceptance-tests.md`
- `production-handoff.md`

Compile:

- source packet;
- triangulation table;
- graph verdict;
- acceptance verdict;
- handoff.

## Phase-4 Output Contract

For phase-4 requests, produce:

- **라우팅 결과**:
- **소스 패킷**:
- **장르 코어**:
- **정규화한 카드 풀**:
- **클리셰 그래프**:
- **1화 증명 장면**:
- **1-5화 루프**:
- **장기 확장 사다리**:
- **상품 패키지 방향**:
- **검증 판정**:
- **생산 인계**:

Keep the visible answer compact unless the user explicitly asks for the full YAML schema.

## Failure Modes

### Reference overload

Symptom: many source names, no usable scene.

Repair: reduce to one source packet and compile a first proof scene.

### Card hoarding

Symptom: many cards, no graph.

Repair: require causal edges and cut decorative cards.

### Validation theater

Symptom: scores appear but do not change the design.

Repair: name the first repair and update the graph path.

### Package drift

Symptom: title sells one reward, proof scene pays another.

Repair: align title noun, protagonist action, proof object, and first reward.

### Genre inversion

Symptom: support genre owns the opening.

Repair: move support genre to cost, witness, or escalation.
