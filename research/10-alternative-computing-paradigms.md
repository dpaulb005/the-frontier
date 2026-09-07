# Beyond Moore, Beside Quantum: The Non-Quantum Post-Moore Paradigms That Could Matter for AI

*Research report — compiled 2026-09-07. Claims labeled **CONFIRMED** (peer-reviewed or verifiable shipping product), **REPORTED** (credible press/company disclosure, not independently verified), **SPECULATION** (projection, simulation, or roadmap).*

*Companion briefs: **04** (AI compute hardware — Nvidia/AMD/hyperscaler ASICs, HBM, co-packaged optics as a product category) and **06** (semiconductor and EE frontiers — process nodes, GAA/CFET, packaging). This brief deliberately does not re-derive those; it covers only paradigms **outside** the CMOS-GPU mainline, and cross-references where they touch.*

---

## TL;DR

1. **Photonic interconnect has won; photonic compute has not** — and Lightmatter, the best-funded optical-compute startup, has quietly removed Envise from its product listing and gone interconnect-first [4][49]. Marvell paid ~$3.25B for Celestial AI; Ayar Labs raised $500M at $3.75B; Lightmatter raised $400M at $4.4B [8][10][50]. Optical *matrix multiply* remains a research object (65 TOPS at 78 W; 4,096 effective weights in Microsoft's *Nature* system) [7][1].
2. **Microsoft's analog optical computer is the field's most rigorous result and its clearest indictment**: 16 microLEDs, 256 weights per pass, ~20 ns loop, 99.8% MNIST — with a *projected* 500 TOPS/W against a measured 4.5 TOPS/W GPU baseline, and an admission that useful model sizes need **50–1,000 optical modules** [1][2].
3. **Thermodynamic computing has real silicon and a self-undermining benchmark.** Extropic's Z1 is a genuine watt-class die with 269,568 p-bits [51][52]. But in its own Z1T disclosure, **97% of per-token energy (285.78 of 294.52 nJ) is the FPGA**, not the thermodynamic core — and the Z1 figures are estimates, not measurements [52]. Extropic signed a $75M LOI with the US Department of Commerce in July 2026 [17].
4. **Reversible computing crossed a physics threshold, not a product one.** Vaire's 22 nm "Ice River" is the first commercial-CMOS part with *net* energy recovery — 1.77× on a capacitor array, ~50% recycled [22][23]. The clock-rate penalty makes it structurally wrong for accelerators.
5. **Analog in-memory is shipping at the edge, not the rack.** EnCharge's EN100: 200+ TOPS at 8.25 W [24]. Mythic raised $125M in Dec 2025 after nearly dying [53]; TetraMem validated a 22 nm RRAM SoC [64]; Rain AI failed to fund a leading-node tape-out and retreated to IP licensing [55]. Both outcomes are instructive.
6. **Neuromorphic is a sensor and simulation-instrument business.** Hala Point's 1.15B neurons is impressive [28]; BrainChip, the listed pure-play, books ~US$1–2M/year [58]; SpiNNcloud sells 650M-neuron machines to Leipzig and Sandia — national labs buying simulators, not hyperscalers buying inference [56][57].
7. **Wafer-scale is the only exotic paradigm genuinely at datacenter scale, and the 2026 numbers settle it.** Cerebras IPO'd at $185/share raising $5.55B, booked $209.9M core revenue in Q2 2026 (+103% YoY), and has **>600 MW live or under contract** plus a 750 MW / $20B+ OpenAI agreement [45][47][48]. No other paradigm here has a megawatt figure at all.
8. **Processing-in-memory is the highest-probability *new* entrant**, because it rides the HBM supply chain: Samsung's zHBM roadmap and 4 nm GAIA (MP as early as 2027), SK hynix's AiMX prototypes [38][60][61].
9. **Biological and DNA computing are not AI-compute stories.** Cortical Labs' 20-unit Singapore rack has 59 electrodes per ~800,000 neurons and a six-month lifespan [32][33]. DNA storage is ~$100k/MB against a ~$1,000/TB threshold [34].
10. **Data movement, not arithmetic, is the binding constraint.** A Landauer erasure at 300 K costs 2.87×10⁻²¹ J; a real 8-bit MAC costs 10⁷–10⁸× that, and most GPU joules go to moving bits [41][42]. That asymmetry is why optics wins at *moving* data long before it wins at *computing* — and why the winners in the verdict table below are packaging, memory and light rather than new device physics.

---

## 1. Photonics: the interconnect is real, the compute is a demo

### What has actually been demonstrated

**Microsoft's analog optical computer (AOC)** — published in *Nature*, 3 September 2025 — is the most carefully documented optical AI result to date [1][2][3]. **CONFIRMED**: the physical hardware is 16 microLEDs and 16 photodetectors with two spatial light modulators (one each for positive and negative matrix entries), supporting a 16-variable state vector and 256 weights per pass; up to 4,096 weights were demonstrated by time-multiplexing 16 independent 256-weight models. It hit 99.8% agreement with expected labels on MNIST, solved a 64-variable MRI-reconstruction QUMO problem and a 41-variable transaction-settlement instance with Barclays, and ran up to three orders of magnitude faster than Gurobi on selected QPLIB instances. Round-trip loop latency is ~20 ns; ML tasks converge in ~9 iterations (~180 ns).

**SPECULATION** (the authors are explicit about this): the 500 TOPS/W at 8-bit figure — roughly 2 fJ/op, versus 4.5 TOPS/W for current GPUs at the same precision, hence "100×" — is a *projection* for a future integrated system, not a measurement of the built machine. The paper itself states that practical applications need 0.1–2 billion weights, requiring **50 to 1,000 optical modules**, and estimates 800 W for a 100-million-weight system across 25 modules. Noise forces up to 11 repeated runs for averaging on regression tasks. This is the honest version of optical computing: elegant physics, four orders of magnitude of engineering left.

**Lightmatter** demonstrated four racks of production hardware at SC25 including M1000 and Passage 50, with a 16-wavelength bidirectional link at 800 Gbps over a single fiber and BER below 10⁻⁹ under thermal stress (**REPORTED**) [4]. In March 2026 it announced Passage L20, a 6.4 Tbps unified optical engine for near-package and on-board optics, sampling late 2026, and joined NVIDIA's NVLink Fusion ecosystem [5]. Its 2025 *Nature* paper demonstrated a photonic processor running ResNet, BERT, and an Atari deep-RL policy at near-electronic accuracy (**CONFIRMED**) [6]. Note the split, and note that Lightmatter has now made it official: **Envise, its photonic AI inference server, has been removed from the company's products listing**, and both its public messaging and its roadmap are now interconnect-first — Passage L200/L200x at 32–64 Tbps in 2026 [4][5][49]. **REPORTED**: a $400M Series D in October 2025 (Google re-investing) at a $4.4B valuation, ~$850M raised in total [49][50]. When the best-funded photonic-compute startup quietly stops selling photonic compute, that is the single most informative data point in this section.

**Q.ANT** is the most interesting counterexample — a thin-film lithium niobate photonic NPU shipped as a PCIe card in a rack server. **CONFIRMED**: units are installed at Germany's LRZ and Jülich supercomputing centres. **REPORTED**: LRZ found the second-generation NPU up to 100× faster than gen 1; Q.ANT's internal benchmarks claim up to 30× energy efficiency versus conventional processors; in May 2026 IONOS became the first commercial cloud datacenter to host the Native Processing Server [11][12]. The load-bearing caveat: 100× over your own first prototype is not 100× over an H200.

**Lightelligence** showed PACE 2 at OFC 2026 — an optoelectronic accelerator card with >40,000 photonic devices and a fully configurable 128×128 optical matrix, with ONNX/PyTorch/TVM support — and listed on the Hong Kong Stock Exchange on 28 April 2026 (01879.HK), the first pure-play AI silicon photonics listing (**REPORTED**) [13]. Academic work reports 65.5 TOPS from four 128×128 photonic tensor cores at 78 W electrical (**CONFIRMED**) [7] — real, and roughly two orders of magnitude below a modern GPU's dense throughput.

**Celestial AI** was acquired by Marvell for ~$3.25B, completed early 2026, after a $250M Series C1 in March 2025 (total >$515M) [8][9]. **Ayar Labs** raised $500M Series E in March 2026 — $870M total, $3.75B valuation — for its TeraPHY chiplet and SuperNova light source, with CEO Mark Wade projecting on-chip optical I/O maturity in 2026–2028 [10].

### Honest skepticism

Analog optical neural networks still need DACs to load inputs and ADCs to read results, and high-speed converters are expensive enough in power to erase the optical MAC advantage [14]. There is no mature optical nonlinearity, so hybrid systems bounce between domains, adding latency and joules; offline-trained weights degrade under thermal and fabrication drift; and optical processors remain "far too bulky to achieve a compute density competitive with the best modern electronic processors" [15] — the wavelength of light is a floor on component size that Moore's law does not lower. Recent electro-optic analog memory co-located with the compute unit claims >26× power savings versus SRAM-DAC architectures [14] — the right attack on the right problem, but 2026 lab work.

**Verdict for 2030:** Optical interconnect — co-packaged optics, optical scale-up fabric — is a near-certainty in AI datacenters, arguably already there. Optical *compute* as a mainstream training or inference substrate by 2030: unlikely; plausible as a niche co-processor for fixed-weight, latency-critical, or optimization workloads.

---

## 2. Thermodynamic and probabilistic computing

The pitch: generative AI is fundamentally sampling from a distribution. GPUs compute a probability vector and then sample from it — two expensive steps. A thermodynamic sampling unit (TSU) uses the chip's own electrical noise as the sampler, skipping the first step entirely.

**Extropic.** **CONFIRMED**: the X0 prototype exists and runs at room temperature, comprising dozens of probabilistic circuits (p-bits); the XTR-0 development platform shipped from Q3 2025 [16]. **REPORTED** (as of mid-2026, materially further along than the 2025 picture): the Z1 production part is specified at >269,000 p-bits with 16-neighbour connectivity, a sampling rate above 50 MHz, on a die under 12 mm a side, drawing under one watt — to ship as an M.2 "thermo compute stick" and as a PCIe card carrying >4 million p-bits [16][51]. Extropic also published **Z1T** in August 2026 — a family of sparse transformer-*like* models fitted to Z1's topology (269,568 p-bits, 2,135,904 coupling edges), replacing softmax attention with gated convolutional attention and splitting inference between Z1 and an FPGA [52]. The Z1T numbers are the most useful disclosure any thermodynamic-computing company has made, precisely because they are self-undermining in the right way: per-token energy is **294.52 nJ, of which 285.78 nJ (97%) is the FPGA and only 8.74 nJ is the Z1 itself**. Against an H100 at 50% MFU that is ~28× including the FPGA overhead, versus 935× for the Z1-only sparse layers. And Z1T needs roughly **an order of magnitude more FLOPs than GPT-2 to reach the same loss**. Extropic states plainly that the Z1 energy figures are theoretical estimates anchored to X0 experiments, not measurements from Z1 silicon [52]. **SPECULATION**: the widely-quoted 10,000× energy saving still comes from *simulating part of* Z1 running a Denoising Thermodynamic Model on a low-resolution image benchmark [16][18]. Read the 28× and the 97%-is-FPGA together and you have this entire report's thesis in one company: the exotic core is genuinely cheap, and the conventional digital periphery it needs eats the win. That is the same tax that has beaten analog optical, memristive, and neuromorphic accelerators for two decades. **REPORTED**: on 30 July 2026 Extropic signed a letter of intent with the US Department of Commerce for up to $75M through the CHIPS R&D Office to scale TSUs and onshore manufacturing [17] — meaningful third-party diligence, though an LOI is not disbursed money.

The skeptical read: p-bit and stochastic computing are decades-old ideas, and analog device variability, calibration and verification are exactly what has historically killed analog accelerators. The counter is that Extropic's device physics — shaping thermal fluctuations directly rather than building a digital RNG — is genuinely different and CMOS-compatible at room temperature, which was the historical blocker.

**Normal Computing** took a more conservative path. **CONFIRMED**: CN101, announced taped out on 12 August 2025, is a *digital* thermodynamic computing chip on standard CMOS using stochastic-computing and metastability principles, targeting linear algebra, matrix operations, and stochastic sampling [19][20][21]. **REPORTED**: up to 1000× energy efficiency on targeted workloads; roadmap of CN201 in 2026 and CN301 in late 2027 (**SPECULATION**). Doing it in standard CMOS is strategically smart — fab access and yield are not the risk. *Quanta* covered the field in July 2026, a marker that it has moved from fringe to legitimately-watched [18].

**Verdict for 2030:** The highest-variance category here. If energy-based/diffusion models stay economically central and TSUs scale, the payoff is enormous; if demand stays autoregressive-transformer-shaped, TSUs address the wrong workload. A measured 10× on a production model would move me more than any funding round.

---

## 3. Reversible and adiabatic computing

Landauer's principle says erasing a bit must dissipate at least *kT* ln 2 — 2.87×10⁻²¹ J at 300 K. Reversible computing avoids erasure and recycles the energy in the switching capacitance rather than dumping it to heat.

**CONFIRMED**: In March 2025, **Vaire Computing** taped out "Ice River" in a commercial 22 nm planar CMOS process — the first chip to achieve *net* energy recovery in a commercial process, with a measured energy-recovery factor of 1.77× for a capacitor array and 1.41× for a shift-register/adder relative to square-wave-driven equivalents, and an on-chip resonator recycling ~50% of energy on average [22][23]. IEEE Spectrum's framing — "reversible computing escapes the lab" — is fair.

The honest caveats: adiabatic switching energy scales roughly with 1/(switching time), so savings are bought with clock speed — at AI-accelerator frequencies, adiabatic circuits lose. Resonator infrastructure costs area. Vaire's "near-zero energy chips" framing outruns its data by a wide margin.

**Verdict for 2030:** Not in AI datacenters. Plausible in ultra-low-power edge or in specific always-on blocks. Worth tracking as the only line of work attacking the thermodynamic floor directly rather than the constant factors above it.

---

## 4. Analog in-memory computing

Multiply-accumulate performed physically in a memory array — by charge, resistance, or magnetization — eliminating the weight-fetch that dominates AI energy.

**EnCharge AI** is the furthest along commercially. **CONFIRMED**: EN100 launched May 2025 in two forms — an M.2 module delivering 200+ TOPS at 8.25 W, and a four-NPU PCIe card at roughly 1 petaops — built on capacitor-based (not resistive) analog compute-in-memory, achieving >40 TOPS/W and ~20× better performance-per-watt than competing solutions [24][25]. The capacitor choice matters: capacitance is set by geometry, which fabs control precisely, sidestepping the device-variability problem that has plagued resistive analog memory for fifteen years.

**Mythic** — the field's cautionary tale and its comeback story. **CONFIRMED**: Mythic nearly died in 2022 after running out of money, was rescued by investors, and then raised an oversubscribed **$125M round in December 2025** led by DCVC with NEA, SoftBank KR and Honda, taking total funding past $175M [53][54]. **REPORTED**: it claims ~100× performance-per-watt versus GPUs and up to 750× tokens/s for APU-based servers, and is scaling from prototypes to the M2000 series. Treat the 100× as a marketing number until a third party runs it; the more meaningful fact is that flash-based analog compute-in-memory raised nine figures in a market that had written it off.

**Rain AI** is the counter-example. **REPORTED**: despite Sam Altman's backing and early chip shipments in October 2024, Rain failed to raise the capital for a 7 nm/5 nm TSMC tape-out, and appears to have retreated to IP licensing of its (now *digital*) in-memory compute tile rather than building analog silicon [55]. The trajectory — analog neuromorphic ambition → digital in-memory tile → IP licensing — is the standard failure mode of this category, and it is worth remembering when reading any startup's TOPS/W slide.

**IBM** has the deepest research bench: the HERMES phase-change-memory analog chip has shown near-software accuracy on real workloads, an earlier PCM prototype held 17M parameters across 35M PCM cells, and IEDM 2025 work extended PCM inference to ultra-low-power edge devices [27][63]. None of it has a product date. **NorthPole** — 25× more power-efficient than 12 nm GPUs — remains a research chip with no announced commercial release [27].

**Sagence** claims Llama 2-70B at one-tenth the power of an H100 system, one-twentieth the cost and space (**REPORTED**, unverified) [26]. **TetraMem** is the RRAM entry: **CONFIRMED** tape-out, manufacture and initial silicon validation of MLX200, a 22 nm multi-level-RRAM analog IMC SoC on TSMC, with evaluation sampling expected in H2 2026 — the first credible move of memristive analog compute from 65 nm research silicon to a manufacturable node [64]. **Rain AI** has pivoted repeatedly and has not shipped a datacenter part.

**Memristors/RRAM**: 2026 *Nature Electronics* work on fault-free analogue computing with imperfect hardware [35] and 5-bit-controllable oxide RRAM crossbars are genuine progress on the precision problem [64]. **Spintronics**: a lossless, fully parallel STT-MRAM *digital* compute-in-memory macro [36], plus CRAM-ER extending spintronic CRAM to multi-bit DNNs [44]. MRAM's non-volatility and near-zero leakage make it a strong weight-*storage* candidate; that the strongest recent result is digital CIM rather than analog is telling.

**Honest skepticism**: IEEE Spectrum's summary is the one to keep — analog AI has historically "delivered modest savings, and only for modest-sized neural networks" [25]. Analog wins at low precision and small models; frontier training needs high dynamic range, the ADC tax scales with array size, and every analog generation has been outrun by the next digital node.

**Verdict for 2030:** Edge and client devices, yes — already happening. Datacenter inference for smaller models: possible, ~30%. Training: no.

---

## 5. Neuromorphic computing

**CONFIRMED**: Intel's Hala Point packs 1.15 billion neurons across 1,152 Loihi 2 processors on Intel 4, in a six-rack-unit chassis [28]. Neuromorphic principles applied to LLMs on Loihi 2 report up to ~3× less energy than transformer LLMs on an edge GPU [29] — real, but a 3× against an edge GPU is not a datacenter argument.

Commercial traction is at the sensor edge: **Innatera** raised $21M and launched Pulsar, positioned as the first mass-market neuromorphic microcontroller [30]; **SynSense** raised $27.7M in July 2025 for its Speck vision SoC and DYNAP-CNN2 [31].

**SpiNNcloud / SpiNNaker2** is the most credible attempt to put neuromorphic hardware in an actual machine room, and it deserves to be in this brief. **CONFIRMED**: SpiNNaker2 (Steve Furber's architecture, commercialized by Dresden-based SpiNNcloud) packs 152 Arm cores plus accelerators per chip, 48 chips per board. Sandia National Laboratories took delivery in June 2025 of a system simulating 150–180 million neurons [56]. **REPORTED**: a Leipzig University system of 656,640 cores / ~4,320 chips, simulating ≥650 million neurons, is the largest ordered to date, and is aimed at protein folding and personalized medicine [57]. Note what those customers are: national labs and universities buying a *simulation instrument*, not hyperscalers buying inference capacity.

**BrainChip** is the public-market reality check on edge neuromorphic. **CONFIRMED**: revenue of US$1.89M for FY2025 (up 374% from US$398k) and US$1.22M in H1 2026 against a ~US$12M net loss; a US$25M raise in December 2025; AKD1500 in volume production with silicon expected Q3 2026; a US$1.8M Raytheon/AFRL SBIR contract for neuromorphic radar processing [58][59]. Those are real numbers and they are tiny — a listed neuromorphic pure-play doing single-digit-million revenue after a decade is the honest scale of this market.

The structural problem: spiking networks excel at sparse, event-driven, temporally-structured data; dense transformer matmuls are the opposite, and neuromorphic hardware lacks a training story competitive with backpropagation at scale. Eight years after Loihi 1, there is no neuromorphic datacenter workload with a compelling TCO case.

**Verdict for 2030:** In AI *datacenters*, no. In always-on sensors, wearables, robotics and satellites, yes — a real and growing market that is simply not the AI-compute market.

---

## 6. Superconducting and cryogenic logic

Single-flux-quantum (SFQ) logic encodes bits as magnetic flux quanta, switches with Josephson junctions, and operates above 50–100 GHz with extraordinarily low switching energy [43]. **CONFIRMED** 2026 activity is real but pointed elsewhere: IBM demonstrated large-scale cryo-CMOS control for superconducting qubits [65], and a 4 K superconducting ML accelerator for qubit *state discrimination* exists [66]. Both are quantum-control applications.

The blockers are unchanged: cryogenic overhead at 4 K costs roughly 10²–10³ W at room temperature per watt removed; superconducting memory density is dismal, so you either keep DRAM warm and pay enormous I/O energy across the thermal boundary or you have almost no memory; area density has historically defeated prototypes; and there is no fab ecosystem near CMOS scale. There is no credible industrial roadmap for SFQ AI accelerators in 2026.

**Verdict for 2030:** No. Its future is as classical control logic *for quantum computers*, not as an AI substrate.

---

## 7. DNA data storage

**REPORTED**: Atlas Data Storage, spun out of Twist Bioscience in 2025, targets terabyte-scale DNA storage in 2026 with a stated ambition of 13 TB in a single drop of water [34]. Twist's long-term roadmap — a 150 nm synthesis chip — projects ~$100/TB.

**Honest skepticism**: current pricing is around **$100,000 per megabyte** (~10¹¹ $/TB) against a ~$1,000/TB enterprise adoption threshold — eight orders of magnitude of cost reduction required — with hours-to-days read/write latency, and density claims that assume near-theoretical molecular packing.

**Verdict for 2030:** Not an AI-compute technology at all. A plausible cold-archive niche at best.

---

## 8. Biological computing

**CONFIRMED**: On 6 August 2026, Cortical Labs, NUS Medicine, and datacenter operator DayOne switched on a prototype rack of 20 CL1 units in Singapore — the first "biological datacenter" [32]. Each CL1 holds ~800,000 lab-grown human neurons on a multielectrode array with 59 input channels, draws ~25 W (800–1,000 W per rack), and keeps neurons alive up to six months via onboard life support [33]. A ~120-unit Melbourne facility is planned (**REPORTED**). Switzerland's **FinalSpark** runs a remote platform of 16 brain organoids and claims ~10⁶× lower energy than digital chips (**REPORTED**, and effectively unfalsifiable given no comparable workload).

**Honest skepticism**: 59 electrodes is the entire I/O bandwidth to 800,000 neurons. Neurons die in six months. There is no programming model, no training algorithm competitive with SGD, no reproducibility across biological samples, and no benchmark on any task a GPU is used for. Superb neuroscience instrument; not computing infrastructure.

**Verdict for 2030:** No AI-datacenter role.

---

## 9. Wafer-scale, processing-in-memory, and reconfigurable dataflow — the boring winners

These three share a property the exotic paradigms lack: transistors, existing fabs, existing supply chains.

**Wafer-scale (Cerebras).** **CONFIRMED**: WSE-3 is 4 trillion transistors, 900,000 cores, 44 GB on-wafer SRAM, 46,225 mm². **REPORTED**: WSE-3 Turbo doubles compute to 250 PFLOPS per wafer at the same silicon; the CS-4, announced 18 August 2026, ties three wafers in parallel and delivers >4,400 tokens/s/user on gpt-oss-120B, claimed up to 30× faster than GPU solutions; Cerebras runs OpenAI's GPT-5.6 Sol at up to 750 tokens/s [37].

The scale question deserves specifics, because this is the one place where an exotic architecture has crossed from "deployed" to "material." **CONFIRMED**: Cerebras IPO'd in May 2026 at $185/share, raising $5.55B — the largest semiconductor IPO on record — after filing in April [45][46]. **CONFIRMED** (company financials): Q1 2026 GAAP revenue $193.4M; Q2 2026 core revenue $209.9M, up 103% year-over-year, with the fast-inference cloud business nearly quadrupling [47]. **REPORTED**: more than 600 MW of datacenter capacity live or under contract for delivery by end-2027, and a multi-year OpenAI agreement for 750 MW of inference capacity valued at over $20B, expandable toward 2 GW by 2030, plus an AWS partnership [48][47].

Put that against the rest of this report: 600 MW is a real fraction of global AI inference capacity, and no other paradigm in this document has a megawatt figure at all. Caveat the ambition properly — 750 MW *contracted* is not 750 MW *installed*, and a single customer concentration of that size is itself a risk — but the thesis "wafer-scale is the only exotic paradigm already in production AI datacenters at scale" survives contact with the numbers. The lesson: the winning "post-Moore" move so far was not new physics but refusing to cut the wafer — eliminating off-package data movement, which is where the joules were. (See brief 04 for how this sits against Nvidia Rubin and hyperscaler ASICs.)

**Processing-in-memory.** **REPORTED**: at Hot Chips 2026 Samsung laid out a three-phase HBM roadmap that progressively moves logic and compute into memory, culminating in "zHBM" — DRAM stacked directly on the processor [38]. SK hynix showed a 16-layer, 48 GB HBM4 at CES 2026 with Q3 2026 mass production, and continues to demo AiM/AiMX PIM accelerators [39]. **REPORTED** (Aug 2026): Samsung's 4 nm **GAIA** could be the first commercial PIM part, targeted at AI PCs with mass production as early as 2027 [60]; SK hynix showed AiMX (a GDDR6-AiM-based LLM accelerator prototype), CuD and CMM-Ax to hyperscaler customers at CES 2026 [39][61]. Industry estimates put PIM's energy-efficiency advantage at "dozens of times" for memory-bound operations, and the consensus timeline has specialized AI units integrated into the HBM *logic die* around 2027 [60]. The strategic split is notable: Samsung is betting PIM succeeds HBM; SK hynix is betting HBM stays the standard and is hedging with prototypes [62]. (Brief 06 covers the HBM4/HBM4E process and packaging side; this brief covers only the compute-in-memory question.)

**Reconfigurable dataflow / CGRA.** **REPORTED**: SambaNova's fifth-generation SN50 RDU targets models up to 10T parameters and 10M-token context, chaining operations into continuous dataflow to avoid memory round-trips; the SN40L reported 129 tokens/s/user on Llama 3.1 405B [40]. FPGA-style reconfigurability has not "revived" so much as been absorbed — the winning form is coarse-grained and AI-specific, not LUT-level.

**Verdict for 2030:** PIM is the highest-probability entrant (I would put it near-certain in some form, given it ships inside HBM). Wafer-scale is already deployed. CGRA persists as a differentiated niche against a dominant GPU incumbent.

---

## 10. The physics that actually constrains everything

Landauer's bound at 300 K is 2.87×10⁻²¹ J per erased bit. A real 8-bit MAC in leading-edge CMOS costs on the order of 0.1–1 pJ — roughly **10⁷ to 10⁸ times** the thermodynamic floor. So the interesting fact is not that we are near a physical limit; it is that we are nowhere near it, and something else is binding.

That something else is **data movement**. In GPUs the majority of energy is spent moving bits, not multiplying them; designers now budget in picojoules per bit, and as clusters scale to hundreds of thousands of accelerators, interconnect power becomes architecture-defining [41].

This reframes the whole list. Every paradigm above is a bet on one of three propositions:

- **Move data more cheaply** (photonic interconnect, co-packaged optics, wafer-scale, PIM) — where the real money and near-term deployments are.
- **Don't move data at all** (analog in-memory, PIM, memristors, spintronics) — second most likely to matter.
- **Change what a computation costs** (thermodynamic, reversible, neuromorphic, biological) — highest ceiling, longest odds, least evidence.

Analyses of CMOS energy-efficiency limits [42] suggest conventional digital has perhaps 1–2 orders of magnitude of headroom left via voltage scaling, specialization and lower precision — enough to keep GPUs winning through 2030 unless an alternative delivers 10× on a *real* production workload.

---

## What people are underestimating (labeled analysis)

**ANALYSIS — The interconnect/compute split inside photonics is the whole story, and most coverage blurs it.** "Photonic computing company raises $500M" reads as optical-matrix-multiply funding. It almost never is. Ayar Labs, Celestial AI and Lightmatter's Passage line are *networking* companies selling bandwidth per joule per millimetre of package edge — an enormous, near-certain business. Lightmatter delisting Envise while shipping Passage is the clearest confirmation available [4][49]. **Underestimated:** how much of the photonics investment thesis is really a copper-replacement thesis.

**ANALYSIS — Wafer-scale proved the winning post-Moore move is packaging, not physics.** Cerebras invented no new device; it refused to dice the wafer, keeping 44 GB of SRAM one hop from 900,000 cores. Its advantage — token-generation latency GPUs structurally cannot match — comes from deleting off-chip data movement. Samsung's zHBM endpoint is the same insight applied vertically [38]. **Underestimated:** the next decade of gains is likely 3D integration and memory co-location, delivered by memory companies rather than exotic-device startups.

**ANALYSIS — Thermodynamic computing is a bet on the shape of future models, not on hardware.** TSUs sample from energy-based distributions. If the frontier stays autoregressive-transformer-shaped, they are a solution looking for a workload; if diffusion, energy-based or uncertainty-aware inference becomes economically central, they are extremely well-placed. Z1T is literally an attempt to bend transformers into Z1's topology — at a cost of ~10× more FLOPs for equal loss [52], which is the coupling risk made explicit. **Underestimated:** the DoC's $75M LOI [17] suggests at least one institutional buyer thinks the model-shape bet is worth hedging.

**ANALYSIS — The ADC/DAC tax is the analog killer, and it is not going away by itself.** Every analog scheme — optical, memristive, capacitive, thermodynamic — must eventually return digital numbers. Converter energy scales super-linearly with resolution and roughly linearly with sample rate, and it does not benefit from the physics that makes the analog core efficient. EnCharge's capacitor approach and the 2026 electro-optic analog memory work [14] are attacking this correctly by keeping more of the pipeline analog and reducing conversion frequency. **Underestimated:** judge any analog claim by asking where the converters are and how often they fire. Claims that omit converter energy are not comparable to GPU numbers.

**ANALYSIS — Neuromorphic and biological computing are judged against the wrong benchmark in both directions.** Critics dismiss them for losing to GPUs on transformer inference, which was never the claim; boosters cite brain energy efficiency, unachievable through 59 electrodes. The correct frame for neuromorphic is microwatt always-on sensing (Innatera, SynSense [30][31]) and simulation instruments for national labs (SpiNNcloud [56][57]); the correct frame for Cortical Labs is neuroscience instrumentation. **Underestimated:** both fields would be better served by dropping the datacenter framing entirely. Reversible computing is the mirror image — a 1.41× recovery factor is unimpressive as a product but significant as physics, since every prior attempt lost more in the resonator than it saved [22][23].

**ANALYSIS — The most likely 2030 outcome is unexciting and worth saying plainly.** AI datacenters in 2030 will be GPUs and GPU-like ASICs, with optical interconnect between and within racks, HBM with increasing amounts of compute inside it, and wafer-scale systems occupying a meaningful latency-sensitive niche. Analog, thermodynamic, reversible, neuromorphic, and biological compute will collectively be a rounding error in deployed FLOPs. That is not a reason to ignore them — the option value is asymmetric and the physics arguments are sound — but a forecast that has several of them mainstream by 2030 is not supported by anything demonstrated as of September 2026.

---

## Ranked verdict: what is actually inside AI datacenters by 2030

Ranked by my probability that the paradigm is a *material line item* in AI datacenter spend by 2030 — not a pilot, not a press release.

| # | Paradigm | P(material by 2030) | Timeline | Why |
|---|---|---|---|---|
| 1 | **Optical interconnect / co-packaged optics** | ~95% | **Already arriving** | Copper reach is the binding constraint; Marvell/Celestial ~$3.25B, Ayar $3.75B val., NVLink Fusion [8][10] |
| 2 | **Wafer-scale (Cerebras)** | ~90% | **Already deployed** | 600 MW live-or-contracted; $20B+/750 MW OpenAI deal; $209.9M Q2-26 core revenue [47][48] |
| 3 | **Processing-in-memory (HBM-resident)** | ~80% | 2027–2030 | Rides the HBM supply chain; Samsung GAIA, zHBM; SK hynix AiMX [38][60][61] |
| 4 | **Analog in-memory — edge/client** | ~75% | Shipping now | EnCharge EN100 >40 TOPS/W; Mythic $125M; TetraMem 22 nm [24][53][64] |
| 5 | **CGRA / reconfigurable dataflow** | ~50% | Persists as niche | SambaNova SN50; absorbed into AI-specific coarse-grained silicon [40] |
| 6 | **Analog in-memory — datacenter inference** | ~30% | 2028+ | ADC tax scales with array size; no frontier-model demonstration |
| 7 | **Photonic NPU (fixed-weight co-processor)** | ~25% | 2028+ | Q.ANT at LRZ/JSC and IONOS is real but small; no optical nonlinearity [11][12] |
| 8 | **Thermodynamic / probabilistic (TSU)** | ~15% | 2029+, high variance | Z1 is a genuine watt-class die, but 97% of Z1T's per-token energy is the FPGA [52] |
| 9 | **Spintronics / MRAM** | ~15% | As weight memory, not compute | Strongest result is *digital* CIM in MRAM [36] |
| 10 | **Neuromorphic** | ~10% | Sensor edge yes, DC no | BrainChip does ~$1–2M/yr revenue; SpiNNcloud sells to labs [57][58] |
| 11 | **Analog optical compute (general)** | ~5% | 2035+ | Microsoft AOC needs 50–1,000 modules for useful sizes [1] |
| 12 | **Reversible / adiabatic** | ~3% | 2035+ / never for AI | Energy savings bought with clock speed; wrong tradeoff for accelerators |
| 13 | **Superconducting SFQ** | ~2% | Never (for AI) | Cryo overhead + no memory; future is quantum control [43][65] |
| 14 | **DNA storage** | ~1% | Archive niche only | ~10⁸× cost gap; not compute at all [34] |
| 15 | **Biological / organoid** | <1% | Never (as infrastructure) | 59 electrodes, six-month neuron lifespan [32][33] |

The honest shape of this table: **ranks 1–4 are packaging, memory and light — engineering, not new physics.** Ranks 8–15 are the exciting ones, and they are the ones with no megawatts.

---

## Key numbers table

Only measured or company-disclosed figures. Projections are marked.

| Item | Number | Label |
|---|---|---|
| Microsoft AOC hardware | 16 microLEDs / 16 photodetectors; 256 weights per pass, 4,096 time-multiplexed; ~20 ns loop; 99.8% MNIST [1] | CONFIRMED |
| Microsoft AOC efficiency | 500 TOPS/W @ 8-bit vs 4.5 TOPS/W GPU baseline; needs 50–1,000 modules for 0.1–2B weights [1] | SPECULATION (projection) |
| Photonic tensor cores (academic) | 65.5 TOPS at 78 W electrical, 4× 128×128 cores [7] | CONFIRMED |
| Lightmatter optical link | 16λ bidirectional, 800 Gbps single fiber, BER <10⁻⁹; Passage L20 6.4 Tbps [4][5] | REPORTED |
| Photonics funding | Celestial→Marvell ~$3.25B; Ayar $870M raised / $3.75B val.; Lightmatter ~$850M / $4.4B val. [8][10][49][50] | CONFIRMED |
| Extropic Z1 | 269,568 p-bits, 2,135,904 coupling edges, >50 MHz sampling, <12 mm die, <1 W [51][52] | REPORTED (spec) |
| Extropic Z1T per-token energy | 294.52 nJ = 8.74 nJ Z1 + **285.78 nJ FPGA**; ~28× vs H100 all-in, 935× Z1-only; ~10× more FLOPs than GPT-2 for equal loss [52] | SPECULATION (estimated, not measured) |
| Vaire reversible | 1.77× recovery (capacitor array), 1.41× (shift-register/adder), ~50% recycled, 22 nm [22][23] | CONFIRMED |
| EnCharge EN100 | 200+ TOPS at 8.25 W (>40 TOPS/W), M.2 form factor [24] | CONFIRMED (shipping) |
| Mythic / TetraMem | Mythic $125M Dec-2025, >$175M total; TetraMem MLX200 22 nm RRAM SoC, sampling H2-2026 [53][64] | CONFIRMED |
| Intel Hala Point | 1.15B neurons, 1,152 Loihi 2, 6RU; LLM work ~3× energy vs edge GPU [28][29] | CONFIRMED |
| SpiNNcloud | Sandia 150–180M neurons (2025); Leipzig 656,640 cores / ~4,320 chips / ≥650M neurons [56][57] | CONFIRMED / REPORTED |
| BrainChip revenue | US$1.89M FY25 (+374%); US$1.22M H1-26 vs ~US$12M net loss [58] | CONFIRMED |
| Cerebras WSE-3 / CS-4 | 4T transistors, 900k cores, 44 GB SRAM, 46,225 mm²; CS-4 >4,400 tok/s/user on gpt-oss-120B [37] | CONFIRMED / REPORTED |
| Cerebras scale | IPO $185/sh, $5.55B raised; Q2-26 core rev $209.9M (+103% YoY); >600 MW live-or-contracted; OpenAI 750 MW / >$20B [45][47][48] | CONFIRMED / REPORTED |
| Memory PIM | SK hynix 16-hi 48 GB HBM4 (CES-26); Samsung 4 nm GAIA PIM, MP as early as 2027; zHBM roadmap [38][60][61] | REPORTED / roadmap |
| Cortical Labs CL1 | 20 units, ~800k neurons each, 59 electrodes, ~25 W/unit, 6-month lifespan [32][33] | CONFIRMED |
| DNA storage cost | ~$100,000/MB today vs ~$1,000/TB adoption threshold [34] | REPORTED |
| Landauer bound | 2.87×10⁻²¹ J/bit erased @ 300 K; real 8-bit MAC ~0.1–1 pJ = 10⁷–10⁸× the floor [42] | CONFIRMED |

---

## Sources

1. *Nature*, "Analog optical computer for AI inference and combinatorial optimization," 3 Sep 2025 — https://www.nature.com/articles/s41586-025-09430-z
2. PMC full text of [1], accessed Sep 2026 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12422976/
3. Microsoft Research, Future AI Infrastructure / Computing theme, accessed Sep 2026 — https://www.microsoft.com/en-us/research/theme/future-ai-infrastructure/computing/
4. Lightmatter company site (SC25 demonstrations, product lines), accessed Sep 2026 — https://lightmatter.co/
5. Lightmatter press release, "Passage L20 Unified Optical Engine," Mar 2026 — https://lightmatter.co/press-release/lightmatter-expands-photonic-interconnect-roadmap-with-passage-l20-unified-optical-engine-for-npo-and-obo-applications/
6. *Nature*, "Universal photonic artificial intelligence acceleration," 2025 — https://www.nature.com/articles/s41586-025-08854-x
7. *Nature Communications*, "65 TOPS optoelectronic multi-core computing," 2026 — https://www.nature.com/articles/s41467-026-76128-9
8. Converge Digest, "Marvell Bets Big on Optical Scale-Up, Acquires Celestial AI," 2026 — https://convergedigest.com/marvell-bets-big-on-optical-scale-up-acquires-celestial-ai-for-photonic-fabric/
9. BusinessWire, "Celestial AI Secures $250 Million Funding," 10 Mar 2025 — https://www.businesswire.com/news/home/20250310333743/en/Celestial-AI-Secures-$250-Million-Funding-to-Revolutionize-AI-Infrastructure-with-Its-Photonic-Fabric
10. AI2Work, "Ayar Labs Raises $500M," Mar 2026 — https://ai2.work/blog/ayar-labs-raises-500m-to-replace-copper-with-light-in-ai-chips-2026
11. Q.ANT, "Q.ANT Takes Photonic AI Computing Commercial," 20 May 2026 — https://qant.com/news/q-ant-takes-photonic-ai-computing-commercial-as-ais-power-demand-surges/
12. Yole Group, "Q.ANT unveils second-generation photonic processing server," 2026 — https://www.yolegroup.com/industry-news/q-ant-unveils-second-generation-photonic-processing-server-to-power-the-next-wave-of-ai-and-hpc/
13. GlobeNewswire, "Lightelligence Demonstrates its Full Complement of Optical Compute Products at OFC," 5 Mar 2026 — https://www.globenewswire.com/news-release/2026/03/05/3250525/0/en/Lightelligence-Demonstrates-its-Full-Complement-of-Optical-Compute-Products-at-OFC.html
14. *Nature Communications*, "Neuromorphic photonic computing with an electro-optic analog memory," 2026 — https://www.nature.com/articles/s41467-026-69084-x
15. IEEE Spectrum, "Optical Metamaterials Could Boost AI Data Centers," 2026 — https://spectrum.ieee.org/optical-metamaterials-ai-data-centers
16. Extropic, "Inside X0 and XTR-0," accessed Sep 2026 — https://extropic.ai/writing/inside-x0-and-xtr-0
17. Extropic, "$75 Million Letter of Intent with U.S. Department of Commerce," 30 Jul 2026 — https://extropic.ai/writing/thermodynamic-computing-chips-in-america
18. *Quanta Magazine*, "Thermodynamic Computers Go With the (Energy) Flow," 15 Jul 2026 — https://www.quantamagazine.org/thermodynamic-computers-go-with-the-energy-flow-20260715/
19. Normal Computing, "Tape-Out of World's First Thermodynamic Computing Chip," 12 Aug 2025 — https://www.normalcomputing.com/blog/normal-computing-announces-tape-out-of-worlds-first-thermodynamic-computing-chip
20. arXiv:2608.00754, "CN101 — A Digital Thermodynamic Computer for Generative AI," 2026 — https://arxiv.org/pdf/2608.00754
21. Tom's Hardware, "World's first thermodynamic computing chip reaches tape out," 2025 — https://www.tomshardware.com/tech-industry/semiconductors/worlds-first-thermodynamic-computing-chip-reaches-tape-out-normal-computings-physics-based-asic-changes-lanes-to-train-more-ai
22. EE Times, "Vaire Demos Energy Recovery With Reversible Computing Test Chip," 2025 — https://www.eetimes.com/vaire-demos-energy-recovery-with-reversible-computing-test-chip/
23. IEEE Spectrum, "Reversible Computing Escapes the Lab in 2025" — https://spectrum.ieee.org/reversible-computing
24. BusinessWire, "EnCharge AI Announces EN100," 29 May 2025 — https://www.businesswire.com/news/home/20250529108055/en/EnCharge-AI-Announces-EN100-First-of-its-Kind-AI-Accelerator-for-On-Device-Computing
25. IEEE Spectrum, "EnCharge's Analog AI Chip Promises Low-Power and Precision" — https://spectrum.ieee.org/analog-ai-chip-architecture
26. IEEE Spectrum, "Analog AI Startup Aims to Lower the Power of Gen AI" (Sagence) — https://spectrum.ieee.org/analog-ai-2669898661
27. Towards Data Science, "Analog AI Is Back, But Can It Survive Its Own Noise?", 2026 — https://towardsdatascience.com/analog-ai-is-back-can-it-survive-its-own-noise/
28. Intel Newsroom, "Intel Builds World's Largest Neuromorphic System" (Hala Point) — https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system-to-enable-more-sustainable-ai
29. arXiv:2503.18002, "Neuromorphic Principles for Efficient Large Language Models on Intel Loihi 2" — https://arxiv.org/html/2503.18002v2
30. Data Center Dynamics, "Neuromorphic processor startup Innatera raises $21m" — https://www.datacenterdynamics.com/en/news/neuromorphic-processor-startup-innatera-raises-21m/
31. SynSense, "$27.7M to Accelerate Neuromorphic AI Edge Computing," Jul 2025 — https://www.trysignalbase.com/news/funding/synsense-secures-277m-to-accelerate-the-future-of-neuromorphic-ai-edge-computing
32. The Next Web, "A data centre rack running on living neurons is now operating in Singapore," Aug 2026 — https://thenextweb.com/news/singapore-biological-data-centre-cortical-labs-neurons
33. Cortical Labs, CL1 product page, accessed Sep 2026 — https://corticallabs.com/cl1
34. TechRadar Pro, "Twist Bioscience spin-off plans terabyte-scale DNA storage in 2026" — https://www.techradar.com/pro/after-nearly-10-years-twist-bioscience-spin-off-plans-terabyte-scale-dna-storage-in-2026-intending-to-store-13tb-of-data-in-a-single-drop-of-water
35. *Nature Electronics*, "Fault-free analogue computing with imperfect hardware," 2026 — https://www.nature.com/articles/s41928-026-01638-9
36. *Nature Electronics*, "Spintronic digital compute-in-memory macro for efficient artificial intelligence," Oct 2025 — https://www.nature.com/articles/s41928-025-01480-5
37. Cerebras investor relations, "Cerebras Unveils CS-4," 18 Aug 2026 — https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions
38. Tom's Hardware, "Hot Chips 2026: Samsung reveals a three-phase HBM roadmap … zHBM," 2026 — https://www.tomshardware.com/tech-industry/semiconductors/hot-chips-2026-samsung-reveals-a-three-phase-hbm-roadmap-that-puts-logic-and-compute-inside-memory-zhbm-ultimately-stacks-dram-directly-on-top-of-the-processor
39. SK hynix Newsroom, "Next-Generation AI Memory Innovations at CES 2026" — https://news.skhynix.com/en/sk-hynix-showcases-next-generation-ai-memory-innovations-at-ces-2026/
40. SambaNova, RDU product page (SN50), accessed Sep 2026 — https://sambanova.ai/products/rdu-ai-chips
41. *Nature Electronics*, "Co-packaged optics for high-performance computing and artificial intelligence," 2026 — https://www.nature.com/articles/s41928-026-01681-6
42. arXiv:2312.08595, "Limits to the Energy Efficiency of CMOS Microprocessors" — https://arxiv.org/pdf/2312.08595
43. Wikipedia, "Superconducting computing" (SFQ overview and references), accessed Sep 2026 — https://en.wikipedia.org/wiki/Superconducting_computing
44. arXiv:2606.02781, "CRAM-ER: Error-Resilient Spintronic Computational RAM," GLSVLSI 2026 — https://arxiv.org/pdf/2606.02781
45. Quartz, "Cerebras IPO prices at $185, raising $5.55 billion," May 2026 — https://qz.com/cerebras-ipo-pricing-185-dollars-ai-chips-051426
46. CNBC, "AI chipmaker Cerebras files to go public after scrapping IPO plans last year," 17 Apr 2026 — https://www.cnbc.com/2026/04/17/cerebras-new-ipo-ai-chips.html
47. Cerebras investor relations, "Fast Inference Cloud Business Nearly Quadruples in Q2 2026," 12 Aug 2026 — https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-fast-inference-cloud-business-nearly-quadruples
48. Pulse 2.0, "Cerebras: Data Center Capacity Tops 600 MW," 2026 — https://pulse2.com/cerebras-data-center-capacity-tops-600-mw-as-manufacturing-capacity-targets-more-than-10x-expansion/
49. Lightmatter, "Vision" (product/roadmap positioning), accessed Sep 2026 — https://lightmatter.co/vision/
50. EE Times, "Lightmatter Raises $400 Million Series D," Oct 2025 — https://www.eetimes.com/lightmatter-raises-400-million-series-d/
51. Untapped Ventures, "Extropic's Z1 Chip: A Leap in Thermodynamic Computing," 2026 — https://www.untapped.ventures/post/extropic-z1-thermodynamic-computing-autonomous-economy
52. Extropic, "Z1T: Transformer-like models for Z1," Aug 2026 — https://extropic.ai/writing/z1t/
53. SiliconANGLE, "Compute-in-memory chip startup Mythic raises $125M round," 17 Dec 2025 — https://siliconangle.com/2025/12/17/compute-memory-chip-startup-mythic-raises-125m-round/
54. EE Times, "Mythic Rises from the Ashes with $125M Funding Round," 2025 — https://www.eetimes.com/mythic-rises-from-the-ashes-with-125-million-funding-round/
55. NeuromorphicCore, "Rain AI" company profile, accessed Sep 2026 — https://neuromorphiccore.ai/insights/rain-ai/
56. HPCwire, "Sandia Deploys SpiNNaker2 Neuromorphic System from SpiNNcloud," Jun 2025 — https://www.hpcwire.com/off-the-wire/sandia-deploys-spinnaker2-neuromorphic-system-from-spinncloud/
57. Data Center Dynamics, "SpiNNcloud to deploy world's largest neuromorphic supercomputer at Leipzig University," Jul 2025 — https://www.datacenterdynamics.com/en/news/spinncloud-to-deploy-worlds-largest-neuromorphic-supercomputer-at-leipzig-university/
58. Yahoo Finance / Simply Wall St, "Renewed Focus on Akida Ahead of 2026 Earnings — BrainChip (ASX:BRN)," 2026 — https://finance.yahoo.com/news/did-renewed-focus-akida-ahead-031652628.html
59. Edge Infrastructure Review, "BrainChip secures $25M to push neuromorphic AI into real-world edge devices," 15 Dec 2025 — https://www.edgeir.com/brainchip-secures-25m-to-push-neuromorphic-ai-into-real-world-edge-devices-20251215
60. TrendForce, "Samsung's 4nm GAIA Could Mark First PIM Commercialization in AI PCs," 26 Aug 2026 — https://www.trendforce.com/news/2026/08/26/news-samsungs-4nm-gaia-could-mark-first-pim-commercialization-in-ai-pcs-mass-production-as-early-as-2027/
61. TrendForce, "SK hynix Debuts 16-Layer 48GB HBM4 at CES 2026," 6 Jan 2026 — https://www.trendforce.com/news/2026/01/06/news-sk-hynix-debuts-16-layer-48gb-hbm4-at-ces-2026-alongside-socamm2-and-lpddr6/
62. Korea JoongAng Daily, "Samsung bets on PIM as SK hynix advances cooler HBM for AI memory," 2026 — https://www.koreajoongangdaily.com/business/samsung-bets-on-pim-while-sk-hynix-keeps-eye-on-hbm/12846274
63. IBM Research, "An energy-efficient analog chip for AI inference," accessed Sep 2026 — https://research.ibm.com/blog/analog-ai-chip-inference
64. BusinessWire, "TetraMem Announces 22nm Multi-Level RRAM Analog In-Memory Computing SoC Milestone," 16 May 2026 — https://www.businesswire.com/news/home/20260516556464/en/TetraMem-Announces-22nm-Multi-Level-RRAM-Analog-In-Memory-Computing-SoC-Milestone
65. IBM Research, "A Cryo-CMOS Control System for Large-Scale Superconducting Qubit Quantum Computing," APS Global Physics Summit 2026 — https://research.ibm.com/publications/a-cryo-cmos-control-system-for-large-scale-superconducting-qubit-quantum-computing-part-1
66. Research Square, "Cryogenic hardware accelerator for Quantum State Discrimination at 4K," 2025 — https://www.researchsquare.com/article/rs-7661185/v1
