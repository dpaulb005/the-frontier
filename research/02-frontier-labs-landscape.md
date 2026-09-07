# The Frontier AI Landscape Beyond OpenAI — State of Play, September 2026

*Research memo, dated 2026-09-07. Claims are tagged **CONFIRMED** (primary source or multiple credible outlets), **REPORTED** (single credible outlet or company-friendly secondary coverage), or **RUMOR** (leaks, prediction markets, unsourced blogs). Inline [n] citations map to the Sources list.*

---

## TL;DR

- **Anthropic has taken the capability and revenue lead.** Claude Fable 5.1 (Sept 1) tops the Artificial Analysis Intelligence Index v4.2 (57) and the LMArena text board; Anthropic's run-rate revenue went $9B → $14B → $30B → $47B → $65B between Dec 2025 and end-July 2026, with investors expecting $100–120B by year-end and an IPO "as soon as this fall" [2][4][5][6][12]. **CONFIRMED** for revenue path; **REPORTED** for IPO timing.
- **The Mythos/Fable split is the new release pattern.** Anthropic now ships a restricted twin (Mythos 5.1, for ~200 vetted Glasswing orgs) alongside a safeguarded public twin (Fable 5.1). Terminal-Bench 4.0: Mythos 5.1 60.9% vs Fable 5.1 55.8% — the gap is the safeguard cost [1][2][10].
- **Google's Pro line has stalled; its Flash line has not.** Gemini 3.5 Pro was promised at I/O (May 19) and is still unreleased; Google has pivoted to pretraining Gemini 4 while shipping 3.6/3.7/3.8 Flash in six weeks. Google ranks 7th among labs on AA v4.2 as a result [12][14][16]. Deep Think and Ironwood TPUs remain genuine strengths [17][9].
- **Open weights sit ~4 months / ~8 ECI points behind closed** (Epoch, May 2026) — and the gap is not closing; it tracks the widening compute-investment gap [48]. But Chinese open models keep producing "firsts": Kimi K3 (2.8T, MXFP4) took #1 on LMArena's Frontend Code Arena, the first open model to top any board outright [29][30][52].
- **xAI became SpaceXAI.** SpaceX absorbed xAI (Feb 2026, ~$1.25T combined) and has IPO'd; Grok 4.5/4.6 shipped at $2/$6 pricing and Grok 4.6 ties GPT-5.6 Sol for #3 on AA. Grok 5 (6T params, RUMOR-grade specs) has missed Q1 and Q2 2026 targets [21][22][24].
- **Meta went closed, then half-way back.** Muse Spark (April, closed-weight) reached the AA top five; Muse Glimmer (Aug 10, 30B, Apache 2.0) reopened the door; Behemoth is shelved; 2026 capex guidance is $135–145B [25][26][28].
- **Agentic time horizons are doubling every ~3–4 months** (METR TH1.1), versus ~7 months historically; frontier models are now near saturation on METR's suite, which is itself the headline risk to the metric [46][47].
- **Neolabs have ~$50B+ of paper commitments and one shipped model.** Thinking Machines' Inkling (975B, Apache 2.0) ranks 41st on AA; SSI ($8B raised, $5B from Nvidia) and Reflection ($25B valuation, $6.3B SpaceX compute contract) have shipped nothing [41][43][44][45].

---

## 1. Anthropic

**Latest models (CONFIRMED).** The 2026 sequence: Mythos Preview announced April 7 (restricted, Project Glasswing) [1][11]; Claude Mythos 5 + Claude Fable 5 released June 9 [1]; Claude Opus 5 released July 24, positioned as "close to Fable on many tasks at half the price" ($5/$25 per M tokens) [3][2]; Claude Fable 5.1 + Mythos 5.1 on September 1, with Sonnet 5 ($2/$10) as the cheaper tier and Haiku 4.5 still the small model [2]. Fable 5.1 keeps $10/$50 pricing but cuts cache reads 75% to $0.25/M, which Anthropic says is ~25% cheaper for typical and ~45% cheaper for heavily agentic workloads [2]. Thinking is now on by default with a five-level effort parameter (low → max) [2]. A 1M-token context and 128K output are listed by third-party trackers (REPORTED).

**Benchmark standing (CONFIRMED).** AA Intelligence Index v4.2 (Sept 4): Fable 5.1 max = 57, ahead of GPT-6 Astra max (55, released Sept 3) and Opus 5 max (54) [12][13]. Anthropic-published numbers for Fable 5.1: Terminal-Bench 4.0 55.8% (Fable 5: 42.0%, Opus 5: 52.3%; Mythos 5.1: 60.9%); Terminal-Bench-Science 52.6% (Fable 5: 24.7%); SWE-bench Verified 95.0%; GDPval-AA v2 1,853; AutomationBench 31.4%; Browserbase "hardest" 82% [2]. On LMArena (Aug 3 snapshot) Fable 5 is #1 at ~1525 with Opus 4.8 and GPT-5.5 Pro ~15 points behind — the top five are within noise of one another [52]. Note that even OpenAI's own GPT-6 Astra launch table shows Fable 5.1 ahead on HLE-with-tools and on the AA index [53].

**Mythos and Glasswing (CONFIRMED with caveats).** Mythos was withheld because of offensive-cyber capability; Glasswing gave ~45 partners access with $100M in credits, expanded on June 2 to ~200 organizations in 15+ countries (reportedly adding Samsung and NATO) [10][11]. Mozilla reported 271 Firefox vulnerabilities found with Mythos; UK AISI ranked it highest on cyber evals; independent researchers noted some findings were also reachable with cheaper open models [1]. Commerce imposed export restrictions on non-U.S. access June 12 and lifted them June 30 [1]. Parameter counts (~8T Mythos, ~5T Fable) are **RUMOR**. A Fable 5-assisted counterexample to the 3D Jacobian conjecture (July 19) is REPORTED via Wikipedia's sourcing [1].

**Revenue and Claude Code (CONFIRMED).** Run-rate: $9B (Dec 31, 2025) → $14B (Feb 12) → $19B (March) → $30B (Apr 6) → $47B (May 29) → $65B (end July) [4][5][6]. Claude Code passed $1B ARR within six months of its mid-2025 launch and >$2.5B by February 2026; 1,000+ customers spend >$1M/yr; Dario Amodei said the company planned for 10x growth and "saw 80x" [6]. Series H raised $65B (May); Bloomberg puts the valuation at $965B and an IPO target of $2T+ [4][5] (**REPORTED**). SaaStr's framing: by year-end Anthropic will out-earn every public software company except Microsoft.

**Compute (CONFIRMED unless noted).** Amazon (Apr 20): up to 5 GW of new capacity, >1M Trainium2 chips in use today, ~1 GW of Trainium2/3 online by end-2026, $5B immediate Amazon investment plus up to $20B more on top of the prior $8B, and >$100B committed by Anthropic to AWS over a decade [7]. Google (Oct 2025): up to 1M TPUs and "well over" 1 GW online in 2026, "tens of billions" of dollars [8]; SemiAnalysis pegs the backlog at ~$49B, split ~400k purchased / ~600k rented, and estimates ~52% lower TCO per effective PFLOP vs GB300 NVL72 [9]. A further 3.5–5 GW Google/Broadcom tranche for 2027 is **REPORTED** [6][20]. Most surprising: VentureBeat's May summary lists 220k+ GPUs (300+ MW) at SpaceX's Colossus 1 among Anthropic's compute commitments — i.e., Anthropic renting from a competitor (**REPORTED**, single source) [6].

**Distinctive bets.** (1) Safeguards as a product tier (Mythos vs Fable; "Enterprise Frontier Safeguards" run monitoring inside customer infrastructure) [2]; (2) coding-agent distribution via Claude Code as the revenue engine; (3) a three-silicon strategy (Trainium, TPU, Nvidia) that trades ecosystem lock-in for price and supply resilience [7][9].

---

## 2. Google DeepMind

**Latest models (CONFIRMED).** Gemini 3 Pro + 3 Deep Think (Nov 2025); Gemini 3.1 Pro preview (Feb 19, 2026) at $2/$12 — ARC-AGI-2 77.1% (vs 31.1% for 3 Pro), GPQA Diamond 94.3%, LiveCodeBench Pro Elo 2887, SciCode 59.0%, MCP Atlas 69.2% [15]. Gemini 3.5 Flash (May); 3.6 Flash + 3.5 Flash-Lite + 3.5 Flash Cyber (July 21) [14]; 3.7 Flash (August, DeepSWE 49.0 → 65.3% at half the cost); 3.8 Flash + 3.8 Flash Cyber (Sept 2) at $0.75/$3.75, ties Opus 5 on HLE-Verified (54.9 vs 54.4) but uses ~70% more output tokens and has 13.3s TTFT; Google's own card says 3.8 is a tuned 3.7 and prices double Jan 1, 2027 [16].

**The Pro-line problem (CONFIRMED via Bloomberg/TechCrunch).** Pichai promised 3.5 Pro "within a month" at I/O on May 19; it missed. Bloomberg reported coding performance below internal targets and that a late-June data refresh made results worse; on July 21 Logan Kilpatrick said 3.5 Pro is "with partners" and that Google "has started its most ambitious pre-training run yet for Gemini 4" [14]. The flagship therefore hasn't moved since February. That is why AA v4.2 ranks Google 7th among labs (behind Meta, SpaceXAI, Moonshot and Z.ai) — its best listed model is 3.8 Flash at 47 [12][13]. On LMArena, 3.1 Pro Preview still sits ~1505, within 20 points of #1 [52].

**Deep Think and science (CONFIRMED).** Gemini Deep Think hit IMO gold (35/42) in July 2025 [18]. The Feb 11, 2026 DeepMind post reports the Jan-2026 Deep Think scoring up to 90% on IMO-ProofBench Advanced as inference compute scales; an agent called Aletheia autonomously solved four Erdős-database problems, disproved a decade-old online-submodular-optimization conjecture, and produced one ICLR '26 acceptance among 18 collaborative problems. DeepMind's framing: "the scaling law continues to hold... beyond Olympiad level into PhD-level exercises" [17]. Whether a Gemini system took IMO 2026 gold in July is **unverified** in this memo.

**World models (CONFIRMED).** Genie 3 (Aug 2025): 720p, 24 fps, ~1 minute of consistency. Project Genie shipped Jan 29, 2026 to AI Ultra subscribers, capped at 60-second sessions. Waymo built a "Waymo World Model" on Genie 3 that outputs lidar 4x faster and supported its expansion to 11 U.S. cities [19]. No Genie 4 found.

**Compute (CONFIRMED / REPORTED).** TPU v7 Ironwood: ~GB200-class peak FLOPs, 192 GB HBM3E, 9,216-chip pods on a 3D torus; SemiAnalysis lists Anthropic, Meta, xAI, OpenAI and SSI as merchant TPU customers [9]. Ironwood GA on April 22, 2026, "inference-first" positioning (**REPORTED**) [20]. Alphabet capex and Cloud numbers were not verified here. AlphaEvolve: no 2026 update surfaced; treat any "AlphaEvolve 2" claims as **RUMOR**.

**Distinctive bets.** Vertical integration (TPUs + DeepMind + distribution via Search/Android/Workspace, plus Apple-Siri integration), math/science discovery via test-time scaling, and world models for robotics/AV simulation. The risk is that the Pro-line slip lets Anthropic/OpenAI own the agentic-coding tier for a full product cycle.

---

## 3. xAI → SpaceXAI

**Corporate (CONFIRMED).** SpaceX acquired xAI in February 2026 (combined ~$1.25T) and the unit now trades as SpaceXAI under the public SpaceX (SPCX) umbrella; it also acquired Cursor, and Grok models from 4.5 onward are "co-developed" with it [21][22][23].

**Models (CONFIRMED).** Grok 4.1 (Nov 2025), 4.20 (Feb 2026), 4.3 (April, new pretrain), Grok 4.5 (July 8; "1.5T-parameter V9 foundation," trained on tens of thousands of GB300s, $2/$6, Musk: "roughly comparable to Opus 4.7, but much faster") [21][23]; Grok 4.6 (Aug 12–19): AA index 61 on the v4.1 scale, matching GPT-5.6 Sol for #3 globally and passing Kimi K3; 500K context, $2/$6 under 200K tokens, $4/$12 above; ships in Grok Build and Cursor [22]. On the rebased v4.2 index Grok 4.6 scores 50–51 [13]. Grok 4.7 was promised "within weeks" [23] (**REPORTED**). Grok added to DoD's GenAI.mil at IL5 in August [23].

**Grok 5 (RUMOR-grade specs, REPORTED delays).** Musk's stated 6T-parameter MoE with 1.5M context and a "10% and rising" chance of AGI [24]; missed Q1 and Q2 targets; prediction markets gave 33% for a June 30 ship; still training as of August.

**Compute (REPORTED).** Colossus 1: ~230k GPUs including 32k GB200s. Colossus 2 (Memphis): target 550k GB200/GB300s, >1 GW in January 2026, 1.5 GW after an April upgrade, ~$18B [24]. Reflection AI's $150M/month contract for GB300 capacity at Colossus 2 [44] and Anthropic's reported use of Colossus 1 [6] suggest SpaceXAI is also monetizing the cluster as a neocloud.

**Distinctive bets.** Raw cluster scale, aggressive pricing/token efficiency, the Cursor data flywheel, and government/defense distribution.

---

## 4. Meta (Meta Superintelligence Labs)

**Organization (CONFIRMED).** MSL formed June 2025 after the $14.3B Scale AI deal; Alexandr Wang is Chief AI Officer, Nat Friedman runs product; four groups (TBD Lab, FAIR, Products & Applied Research, MSL Infra); ~600 cuts in Oct 2025; Yann LeCun left in Nov 2025 to found AMI Labs (~€500M at €3B) [25][51]. Attempted acquisitions of SSI, Thinking Machines and Perplexity failed [25].

**Models (CONFIRMED).** Muse Spark (April 8, 2026) — Meta's first closed-weight, API-only frontier model, shipped inside Meta AI/WhatsApp/Instagram and Ray-Ban glasses; ranked #4 on AA at launch (index 52), led HealthBench Hard (42.8 vs 20.6 for Gemini 3.1 Pro) [26]. Muse Spark 1.3 now scores 53 (max) on AA v4.2 at ~$0.96 per index run — the cheapest model in the top ten [13] — and Meta reported 75.4% on the 113-task agentic-coding eval OpenAI used for Astra (74.1%) [53]. Muse Glimmer (Aug 10): 30B dense, multimodal, Apache 2.0, 128K, runs at <20 GB in 4-bit; trails Qwen 3.6-27B generally but is tuned for tool calling; Meta also said it will open-source Muse Spark 1.2 weights [25][26] (**REPORTED**). Llama 4 Behemoth (~2T, 288B active) is shelved but never cancelled; reported root causes are MoE-routing and chunked-attention issues at 2T scale [26]. Llama 5 ("Avocado") is forecast for 2027 by sell-side; markets put 2026 odds under 20% [26] (**RUMOR**).

**Capex (CONFIRMED).** 2026 guidance raised twice to $135–145B; Q2 2026 revenue $60.8B, EPS $6.18 (miss), stock fell on shrinking free cash flow [27][28]. Hyperion (Louisiana) scaled to a 5 GW target and >$50B; Prometheus (1 GW) online in 2026; a $14B BlackRock JV in El Paso [28].

**Distinctive bets.** Talent-density plus the largest capex line of any lab; distribution through 3B+ users; a hedged open/closed posture (closed flagship, open small models). Meta is the third-ranked lab on AA v4.2 — a real recovery from the Llama 4 debacle [12].

---

## 5. Chinese labs

**DeepSeek (CONFIRMED / REPORTED).** V4-Pro (1.6T) and V4-Flash (284B) released April 24, 2026 under MIT (**REPORTED**, multiple secondary sources; the February "mid-Feb launch" reporting was wrong) [34][33]. Architecture notes from DeepSeek's own papers: Engram conditional memory (offloading a 100B-entry embedding table to host DRAM at <3% throughput penalty), sparse attention, 1M context [34]. AA v4.2 scores V4 Pro at 42; LMArena lists a V4.1 Pro (~1410) [13][52]. R2 remains unreleased; FT-sourced reports say a training run on Huawei Ascend 910C failed on distributed-training stability and DeepSeek fell back to Nvidia [33] (**REPORTED**). The DeepSeek story in 2026 is that the price/efficiency lead persists but the capability lead among Chinese labs passed to Moonshot and Alibaba.

**Alibaba Qwen (CONFIRMED).** Qwen3.5 (Feb 16–Mar 2): 397B-A17B flagship with gated-delta-network linear attention, Apache 2.0, sizes 0.8B–397B; beat GPT-5.2/Opus 4.5/Gemini 3 Pro on 28 of 44 vision benchmarks [36]. Qwen 3.6 (incl. a 35B-A3B coder) followed; Qwen 3.7 Max sits ~1488 on LMArena; a Qwen3.8-Max at 2.4T-A95B is reported as an open-weight release [37][52] (**REPORTED**). Alibaba is also the reported supplier of 20k H200s to Moonshot (denied by Alibaba) [29].

**Moonshot / Kimi (CONFIRMED).** K2.5 (Jan 27, 1.04T-A32B, MoonViT vision), K2.6 (April, ties GPT-5.5 on coding per secondary coverage), K2.7 (June 12), and Kimi K3 (API July 16, weights July 26–27): 2.8T total, 896 experts with 16 active (~50B-equivalent active), 1M context, native vision, MXFP4 quantization-aware training so the checkpoint is ~1.4 TB rather than ~5.6 TB; new "Kimi Delta Attention," attention residuals and a latent-MoE router; Agent Swarm up to 300 sub-agents [29][30]. Benchmarks: GPQA-Diamond 93.5, SWE Marathon 42.0, DeepSearchQA F1 95.0; #1 on LMArena Frontend Code Arena at 1,679 — the first open model to top a board — and ~1500 on text [30][31][52]. AA v4.2: 50 (max), i.e., level with Grok 4.6 and above GPT-5.6 Sol xhigh [13]. License is custom: revenue-share up to 30% for providers above $20M/yr [29]. Moonshot raised at a $35B valuation on July 30; ARR ~$200M in April [29].

**Zhipu / Z.ai (REPORTED).** GLM-5.2 (June 13): 744B-A40B, MIT, 1M context; GLM-5.3 scores 49 on AA v4.2, making Z.ai the #6 lab [13][38].

**MiniMax (REPORTED).** M3 (June 1): first open-weight model combining frontier coding, 1M context and native multimodality [38]. Xiaomi's MiMo V2.5 Pro (~1T) is also in the open pack [31].

**The pattern.** Open Chinese flagships are now 1.6T–2.8T MoEs trained with quantization-aware low precision, released under MIT/Apache or revenue-gated custom licenses, and priced near zero — but they trail the closed frontier by ~4 months and lean on Nvidia (H200/GB-class) for pretraining. The Huawei Ascend training failure is the clearest evidence that export controls still bite at the training stage, less so at inference [33].

---

## 6. Mistral

**Models (CONFIRMED).** Mistral Large 3 (Dec 2025, 675B-A41B MoE, Apache 2.0, 256K, $0.50/$1.50); Mistral Medium 3.5 (April 30, 2026): 128B dense "merged" model that retires Magistral (reasoning) and Devstral 2 (coding), modified-MIT license, 256K, per-request reasoning effort, SWE-bench Verified 77.6%, τ³-Telecom 91.4, $1.50/$7.50 [39]. Later 2026 releases are vertical: Leanstral 1.5 (Lean 4 proofs), OCR 4.1, Agentic Search.

**Funding/compute (CONFIRMED).** €1.7B Series C at €11.7B (Sept 2025, ASML €1.3B); $830M bank debt (Mar 30, 2026) to build a 13,800-GPU data center outside Paris — Medium 3.5 is the first flagship trained on it [39][40].

**Standing.** Not on the AA top-20; positioned as the EU sovereign, enterprise-deployable option between Sonnet and Opus class. Its distinctive bet is regulatory/sovereignty demand plus consolidation into fewer, denser models.

---

## 7. New entrants

**Thinking Machines Lab (CONFIRMED).** $2B at $12B (July 2025, a16z); Nvidia partnership with 1 GW of compute (March 2026); co-founders Zoph and Metz returned to OpenAI (Jan 2026); a $50B raise reportedly stalled [41][42]. Shipped: an "interaction model" preview (May 11) processing audio/video/text in 200 ms chunks; Inkling (July 15): 975B-A41B MoE, Apache 2.0, 45T training tokens across four modalities, plus Inkling Small (276B); the company itself says it is "not the strongest model available, open or closed" and it ranks ~41st on AA. Revenue model is Tinker fine-tuning and hosting [41][45].

**Safe Superintelligence (CONFIRMED).** $1B → $2B at $32B (Feb 2025) → $5B from Nvidia (July 27, 2026) on the Vera Rubin platform; Google Cloud is also a provider; ~50 employees, no product or paper [43]. A first release "this month" was floated by an investor on a podcast in August — **RUMOR** [45].

**Reflection AI (CONFIRMED).** $2B at $8B (Oct 2025, Nvidia $800M); ~$25B implied valuation in mid-2026 talks; compute: $6.3B SpaceX/Colossus 2 contract ($150M/month, July 2026–2029), $1B+ Nebius (GB300), a 250 MW Korean site. Product: Asimov code-comprehension agent. No open-weight flagship shipped as of this writing; investor materials point to Q3 2026 [44].

**Others (REPORTED).** AMI Labs (LeCun, JEPA world models); Ineffable Intelligence ($1.1B seed); Discovery Loop; Periodic Labs. FutureSearch's median forecasts put a genuinely frontier model from any neolab at 2029 or later and frames the category as "a bet against superintelligence" [45].

---

## 8. Cross-cutting trends

**Open vs closed.** Epoch (May 29): open-weight models lag closed SOTA by ~4 months and ~8 ECI points (GPT-5 → GPT-5.5 sized), slightly worse than the ~3-month lag measured through Oct 2025, and the true lag is longer because labs withhold their best models (Mythos, Deep Think) [48]. What changed in 2026 is the *composition* of the open frontier: Chinese MoEs at 1.6–2.8T plus U.S. neolab and Meta entrants — and the first open #1 on a public arena [52]. The counterweight is compute: closed labs are locking 5 GW-scale contracts, open labs are training on rented H200s.

**Price/performance.** Epoch's series measures 9x–900x/yr declines in price-at-fixed-capability depending on the threshold (~40x/yr for GPQA-Diamond level) [49]; GPT-4-class output fell from ~$20–30/M to ~$0.40–0.80/M by 2026. At the frontier the curve is more visible in cache economics and effort knobs than in list price: Fable 5.1 held $10/$50 but cut cache reads 75% [2]; Opus 5 delivers ~Fable performance at $5/$25 [3]; Grok 4.6 and Muse Spark 1.3 sit within 3–6 index points of the leader at one-third to one-sixth the index-run cost [13]. AA notes 40% of its index is now private held-out data to resist gaming [12].

**Reasoning / test-time compute.** Every frontier vendor now exposes an effort dial (Anthropic low→max, OpenAI medium→max, Grok reasoning modes, Mistral reasoning_effort). DeepMind's Deep Think results are the cleanest evidence that inference scaling keeps paying past Olympiad level [17]; Gemini 3.8 Flash is the cleanest evidence of the cost — 70% more tokens and 13 s to first token for a few points of quality [16]. Astra's headline scores (FrontierMath T4 97.6%, ARC-AGI-3 99.9%) mean the reasoning benchmarks of 2025 are effectively closed [53].

**Agentic long-horizon tasks.** METR TH1.1 (Jan 29): doubling time 89 days since 2024 (109 under TH1), ~131 days since 2023, ~196 days all-time; Opus 4.5 at 320 min (p50) / 729 min (p80) [46]. LessWrong's rollup calls it 10x/yr [47]. Caveat from METR itself: latest models approach saturation on the suite, only 5 of 31 long tasks have measured human baselines, and the suite is coding-heavy. Vendor evals now emphasize multi-hour agent runs (AutomationBench, Browserbase, DeepSWE, OSWorld — Astra cut average task time from ~75 to ~40 min) [2][53].

**World models.** Google (Genie 3/Project Genie, Waymo variant), World Labs (Marble, $95/mo tiers), Nvidia Cosmos (2M downloads), Runway Gen-4.5, OpenAI Sora 2, AMI Labs (JEPA) [19][51]. Still bottlenecked by inference cost (8–32 GPUs per session) and short memory (~60 s); the commercially proven use is simulation for AV/robotics, not consumer.

**Continual learning.** Unsolved in weights; shipped in context. Anthropic's Sholto Douglas predicted it would be "solved in a satisfying way" in 2026 and Amodei said it is "not as difficult as it seems"; Sutskever calls it a "huge huge problem"; Google's Titans/Nested Learning are the main published architectures [50]. In practice, 2026 agents implement continual learning as tool-managed memory over frozen weights. No frontier lab has shipped weight-level online learning (**CONFIRMED absence**).

---

## 9. What people are underestimating (analysis)

1. **Safeguard tax is now a measurable capability variable.** Mythos 5.1 vs Fable 5.1 on Terminal-Bench 4.0 is 60.9 vs 55.8 — five points, about one model generation. Whoever narrows that gap (better classifiers, enterprise-side monitoring) ships the effectively strongest public model without training a new one [2].
2. **Google's slip is a pretraining story, not a product story.** A failed data refresh and a restart on Gemini 4 imply 3.5 Pro was an incremental post-train on the 3-series base [14]. If Gemini 4 lands on Ironwood at scale in H1 2027, Google re-enters the top three abruptly; if not, the Flash line keeps Google as the price leader but not the capability leader.
3. **Compute rentals are blurring lab boundaries.** Anthropic on Colossus 1 and Reflection on Colossus 2, TML and SSI on Nvidia allocations, Anthropic on Google TPUs: capacity is fungible and being sold to rivals [6][9][44]. The moat is contracted gigawatts, not proprietary chips.
4. **Open-weight "firsts" are arena-shaped.** Kimi K3's Frontend Code #1 is real, but on AA's private-set-weighted index it sits at 50 vs 57 [13][52]. Human-preference boards flatter models tuned for output style; the open-closed gap on held-out agentic evals is wider than headlines suggest.
5. **The revenue curve is the strongest forward indicator of compute.** Anthropic at a $65B run-rate funds ~2 GW/yr of buildout from operations; a $100–120B exit rate supports the 5 GW Amazon and reported 3.5–5 GW Google tranches without further equity [4][6][7]. Investors are pricing the neolabs as if this curve bends; nothing in 2026 data suggests it has.
6. **Time-horizon saturation is the next measurement crisis.** METR says frontier models are near the ceiling of its suite [46]. When the metric breaks, the field loses its only cross-lab long-horizon yardstick, and vendor-published agent benchmarks (mostly private) fill the gap.
7. **China's constraint moved from chips-for-inference to chips-for-training.** DeepSeek's Ascend failure and Moonshot's reported H200 sourcing say the same thing: export controls delay Chinese *frontier* runs by roughly the Epoch lag, but do not stop open distribution [29][33][48].

---

## 10. Key numbers

| Item | Value | Status | Source |
|---|---|---|---|
| AA Intelligence Index v4.2 leader | Claude Fable 5.1 (max) = 57; GPT-6 Astra 55; Opus 5 54; Muse Spark 1.3 53; GPT-5.6 Sol 51; Grok 4.6 51; Kimi K3 50; GLM-5.3 49; Gemini 3.8 Flash 47; DeepSeek V4 Pro 42 | Confirmed | [12][13] |
| AA lab ranking | Anthropic, OpenAI, Meta, SpaceXAI, Moonshot, Z.ai, Google | Confirmed | [12] |
| LMArena text #1 (Aug 3) | Claude Fable 5 ~1525; top 5 within ~20 Elo | Confirmed | [52] |
| First open model #1 on an arena board | Kimi K3, Frontend Code, 1,679 | Confirmed | [52] |
| Fable 5.1 pricing | $10 / $0.25 cache / $50 per M; Opus 5 $5/$25; Sonnet 5 $2/$10 | Confirmed | [2] |
| Fable 5.1 vs Mythos 5.1, Terminal-Bench 4.0 | 55.8% vs 60.9% | Confirmed | [2] |
| Anthropic run-rate | $9B (12/25) → $30B (4/26) → $47B (5/26) → $65B (7/26); $100–120B exit expected | Confirmed / Reported | [4][5][6] |
| Anthropic valuation | $965B post-Series H ($65B raised); IPO target $2T+ | Reported | [4] |
| Anthropic compute | Amazon up to 5 GW, >1M Trainium2, ~1 GW T2/T3 by end-2026; Google up to 1M TPUs, >1 GW in 2026, ~$49B backlog | Confirmed / Reported | [7][8][9] |
| Gemini 3.1 Pro | ARC-AGI-2 77.1%, GPQA 94.3%, $2/$12 | Confirmed | [15] |
| Gemini 3.5 Pro | Unreleased as of Sept 7; Gemini 4 pretraining underway | Confirmed | [14][16] |
| Deep Think | IMO gold (2025); 90% IMO-ProofBench Advanced (Jan 2026) | Confirmed | [17][18] |
| Ironwood TPU | 9,216-chip pods, 192 GB HBM3E, ~GB200 FLOPs; ~52% lower TCO/PFLOP vs GB300 (SemiAnalysis) | Reported | [9] |
| Grok 4.5 / 4.6 | July 8 / Aug 12–19; $2/$6; 500K ctx; #3 on AA at launch | Confirmed | [21][22] |
| Grok 5 | 6T MoE (Musk), still training, missed Q1 & Q2 | Rumor / Reported | [24] |
| Colossus 2 | 550k GB200/GB300 target, 1.5 GW, ~$18B | Reported | [24] |
| Meta capex 2026 | $135–145B; Hyperion 5 GW, >$50B | Confirmed | [27][28] |
| Muse Spark | Apr 8, closed; AA #4 at launch; 1.3 = 53 | Confirmed | [13][26] |
| DeepSeek V4 | V4-Pro 1.6T, V4-Flash 284B, MIT, Apr 24; R2 unreleased | Reported | [33][34] |
| Kimi K3 | 2.8T, 896 experts/16 active, 1M ctx, MXFP4, weights July 26–27 | Confirmed | [29][30] |
| Moonshot valuation | $35B (July 30) | Confirmed | [29] |
| Qwen3.5 flagship | 397B-A17B, Apache 2.0, Feb 16 | Confirmed | [36] |
| Mistral Medium 3.5 | 128B dense, SWE-bench V 77.6%, $1.50/$7.50; $830M debt, 13,800 GPUs | Confirmed | [39] |
| Inkling (TML) | 975B-A41B, Apache 2.0, ~41st on AA | Confirmed | [41][45] |
| SSI | $8B raised incl. $5B Nvidia; no product | Confirmed | [43] |
| Reflection AI | ~$25B val; $6.3B Colossus 2 contract; no model yet | Confirmed | [44] |
| Epoch open-closed gap | ~4 months, ~8 ECI points (May 2026) | Confirmed | [48] |
| METR doubling time | 89 days since 2024 (TH1.1); Opus 4.5 p50 = 320 min | Confirmed | [46] |
| Epoch price decline | 9x–900x/yr by threshold; ~40x/yr at GPQA level | Confirmed | [49] |

---

## Sources

1. Wikipedia, "Claude Mythos" — https://en.wikipedia.org/wiki/Claude_Mythos (accessed 2026-09-07)
2. VentureBeat, "Anthropic's Claude Fable 5.1 and Mythos 5.1 arrive with a 75% cost reduction for Fable cache reads" — https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads (2026-09-01)
3. Axios, "Anthropic releases new model, Opus 5" — https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5 (2026-07-24)
4. TechCrunch, "Anthropic's annualized revenue surges to $65B" — https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/ (2026-08-17)
5. Simon Willison, "Anthropic's run-rate revenue hits $47 billion" — https://simonwillison.net/2026/May/29/anthropic/ (2026-05-29)
6. VentureBeat, "Anthropic says it hit a $30 billion revenue run rate after 'crazy' 80x growth" — https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth (2026-05-08)
7. Anthropic, "Anthropic and Amazon expand collaboration for up to 5 gigawatts of new compute" — https://www.anthropic.com/news/anthropic-amazon-compute (2026-04-20)
8. Maginative, "Anthropic Secures 1M Google TPUs While Keeping Amazon as Primary Training Partner" — https://www.maginative.com/article/anthropic-secures-1m-google-tpus-while-keeping-amazon-as-primary-training-partner/ (2025-10-23)
9. SemiAnalysis, "TPUv7: Google Takes a Swing at the King" — https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the (2025-11)
10. 9to5Mac, "Anthropic expands Glasswing as it promises public Claude Mythos-class model releases" — https://9to5mac.com/2026/06/02/anthropic-expands-glasswing-as-it-promises-public-claude-mythos-class-model-releases/ (2026-06-02)
11. Anthropic, "Project Glasswing" — https://www.anthropic.com/glasswing (2026-04)
12. Artificial Analysis, "Announcing Artificial Analysis Intelligence Index v4.2" — https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2 (2026-09-04)
13. Artificial Analysis, LLM Leaderboard — https://artificialanalysis.ai/leaderboards/models (accessed 2026-09-07)
14. TechCrunch, "Google releases three new Gemini models — but no 3.5 Pro" — https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/ (2026-07-21)
15. SmartScope, "Behind Gemini 3.1 Pro's '13 out of 16 Wins'" — https://smartscope.blog/en/generative-ai/google-gemini/gemini-3-1-pro-benchmark-analysis-2026/ (2026-02-20)
16. eesel AI, "Gemini 3.8 Flash review 2026" — https://www.eesel.ai/blog/gemini-3-8-flash (2026-09-02)
17. Google DeepMind, "Gemini Deep Think: Redefining the Future of Scientific Research" — https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think/ (2026-02-11)
18. Google DeepMind, "Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the IMO" — https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/ (2025-07-21)
19. Wikipedia, "Genie (world model)" — https://en.wikipedia.org/wiki/Genie_(world_model) (accessed 2026-09-07)
20. Doolpa, "Google Ironwood TPU general availability" — https://doolpa.com/news/google-ironwood-tpu-general-availability-tpu-8-split-cloud-next-april-2026 (2026-04)
21. TechCrunch, "SpaceXAI releases Grok 4.5, which Elon describes as an 'Opus-class model'" — https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/ (2026-07-08)
22. VentureBeat, "SpaceXAI debuts Grok 4.6, overtaking Kimi K3's performance and matching GPT-5.6 Sol" — https://venturebeat.com/technology/spacexai-debuts-grok-4-6-overtaking-kimi-k3s-performance-and-matching-gpt-5-6-sol-for-worlds-third-best-on-artificial-analysis (2026-08)
23. Wikipedia, "Grok (chatbot)" — https://en.wikipedia.org/wiki/Grok_(chatbot) (accessed 2026-09-07)
24. AdwaitX, "Grok 5 Is Still Being Trained on Colossus 2" — https://www.adwaitx.com/grok-5-release-date-colossus-2-training/ (2026-02-26)
25. Wikipedia, "Meta Superintelligence Labs" — https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs (accessed 2026-09-07)
26. Codersera, "Llama 4 Guide: Scout, Maverick, Behemoth Status & Muse Spark (2026)" — https://codersera.com/blog/llama-4-complete-guide-2026/ (2026-08)
27. CNBC, "Meta's stock drops on disappointing guidance, dwindling free cash flow" — https://www.cnbc.com/2026/07/29/meta-q2-earnings-report-2026.html (2026-07-29)
28. KuCoin News, "Meta Q2 2026 Earnings Miss Estimates, Capex Guidance Rises to $145 Billion" — https://www.kucoin.com/news/flash/meta-q2-2026-earnings-miss-estimates-capex-guidance-rises-to-145-billion (2026-07-29)
29. Wikipedia, "Moonshot AI" — https://en.wikipedia.org/wiki/Moonshot_AI (accessed 2026-09-07)
30. Hugging Face blog, "Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization" — https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei (2026-07)
31. Tom's Hardware, "China's 2.8-trillion-parameter Kimi K3 beats Claude Fable 5 in Frontend Code Arena" — https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3 (2026-07)
32. Layer3 Labs, "Best Chinese AI Models 2026" — https://www.layer3labs.io/comparisons/best-chinese-ai-models (2026-08-28)
33. Meta Intelligence, "DeepSeek V4 and R2 Deep Dive" — https://www.meta-intelligence.tech/en/insight-deepseek-v4-r2 (2026-02-05)
34. Introl, "DeepSeek V4 Targets Coding Dominance" — https://introl.com/blog/deepseek-v4-february-2026-coding-model-release (2026-02)
35. Manifold Markets, "R2 / V4-Thinking (DeepSeek) release date" — https://manifold.markets/Bayesian/when-will-deepseek-release-r2
36. DeepLearning.AI The Batch, "Alibaba's Latest Flagship Qwen3.5 Models Are Open-Weights MoE Performers" — https://www.deeplearning.ai/the-batch/alibabas-latest-flagship-models-are-open-weights-moe-performers-in-sizes-from-less-than-1b-parameters (2026-03)
37. DataNorth, "Qwen3.8-Max: Alibaba's 2.4T open-weight AI model" — https://datanorth.ai/news/alibaba-releases-qwen3-8-max (2026-08)
38. Bright Coding, "GLM 5.2 vs Kimi K2.7 vs MiniMax M3" — https://www.blog.brightcoding.dev/2026/07/06/glm-52-vs-kimi-k27-vs-minimax-m3-the-ultimate-open-weight-ai-showdown-of-2026 (2026-07-06)
39. Let's Data Science, "Mistral Medium 3.5: 128B Open-Weight Model Replaces Devstral 2 and Magistral" — https://letsdatascience.com/blog/mistral-medium-3-5-128b-open-weight-merged-model (2026-04-30)
40. Clay, "How Much Did Mistral AI Raise?" — https://www.clay.com/dossier/mistral-ai-funding (2026)
41. TechCrunch, "Thinking Machines amps up its bet against one-size-fits-all AI with its first open model, Inkling" — https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/ (2026-07-15)
42. Wikipedia, "Thinking Machines Lab" — https://en.wikipedia.org/wiki/Thinking_Machines_Lab (accessed 2026-09-07)
43. TechCrunch, "Ilya Sutskever's Safe Superintelligence partners with Nvidia to scale its AI research" — https://techcrunch.com/2026/07/27/ilya-sutskevers-safe-superintelligence-partners-with-nvidia-to-scale-its-ai-research/ (2026-07-27)
44. Wikipedia, "Reflection AI" — https://en.wikipedia.org/wiki/Reflection_AI (accessed 2026-09-07)
45. FutureSearch, "The Neolabs Are a Bet Against Superintelligence" — https://futuresearch.ai/neolab-challengers-forecast/ (2026-08-05, updated 2026-08-29)
46. METR, "Time Horizon 1.1" — https://metr.org/blog/2026-1-29-time-horizon-1-1/ (2026-01-29)
47. LessWrong, "METR Time Horizons: Now 10x/Year" — https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year (2026-02-13)
48. Epoch AI, "Open models lag state-of-the-art closed models by 4 months" — https://epoch.ai/data-insights/open-closed-eci-gap (2026-05-29)
49. Epoch AI, "LLM inference prices have fallen rapidly but unequally across tasks" — https://epoch.ai/data-insights/llm-inference-price-trends (2025-03-12)
50. Transformer, "Why is everyone talking about continual learning?" — https://www.transformernews.ai/p/teaching-ai-to-continual-learning (2026-01-22)
51. Introl, "World Models Race 2026" — https://introl.com/blog/world-models-race-agi-2026 (2026-01-03)
52. LocalAIMaster, "LMArena Leaderboard (Live)" — https://localaimaster.com/blog/lmarena-chatbot-arena-leaderboard (2026-08-03)
53. Vellum, "GPT-6 Astra Benchmarks Explained" — https://www.vellum.ai/blog/gpt-6-astra-benchmarks-explained (2026-09)
54. Medium (AI Engineering Simplified), "Gemini 3.5 Pro release date 2026: why Google delayed it 3 times" — https://medium.com/ai-engineering-simplified/gemini-3-5-pro-release-date-2026-why-google-delayed-it-3-times-and-started-training-gemini-4-427f55207e5b (2026-07)
