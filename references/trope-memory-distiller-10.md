# Trope Memory Distiller 10

Use this file when the request asks for "고도화 진행10", trope memory, cliche memory, reusable reference distillation, case library, pattern library, or learning from prior trope-engine outputs.

Phase 10 upgrades the engine from "quality-gated output" to "reusable cliche knowledge." It turns reference-derived cards, generated engines, reader feedback, and quality audits into durable memory cards that can be retrieved, adapted, and safely recombined later.

## Reference Basis

Extract method, not examples.

| Reference family | What to extract | Skill use |
| --- | --- | --- |
| Trope ideation systems | tropes as intermediate story building blocks | store cliches as reusable structures, not prose |
| Narrative graph research | connected trope/event graphs and coherence checks | preserve causal edges when saving memory |
| Narrative schema mining | plot schemas, character functions, instantiable templates | store abstract roles and fillable slots |
| Story planning research | preconditions, causal links, goal satisfaction | save what must be true before the cliche works |
| Fictional ideation/knowledge-base manipulation | alter and combine facts while preserving evaluative capacity | define what can be changed safely |
| Case-based reasoning | retrieve, adapt, test, and learn from past cases | reuse prior successful engines without copying them |
| Korean webnovel practice | paid trust, episode rhythm, platform-readable tags | add commercial serial fields to every memory card |

## Memory Card Schema

Each saved cliche memory should be smaller than a full concept but stronger than a raw cliche name.

```yaml
trope_memory_card:
  id:
  label:
  source_family:
  source_abstraction:
  genre_origin:
  reusable_promise:
  trope_dna:
    pressure:
    protagonist_method:
    proof_object:
    witness:
    reward:
    cost:
    institution:
    hook_object:
  preconditions:
  causal_edges:
  retrieval_cues:
  transfer_axes:
  protected_core:
  flexible_shell:
  anti_copy_rules:
  best_use:
  fatigue_risk:
  validation:
  next_artifact:
```

## Distillation Procedure

Use this when converting a reference, output, or prior phase artifact into memory.

1. **Scope the case**: name whether it came from a reference family, trope pack, compiled engine, portfolio, feedback artifact, serial deployment, or quality audit.
2. **Abstract the source**: convert named examples into pressure, function, proof object, witness, cost, and institution.
3. **Find the reusable promise**: state the pleasure a reader recognizes before naming any setting.
4. **Extract trope DNA**: fill pressure, method, proof, witness, reward, cost, institution, and hook.
5. **Record preconditions**: define what must exist before the cliche works, such as ranking system, public metric, family hierarchy, sect law, gate rule, or market data.
6. **Record causal edges**: use because/therefore/but links instead of a loose card list.
7. **Split protected core and flexible shell**: core is the reader reward; shell is genre costume, institution, proof object, and timing.
8. **Add retrieval cues**: tags that let the skill find the memory later.
9. **Add anti-copy rules**: what cannot be reused from any named work or prior output.
10. **Attach validation**: which lint or acceptance test should be run before reuse.

## Protected Core vs Flexible Shell

Do not adapt a memory by changing everything.

| Layer | Preserve | May change |
| --- | --- | --- |
| reader promise | status, revenge, money, power, recognition, knowledge, safety, relationship | exact wording |
| pressure | the reason action is needed now | institution causing the pressure |
| protagonist method | active advantage and repeatable tactic | tool, profession, skill, asset, martial technique |
| proof object | visible evidence of value | metric, artifact, contract, wound, stock chart, duel result |
| witness | authority whose reaction creates social proof | guild, board, sect elder, professor, media, constellation |
| cost | consequence caused by success | legal, social, market, sect, system, relationship cost |
| hook | concrete next question | message, bid, warrant, duel, raid, audit, prophecy |

## Retrieval Cues

Use 5-9 cues per memory.

| Cue type | Examples |
| --- | --- |
| genre | hunter, tower, regression, finance, murim, academy, possession, support, romance fantasy |
| reward | rank, money, revenge, recognition, hidden knowledge, safety, relationship |
| institution | association, guild, family, corporation, sect, academy, tower, state, media |
| proof | public test, ledger, raid footage, audit, duel, contract, market move, artifact |
| pressure | deadline, humiliation, debt, expulsion, hostile acquisition, gate break, marriage contract |
| transfer | finance-to-hunter, murim-to-academy, regression-to-romance, support-to-tower |
| risk | too-easy, copy-shadow, private proof, weak witness, debt pileup, package mismatch |

## Memory Lifecycle

| Stage | Action | Output |
| --- | --- | --- |
| capture | identify useful cliche case | source note |
| normalize | fill memory card schema | reusable card |
| deduplicate | merge cards with same proof/reward/witness | cleaner library |
| enrich | add transfer axes and anti-copy rules | safer card |
| validate | run quality/acceptance/lint checks | pass/revise/rebuild |
| retrieve | select cards by cues and brief | candidate set |
| adapt | transfer with protected core preserved | genre-ready card |
| learn | record fatigue, reader response, and repair | updated memory |

## Deduplication Rules

Merge or split cards using these tests.

| Situation | Action |
| --- | --- |
| same reward, proof, witness, and cost | merge as one memory with multiple genre shells |
| same reward but different proof and cost | keep separate cards |
| same proof object but different reward | split; proof alone is not the cliche |
| same source vibe but different causal path | split; path matters |
| same named-work shadow | rewrite or reject |

## Memory Output Contract

For phase-10 outputs, include:

- source cases used;
- normalized memory cards;
- retrieval cues;
- protected core and flexible shell;
- transfer axes;
- anti-copy rules;
- dedupe/merge decisions;
- validation target;
- next artifact.
