# Narrative Coherence Audit 9

Use this file with `cliche-quality-regression-suite-9.md` when checking whether a trope engine, serial deployment, or episode brief is logically and emotionally coherent.

Phase 9 treats coherence as more than "the text sounds fluent." A commercial webnovel engine needs local event coherence, global reward coherence, institution coherence, and reader-memory coherence.

## Coherence Layers

| Layer | Question | Webnovel-specific check |
| --- | --- | --- |
| temporal coherence | Did events happen in an understandable order? | no payoff relies on an event not yet shown |
| causal coherence | Did this happen because of the previous action/cost? | wins create the next pressure |
| motivational coherence | Does the protagonist's method match their wound, goal, and advantage? | advantage creates choices, not random luck |
| institutional coherence | Does the world react consistently? | guilds, sects, schools, boards, systems, markets follow their incentives |
| reward coherence | Does each episode pay the promised pleasure? | rank/money/status/revenge/knowledge/safety/relationship/recognition remain visible |
| scale coherence | Does the bigger arc grow from the smaller arc? | personal -> institution -> region/world is connected |
| reader-memory coherence | Can readers remember why the current problem matters? | old debts and witnesses are reintroduced through action |
| packaging coherence | Do title/logline/tags/opening/paid boundary sell the same promise? | marketing does not promise a different genre |

## Coherence Questions

Use these after building a plan.

1. What did the protagonist do that caused the current reward?
2. Who saw the reward, and why does that witness matter?
3. What new pressure was created by the reward?
4. Which old promise was paid before the new hook opened?
5. Which institution changed its behavior because of the proof?
6. Which cliche card would break the plan if removed?
7. Which card is decorative and should be cut?
8. Does the antagonist know enough to be dangerous without becoming omniscient?
9. Does the long-term hook preserve the same reader reward?
10. Is any unique source-work chain still recognizable?

## Inference Gap Check

Readers should not need to invent missing logic.

| Gap | Sign | Repair |
| --- | --- | --- |
| action gap | result appears without protagonist method | add method step under pressure |
| witness gap | status changes but no authority saw it | add authority witness or proof record |
| cost gap | new trouble appears randomly | connect cost to the public proof |
| institution gap | world reacts only because plot needs it | define incentive or rule |
| memory gap | old debt returns without reminder | reintroduce debt through object, witness, or consequence |
| scale gap | suddenly national/world stakes | pass through institution escalation |
| emotion gap | relationship shift has no scene | add public/private choice that changes behavior |
| originality gap | events follow a known source order | change institution, proof object, consequence, and timing |

## Coherence Stress Test

Apply these removals.

| Remove | If nothing changes | Problem |
| --- | --- | --- |
| proof object | proof is decorative | reward is not visible |
| witness | social reaction is fake | recognition is unsupported |
| cost | no next pressure | serial engine is weak |
| institution | world has no rules | setting is wallpaper |
| antagonist | conflict is artificial | no opposition engine |
| reward debt | hooks are empty | paid trust is weak |
| title promise | packaging is disconnected | wrong readers may click |

## Repair Operators

| Operator | Use when | Effect |
| --- | --- | --- |
| because-chain rewrite | events feel adjacent | add because/therefore/but logic |
| proof anchoring | reward is abstract | add object, metric, contract, rank, money, wound, witness |
| institution incentive | authority reacts randomly | define what the institution gains, loses, fears, or controls |
| debt callback | readers may forget a promise | reintroduce through consequence or witness |
| scale bridge | next arc jumps too far | insert intermediate institution or regional consequence |
| antagonist information limit | enemy feels stupid or omniscient | give partial truth and one wrong assumption |
| packaging realignment | title and opening diverge | rewrite title/logline or first proof to match |

## Audit Output

Use this structure for phase-9 coherence checks.

```yaml
narrative_coherence_audit:
  artifact:
  core_promise:
  coherence_scores:
    temporal:
    causal:
    motivational:
    institutional:
    reward:
    scale:
    reader_memory:
    packaging:
  inference_gaps:
    - gap:
      location:
      repair:
  decorative_cards:
  missing_edges:
  strongest_coherent_chain:
  weakest_chain:
  repair_order:
  verdict:
```

## Coherence Verdict

| Verdict | Use when |
| --- | --- |
| pass | all core chains are understandable and paid |
| revise | one or two inference gaps need explicit repair |
| rebuild | core promise, first proof, or causal chain fails |
