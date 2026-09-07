# Quantum Computing Reality Check — September 2026

*A skeptical-but-fair assessment of where quantum computing actually stands, what it will plausibly do in 2026–2032, and where classical AI/ML is quietly eating its lunch. Every claim is tagged **CONFIRMED** (peer-reviewed or primary-source, independently reproduced or uncontested), **REPORTED** (company/press claim, preprint, or single-source), or **SPECULATION** (roadmap, forecast, or opinion).*

---

## TL;DR

- **Error correction is real, and 2025–26 is the year it stopped being hypothetical.** Google's Willow demonstrated below-threshold surface codes (logical error halving per code-distance step, d=7) [1][2]; Quantinuum's Helios ran 48 error-corrected / 94 error-detected logical qubits with encoded errors ~5–15× below physical ones [5]; Harvard/QuEra/Atom Computing showed repeated QEC cycles, transversal logical gates and magic-state distillation on hundreds of neutral atoms [12][13]. **CONFIRMED.** None of it is yet a fault-tolerant computer running deep circuits — most logical-qubit demos still lean on post-selection.
- **"Quantum advantage" has moved from sampling toys to narrow physics simulations — and the classical counter-attack has not stopped.** Google's verifiable OTOC "Quantum Echoes" (Oct 2025, ~13,000× vs Frontier) [3] and IBM/Qedma's 74-qubit Floquet Ising result (July 2026) [7] are the strongest surviving claims; D-Wave's 2025 "beyond-classical" annealing was reproduced on laptops in May 2026 [9][10]; IBM's 2023 "utility" result was reproduced on a laptop in seconds [11]. Scott Aaronson now says the reality of quantum advantage "is no longer a live question" [14] — but *useful* advantage still is.
- **Resource estimates for real applications keep falling, and that is the scariest number in the field:** RSA-2048 dropped from 20M physical qubits (2019) to <1M (Gidney, May 2025) [15]; architecture-changing 2026 proposals claim <100k (qLDPC) and even ~10k neutral atoms with long runtimes [16] — **REPORTED**, not comparable like-for-like. Nobody has more than a few hundred physical qubits in a single error-corrected system today.
- **The chemistry-and-drug-discovery narrative is the most overhyped and the most exposed to classical AI.** The honest scope of "classically intractable" chemistry is ~5–10% of what industrial R&D actually computes [17]; ML interatomic potentials, neural-network wavefunctions, DMRG/tensor networks and AlphaFold-class models are absorbing the rest. Quantum-chemistry resource estimates still require thousands of logical qubits and days of runtime [17].
- **Optimization advantage remains unproven and theoretically weak.** Quadratic (Grover-type) speedups do not beat GPUs at any practical scale (Hoefler/Häner/Troyer) [18]; every annealing "supremacy" claim has been eroded by tensor networks [9][10][11].
- **Money and hype diverged violently.** IonQ/Rigetti/D-Wave rose 521%/3,270%/3,290% from Oct 2024, then fell 60–76% from 52-week highs by July 2026 [19][20]; insiders net-sold $862M over three years; P/S ratios of 59/398/542 [20]. Meanwhile Quantinuum IPO'd at >$14B (June 2026) [21], IonQ bought SkyWater for $1.8B [22], PsiQuantum raised $1B [23], and DARPA's QBI advanced 11 firms toward a 2033 "utility-scale" verdict [24].
- **Timelines have compressed but remain years out.** Expert survey (GRI, March 2026): 28–49% chance of a cryptographically relevant QC within 10 years [25]. Google, IBM, Quantinuum, Microsoft and PsiQuantum all point at 2028–2029 for "useful"/fault-tolerant machines [4][26] — **SPECULATION** until a logical gate set runs at scale.
- **Verdict for 2026–2032:** quantum will most likely deliver (a) verifiable scientific advantage in many-body physics/materials simulations by ~2027–28, (b) first fault-tolerant machines of 100–200 logical qubits by ~2029–30 if roadmaps hold, and (c) a credible cryptographic threat that forces PQC migration *before* it exists. It will **not** out-compete AI on economic impact this decade; AI is the general-purpose technology, quantum is a specialist co-processor for a narrow class of problems.

---

## 1. Error correction: the actual state of play

### Google (superconducting)

**CONFIRMED.** Willow (105 transmons, Dec 2024, *Nature*) is the first superconducting demonstration that scaling a surface code from distance 3 → 5 → 7 reduces logical error each step (suppression factor Λ ≈ 2.14; d=7 logical error ≈ 0.143%/cycle; the logical qubit outlived every one of its 101 constituent physical qubits) [1][2]. This is the "below threshold" result the field waited 30 years for.

**REPORTED.** Google's public roadmap milestones 3 (long-lived logical qubit) and 4 (logical gate between logical qubits) have not been published as of this writing; no named Willow successor with verified specs has been announced [4]. Google added a neutral-atom effort in Boulder in March 2026 [4] — a quiet hedge that superconducting qubits alone may not reach the ~1M-qubit "milestone 6". Sundar Pichai's public target is a "useful, error-corrected quantum computer" by 2029 [4]. **SPECULATION.**

### IBM (superconducting, qLDPC)

**CONFIRMED (roadmap published; hardware partly delivered).** IBM's June 2025 fault-tolerance plan: Starling (2029, Poughkeepsie) with **200 logical qubits and 100 million gates**, using bivariate-bicycle qLDPC codes IBM says need ~10× fewer physical qubits than surface codes, a "Relay-BP" decoder, and modular l-couplers; Blue Jay (2033) targets 2,000 logical qubits / 1B gates [26]. Loon (c-couplers, 6-way connectivity) shipped in 2025; Kookaburra (a single Starling module — qLDPC memory plus logical processing unit) is due in 2026; Cockatoo (inter-module entanglement) in 2027 [26][27]. Nighthawk r2 (Aug 31, 2026): 120 qubits, 218 couplers, >100k circuits/s, accurate results at 7,500+ gates [28].

**Watch item:** whether Kookaburra actually demonstrates a working qLDPC logical memory *with* logical operations in 2026. That is the load-bearing step for the 2029 date. No public result as of Sept 7, 2026.

### Quantinuum (trapped ions)

**CONFIRMED.** Helios (Nov 5, 2025): 98 barium-ion qubits, all-to-all connectivity, 2-qubit fidelity 99.921%, 1-qubit 99.9975% [29]. March 10, 2026: up to **94 error-detected and 48 error-corrected logical qubits** via concatenated "iceberg" codes (k logical in k+2 physical; 80:48 physical:logical at distance 4), with logical SPAM 3×10⁻⁵ vs 4.8×10⁻⁴ physical and logical gate error ~1×10⁻⁴ vs ~8×10⁻⁴ [5]. **Caveat:** heavy post-selection (acceptance as low as 3.2% for the deepest circuits); distance-4 codes are not a path to cryptographic scale [5]. Trapped-ion gate times (ms-scale shuttling) remain 100–1,000× slower than superconducting.

**REPORTED.** Next-generation "Sol" (2D grid, more qubits) is named in the launch coverage [29]; "Apollo" (fault-tolerant, ~2029) is the roadmap endpoint. **SPECULATION.**

### Neutral atoms (QuEra/Harvard/MIT, Atom Computing, Caltech)

**CONFIRMED.** June 2025 (*Nature*): 448-atom system, repeated (3+) QEC cycles without reset, transversal entangling gates, logical teleportation, ML decoders handling atom loss — but still **~2× above** the surface-code threshold [12]. Continuous operation of >3,000 atoms for >2 hours with reloading (Harvard, Sept 2025); Caltech ~6,100-atom arrays with >12 s coherence; first logical magic-state distillation (Harvard/QuEra) [13]. Atom Computing: toric-code QEC (June 3, 2026), NVQLink integration (Mar 2026), >$300M raise (June 16, 2026); Microsoft/Atom "Level 2" on-prem machine spec'd at 50 logical qubits [30].

**REPORTED.** QuEra's 2026 target of 100 logical qubits on ~10,000 atoms [31]; a 96-logical-qubit-on-448-atoms high-rate-code result is widely cited [12][31] but is a shallow-depth demonstration. Neutral-atom cycle times (~4–5 ms) are a serious throughput constraint: a Gidney-style factoring run at 1 µs cycles becomes years at 4 ms cycles unless massively parallelized [12][16].

### Microsoft Majorana: still unverified

**CONFIRMED.** Majorana 1 (Feb 2025): *Nature*'s own editorial note stated the paper's results "do not represent evidence for the presence of Majorana zero modes" [32]; Microsoft's Nayak conceded the qubit evidence post-dated the paper [32]. In 2026 Henry Legg published a *Nature* critique of the Topological Gap Protocol alleging an indexing bug (array indices used in place of values) and selective data; Microsoft acknowledged an "off-by-one pixel bug", called it minor, and disputes the conclusions [33].

**REPORTED.** Majorana 2 (June 2, 2026): parity lifetimes >20 s (≈1,000× improvement), lead replacing aluminum, topological gap doubled to ~70 µeV, restated 2029 goal — **not peer reviewed, no independent replication** [34]. Microsoft advanced to DARPA's final US2QC evaluation phase [34]. Bottom line: after ~20 years, no third party has confirmed a topological qubit. Treat 2029 as **SPECULATION** with lower credibility than the transmon/ion/atom roadmaps.

### PsiQuantum (photonics)

**REPORTED.** >$2B raised including a $1B Series E (Sept 2025); Brisbane site backed by ~A$940M public money; Chicago site; GlobalFoundries manufacturing; utility-scale projected 2027–28 [23][35]. **No public integrated processor beyond small cluster states; photon loss is the unresolved physics** [35]. Xanadu (GKP states demonstrated 2025) is pursuing a SPAC [23]. Photonic fault tolerance remains the least de-risked mainstream path.

---

## 2. Quantum advantage: strongest claims vs. the classical rebuttals

| Claim | Status | What happened |
|---|---|---|
| Google Sycamore RCS (2019) | **Eroded** | Tensor-network contraction reproduced samples in 86.4 s on a GPU cluster by 2024 [11] |
| USTC Gaussian boson sampling | **Eroded** | Classical algorithms simulate under realistic loss [8] |
| IBM 127-qubit "utility" (2023) | **Refuted** | BP-PEPS on a laptop, seconds, higher accuracy than hardware [11] |
| D-Wave Advantage2 "beyond classical" (Science, Mar 2025) | **Largely refuted** | Flatiron (Tindall et al., *Science*, May 2026): 3D belief-propagation tensor networks on workstations/laptops "more accurate than the latest quantum annealers" on most lattices; D-Wave says the rebuttal skipped its hardest geometries [9][10] |
| Google Quantum Echoes OTOC (Nature, Oct 22, 2025) | **Standing** | 65-qubit beyond-classical regime, 2 h vs ~13,000× longer on Frontier across nine classical methods; deterministic, cross-platform verifiable observable [3]. April 2026 preprint argues TNBP cannot feasibly simulate it [36] — note the authors are Google-affiliated. Orús et al.'s independent tensor-network review also flags it as a "potential genuine quantum advantage" [11]. The touted NMR "molecular ruler" application is explicitly "not yet beyond classical" [3] |
| Quantinuum Helios Fermi-Hubbard superconductivity (Nov 2025) | **Standing, unrefuted** | 90 qubits (72 system + 18 ancilla), non-zero pairing correlations; no classical rebuttal yet, but "no amount of classical computing could match it" is a company assertion [6] |
| IBM's three "quantum advantage era" preprints (July 27–28, 2026) | **Contested** | (i) IBM/UChicago doped-Clifford sampling: 97 physical qubits, certified fidelity lower bound 0.284, but **one accepted sample per ~1,700 shots**; (ii) Qedma/RIKEN Floquet Ising, 74 qubits vs. Fugaku (12,888 nodes, ~10¹² Pauli strings) — classical diverged after 7–15 cycles; (iii) Algorithmiq 56-qubit Loschmidt echo with no quantitative bound. A "frozen-tree" classical preprint (Oh, July 2026) already targets (i) [7]. IBM's separate Heron+Fugaku iron-sulfur chemistry result beat CCSD but sat ~0.1 Ha (≈63 kcal/mol) from DMRG — i.e., **behind** the best classical method [37] |

**Assessment.** The honest reading (shared by LaRose's Sept 2026 review [8] and Orús et al. [11]): classical methods win wherever the circuit geometry is tree-like, the dynamics are near-Clifford, or entanglement stays bounded; quantum hardware wins in high-coordination, non-Clifford, strongly entangling regimes — which is exactly the OTOC/Floquet/Fermi-Hubbard niche. That niche is *real physics*, not commerce. Aaronson's July 2026 position: sampling experiments "quite clearly are beating what can easily be simulated," and the "best available estimates of certain observables apparently now come from quantum computers" [14] — the first time that sentence has been defensible.

---

## 3. What it would actually take: resource estimates

| Application | Best current estimate | Source / status |
|---|---|---|
| RSA-2048 factoring | **<1M physical qubits, <1 week**, assuming 0.1% gate error, 1 µs surface-code cycle, 10 µs reaction time (100× Toffoli reduction vs. 2024 prior; down from 20M in 2019) | Gidney, May 2025 [15] — **CONFIRMED** (peer-reviewed analysis, not an experiment) |
| RSA-2048, qLDPC architecture | <100,000 physical qubits (Iceberg Quantum "Pinnacle", Feb 2026) | **REPORTED**, different code/connectivity — not like-for-like [16] |
| RSA-2048, neutral atoms | ~10,000 reconfigurable atoms, much longer runtime (Cain et al., Mar 2026) | **REPORTED** [16] |
| FeMoco (nitrogenase) | 2,142 logical qubits, 5.3×10⁹ Toffolis, ~4 days on ~4M physical (Lee et al. 2021); 4–195× algorithmic speedups in 2025 | **CONFIRMED** estimates [17] |
| Cytochrome P450 | ~4,900 logical qubits, ~10⁹ Toffolis, 73 h (Goings 2022); 234× via photonic compilation (2025) | **CONFIRMED** estimates [17] |
| Battery cathode XAS/RIXS | 100–500 logical qubits, <4×10⁸ T-gates (Xanadu/NRC, 2025–Feb 2026) | **REPORTED** [17] |
| Optimization (Grover-type) | Crossover vs. GPUs takes months even for trivial per-step cost; ≤68 logical binary ops affordable within a 2-week budget | Hoefler/Häner/Troyer, CACM [18] — **CONFIRMED** analysis |

Context: the largest single error-corrected demonstrations today are ~100 physical qubits (Quantinuum) to ~450 atoms (Harvard/QuEra), with logical error rates ~10⁻⁴–10⁻³. RSA-2048 needs ~10³–10⁴× more physical qubits *and* ~10⁶–10⁹ more error-free logical operations. Chemistry at FeMoco scale needs ~2,000–5,000 logical qubits at ~10⁻¹⁰ logical error. IBM Starling (200 logical, 10⁸ gates) would be roughly one order of magnitude short on qubits and 1–2 orders short on gate depth for either — which is why IBM's 2033 Blue Jay is the real "applications" machine.

---

## 4. Money, hype and government

**CONFIRMED (market data).** From Oct 1, 2024 to Jan 2026 IonQ, Rigetti and D-Wave gained 521%, 3,270% and 3,290% [19]. By July 17, 2026 they were 59.5%, 76.1% and 64.5% below 52-week highs [20]; Aug 2026 P/S ratios 59 / 398 / 542; three-year net insider selling $457M (IonQ), $74M (Rigetti), $331M (D-Wave) = $862.5M, against ~$3M of insider buying [20]. IonQ raised $2B at $93/share (Oct 2025), announced the $1.8B SkyWater acquisition (Jan 26, 2026; closed July 31), and reported Q2 2026 revenue +287% YoY [22]; it has also morphed into a space/optical-comms conglomerate (84 Skyloom terminals on orbit, NRO contract) [22] — a diversification that reads as hedging. Aaronson publicly condemned IonQ's "quantum computers won't hallucinate because they're deterministic" pitch to officials as false [38].

**CONFIRMED.** Quantinuum: $600M at $10B pre-money (Sept 2025) → IPO June 4, 2026 raising ~$1.68–1.7B at >$14B (Nasdaq: QNT); first post-IPO report (Aug 12, 2026) showed revenue +279% YoY, an Oracle Cloud Helios deployment, and a Quanta manufacturing deal [21]. Atom Computing >$300M (June 2026); QuEra $230M (early 2025, Google/SoftBank); PsiQuantum $1B (Sept 2025) [23][30][31]. Bank of America's July 2026 view: the sector still lacks "commercially relevant algorithms and fault-tolerant hardware"; IBM is the "category leader" for real revenue [20].

**CONFIRMED (government).** DARPA QBI advanced 11 firms to Stage B on Nov 6, 2025 — Atom Computing, Diraq, IBM, IonQ, Nord Quantique, Photonic, Quantinuum, Quantum Motion, QuEra, SQC, Xanadu — toward a Stage C government verification of whether a utility-scale (value > cost) machine is buildable by 2033; Stage C selections expected late 2026 [24]. Notably absent: Google, Microsoft, PsiQuantum (the latter two are in the parallel US2QC track), Rigetti, D-Wave. US Executive Order 14413 on quantum; DOE "Quantum Genesis" targeting a "fault-tolerant, scientifically relevant" capability by 2028; DIU up to $200M for quantum sensing; NIST/SRI quantum manufacturing center [39]. **SPECULATION:** DOE's 2028 date is more aggressive than any vendor's.

**Cryptography policy (CONFIRMED).** NIST IR 8547 deprecates RSA/ECC at 112-bit security by 2030 and disallows them by 2035 [16][40]. Google announced Android PQC deployment on March 25, 2026 and is widely reported to have set an internal 2029 migration target [41] — **REPORTED**.

---

## 5. Expert timelines

- **GRI Quantum Threat Timeline 2025** (published Mar 9, 2026; 26 experts): 28–49% probability of a CRQC within 10 years — the highest in seven years of surveys; 69% of respondents put ≥50% odds at 15 years; 92% at 20 years [25]. Critique: small sample, no Chinese respondents, opinion lags capability [42].
- **Scott Aaronson** (Dec 21, 2025): 2025 "met or exceeded my expectations on hardware, with multiple platforms now boasting >99.9% fidelity two-qubit gates"; he now takes the 2028–29 roadmaps of Google, Quantinuum, QuEra and PsiQuantum "more seriously" and expects detailed Shor cost estimates to stop being published for security reasons [38]. Aug 2026: "pending some breakthrough in complexity theory, the reality of quantum advantage is no longer a live question" [14].
- **Vendors**: IBM Starling 2029; Google "useful" 2029; Quantinuum Apollo ~2029; Microsoft 2029; PsiQuantum 2027–28; DOE 2028; DARPA verdict 2033 [4][23][26][34][39]. All **SPECULATION**; the 2029 clustering is partly a coordination effect.

---

## 6. Quantum vs. AI: who actually wins the next decade (analysis)

### The strongest case FOR quantum (2026–2032)

1. **The physics now works.** Below-threshold error suppression (Google), beyond-break-even logical qubits (Quantinuum), repeated QEC on hundreds of atoms — three modalities, all peer-reviewed [1][5][12]. The remaining problems are engineering and scale, not existence proofs.
2. **Verifiable advantage exists in a domain with scientific value.** OTOCs, Floquet dynamics and Fermi-Hubbard pairing are questions condensed-matter physicists actually ask; the answers are now cheaper on quantum hardware [3][6][7][14]. This is the "Megaquop" regime Preskill predicted, arriving roughly on schedule.
3. **Resource estimates have collapsed by 20–200×** in five years for both factoring and chemistry [15][17], and the trend is algorithmic, so it compounds independently of hardware.
4. **Capital is now patient and institutional**: a $14B public Quantinuum, IBM's balance sheet, Google, DARPA's 2033 gate, sovereign money in Australia/Japan/Denmark/UK [21][23][24]. The 2025–26 stock bust hit the weakest balance sheets, not the frontier labs.
5. **The cryptographic externality forces adoption regardless.** Even a 30% chance of a CRQC by 2036 makes PQC migration rational today [25]; that spend happens whether or not the machine arrives, and it is measured in the trillions of dollars of dependent infrastructure.

### The strongest case that quantum is OVERHYPED relative to AI

1. **AI is a general-purpose technology; quantum is a specialist accelerator for a small problem class.** Quantum speedups require super-quadratic algorithmic advantage on small-data problems [18]. That excludes essentially all of search, recommendation, language, vision, logistics-at-scale, and most of ML. Aaronson's own Aug 2026 post juxtaposes an OpenAI model solving ten open mathematics problems with a 74-qubit Floquet demo [14] — the asymmetry in scope is the whole story.
2. **Classical AI is eating quantum's flagship use-case from three sides.** (a) ML interatomic potentials (NequIP, AIMNet2, universal models trained on tens of millions of DFT calculations) deliver near-DFT accuracy in seconds and dominate materials/drug screening [43]; (b) neural-network quantum states (FermiNet/Psiformer-class) reach chemical accuracy on strongly correlated small molecules classically [44]; (c) AlphaFold-3-class models address the protein/binding problem that quantum never touched. The honest quantum-chemistry ledger says strongly correlated, multi-reference cases are ~5–10% of industrial computational chemistry [17], require thousands of logical qubits, and even then "evidence for exponential quantum advantage across generic chemical space has yet to be found" (Lee/Dalzell et al.) [17]. The commercial "quantum drug discovery" narrative is largely marketing.
3. **Tensor networks and GPU simulation keep moving the goalposts.** IBM 2023 on a laptop, D-Wave 2025 on a laptop, Sycamore in 86 s [9][11]. Every NISQ advantage claim carries an implicit expiry date; only error-corrected, non-Clifford-heavy circuits escape this (LaRose) [8]. AI even helps here: AlphaQubit-style neural decoders and GPU decoding (NVQLink) are classical-AI contributions *to* quantum, not the reverse [30].
4. **Optimization is theoretically dead-on-arrival for this window.** No known super-quadratic speedup for generic combinatorial optimization; annealing claims fall to belief-propagation tensor networks [10][18]. "Quantum for logistics/finance/portfolio" pitches should be discounted heavily.
5. **Timeline risk is asymmetric.** The 2029 cluster depends on unproven steps: IBM's qLDPC Kookaburra module (due 2026, not yet shown), Google's logical gates (not yet published), Microsoft's topological qubit (never independently confirmed), PsiQuantum's loss budget (no prototype) [4][26][33][35]. Meanwhile AI capabilities compound quarterly. Any 2–3-year slip pushes useful quantum outside the 2032 window entirely.
6. **The economics are still absent.** Pure-play revenue is tens of millions against multi-billion valuations; insiders sold $862M; DARPA's *own* framing is that it does not yet know if any approach can be worth more than it costs by 2033 [20][24].

### Labeled verdict

- **Near-certain (2026–2028):** more verifiable physics-simulation advantages; 100+ error-corrected logical qubits in a lab; logical gates between logical qubits on superconducting hardware; continued classical erosion of NISQ claims; PQC migration accelerating on policy, not hardware, timelines.
- **Likely (2029–2031):** at least one machine with ~100–200 logical qubits running 10⁷–10⁸ gates (IBM Starling class); first quantum-derived results in materials/catalysis that classical methods cannot check; RSA-2048 still safe from public machines.
- **Possible but unproven (by 2032):** genuine commercial ROI in chemistry/materials for the strongly correlated niche; a CRQC-scale machine in a state lab (the GRI 10-year band starts biting around 2033–36).
- **Unlikely by 2032:** broad enterprise optimization or ML advantage; quantum displacing any GPU workload; quantum being the larger economic story vs. AI in any year of the decade.

**Bottom line:** Quantum wins the *science* of computation this decade — the advantage question is settled and fault tolerance is arriving. AI wins the *economy* by a very wide margin. The right mental model is not "quantum vs. AI" but "AI everywhere, plus a quantum co-processor for a short list of many-body problems and one very important cryptanalytic one." The investment error to avoid is paying AI-platform multiples for specialist-accelerator economics.

---

## 7. Key numbers

| Metric | Value | Status | Source |
|---|---|---|---|
| Willow physical qubits / QEC | 105 qubits; Λ≈2.14 per distance step; d=7 logical error ~0.143%/cycle | CONFIRMED | [1][2] |
| Quantum Echoes advantage | 65 qubits; ~13,000× vs Frontier; 2 h runtime | CONFIRMED | [3] |
| Helios | 98 ions; 2q fidelity 99.921%; 48 corrected / 94 detected logical qubits | CONFIRMED | [5][29] |
| Helios logical vs physical error | SPAM 3×10⁻⁵ vs 4.8×10⁻⁴; gate ~1×10⁻⁴ vs ~8×10⁻⁴ | CONFIRMED | [5] |
| Neutral atoms | 448-atom QEC (2× above threshold); 3,000-atom continuous >2 h; 6,100-atom arrays | CONFIRMED | [12][13] |
| IBM Starling (2029) | 200 logical qubits, 10⁸ gates; qLDPC ~10× fewer physical qubits | ROADMAP | [26] |
| IBM Nighthawk r2 (Aug 2026) | 120 qubits, 7,500+ gates, >100k circuits/s | CONFIRMED | [28] |
| IBM/UChicago advantage certificate | fidelity ≥0.284; 0.059% acceptance (1 per ~1,700 shots) | REPORTED (preprint) | [7] |
| Majorana 2 | parity lifetime >20 s; gap ~70 µeV; no peer review/replication | REPORTED | [34] |
| RSA-2048 (surface code) | <1M physical qubits, <1 week, 0.1% error | CONFIRMED (analysis) | [15] |
| RSA-2048 (qLDPC / atoms) | <100k physical / ~10k atoms | REPORTED | [16] |
| FeMoco / P450 | 2,142 LQ, 5.3×10⁹ Toffoli, ~4 days / 4,900 LQ, 73 h | CONFIRMED (analysis) | [17] |
| Classically hard share of industrial chemistry | ~5–10% | ESTIMATE | [17] |
| CRQC within 10 yrs (expert survey) | 28–49% (n=26) | CONFIRMED (survey) | [25] |
| Pure-play stock run-up / drawdown | +521% / +3,270% / +3,290% then −59.5% / −76.1% / −64.5% | CONFIRMED | [19][20] |
| Insider net sales (IonQ/RGTI/QBTS, 3 yr) | $862.5M | CONFIRMED | [20] |
| Quantinuum IPO | ~$1.7B raised, >$14B valuation, revenue +279% YoY | CONFIRMED | [21] |
| DARPA QBI | 11 firms in Stage B; utility-scale verdict target 2033 | CONFIRMED | [24] |
| NIST PQC | deprecate 2030, disallow 2035 | CONFIRMED | [40] |

---

## Sources

1. Google, "Meet Willow, our state-of-the-art quantum chip," Dec 9, 2024 — https://blog.google/innovation-and-ai/technology/research/google-willow-quantum-chip/
2. The Next Platform, "Google Claims Quantum Error Correction Milestone With Willow Chip," Dec 9, 2024 — https://www.nextplatform.com/compute/2024/12/09/google-claims-quantum-error-correction-milestone-with-willow-chip/1649318
3. Google Research, "A verifiable quantum advantage," Oct 22, 2025 — https://research.google/blog/a-verifiable-quantum-advantage/
4. Quantum Zeitgeist, "Google Quantum AI: The Complete 2026 Guide," 2026 — https://quantumzeitgeist.com/google-quantum-computing/
5. PostQuantum, "Quantinuum Squeezes 94 Logical Qubits from 98 Physical," Mar 2026 — https://postquantum.com/quantum-research/quantinuum-94-logical-qubits/
6. Quantinuum, "Helios Delivers Quantum Advantage with Real-World Impact," Nov 5, 2025 — https://www.quantinuum.com/blog/helios-delivers-quantum-advantage-with-real-world-impact
7. PostQuantum, "IBM's Three Quantum Advantage Claims, Fact-Checked," July 2026 — https://postquantum.com/industry-news/ibm-three-quantum-advantage-papers/
8. R. LaRose, "A brief history of quantum vs classical computational advantage," *Quantum* 10, Sept 1, 2026 — https://quantum-journal.org/papers/q-2026-09-01-2198/
9. Quantum Computing Report, "Flatiron Institute Tensor Network Algorithm Advances Classical Simulation," May 22, 2026 — https://quantumcomputingreport.com/flatiron-institute-tensor-network-algorithm-overturns-historical-d-wave-quantum-supremacy-claim/
10. Physics World, "No quantum advantage (yet) in the world of tensor networks," Aug 21, 2026 — https://physicsworld.com/a/no-quantum-advantage-yet-in-the-world-of-tensor-networks/
11. Kshetrimayum, Jahromi, Singh, Orús, "Quantum Advantage: a Tensor Network Perspective," arXiv:2603.18825, Mar 2026 — https://arxiv.org/html/2603.18825
12. The Quantum Insider, "Neutral Atom Quantum Processor Demonstrates Repeatable Error Correction," June 26, 2025 — https://thequantuminsider.com/2025/06/26/neutral-atom-quantum-processor-demonstrates-repeatable-error-correction/
13. QuEra, "Neutral Atoms and the Path to Fault-Tolerant Quantum Computing," Feb 2026 — https://www.quera.com/blog-posts/neutral-atoms-and-the-path-to-fault-tolerant-quantum-computing
14. S. Aaronson, Shtetl-Optimized, "NISQ and quantum supremacy did not fail" (July 18, 2026) and "Enough with all the world-historic milestones" (Aug 7, 2026) — https://scottaaronson.blog/?cat=4
15. C. Gidney, "How to factor 2048 bit RSA integers with less than a million noisy qubits," arXiv:2505.15917, May 2025 — https://arxiv.org/abs/2505.15917
16. PostQuantum, "Quantum Breakthrough Slashes Qubit Needs for RSA-2048 Factoring" (with June 2026 update on Iceberg Quantum and Cain et al.) — https://postquantum.com/quantum-research/quantum-breakthrough-rsa-2048/
17. PostQuantum, "Quantum Chemistry's Honest Ledger: Drug Discovery & Beyond," 2026 — https://postquantum.com/quantum-utility-map/quantum-chemistry-drug-discovery-catalysis/
18. Hoefler, Häner, Troyer, "Disentangling Hype from Practicality: On Realistically Achieving Quantum Advantage," *CACM* 2023 — https://cacm.acm.org/research/disentangling-hype-from-practicality-on-realistically-achieving-quantum-advantage/
19. Motley Fool, "5 Reasons Quantum Computing Stocks Can Crash in 2026," Jan 9, 2026 — https://www.fool.com/investing/2026/01/09/5-reasons-quantum-computing-stocks-crash-in-2026/
20. Motley Fool, "$863 Million Warning," Aug 24, 2026 — https://www.fool.com/investing/2026/08/24/quantum-computing-stocks-ionq-863-million-warning/ ; Investing.com, "Quantum computing stocks outlook after a brutal selloff," July 17, 2026 — https://www.investing.com/news/stock-market-news/quantum-computing-stocks-outlook-ionq-rigetti-and-dwave-after-a-brutal-selloff-93CH-4798766
21. The Quantum Insider / Quantum Computing Report coverage of Quantinuum IPO (June 4, 2026) and Q2 results (Aug 12, 2026) — https://thequantuminsider.com/?s=quantinuum+valuation ; https://quantumcomputingreport.com/?s=Quantinuum+2026
22. IonQ newsroom, 2026 announcements (SkyWater acquisition Jan 26/July 31; Q2 2026 results Aug 5) — https://ionq.com/news
23. The Quantum Insider, "Top Photonic Quantum Computing Companies in 2026," Mar 24, 2026 — https://thequantuminsider.com/2026/03/24/11-companies-lighting-up-the-quantum-photonics-sector/
24. DARPA, "Quantum Benchmarking Initiative — Stage B selection," Nov 6, 2025 — https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection
25. Global Risk Institute, "Quantum Threat Timeline Report 2025," Mar 9, 2026 — https://globalriskinstitute.org/publication/quantum-threat-timeline-report-2025b/
26. IBM, "IBM lays out clear path to fault-tolerant quantum computing," June 2025 — https://www.ibm.com/quantum/blog/large-scale-ftqc
27. IBM Technology Atlas, "Quantum 2026" — https://www.ibm.com/roadmaps/quantum/2026/
28. IBM, "IBM Quantum Nighthawk r2 — more circuits, faster," Aug 31, 2026 — https://www.ibm.com/quantum/blog/nighthawk-r2
29. Quantum Computing Report, "Quantinuum Launches Helios," Nov 5, 2025 — https://quantumcomputingreport.com/quantinuum-launches-helios-quantum-computer-with-industry-leading-fidelity-and-singapore-partnership/
30. Atom Computing newsroom (toric-code QEC June 3, 2026; $300M raise June 16, 2026; NVQLink Mar 16, 2026; DARPA Nov 7, 2025) — https://atom-computing.com/news/
31. PostQuantum, "QuEra Computing" company profile — https://postquantum.com/quantum-computing-companies/quera/
32. Physics World, "Experts weigh in on Microsoft's topological qubit claim," Feb 25, 2025 — https://physicsworld.com/a/experts-weigh-in-on-microsofts-topological-qubit-claim/
33. Hackaday, "Microsoft's Topological Quantum Computing Claims Once Again In Question," June 30, 2026 — https://hackaday.com/2026/06/30/microsofts-topological-quantum-computing-claims-once-again-in-question/
34. The Quantum Insider, "Microsoft Reports Advances in Majorana 2," June 2, 2026 — https://thequantuminsider.com/2026/06/02/microsoft-reports-advances-in-majorana-2-following-debate-over-last-years-topological-claims/
35. PostQuantum, "PsiQuantum" company profile — https://postquantum.com/quantum-computing-companies/psiquantum/
36. Bermejo, Villalonga, Ware, Vidal, Szasz, "Tensor Networks with Belief Propagation Cannot Feasibly Simulate Google's Quantum Echoes Experiment," arXiv:2604.15427, Apr 16, 2026 — https://arxiv.org/abs/2604.15427
37. PostQuantum, "IBM Quantum Advantage 2026: Heron + Fugaku Analyzed" — https://postquantum.com/quantum-research/ibm-quantum-advantage-2026-heron-fugaku/
38. S. Aaronson, "More on whether useful quantum computing is 'imminent'," Dec 21, 2025 — https://scottaaronson.blog/?p=9425
39. National Quantum Initiative (quantum.gov), EO 14413, DOE Quantum Genesis, DIU sensing initiative, 2026 — https://www.quantum.gov/
40. NIST IR 8547 (ipd), "Transition to Post-Quantum Cryptography Standards," Nov 2024 — https://csrc.nist.gov/pubs/ir/8547/ipd
41. Google Security Blog, "Security for the Quantum Era: Implementing Post-Quantum Cryptography in Android," Mar 25, 2026 — https://security.googleblog.com/2026/03/
42. PostQuantum, "Quantum Threat Timeline Report 2025: Record Predictions, But Can the Survey Keep Up?" 2026 — https://postquantum.com/security-pqc/quantum-threat-timeline-report-2025/
43. AIMNet2 (PMC, 2025) and NequIP-class MLIP literature — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12057637/
44. Hermann et al., "Ab initio quantum chemistry with neural-network wavefunctions," *Nature Reviews Chemistry* 2023 — https://www.nature.com/articles/s41570-023-00516-8
