# Cliche Quality Regression Suite 9

Use this file when the request asks for "고도화 진행9", quality regression, release gate, engine QA, output consistency, post-deployment audit, or checking whether a trope engine still satisfies earlier phase promises after changes.

Phase 9 upgrades the engine from "serial deployment plan" to "repeatable quality gate." It catches regressions across all prior layers: reference abstraction, originality safety, graph causality, portfolio balance, reader feedback, serial deployment, reward debt, and product packaging.

## Reference Basis

Do not copy examples from external references. Extract quality principles:

| Reference family | What to extract | Skill use |
| --- | --- | --- |
| Narrative coherence research | temporal order, causal transition, meaning/interpretation | test whether events and cliche payoffs make sense in order |
| Story-generation evaluation research | automatic metrics are weak without human-style checks | use explicit checklist gates instead of trusting fluency |
| Open-ended story metric benchmarks | coherence, robustness, inferential knowledge gaps | test cause/effect and missing implication |
| Serial fiction and webnovel research | continuity, release rhythm, retention, paid boundary | check if deployment pays and opens promises correctly |
| Trope and motif references | reusable recognition signals | ensure trope cards still pay generic genre grammar, not copied details |
| Reader feedback calibration | likely praise/complaints | check that repairs address the most likely complaint |

## Regression Targets

Run these gates after a substantial engine update, phase 9 request, or when a saved artifact will be reused.

| Gate | Checks | Fails when |
| --- | --- | --- |
| source gate | reference families are named and abstracted safely | sources are listed but not converted into function/proof/cost |
| promise gate | one-line reader promise is visible in title/opening/proof | output is mostly setting or terminology |
| proof gate | first proof has pressure, action, proof object, witness, reward, cost | power-up is private or witness is meaningless |
| graph gate | reward -> witness -> institution -> cost -> hook has causal edges | cards sit side by side without "because/therefore/but" |
| portfolio gate | identity, advantage, proof, witness, cost, renewal, institution, long-term are covered | top cards duplicate the same job |
| feedback gate | likely praise, complaints, fatigue, paid-trust risk are named | output predicts only positive reaction |
| serial gate | each episode/segment has one job and one paid reward | episodes are event lists without operating purpose |
| debt gate | open promises are tracked and paid | new mysteries open faster than old rewards are paid |
| packaging gate | title, logline, tags, 1화, paid boundary sell the same reward | packaging promises a different pleasure |
| originality gate | named settings, unique rules, signature scene order are removed | output reads like a disguised existing work |

## Regression Severity

| Severity | Meaning | Required response |
| --- | --- | --- |
| P0 | copying risk, no first proof, or genre promise missing | rebuild before use |
| P1 | causal graph, paid trust, or reward debt broken | revise before production |
| P2 | portfolio imbalance, fatigue risk, weak witness, package mismatch | repair in the next pass |
| P3 | wording, table completeness, or optional metadata issue | polish only |

## Gate Procedure

Run gates in this order:

1. **Scope**: identify the artifact being tested: trope pack, compiled engine, portfolio, feedback artifact, serial deployment, bible insert, or episode brief.
2. **Source abstraction**: check that references became function, pressure, proof object, witness, cost, and safe variation.
3. **Reader promise**: verify that the promise can be understood in 10 seconds.
4. **First proof**: verify the opening proof scene.
5. **Causal graph**: verify because/therefore/but links.
6. **Portfolio balance**: verify role coverage.
7. **Feedback and fatigue**: verify likely complaint and repair.
8. **Serial deployment**: verify episode jobs, hook cadence, and reward debt.
9. **Packaging alignment**: verify title/logline/tags/opening/paid boundary.
10. **Originality safety**: verify no named-work shadow.
11. **Release verdict**: pass, revise, or rebuild.
12. **Patch list**: write the smallest concrete repairs.

## Cross-Phase Compatibility Matrix

Use this matrix when a later output claims to build on earlier phases.

| Earlier phase | Later output must preserve | Regression sign |
| --- | --- | --- |
| phase 2 synthesis | function, pressure, proof, witness, cost | references become decorative names |
| phase 3 graph | required nodes and causal edges | graph becomes a loose card list |
| phase 4 compiler | route, source packet, first proof, validation, handoff | compiled engine lacks handoff or verification |
| phase 5 portfolio | selected slots and rejected-card reasoning | top scores replace role balance |
| phase 6 feedback | likely complaint and first repair | only praise remains |
| phase 7 deployment | episode jobs, reward debt, hook cadence | plan becomes summary beats |

## Release Score

Score each gate 0-5.

| Score | Meaning |
| ---: | --- |
| 5 | complete and production-ready |
| 4 | usable with minor repair |
| 3 | usable but risky |
| 2 | major missing element |
| 1 | present only as a label |
| 0 | absent |

Verdict:

| Average | Critical issue | Verdict |
| ---: | --- | --- |
| 4.3-5.0 | none | pass |
| 3.2-4.2 | no P0 | revise |
| any | P0 present | rebuild |
| 0-3.1 | any | rebuild |

## Patch List Format

Each repair must be concrete.

```yaml
quality_regression_patch:
  issue_id:
  severity:
  gate:
  problem:
  why_it_matters:
  repair:
  expected_effect:
  verify_with:
```

Bad repair:

```text
make it more interesting
```

Good repair:

```text
episode 2 repeats the same rank proof; replace it with an association audit and make the guild lawsuit the cost caused by episode 1's public recognition
```

## Output Contract

For phase-9 outputs, include:

- artifact under test;
- source families used;
- gate score table;
- severity list;
- cross-phase regression check;
- release verdict;
- patch list;
- verification command or lint target if saved;
- next production artifact.
