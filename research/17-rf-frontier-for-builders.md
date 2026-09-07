# The Frontier of RF Engineering (September 2026): Is It Really Ripe for a Fast-Moving AI-Armed Builder?

*Thesis under test: "RF is a stale field with entrenched incumbents, slow tooling, and tribal knowledge, and is therefore ripe for a fast-moving builder armed with AI tools."*

*Research date: 2026-09-07. Evidence labels: **CONFIRMED** = primary source (paper, filing, vendor release, price list); **REPORTED** = single credible secondary source, vendor claim, or market-research estimate; **SPECULATION** = my analysis or extrapolation.*

*Companion brief: `/home/user/the-frontier/research/18-signal-processing-frontier.md` covers the adjacent DSP/foundation-model opportunity. Section 6 below maps the overlap rather than repeating it.*

---

## TL;DR

1. **The thesis is half right, and wrong in an expensive way.** RF is genuinely constrained by an aging, scarce workforce and expensive closed tooling — Keysight launched a 2026 product explicitly framed around "the semiconductor talent gap," citing McKinsey's projection of 88,000 additional semiconductor engineers needed by 2029 [16]. That is an incumbent conceding the premise. But the *physics layer* is in its most disruptive decade since RF went CMOS, and a builder who mistakes "slow tools" for "slow field" will build the wrong thing.
2. **AI-designed RF hardware has crossed from simulation into measured silicon.** Multiple 2026 papers report *fabricated and measured* GaN Doherty PAs whose output combiners were inverse-designed by CNNs plus genetic/pixelated search: >74% peak drain efficiency at 2.75 GHz with 52% retained at 9-dB back-off [44], and 71.2% peak with 64% at 6-dB back-off over 2.6-2.8 GHz [45]. This is the single strongest evidence that AI methods produce competitive RF hardware, not just plots.
3. **The EDA incumbents are handing you the API surface.** Keysight's 2026 "executable RF design whiteboard" captures the engineer's decision process and emits **editable Python at every step**, redeployable across ADS, Cadence Virtuoso and Synopsys Custom Compiler, with Ansys HFSS in the signoff path [16][17]. Keysight calls the structured data plus Python APIs "the first step toward fully automated, AI/ML-driven RF design" [16]. Flux shipped an **MCP server for external AI agents in August 2026** [52]. Agent-drivable RF EDA is now a shipped feature, not a thesis.
4. **The open EM-solver gap is the most exploitable technical hole in the field.** Meep and openEMS — the two workhorse free solvers — are *not GPU-capable* [30][31][32]. GPU + autodiff FDTD (FDTDX) reports ~10x over Meep and ~415x over Ceviche on a 288M-cell problem [32]. Photonics got this; microwave/antenna/PCB did not.
5. **RF foundation models are a land grab with no incumbent and, critically, no corpus.** Six-plus surveys and architectures appeared in Aug-Sep 2026 alone [41][42][43], and **none of the abstracts report open weights or open data** [42]. Meanwhile DeepSig's RadioML datasets — still the field's de facto benchmark — are 2016/2018 vintage, carry "several known errata," are CC BY-NC-SA, and DeepSig itself says they are "NOT currently used within DeepSig products" and recommends you collect your own over-the-air data [39]. The benchmark of record is a decade old and disowned by its author.
6. **Money is flowing, but the checks are small.** Quilter: $25M Series B (Index Ventures, Oct 2025), $40M total [5]. Flux: $37M (8VC, Feb 2026) [52]. DeepSig: ~$14-16.5M *total* across its life [38][64]. Compare to any AI-infra round. **SPECULATION:** RF-AI is under-capitalized relative to the size of the problem, which is good news for a small team and bad news for anyone needing a big Series A.
7. **Defense pays fastest and buys most specifically.** DARPA's DRBE built the largest real-time virtual RF test range and transitioned a system to a Navy lab in late 2025 [20][21]. AFRL's Kaiju cognitive-EW effort is reported at ~$150M [23]. And there are *named, open SBIR topics closing 23 Sep 2026* that a two-person company can bid: 12849 "Signal Classification and Anomaly Detection in Contested Spectral Environments," 12846 "Collaborative Distributed Swarm Radar," 12880 "High Temp Semiconductor Transistors for ... Electronic Warfare" [49].
8. **The Ukraine market is real, fast, and turning against pure-RF solutions.** Brave1/DOT-Chain delivered 181,000+ units with order values above $235M by Q2 2026, at ~10-day order-to-delivery [24][25]. But fiber-optic FPV drones are jam-immune, 35+ Ukrainian manufacturers now build them, and procurement is shifting "toward kinetic and laser solutions" in a tiered architecture [25]. A pure RF-defeat business is entering a shrinking share of a growing market.
9. **Reconfigurable intelligent surfaces are the field's clearest hype trap.** Ten consecutive most-recent arXiv RIS papers (Aug-Sep 2026) contain **zero hardware prototypes, deployment trials, or commercialization** [55]. Do not build here.
10. **Best builder posture (SPECULATION):** don't compete with HFSS's solver kernel and don't chase RIS. Sell the *loop around* the incumbent tools — data capture, automated test, differentiable surrogates, agentic sweeps — plus the one genuinely missing public good: **an open, over-the-air, permissively licensed RF corpus and the model trained on it.** The moat is workflow and data, not math.

---

## 1. State of the Field: Why RF Is Hard and Slow

### 1.1 The talent problem is structural, quantified, and admitted by incumbents

- **CONFIRMED:** RF engineers are unusually rare because RF is a specialized analog domain requiring its own tools and analysis methods; EE Times covered this directly as a talent gap in RF development [1].
- **CONFIRMED:** Roughly half of US engineers are 50+; ~20% of practicing engineers are within 10 years of retirement; more than 25% plan to retire within five years [2]. In broadcast alone, the US needs ~5,100 broadcast engineers over the next decade against 6,200 retirements [3].
- **CONFIRMED:** In Quilter's 2026 compilation of IEEE/BLS/Electronic Design data (reproduced in the companion brief), the hardest roles to fill are analog at 44%, embedded at 43%, and **RF at 33%**, with an average time-to-hire of 58-62 days; US EE enrollment is down ~90% relative to CS since the 1980s; there are roughly 3 retirees per 1-2 new grads [64].
- **CONFIRMED:** Keysight, launching its 2026 RF Circuit Simulation Professional feature, states that RF simulation methodologies span multiple physics domains and "can take years to master," and cites McKinsey's 88,000-engineer semiconductor gap by 2029 [16].
- **CONFIRMED:** By 2031, demand for engineering skills is expected to grow ~13% while about a third of new engineering roles go unfilled [4].

### 1.2 Tooling: expensive, closed — and, as of 2026, newly scriptable

Keysight ADS, Cadence AWR, Ansys HFSS and Dassault CST are the de facto stack. Seats are five figures annually; node-locked licensing and per-solver-core pricing make large parametric sweeps a *budget* decision rather than an engineering one. This is the ossification the thesis correctly identifies.

What changed in 2026:

- **CONFIRMED:** Keysight's "executable RF design whiteboard" captures simulations, optimizations, decision trees and design parameters, generating editable Python at each step, saveable, shareable and redeployable across ADS, Cadence Virtuoso and Synopsys Custom Compiler, with Ansys HFSS in the enterprise signoff path [16][17]. Design review and tapeout steps that previously required manual setup now run automatically [16].
- **CONFIRMED:** Keysight presented chiplets, RF and AI-driven design as its DAC 2026 story [19], and shipped ADS 2026 and RF Circuit Simulation Professional 2026 releases [18][17].
- **CONFIRMED:** Flux ships Copilot (component research, schematic generation), AI auto-layout, AI design review, prompt-to-simulation, and a Python code interpreter; in **August 2026 it shipped an MCP server so external AI agents can drive the tool**, plus chat mode and voice dictation [52].

**SPECULATION:** This is the most important structural change for a builder. Closed solvers with Python/MCP surfaces are *agent substrate*. The defensible layer moves up the stack — to orchestration, design-space memory, and the surrogate — and away from the solver kernel, which you were never going to beat anyway.

### 1.3 The physical-layer frontier is not stale

**Sub-THz and 6G.** Sub-THz (100-300 GHz) offers enormous bandwidth but demands new RF architectures: InP power amplifiers, dense arrays, sophisticated beamforming [29]. imec reports InP chiplet integration on a **300 mm RF silicon interposer with strong 140 GHz performance** [28] — heterogeneous integration is how sub-THz becomes manufacturable rather than a lab curiosity.

**Compound semiconductors.** RF GaN is projected at ~$2.01B (2025) → $2.41B (2026) → ~$5.90B (2031), ~19.6% CAGR, driven by sub-6 GHz massive MIMO, AESA radar procurement, and larger GaN-on-SiC wafers that have cut ~30% off $/W since 2024 [27]. **REPORTED** — these are market-research figures, treat the CAGR as directional.

**Direct RF sampling.** AMD Zynq UltraScale+ RFSoC Gen 3 (e.g. ZU49DR) integrates 16 ADC + 16 DAC channels, 14-bit, ~6 GHz analog bandwidth, ADCs to ~5 GSa/s and DACs to ~9.85 GSa/s, tightly coupled to programmable logic and Arm cores [7][8]. As of Nov 2025 **AMD Versal RF** ships with 14-bit converters at 32 GSPS, 18 GHz RF-ADC input bandwidth and 80 TOPS of DSP, presented at Hot Chips 2026 — but it is aimed at aerospace/defense and test-and-measurement with no hobbyist pricing [64]. **CONFIRMED.** The architectural consequence: for a widening class of systems the superheterodyne chain collapses into software, and the hard part migrates from mixers to calibration, clocking and thermal.

**Power amplifiers.** Doherty and envelope tracking remain the efficiency battleground, and this is exactly where AI design is landing (Section 2.1). A 24 GHz 65-nm CMOS transformer-based three-Tline series Doherty achieves 39% peak PAE with >24% at 6-dB back-off across 22-32.5 GHz [47] — CMOS is now credible at K/Ka-band, which matters enormously for cost-down phased arrays.

**Standards timeline.** 3GPP Release 20 began H2 2025 as the formal 6G study phase; SA1 completed the 6G use-case/requirements study (TR 22.870) in Q1 2026; Stage-2 targets ~80% completion by June 2026 with freeze in **September 2026**; Stage-3 protocol work targets **March 2027**, with Release 21 doing normative 6G specification [13][14]. **CONFIRMED.** The AI-native air interface is being specified *now*, in Rel-20 study items, with normative work in Rel-21 [15].

**Radar.** 4D imaging radar has become a standard modality in autonomous-driving datasets — KITScenes pairs global-shutter cameras, 400 m+ lidar and 4D imaging radar with HD maps [59]; STONE ships three 4D imaging radars alongside 128-channel lidar [58]. The research center of gravity has moved from the MMIC to the point cloud: fusion frameworks (Sparse4D-Radar at ~10 FPS surround-view [58]), micro-Doppler pre-crash classification [58], and graph-theoretic outlier rejection for registration in feature-poor environments [58].

**Joint communication and sensing (ISAC).** Unlike RIS, ISAC has real hardware. Recent work includes VNA-based characterization of frequency anisotropy across 6-24 GHz over 10 objects and 120 viewpoints for multi-band FR3 ISAC [56], a PIN-diode reconfigurable antenna doing passive multi-target DOA over -40° to +40° from a *single RF chain* [57], and a 5G O-RAN CSI-assisted edge-SLAM testbed on a custom UGV [56].

---

## 2. AI Meets RF

### 2.1 Inverse design has produced measured hardware

This is the section that most damages the "AI can't do real RF" objection.

- **CONFIRMED:** *Deep Learning-Driven Black-Box Doherty Power Amplifier with Pixelated Output Combiner* (arXiv 2603.16565, Mar 2026): a CNN surrogate optimizes a three-port pixelated combiner; the fabricated GaN HEMT prototype delivers >74% peak drain efficiency and 44.1+ dBm at 2.75 GHz, with 52% efficiency maintained at 9-dB back-off and >51% PAE with DPD [44].
- **CONFIRMED:** *Deep Learning-Driven Inverse Design of Doherty PAs Using Pixelated Combiners and Dual-State Impedance Synthesis* (arXiv 2606.18395, Jun 2026): CNN + genetic algorithm; measured GaN prototypes exceed 44.2 dBm with peak drain efficiency above 71.2% over 2.6-2.8 GHz and 64% at 6-dB back-off [45].
- **CONFIRMED:** *Inverse Design of Compact and Wideband Inverted Doherty PAs Using Deep Learning* (arXiv 2606.27002, Jun 2026): 51-63% peak drain efficiency, 48-54% at 6-dB back-off across 1.9-2.5 GHz at 44±0.3 dBm, with DPD [44].
- **CONFIRMED:** A 2026 *Scientific Reports* paper presents an AlphaGo-style framework for planar antenna topology synthesis — Monte Carlo tree search over design decisions with an ML surrogate predicting performance from topology [34].
- **CONFIRMED:** Pixelated-microstrip + CNN + binary PSO pipelines generate antenna geometries from performance targets; a two-stage generative + test-time-optimization framework produces *physically realizable* rectangular patch antennas hitting specified frequency responses [35].
- **REPORTED:** Huawei publicly describes AI-driven RF/antenna design as production practice [36]; IEEE Transactions on Antennas and Propagation ran a special issue on ML in antenna design, modeling and measurement [37].

The consistent pattern is **surrogate + search over a pixelated/discretized geometry**, not end-to-end generation. The surrogate is cheap to evaluate; the search carries the design intent; a final full-wave verification pass keeps it honest. **SPECULATION:** this recipe generalizes to filters, couplers, transitions, matching networks, packages, and antenna arrays, and almost none of it is productized. Every one of those papers rebuilt the pipeline from scratch.

### 2.2 Digital predistortion is already open-source and neural

- **CONFIRMED:** OpenDPDv2 (arXiv 2507.06849) is an open-source unified learning and optimization framework for neural-network DPD, reaching -59.9 dBc ACPR on a 3.5 GHz GaN Doherty PA with a quantized 450-parameter model [46].
- **CONFIRMED:** DeltaDPD exploits dynamic temporal sparsity in RNNs to reach -50.03 dBc ACPR with 52% temporal sparsity and 1.8x lower inference power [46].

**SPECULATION:** DPD is the most immediately commercializable AI-RF niche because the metric is unambiguous (ACPR/EVM), the training data comes off a bench in an afternoon, and the customer (anyone shipping a PA) already has a budget line for it.

### 2.3 The open-solver gap

- **CONFIRMED:** Meep (MIT, FDTD, Scheme/C++/Python) and openEMS (EC-FDTD, Matlab/Octave/Python) are the dominant free solvers — and neither is GPU-capable [30][31][32].
- **CONFIRMED:** FDTDX, a GPU-accelerated FDTD framework with automatic differentiation, reports ~10x over Meep and ~415x over Ceviche on a 288M-cell simulation [32]. Related work provides large-scale open-source FDTD inverse design for 3D nanostructures [33]. Neural surrogates (e.g. PIC-Flow) predict field distributions directly from geometry [32].
- **CONFIRMED:** Time-reversible gradient computation for open-source GPU-accelerated FDTD is an active 2026 research line [32].

**SPECULATION:** Photonics got GPU+autodiff FDTD first because inverse design is native to that community's economics (one mask set, huge design space). Microwave/antenna/PCB has the same Maxwell equations, a larger user base, and none of the tooling. A GPU-native, autodiff-capable solver with openEMS-compatible geometry import and a Python-first API is a genuinely unclaimed position — and it is the enabling layer under half the ideas in Section 5.

### 2.4 LLM agents driving EM simulators: real but embryonic

- **CONFIRMED:** *VortexChat* (arXiv 2608.20688, Aug 2026) is an agentic framework where an LLM orchestrates topology generation, gradient refinement and full-wave EM simulation for autonomous multi-objective photonic design from natural-language specs [53].
- **CONFIRMED:** *Research and Prototyping Study of an LLM-Based Chatbot for Electromagnetic Simulations* (arXiv 2511.17680, Nov 2025) builds a Gemini-2.0-Flash chatbot that generates and solves 2D finite-element eddy-current models using Gmsh and GetDP [54].
- **REPORTED:** Reviews of AI-enabled metadevices now explicitly discuss "large language model-assisted design" as a category [53].

**SPECULATION:** The entire published corpus of LLM-drives-EM-solver work is a handful of papers, mostly in photonics and low-frequency FEA, none in microwave/antenna, and none using the commercial solvers that actual RF teams own. Given that Keysight now emits Python for every design step [16] and Flux ships an MCP server [52], the gap between "what is possible" and "what has been built" is currently as wide as it will ever be.

### 2.5 The AI-native air interface

- **CONFIRMED:** NVIDIA open-sourced Aerial (CUDA-accelerated, software-defined full RAN stack) and ships the Sionna neural radio framework with PyTorch/TensorFlow integration, plus the Sionna Research Kit and Aerial Testbed on DGX Spark [9][10][11].
- **CONFIRMED:** NVIDIA has a real-time-capable neural receiver prototype replacing parts of PHY signal processing with learned components [9]. Note the boundary carefully: it replaces channel estimation, equalization and demapping; synchronization, FFT/OFDM and LDPC decoding remain conventional [64].
- **CONFIRMED:** The Aerial Omniverse Digital Twin does physically accurate, ray-traced 6G simulation from single tower to city scale, with software-defined RAN and UE simulators over realistic terrain [11].
- **CONFIRMED:** Rohde & Schwarz built a PoC with NVIDIA integrating digital-twin ray tracing to test 5G-Advanced/6G neural receivers under realistic radio environments [9].
- **CONFIRMED:** European research consortia are building AI-native wireless on the NVIDIA 6G research portfolio [12].

**SPECULATION:** Sionna is the most leverage-dense free artifact in RF right now — differentiable, GPU-native, ray-traced, standards-aware. A two-person team fluent in Sionna RT plus a $1.5k USRP has a simulation-to-hardware loop that a well-funded 2019 team could not have assembled at any price.

### 2.6 RF fingerprinting, spectrum sensing, and the missing corpus

- **CONFIRMED:** DeepSig received an NTIA Public Wireless Innovation Fund grant (Jan 2025) to productionize its OmniSIG AI spectrum-sensing solution inside Open RAN radio units with open interfaces, building "sensing-native RAN" [38].
- **REPORTED:** DeepSig has raised ~$16.5M total (investors include Lockheed Martin Ventures, Scout Ventures, Blu Venture) [38]; the companion brief records ~$14M [64]. Either way: the best-funded pure-play RF-ML startup has raised less than a seed-stage AI application company.
- **CONFIRMED:** The DeepSig-Anritsu partnership lets new RF signal models be learned "in days rather than months" [38]; DeepSig joined the OCUDU Ecosystem Foundation in March 2026 [38].
- **CONFIRMED:** RadioML 2018.01A (24 modulations, 2M examples of 1024 samples, HDF5), 2016.10A (11 modulations, GNU Radio, pickle) and 2016.04C are the field's benchmarks — all CC BY-NC-SA, all with "several known errata," and DeepSig states they are "NOT currently used within DeepSig products," recommending real over-the-air data instead [39].
- **CONFIRMED:** Foundation-model framing has arrived at volume: EMind (multi-task EM signal understanding) [40], *Wireless Foundation Models: State-of-the-Art and Open Challenges* (Sep 2026) [41], *Wireless Physical-Layer Foundation Models* (Aug 2026) [42], Channel2World (transformer pretrained on ~5,000 channel measurements per environment across 26,000 simulated environments) [43], GLocFM (multimodal indoor localization trained on 221 synthetic scenes via Sionna RT) [43], and foundation models for wireless localization [43].
- **CONFIRMED:** Across those abstracts, **no open weights and no open datasets are reported** [42][43].

**SPECULATION and the single clearest opportunity in this report:** the RF-ML community has a decade-old, NC-licensed, erratum-ridden, author-disowned benchmark and a rush of foundation-model papers with nothing to train on. Whoever ships a large, permissively licensed, *over-the-air* IQ corpus with a documented capture rig — plus baseline open weights — becomes the field's ImageNet moment and owns the benchmark. This is a 6-9 month project for two people with $20k of SDRs, and it converts directly into consulting, model licensing, and defense contracts.

### 2.7 What the vendors and startups are shipping

| Player | What shipped | Date | Label |
|---|---|---|---|
| Keysight | Executable RF design whiteboard; Python at every step; cross-tool | May 2026 | CONFIRMED [16] |
| Keysight | ADS 2026, RF Circuit Simulation Professional 2026 | 2026 | CONFIRMED [17][18] |
| Keysight | Chiplets + RF + AI-driven design push at DAC 2026 | Jun 2026 | REPORTED [19] |
| Flux | Copilot, AI auto-layout, AI design review, prompt-to-sim, **MCP server** | Aug 2026 | CONFIRMED [52] |
| Flux | $37M raise led by 8VC (Bain Capital Ventures, Liquid 2, Outsiders) | Feb 2026 | CONFIRMED [52] |
| Quilter | Physics-driven RL for autonomous PCB place/route/verify | ongoing | CONFIRMED [5] |
| Quilter | $25M Series B (Index); $40M total; Benchmark, Coatue, Root, Lip-Bu Tan | Oct 2025 | CONFIRMED [5][6] |
| NVIDIA | Aerial open-sourced; Sionna Research Kit on DGX Spark | 2025-2026 | CONFIRMED [10] |
| DeepSig | OmniSIG into O-RU under NTIA grant; Anritsu partnership; OCUDU | 2025-2026 | CONFIRMED [38] |
| SRS | **srsRAN_Project archived Jun 2026; development moved to OCUDU (Dec 2025)** | Dec 2025 | CONFIRMED [50][51] |

That last row matters and is easy to miss: the most-used open 5G CU/DU codebase changed identity and governance between Dec 2025 and Jun 2026. Anyone building on srsRAN needs to be on OCUDU.

---

## 3. The Talent and Knowledge Gap as a Market

This is the part of the thesis that is most correct, and most monetizable.

**Who is retiring.** ~50% of US engineers are over 50 [2][64]; >25% plan to retire within five years [2]; the ratio is roughly 3 retirees per 1-2 new engineering grads [64]. US EE enrollment is down ~90% relative to CS since the 1980s, with ~20,000 EE grads/year and fewer than half entering engineering roles [64]. RF is the third-hardest specialty to fill at 33%, behind analog (44%) and embedded (43%) [64].

**What knowledge is actually being lost.** **SPECULATION**, but specific:
- Bench craft: fixture de-embedding, TRL/SOLT calibration judgment, probe-station technique, how to tell a measurement artifact from a real resonance.
- Grounding, shielding and return-path intuition — the reason a layout that simulates clean radiates at 3 m.
- Process-specific layout rules that live in a foundry's application engineers' heads, not the PDK.
- Yield and tolerance intuition: which of your matching-network elements will actually vary and by how much.
- Failure-mode pattern matching across thermal, EMI/EMC, intermodulation and PA ruggedness — knowledge that exists as war stories, not documents.

**Who is trying to capture it, and how.**
- **Keysight** is the most explicit: the executable whiteboard exists precisely to make one engineer's decision process into "a repeatable methodology that can be shared across teams, reused, and driven by AI" [16]. That is knowledge capture sold as a workflow feature.
- **Flux** captures it as agent-accessible design context plus supply-chain data [52].
- **Quilter** captures it as learned layout policy — RL over physics, so the policy encodes what a senior layout engineer knows without anyone writing it down [5].
- **DeepSig/Anritsu** capture it as signal models learned "in days rather than months" instead of being hand-specified by an EW analyst [38].

**SPECULATION — the builder's read:** every one of those is knowledge capture at the *tool vendor's* layer, which means the captured knowledge accrues to the vendor's moat. There is no independent product that captures an *individual organization's* RF tribal knowledge (their fixtures, their PDK quirks, their historical measurement-vs-simulation deltas) and makes it queryable. That is a services-led wedge with a data moat at the end of it, and defense primes with retiring EW staff will pay for it out of a program budget rather than a tools budget.

---

## 4. Builder Opportunities: Tools, Costs, and Who Pays

### 4.1 The cheap-hardware stack (CONFIRMED prices where cited)

| Layer | Options | Cost |
|---|---|---|
| Receive-only SDR | RTL-SDR Blog V3/V4 | $30-50 [64] |
| TX/RX SDR | HackRF One, ADALM-PlutoSDR, LimeSDR | ~$150-400 |
| Research SDR | USRP B200mini $1,503; B200mini-i $1,735; B205mini-i $1,875; B206mini-i $1,820 (all 70 MHz-6 GHz, 1x1) | $1.5-1.9k [60] |
| Direct-RF sampling | RFSoC 4x2 $2,499 (academic-only); ZCU208 $17,658 | $2.5-18k [64] |
| Scalar/vector test | NanoVNA, TinySA Ultra | $50-350 |
| Software | GNU Radio (4.0 RC1, Mar 2026), OCUDU (ex-srsRAN), OpenAirInterface, Open5GS, KiCad, scikit-rf, openEMS, Meep, Sionna, OpenDPDv2 | $0 [50][51][64][46] |

Note **GNU Radio 4 RC1 (22 Mar 2026)**: modern C++ rewrite, compile-time block merging (2-10x speedups, "tens of GS/s" in fused pipelines), and a **reflection system that makes blocks self-describing** — which is exactly the interface an LLM agent needs to compose flowgraphs [64]. That is a meaningful and under-noticed enabler.

### 4.2 Silicon access for a small team (CONFIRMED, Europractice 2026 MPW price list [48])

This is the number most "just build RF chips" arguments ignore:

| Process | Price/mm² (standard) | Min area | Effective floor |
|---|---|---|---|
| UMS GH25 GaN HEMT | €3,400 | 4 mm² | ~€13.6k |
| UMS GH15 GaN HEMT | €3,600 | 4 mm² | ~€14.4k |
| UMS GH10 GaN HEMT | €4,600 | 4 mm² | ~€18.4k |
| UMS PH10 GaAs pHEMT | €2,300 | 4 mm² | ~€9.2k |
| IHP SG13G2 SiGe (350/450 GHz fT/fmax) | €7,300 | 0.8 mm² | ~€5.8k |
| GF SiGe 8XP | €5,060 | 12 mm² | ~€60.7k |
| **GF 45nm RF-SOI** | **€9,350** | **12 mm²** | **~€112k** |
| X-FAB XR013 0.13µ RF-SOI | €2,043 | 10 mm² | ~€20.4k |

Delivery is 25-50 dies; registration deadlines run ~4 weeks before GDS submission; each process runs only a handful of shuttles per year [48]. **Read this as the boundary of the thesis:** an RF *software* company can iterate weekly; an RF *silicon* company iterates on a shuttle calendar, and 45nm RF-SOI alone is a ~€112k minimum bet per attempt before packaging, test fixtures, or a single measurement.

### 4.3 Who pays

- **Defense / DoD / DARPA.** DRBE demonstrates DoD appetite for large-scale RF emulation and AI-EW test infrastructure, with transition to a Navy lab in late 2025 [20][21][22]. AFRL's Kaiju is reported at ~$150M for cognitive EW (autonomous threat classification, real-time waveform optimization, machine cognition for spectrum dominance); DARPA's Adaptive EW and RFMLS programs established the cognitive-EA and signal-classification lineage [23]. **Concretely biddable now:** SBIR/STTR topics 12846, 12849 and 12880, all closing 23 Sep 2026, among 337 open RF-keyword topics [49].
- **Ukraine and the attrition market.** The EW ↔ counter-EW cycle turns in weeks [24]. Procurement authority is decentralized to unit level; 165B+ UAH flows outside the traditional defense-industrial base; Brave1/DOT-Chain delivered 181,000+ units worth $235M+ by Q2 2026 with ~10-day order-to-delivery [24][25]. Ukraine built ~1,500 FPV-based interceptors *daily* by January 2026 [25]. Named vendors: MaXon Systems ($3,500 autonomous Shahed interceptor), Wild Hornets ($2,100 STING, 1,000+ UAV kills by Oct 2025), TAF Industries, Celebra Tech; Western: Perennial Autonomy (up to $500M Pentagon award), Anduril Roadrunner, Raytheon Coyote [25]. Economics: Shahed/Geran costs $40-80k; Ukrainian interceptors $1-3.5k; a Patriot interceptor ~$4M [25]. **Counter-signal:** fiber-optic and inertially guided drones are jam-immune, pushing procurement "toward kinetic and laser solutions" [25].
- **Operators and infrastructure.** 6G study-phase vendors need evidence before Rel-20 Stage-2 freeze (Sep 2026) and Stage-3 (Mar 2027) [13][14]. Private 5G/CBRS: the OnGo Alliance has 185+ member companies and enterprise deployments including DFW, Miami International and Minneapolis-St. Paul airports, with the current sales argument centered on TCO and ROI rather than spectrum novelty [61].
- **Automotive.** 4D imaging radar is now standard in perception datasets and stacks [58][59]; the value has moved to point-cloud processing and sensor fusion.
- **Satellite.** Direct-satellite-to-device is an active 6G research area with transformer-based detection reported at 90.5% presence-detection probability for DS2D signals [63], alongside LEO mega-constellation interference modeling and digital-twin satellite network operations [63]. **REPORTED** — commercial deployment detail is thin in the literature.

---

## 5. Top 10 Concrete Things a Fast Builder Could Ship in 6-12 Months

*All entries are labeled ANALYSIS / SPECULATION. Evidence for the "why now" is cited; the business judgment is mine.*

---

**1. An open, over-the-air RF/IQ corpus plus baseline open weights ("ImageNet for RF").**
- *Wedge:* The field's benchmark (RadioML) is 2016/2018, synthetic, CC BY-NC-SA, has known errata, and is disowned by its own author [39]; meanwhile 2026 produced a wave of wireless foundation models with no open weights or data [41][42][43].
- *V1 to ship:* 500-2,000 hours of over-the-air IQ across ISM, cellular, aviation and ISM-adjacent bands from 3-5 geographically separated capture nodes, with a **fully documented, reproducible capture rig**, per-capture metadata (LO, gain, antenna, temperature, GNSS time), Apache-2.0 or CC-BY licensing, plus a distilled baseline model and a leaderboard.
- *Tools/cost:* 5x RTL-SDR v4 ($250) or 3x PlutoSDR (~$1,000) for breadth, 2x USRP B200mini ($3,006) for quality [60], GNSSDO references, 1 rack of storage, a single A100/H100 rental for baselines. Realistic all-in: **$15-30k plus 6 months**.
- *Who pays:* nobody, directly — that is the point. It monetizes downstream as consulting for defense primes and O-RAN vendors, as licensed enterprise-grade variants, and as the credibility that wins SBIR topic 12849 [49].
- *Risk:* legal exposure on recording licensed traffic (record energy and metadata, not decoded content); the corpus must be diverse enough to generalize or it becomes RadioML 2.0.

**2. GPU + autodiff FDTD for microwave (not photonics).**
- *Wedge:* Meep and openEMS are CPU-only [30][31]; FDTDX proved 10-415x is on the table [32]; the entire GPU-autodiff EM stack was built by and for the photonics community.
- *V1:* a JAX or CUDA FDTD kernel with openEMS-compatible geometry/excitation import, S-parameter extraction into scikit-rf, and gradients through geometry. Ship as a pip package plus a hosted GPU runner.
- *Tools/cost:* 2 engineers, cloud A100/H100 time (~$2-5k/mo), no hardware.
- *Who pays:* antenna, package and PCB teams currently rationing HFSS solver cores — sell per-GPU-hour, not per seat, which is precisely the pricing the incumbents cannot match without cannibalizing licenses. Later, an EDA vendor acquisition.
- *Revenue model:* usage-based cloud ($1-5/GPU-hour margin) plus a $25-75k/yr enterprise on-prem license.
- *Risk:* accuracy credibility. Nobody tapes out on an unvalidated solver. Budget half the effort for a public validation suite against measured standards and against HFSS/CST on canonical structures.

**3. Agentic parametric-sweep and design-space orchestrator over commercial solvers.**
- *Wedge:* Keysight now emits editable Python for every design step and interops with Virtuoso, Custom Compiler and HFSS [16][17]; Flux exposes MCP [52]. The APIs exist; nobody has built the agent that uses them well.
- *V1:* an agent that takes a spec sheet in natural language, proposes a sweep plan, executes it against the customer's existing ADS/HFSS licenses, maintains a persistent design-space database, and produces a design-review document with the trade-offs surfaced.
- *Tools/cost:* LLM API budget, solver Python APIs, a vector+relational store. No hardware. 2-3 engineers.
- *Who pays:* RF IC and module teams. Position as "one senior engineer's worth of sweeps per license" — a headcount comparison, not a tools comparison, which is a far bigger budget.
- *Revenue model:* $30-100k/yr per team seat-block.
- *Risk:* the incumbent ships this themselves — Keysight explicitly says its Python/structured-data layer is "the first step toward fully automated, AI/ML-driven RF design" [16]. Your defensibility is cross-vendor coverage and the accumulated design-space data, not the agent.

**4. Neural DPD as a product.**
- *Wedge:* OpenDPDv2 and DeltaDPD prove neural DPD works and is open [46], but every PA vendor still hand-rolls its own; the metric (ACPR/EVM) is unambiguous and contractual.
- *V1:* a capture-and-train appliance — customer connects their PA and a signal generator/analyzer, you deliver a quantized DPD model (target: sub-500-parameter class, following OpenDPDv2's 450-parameter result [46]) with an FPGA/DSP reference implementation.
- *Tools/cost:* a mid-range VSA/VSG or an RFSoC board ($2.5-18k [64]), PyTorch, OpenDPDv2 as the starting point.
- *Who pays:* PA and radio-module vendors, small-cell and repeater makers, satcom terminal builders, defense transmitter programs.
- *Revenue model:* per-design NRE ($50-150k) plus per-unit royalty or a perpetual license per PA family.
- *Risk:* the large PA houses have in-house DPD teams; your market is the long tail — and the long tail has less money.

**5. RF test automation as a product (the boring, real one).**
- *Wedge:* Instrument control is still VISA/SCPI scripts owned by one person per lab, and that person is retiring [2][64]. Time-to-hire for RF is 58-62 days [64].
- *V1:* a Python framework plus LLM layer that turns a datasheet/spec table into an executable test plan, drives NanoVNA/TinySA at the low end and PNA/FieldFox/spectrum analyzers at the high end, produces signed test reports, and keeps a measurement history keyed to DUT serial number.
- *Tools/cost:* pyvisa, scikit-rf, NanoVNA + TinySA Ultra (~$400) for development, borrowed access to a real bench.
- *Who pays:* contract manufacturers, module vendors, defense primes' test labs, hardware startups without a test engineer.
- *Revenue model:* $500-2,000/month/bench SaaS; enterprise on-prem at $50k+/yr for ITAR-constrained customers.
- *Risk:* low technical risk, high sales-cycle risk. Test labs are conservative and the buyer is a manager, not the engineer who likes your tool.

**6. Low-cost digital-beamforming phased-array reference design.**
- *Wedge:* RFSoC Gen3 puts 16 coherent TX/RX channels and ~6 GHz BW in one part [7][8], and Versal RF pushes to 32 GSPS/18 GHz [64]; array cost is now dominated by the antenna, feed, calibration and thermals — not the converters. CMOS Doherty PAs are now credible at 22-32.5 GHz [47], which is the other half of the cost-down.
- *V1:* an open 8- or 16-element S- or X-band digital beamforming array: KiCad board files, openEMS/GPU-FDTD antenna models, an RFSoC firmware image, a GNU Radio 4 host stack, and — the actual hard part and the actual product — **a documented calibration procedure**.
- *Tools/cost:* RFSoC 4x2 ($2,499 academic) or ZCU208 ($17,658) [64], 2-4 PCB spins ($5-15k), a modest near-field scan rented or borrowed. Realistic: **$40-80k for V1**.
- *Who pays:* radar and satcom-terminal startups, university labs, defense R&D, C-UAS integrators.
- *Revenue model:* sell the reference design + support ($25-100k), or sell arrays at 40-60% gross margin, or use it as the loss-leader that sells idea #5.
- *Risk:* hardware margins and lead times. Also: calibration is where the tribal knowledge lives, so this is simultaneously the hardest part and the most defensible.

**7. Passive radar and wide-area spectrum monitoring appliance.**
- *Wedge:* commodity SDRs plus modern ML classification (the DeepSig lineage [38], EMind [40]) make distributed monitoring cheap; airports are already joining private-network alliances for their own RF reasons [61]; C-UAS demand is structural [25].
- *V1:* a 3-5 node GNSS-disciplined receive network with a cloud correlator producing (a) an occupancy/anomaly dashboard and (b) passive-radar detections off broadcast illuminators.
- *Tools/cost:* 5x RTL-SDR v4 or Pluto ($250-1,500), GNSSDOs, Raspberry Pi 5 hosts, GNU Radio 4, PyTorch. **Under $5k for a pilot deployment.**
- *Who pays:* airports, prisons, stadiums, data centers, critical infrastructure, spectrum regulators, defense.
- *Revenue model:* $2-10k/site/year monitoring subscription; hardware at cost.
- *Risk:* passive radar performance is illuminator-dependent and demos far better than it deploys. Be honest about detection ranges or you will burn your first three customers.

**8. Spectrum digital twin as a service.**
- *Wedge:* Aerial Omniverse Digital Twin and Sionna RT make city-scale ray-traced RF reproducible [9][11]; GLocFM already trains on 221 Sionna-RT-generated scenes [43]; R&S validated the digital-twin test methodology with NVIDIA [9].
- *V1:* upload a site (OSM/lidar/BIM), get calibrated coverage, interference and beam-planning predictions, plus a synthetic-data generator for the customer's own ML models.
- *Tools/cost:* Sionna RT, cloud GPUs, geometry pipelines. ~$3-8k/month compute for a pilot.
- *Who pays:* private-5G and CBRS integrators (185+ OnGo members [61]), neutral-host operators, C-UAS site planners, 6G research programs.
- *Revenue model:* per-site project fees ($5-25k) moving to a planning-platform subscription.
- *Risk:* ray tracing over-promises indoors and in clutter; the moat is measurement-based calibration, which means you need field data — which means idea #1 and #7 feed this one.

**9. Neural-receiver / AI-PHY evaluation harness.**
- *Wedge:* Aerial is open source [10], the R&S+NVIDIA methodology is published [9], Rel-20 Stage-2 freezes Sep 2026 and Stage-3 lands Mar 2027 [13][14], and Rel-21 does normative AI air-interface work [15]. Vendors need reproducible evidence *now*.
- *V1:* a containerized harness that runs a candidate neural receiver against a battery of Sionna-generated and captured channels, produces BLER/throughput curves against classical baselines, and flags where the learned block degrades (the honest version: NVIDIA's own receiver replaces only channel estimation, equalization and demapping [64]).
- *Tools/cost:* Sionna, Aerial, OCUDU/OAI, 1-2 USRPs ($3k [60]), GPU time.
- *Who pays:* chipset vendors, RAN vendors, test houses, national 6G programs.
- *Revenue model:* $75-250k/yr enterprise license; or run it as a service and sell reports.
- *Risk:* you are in NVIDIA's blast radius. Position as vendor-neutral cross-validation, which NVIDIA structurally cannot sell.

**10. Organizational RF knowledge capture ("your lab's memory").**
- *Wedge:* Keysight, Flux, Quilter and DeepSig are all capturing RF knowledge *into their own products* [16][52][5][38]. Nobody captures a specific organization's fixtures, PDK quirks, and simulation-vs-measurement deltas into an asset that organization owns — and the people holding that knowledge are retiring at ~3 per 1-2 replacements [64].
- *V1:* an on-prem ingestion + retrieval system over a customer's Touchstone files, test reports, ECOs, simulation decks and design reviews, with an agent that answers "why did we choose this matching topology in 2019 and what went wrong at OTA?" and that flags when a new design repeats a known failure.
- *Tools/cost:* self-hostable LLM stack, document/measurement parsers (scikit-rf handles Touchstone), an on-prem GPU box (~$15-40k) for ITAR-constrained deployments.
- *Who pays:* defense primes and tier-1 suppliers with retiring EW/radar staff — funded from program budgets, not tool budgets, which are 10-100x larger.
- *Revenue model:* services-led ($150-400k first engagement) converting to $100-300k/yr platform.
- *Risk:* it is a services business wearing a product costume for the first two years, and the sales cycle inside a prime is 9-18 months. But the data moat at the end is the most durable in this list.

---

## 6. RF vs. the Adjacent Signal-Processing Opportunity

The companion brief [64] tests a parallel thesis about DSP. The two overlap but are not the same bet.

**Where they overlap.**
- Both are bottlenecked by the same hiring numbers (analog 44%, embedded 43%, RF 33%; ~50% of engineers over 50) [64][2].
- Both have an "expert-in-a-box" pull: the skill is learned by apprenticeship on proprietary toolchains, not from open-source repos [64].
- RF foundation models and IQ/CSI foundation models are literally the same research program (IQFM, Radio-FM, CSI-JEPA, SpectrumFM, EMind, WavesFM) [64][40][41][42][43], and the missing open corpus (idea #1) serves both.
- Neural receivers sit exactly on the seam: NVIDIA's replaces channel estimation, equalization and demapping while classical sync/FFT/LDPC remain [64][9].

**Where they diverge, and why it matters for a builder.**
- **DSP is pure software; RF has an irreducible hardware tail.** The companion brief's best bets (LLM-driven DSP-to-HLS codegen, signal-analysis copilots, DDSP audio) have no fab, no chamber and no license [64]. RF's best bets keep running into €112k RF-SOI shuttles [48] and calibration hardware.
- **DSP has consolidated where RF has not.** Speech, audio codecs and DL MRI reconstruction are *closed* niches with entrenched winners [64]; RF/wireless is explicitly identified in the companion brief as "the most active and least consolidated frontier," with many papers, no winner, and no shared corpus [64]. That asymmetry is the strongest argument for choosing RF over DSP right now.
- **The instrument layer is being contested on the DSP side first.** Liquid Instruments raised $50M co-led by Keysight (May 2026) and shipped GenInst Studio — natural language to validated FPGA instrument [64]. The RF-specific analogue (natural language to a validated RF measurement) is idea #5 above and is not yet taken.
- **RF has a defense buyer that DSP mostly lacks.** SBIR topics, DARPA DRBE, AFRL Kaiju and the Ukraine market are RF-shaped demand with real money and short cycles [49][20][23][25].

**SPECULATION:** the highest-expected-value plan is a DSP-shaped *business model* (software, usage-priced, no fab) aimed at an *RF-shaped market* (defense, test, spectrum). Ideas 1, 2, 3, 5, 8, 9 and 10 all have that shape. Ideas 4 and 6 have a hardware tail; idea 7 is in between.

---

## 7. Where the Thesis Is Wrong

1. **"Stale" mistakes slow *tooling* for a slow *field*.** InP chiplets on 300 mm interposers at 140 GHz [28], GaN's ~30% $/W improvement since 2024 [27], 32 GSPS direct-RF sampling with 18 GHz input bandwidth [64], CMOS Doherty at 22-32.5 GHz [47], and an AI-native 6G PHY being specified right now [13][14][15] are not a stagnant frontier. If you build assuming the physics is settled, you will be surprised by a competitor who reads IMS proceedings.
2. **Tribal knowledge is frequently undocumented-but-correct physics, and LLMs confabulate over it silently.** Grounding, return paths, fixture de-embedding, EMI/EMC and thermal-RF coupling failures do not appear in the simulation; they appear at OTA test, months and dollars later.
3. **Calibration and measurement do not compress.** VNA calibration judgment, near-field ranges, OTA chambers and EMC pre-compliance are physical capital and physical skill. A NanoVNA is superb for learning and useless for a 28 GHz product qualification. **SPECULATION on magnitudes:** a serviceable benchtop VNA to 20+ GHz plus fixturing is a five-figure-to-low-six-figure line item, and an OTA/anechoic chamber suitable for mmWave qualification is a six-to-seven-figure facility — which is why chamber time is rented, booked weeks out, and becomes the actual critical path of a hardware schedule.
4. **Certification gates revenue, not code.** Anything that intentionally radiates needs, depending on market and application: FCC equipment authorization under 47 CFR Part 15 (or Part 90/96 for licensed and CBRS use), an EU RED (2014/53/EU) conformity assessment with harmonized EN standards, ISED certification in Canada, plus — for cellular — 3GPP RAN5 conformance and often GCF/PTCRB certification and individual carrier acceptance. Safety-critical and defense markets add DO-160 (airborne), MIL-STD-461 (EMI) and MIL-STD-810 (environmental). Realistically 6-18 months and $50-500k depending on scope. **REPORTED/SPECULATION on the ranges; the standards themselves are CONFIRMED as the applicable regimes.**
5. **Silicon iteration is calendar-bound, not compute-bound.** Europractice 2026 shows each RF process running only a handful of shuttles per year, with GDS deadlines ~4 weeks after registration and 25-50 dies delivered [48]. GF 45nm RF-SOI has a 12 mm² minimum at €9,350/mm² — **~€112k before you have measured anything** [48]. GaN MMIC entry is ~€13.6-18.4k per attempt [48]. Add packaging, fixtures and test and a "fast" RF silicon loop is quarters, not weeks. No surrogate model changes this.
6. **Export control is a real constraint on the highest-paying market.** RF/EW/radar hardware and software commonly fall under ITAR's US Munitions List Category XI (electronics/EW) and Category XV (spacecraft), or under EAR ECCNs in the 3A/5A families, with the practical consequences being US-person restrictions on who may touch the work, licensing for any export or foreign national access, and registration obligations for manufacturers [65]. **REPORTED** at this level of generality — get counsel before assuming a specific item's classification. The effect on a small team is concrete: your cheapest engineering talent may be legally unavailable to you.
7. **The defense buyer is fast in Ukraine and slow in the US.** The ~10-day DOT-Chain cycle [25] is not the US program-of-record cycle. SBIR Phase I is months to award and ~$150-300k; Phase II is another year. Do not model one on the other.
8. **The RF-defeat market is contracting inside a growing C-UAS market.** Fiber-optic and inertially guided drones are jam-immune, 35+ Ukrainian manufacturers produce fiber-optic FPVs, and procurement is shifting toward kinetic and laser tiers [25]. Build sensing and cueing (which survive), not jamming alone.
9. **RIS is not ready and may never be.** Ten consecutive latest arXiv RIS papers report no hardware prototypes, no trials and no commercialization [55]. The literature has moved to fluid/movable-element variants — a sign of theoretical elaboration outrunning practice.
10. **Incumbents own the correlation data.** Ansys, Keysight and Cadence hold decades of validated simulation-to-measurement correlation. Surrogate quality is fundamentally a data problem, and they start with the data. Your counter is either a domain they under-serve (defense EW, spectrum monitoring) or a modality they do not collect (over-the-air corpora).
11. **The exits are small so far.** The three most relevant private companies have raised $40M (Quilter), $37M (Flux) and ~$14-16.5M (DeepSig) *in total* [5][52][38][64]. Plan for a capital-efficient business, not a platform land grab.

---

## 8. Key Numbers

| Metric | Value | Label | Source |
|---|---|---|---|
| Semiconductor engineers needed by 2029 (McKinsey, via Keysight) | 88,000 | REPORTED | [16] |
| US engineers age 50+ | ~50% | CONFIRMED | [2][64] |
| Engineers planning retirement within 5 years | >25% | CONFIRMED | [2] |
| Hardest roles to fill: analog / embedded / RF | 44% / 43% / 33% | CONFIRMED | [64] |
| Average engineering time-to-hire | 58-62 days | CONFIRMED | [64] |
| US EE enrollment vs CS since 1980s | down ~90% | CONFIRMED | [64] |
| Broadcast engineers needed vs retiring (10 yr, US) | 5,100 vs 6,200 | CONFIRMED | [3] |
| RF GaN market 2026 → 2031 | $2.41B → $5.90B (19.6% CAGR) | REPORTED | [27] |
| GaN-on-SiC $/W reduction since 2024 | ~30% | REPORTED | [27] |
| RFSoC Gen3 (ZU49DR) | 16 ADC + 16 DAC, 14-bit, ~6 GHz BW | CONFIRMED | [7][8] |
| AMD Versal RF (shipping Nov 2025) | 14-bit, 32 GSPS, 18 GHz, 80 TOPS | CONFIRMED | [64] |
| AI-inverse-designed GaN Doherty PA | >74% peak DE, 52% at 9-dB back-off, 44.1 dBm @ 2.75 GHz | CONFIRMED | [44] |
| AI-inverse-designed GaN Doherty PA (2.6-2.8 GHz) | >71.2% peak DE, 64% at 6-dB back-off | CONFIRMED | [45] |
| 24 GHz CMOS series Doherty | 39% peak PAE, 21.6 dBm, 22-32.5 GHz | CONFIRMED | [47] |
| Neural DPD (OpenDPDv2, GaN Doherty @3.5 GHz) | -59.9 dBc ACPR, 450 parameters | CONFIRMED | [46] |
| FDTDX speedup vs Meep / Ceviche (288M cells) | ~10x / ~415x | CONFIRMED | [32] |
| GaN MMIC MPW floor (UMS GH25, 4 mm² min) | ~€13,600 | CONFIRMED | [48] |
| GF 45nm RF-SOI MPW floor (12 mm² min) | ~€112,200 | CONFIRMED | [48] |
| IHP SG13G2 SiGe fT/fmax | 350/450 GHz | CONFIRMED | [48] |
| USRP B200mini list price | $1,503 | CONFIRMED | [60] |
| RFSoC 4x2 (academic) / ZCU208 | $2,499 / $17,658 | CONFIRMED | [64] |
| Quilter Series B / total raised | $25M / $40M | CONFIRMED | [5][6] |
| Flux raise (Feb 2026) | $37M | CONFIRMED | [52] |
| DeepSig total raised | ~$14-16.5M | REPORTED | [38][64] |
| AFRL Kaiju cognitive EW | ~$150M | REPORTED | [23] |
| Open SBIR topics matching "radio frequency" | 337 | CONFIRMED | [49] |
| Named open SBIR topics (close 23 Sep 2026) | 12846, 12849, 12880 | CONFIRMED | [49] |
| Ukraine DOT-Chain units / value by Q2 2026 | 181,000+ / $235M+ | REPORTED | [25] |
| Ukraine order-to-delivery | ~10 days | REPORTED | [24] |
| Ukraine FPV interceptor production (Jan 2026) | ~1,500/day | REPORTED | [25] |
| Shahed/Geran cost vs Ukrainian interceptor | $40-80k vs $1-3.5k | REPORTED | [25] |
| Shahed-type launches / intercept rate (May 2026) | 8,161 / 91.73% | REPORTED | [25] |
| Ukrainian fiber-optic (jam-immune) drone makers | 35+ | REPORTED | [24][25] |
| 3GPP Rel-20 Stage-2 freeze / Stage-3 target | Sep 2026 / Mar 2027 | CONFIRMED | [13][14] |
| 6G sub-THz band | 100-300 GHz | CONFIRMED | [29] |
| imec InP chiplet on 300 mm RF interposer | 140 GHz | REPORTED | [28] |
| OnGo Alliance members | 185+ | CONFIRMED | [61] |
| IMS attendance / exhibitors (recent) | 8,808 from 53 countries / 525+ | CONFIRMED | [62] |
| RIS papers (10 most recent) with hardware prototypes | 0 | CONFIRMED | [55] |
| Wireless foundation-model papers with open weights/data | 0 of those surveyed | CONFIRMED | [42][43] |
| RadioML 2018.01A | 24 modulations, 2M x 1024 samples, CC BY-NC-SA | CONFIRMED | [39] |
| GNU Radio 4 RC1 | 22 Mar 2026, 2-10x fused-pipeline speedup | CONFIRMED | [64] |
| srsRAN_Project | archived Jun 2026; dev moved to OCUDU Dec 2025 | CONFIRMED | [50][51] |

---

## Sources

1. EE Times, "Engineer Demand Exposes Talent Gap in RF Development" — https://www.eetimes.com/engineer-demand-exposes-talent-gap-in-rf-development/ (accessed 2026-09-07)
2. Davron, "The Engineering Talent Shortage Explained: Specialization Gaps, Retirements & Workforce Trends (2026)" — https://www.davron.net/engineering-talent-shortage-explained-2026/ (accessed 2026-09-07)
3. Current.org, "Shortage of engineers poses technical challenge for pubmedia stations" (2024-02) — https://current.org/2024/02/shortage-of-engineers-poses-technical-challenge-for-pubmedia-stations/
4. Actalent, "Engineering the Future: Key Engineering Workforce Shifts Shaping 2026" — https://www.actalentservices.com/en/insights/articles/engineering-workforce-trends (accessed 2026-09-07)
5. Businesswire, "Quilter Secures $25M Series B to Eliminate Manual PCB Design with Physics-Driven AI" (2025-10-07) — https://www.businesswire.com/news/home/20251007165399/en/Quilter-Secures-$25M-Series-B-to-Eliminate-Manual-PCB-Design-with-Physics-Driven-AI
6. Crunchbase, Quilter company profile — https://www.crunchbase.com/organization/quilter (accessed 2026-09-07)
7. AMD, "An Adaptable Direct RF Sampling Solution" (WP489) — https://www.amd.com/content/dam/amd/en/documents/solutions/direct-rf-sampling-solution-white-paper.pdf
8. Tria Technologies, "Direct-RF Sampling Modules for RFSoC Systems" — https://www.tria-technologies.com/direct-rf-sampling-modules/ (accessed 2026-09-07)
9. NVIDIA Technical Blog, "Real-Time Neural Receivers Drive AI-RAN Innovation" — https://developer.nvidia.com/blog/real-time-neural-receivers-drive-ai-ran-innovation/
10. TelecomTV, "Nvidia open sources Aerial software to accelerate AI-native 6G" — https://www.telecomtv.com/content/the-future-of-ran/nvidia-open-sources-aerial-software-to-accelerate-ai-native-6g-54179/
11. NVIDIA, "AI-RAN Solutions for 5G & 6G Cellular Networks" — https://www.nvidia.com/en-us/industries/telecommunications/ai-ran/
12. NVIDIA Blog, "European Researchers Develop AI-Native Wireless Networks With NVIDIA 6G Research Portfolio" — https://blogs.nvidia.com/blog/europe-6g-research/
13. 3GPP, "Release 20" — https://www.3gpp.org/specifications-technologies/releases/release-20
14. Ericsson, "6G standardization milestones and RAN decisions" (2026-06) — https://www.ericsson.com/en/blog/2026/6/6g-standardization-key-milestones-and-ran-decisions
15. IEEE ComSoc, CFP: "Standardizing the AI-Native 6G Air Interface: Protocols, Coordination, and Integration" — https://www.comsoc.org/publications/magazines/ieee-communications-standards-magazine/cfp/standardizing-ai-native-6g-air
16. Keysight, "Keysight Tackles Semiconductor Talent Gap with Executable RF Design Whiteboard" (2026-05-28) — https://www.keysight.com/us/en/about/newsroom/news-releases/2026/0528_pr26-074-keysight-tackles-semiconduct-talent-gap-with-executable-rf-design-whiteboard.html
17. Keysight, "RF Circuit Simulation Professional 2026 Product Release" — https://www.keysight.com/us/en/lib/resources/software-releases/rf-circuit-simulation-professional-2026-product-release.html
18. Keysight, "ADS 2026 Product Release" — https://www.keysight.com/us/en/lib/resources/software-releases/ads-2026-product-release.html
19. SemiWiki, "Keysight Design Engineering Software at DAC 2026: Going Deep on Chiplets, RF and AI-Driven Design" — https://semiwiki.com/eda/keysight-eda/371330-keysight-design-engineering-software-at-dac-2026-going-deep-on-chiplets-rf-and-ai-driven-design/
20. DARPA, "Digital RF Battlespace Emulator (DRBE)" program page — https://www.darpa.mil/research/programs/digital-rf-battlespace-emulator
21. DARPA news, "Off to the races: DRBE develops world's largest real-time EW test range" (2025) — https://www.darpa.mil/news/2025/drbe-develops-largest-real-time-EW-test-range
22. Military Embedded Systems, "Electronic-warfare emulator the largest virtual RF test range ever, says DARPA" — https://militaryembedded.com/radar-ew/rf-and-microwave/electronic-warfare-emulator-the-largest-virtual-rf-test-range-ever-says-darpa
23. AW Intelligence, "AI in Electronic Warfare 2026: Cognitive Jamming, Spectrum Warfare" — https://artificialweapons.com/articles/ai-electronic-warfare-jamming (AFRL Kaiju figure: REPORTED)
24. Modern War Institute, "Build at Scale, Innovate at the Edge, Close the Feedback Loop Fast: Transforming Acquisition for the Drone Age" — https://mwi.westpoint.edu/build-at-scale-innovate-at-the-edge-close-the-feedback-loop-fast-transforming-acquisition-for-the-drone-age/
25. Drone Intelligence, "Ukraine Counter-Drone Market 2026" — https://droneintelligence.ai/intelligence/counter-drone-market-ukraine (accessed 2026-09-07)
26. CSIS, "Unleashing U.S. Military Drone Dominance: What the United States Can Learn from Ukraine" — https://www.csis.org/analysis/unleashing-us-military-drone-dominance-what-united-states-can-learn-ukraine
27. Mordor Intelligence, "RF GaN Market — Share, Size & Analysis" — https://www.mordorintelligence.com/industry-reports/rf-gan-market
28. imec, "Beyond 5G and 6G technologies" — https://www.imec-int.com/en/expertise/solutions-5g-and-wireless-iot-communication/beyond-5g-technology
29. GlobeNewswire, "6G Market Outlook 2026-2036: Sub-THz Networks, AI Integration, and Non-Terrestrial Systems Drive $300 Billion Opportunity" (2025-10-08) — https://www.globenewswire.com/news-release/2025/10/08/3163110/0/en/6G-Market-Outlook-2026-2036-Sub-THz-Networks-AI-Integration-and-Non-Terrestrial-Systems-Drive-300-Billion-Opportunity.html
30. openEMS — https://github.com/thliebig/openEMS and https://www.openems.de/
31. Meep documentation — https://meep.readthedocs.io/
32. Latitude DS, "FDTDX: An Open-Source Framework for Large-Scale Electromagnetic Simulation and Inverse Design" — https://www.latitudeds.com/post/fdtdx-an-open-source-framework-for-large-scale-electromagnetic-simulation-and-inverse-design ; see also arXiv 2603.24027, "Numerical field optimization for enhanced efficiency in time-reversible gradient computation of open-source GPU-accelerated FDTD simulations" — https://arxiv.org/pdf/2603.24027
33. arXiv 2412.12360, "A flexible framework for large-scale FDTD simulations: open-source inverse design for 3D nanostructures" — https://arxiv.org/pdf/2412.12360
34. Nature Scientific Reports, "AlphaGo-driven generative machine learning framework for inverse topology synthesis and optimization of planar antennas" — https://www.nature.com/articles/s41598-026-61389-7
35. arXiv 2505.18188, "Improving Generative Inverse Design of Rectangular Patch Antennas with Test Time Optimization" — https://arxiv.org/pdf/2505.18188
36. Huawei, "AI-Driven Innovations in RF and Antenna Design" — https://www.huawei.com/en/huaweitech/future-technologies/ai-driven-innovations-rf-antenna-design
37. IEEE APS, "Special Issue on Machine Learning in Antenna Design, Modeling, and Measurements" — https://ieeeaps.org/ieee-tap/for-readers/special-issues/special-issue-on-machine-learning-in-antenna-design-modeling-and-measurements
38. DeepSig, "DeepSig Secures NTIA Grant to Advance Telecom AI-Driven Spectrum Sensing" — https://www.deepsig.ai/deepsig-secures-ntia-grant-to-advance-telecom-ai-driven-spectrum-sensing/ ; CB Insights DeepSig profile — https://www.cbinsights.com/company/deepsig
39. DeepSig, RadioML datasets — https://www.deepsig.ai/datasets/ (accessed 2026-09-07)
40. arXiv 2508.18785, "EMind: A Foundation Model for Multi-task Electromagnetic Signals Understanding" — https://arxiv.org/pdf/2508.18785
41. arXiv 2609.04707, "Wireless Foundation Models: State-of-the-Art and Open Challenges" (2026-09-04) — https://arxiv.org/abs/2609.04707
42. arXiv 2608.20486, "Wireless Physical-Layer Foundation Models: Architectures, Learning Paradigms, Applications, and Deployment" (2026-08-20) — https://arxiv.org/abs/2608.20486 ; arXiv 2608.14694, "A Comprehensive Survey of Wireless Foundation Models for AI-Native 6G Networks" — https://arxiv.org/abs/2608.14694
43. arXiv 2608.17544, "Channel2World: A Wireless Foundation Model for RF Environment Representation" — https://arxiv.org/abs/2608.17544 ; arXiv 2608.09285, "GLocFM: A Geometry-Aware Foundation Model for 3D Indoor Wireless Localization" — https://arxiv.org/abs/2608.09285 ; arXiv 2608.30540, "Foundation Models for Wireless Localization" — https://arxiv.org/abs/2608.30540
44. arXiv 2603.16565, "Deep Learning-Driven Black-Box Doherty Power Amplifier with Pixelated Output Combiner and Extended Efficiency Range" — https://arxiv.org/abs/2603.16565 ; arXiv 2606.27002, "Inverse Design of Compact and Wideband Inverted Doherty Power Amplifiers Using Deep Learning" — https://arxiv.org/abs/2606.27002
45. arXiv 2606.18395, "Deep Learning-Driven Inverse Design of Doherty Power Amplifiers Using Pixelated Combiners and Dual-State Impedance Synthesis" — https://arxiv.org/abs/2606.18395
46. arXiv 2507.06849, "OpenDPDv2: A Unified Learning and Optimization Framework for Neural Network Digital Predistortion" — https://arxiv.org/abs/2507.06849 ; arXiv 2505.06250, "DeltaDPD: Exploiting Dynamic Temporal Sparsity in RNNs for Energy-Efficient Wideband Digital Predistortion" — https://arxiv.org/abs/2505.06250
47. arXiv 2511.12137, "A 24-GHz CMOS Transformer-Based Three-Tline Series Doherty Power Amplifier Achieving 39% PAE" — https://arxiv.org/abs/2511.12137
48. Europractice IC Service, "Schedules & Prices 2026" (MPW shuttle price list) — https://europractice-ic.com/schedules-prices-2026/ (accessed 2026-09-07)
49. SBIR.gov, open topics search for "radio frequency" — https://www.sbir.gov/topics?search=radio+frequency (accessed 2026-09-07; topics 12846, 12849, 12880 close 2026-09-23)
50. srsRAN_Project GitHub repository (archived 2026-06-01; development moved to OCUDU as of Dec 2025) — https://github.com/srsran/srsRAN_Project
51. OCUDU project — https://gitlab.com/ocudu/ocudu
52. Flux, product blog and 2026 announcements (Copilot, AI auto-layout, MCP server Aug 2026; $37M raise led by 8VC, Feb 2026) — https://www.flux.ai/p/blog (accessed 2026-09-07)
53. arXiv 2608.20688, "VortexChat: An agentic framework for autonomous multi-objective integrated photonic design" — https://arxiv.org/abs/2608.20688 ; arXiv 2510.00283, "Data driven approaches in nanophotonics: A review of AI-enabled metadevices" — https://arxiv.org/abs/2510.00283
54. arXiv 2511.17680, "Research and Prototyping Study of an LLM-Based Chatbot for Electromagnetic Simulations" — https://arxiv.org/abs/2511.17680
55. arXiv eess.SP listing for "reconfigurable intelligent surface," 10 most recent as of 2026-09-07 (incl. 2609.03484, 2608.27837, 2608.25393, 2608.21669) — http://export.arxiv.org/api/query?search_query=cat:eess.SP+AND+abs:%22reconfigurable+intelligent+surface%22
56. arXiv 2607.20994, "Beyond Point Targets: Experimental Analysis of Frequency Anisotropy for Multi-band ISAC in FR3" — https://arxiv.org/abs/2607.20994 ; arXiv 2607.10394, "CSI-Assisted Edge SLAM Testbed Platform for 5G Connected Unmanned Autonomous Vehicles" — https://arxiv.org/abs/2607.10394
57. arXiv 2607.16822, "A Compact Reconfigurable Antenna for Single-RF-Chain Passive Multi-Target DOA Estimation" — https://arxiv.org/abs/2607.16822
58. arXiv 2607.04098, "Sparse4D-Radar" — https://arxiv.org/abs/2607.04098 ; arXiv 2608.08701, "Anchor-Based AI Approach for Pre-Crash Object Detection Utilizing Micro-Doppler Signatures in Automotive Radar" — https://arxiv.org/abs/2608.08701 ; arXiv 2604.14857, "Graph Theoretical Outlier Rejection for 4D Radar Registration" — https://arxiv.org/abs/2604.14857 ; arXiv 2603.09175, "STONE Dataset" — https://arxiv.org/abs/2603.09175
59. arXiv 2606.02956, "The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset" — https://arxiv.org/abs/2606.02956
60. Ettus Research, USRP Bus Series product pricing — https://www.ettus.com/product-categories/usrp-bus-series/ (accessed 2026-09-07)
61. OnGo Alliance (CBRS) — https://ongoalliance.org/ (accessed 2026-09-07)
62. IEEE MTT-S International Microwave Symposium — https://ims-ieee.org/ (IMS2027: San Antonio, 23-28 May 2027, reorganized into RFIC / RFTT / RFSA / ARFTG; recent attendance 8,808 from 53 countries, 525+ exhibitors)
63. arXiv 2609.02955, "Direct Satellite-to-Device Communications: From Cooperative Task Offloading to Non-Cooperative Access Monitoring" — https://arxiv.org/abs/2609.02955 ; arXiv 2608.20651, "Fluid-Dynamic Interference Modeling for LEO Mega-Constellations" — https://arxiv.org/abs/2608.20651 ; arXiv 2608.12865, "Digital Twin Satellite Networks" — https://arxiv.org/abs/2608.12865
64. Companion brief: `/home/user/the-frontier/research/18-signal-processing-frontier.md` (2026-09) — hiring statistics (Quilter's 2026 compilation of IEEE/BLS/Electronic Design data), GNU Radio 4 RC1, AMD Versal RF, RFSoC/ZCU208 pricing, neural-receiver scope, RF foundation-model landscape, Liquid Instruments
65. eCFR Title 22 Part 121, US Munitions List (Category XI Electronics/EW, Category XV Spacecraft) — https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M/part-121 (classification of any specific item requires counsel)
