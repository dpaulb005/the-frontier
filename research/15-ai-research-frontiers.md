# The Technical Research Frontier of AI Itself — September 2026

*Research memo. Compiled 2026-09-07. Every substantive claim is tagged **CONFIRMED** (primary source: paper, model card, lab blog, official docs), **REPORTED** (credible secondhand press or single-sourced), or **SPECULATION** (my inference or widely-held-but-unverified).*

---

## TL;DR

1. **GPT-6 "Astra" shipped September 3, 2026** (limited preview to trusted partners; broader paid release Sept 4). It is **CONFIRMED** the largest training run to date and the first OpenAI pretraining run above ~100,000 GPUs, at the Abilene/Texas Stargate site. [1][2]
2. The headline architectural claim — that Astra uses a constrained form of **recurrent depth / looped transformers** — is **REPORTED**, sourced to *The Information* (Sept 1, 2026) and echoed downstream. OpenAI's own system card and launch materials do **not** name the technique. Treat the architecture as reported, not confirmed. [1][3]
3. Recurrent depth is not new: it descends from **Universal Transformers** (2018), **ALBERT-style layer sharing**, **Adaptive Computation Time**, and most directly from **Geiping et al., "Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach"** (arXiv 2502.05171, NeurIPS 2025), which unrolled a shared block at test time and got a 3.5B model to behave like ~50B of compute. [4]
4. The strategic point of latent/recurrent reasoning: **decouple reasoning compute from token count.** Chain-of-thought buys test-time compute at the cost of serialized tokens and a natural-language bottleneck; recurrent depth buys it in latent space, per-token, adaptively. This is why a "no-CoT time horizon" jump is the interesting metric, not a benchmark score.
5. **RL is now a first-class scaling axis.** RLVR/GRPO-family post-training moved from ~3.75% of pretraining compute (DeepSeek-R1-Zero) to order-of-magnitude larger budgets across o1→o3 and Grok-3→Grok-4 generations, with published RL-compute scaling laws now existing. [5][6]
6. **Continual learning is the consensus missing piece.** Sutton's "era of experience" framing and Google's Nested Learning / **Hope** architecture (Nov 2025) attack the same gap: models that don't update after deployment. Titans/TTT/CMS-style multi-timescale memory is the live research line. [7][8]
7. **Efficiency is where the compounding is.** DeepSeek Sparse Attention cuts long-context attention FLOPs ~98% at 128K; V4-class hybrid attention makes 1M-token context economically routine; FP4/MXFP4 native training is now competitive with FP8. [9][10][11]
8. **World models split into two camps** — generative ("render to predict": Genie 3, Cosmos, Sora-lineage) and latent-predictive ("compress to understand": V-JEPA 2, Dreamer 4). Genie 3's real-time 24fps interactive worlds with ~1 minute of memory is the capability marker. [12]
9. **Self-improvement loops are measurably real but bounded.** AlphaEvolve-lineage systems, MLE-Bench/RE-Bench/PaperBench, and a 2026 crop of "AI4AI" benchmarks show agents doing genuine ML-engineering work — while remaining far from closed-loop recursive improvement. [13]
10. **The discontinuity claim is defensible but narrow**: not "AGI arrived," but that three previously-separate curves (pretraining scale, RL post-training, and now latent test-time depth) are being scaled *simultaneously* for the first time, and interpretability tooling is losing its best handle (readable CoT) exactly as that happens.

---

## 1. Recurrent depth: what it actually is, and where it comes from

*(draft section — expanded below)*

## 2. Reasoning and RL scaling

## 3. Continual learning and memory

## 4. Architecture shifts

## 5. Data limits and synthetic data

## 6. Self-improvement loops

## 7. World models

## 8. Interpretability

## 9. Efficiency: distillation, low-precision, optimizers

## What people are underestimating

## Key numbers

## Sources
