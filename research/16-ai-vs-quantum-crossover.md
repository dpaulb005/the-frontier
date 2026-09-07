# The AI/Quantum Crossover — Is AI Eating Quantum's Lunch?

*Research date: 2026-09-07. Companion to `03-quantum-reality-check.md`, which covers quantum hardware, error-correction milestones and the advantage-claim ledger. This report does not re-litigate those; it examines the **crossover** — the classical-AI attack surface on quantum's application layer, the AI tooling flowing back into quantum, and the economics of the two bets.*

**Thesis under test:** *"AI, not quantum computing, will deliver most of what quantum computing was promised for, and sooner."*

**Labels used throughout:** **[CONFIRMED]** = published, peer-reviewed or otherwise directly verifiable; **[REPORTED]** = credible press/preprint/company claim not independently replicated; **[SPECULATION]** = my inference or forecast.

---

## TL;DR

1. **The thesis is largely correct for chemistry and materials — the two use cases quantum marketing leaned on hardest.** In January 2026 Garnet Chan's group published a classical solution of the FeMo-cofactor (FeMoco) active-space model *to chemical accuracy*, using coupled cluster + DMRG + extrapolation. FeMoco was the canonical "you need a quantum computer for this" problem for a decade [1]. **[CONFIRMED]**
2. **The classical attack is a three-front war**: (a) neural-network quantum states (FermiNet → PsiFormer → Orbformer, neural backflow) for strongly correlated wavefunctions; (b) universal ML interatomic potentials (MACE, Meta UMA, MatterSim, Orb) replacing DFT for dynamics at 10⁴–10⁶× speedup; (c) learned exchange-correlation functionals (Microsoft Skala) replacing DFT's accuracy ceiling itself. All three matured 2024–2026. **[CONFIRMED]**
3. **Quantum's chemistry moat is narrower than advertised but not zero.** Chemical accuracy on FeMoco does *not* mean all strongly correlated systems are solved; it means the *specific* flagship benchmark fell to classical methods before a quantum computer could touch it.
4. **Optimization was always the weakest quantum claim, and it has gotten weaker.** QAOA results in 2026 show "empirical utility" against restricted classical baselines, not advantage against best-in-class classical solvers. **[CONFIRMED]**
5. **Quantum machine learning is the weakest claim of all.** Dequantization (Tang/Aaronson lineage) plus the data-loading bottleneck mean QML's plausible advantage lives only on data that is *already quantum*. **[CONFIRMED]**
6. **The reverse flow is real and underrated: AI is quantum's most valuable near-term supplier.** AlphaQubit 2 (Senior, Bausch et al., Google DeepMind + Google Quantum AI, Dec 2025 / rev. Mar 2026) decodes the distance-11 surface code in real time at **<1 µs/cycle** on commercial accelerators, and delivers the first real-time color-code decoding at distance 9 [2]. Learned decoders, RL calibration and ML pulse control are on the critical path to fault tolerance. **[CONFIRMED]**
7. **Quantum's genuine, non-dequantizable moat is cryptanalysis** (Shor). The field's leading skeptic, Scott Aaronson, co-signed a May 2026 position paper with Dan Boneh and Justin Drake putting crypto-relevant machines near **~2029** [3], and April 2026 estimates dropped the cost of attacking Bitcoin signatures to **~25,000 physical qubits** from "millions" a year earlier [48]. **[REPORTED]**
8. **Compute economics are not close.** 2026 hyperscaler AI capex is ~$660–750B with 23+ GW of datacenter capacity under construction; total 2026 private quantum VC is tracking below 2025's $4.1–4.9B. That is a **~150:1** annual spend ratio. **[CONFIRMED]**
9. **Jensen Huang's arc is the cultural tell**: Jan 2025 "15 years is on the early side" → March 2025 public walk-back at GTC Quantum Day → June 2025 "inflection point" → NVAQC in Boston. Nvidia's actual bet is that quantum is a *peripheral to GPUs*, not a replacement. **[CONFIRMED]**
10. **Verdict (high confidence):** AI delivers most of the *practically valuable* quantum promise (chemistry, materials, drug design, optimization) first and cheaper. Quantum retains a real but narrow moat in cryptanalysis, verified sampling, and a residual class of strongly correlated dynamics. The correct framing is not "AI beats quantum" but **"AI ate quantum's application layer; quantum keeps its complexity-theoretic core."**

---

## 1. The promised use cases, and what happened to each

Quantum computing's commercial pitch has, since roughly 2016, rested on five pillars. Here is the 2026 scorecard.

### 1.1 Quantum chemistry / catalysis / FeMoco — **largely conceded to classical+AI**

FeMoco, the iron-molybdenum cofactor of nitrogenase, was *the* poster child. Reiher, Wiebe, Svore, Wecker and Troyer's 2017 PNAS paper estimated ~111 logical qubits but ~10¹⁴ T-gates. A decade of algorithmic improvement — sparse qubitization (Berry/Gidney 2019, ~10¹⁰ T-gates), tensor hypercontraction (Lee et al. 2021, 2,142 logical qubits and 5.3×10⁹ Toffolis) — brought it down; Google Quantum AI's more recent compendium puts a 76-orbital FeMoco calculation near ~1,500 logical qubits and ~9 hours of runtime [4]. **[CONFIRMED as published estimates]** No machine on any public roadmap has 1,500 logical qubits before ~2029–2033.

Meanwhile the classical side finished the job. Zhai, Li, Zhang, Li, Lee and Chan (arXiv 2601.04621, submitted 8 Jan 2026, revised 22 June 2026) report the ground-state energy of a FeMo-cofactor model **to chemical accuracy** via high-order coupled cluster plus DMRG with a systematic extrapolation protocol, and find several near-degenerate spin isomers [1]. **[CONFIRMED]** Complementing this, spin-adapted neural-network backflow (SA-NNBF, arXiv 2604.06841) produces a compact variational state with far fewer parameters that beats spin-adapted DMRG at bond dimension D=1000 on strongly correlated systems [5], and mixed-precision DMRG on NVIDIA Blackwell (FP64 emulation via the Ozaki scheme) reaches milli-Hartree accuracy for active spaces up to 113 electrons in 76 orbitals [6]. **[CONFIRMED]**

The asymmetry is stark: the exact active space a quantum computer was supposed to need ~1,500 logical qubits and hours for, classical methods now do on GPUs, and the qubit count keeps being chased by better classical algorithms. There is a notable IBM-hardware attempt — "Quantifying the Coherence Wall: FeMoCo Quantum Chemistry from 48 to 108 Qubits on IBM Heron r2" — whose framing (a *coherence wall*) concedes the point; the classical DMRG-MSD + ph-AFQMC route hits chemical accuracy at the 48-qubit scale [7]. **[REPORTED — preprint]**

The broader ledger is equally unflattering to the quantum pitch. The most careful public accounting puts quantum advantage at only **5–10% of computational-chemistry workloads** — the strongly correlated, multireference cases — and dates the flagship targets accordingly: FeMoco at 2,142 logical qubits, **2033–2035**, ~$200k/calculation for ~3× efficiency over classical DMRG; cytochrome P450 (drug metabolism) at 4,900 logical qubits, **2035–2038**; battery degradation at 100–500 logical qubits, 2029–2032 — with the explicit caveat that "classical AI-driven materials discovery methods may solve the degradation puzzle first" [47]. **[REPORTED]** Note that even the friendly accounting concedes the AI race on the *earliest* achievable quantum chemistry target.

### 1.1b Neural-network quantum states: the AI front on wavefunctions

The FeMoco result above was won by *classical* methods (CC + DMRG). The specifically-AI front is neural-network quantum states (NNQS), and it has moved from toy to tool in five years:

- **FermiNet** (DeepMind, 2020) established deep-network fermionic ansätze in real space; **PsiFormer** (arXiv:2211.13672) added self-attention and improved ground-state energies by *dozens of kcal/mol* on larger molecules [43]. **[CONFIRMED]**
- **Excited states**: FermiNet/PsiFormer-based VMC recovers excitation energies and oscillator strengths accurately (Entwistle et al., *Science*, 2024) — the first NNQS result publishable in a top general-science venue [44]. **[CONFIRMED]**
- **Orbformer** (Foster, Noé, Hermann et al., arXiv:2506.19960, Jun 2025) is the field's foundation-model turn: a *transferable* wavefunction pretrained on 22,000 equilibrium and dissociating structures, amortizing cost across molecules rather than re-solving each system. On bond-dissociation benchmarks it is reported as **the only method that consistently converges to chemical accuracy (1 kcal/mol)**, with an accuracy-cost ratio rivalling classical multireference methods (NEVPT2, MRCI, MRCC) [45]. **[CONFIRMED — preprint]**
- **Neural backflow**: spin-adapted NNBF beats spin-adapted DMRG at bond dimension D=1000 with far fewer parameters [5]. **[CONFIRMED — preprint]**

Bond breaking and multireference character were exactly the regime where the quantum-chemistry-needs-a-quantum-computer argument was strongest. It is now the regime where a pretrained transformer is competitive. The scaling question is open — WF-Bench (Zhang, Duan & Luo, arXiv:2605.29683) exists precisely to measure NNQS expressivity and scaling laws, which implies the community does not yet know how far these ansätze extend [46]. **[REPORTED]**

### 1.2 Materials discovery — **decisively AI's**

Universal ML interatomic potentials (uMLIPs) are the single biggest practical transfer of quantum-chemistry workload to AI. Meta's Open Molecules 2025 (OMol25) dataset consumed ~6 billion core-hours of DFT and trained the Universal Model for Atoms (UMA) on >30 billion atoms; UMA evaluates structures in seconds on a consumer GPU [8]. **[CONFIRMED]** Alongside MACE, MatterSim (Microsoft), Orb (Orbital Materials) and the GNoME lineage, this is a working replacement for DFT-in-the-loop screening at ~10³–10⁶× cost reduction.

Caveats are real and worth stating: independent evaluation of UMA across transition-metal catalyst conformational/configurational space shows meaningful errors on exactly the hard multireference cases [9], there is documented bias in uMLIPs affecting fine-tuning [10], and a September 2025 paper asks pointedly whether "neural scaling laws [are] leading quantum chemistry astray" [11]. **[CONFIRMED as published critiques]** But the relevant comparison is not "uMLIP vs. exact"; it is "uMLIP vs. what a quantum computer will deliver by 2032," and the uMLIP is available today.

### 1.3 DFT replacement — **Microsoft is attacking the base layer**

Skala is a deep-learned exchange-correlation functional that reaches **2.8 kcal/mol MAE on GMTKN55** — better than state-of-the-art hybrid functionals — at semi-local DFT cost [12] — lead author Giulia Luise with 27 co-authors, Microsoft Research AI for Science; submitted Jun 2025, v6 Apr 2026, model and inference code open under MIT license. **[CONFIRMED — arXiv:2506.14665]** Skala 1.1, trained on 2.5× more data, shipped in CP2K with Psi4/FHI-aims/ORCA/VASP integration planned [13]. **[REPORTED]** Note the irony: Microsoft, the company that spent two decades on topological qubits partly to enable quantum chemistry, is now shipping a neural network that improves classical chemistry instead.

### 1.4 Drug binding — **never really quantum's, now clearly AI's**

The drug-discovery quantum pitch (exact binding free energies from quantum simulation) always required fault-tolerant machines that don't exist. The field moved without it: AlphaFold3 and the open Boltz/Chai lineage do co-folding; Boltz-2 predicts affinity; BoltzMol-1 (June 2026) reports confirmed hits on 6 of 10 hard targets while testing only 28–51 compounds per target [14]. **[REPORTED]** Independent evaluation is appropriately harsh — Boltz-2's top-100 predictions show no significant correlation with physics-based ESMACS binding free energies, i.e. good for triage, not for lead optimization [15]. **[CONFIRMED]** Still, "AI screening plus classical FEP" is a deployed pipeline; quantum binding-affinity calculation is a slide.

### 1.5 Optimization — **the weakest pillar, and getting weaker**

QAOA and quantum annealing were sold to logistics, finance and energy. The honest 2026 state: JPMorgan's Regularized Warm-Started QAOA on Quantinuum hardware beat *classical algorithms with the best provable guarantees* on 96-node 3-regular Max-Cut, and tensor-network simulations to 10,000 nodes showed depth-6 RWS-QAOA surpassing "the best classical heuristics under matched restrictions" [16]. **[REPORTED — preprint arXiv 2603.10191]** Read the qualifiers. "Best provable guarantee" is not "best solver"; "under matched restrictions" is not "unrestricted." The literature's own summary is that QAOA shows *empirical utility*, not formal advantage, and that hard instances may force depth to grow with problem size, killing the scaling case.

Meanwhile learned/neural combinatorial optimization and GPU-accelerated classical solvers keep moving. **[SPECULATION, medium confidence]** I expect no defensible end-to-end QAOA advantage on an industrially relevant optimization problem before 2030.

### 1.6 Quantum machine learning — **structurally cornered**

Dequantization is the decisive result. Ewin Tang's line of work, and the Aaronson-adjacent analysis that followed, showed that most claimed exponential QML speedups assumed quantum data access (QRAM) whose classical analogue (sample-and-query access) restores classical efficiency [17]. Later work tied trainability directly to dequantizability: variational models that are classically trainable tend also to be classically simulable [18]. The 2026 field consensus is explicitly defensive — "hybrid by default, kernel-first, never deployed without a classical baseline" — and that plausible advantage exists only for data with *quantum or deep algebraic structure* [19]. **[CONFIRMED as field consensus]**

The compounding problem is I/O: any QML application on classical data must load N classical numbers into a quantum state, and that loading cost typically erases the speedup. **[CONFIRMED — standard result]**

---

## 2. Tensor networks and GPUs: the classical simulation counter-punch

The pattern of the last five years is that quantum advantage claims are perishable goods.

- **Random circuit sampling:** GPU tensor-network contraction on 1,432 GPUs simulated the Sycamore 53-qubit task **7× faster** than the quantum device, with far better energy efficiency [20]. **[CONFIRMED]**
- **D-Wave's 2025 Science annealing supremacy claim:** a May 2026 Flatiron Institute Science paper on 3D tensor-network algorithms is widely reported as overturning it; D-Wave publicly disputes this, saying the classical work does not reproduce the full scope or solve the hardest instances [21][22]. **[REPORTED — contested]**
- **Fermi-Hubbard dynamics:** a Q-CTRL/IBM claim of ~3000× speedup was reduced to roughly **36×** once GPU-accelerated tensor contraction baselines were applied [23]; separate June 2026 work pushes 1D Fermi-Hubbard quench dynamics *beyond* current quantum simulations classically [24]. **[REPORTED]**
- **Google "Quantum Echoes" (Oct 2025):** OTOC-based, 65 of 105 Willow qubits, claimed 13,000× vs. the best classical method and 2.1 hours vs. ~3.2 years on Frontier per data point, and — importantly — *verifiable* [25]. Here the classical counter-attack has so far **failed**: an April 2026 paper argues that belief-propagation tensor networks **cannot** feasibly simulate the Quantum Echoes experiment [26]. **[CONFIRMED — this one is holding, as of Sept 2026]**

The correct inference is not "classical always wins." It is that (i) the claims that fall are the *application-flavored* ones, and (ii) the claims that survive are the *physics-flavored* ones (sampling, OTOCs, chaotic dynamics) with no obvious commercial customer. That distinction is the entire thesis of this report.

---

## 3. The reverse direction: AI is quantum computing's best supplier

This is where the crossover is unambiguously positive-sum, and where quantum's timeline actually improves because of AI.

**Learned decoders.** AlphaQubit (Nature, 2024) was a recurrent-transformer surface-code decoder more accurate than matching-based decoders but too slow for real time. **AlphaQubit 2** (arXiv:2512.07737, submitted 8 Dec 2025, rev. 11 Mar 2026; Senior et al., 24 authors, Bausch corresponding) closes that gap: near-optimal logical error rates for surface *and* color codes under realistic noise, real-time decoding **<1 µs per cycle** on commercial accelerators for the distance-11 surface code, better accuracy than leading real-time decoders, and the first real-time color-code decoding at distance 9 — orders of magnitude faster than other high-accuracy color-code decoders [2]. **[CONFIRMED — preprint]**

This matters more than it sounds. Decoder latency is an architectural constraint on utility-scale machines [27]; a fast, accurate neural decoder relaxes it. AI pre-decoders for surface codes [28] and RL-based decoding [29] extend the same idea. There is also "vibe decoding" work bringing color codes to surface-code performance [30]. **[REPORTED]**

**Beyond decoding**, ML is used for qubit calibration and tune-up, pulse shaping and optimal control, noise characterization, and circuit compilation/transpilation. Nvidia's NVAQC in Boston is explicitly built around GPU-accelerated quantum-classical co-processing, and CUDA-Q is the plumbing [31].

**[SPECULATION, medium-high confidence]** AI's contribution pulls fault tolerance *earlier* by perhaps 1–3 years relative to a no-ML counterfactual, chiefly via decoder throughput and calibration automation. It does not change the physical-qubit manufacturing bottleneck.

---

## 4. Where quantum keeps a genuine moat

Three areas survive the classical/AI onslaught. Confidence levels attached.

**(a) Cryptanalysis (Shor). Confidence: very high that the moat is real; medium on the date.**
There is no dequantization of Shor, no neural network that factors RSA-2048, no classical algorithm in sight. This is quantum's one unambiguous, commercially consequential advantage. The 2026 development that matters: Scott Aaronson — the field's most-cited skeptic, fresh off a two-year leave at OpenAI working on AI-safety theory — published a May 2026 post plus a position paper co-authored with Dan Boneh and Justin Drake putting crypto-relevant quantum computers around **~2029** [3]. **[REPORTED — a position paper, not a demonstration]** Resource estimates are the mechanism behind the date compression, and they collapsed again in **April 2026**: Aaronson reports a Google paper giving a more efficient Shor implementation against 256-bit elliptic-curve cryptography (published via zero-knowledge proof rather than full circuit disclosure), and a Caltech/Oratomic fault-tolerance paper with high-rate codes suited to neutral atoms. His summary: **"a mere 25,000 physical qubits might suffice"** to attack Bitcoin signatures, against estimates "in the millions" a year earlier, with ~1,200–1,450 logical qubits for the computation itself. He judges the net timeline effect at "maybe a year" [48]. **[REPORTED]** A telling AI footnote: Oratomic claimed AI was instrumental in developing their algorithm — which Aaronson treats as unremarkable contemporary practice, not a quantum-specific fact.

Practically, this makes **PQC migration**, not quantum computing, the real 2026–2030 quantum industry. NIST IR 8547 deprecates 112-bit-security classical public-key (RSA-2048, P-256) in **2030** and disallows all quantum-vulnerable public-key by **2035**; NSA CNSA 2.0 requires quantum-resistant crypto for new NSS acquisitions from **2027**, with full enforcement by end of **2031** [32]. Only ~5% of organizations report a defined quantum strategy [33]. **[CONFIRMED]** "Harvest now, decrypt later" makes the migration deadline effectively *today* for long-lived secrets.

**(b) Simulating quantum dynamics that resist tensor-network compression. Confidence: high that a residual class exists; low that it is commercially valuable this decade.**
The Quantum Echoes result surviving the belief-propagation attack [26] is the best current evidence. Real-time dynamics of strongly correlated systems, high entanglement growth, and out-of-equilibrium quantum matter are where classical methods genuinely scale badly. **[CONFIRMED]** The honest caveat: these are physics experiments, and the path from "OTOC on 65 qubits" to "NMR structure determination that pharma pays for" is unproven.

**(c) Certified randomness and verifiable sampling. Confidence: high technically, low commercially.**
Sampling-based advantage claims are the most robust class, and certified randomness is a genuine product. It is a small market.

**What does *not* survive:** generic optimization, machine learning on classical data, "quantum finance," and — increasingly — the mainline quantum-chemistry pitch as it was sold.

---

## 5. Public statements: the two camps talking past each other

**Jensen Huang** is the useful case study. January 2025: useful quantum computers are 15+ years out, "15 years is on the early side" — quantum stocks (IonQ, Rigetti, D-Wave, QUBT) fell double digits [34]. March 2025 GTC "Quantum Day": Huang walked it back on stage — "the first event in history where a company CEO invites all of the guests to explain why he was wrong" [35]. June 2025: quantum is at an "inflection point" and "within reach" [36]. **[CONFIRMED]**

Read this as positioning, not physics. Nvidia's structural bet — NVAQC, CUDA-Q, GPU tensor-network simulators, GPU-accelerated decoders — is that **quantum processors become accelerators attached to GPU supercomputers**, and that the GPU sells either way. Nvidia simultaneously funds the strongest classical rebuttals to quantum advantage (GPU tensor networks) and the strongest AI tooling for quantum error correction. That is a hedge, and it is a rational one.

Scott Aaronson supplies the other useful data point, from the opposite direction. He rejects the idea that he has reversed himself — "A decade ago you said you were 35. Now you say you're 45" — while conceding real optimism after multiple platforms cleared >99.9% two-qubit gate fidelity. Critically, his list of what quantum computers will actually do is unchanged and short: simulate quantum physics/chemistry, break deployed cryptography, and eventually give **"modest benefits"** for optimization and machine learning [49]. **[CONFIRMED]** He is scathing about vendor conflation of the two technologies, singling out IonQ's claim that quantum computers "won't hallucinate because they're deterministic" as a misrepresentation with no connection to quantum computing's actual advantages [49]. That is the cleanest example of the category error this report is about: quantum being marketed with AI's vocabulary to an audience that has stopped distinguishing them.

On the other side, quantum vendors have moved from "advantage soon" to date-certain roadmaps: IBM's Kookaburra (2026, first fault-tolerant module), Cockatoo (2027), **Starling (2029: 200 logical qubits, 100M gates)** and Blue Jay (2033: ~2,000 logical qubits, 1B ops), with qLDPC codes cutting physical overhead up to 90% [37]. IBM also says quantum advantage arrives "by 2026" — a claim that, as of September 2026, remains unmet in any commercially meaningful sense. **[REPORTED]**

---

## 6. Compute economics: a 150:1 mismatch

| Metric | AI (2026) | Quantum (2026) |
|---|---|---|
| Annual capital deployed | **$660–750B** hyperscaler capex (MSFT/GOOGL/AMZN/META/ORCL: $660–690B) [38][39] | **~$1.2B** startup funding YTD, tracking below 2025's $4.1B [40]; ~$4.9B private VC in 2025 [41] |
| Government programs | Multiple national programs, chips + energy | ~**$2B** US grants/equity across 9 companies, ~$1B to IBM [41] |
| Power | **23+ GW** datacenter capacity under construction globally [38]; US utilities planning ~$1.4T [42] | Megawatt-scale at most; dilution refrigerators are ~10–25 kW each |
| Deployed revenue-generating workloads | Enormous | Cloud access, R&D contracts, certified randomness |
| Time-to-value on chemistry | Today (uMLIPs, Skala, NNQS) | ~2029–2033 for fault-tolerant chemistry |

**Interpretation.** Annual capital runs roughly **100–150:1** in AI's favor; the power ratio is larger still. Capital does not guarantee scientific success, but it buys iteration speed — and where both sides attack the same target (electronic structure), the side with 150× the resources and a five-year deployment head start takes the application layer by default. **[SPECULATION — my inference, high confidence]**

A second-order effect: AI capex is itself *creating* the classical hardware that defeats quantum advantage claims. Every GPU cluster built for LLM training is a latent tensor-network simulator. This is a structural headwind unique to quantum — its competitor's infrastructure spending directly raises quantum's own bar for advantage.

---

## 7. Verdict

**Overall: the thesis is CORRECT as stated, with one important amendment.** AI will deliver most of what quantum was *marketed* for, sooner and cheaper. But quantum was marketed dishonestly; the things quantum was *theoretically* promised for (Shor, sampling, quantum dynamics) are not things AI touches at all.

| Claim | Verdict | Confidence |
|---|---|---|
| AI/classical methods deliver practical quantum-chemistry value before fault-tolerant QC does | **True** | **High (85%)** — FeMoco solved classically Jan 2026 [1]; uMLIPs and Skala deployed |
| Materials discovery goes to AI, not quantum | **True** | **Very high (90%)** |
| Drug binding goes to AI + classical FEP, not quantum | **True** | **Very high (90%)** |
| Optimization: no quantum advantage on industrial problems before 2030 | **True** | **High (80%)** |
| QML on classical data has no exponential advantage | **True** | **Very high (92%)** — dequantization + I/O bottleneck |
| AI materially accelerates quantum error correction | **True** | **High (85%)** — AlphaQubit 2 [2] |
| Quantum keeps an unbreachable cryptanalytic moat | **True** | **Very high (95%)** on existence; **medium (55%)** on ~2029–2032 date |
| Quantum keeps a real advantage on some strongly correlated dynamics | **True** | **Medium-high (70%)** — Quantum Echoes survived the tensor-network attack [26] |
| Quantum will be commercially significant (>$5B/yr non-government revenue) by 2030 | **Doubtful** | **Low-medium (30%)** |
| Some quantum advantage claim from 2025–26 is overturned classically by 2028 | **Likely** | **High (80%)** — base rate strongly supports this |

**The sharpest formulation:** *Quantum computing's application layer was dequantized by machine learning; its complexity-theoretic core was not.* The industry's problem is that the surviving core (factoring, sampling, exotic dynamics) has a much smaller and much stranger market than the layer it lost.

**[SPECULATION, medium confidence]** The most likely 2027–2030 storyline: quantum's commercial narrative quietly migrates from "simulate molecules" to "break/defend cryptography," PQC becomes the dominant revenue line for anything with "quantum" in the name, and quantum chemistry becomes a co-processing niche where a small quantum device supplies an active-space correction to a mostly classical/AI pipeline. That hybrid outcome is the honest bull case, and it is much less than what was sold.

---

## Sources

1. Zhai, Li, Zhang, Li, Lee, Chan — "Classical computational simulation of the FeMo-cofactor model to chemical accuracy and its implications," arXiv:2601.04621 (submitted 8 Jan 2026, rev. 22 Jun 2026). https://arxiv.org/pdf/2601.04621
2. "A scalable and real-time neural decoder for topological quantum codes" (AlphaQubit 2), arXiv:2512.07737 (Dec 2025). https://arxiv.org/abs/2512.07737
3. Scott Aaronson, "Will you heed my warnings?", Shtetl-Optimized (1 May 2026), with Boneh & Drake position paper. https://scottaaronson.blog/
4. "The Quantum Utility Ladder: Fault-Tolerant Algorithm Map" (FeMoco resource-estimate history), PostQuantum (2026). https://postquantum.com/quantum-utility-map/quantum-utility-ladder-fault-tolerant-algorithms/
5. "Spin-adapted neural-network backflow for symmetry-preserving simulations of strongly correlated electrons," arXiv:2604.06841 (2026). https://arxiv.org/html/2604.06841
6. "Mixed-Precision Ab Initio Tensor Network State Methods Adapted for NVIDIA Blackwell Technology via Emulated FP64 Arithmetic," PMC13374020 (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13374020/
7. "Quantifying the Coherence Wall: FeMoCo Quantum Chemistry from 48 to 108 Qubits on IBM Heron r2," ChemRxiv (2026). https://chemrxiv.org/doi/full/10.26434/chemrxiv.15001770/v2
8. Meta AI — OMol25 + UMA release (May 2025). https://ai.meta.com/blog/meta-fair-science-new-open-source-releases/
9. "Performance of Meta's Universal Model for Atoms across the Conformational and Configurational Space of Diverse Transition-Metal Catalysts," J. Phys. Chem. A 130(9):1897 (2026). https://pubs.acs.org/jpcafh/article/130/9/1897/5073732/
10. "Bias in Universal Machine-Learned Interatomic Potentials and its Effects on Fine-Tuning," arXiv:2603.10159. https://arxiv.org/pdf/2603.10159
11. "Are neural scaling laws leading quantum chemistry astray?", arXiv:2509.26397. https://arxiv.org/pdf/2509.26397
12. "Accurate and scalable exchange-correlation with deep learning" (Skala), arXiv:2506.14665. https://arxiv.org/abs/2506.14665
13. Microsoft Research — Skala 1.1 / DFT project page. https://www.microsoft.com/en-us/research/project/dft/use-skala/
14. "BoltzMol-1, BoltzProt-1 and the Boltz API," Labcritics (17 Jun 2026). https://labcritics.com/blog/2026/06/17/boltzmol-1-boltzprot-1-and-the-boltz-api-ai-drug-discovery-goes-full-stack/
15. "On the Reliability of AI Methods in Drug Discovery: Evaluation of Boltz-2," arXiv:2603.05532 / PMC13472093 (2026). https://arxiv.org/abs/2603.05532
16. "Regularized Warm-Started Quantum Approximate Optimization and Conditions for Surpassing Classical Solvers on the Max-Cut Problem," arXiv:2603.10191 (Mar 2026). https://arxiv.org/pdf/2603.10191
17. "Dequantizing algorithms to understand quantum advantage in machine learning," Nature Reviews Physics (2022). https://www.nature.com/articles/s42254-022-00511-w
18. "On the relation between trainability and dequantization of variational quantum learning models," arXiv:2406.07072. https://arxiv.org/pdf/2406.07072
19. "Quantum Machine Learning in 2026: State of the Field," PostQuantum. https://postquantum.com/quantum-ai/quantum-machine-learning-reality/
20. "Leapfrogging Sycamore: harnessing 1432 GPUs for 7× faster quantum random circuit sampling," PMC11881702. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11881702/
21. "Flatiron Institute Tensor Network Algorithm Advances Classical Simulation," Quantum Computing Report (May 2026). https://quantumcomputingreport.com/flatiron-institute-tensor-network-algorithm-overturns-historical-d-wave-quantum-supremacy-claim/
22. D-Wave — "D-Wave's Quantum Supremacy Result Stands" (2026). https://www.dwavequantum.com/company/newsroom/press-release/d-wave-s-quantum-supremacy-result-stands/
23. "Quantum Advantage: a Tensor Network Perspective," arXiv:2603.18825. https://arxiv.org/html/2603.18825
24. "Pushing the Classical Frontier of 1D Fermi-Hubbard Quench Dynamics Beyond Current Quantum Simulations," arXiv:2606.04771 (Jun 2026). https://arxiv.org/abs/2606.04771
25. Google — "Our Quantum Echoes algorithm is a big step toward real-world applications" (22 Oct 2025). https://blog.google/innovation-and-ai/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/
26. "Tensor Networks with Belief Propagation Cannot Feasibly Simulate Google's Quantum Echoes Experiment," arXiv:2604.15427 (2026). https://arxiv.org/html/2604.15427v1
27. "Impacts of Decoder Latency on Utility-Scale Quantum Computer Architectures," arXiv:2511.10633. https://arxiv.org/pdf/2511.10633
28. "Fast and accurate AI-based pre-decoders for surface codes," arXiv:2604.12841. https://arxiv.org/pdf/2604.12841
29. "Decoding surface codes with deep reinforcement learning and probabilistic policy reuse," arXiv:2212.11890. https://arxiv.org/pdf/2212.11890
30. "Colour Codes Reach Surface Code Performance using Vibe Decoding," arXiv:2508.15743. https://arxiv.org/pdf/2508.15743
31. Network World — "Nvidia launches research center to accelerate quantum computing breakthrough" (NVAQC, Mar 2025). https://www.networkworld.com/article/3851393/nvidia-launches-research-center-to-accelerate-quantum-computing-breakthrough.html
32. NIST IR 8547 (ipd), "Transition to Post-Quantum Cryptography Standards" (Nov 2024). https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf
33. The Quantum Insider — "Quantum Security Deadlines are Here" (8 May 2026). https://thequantuminsider.com/2026/05/08/post-quantum-migration-timelines-government-industry-impact/
34. Sherwood News — "Nvidia's Huang was 'wrong' about quantum computing timeline." https://sherwood.news/tech/nvidias-huang-was-wrong-about-quantum-computing-timeline/
35. CNBC — "Nvidia CEO Huang says was wrong about timeline for quantum computing" (20 Mar 2025). https://www.cnbc.com/2025/03/20/nvidia-ceo-huang-says-was-wrong-about-timeline-for-quantum-computing.html
36. CNBC — "Nvidia CEO says quantum computing is reaching an 'inflection point'" (11 Jun 2025). https://www.cnbc.com/2025/06/11/nvidia-ceo-says-quantum-computing-is-reaching-an-inflection-point.html
37. IBM Quantum — "IBM lays out clear path to fault-tolerant quantum computing." https://www.ibm.com/quantum/blog/large-scale-ftqc
38. BloombergNEF — "AI Data Center Build Advances at Full Speed." https://about.bnef.com/insights/data-centers/ai-data-center-build-advances-at-full-speed-five-things-to-know/
39. Futurum — "AI Capex 2026: The $690B Infrastructure Sprint." https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/
40. Crunchbase News — "Quantum Computing Startup Investment Slows In 2026." https://news.crunchbase.com/venture/quantum-computing-startup-investment-data-quantinuum-ipo/
41. The Quantum Insider — "Top Quantum Computing Investors in 2026" (26 Jun 2026). https://thequantuminsider.com/2026/06/26/top-quantum-computing-investors-in-2026/
42. Tech Insider — "US Utilities Plan $1.4T for AI Data Centers" (2026). https://tech-insider.org/us-utility-1-4-trillion-ai-data-center-energy-2026/
43. "A Self-Attention Ansatz for Ab-initio Quantum Chemistry" (PsiFormer), arXiv:2211.13672. https://arxiv.org/abs/2211.13672
44. Entwistle et al., "Accurate computation of quantum excited states with neural networks," *Science* (2024). https://www.science.org/doi/10.1126/science.adn0137
45. Foster, Noé, Hermann et al., "An ab initio foundation model of wavefunctions that accurately describes chemical bond breaking" (Orbformer), arXiv:2506.19960 (24 Jun 2025). https://arxiv.org/abs/2506.19960
46. Zhang, Duan & Luo, "WF-Bench: A Benchmark for Neural Network WaveFunction Expressivity and Scaling Laws," arXiv:2605.29683 (2026). https://arxiv.org/pdf/2605.29683
47. "Quantum Chemistry's Honest Ledger: Drug Discovery & Beyond," PostQuantum (2026). https://postquantum.com/quantum-utility-map/quantum-chemistry-drug-discovery-catalysis/
48. Scott Aaronson, "Quantum computing bombshells that are not April Fools," Shtetl-Optimized (Apr 2026). https://scottaaronson.blog/?p=9665
49. Scott Aaronson, "More on whether useful quantum computing is 'imminent'," Shtetl-Optimized (2025). https://scottaaronson.blog/?p=9425
50. DeepMind — FermiNet. https://deepmind.google/blog/ferminet-quantum-physics-and-chemistry-from-first-principles/
