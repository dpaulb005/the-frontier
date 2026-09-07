# AI That Does Science and Engineering: The Automated-Researcher Trajectory as of September 2026

*Research report — compiled 2026-09-07. Claims are labeled **CONFIRMED** (primary source or replicated public record), **REPORTED** (credible secondary reporting, single-source, or vendor claim not independently verified), or **SPECULATION** (forecast, extrapolation, or my own analysis).*

---

## TL;DR

1. **Math fell first, and faster than almost anyone predicted.** IMO gold went from "not yet" (2024 silver) to two labs at gold in July 2025 to a commodity capability in 2026. The frontier moved to *research-level* math: original solutions to open Erdős problems, verified by Fields medalists, and an improvement to the matrix-multiplication exponent ω. **CONFIRMED**

2. **The Erdős story is the cleanest case study in how to read AI-science claims.** October 2025's "GPT-5 solved 10 open problems" was a literature-search artifact and was retracted in substance. January–May 2026's results (Erdős #397, #728, #729, and DeepMind's Lean-verified batch) appear to be genuinely novel proofs. Same headline, opposite epistemics. **CONFIRMED (the retraction) / REPORTED (novelty of the 2026 proofs)**

3. **Formal verification is the load-bearing infrastructure.** Lean/AlphaProof-style pipelines convert "an LLM says it proved this" into a machine-checkable object. Where formalization exists, AI math claims have held up; where it doesn't, they have repeatedly deflated. **CONFIRMED**

4. **Terence Tao has become the de facto standards body.** His ICM 2026 essay ("Mathematics in the age of AI") reframes the debate from capability to *what mathematics is for*, and proposes concrete norms: disclosure of tool use, and authors must be able to give an expert talk on their own AI-assisted result. **CONFIRMED**

5. **AlphaEvolve is the most economically legible science-AI system.** It found a 48-multiplication scheme for 4×4 complex matrices (first improvement on Strassen in that setting in 56 years), recovered real datacenter compute at Google, and in August 2026 was part of the pipeline that pushed ω below 2.371177. **CONFIRMED**

6. **Biology's flagship claim — an AI-designed drug in humans — arrived late and small.** Isomorphic Labs slipped from "end of 2025" to 2026 and began oncology-first human trials in 2026. **REPORTED.** The real volume story is antibodies: Chai-2 hit double-digit zero-shot de novo hit rates, Chai-3 roughly doubled that, and Lilly, Pfizer, Novartis and BMS all signed on during 2026. **CONFIRMED (partnerships) / REPORTED (hit rates)**

7. **Autonomous-discovery agents produced their first Nature-grade results.** FutureHouse's Robin identified ripasudil for dry AMD end-to-end and published in Nature (May 2026); Kosmos claims ~6 months of research per day with ~80% finding accuracy (self-assessed); Google's Co-Scientist graduated from demo to Nature paper with wet-lab-validated hypotheses. **CONFIRMED (publications) / REPORTED (accuracy claims)**

8. **A fully AI-generated paper passed human peer review — at a workshop.** Sakana's AI Scientist-v2 result was published in Nature in March 2026. As of mid-2026 no AI-solo-authored paper had cleared a main-track journal or conference. The gap between those two facts is the whole story. **CONFIRMED**

9. **The AI-accelerating-AI loop is now measured, not just asserted.** METR's time horizons show post-2024 doubling near ~3 months (89 days) with the best models at ~16–20 hours on the 50% horizon; OpenAI declared its "automated research intern" milestone on 2026-09-06 and reports 3.1 agent-workdays per human workday internally, targeting a "legitimate AI researcher" by March 2028. **CONFIRMED (announcements) / REPORTED (internal metrics)**

10. **The binding constraint has moved from cognition to the physical world.** Nothing in the 2026 record shows AI short-circuiting synthesis, characterization, animal models, or clinical trials. The systems that look fastest are exactly the ones whose verification loop is symbolic (math, code, kernels) rather than material. **ANALYSIS**

---

## 1. Mathematics: from competition gold to research contributions

### The olympiad ladder

Google DeepMind's AlphaProof/AlphaGeometry hybrid reached **silver** at IMO 2024. In July 2025 both Google DeepMind (with an advanced Gemini Deep Think) and OpenAI reported **gold-medal-standard** performance: 5/6 problems, 35/42 points, against a field where only ~67 of 630 human contestants (~10%) took gold [1][2][3]. **CONFIRMED**

An important asymmetry that shaped later credibility fights: DeepMind's run was graded under IMO's official process, while OpenAI evaluated itself on the publicly released problems and self-graded. The IMO could not verify OpenAI's claim [1][3]. **CONFIRMED**

By 2026 the competition-math frontier is essentially closed as a research question. Gemini 3-class and GPT-5.x-class models reach gold-level performance as a routine capability rather than a bespoke system, and prediction markets treated "AI wins IMO gold in 2026" as near-consensus rather than a live question [4]. **REPORTED**

### Erdős problems: the retraction and the real results

October 2025 produced the canonical cautionary tale. An OpenAI VP posted that GPT-5 had "found solutions to 10 previously unsolved Erdős problems and made progress on 11 others." It had not: it had found *existing* solutions in the literature that the problem database had marked open. The claim was withdrawn [5]. **CONFIRMED**

The 2026 results are different in kind:

- **January 2026:** GPT-5.2 autonomously produced a solution to open Erdős problem **#397**, verified by Terence Tao. Problems **#728** and **#729** followed. These are described as original proofs — assembled from known techniques, but not present in the prior literature [5][6]. A Lean formalization of the #728 proof was written up separately [7]. **REPORTED**
- **May 2026:** OpenAI reported that GPT-5.4 Pro resolved a ~60-year-old (in some tellings 80-year-old) Erdős conjecture from a single prompt in roughly 80 minutes, using an approach not previously applied to the problem [8][9]. **REPORTED**
- **May 21, 2026:** Google DeepMind published, one day later, results from an AlphaProof successor solving nine further Erdős problems with Lean-verified formal proofs [8]. **REPORTED**

The community-maintained ledger of AI contributions to the Erdős problem list is the best-calibrated public source here, precisely because it distinguishes "found in literature," "solved with human guidance," and "solved autonomously" [5]. **CONFIRMED**

### Benchmarks: FrontierMath and the saturation clock

Epoch AI's FrontierMath went from **<2% solved by every model tested at launch (Nov 2024)** to **~88% top scores in 2026** — a >40× improvement in under two years [10][11]. Epoch expects saturation within two years, possibly sooner. **CONFIRMED**

The structure underneath matters more than the headline:

- A **June 12, 2026** v2 release corrected errors in **42%** of problems, leaving 338 problems. Benchmark error rates at this level are a standing warning about all AI-science benchmark claims [10]. **CONFIRMED**
- **Tier 4** (the hardest tier) leads below **40%**, with most models in single digits [10]. **CONFIRMED**
- On **July 31, 2026**, Epoch launched **FrontierMath: Open Problems** — 50 genuinely unsolved research problems. **AI has solved three** [10]. **CONFIRMED**

That last number is the most informative single statistic in AI-for-math right now: 3/50 on real open problems, against ~88% on hard-but-solved problems. **ANALYSIS**

### Tao's framework

Tao's ICM 2026 lecture and accompanying essay, *Mathematics in the age of AI* (arXiv 2608.16753, August 2026), deliberately sidesteps capability forecasting [12][13]. His argument: problem-solving is one stage of five — proof generation, **verification, exposition, publication, and canonicalization** — and AI is currently strong at the first and weak-to-absent at the rest.

His proposed norms are concrete and are being adopted piecemeal by journals and conferences: **mandatory disclosure of tool use**, and **authors must be able to give a clear expert-level talk on their own AI-assisted result** or the work should not be published [12]. **CONFIRMED**

Related: **First Proof**, an independent assessment running batches of ten novel research-level problems against frontier harnesses. In the second batch (tested 2026-05-28), **7 of 10** problems were solved at publication-level quality by at least one team, at **$10–$1,000 of compute per problem** [12]. **REPORTED** — and note the cost figure, which is the number that makes this an economic story rather than a curiosity.

---

## 2. Algorithms, kernels, and chips

### AlphaEvolve

AlphaEvolve — an evolutionary coding agent wrapping Gemini, published as arXiv 2506.13131 [14] — is the clearest existence proof that LLM-driven search can produce *deployed* engineering artifacts rather than papers.

Confirmed results:
- A procedure multiplying two **4×4 complex matrices in 48 scalar multiplications**, the first improvement over Strassen's approach in that setting in **56 years** [14][15]. **CONFIRMED**
- Recovery of on the order of **0.7% of Google's global datacenter compute** through a discovered scheduling heuristic, plus TPU circuit and kernel improvements — i.e., value realized in production, not in a benchmark [16]. **REPORTED**
- **August 17, 2026:** a paper establishing **ω < 2.371177**, improving the prior bound of 2.371339, with AlphaEvolve used as the final refinement step in a larger optimization pipeline. Authors include DeepMind researchers alongside Josh Alman and Virginia Vassilevska Williams, who held the previous record [17]. **CONFIRMED**

The ω improvement is worth reading carefully: the delta is ~0.000162 and has no practical consequence. Its significance is sociological — the human record-holders co-authored with the machine, and the machine's contribution was a *refinement step inside a human-designed pipeline*, not an end-to-end discovery. **ANALYSIS**

### AI-written GPU kernels

2026 saw a dense wave of kernel-generation work: ParallelKernelBench (multi-GPU kernel generation), KernelFoundry (hardware-aware evolutionary optimization), STARK, Xe-Forge (Intel GPUs), AscendCraft (Huawei NPUs), and PEAK [18]. KernelBench remains the reference testbed for correctness-plus-speed. **CONFIRMED**

The honest summary: LLM agents now routinely produce correct kernels and frequently beat naive baselines, but "beats an expert-tuned production kernel on a workload that matters" remains selective rather than general. The proliferation of vendor-specific benchmarks (Ascend, Intel, multi-GPU) is itself evidence that the wins are workload-specific. **ANALYSIS**

**AlphaChip** — DeepMind's RL floorplanning system used across multiple TPU generations — remains the longest-running deployed instance of AI doing engineering design, and also the most contested, with published replication disputes. It is a useful reminder that "AI designed our chip" claims have a decade-long history of being harder to verify than they sound. **REPORTED**

---

## 3. Biology, chemistry, and materials

### Structure prediction → drug design

**AlphaFold 3** (2024) extended prediction from proteins to protein–ligand, protein–nucleic-acid, and modified-residue complexes, and is the technical basis of **Isomorphic Labs** [19]. **CONFIRMED**

Isomorphic's timeline is the single most useful reality check in AI-for-biology:
- 2024: Hassabis says AI-designed drugs in trials by **end of 2025**.
- January 2026 (Davos): slipped to **end of 2026** [20].
- 2026: human trials commence, **oncology first** [21][22]. **REPORTED**

Two years of slip on a two-year promise, from the best-resourced team in the field. Nothing about the underlying science was wrong; the bottleneck was everything downstream of design. **ANALYSIS**

### Antibodies: the fastest-moving real application

De novo antibody design is where AI has most clearly changed a wet-lab workflow:
- **Chai-2** (June 2025) was the first zero-shot platform to reach **double-digit experimental hit rates** in de novo antibody design — reported as a ~100× improvement over prior methods, compressing discovery from months to weeks [23]. **REPORTED**
- **Chai-3** (2026) roughly **doubled** that: reported ~50% of designs binding at therapeutic affinities [24]. **REPORTED**
- Commercial validation in 2026: **Eli Lilly** (Jan 9/12, 2026), then **Pfizer**, **Novartis**, and **Bristol Myers Squibb** (Aug 20, 2026) [23][24][25]. **CONFIRMED**

Big-pharma money is a stronger signal than a hit-rate number, because pharma partners see the failed designs too. **ANALYSIS**

### Materials

- **GNoME** (DeepMind, 2023) identified **381,000** new stable materials, later expanded past **520,000** within 1 meV/atom of the convex hull [26]. **CONFIRMED**
- **MatterGen** (Microsoft Research) trained on 600,000+ DFT-verified structures, generates structures >2× more likely to be stable-unique-new than predecessors, rediscovered 2,000+ known-but-unseen experimental structures, and had **one** generated material (TaCr₂O₆) experimentally validated [27]. **CONFIRMED**
- A 2026 evaluation found diffusion models (MatterGen, DiffCSP) perform stably in well-sampled chemical spaces (ternary oxides, nitrides) but **degrade in unusual spaces** — including the GNoME distribution itself, which is rich in rare-earth and unconventional stoichiometries [27]. **CONFIRMED**

The ratio to hold in mind: **~10⁵–10⁶ computationally predicted materials vs. single-digit experimentally validated novel ones.** Universal machine-learning interatomic potentials (MLIPs) are the piece that could actually close this gap — they now support condensed-phase MD and zero-shot property prediction (e.g. ionic conductivity) at near-DFT accuracy — but published assessments still flag surfaces and defects as weak spots [28]. **ANALYSIS**

### Self-driving labs and the new AI-science companies

- **Periodic Labs** — founded 2025 by Liam Fedus (ex-OpenAI VP of research, ChatGPT co-creator) and Ekin Doğuş Çubuk (led GNoME's materials work). **$300M seed** led by a16z in Sept 2025; reported in talks in 2026 at a **$7B+ valuation**. North star: a high-temperature superconductor, via AI scientists coupled to autonomous labs [29][30]. **CONFIRMED (funding) / REPORTED (valuation talks).** No published experimental discovery as of this writing. **CONFIRMED (absence)**
- **Lila Sciences** — "AI Science Factories," robotic labs running continuous AI-directed experiments; No. 25 on CNBC's 2026 Disruptor 50; reports early proof of concept in novel antibodies and carbon-capture materials [31]. **REPORTED**
- **FutureHouse / Edison Scientific** — **Robin**, a multi-agent system, autonomously generated hypotheses, designed experiments, analyzed data and identified **ripasudil** (an existing glaucoma drug) as a candidate therapy for **dry age-related macular degeneration**; concept-to-paper in **2.5 months**, published in **Nature, May 19, 2026** [32][33]. **CONFIRMED.** **Kosmos** claims six months of research per day, reading 1,500+ papers and running 42,000 lines of analysis code per run, with **~80% of findings accurate by internal evaluation**; seven claimed discoveries with academic beta testers, three replicating unpublished/recent human findings and four novel (including a genetic mechanism possibly reducing type 2 diabetes risk, and a SOD2–cardiac-fibrosis link) [34]. **REPORTED**
- **Google Co-Scientist** — Gemini-based multi-agent system, graduated from demo to a **Nature** publication in 2026. Validated instances: a drug-repurposing candidate for liver fibrosis that blocked **91%** of a scarring-linked response in lab tests (Gary Peltz, Stanford); a novel integrated-stress-response hypothesis later confirmed in the lab at Calico; antimicrobial resistance and plant immunity work [35][36][37]. **CONFIRMED (publication) / REPORTED (individual results).** Explicitly **lab-validated, not clinic-validated** [37].

---

## 4. AI-generated papers and peer review

Sakana AI's **AI Scientist** (Aug 2024) and **AI Scientist-v2** (2025) run the full loop: idea generation, code, experiments, plots, manuscript, and self-review. A v2-generated paper became the **first fully AI-generated paper to pass human peer review**, and the work was published in **Nature on March 25, 2026** [38][39][40]. **CONFIRMED**

Three qualifications that the coverage usually buries:
1. The accepted paper was at a **workshop track**, not a main conference or journal [38][41]. **CONFIRMED**
2. As of April 2026, **no AI-solo-authored paper had been published in a major peer-reviewed journal** [41]. **CONFIRMED**
3. Independent evaluations of the AI Scientist have been mixed, finding the generated work often technically valid but low-novelty [42]. **CONFIRMED**

The 2026 arXiv literature has since filled with successors — ScientistOne, PaperOrchestra, ResearchEVO — which is itself the signal: automated paper generation is now a crowded engineering subfield, and journals' review capacity is the constraint being tested. **ANALYSIS**

---

## 5. Fusion and plasma control

DeepMind's 2022 *Nature* result — deep RL controlling tokamak magnets to stabilize plasma shapes, with EPFL's Swiss Plasma Center — remains the canonical demonstration that learned controllers can run real physical apparatus in real time [43]. **CONFIRMED**

Since October 2025, DeepMind has partnered with **Commonwealth Fusion Systems** on AI plasma control for **SPARC**, using **TORAX** (a differentiable plasma simulator) plus RL/evolutionary search to explore operating scenarios in simulation before the machine runs at power [44][45][46]. SPARC targets first plasma in 2026 and net energy (Q>1) in 2027. **REPORTED**

Adjacent confirmed work: AI-based suppression of **tearing-mode instabilities** (DIII-D, Princeton/DOE), and real-time image-analysis control of divertor detachment [47]. 2026 added an offline-RL benchmark and codebase for plasma control, which matters because it lets non-tokamak-owning researchers work on the problem [48]. **CONFIRMED**

Note the shape of the claim here: AI is doing **control and scenario optimization**, not fusion physics discovery. That is a real engineering contribution with a clean verification loop (the plasma either holds or it doesn't). **ANALYSIS**

---

## 6. AI accelerating AI research

### The measurement layer

**METR time horizons** — the length of task (measured in human-expert time) a model completes with 50% reliability — is the most-cited quantitative handle on the loop [49][50]:

- Under the revised **Time Horizon 1.1** methodology (Jan 2026), the post-2023 doubling time is **131 days**, vs. 165 days under TH1 — i.e., ~20% faster than previously estimated. **CONFIRMED**
- All-time doubling: **188 days**. From 2023: **129 days**. From 2024: **89 days (~3 months)** [50]. **CONFIRMED**
- The strongest assessed agents in 2026 are **at or beyond the reliable measurement range** of TH1.1, with the most capable shared model estimated near **16–20 hours at 50%** and **3–4 hours at 80%** [49]. **REPORTED**

METR itself published a note (2026-01-22) on the metric's limitations [51] — the tasks are software/research-engineering tasks with clean scoring, and the extrapolation to open-ended research is not warranted by the data. **CONFIRMED**

### OpenAI's declared milestones

On **2026-09-06**, OpenAI announced it had met the goal Sam Altman set in October 2025: an **"automated research intern" by September 2026** [52][53][54]. Definitions matter enormously:

- OpenAI defines it narrowly: a **supervised** system completing **well-defined** research tasks that would take a skilled researcher **a few days** [52][55]. **CONFIRMED**
- Reported internal metric: **3.1 agent-workdays of effort per workday of human labor** across the research org [53][56]. **REPORTED**
- Next target: a **"legitimate AI researcher" by March 2028** [52][54]. **CONFIRMED (as a stated target)**

What it is explicitly *not*: an autonomous scientist, an unsupervised research program, or a system that chooses its own research priorities [55]. **CONFIRMED**

### The rest of the field

Anthropic has said publicly that a large and growing majority of the code in Claude Code is written by Claude, and frames internal model-assisted engineering as a primary driver of its own velocity. **REPORTED**

Forecasting artifacts: **AI 2027** (Kokotajlo et al.) sits at the aggressive end, with a superhuman-coder-then-fast-takeoff structure; the AI 2027 tracker now benchmarks its predictions against reality, including the METR doubling series [57]. Critiques from Epoch AI and others focus on: compute-scaling limits, the gap between benchmark tasks and real research, and the absence of a mechanism by which cognitive speedup translates into physical-world speedup. **ANALYSIS**

---

## What people are underestimating *(labeled analysis — my read, not established fact)*

**1. Verification, not generation, is the whole game — and it's why math is the outlier.** Every domain where AI-for-science has produced hard, durable results has a cheap automated verifier: Lean for proofs, a compiler and a stopwatch for kernels, a plasma that either stays confined or doesn't. Every domain where claims deflate — materials, biology, "discoveries" from literature agents — has an expensive, slow, physical verifier. The 3/50 on FrontierMath Open Problems versus ~88% on solved-but-hard problems is the same phenomenon in miniature: solved problems come with an answer key. Expect the next two years of genuine progress to concentrate wherever someone succeeds in building a cheap verifier for a previously unverifiable domain. **SPECULATION**

**2. The "AI accelerating AI" loop is real but is currently a *throughput* effect, not an *insight* effect.** OpenAI's 3.1 agent-workdays-per-human-workday is a parallelism number. It says researchers can run more experiments, not that the experiments are better chosen. The AI 2027 model assumes these convert into each other; nothing in the 2026 public record demonstrates that conversion. The strongest counter-evidence to fast takeoff is not that agents are weak — it's that OpenAI's own definition of its September 2026 milestone required the words "supervised" and "well-defined." **ANALYSIS**

**3. Benchmark error rates are an under-priced systemic risk.** Epoch corrected errors in **42%** of FrontierMath problems in one release. If the field's most carefully constructed math benchmark had that error rate, the informal benchmarks driving lab roadmaps and investor decisions are worse. Much of what reads as capability progress in 2024–2026 may partly be benchmark-quality progress running in the opposite direction. **ANALYSIS**

**4. The Erdős episode will repeat, in biology, at higher stakes.** The failure mode was specific and reproducible: a model retrieved a known result, a database said "open," and a credible person amplified it. Substitute "this compound is a novel candidate for X" for "this problem is open" and you have the shape of the next embarrassment. Biology has no Lean. **SPECULATION**

**5. Timeline slippage is domain-structural, not managerial.** Isomorphic slipping two years is not a story about Isomorphic. Design was never the rate-limiting step in drug development; the trial is. AI compresses the 10% of the pipeline it touches and leaves the other 90% untouched, which produces a characteristic pattern: dramatic capability demonstrations, followed by unchanged end-to-end timelines, followed by disillusionment that is itself mispriced. **ANALYSIS**

**6. The most consequential 2026 result may be the most boring one.** Not IMO gold; the ω < 2.371177 paper, where two human record-holders co-authored with an AI system that served as a refinement step in a human-designed pipeline. That is what "AI does science" actually looks like in the near term — not an autonomous scientist, but a superhumanly patient search subroutine embedded in human research programs. The org chart changes before the science does. **SPECULATION**

**7. Peer review is about to be the bottleneck, and no one is funding it.** Automated paper generation went from one Sakana system to a crowded arXiv subfield in eighteen months. Review capacity is fixed and volunteer-supplied. Tao's disclosure-and-can-you-give-the-talk norm is the only serious proposal on the table, and it is enforced socially, by individuals, with no infrastructure behind it. **SPECULATION**

**8. Self-driving labs are underrated relative to agents.** Periodic Labs at a reported $7B valuation with no published discovery is a bet that the physical loop is the moat — and that bet is probably right. The lab that can run 10,000 syntheses a week generates the training data that no amount of literature-reading produces. Materials MLIPs are the leading indicator: when a universal potential handles surfaces and defects reliably, the simulation-to-synthesis funnel narrows by an order of magnitude. **SPECULATION**

---

## Key numbers

| Metric | Value | Date | Label |
|---|---|---|---|
| IMO 2025 — DeepMind & OpenAI score | 35/42, 5/6 problems (gold) | Jul 2025 | CONFIRMED |
| Human gold medalists, IMO 2025 | 67 of 630 (~10%) | Jul 2025 | CONFIRMED |
| FrontierMath — all models at launch | <2% solved | Nov 2024 | CONFIRMED |
| FrontierMath — top score | ~88% | 2026 | CONFIRMED |
| FrontierMath v2 — problems with corrected errors | 42% (338 problems remain) | 2026-06-12 | CONFIRMED |
| FrontierMath Tier 4 — leading score | <40% | 2026 | CONFIRMED |
| FrontierMath Open Problems — solved by AI | 3 of 50 | since 2026-07-31 | CONFIRMED |
| First Proof batch 2 — publication-quality solutions | 7 of 10 problems | 2026-05-28 | REPORTED |
| First Proof — compute cost per problem | $10–$1,000 | 2026-05-28 | REPORTED |
| AlphaEvolve — 4×4 complex matrix multiply | 48 scalar multiplications (1st gain in 56 yrs) | 2025 | CONFIRMED |
| Matrix multiplication exponent ω | < 2.371177 (from 2.371339) | 2026-08-17 | CONFIRMED |
| AlphaEvolve — Google datacenter compute recovered | ~0.7% | 2025 | REPORTED |
| Erdős problems — solved by DeepMind Lean pipeline | 9 (one batch) | 2026-05-21 | REPORTED |
| GPT-5.4 Pro — Erdős conjecture solve time | ~80 min from one prompt | May 2026 | REPORTED |
| METR 50% time horizon — best model | ~16–20 hours | 2026 | REPORTED |
| METR 80% time horizon — best model | ~3–4 hours | 2026 | REPORTED |
| METR doubling time — from 2024 | 89 days (~3 months) | 2026-01-29 | CONFIRMED |
| METR doubling time — from 2023 (TH1.1) | 131 days | 2026-01-29 | CONFIRMED |
| OpenAI — agent-workdays per human workday | 3.1 | 2026-09-06 | REPORTED |
| OpenAI — "legitimate AI researcher" target | March 2028 | stated 2025-10 | CONFIRMED (target) |
| GNoME — stable materials identified | 381,000 (→520,000+ near-hull) | 2023–2024 | CONFIRMED |
| MatterGen — training structures / experimental validations | 600,000+ DFT / 1 material (TaCr₂O₆) | 2025 | CONFIRMED |
| Chai-3 — de novo antibody therapeutic-affinity rate | ~50% of designs (2× Chai-2) | 2026 | REPORTED |
| Robin — concept to Nature paper | 2.5 months | pub. 2026-05-19 | CONFIRMED |
| Kosmos — self-assessed finding accuracy | ~80% | 2026 | REPORTED |
| Co-Scientist — liver fibrosis candidate effect | blocked 91% of scarring-linked response | 2026 | REPORTED |
| Periodic Labs — seed round / reported valuation | $300M / $7B+ in talks | Sep 2025 / 2026 | CONFIRMED / REPORTED |
| AI-solo-authored papers in major journals | 0 | as of Apr 2026 | CONFIRMED |

---

## Sources

1. Google DeepMind — "Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the IMO" — https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/ (Jul 2025)
2. Gizmodo — "Google and OpenAI Chatbots Claim Gold at International Math Olympiad" — https://gizmodo.com/google-and-openai-chatbots-claim-gold-at-international-math-olympiad-2000632289 (Jul 2025)
3. TechCrunch — "OpenAI and Google outdo the mathletes, but not each other" — https://techcrunch.com/2025/07/21/openai-and-google-outdo-the-mathletes-but-not-each-other (2025-07-21)
4. Polymarket — "AI wins IMO gold medal in 2026?" — https://polymarket.com/event/ai-wins-imo-gold-medal-in-2026 (2026)
5. Terence Tao et al. — "AI contributions to Erdős problems" (community wiki) — https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems (ongoing, 2025–2026)
6. Delante — "GPT-5.2 Solves Erdős Problems" — https://delante.co/gpt-5-2-solves-erdos-problems/ (Jan 2026)
7. arXiv 2601.07421 — "Resolution of Erdős Problem #728: a writeup of Aristotle's Lean proof" — https://arxiv.org/pdf/2601.07421 (Jan 2026)
8. TechCrunch — "OpenAI claims it solved an 80-year-old math problem — for real this time" — https://techcrunch.com/2026/05/20/openai-claims-it-solved-an-80-year-old-math-problem-for-real-this-time/ (2026-05-20)
9. BuildFastWithAI — "GPT-5.4 Solved a 60-Year Math Problem: What Happened" — https://www.buildfastwithai.com/blogs/gpt-5-4-solved-a-60-year-math-problem-what-happened (2026)
10. Epoch AI — FrontierMath — https://epoch.ai/frontiermath (accessed 2026-09-07)
11. Epoch AI — "Less than 70% of FrontierMath is within reach for today's models" — https://epoch.ai/gradient-updates/less-than-70-percent-of-frontiermath-is-within-reach-for-todays-models (2026)
12. Terence Tao — "Mathematics in the age of AI" (ICM 2026), arXiv 2608.16753 — https://arxiv.org/abs/2608.16753 (Aug 2026)
13. Simons Foundation — "Fields Medalist Terence Tao on Artificial Intelligence and Why We Do Math" — https://www.simonsfoundation.org/2026/08/13/fields-medalist-terence-tao-on-artificial-intelligence-and-why-we-do-math/ (2026-08-13)
14. arXiv 2506.13131 — "AlphaEvolve: A coding agent for scientific and algorithmic discovery" — https://arxiv.org/abs/2506.13131 (Jun 2025)
15. arXiv 2508.03857 — "A 60-Addition, Rank-23 Scheme for Exact 3×3 Matrix Multiplication" — https://arxiv.org/pdf/2508.03857 (Aug 2025)
16. VentureBeat — "Meet AlphaEvolve, the Google AI that writes its own code—and just saved millions in computing costs" — https://venturebeat.com/ai/meet-alphaevolve-the-google-ai-that-writes-its-own-code-and-just-saved-millions-in-computing-costs (2025)
17. arXiv 2608.16884 — "Improving the matrix multiplication exponent with modern optimization and AlphaEvolve" — https://www.alphaxiv.org/abs/2608.16884 (2026-08-17)
18. arXiv 2603.12440 — "KernelFoundry: Hardware-aware evolutionary GPU kernel optimization" — https://arxiv.org/pdf/2603.12440 (Mar 2026); see also ParallelKernelBench, STARK (arXiv 2510.16996), Xe-Forge (arXiv 2605.26118), AscendCraft (arXiv 2601.22760)
19. IntuitionLabs — "Isomorphic Labs & AlphaFold: AI Drug Discovery in Trials" — https://intuitionlabs.ai/articles/isomorphic-labs-alphafold-ai-drug-discovery-trials (2026)
20. Reuters via Investing.com — "Google-backed Isomorphic Labs delays clinical trial timeline" — https://www.investing.com/news/stock-market-news/googlebacked-ai-drug-discovery-startup-isomorphic-labs-delays-clinical-trial-timeline-4456134 (Jan 2026)
21. Clinical Trials Arena — "Isomorphic Labs prepares to launch trials for AI-designed drugs" — https://www.clinicaltrialsarena.com/news/isomorphic-labs-prepares-trials-ai-designed-drugs/ (2026)
22. ChemDiv — "Isomorphic Labs Launches Human Trials for AI-Designed Cancer Drugs" — https://www.chemdiv.com/company/media/pharma-news/2026/isomorphic-labs-launches-human-trials-for-ai-designed-cancer-drugs/ (2026)
23. Businesswire — "Chai Discovery Unveils Chai-2 Breakthrough Achieving Fully De Novo Antibody Design With AI" — https://www.businesswire.com/news/home/20250630307418/en/Chai-Discovery-Unveils-Chai-2-Breakthrough-Achieving-Fully-De-Novo-Antibody-Design-With-AI (2025-06-30)
24. IntuitionLabs — "Generative Antibody Design: Chai-3 and Pharma AI Strategy" — https://intuitionlabs.ai/articles/generative-antibody-design-chai-3-pfizer (2026)
25. HIT Consultant — "Bristol Myers Squibb Partners with Chai Discovery for AI Antibody Design" — https://hitconsultant.net/2026/08/20/chai-discovery-collaborates-bristol-myers-squibb-ai-antibody-discovery/ (2026-08-20)
26. Ready Tensor — "Materials Discovery: GNoME" — https://app.readytensor.ai/publications/materials-discovery-gnome-vyH2wPwb1fum (2024–2026)
27. PMC — "Are diffusion models ready for materials discovery in unexplored chemical space?" — https://pmc.ncbi.nlm.nih.gov/articles/PMC13280719/ (2026)
28. arXiv 2503.09814 — "A practical guide to machine learning interatomic potentials — Status and future" — https://arxiv.org/pdf/2503.09814 (2025); see also arXiv 2504.06993 on defect screening
29. Implicator.ai — "Periodic Labs Raises $300M for AI-Driven Materials Science" — https://www.implicator.ai/periodic-labs-raises-300-million-to-automate-science/ (Sep 2025)
30. Contrary Research — "Periodic Labs Business Breakdown & Founding Story" — https://research.contrary.com/company/periodic-labs (2026)
31. CNBC — "Lila Sciences — 2026 Disruptor 50, No. 25" — https://www.cnbc.com/2026/05/19/lila-sciences-cnbc-disruptor-50-ranking.html (2026-05-19)
32. FutureHouse — "Demonstrating end-to-end scientific discovery with Robin: a multi-agent system" — https://www.futurehouse.org/research/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system (2025–2026)
33. C&EN — "AI companies introduce new agent-based tools for scientific discovery" — https://cen.acs.org/pharmaceuticals/drug-discovery/ai-companies-introduce-agent-based-research-tools/104/web/2026/05 (May 2026)
34. Edison Scientific — "Kosmos: An AI Scientist for Autonomous Discovery" — https://edisonscientific.com/news/announcing-kosmos (2025–2026)
35. Google DeepMind — "Co-Scientist: A multi-agent AI partner to accelerate research" — https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/ (2026)
36. IEEE Spectrum — "Google's AI Co-Scientist Is Changing the Face of Scientific Research" — https://spectrum.ieee.org/ai-co-scientist (2025–2026)
37. TechTimes — "Google Co-Scientist Reaches Nature: Hypothesis Agents Validated in Lab, Not Yet in Clinic" — https://www.techtimes.com/articles/317408/20260530/google-co-scientist-reaches-nature-hypothesis-agents-validated-lab-not-yet-clinic.htm (2026-05-30)
38. Nature — "How to build an AI scientist: first peer-reviewed paper spills the secrets" — https://www.nature.com/articles/d41586-026-00899-w (2026)
39. Sakana AI — "The AI Scientist: Towards Fully Automated AI Research, Now Published in Nature" — https://sakana.ai/ai-scientist-nature/ (2026-03-25)
40. Phys.org — "AI writes a research paper that passes peer review" — https://phys.org/news/2026-03-ai-paper-peer.html (Mar 2026)
41. Pebblous — "When AI Writes Science: JAIGP and Sakana AI Scientist Analysis" — https://blog.pebblous.ai/report/ai-science-new-era/en/ (2026)
42. arXiv 2502.14297 — "Evaluating Sakana's AI Scientist: Bold Claims, Mixed Results, and a Promising Future?" — https://arxiv.org/pdf/2502.14297 (Feb 2025)
43. Nature — "Magnetic control of tokamak plasmas through deep reinforcement learning" — https://www.nature.com/articles/s41586-021-04301-9 (2022)
44. Google DeepMind — "Bringing AI to the next generation of fusion energy" — https://deepmind.google/blog/bringing-ai-to-the-next-generation-of-fusion-energy/ (Oct 2025)
45. Commonwealth Fusion Systems — "With AI alliance, Google DeepMind and CFS take fusion to the next level" — https://blog.cfs.energy/with-ai-alliance-google-deepmind-and-cfs-take-fusion-to-the-next-level/ (Oct 2025)
46. SiliconANGLE — "Google's DeepMind and CFS are building an AI plasma control system for nuclear fusion" — https://siliconangle.com/2025/10/16/googles-deepmind-cfs-building-ai-plasma-control-system-nuclear-fusion/ (2025-10-16)
47. US DOE — "AI Tackles Disruptive Tearing Instability in Fusion Plasma" — https://www.energy.gov/science/fes/articles/ai-tackles-disruptive-tearing-instability-fusion-plasma (2024)
48. arXiv 2606.07550 — "Offline Reinforcement Learning for Plasma Control in Nuclear Fusion: Codebase and Benchmark" — https://arxiv.org/pdf/2606.07550 (Jun 2026)
49. METR — "Time Horizon 1.1" — https://metr.org/blog/2026-1-29-time-horizon-1-1/ (2026-01-29)
50. METR — "Task-Completion Time Horizons of Frontier AI Models" — https://metr.org/time-horizons/ (2025–2026)
51. METR — "Clarifying limitations of time horizon" — https://metr.org/notes/2026-01-22-time-horizon-limitations/ (2026-01-22)
52. Archyde — "OpenAI Hits 'Automated Research Intern' Milestone, Targets AI Researcher by 2028" — https://www.archyde.com/openai-hits-automated-research-intern-milestone-targets-ai-researcher-by-2028/ (2026-09)
53. DataStudios — "OpenAI Says It Has Reached an Automated Research Intern" — https://www.datastudios.org/post/openai-automated-research-intern-coding-agents-research-acceleration-ai-researcher (2026-09)
54. Engadget — "OpenAI says it reached its goal of creating an automated research intern" — https://www.engadget.com/2251859/openai-says-it-reached-its-goal-of-creating-an-automated-research-intern/ (2026-09)
55. Help Net Security — "OpenAI just hit a milestone on the road to self-improving AI" — https://www.helpnetsecurity.com/2026/09/07/openai-research-automation-intern/ (2026-09-07)
56. ChatGPT AI Hub — "OpenAI Reaches the Automated Research Intern Milestone: What 3.1 Agent Workdays per Human Workday Mean" — https://chatgptaihub.com/openai-automated-research-intern-codex-agent-workdays-human-intervention (2026-09)
57. AI 2027 Tracker — "METR time horizon doubles every 4 months" — https://ai2027-tracker.com/predictions/metr-doubling/ (2026)
