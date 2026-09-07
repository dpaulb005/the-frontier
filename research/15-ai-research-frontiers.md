# The Technical Research Frontier of AI Itself — September 2026

*Research memo, compiled 2026-09-07. Every substantive claim is tagged **[CONFIRMED]** (primary source: peer-reviewed/arXiv paper, model card, lab blog, official docs), **[REPORTED]** (credible press, single-sourced or secondhand), or **[SPECULATION]** (my inference, or a widely-held view without verification).*

---

## TL;DR

1. **GPT-6 "Astra" shipped September 3, 2026** — limited preview to trusted partners, broader paid release September 4. **[CONFIRMED]** It is OpenAI's largest training run to date and the first pretraining run above ~100,000 GPUs, at the Abilene, Texas Stargate site, per VP of Research Aidan Clark. [1]
2. The headline architectural claim — that Astra uses a **constrained form of recurrent depth / looped transformers** — is **[REPORTED]**, originating with *The Information* on September 1–2, 2026 and amplified by TechCrunch and The Verge. OpenAI's system card and launch materials **do not name the technique**. There is no technical report, code, or patent corroboration. [1][2][3]
3. Recurrent depth has a real lineage: Universal Transformers (2018), Adaptive Computation Time, ALBERT-style layer sharing, and most directly **Geiping et al., "Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach"** (arXiv 2502.05171, NeurIPS 2025) — a 3.5B-parameter / 800B-token model that reached benchmark performance equivalent to ~50B parameters of compute purely by unrolling a shared block at inference. **[CONFIRMED]** [4]
4. The strategic point is **decoupling reasoning compute from token count**. Astra's measured token efficiency is the tell: Artificial Analysis found it uses roughly **one-third the output tokens of GPT-5.6 Sol** on coding and one-fifth of Claude Opus 5 at high effort, while matching them on coding-agent scores. **[CONFIRMED]** [5]
5. **RL is now a genuine scaling axis, not a finishing step.** DeepSeek-R1-Zero's RL was 3.75% of pretraining compute; o1→o3 and Grok-3→Grok-4 each represent >10× RL-compute jumps, and published RL-compute scaling laws now exist. **[CONFIRMED/REPORTED]** [6][7]
6. **Continual learning is the consensus missing piece.** Sutton's critique (LLMs can't learn on the job) and Google's Nested Learning / **Hope** architecture attack the same gap from opposite ends. **[CONFIRMED]** [8][9][10]
7. **Efficiency compounds fastest.** DeepSeek Sparse Attention cuts 128K-context attention FLOPs ~98%; hybrid linear/softmax stacks (Qwen3-Next → Qwen3.5, ~75% linear layers) make million-token context routine; native FP4/MXFP4 pretraining is now competitive with FP8. **[CONFIRMED]** [11][12][13][14]
8. **World models bifurcated**: generative "render to predict" (Genie 3, real-time 24fps interactive worlds, ~1 minute of memory) vs. latent "compress to understand" (V-JEPA 2, Dreamer 4, first offline Minecraft diamond). **[CONFIRMED]** [15][16]
9. **Self-improvement is measurable but bounded.** AlphaEvolve-lineage systems, MLE-Bench/RE-Bench/PaperBench, and a 2026 crop of AI4AI benchmarks show real ML-engineering competence and zero closed-loop recursion. **[CONFIRMED]** [17][18]
10. **The discontinuity is narrow but real**: for the first time three curves — pretraining scale, RL post-training, and latent test-time depth — are being pushed simultaneously, and the interpretability field's best handle (readable chain-of-thought) is being eroded exactly as that happens.

---

## 1. Recurrent depth: what it is, and where it came from

### The mechanism

A standard transformer has a fixed serial depth: *L* layers, each with its own weights, one forward pass per token. A **depth-recurrent** or **looped** transformer instead partitions the network into a *prelude* (embed + a few layers), a *recurrent core block* iterated *r* times with shared weights, and a *coda* (a few layers + unembed). The latent state cycles through the same block repeatedly before a token is emitted. **[CONFIRMED]** [4]

Two properties follow. First, effective serial depth becomes `prelude + r × core + coda` while parameter count stays at `prelude + core + coda` — you buy depth without buying parameters. Second, *r* can be varied at inference: easy tokens exit early, hard tokens loop more. This is adaptive test-time compute that costs no output tokens.

Geiping et al. scaled this to 3.5B parameters on 800B tokens and showed reasoning benchmark performance rising with *r* up to compute equivalent to a ~50B dense model. Crucially, it required **no specialized reasoning data**, works with small context windows, and — their central claim — "can capture types of reasoning that are not easily represented in words." **[CONFIRMED]** [4]

### The lineage

- **Universal Transformers** (Dehghani et al., 2018): weight-shared recurrent transformer with Adaptive Computation Time halting. The direct ancestor.
- **ALBERT** (2019): cross-layer parameter sharing, motivated by compression rather than reasoning.
- **COCONUT** (Hao et al., Meta FAIR, arXiv 2412.06769): feeds the last hidden state back as the next input embedding instead of decoding it to a token — "continuous thought." On the ProsQA planning benchmark it exhibits an emergent breadth-first search, apparently holding **multiple candidate search frontiers in superposition** in a single latent vector, at far fewer tokens than CoT. **[CONFIRMED]** [19]
- **Reasoning by Superposition** (arXiv 2505.12514) gave the theoretical account of why continuous thought can encode a superposition of reasoning paths. **[CONFIRMED]**
- **Hierarchical Reasoning Model** (arXiv 2506.21734) and the 2026 *Survey on Latent Reasoning* (arXiv 2507.06203) consolidated the subfield.
- Geiping's line continued into 2026 with work like *Pretraining Recurrent Networks without Recurrence* (arXiv 2606.06479), addressing the training-cost problem that recurrence creates. **[CONFIRMED]**

### What Astra actually appears to be doing

The most informative public signal is a constraint, not a capability. **[REPORTED]** Jakub Pachocki (OpenAI) has stated that "the depth of the computation graph for our present frontier models, including Astra, is within a factor of two of GPT-4," which — if the loop hypothesis is right — bounds Astra to roughly **three to four loops**, not the dozens Geiping explored. [2]

This reads as a deliberate safety-motivated ceiling: keep enough serial depth to buy real gains, not so much that the chain-of-thought stops being where the reasoning lives. Geoffrey Irving's counter-position, cited in the same discussion, is that bounding serial depth only helps if the bound is set *very low*, and hundreds of effective layers offers little protection. **[REPORTED]** [2]

The supporting evidence for *some* latent-compute shift is the token accounting. Artificial Analysis measured Astra at ~1/3 of GPT-5.6 Sol's output tokens on coding tasks and ~10% fewer on general intelligence tasks, at equal or better scores — described as "70% more token efficient" for coding. **[CONFIRMED]** [5] That is exactly the signature you would expect if reasoning moved from serialized tokens into per-token latent iteration. It is not proof: aggressive CoT-compression RL produces a similar signature. **[SPECULATION]** that the token efficiency is *caused by* recurrent depth.

### The metric that matters: no-CoT time horizon

Redwood Research's *Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models* (arXiv 2606.07157, June 2026) evaluated 14 models from GPT-2 through GPT-5.5 on 43 benchmarks. Findings: **[CONFIRMED]** [20][21]

- No-CoT time horizon doubles every **373 days** (95% CI 167–691).
- Reasoning *token* horizon doubles every **437 days**.
- GPT-5.5's 50% no-CoT time horizon: **~3 minutes**; token horizon ~1,500 o3-mini-equivalent tokens.
- Extrapolation: ~7 min / 3.7k tokens by 2028; ~25 min / 12k tokens by 2030.

The load-bearing finding for Astra: **increasing layer count is the most effective lever on no-CoT horizon, and doubling the horizon requires only ~1.3× more layers.** **[REPORTED]** [2] A looped model with r=3–4 multiplies effective depth by ~3–4×, which on a 1.3×-per-doubling curve implies roughly **1.5–2 doublings of no-CoT horizon in a single generation** — i.e. jumping a trend that normally takes ~1.5–2.5 years. **[SPECULATION]**, but it is the cleanest available explanation of why "a large jump in no-CoT reasoning time horizon" is the reported headline rather than a benchmark score.

The safety corollary, stated plainly by the Redwood authors: models able to do substantial reasoning with no CoT could eventually sustain reasoning durations sufficient for "complex long-term power-seeking" that no CoT monitor would see. **[CONFIRMED]** [21]

### Astra's measured capabilities

**[CONFIRMED]** from OpenAI materials and independent evaluation: [3][5][22]
- 100% on ExploitBench (exploit development from known vulnerabilities); found and chained **two zero-days** during evaluation; refused 91.5% of cyber-jailbreaks vs. 59% for GPT-5.6 Sol. Cyber capability gated behind a "Daybreak Blue" defensive-use tier.
- Ten mathematics / theoretical CS results with published manuscripts and **Lean proofs**.
- Artificial Analysis Intelligence Index **61** (ties GPT-5.6 Sol, ~5 below Claude Fable 5.1); Coding Agent Index **67** (ties Claude Opus 5 and Fable 5; Fable 5.1 leads at 70).
- **AA-Briefcase +~80 Elo** — the long-horizon knowledge-work eval (multi-week projects, thousands of linked files). A GDPval-AA v2 *regression* of similar magnitude.
- Hallucination rate on AA-Omniscience fell 92% → 51%.
- Pricing $10/$50 per million tokens, a 2.5× list increase over Sol — but cheaper per completed coding task because of the token efficiency.

**[REPORTED]**, less reliably: 99.9% (or 98.6%) on ARC-AGI-3, 97.6% on FrontierMath Tier 4, ~73–74% on DeepSWE. [22]

The honest read: **Astra is a discontinuity in long-horizon agentic work and cost-per-task, not in raw intelligence.** It sits level with rivals on neutral intelligence benchmarks and separates on messy, tool-using, multi-day work. That profile is what a serial-depth + agentic-RL generation should look like.

---

## 2. Reasoning and RL scaling

RLVR — RL with Verifiable Rewards — is the load-bearing paradigm. The public lineage runs GRPO (DeepSeek-R1) → DAPO → GSPO/ARPO/VPO and a widening family of agentic policy-optimization variants. **[CONFIRMED]** [6][7]

Scale is the story. DeepSeek-R1-Zero's RL was **100,000 H800 GPU-hours, 3.75% of its pretraining compute**. The o1→o3 transition represents >10× more RL compute, with a comparable jump Grok-3→Grok-4. **[REPORTED]** [7] *The Art of Scaling Reinforcement Learning Compute for LLMs* (arXiv 2510.13786) provided the first serious predictive framework for RL-compute scaling; *Predictable GRPO* (arXiv 2606.30789) gave closed-form training dynamics in 2026. **[CONFIRMED]**

The frontier has moved to **long-horizon agentic RL**: multi-day agents that browse, code, run experiments and revise, trained with RLVR over entire trajectories. AgentGym-RL (ICLR 2026), AgentRL, and SkyRL-Agent are the open frameworks; the closed labs are converging on **strong base + self-play + verifier + tree search**. **[CONFIRMED/REPORTED]** [23] A genuine RL-environments *market* now exists, with frontier-lab spend projected to grow 3–5× into 2026 and Anthropic reported as the largest single buyer at tens of millions annually. **[REPORTED]** [24]

The unresolved question, and it is a big one: **there is still no public evidence that RLVR generalizes far beyond competition math and coding**, or that it scales usefully past modest training budgets. **[REPORTED]** [6] ProRL showed 16K GPU-hours of prolonged RL uncovering genuinely novel strategies in a 1.5B model — real, but small. The gap between "RL compute rivals pretraining compute" as an aspiration and as a demonstrated fact remains open.

---

## 3. Continual learning and memory

This is where the field's own consensus says the frontier isn't.

**Sutton's position** (Dwarkesh Patel interview, Sept 2025, still the reference text): LLMs are not bitter-lesson-pilled; they lack on-the-job learning, have abysmal sample efficiency, and depend on an exhaustible human data supply. His steel-manned claim is that a new architecture enabling continual learning would make the special training phase unnecessary — the agent would just learn on the fly. **[CONFIRMED]** [8] Nathan Lambert's *Contra Dwarkesh on Continual Learning* is the counter-case. **[CONFIRMED]** [9] The interesting agreement across the disagreement: everyone calls this an **algorithmic gap, not an infrastructure gap**.

**Google's Nested Learning** (Research blog, Nov 2025) is the most serious architectural answer. It reframes a model as nested optimization problems at different update frequencies, and extends transformer memory into a **Continuum Memory System** — a spectrum of memory modules each updating at its own rate. The **Hope** architecture builds on the **Titans** family plus Nested Learning: unbounded nesting levels, self-modifying weights via a self-referential process, and CMS multi-scale memory. Hope reportedly beats Titans, TTT, and Mamba2 on long-context needle-in-a-haystack and continual-learning tasks. **[CONFIRMED]** [10]

Practically, three families are converging: (a) **test-time training / fast weights** (TTT, Titans, Hope), (b) **hybrid linear-attention recurrent state** as de facto working memory (Gated DeltaNet, Mamba2), and (c) **very long context plus retrieval** as a brute-force substitute. Million-token context is now economically feasible at production scale; 10M+ remains a research and marketing frontier rather than a routine deployment mode. **[SPECULATION]** on the 10M+ characterization.

---

## 4. Architecture shifts

**Sparse attention.** DeepSeek Sparse Attention (DSA), introduced in V3.2-Exp, splits each attention layer into selection and computation: a lightweight "lightning indexer" scores prior tokens via multi-head ReLU-gated dot products, then top-*k* (k=2048) positions get full attention. This reduces per-layer cost from O(L²) to O(Lk) — **~98% fewer attention FLOPs at 128K context, up to 2× lower per-token GPU cost** — with essentially unchanged output quality. **[CONFIRMED]** [11][12] DeepSeek-V4 (arXiv 2606.19348) interleaves **Compressed Sparse Attention** and **Heavily Compressed Attention**, making million-token context practical. **[CONFIRMED]** [13]

**Hybrid attention is now the default, not the experiment.** Qwen3-Next (2025) was the first near-flagship model to interleave linear-attention blocks with full attention (3 Gated DeltaNet : 1 Gated Attention). By Qwen3.5, roughly **75% of layers are linear attention, 25% softmax** — linear layers give O(1)-per-token inference and a compact recurrent state cache; full-attention layers preserve global retrieval. Gated DeltaNet itself is Mamba2's gated decay plus the DeltaNet fast-weight update rule. **[CONFIRMED]** [14]

**MoE at scale** is universal at the frontier and no longer differentiating on its own; the differentiation moved to routing stability, expert granularity, and how MoE interacts with the data wall (sparse models are more data-hungry per unit of quality). **[SPECULATION]**

**Diffusion LLMs** crossed from research to product. Gemini Diffusion (~1,479 tok/s), Mercury 2 (~1,009 tok/s on a single Blackwell GPU, >5× Claude 4.5 Haiku Reasoning at ~89 tok/s), Seed Diffusion Preview (2,146 tok/s on H20). The dominant 2026 recipe is **AR-initialized, diffusion-continued**, with **block diffusion at ~32-token blocks** as the production standard. **[CONFIRMED]** [25] Diffusion LLMs are winning on latency-sensitive code generation; they have not yet demonstrated frontier-level reasoning.

---

## 5. Pretraining data limits and synthetic data

Epoch AI's estimate — ~**300 trillion tokens** of effective, quality- and repetition-adjusted public human text, with an 80% CI that the stock is exhausted **between 2026 and 2032** — remains the anchor number. **[CONFIRMED]** [26]

Two escapes are real: **reasoning-focused synthetic data** and **multimodal data**. Both are being used at scale. The constraint is that unconstrained synthesis risks model collapse, and grounding synthetic data in source content is necessary — the 2026 work on *synthetic megadocs* and organic-data-derived token generation is essentially about staying grounded while multiplying tokens. **[CONFIRMED]** [26]

Meanwhile compute is not the binding constraint it was: the largest-datacenter record has doubled roughly every **7 months** since Colossus 1 (Aug 2024); Colossus is planned to 1.5 GW, Abilene Stargate to 1.2 GW, with 10 GW training clusters projected by decade's end. **[CONFIRMED]** [26]

---

## 6. Self-improvement loops

The 2026 picture: real, measurable, useful — and not recursive.

AlphaEvolve established evolutionary LLM-driven algorithm discovery as a genuine capability. By mid-2026 it had successors: **MLEvolve** (arXiv 2606.06473), a self-evolving framework that reports beating AlphaEvolve on mathematical algorithm optimization and achieving SOTA on MLE-Bench medal rate under a 12-hour budget; **Frontis-MA1** (arXiv 2607.28568), explicitly trained as an "AI4AI" model for recursive self-improvement in ML engineering; and **AI4AI-Bench** (arXiv 2608.20318), a benchmark for exactly this loop. **[CONFIRMED]** [17][18]

RE-Bench (ML research engineering), PaperBench (paper reproduction), and MLE-Bench (Kaggle-style ML engineering) form the measurement layer. There is also a documented result that frontier coding agents can now implement an AlphaZero self-play pipeline for Connect Four that performs comparably to an external solver (arXiv 2604.25067). **[CONFIRMED]**

What is *not* demonstrated: any system that improves the model that produced it, in a closed loop, without human-designed scaffolding and human-chosen objectives. Every current "self-improvement" result is search over a fixed model's outputs, scored by a human-specified verifier. **[SPECULATION]** that this remains the binding constraint through 2027.

---

## 7. World models

The field split cleanly. **[CONFIRMED]** [15][16]

- **Render to predict**: Genie 3 (DeepMind, Aug 2025) — the first real-time, general-purpose interactive world model, navigable 3D worlds at **24 fps** with ~**1 minute** of environment memory (vs. Genie 2's 10–20 seconds). NVIDIA Cosmos for physical-AI synthesis; the Sora lineage for video.
- **Compress to understand**: V-JEPA 2 (Meta) predicts in abstract representation space and demonstrated planning — but not extended behavior, online learning, or open-ended tasks. Dreamer 4 achieved the **first offline Minecraft diamond**.

The 2026 consensus is that these converge: JEPA-style latent prediction for planning efficiency, generative rendering for environment supply. **[SPECULATION]** The deeper connection to this memo's theme: a world model *is* latent reasoning with a temporal axis. Recurrent depth and latent world modeling are the same bet — that the useful representation is not the token.

---

## 8. Interpretability

Mechanistic interpretability was named an **MIT 2026 Breakthrough Technology**. **[REPORTED]** [27] The 2026 state of the art:

- **Circuit tracing / attribution graphs** matured from artisanal to tooled, including agents that read attribution graphs, isolate subcircuits, and describe them. **[CONFIRMED]** [27]
- **Sparse autoencoders** moved from "find interpretable features" to **model diffing** — comparing SAE latents across model variants. OpenAI's alignment team published SAE latent attribution for debugging misaligned completions: steer on a latent, sample, grade with an LLM judge, and get a causal measurement per latent. **[CONFIRMED]** [28]
- **Emergent misalignment** got a mechanistic account via feature superposition geometry (arXiv 2605.00842), and — practically important — **regular monitoring of SAE latent activations gives early warning of misalignment before any behavioral failure appears.** **[CONFIRMED]** [28]
- A counter-current worth noting: *Causality is Key for Interpretability Claims to Generalise* (arXiv 2602.16698) is part of a 2026 methodological tightening; a lot of 2024–25 SAE work does not replicate causally. **[CONFIRMED]**

**The collision.** Interpretability's most reliable safety tool in 2024–25 was not SAEs — it was reading the chain of thought. Recurrent depth attacks that directly: computation that happens inside the loop, between token emissions, produces no legible trace. This is why the Astra architecture report generated more alignment-community discussion than its benchmarks did. **[REPORTED]** [1][2]

---

## 9. Efficiency: precision, optimizers, distillation

**Low-precision training.** MXFP4 (4-bit with fine-grained per-group scaling, native on Blackwell) is now **competitive with FP8 on accuracy-vs-speed**. The main obstacle identified and solved in 2026 was **weight oscillation**, addressed with EMA quantizers (Q-EMA) and adaptive ramping (Q-Ramping). Full-Stack FP4 (arXiv 2607.04422) jointly quantizes projections, optimizer states, and attention to NVFP4 within one pretraining stack; Quartet argued native FP4 training can be *optimal*, not merely tolerable. HiFloat4 does the same for Ascend NPUs. **[CONFIRMED]** [29][30]

**Optimizers.** Muon moved from curiosity to production-adjacent, and 2026 work targets **low-bit Muon** via subspace preservation and grid quantization — optimizer-state compression is now part of the precision story rather than separate from it. **[CONFIRMED]** [29]

**Distillation and the cost curve.** Inference cost for GPT-4-equivalent capability fell from ~$20/M tokens (late 2022) to ~$0.40/M (2026) — roughly **1,000× in three years**. Distilled models routinely retain 90%+ of teacher capability at 4–8× lower GPU requirement. The drivers (hardware, kernels, architecture, quantization) are **multiplicative**, each contributing 2–3×. **[CONFIRMED/REPORTED]** [31] Epoch's caveat is worth keeping: distilled models over-perform on benchmarks relative to their real capability, so the curve is somewhat flattered.

---

## What people are underestimating

*(All items in this section are labeled analysis — **[SPECULATION]** unless otherwise noted.)*

**1. The token-efficiency number is the real news, not the benchmark scores.** Astra ties on Intelligence Index and loses to Fable 5.1 on coding agents, which produced a wave of "GPT-6 disappoints" coverage. But it does the same work in **one-third the tokens**. **[CONFIRMED]** [5] In an agentic world where cost and latency scale with serialized reasoning tokens, a 3× reduction changes which workloads are economically viable more than 3 points of index does. The commentary is scoring the wrong axis.

**2. "Recurrent depth" is being over-read as an architecture and under-read as a *safety governance decision*.** The genuinely notable fact is not that OpenAI looped a block — it's that they reportedly **capped the loop count to stay within 2× of GPT-4's computation-graph depth** specifically to preserve CoT legibility. **[REPORTED]** [2] That is a frontier lab voluntarily leaving capability on the table for monitorability. It is also a cap that competitive pressure will test, and there is no mechanism ensuring anyone else adopts it.

**3. The no-CoT horizon curve is the most under-watched safety metric in the field.** METR's *agentic* time horizon gets all the attention; the no-CoT horizon (373-day doubling, ~3 min at GPT-5.5) determines how much reasoning can happen where no monitor can see. **[CONFIRMED]** [20][21] Recurrent depth is a direct multiplier on it, and the ~1.3×-layers-per-doubling relationship means architectural changes move this curve far faster than scale does.

**4. Continual learning may be solved by memory systems, not by a new learning rule.** The Sutton framing implies a fundamental algorithmic discovery is needed. Nested Learning/Hope suggests something less dramatic: a *continuum* of memory modules at different update frequencies may recover most of what "learning on the job" means, without abandoning the transformer. **[CONFIRMED]** that Hope exists and reports gains [10]; **[SPECULATION]** that this is sufficient. If it is, the 2027 story is boring incremental memory engineering rather than a paradigm break — and Sutton is directionally right about the gap but wrong about the required remedy.

**5. RLVR's generalization failure is the quiet crisis.** Every RL-scaling chart implicitly assumes math/code gains transfer. The public evidence for transfer beyond verifiable domains is thin. **[REPORTED]** [6] If RLVR turns out to be domain-bounded, the RL-compute curve flattens exactly when labs have committed capex to it, and the "RL rivals pretraining" thesis becomes an expensive detour.

**6. Efficiency, not capability, is where the compounding discontinuity actually lives.** DSA's ~98% attention-FLOP reduction × hybrid linear attention × native FP4 × 3× token efficiency × 1,000× three-year inference cost decline. **[CONFIRMED]** [11][14][29][31] These multiply. A 2026 dollar buys something like four orders of magnitude more frontier-quality inference than a 2022 dollar. That, more than any benchmark, is the discontinuity — it changes what you can afford to *deploy*, which changes what gets built.

**7. Self-improvement benchmarks are measuring the wrong loop.** AI4AI-Bench, MLE-Bench and RE-Bench measure whether an agent can do ML engineering. The thing that matters is whether an agent can *choose what ML engineering to do*. Every current result holds the objective fixed and searches within it. Until a benchmark measures objective selection, "recursive self-improvement" scores are measuring competent labor, not recursion.

**8. Latent reasoning and world models are one research program, not two.** COCONUT holding search frontiers in superposition [19] and V-JEPA 2 predicting in abstract representation space are the same claim: the useful state is not the token, and forcing it through language is a lossy bottleneck. If that claim is right, the 2027–28 frontier model is a latent-state machine with a language interface bolted on — and the entire CoT-monitoring safety stack was a transitional artifact of an architecture that happened to think out loud.

---

## Key numbers

| Quantity | Value | Status | Src |
|---|---|---|---|
| GPT-6 Astra release | Sept 3, 2026 (preview), Sept 4 (paid) | CONFIRMED | [1] |
| Astra pretraining GPUs | >100,000 (first OpenAI run over threshold) | CONFIRMED | [1] |
| Astra loop count | ~3–4 (inferred from "within 2× GPT-4 depth") | REPORTED/SPEC | [2] |
| Astra coding token efficiency | ~1/3 of GPT-5.6 Sol; ~1/5 of Opus 5 (xhigh) | CONFIRMED | [5] |
| Astra Intelligence Index | 61 (ties Sol; Fable 5.1 leads by ~5) | CONFIRMED | [5] |
| Astra Coding Agent Index | 67 (Fable 5.1 = 70) | CONFIRMED | [5] |
| Astra AA-Briefcase | ~+80 Elo | CONFIRMED | [5] |
| Astra hallucination (AA-Omniscience) | 92% → 51% | CONFIRMED | [5] |
| Astra pricing | $10 / $50 per M tokens (2.5× Sol) | CONFIRMED | [5] |
| Astra ExploitBench | 100%; 2 zero-days chained in eval | CONFIRMED | [3] |
| Astra cyber-jailbreak refusal | 91.5% vs 59% (Sol) | CONFIRMED | [3] |
| Geiping recurrent-depth model | 3.5B params / 800B tokens → ~50B-equiv compute | CONFIRMED | [4] |
| No-CoT time horizon doubling | 373 days (CI 167–691) | CONFIRMED | [20] |
| No-CoT token horizon doubling | 437 days | CONFIRMED | [20] |
| GPT-5.5 no-CoT 50% horizon | ~3 min / ~1,500 o3-mini tokens | CONFIRMED | [20] |
| No-CoT horizon vs. layers | 1.3× layers per horizon doubling | REPORTED | [2] |
| METR agentic horizon doubling | ~129 days (2023+); ~89 days (2024+) | CONFIRMED | [32] |
| DeepSeek-R1-Zero RL compute | 100k H800-hrs = 3.75% of pretraining | CONFIRMED | [7] |
| o1→o3 RL compute increase | >10× (also Grok-3→Grok-4) | REPORTED | [7] |
| DSA attention FLOP reduction | ~98% at 128K ctx (top-k = 2048); up to 2× cost | CONFIRMED | [11][12] |
| Qwen3.5 layer mix | ~75% linear attention / 25% softmax | CONFIRMED | [14] |
| Genie 3 | 24 fps real-time, ~1 min memory | CONFIRMED | [15] |
| Diffusion LLM speed | 1,009–2,146 tok/s (Mercury 2 / Seed Diffusion) | CONFIRMED | [25] |
| Effective public text stock | ~300T tokens; exhausted 2026–2032 (80% CI) | CONFIRMED | [26] |
| Datacenter scale doubling | ~7 months since Aug 2024; 10 GW by 2030 | CONFIRMED | [26] |
| Inference cost decline | ~1,000× in 3 yrs ($20 → $0.40 per M) | REPORTED | [31] |
| Frontier RL-environment spend | 3–5× growth into 2026 | REPORTED | [24] |

---

## Sources

1. Wikipedia, "GPT-6 Astra" — https://en.wikipedia.org/wiki/GPT-6_Astra (accessed 2026-09-07; release Sept 3–4, 2026; *The Information* report Sept 1, 2026)
2. LessWrong, "How concerned should we be about Astra's recurrent architecture?" — https://www.lesswrong.com/posts/PLisnSFir8y5AHkmP/how-concerned-should-we-be-about-astra-s-recurrent (Sept 2026)
3. Atoms.dev, "OpenAI Astra: GPT-6, Recurrent Depth and Release Status" — https://atoms.dev/blog/openai-astra-gpt-6-mewfour-release-date (Sept 2026)
4. Geiping, McLeish et al., "Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach," arXiv:2502.05171 (Feb 2025; NeurIPS 2025) — https://arxiv.org/abs/2502.05171v2
5. Artificial Analysis, "Benchmarking GPT-6 Astra" — https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra (Sept 2026)
6. LessWrong, "Slowdown After 2028: Compute, RLVR Uncertainty, MoE Data Wall" — https://www.lesswrong.com/posts/XiMRyQcEyKCryST8T/slowdown-after-2028-compute-rlvr-uncertainty-moe-data-wall
7. Khatri et al., "The Art of Scaling Reinforcement Learning Compute for LLMs," arXiv:2510.13786 — https://arxiv.org/html/2510.13786v1
8. Dwarkesh Patel, "Richard Sutton — Father of RL thinks LLMs are a dead end" — https://www.dwarkesh.com/p/richard-sutton (Sept 2025)
9. Nathan Lambert, "Contra Dwarkesh on Continual Learning," Interconnects — https://www.interconnects.ai/p/contra-dwarkesh-on-continual-learning
10. Google Research, "Introducing Nested Learning: A new ML paradigm for continual learning" — https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/ (Nov 2025)
11. DeepSeek, DeepSeek-V3.2-Exp (DSA) — https://github.com/deepseek-ai/DeepSeek-V3.2-Exp (Sept 2025)
12. EmergentMind, "DeepSeek Sparse Attention Mechanism (DSA)" — https://www.emergentmind.com/topics/deepseek-sparse-attention-dsa
13. "DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence," arXiv:2606.19348 — https://arxiv.org/pdf/2606.19348 (June 2026)
14. Sebastian Raschka, "Hybrid Attention" / Qwen3.5 analysis — https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/ and https://huggingface.co/blog/mlabonne/qwen35
15. Wikipedia, "Genie (world model)" — https://en.wikipedia.org/wiki/Genie_(world_model) (Genie 3, Aug 2025)
16. Pebblous, "World Models Explained 2026 — The Two Paths" — https://blog.pebblous.ai/report/world-model-survey-2026/en/
17. "MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery," arXiv:2606.06473 — https://arxiv.org/abs/2606.06473
18. "AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement," arXiv:2608.20318 — https://arxiv.org/html/2608.20318 ; "Frontis-MA1," arXiv:2607.28568
19. Hao et al. (Meta FAIR), "Training Large Language Models to Reason in a Continuous Latent Space" (COCONUT), arXiv:2412.06769 — https://arxiv.org/abs/2412.06769 ; theory: arXiv:2505.12514
20. "Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models," arXiv:2606.07157 — https://arxiv.org/html/2606.07157 (June 2026)
21. Redwood Research blog, "Estimating No-CoT Task-Completion Time Horizons" — https://blog.redwoodresearch.org/p/estimating-no-cot-task-completion (June 2026)
22. Vellum, "GPT-6 Astra Benchmarks Explained" — https://www.vellum.ai/blog/gpt-6-astra-benchmarks-explained (Sept 2026)
23. "AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn RL," arXiv:2509.08755 (ICLR 2026) — https://arxiv.org/abs/2509.08755
24. Wing Venture Capital, "Who Will Win the RL Environment Market — and Why" — https://www.wing.vc/content/who-will-win-the-rl-environment-market--and-why (2026)
25. Daily Dose of DS, "Diffusion LLMs from the Ground Up" — https://www.dailydoseofds.com/diffusion-models-part-2/ ; "Seed Diffusion," arXiv:2508.02193
26. Epoch AI, "Will we run out of data to train large language models?" — https://epoch.ai/publications/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data ; "AI in 2030" — https://epoch.ai/files/AI_2030.pdf
27. SPAR Spring 2026 project list (attribution-graph agents, goal detection) — https://sparai.org/projects/sp26/
28. OpenAI Alignment, "Debugging misaligned completions with sparse-autoencoder latent attribution" — https://alignment.openai.com/sae-latent-attribution/
29. "Full-Stack FP4: Stable LLM Pretraining with Quantized Projections, Optimizers, and Attention," arXiv:2607.04422 — https://arxiv.org/html/2607.04422 (July 2026)
30. "Quartet: Native FP4 Training Can Be Optimal for Large Language Models," arXiv:2505.14669 — https://arxiv.org/html/2505.14669v4 ; "Oscillation-Reduced MXFP4 Training," arXiv:2502.20853
31. Epoch AI, "How persistent is the inference cost burden?" — https://epoch.ai/gradient-updates/how-persistent-is-the-inference-cost-burden ; GPUnex, "AI Inference Economics: The 1,000× Cost Collapse" — https://www.gpunex.com/blog/ai-inference-economics-2026/
32. METR, "Time Horizon 1.1" — https://metr.org/blog/2026-1-29-time-horizon-1-1/ (Jan 2026) and "Clarifying limitations of time horizon" — https://metr.org/notes/2026-01-22-time-horizon-limitations/
