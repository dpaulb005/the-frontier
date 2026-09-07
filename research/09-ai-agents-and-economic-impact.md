# AI Agents, Software Automation, and Economic Impact — State of Play, September 2026

*Research report compiled 2026-09-07. Evidence labels: **[CONFIRMED]** = primary source (official filing, lab publication, statistical agency, published paper); **[REPORTED]** = credible secondary sourcing or journalism, not primary-verifiable here; **[SPECULATION]** = forecast, model output, or opinion.*

---

## TL;DR

1. **Coding agents moved from autocomplete to multi-hour autonomy.** METR's revised Time Horizon 1.1 suite (Jan 2026) puts Claude Opus 4.5 at a **320-minute** 50%-success time horizon, with a **post-2023 doubling time of ~131 days** and a post-2024 doubling of ~89 days — materially faster than the "7 months" figure that anchored 2025 discourse [1]. **[CONFIRMED]**
2. **SWE-bench Verified is saturating.** Frontier models cluster at **80-81%**, and attention has shifted to SWE-bench Pro, Terminal-Bench 2.0 (top score ~0.83) and OSWorld 2.0, where the best computer-use agent completes only **~31%** of long-horizon desktop tasks [2][3][4]. **[CONFIRMED/REPORTED]**
3. **The best causal evidence on developer productivity still does not show a speedup.** METR's 2025 RCT found experienced open-source developers were **19% slower** with AI. The 2026 follow-up was **abandoned as uninterpretable** — developers refused the no-AI control arm — with a returning-cohort point estimate of **-18% (95% CI -38% to +9%)** [5][6]. **[CONFIRMED]**
4. **AI now writes a large, contested share of code:** ~42% of committed code (Sonar survey), ~27% of production code (large empirical study), ~75% of new code at Google by its own account [7][8]. Definitions differ enough that these are not the same statistic. **[REPORTED]**
5. **Protocols consolidated fast.** MCP passed **~97M monthly SDK downloads** and moved to the Linux Foundation's Agentic AI Foundation; A2A reached **1.0** in April 2026; a five-layer agentic-commerce stack (AP2, UCP, ACP, Visa TAP, Web Bot Auth) formed above them [9][10]. **[REPORTED]**
6. **Revenue is real and enormous.** Nvidia's quarter ended July 2026: **$96.2B revenue, $89.0B data center, +106% YoY** [11]. Anthropic run rate **[REPORTED]** ~$65B; OpenAI ~$40B [12][13]. Cursor ~$4B ARR; Cognition/Devin ~$900M+ [14][15].
7. **AI capex is now a macro variable.** ~**$1T** global AI investment in 2026 (~1.8% of US GDP), and AI-related investment accounted for roughly **74% of Q1 2026 US GDP growth** [16][17][18]. **[REPORTED, from official BEA data]**
8. **The bubble debate produced an actual event:** a **June 2026 correction** erased ~$1.3T in semiconductor market value in a week, against Bain's **$800B-by-2030 revenue shortfall** framing and its 2026 finding that promised AI cost savings largely "didn't arrive" [19][20][21]. **[REPORTED]**
9. **Labor evidence sharpened rather than exploded.** Stanford's August 2026 Canaries update: **no economy-wide displacement**, but a **19% employment gap** for 22-25-year-olds in AI-exposed occupations (up from 15%), driven by reduced hiring rather than separations [22]. CS new-grad unemployment ~**6.1%** [23]. **[CONFIRMED/REPORTED]**
10. **Forecasts moved *later*, not earlier.** Kokotajlo's median slipped from 2028 to ~late 2029; other AI Futures forecasters to 2032 — even as the METR trend they rely on *accelerated* [24]. That divergence is the single most interesting fact in the forecasting literature this year. **[REPORTED]**

---

## 1. Coding agents: capability

### Benchmarks

**SWE-bench Verified.** Epoch AI's independently-run version of the benchmark shows frontier models between roughly 54% and 81%, with Claude Opus 4.5/4.6 and Gemini 3.1 Pro clustered at **~80.6-80.9%** as of spring 2026 [2]. Epoch upgraded scaffolding, environments and token limits to v2.0.0 in February 2026 and re-ran key models — a reminder that "SOTA on SWE-bench" is a harness result as much as a model result. **[CONFIRMED]**

The benchmark's remaining headroom is largely contaminated by test-quality issues. Work like UTBoost and 2026's SWE-ABS ("adversarial benchmark strengthening") shows measurable inflation in reported success rates from weak or gameable test suites [2]. Treat the last ~10 points of SWE-bench Verified as noise. **[CONFIRMED — published papers]**

**SWE-bench Pro** and long-horizon suites (RoadmapBench, agentic-SDLC benchmarks) are where the discriminating signal now lives; a 2026 position paper argued directly that "coding benchmarks are misaligned with agentic software engineering" [2]. **[CONFIRMED]**

**Terminal-Bench 2.0** — 89 tasks across 16 categories in isolated Docker containers — has GPT-5.5 leading at **0.827** across 51 evaluated models as of September 2026 [3]. **[REPORTED]**

**Computer-use is the laggard.** On **OSWorld 2.0** (108 long-horizon real desktop tasks, 500-step budget), the top system — Claude Opus 5 — completes **31.4%** end-to-end (68.3% partial credit), with GPT-5.6 close behind at 27.3% [4]. The gap between ~80% on repo-level code tasks and ~31% on GUI tasks is the clearest capability asymmetry in the field: agents are far better at text-and-tools than at pixels-and-menus. **[REPORTED]**

### METR time horizons — the number that matters

METR's Time Horizon 1.1 (29 Jan 2026) expanded the suite from 170 to 228 tasks (+34%) and more than doubled the 8-hour-plus tasks (14 → 31) [1]. Headline 50%-success horizons:

| Model | 50% time horizon | 95% CI |
|---|---|---|
| Claude Opus 4.5 | **320 min** | 170-729 min |
| GPT-5 | 214 min | 117-480 min |
| o3 | 121 min | 74-201 min |
| Claude Opus 4 | 101 min | 58-170 min |

Doubling times: **196.5 days all-time; 130.8 days since 2023; 88.6 days since 2024** — i.e. the trend has been *accelerating*, and TH1.1 estimates progress ~20% faster than TH1 did [1]. **[CONFIRMED]**

Two caveats METR states explicitly and that most secondary coverage drops: (a) the suite has "relatively few tasks that the latest generation of models cannot perform successfully" — **saturation is compressing the top of the scale**; (b) only 5 of the 31 long tasks have measured human baselines, the rest are estimates [1]. Secondary reporting of "16-20 hour horizons" for the newest unreleased-name models is **[REPORTED]** and, by METR's own caution, unreliable above ~16 hours.

### The productivity RCT that refused to flip

METR's July 2025 randomized trial remains the most-cited counterweight to capability optimism: 16 experienced open-source developers on their own repositories were **19% slower** with AI tools, while *self-reporting* a 20% speedup [5]. That perception-reality inversion is the finding, more than the point estimate.

The 2026 follow-up (24 Feb 2026) is more important than its coverage suggests [6]:

- Scaled to **57 developers, 143 repositories, 800+ tasks**.
- Returning developers (n=10): **-18% speedup, 95% CI -38% to +9%**.
- New developers (n=47): **-4%, 95% CI -15% to +9%**.
- METR **abandoned the original design**: many developers refused to participate at all because they would not work without AI even at $50/hour, and 30-50% of participants avoided submitting tasks they believed AI would accelerate.

METR's own read: they believe developers are probably *more* sped up in 2026 than 2025, but "our data is only very weak evidence for the size of this increase," and "the true speedup could be much higher among the developers and tasks which are selected out" [6]. **[CONFIRMED]**

**Analysis:** both camps misuse this study. Bears cite "-19%" as if it were a stable causal estimate of AI's effect in 2026; it is a 2025 estimate on a narrow, adversarially-selected population (expert maintainers, mature repos, high tacit context) that METR itself no longer stands behind as current. Bulls cite the selection problem as if it proved a large speedup; non-random attrition tells you the estimate is biased, not which way it would land at scale. The honest statement is that **as of September 2026 there is no credible RCT-grade estimate of AI's effect on professional developer throughput** — the control group has ceased to exist.

### Products and money

- **Cursor (Anysphere):** ~$4B ARR as of June 2026, from ~$100M in Jan 2025; acquired by SpaceX in an all-stock deal valued around **$60B**, closed 14 Aug 2026 [14]. **[REPORTED — the acquisition in particular should be treated as reported, not confirmed]**
- **Cognition (Devin/Windsurf):** ~**$900M+ ARR**, ~$47B valuation as of Sept 2026 [15]. **[REPORTED]**
- **GitHub Copilot:** ~**4.7M paid subscribers** (Jan 2026), ~$2B ARR class [14][15]. **[REPORTED]**
- **Claude Code** is credited with roughly parity with Cursor at ~18% of the paid AI-coding market [14]. **[REPORTED]**

The structural story is a **bifurcation**: an *assistance* tier (Copilot, Cursor, Claude Code) monetizing developer seats, and an *autonomy* tier (Devin) monetizing task completion. The second is smaller but growing faster and is the one whose unit economics actually test the "agents replace labor" thesis.

### Share of code written by AI

Estimates for 2026 **[REPORTED]**: ~42% of committed code (Sonar, Jan 2026); ~46% of code from active developers; ~26.9% of production code in a study spanning 4.2M developers; ~75% of *new* code at Google, AI-generated and human-approved (April 2026) [7][8]. These measure different things — suggestions accepted, lines attributable, code in an agent-authored commit — and none of them measure *value*. The gap between "42% of code" and Bain's finding that savings did not arrive is the central puzzle of the year.

---

## 2. Computer-use agents and protocols

**Computer use** crossed into production in 2026: OpenAI folded Operator into ChatGPT Agent and extended it to Enterprise tiers; Anthropic shipped desktop-level control for Claude, available through AWS Bedrock, Vertex AI and Microsoft Foundry [25]. The dominant deployment pattern is a **risk-tiered approval gate** — read/scroll/screenshot run unattended, while delete/submit/purchase halt for a human [25]. That pattern exists precisely because OSWorld-class reliability (~31%) is not good enough to leave unsupervised. **[REPORTED]**

**Protocols.** The 2025 protocol war resolved into a layered stack rather than a winner:

- **MCP** (Anthropic, donated to the Linux Foundation's Agentic AI Foundation in Dec 2025): ~**97M monthly SDK downloads** by Feb 2026, adopted by Anthropic, OpenAI, Google, Microsoft and Amazon. Shopify ships MCP endpoints on every store by default at `/api/mcp` [9][10]. **[REPORTED]**
- **A2A** (Google → Linux Foundation): **v1.0 in April 2026**, with signed Agent Cards for verifiable agent identity [9]. **[REPORTED]**
- **Agentic commerce**: an eight-protocol, five-layer map — MCP, A2A, AP2, UCP, ACP, Visa TAP, Mastercard Verifiable Intent, Web Bot Auth — covering tools, agent-to-agent, payment intent, catalog/checkout and trust [10]. **[REPORTED]**

**Analysis:** the interesting move is that MCP and A2A both ended up under *neutral foundation governance* within roughly a year of launch. That is unusually fast standardization, and it is what makes 2026's "agent" market look more like early HTTP than like a proprietary platform war. The unsolved layer is **identity and liability** — Agent Cards and Web Bot Auth are the first serious attempts, and neither has been stress-tested by a large fraud event yet.

---

## 3. Enterprise adoption: the pilot-production gap

The single most consistent finding across sources is a wide gap between *use* and *scaled deployment* [26][27]:

- McKinsey: **88%** of organizations use AI in at least one function; only **23%** are scaling an agentic system.
- S&P Global / McKinsey: **31%** of enterprises have at least one AI agent in production — 47% in banking/insurance, 18% in healthcare/government.
- Gartner-class forecast: **40%** of enterprise applications will embed task-specific agents by end-2026, up from <5% in 2025. **[SPECULATION — vendor forecast]**
- US Census BTOS (May 2026): **37%** of firms with 250+ employees use AI in producing goods or services, versus under 20% of the smallest firms — up from ~9.7% economy-wide in Aug 2025 [26].

The **Anthropic Economic Index** provides the best inside-the-usage view [28]. Its 2026 reports show the *automation* share (directive use, minimal back-and-forth) rising from **27% in late 2024 to 39%**, crossing above augmentation for the first time; computer/mathematical tasks are ~35% of Claude.ai conversations and nearly half of API traffic; and 49% of jobs in the sample saw Claude used for at least a quarter of their tasks, up from 36% in Jan 2025. Higher-income countries skew toward augmentation; lower-income toward automation. **[CONFIRMED — Anthropic publication]**

---

## 4. The money

| Item | Figure | Label |
|---|---|---|
| Nvidia Q2 FY2027 (quarter ended 26 Jul 2026) revenue | **$96.2B**, +106% YoY | CONFIRMED [11] |
| — Data center segment | **$89.0B**, +117% YoY | CONFIRMED [11] |
| Nvidia FY2026 full year | $215.9B (+65%); data center $193.7B (+68%) | CONFIRMED [11] |
| Anthropic run rate (Jul 2026) | ~$65B (from ~$14B in Feb 2026) | REPORTED [12] |
| OpenAI run rate (Aug 2026) | ~$40B, ~$3.3B/month | REPORTED [13] |
| OpenAI vendor commitments 2025-2035 | ~$1.15T across seven vendors | REPORTED [29] |
| Global AI investment 2026 | ~$1T (~$600B US); ~1.8% of US GDP | REPORTED, Goldman [16] |
| AI-related investment share of Q1 2026 US GDP growth | **~74%** of 2.0-2.1% growth | REPORTED from BEA [17] |
| AI data center + hardware + networking capex | 1.4% of US GDP in Q1 2026, up from 0.7% | REPORTED, Fed/Epoch [18] |
| US labor productivity, Q1 2026 | +2.9% YoY; +2.4% annualized since 2024 | CONFIRMED, BLS [30] |

Caution on the lab run-rate figures: OpenAI and Anthropic **do not define run rate the same way**, and Bloomberg's own reporting flags this [12][13]. Treat cross-company comparisons as directional only. The reported ordering — Anthropic passing OpenAI during 2026 on enterprise/API strength while OpenAI leads on consumer — is plausible and widely reported but not independently auditable.

---

## 5. The bubble debate, argued both ways

### Bear case

1. **The revenue gap.** Bain: AI firms need ~$2T in annual revenue by 2030 to fund projected compute demand and will fall roughly **$800B short** [19]. **[REPORTED]**
2. **The savings didn't arrive.** Bain's 2026 survey found AI cost savings falling far short of projections, and — the sharpest detail — **44% of large companies are funding their next wave of AI spend on the basis of prior-round savings that have not materialized** [20]. **[REPORTED]**
3. **Circular financing.** Over **$800B** in arrangements where chipmakers and clouds invest in AI labs that immediately buy their products; OpenAI's ~$1.15T of commitments (Broadcom $350B, Oracle $300B, Microsoft $250B, Nvidia $100B, AMD $90B, AWS $38B, CoreWeave $22B) sit against ~$20B of revenue and an estimated **$14B loss in 2026** [29]. Oracle's stock fell ~30% in a quarter on delivery-and-counterparty risk. **[REPORTED]**
4. **Concentration.** By mid-2026 AI-related firms accounted for roughly 80% of US market gains; the top five tech companies were ~30% of S&P 500 value — the highest in half a century; Shiller P/E above 40 [21]. **[REPORTED]**
5. **A correction already happened.** June 2026: Nasdaq -2.2% in a day, **~$1.3T of semiconductor market value erased in a week** on profitability concerns [21]. **[REPORTED]**
6. **MIT's 95%.** The widely-cited finding that ~95% of enterprise GenAI pilots produce no measurable P&L effect, attributed to a "learning gap" — tools that don't learn, integrate poorly, or don't match workflows [20]. **[REPORTED]**
7. **The RCT.** No credible measurement showing professional developers are faster (§1). **[CONFIRMED]**

### Bull case

1. **The revenue is not hypothetical.** Nvidia at $96.2B/quarter and +106% YoY is a shipped-product number in an audited filing, not a projection [11]. Lab run rates roughly **quadrupled** in twelve months [12][13].
2. **Productivity is showing up where it should.** US labor productivity is running **+2.4% annualized since 2024**; information, finance/insurance and professional/technical services — the three most AI-exposed sectors, just **16% of hours worked** — account for **40% of total US productivity gains since 2024** [30][31]. That is the exact signature you would expect from a real, sector-concentrated GPT effect. **[CONFIRMED — Dallas Fed / KC Fed / BLS]**
3. **Capability is compounding, not plateauing.** METR's doubling time *shortened* under a harder, larger task suite [1].
4. **Capex/GDP is not unprecedented.** Epoch puts AI-related capital formation at ~1.5% of GDP — comparable to, not wildly beyond, the late-1990s telecom peak [18]. Bubbles that build durable infrastructure leave the infrastructure behind.
5. **Standardization lowers integration cost.** MCP/A2A adoption addresses the exact failure mode MIT diagnosed — poor integration and workflow fit [9][10].
6. **Pilot failure is what early diffusion looks like.** The 95% number is a snapshot of organizational learning, not a ceiling; the same statistic would have described enterprise web projects in 1998.

### Where I come down **[SPECULATION]**

Both sides are describing the same fact from opposite ends: **capability is compounding faster than firms can reorganize to use it.** The capability curve (METR, benchmarks) is exponential-ish; the diffusion curve (org design, data access, liability, trust) is S-shaped and slow. That produces exactly the observed pattern — enormous vendor revenue, real sector-level productivity in three industries, near-zero measured savings in the median enterprise, and a violent valuation reset when the market briefly repriced the gap.

The June 2026 correction looks more like a **repricing inside an intact boom** than a burst — the earnings kept coming. But the circular-financing structure is a genuine fragility: it converts a demand slowdown into a *simultaneous* revenue shock across chips, cloud and labs, because the same dollar appears on several income statements.

---

## 6. Labor market

**Stanford Digital Economy Lab, "Canaries in the Coal Mine," August 2026 update** [22] — the most careful evidence available, using ADP payroll microdata:

- **No evidence of widespread, economy-wide displacement.**
- Employment of workers **aged 22-25 in AI-exposed occupations is 19% below** where it would be had it tracked less-exposed peers — **widened from 15%** a year earlier.
- **No comparable gap for experienced workers** in the same occupations.
- The mechanism is **reduced hiring, not increased separations**.
- Concentrated in roles relying on *codified* knowledge. **[CONFIRMED — published paper]**

The lab has also published follow-ups disentangling interest rates and timing from the AI signal — worth noting, because the single strongest bear-on-the-bear-case argument is that 2023-2026 entry-level weakness is a rate-cycle and post-ZIRP-layoff-overhang story with an AI label attached [22].

**Corroborating [REPORTED]:** CS new-grad unemployment ~**6.1%** vs ~4.8% for recent grads overall (computer engineering ~7.8%) — CS graduates are now *more* likely to be unemployed than communications or history graduates [23]. Big Tech new-grad hiring down ~50% from pre-pandemic; entry-level SWE roles down ~30% YoY on Handshake data; ~55,000 US layoffs in 2025 attributed to AI by Challenger [23][32].

**Amodei.** His 2025 warning — AI could eliminate up to half of entry-level white-collar jobs within five years, with unemployment spiking to 10-20% — remains the loudest single forecast [32]. **[SPECULATION]** Notably, by May 2026 he had **shifted framing** toward Jevons-paradox-style job transformation and multiplication rather than pure elimination [32]. Whether that is updating on evidence or managing a narrative is unresolvable from outside; either way, the strongest version of the elimination claim now has less institutional backing than it did a year ago.

---

## 7. Forecasts

- **AI 2027 / AI Futures Project.** Kokotajlo's median for the key milestone slipped from **2028 → ~late 2029**; Eli Lifland to **~early 2032**; Nikola Jurkovic to end-2029 [24]. In April 2026 they published an update noting METR horizons were doubling every ~4 months rather than their assumed 5.5 — i.e. **the trend they track accelerated while their timelines got longer**, because other model components (real-world reliability, R&D automation share) updated the other way [24]. FutureSearch estimates superhuman-coder arrival ~3x later than the AI Futures forecasters. **[REPORTED]**
- **METR's own timelines model** (Feb 2026) puts ~99% AI R&D automation around **2032** [33]. **[CONFIRMED — METR note]**
- **Epoch AI's GATE** is a compute-centric macro model of AI automation: investment drives AI software R&D, which drives automation, which drives further investment. It produces *less aggressive takeoff* than Davidson's predecessor model but *slightly faster timelines*, and illustrates scenarios where over a fifth of annual output is reinvested into AI [34]. **[CONFIRMED — Epoch publication]**, though the outputs themselves are **[SPECULATION]**.
- **Goldman Sachs**: ~$1T global AI investment in 2026, with explicit sensitivity analysis on the assumptions driving build-out scale [16].

---

## What people are underestimating **[analysis — SPECULATION unless noted]**

1. **The control group is gone, and that is a measurement crisis.** METR could not run a 2026 RCT because developers refuse to work without AI [6] **[CONFIRMED]**. This means the causal question "does AI make developers faster?" may be *permanently unanswerable* by randomization at the individual level. Everything from here is quasi-experimental. Most commentary has not absorbed that the evidentiary standard has irreversibly degraded — and both bulls and bears will exploit the vacuum.

2. **The 80% / 31% split is the real story, not the 80%.** Repo-level coding at ~80% versus desktop computer-use at ~31% [2][4] means automation will hit *text-and-API-shaped* work years before *GUI-and-institution-shaped* work. Software engineering is unusually exposed not because it's hard but because its entire work product is already machine-readable. Predictions that generalize from coding agents to "white-collar work" are extrapolating across the widest capability gap in the field.

3. **The productivity data is *already* consistent with the bull case, and almost nobody cites it.** Three sectors that are 16% of hours worked producing 40% of productivity gains since 2024 [31] is a striking, underdiscussed number. It is not proof of causation — but it is the shape the evidence would take if AI were working, and it sits oddly beside the "95% of pilots fail" framing that dominates coverage.

4. **Automation crossing above augmentation is a leading indicator.** Anthropic's index showing directive use rising 27% → 39% and passing collaborative use [28] **[CONFIRMED]** is a change in *how* people use these systems, which precedes changes in headcount by quarters. Watch this series more closely than any benchmark.

5. **Forecast timelines getting longer while the capability trend accelerates is the tell.** [24] The binding constraint in serious forecasters' models has migrated from *capability* to *reliability, integration and real-world R&D automation*. That is the same constraint the Bain and MIT enterprise findings identify from the business side. Two independent literatures converging on "the bottleneck is deployment, not intelligence" is the strongest signal of 2026.

6. **Circular financing is a correlation risk, not a fraud claim.** Most critiques frame it as accounting deception. The sharper worry is structural: it makes chips, cloud and labs into a **single correlated credit exposure** [29]. A demand disappointment doesn't hit one balance sheet, it hits all of them at once. That converts an ordinary cyclical slowdown into a systemic one.

7. **The entry-level effect is real but the mechanism is quiet.** Displacement via *not hiring* [22] produces no layoff announcements, no WARN notices and no news cycle. It is nearly invisible in real time and shows up only in cohort data years later — which means the political response will lag the phenomenon by an entire graduating generation.

8. **Benchmark saturation is hiding the frontier.** METR explicitly warns its suite has too few tasks the newest models fail [1] **[CONFIRMED]**. We may be entering a period where the frontier is genuinely unmeasured — not because progress stopped, but because the rulers ran out. Both "it's plateauing" and "it's exploding" claims about mid-2026 models rest on saturated instruments.

---

## Key numbers table

| Metric | Value | Date | Label | Src |
|---|---|---|---|---|
| METR 50% horizon, Claude Opus 4.5 | 320 min (CI 170-729) | Jan 2026 | CONFIRMED | [1] |
| METR doubling time, post-2023 | 130.8 days | Jan 2026 | CONFIRMED | [1] |
| METR doubling time, post-2024 | 88.6 days | Jan 2026 | CONFIRMED | [1] |
| SWE-bench Verified SOTA | ~80.6-80.9% | Apr 2026 | CONFIRMED | [2] |
| Terminal-Bench 2.0 top score | 0.827 (GPT-5.5) | Sep 2026 | REPORTED | [3] |
| OSWorld 2.0 top binary completion | 31.4% (Claude Opus 5) | 2026 | REPORTED | [4] |
| METR RCT, returning devs | -18% (CI -38% to +9%) | Feb 2026 | CONFIRMED | [6] |
| AI share of committed code (Sonar) | 42% | Jan 2026 | REPORTED | [7] |
| MCP monthly SDK downloads | ~97M | Feb 2026 | REPORTED | [9] |
| Enterprises with ≥1 agent in production | 31% | 2026 | REPORTED | [27] |
| Anthropic index: directive/automation share | 39% (from 27%) | 2026 | CONFIRMED | [28] |
| Nvidia quarterly revenue | $96.2B (+106% YoY) | Q ended Jul 2026 | CONFIRMED | [11] |
| Nvidia quarterly data center revenue | $89.0B (+117%) | Q ended Jul 2026 | CONFIRMED | [11] |
| Anthropic run rate | ~$65B | Jul 2026 | REPORTED | [12] |
| OpenAI run rate | ~$40B | Aug 2026 | REPORTED | [13] |
| Cursor ARR | ~$4B | Jun 2026 | REPORTED | [14] |
| Cognition/Devin ARR | ~$900M+ | Sep 2026 | REPORTED | [15] |
| Global AI investment | ~$1T (1.8% US GDP) | 2026 | REPORTED | [16] |
| AI share of US Q1 GDP growth | ~74% | Q1 2026 | REPORTED | [17] |
| Semiconductor value erased | ~$1.3T in one week | Jun 2026 | REPORTED | [21] |
| Bain AI revenue shortfall | $800B by 2030 | 2025-26 | REPORTED | [19] |
| Young-worker AI employment gap | 19% (from 15%) | Aug 2026 | CONFIRMED | [22] |
| CS new-grad unemployment | ~6.1% | 2026 | REPORTED | [23] |
| US labor productivity | +2.9% YoY | Q1 2026 | CONFIRMED | [30] |
| Kokotajlo median timeline | ~late 2029 (was 2028) | 2026 | REPORTED | [24] |

---

## Sources

1. METR, "Time Horizon 1.1," 29 Jan 2026 — https://metr.org/blog/2026-1-29-time-horizon-1-1/ (also https://metr.org/time-horizons/)
2. Epoch AI, "SWE-bench Verified" benchmark hub, updated 2026 — https://epoch.ai/benchmarks/swe-bench-verified
3. Terminal-Bench 2.0 Leaderboard, updated Sep 2026 — https://llm-stats.com/benchmarks/terminal-bench-2
4. "OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks," arXiv, Jun 2026 — https://arxiv.org/html/2606.29537v1 ; Snorkel leaderboard — https://snorkel.ai/leaderboard/os-world-2-0/
5. METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity," 10 Jul 2025 — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
6. METR, "We are Changing our Developer Productivity Experiment Design," 24 Feb 2026 — https://metr.org/blog/2026-02-24-uplift-update/
7. "How Much Software Is Written by AI in 2026" (aggregating Sonar Jan 2026 and others) — https://www.secondtalent.com/resources/how-much-software-written-by-ai/
8. "AI Code Generation Statistics 2026" — https://uvik.net/blog/ai-code-generation-statistics/
9. "The State of Agentic AI Standards in 2026: MCP, A2A, WebMCP, OSI," 2026 — https://datalakehousehub.com/blog/state-of-agentic-ai-standards-2026/
10. "MCP vs A2A vs AP2 vs UCP vs ACP: Agentic Commerce Protocols (2026)" — https://stellagent.ai/insights/mcp-vs-a2a-vs-ap2-protocol-comparison ; ecosystem map — https://www.digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026-mcp-a2a-acp-ucp
11. NVIDIA, "Financial Results for First Quarter Fiscal 2027" and Q2 FY2027 8-K (quarter ended 26 Jul 2026) — https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027 ; https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm ; FY2026 full year — https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
12. "Anthropic Revenue Run Rate Surpasses $65 Billion Ahead of IPO," Yahoo Finance/Bloomberg, Jul-Aug 2026 — https://finance.yahoo.com/technology/ai/articles/anthropic-revenue-run-rate-surpasses-193745178.html
13. "OpenAI Revenue 2026: $40B ARR as Anthropic Hits $65B," Aug 2026 — https://valueaddvc.com/blog/openai-revenue-2026-20b-arr-4b-month-path-to-profitability ; cross-check: Epoch AI revenue dataset — https://epoch.ai/data/ai_companies_revenue_reports.csv
14. "Cursor (Anysphere): Revenue, Funding & Valuation (2026)" — https://valueaddvc.com/company/cursor ; "Cursor AI Valuation Hits $60B," Aug 2026 — https://tech-insider.org/cursor-60-billion-valuation-anysphere-ai-coding-2026/
15. "$47B Valuation — How Cognition (Devin) Makes Money," Sep 2026 — https://valueaddvc.com/blog/how-does-cognition-make-money-devin-pricing-windsurf-enterprise-and-the-492m-arr-breakdown ; "Three Ways to $2 Billion," Apr 2026 — https://agentmarketcap.ai/blog/2026/04/24/github-copilot-2b-arr-150m-developers-three-agent-revenue-models
16. Goldman Sachs, "Global AI Investment Is Forecast to Exceed $1 Trillion in 2026" — https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026 ; "Tracking Trillions" — https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out
17. "AI Capex Drove 74% of U.S. GDP Growth in Q1 2026" (BEA third estimate) — https://www.tftc.io/ai-capex-gdp-growth-q1-2026-bea-third-estimate/ ; St. Louis Fed, "Tracking AI's Contribution to GDP Growth," Jan 2026 — https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth
18. Federal Reserve, "The AI Buildout and the Economy," FEDS Note, 17 Jul 2026 — https://www.federalreserve.gov/econres/notes/feds-notes/the-ai-buildout-and-the-economy-publicly-available-data-to-assess-ais-impact-20260717.html ; Epoch AI, "Data center buildout share of US GDP" — https://epoch.ai/data-insights/ai-datacenter-share-gdp
19. Bain & Company via Business Standard, "AI's $800 billion revenue shortfall threatens industry growth" — https://www.business-standard.com/technology/tech-news/ai-s-800-billion-revenue-shortfall-threatens-industry-growth-says-bain-125092300111_1.html
20. Bain & Company, "More companies missing revenue targets amid AI and geopolitical volatility," 2026 — https://www.bain.com/about/media-center/press-releases/2026/more-companies-missing-revenue-targets-amid-ai-and-geopolitical-volatility-bain--company-survey-finds/ ; "AI Savings Misses Should Be Making Executives Uncomfortable," Insurance Journal, 1 Jun 2026 — https://www.insurancejournal.com/news/national/2026/06/01/871951.htm
21. "AI Stock Sell-Off June 2026: Are We in a Bubble?" — https://www.claritx.ai/blog/ai-stock-sell-off-june-2026-bubble-analysis ; "AI Bubble or AI Boom? What the 2026 Tech Sell-Off Means" — https://www.onemint.in/articles/ai-bubble-or-ai-boom-2026-tech-selloff-investors
22. Stanford Digital Economy Lab, "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of AI" (August 2026 update) — https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf ; "No Widespread Displacement, but the AI Employment Gap for Young Workers Has Widened to 19%," Aug 2026 — https://digitaleconomy.stanford.edu/news/canariesaug26/ ; interest-rate follow-up — https://digitaleconomy.stanford.edu/news/canaries-interest-rates-and-timinga-more-on-recent-drivers-of-employment-changes-for-young-workers/
23. "Computer Science Unemployment Rate 2026" — https://www.articuler.ai/resources/learn/computer-science-unemployment-rate/ ; "CS New-Grad Unemployment Hit 6.1%" — https://interviewchamp.ai/learn/why-cs-new-grad-unemployment-hit-6-percent-2025
24. FutureSearch, "AI 2027 Update: A One Year Timeline Check," 2026 — https://futuresearch.ai/blog/ai-2027-one-year-later/ ; AI Futures Project, "Clarifying how our AI timelines forecasts have changed" — https://www.lesswrong.com/posts/qPco9BX5kmKCDzzW9/clarifying-how-our-ai-timelines-forecasts-have-changed-since ; https://ai-2027.com/research/timelines-forecast
25. "Computer Use Agents 2026: Claude vs OpenAI vs Gemini" — https://www.digitalapplied.com/blog/computer-use-agents-2026-claude-openai-gemini-matrix ; "Computer Use and GUI Agents in 2026: State of the Art," Zylos, 8 Feb 2026 — https://zylos.ai/research/2026-02-08-computer-use-gui-agents/
26. "AI Agent Adoption 2026: 120+ Enterprise Data Points" (incl. Census BTOS May 2026) — https://www.digitalapplied.com/blog/ai-agent-adoption-2026-enterprise-data-points
27. "Enterprise AI Agent Stats 2026: 80% Embed, 31% Deploy" (S&P Global / McKinsey) — https://paul-okhrem.com/enterprise-ai-agents-statistics-2026/
28. Anthropic, "Anthropic Economic Index report: Learning curves," Mar 2026 — https://www.anthropic.com/research/economic-index-march-2026-report ; "Cadences," Jun 2026 — https://www.anthropic.com/research/economic-index-june-2026-report ; index hub — https://www.anthropic.com/economic-index
29. Bloomberg, "AI Circular Deals: How Microsoft, OpenAI and Nvidia Keep Paying Each Other," 2026 — https://www.bloomberg.com/graphics/2026-ai-circular-deals/ ; "Inside AI's Circular Financing Web," Aug 2026 — https://www.curionic.net/2026/08/ai-circular-financing-nvidia-openai-oracle-coreweave-2026.html ; Noah Smith, "Should we worry about AI's circular deals?" — https://www.noahpinion.blog/p/should-we-worry-about-ais-circular
30. BLS, "Productivity and Costs, Second Quarter 2026" — https://www.bls.gov/news.release/pdf/prod2.pdf ; BLS "Productivity and Artificial Intelligence" — https://www.bls.gov/productivity/articles-and-research/ai-and-productivity/home.htm ; Indeed Hiring Lab Q1 2026 — https://www.hiringlab.org/2026/05/07/q1-2026-productivity-and-costs-release/
31. Dallas Fed, "International comparisons show AI effect on productivity," 7 Jul 2026 — https://www.dallasfed.org/research/economics/2026/0707 ; Kansas City Fed, "A New U.S. Productivity Chapter? What Industry Data Say About AI" — https://www.kansascityfed.org/research/economic-bulletin/a-new-us-productivity-chapter-what-industry-data-say-about-ai/ ; Atlanta Fed WP, Mar 2026 — https://www.atlantafed.org/-/media/Project/Atlanta/FRBA/Documents/research/publication/working-paper/2026/03/25/04-artificial-intelligence-productivity-and-the-workforce-evidence-from-corporate-executives.pdf
32. Fortune, "Dario Amodei spent last year warning of an AI white-collar bloodbath. Now he's changing the narrative," 5 May 2026 — https://fortune.com/2026/05/05/dario-amodei-jevons-paradox-will-ai-wipe-out-white-collar-jobs/ ; Axios original, 28 May 2025 — https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic
33. METR, "A simpler AI timelines model predicts 99% AI R&D automation in ~2032," 10 Feb 2026 — https://metr.org/notes/2026-02-10-simpler-ai-timelines-model/
34. Epoch AI, "GATE: Modeling the trajectory of AI and automation" — https://epoch.ai/blog/announcing-gate ; Epoch AI 2025 Impact Report, 16 Jan 2026 — https://epoch.ai/latest/epoch-impact-report-2025
35. International AI Safety Report 2026, arXiv Feb 2026 — https://arxiv.org/pdf/2602.21012
