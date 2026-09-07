# the-frontier

A sourced survey of where technology actually is in September 2026, and where
it is going next.

The premise: the popular story says quantum computing is the next big thing.
This survey argues the discontinuity is somewhere else, and it is already
here. The evidence is organised into standalone research briefs, each one
tiering its claims and citing its sources.

## How claims are labelled

Every brief marks its claims with one of three tiers:

- **CONFIRMED** — an official source: a company post, a system card, a paper,
  a regulatory filing, or an executive on the record.
- **REPORTED** — a named outlet or named third-party evaluator.
- **SPECULATION / RUMOR** — unsourced, anonymous, inferred, or forecast.

Where a headline number is vendor-reported and an independent evaluator
disagrees, both figures are given. Treat any single benchmark number as a
claim about a harness, not about a model.

## Layout

| File | Subject |
| --- | --- |
| `SYNTHESIS.md` | The argument, drawn from all briefs |
| `research/01` | GPT-6 Astra and OpenAI's trajectory |
| `research/02` | The frontier lab landscape |
| `research/03` | Quantum computing reality check |
| `research/04` | AI compute hardware |
| `research/05` | Power and energy for AI |
| `research/06` | Semiconductor and electrical engineering frontiers |
| `research/07` | AI doing science and engineering |
| `research/08` | Robotics and embodied AI |
| `research/09` | AI agents and economic impact |
| `research/10` | Alternative computing paradigms |
| `research/11` | Brain-computer interfaces and bio-AI |
| `research/12` | Energy technology frontiers |
| `research/13` | Space, telecom, and edge devices |
| `research/14` | Geopolitics, policy, safety, forecasts |
| `research/15` | AI research frontiers and architectures |
| `research/16` | AI versus quantum crossover |
| `research/17` | The RF frontier, for builders |
| `research/18` | The signal processing frontier, for builders |

Briefs 17 and 18 are written for someone deciding what to build. Each ends
with ten concrete projects, what they need, and who would pay.

## Building the combined document

```
python3 scripts/build_report.py
```

This concatenates `SYNTHESIS.md` and every brief into
`THE-FRONTIER-REPORT.md`, and prints word, source, and citation counts per
brief.

## A caution on dates

This survey is a snapshot taken on 2026-09-07. The fastest-moving sections
are the model landscape and the compute build-out, where a month is a long
time. Re-check anything load-bearing before you rely on it.
