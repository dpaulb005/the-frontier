# Beyond Moore, Beside Quantum: The Non-Quantum Post-Moore Paradigms That Could Matter for AI

*Research report — compiled 2026-09-07. Claims labeled **CONFIRMED** (peer-reviewed or verifiable shipping product), **REPORTED** (credible press/company disclosure, not independently verified), **SPECULATION** (projection, simulation, or roadmap).*

---

## TL;DR

1. **Photonic interconnect has won; photonic compute has not.** Optical I/O is entering AI datacenters now — Marvell paid ~$3.25B for Celestial AI, Ayar Labs raised $500M at a $3.75B valuation, Lightmatter is inside the NVLink Fusion ecosystem [8][10][4]. Optical *matrix multiply* remains a research object with real but small demonstrations (65 TOPS at 78 W; 4,096 effective weights in Microsoft's Nature system) [7][1].
2. **Microsoft's analog optical computer is the most rigorous result in the field and also the clearest illustration of the gap**: 16 microLEDs, 16 photodetectors, 256 weights per pass, ~20 ns loop, 99.8% MNIST — with a *projected* 500 TOPS/W versus a measured GPU baseline of 4.5 TOPS/W. Reaching useful model sizes needs 50–1,000 optical modules [1][2].
3. **Thermodynamic/probabilistic computing (Extropic, Normal Computing) has silicon but no product.** Extropic's X0 is "dozens of probabilistic circuits"; the headline 10,000× number comes from *simulating part of* the unbuilt Z1 on a Fashion-MNIST-class benchmark [16][18]. Extropic signed a $75M LOI with the US Department of Commerce in July 2026 — the strongest external validation so far [17].
4. **Reversible/adiabatic computing crossed a real threshold in 2025**: Vaire's 22 nm "Ice River" test chip is the first commercial-CMOS part to demonstrate *net* energy recovery — 1.77× on a capacitor array, ~50% average recycling [22][23]. That is a physics milestone, not a datacenter product; the clock-rate penalty is the unsolved problem.
5. **Analog in-memory compute is shipping — at the edge, not the rack.** EnCharge's EN100 delivers 200+ TOPS at 8.25 W (>40 TOPS/W) in an M.2 module [24]. IEEE Spectrum's honest framing still applies: analog AI has "mostly delivered modest savings, and only for modest-sized neural networks" [25].
6. **Neuromorphic remains a research and sensor-edge technology.** Hala Point's 1.15B neurons across 1,152 Loihi 2 chips is impressive and 8 years old in lineage; Loihi 2 LLM work reports ~3× energy savings versus edge GPUs — good, not transformative [28][29]. The commercial traction is in microwatt sensors (Innatera Pulsar, SynSense Speck), not AI datacenters.
7. **Wafer-scale is the only "exotic" architecture already in production AI datacenters at scale.** Cerebras IPO'd in May 2026 at ~$26–27B and its CS-4 claims >4,400 tokens/s/user on gpt-oss-120B [37]. It is exotic packaging, not exotic physics — which is exactly why it worked.
8. **Processing-in-memory is the highest-probability near-term paradigm shift**, because it rides the HBM supply chain. Samsung's Hot Chips 2026 roadmap ends in "zHBM" — DRAM stacked directly on the processor [38]. This is the one on this list most likely to be a line item in a 2030 datacenter BOM.
9. **Biological and DNA computing are not AI-compute stories.** Cortical Labs has 20 CL1 units in a Singapore rack with ~800,000 neurons each, 59 electrodes, and a six-month neuron lifespan [32][33]. That is a neuroscience instrument. DNA storage is cold archive, and it is ~$100k/MB today against a ~$1,000/TB adoption threshold [34].
10. **The real driver behind all of it is that interconnect energy, not arithmetic, now dominates.** A Landauer-limit erasure at 300 K costs 2.87×10⁻²¹ J; a real 8-bit MAC costs ~10⁷–10⁸ times that, and most of a GPU's joules go to moving bits, not multiplying them [41][42]. That asymmetry is why optics wins at *moving* data long before it wins at *computing*.

---

## 1. Photonics: the interconnect is real, the compute is a demo

### What has actually been demonstrated

**Microsoft's analog optical computer (AOC)** — published in *Nature*, 3 September 2025 — is the most carefully documented optical AI result to date [1][2]. **CONFIRMED**: the physical hardware is 16 microLEDs and 16 photodetectors with two spatial light modulators (one each for positive and negative matrix entries), supporting a 16-variable state vector and 256 weights per pass; up to 4,096 weights were demonstrated by time-multiplexing 16 independent 256-weight models. It hit 99.8% agreement with expected labels on MNIST, solved a 64-variable MRI-reconstruction QUMO problem and a 41-variable transaction-settlement instance with Barclays, and ran up to three orders of magnitude faster than Gurobi on selected QPLIB instances. Round-trip loop latency is ~20 ns; ML tasks converge in ~9 iterations (~180 ns).

**SPECULATION** (the authors are explicit about this): the 500 TOPS/W at 8-bit figure — roughly 2 fJ/op, versus 4.5 TOPS/W for current GPUs at the same precision, hence "100×" — is a *projection* for a future integrated system, not a measurement of the built machine. The paper itself states that practical applications need 0.1–2 billion weights, requiring **50 to 1,000 optical modules**, and estimates 800 W for a 100-million-weight system across 25 modules. Noise forces up to 11 repeated runs for averaging on regression tasks. This is the honest version of optical computing: elegant physics, four orders of magnitude of engineering left.

**Lightmatter** demonstrated four racks of production hardware at SC25 including M1000 and Passage 50, with a 16-wavelength bidirectional link at 800 Gbps over a single fiber and BER below 10⁻⁹ under thermal stress (**REPORTED**) [4]. In March 2026 it announced Passage L20, a 6.4 Tbps unified optical engine for near-package and on-board optics, sampling late 2026, and joined NVIDIA's NVLink Fusion ecosystem [5]. Its 2025 *Nature* paper demonstrated a photonic processor running ResNet, BERT, and an Atari deep-RL policy at near-electronic accuracy (**CONFIRMED**) [6]. Note the split: the *interconnect* is a product roadmap with customers; the *compute* is a paper.

**Q.ANT** is the most interesting counterexample — a thin-film lithium niobate photonic NPU shipped as a PCIe card in a 19-inch rack server. **CONFIRMED**: units are installed at Germany's Leibniz Supercomputing Centre (LRZ) and Jülich Supercomputing Centre (JSC). **REPORTED**: LRZ's independent evaluation found the second-generation NPU up to 100× faster than gen 1, and Q.ANT's internal benchmarks claim up to 30× energy efficiency and 50× performance per application versus conventional processors; in May 2026 IONOS became the first commercial cloud datacenter to host the Native Processing Server [11][12]. The gen-1-to-gen-2 comparison is the load-bearing caveat: 100× over your own first prototype is not 100× over an H200.

**Lightelligence** showed PACE 2 at OFC 2026 — an optoelectronic accelerator card with >40,000 photonic devices and a fully configurable 128×128 optical matrix, with ONNX/PyTorch/TVM support — and listed on the Hong Kong Stock Exchange on 28 April 2026 (01879.HK), the first pure-play AI silicon photonics listing (**REPORTED**) [13]. Academic work in *Nature Communications* (2026) reports 65.5 TOPS from four 128×128 photonic tensor cores at 78 W electrical (**CONFIRMED**) [7] — real, and roughly two orders of magnitude below a single modern GPU's dense throughput.

**Celestial AI** was acquired by Marvell for ~$3.25B, completed early 2026, after a $250M Series C1 in March 2025 (total >$515M) [8][9]. **Ayar Labs** raised $500M Series E in March 2026 — $870M total, $3.75B valuation — for its TeraPHY chiplet and SuperNova light source, with CEO Mark Wade projecting on-chip optical I/O maturity in 2026–2028 [10].

### Honest skepticism

Analog optical neural networks still need DACs to load inputs and ADCs to read results, and high-speed converters are expensive in power — often enough to erase the optical MAC advantage [14]. There is no mature optical nonlinearity, so hybrid systems bounce between domains, adding latency and joules. Offline-trained weights degrade under thermal and fabrication drift. And as IEEE Spectrum notes, optical processors today are "typically far too bulky to achieve a compute density competitive with the best modern electronic processors" [15] — the wavelength of light is a hard floor on component size that Moore's law does not lower. Recent work co-locating electro-optic analog memory with the compute unit claims >26× power savings versus SRAM-DAC architectures, which is the right attack on the right problem [14], but it is 2026 lab work.

**Verdict for 2030:** Optical interconnect — co-packaged optics, optical scale-up fabric — is a near-certainty in AI datacenters, arguably already there. Optical *compute* as a mainstream training or inference substrate by 2030: unlikely; plausible as a niche co-processor for fixed-weight, latency-critical, or optimization workloads.

---

## 2. Thermodynamic and probabilistic computing

The pitch: generative AI is fundamentally sampling from a distribution. GPUs compute a probability vector and then sample from it — two expensive steps. A thermodynamic sampling unit (TSU) uses the chip's own electrical noise as the sampler, skipping the first step entirely.

**Extropic.** **CONFIRMED**: the X0 prototype exists and runs at room temperature, comprising dozens of probabilistic circuits (p-bits); the XTR-0 development platform shipped from Q3 2025 [16]. **SPECULATION**: the Z1 production part — "over 250,000 interconnected pbits" — is unbuilt, and the widely-quoted 10,000× energy saving comes from *simulating a small part of Z1* running a Denoising Thermodynamic Model on a low-resolution image benchmark, compared against GPUs [16][18]. **REPORTED**: on 30 July 2026 Extropic signed a letter of intent with the US Department of Commerce for up to $75M through the CHIPS R&D Office to scale TSUs and onshore manufacturing [17] — meaningful third-party diligence, though an LOI is not disbursed money.

The skeptical read is worth stating plainly: p-bit and stochastic computing are decades-old ideas; the demonstrated benchmark is a small black-and-white image task, not a multimodal or language workload; and analog device variability, calibration, and verification are exactly the problems that have historically killed analog accelerators. Critics have characterized XTR-0 as stochastic computing in thermodynamic packaging. The counter is that Extropic's device physics (shaping thermal fluctuations directly, rather than building a digital RNG) is genuinely different, and CMOS-compatible at room temperature — which was the historical blocker.

**Normal Computing** took a more conservative path. **CONFIRMED**: CN101, announced taped out on 12 August 2025, is a *digital* thermodynamic computing chip on standard CMOS using stochastic-computing and metastability principles, targeting linear algebra, matrix operations, and stochastic sampling [19][20][21]. **REPORTED**: up to 1000× energy efficiency on targeted AI and scientific workloads. **SPECULATION**: roadmap of CN201 in 2026 for high-resolution diffusion models and CN301 in late 2027. Doing it in standard CMOS is the strategically smart move — it means fab access and yield are not the risk.

*Quanta* covered the field in July 2026, a reasonable marker that it has moved from fringe to legitimately-watched [18].

**Verdict for 2030:** SPECULATION either way. This is the highest-variance category on the list: if diffusion/energy-based generative models remain economically central and TSUs scale, the payoff is enormous; if the industry's compute demand stays autoregressive-transformer-shaped, TSUs address the wrong workload. A demonstrated 10× on a real production model would change my assessment more than any funding round.

---

## 3. Reversible and adiabatic computing

Landauer's principle says erasing a bit must dissipate at least *kT* ln 2 — 2.87×10⁻²¹ J at 300 K. Reversible computing avoids erasure and recycles the energy in the switching capacitance rather than dumping it to heat.

**CONFIRMED**: In March 2025, **Vaire Computing** taped out "Ice River" in a commercial 22 nm planar CMOS process — the first chip to achieve *net* energy recovery in a commercial process, with a measured energy-recovery factor of 1.77× for a capacitor array and 1.41× for a shift-register/adder relative to square-wave-driven equivalents, and an on-chip resonator recycling ~50% of energy on average [22][23]. IEEE Spectrum's framing — "reversible computing escapes the lab" — is fair.

The honest caveats: adiabatic switching energy scales roughly with 1/(switching time), so energy savings are bought with clock speed. At the frequencies AI accelerators run, adiabatic circuits lose. The resonator infrastructure costs area. And 1.41× on a shift register is a very long way from a competitive datacenter part. Vaire's own framing ("near-zero energy chips") outruns its data by a wide margin.

**Verdict for 2030:** Not in AI datacenters. Plausible in ultra-low-power edge or in specific always-on blocks. Worth tracking as the only line of work attacking the thermodynamic floor directly rather than the constant factors above it.

---

## 4. Analog in-memory computing

Multiply-accumulate performed physically in a memory array — by charge, resistance, or magnetization — eliminating the weight-fetch that dominates AI energy.

**EnCharge AI** is the furthest along commercially. **CONFIRMED**: EN100 launched May 2025 in two forms — an M.2 module delivering 200+ TOPS at 8.25 W, and a four-NPU PCIe card at roughly 1 petaops — built on capacitor-based (not resistive) analog compute-in-memory, achieving >40 TOPS/W and ~20× better performance-per-watt than competing solutions [24][25]. The capacitor choice matters: capacitance is set by geometry, which fabs control precisely, sidestepping the device-variability problem that has plagued resistive analog memory for fifteen years.

**IBM** has the deepest research bench: the HERMES phase-change-memory analog chip has shown near-software accuracy on real workloads, and an earlier PCM prototype held 17M parameters across 35M PCM cells [27]. **NorthPole** — 25× more power-efficient than 12 nm GPUs — remains a research chip with no announced commercial release [27].

**Mythic** raised $125M in late 2025 (**REPORTED**) after years of struggle. **Sagence** claims Llama 2-70B at one-tenth the power of an H100 system, one-twentieth the cost and space (**REPORTED**, unverified) [26]. **Rain AI** has pivoted repeatedly and has not shipped a datacenter part.

**Memristors/RRAM**: 2026 *Nature Electronics* work on "fault-free analogue computing with imperfect hardware" [35] and 5-bit-controllable oxide RRAM crossbars represent genuine progress on the precision problem, but commercialization "faces substantial hurdles, necessitating a paradigm shift from traditional transistor dominance." **Spintronics**: a *Nature Electronics* paper (October 2025) demonstrated a lossless, fully parallel STT-MRAM digital compute-in-memory macro [36], and CRAM-ER at GLSVLSI 2026 extended spintronic CRAM to multi-bit DNN workloads. MRAM's advantage — non-volatility and near-zero leakage — makes it a strong weight-storage candidate; note that the strongest recent result is *digital* CIM in MRAM, not analog, which is telling.

**Honest skepticism**: IEEE Spectrum's summary is the one to keep — analog AI has historically "delivered modest savings, and only for modest-sized neural networks" [25]. Analog wins at low precision and small models; frontier training needs high dynamic range, and the ADC tax scales with array size. Every analog generation has also been outrun by the next digital node.

**Verdict for 2030:** Edge and client devices, yes — already happening. Datacenter inference for smaller models: possible, ~30%. Training: no.

---

## 5. Neuromorphic computing

**CONFIRMED**: Intel's Hala Point packs 1.15 billion neurons across 1,152 Loihi 2 processors on Intel 4, in a six-rack-unit chassis [28]. Published ICASSP results show orders-of-magnitude gains on small-scale edge workloads. **CONFIRMED** (2025–26 research): neuromorphic principles applied to LLMs on Loihi 2 report up to ~3× less energy than transformer LLMs on an edge GPU, with better scaling [29] — real, but a 3× on an edge comparison is not a datacenter argument.

Commercial traction is at the sensor edge. **Innatera** raised $21M in an extended Series A (from a $16M round that was oversubscribed) and launched Pulsar, positioned as the first mass-market neuromorphic microcontroller, plus the Synfire ecosystem effort [30]. **SynSense** raised $27.7M in July 2025 to scale its Speck vision SoC and DYNAP-CNN2, having merged with iniVation [31].

The structural problem: spiking networks excel at sparse, event-driven, temporally-structured data; dense transformer matmuls are the opposite. Neuromorphic hardware also lacks a training story competitive with backpropagation at scale. Eight years after Loihi 1, there is still no neuromorphic datacenter workload with a compelling TCO case.

**Verdict for 2030:** In AI *datacenters*, no. In always-on sensors, wearables, robotics, and satellites, yes — a real and growing market that is simply not the AI-compute market.

---

## 6. Superconducting and cryogenic logic

Single-flux-quantum (SFQ) logic encodes bits as magnetic flux quanta, switches with Josephson junctions, and can clock above 100 GHz with extraordinarily low switching energy [43]. NIST and university groups have demonstrated SFQ qubit control chips in multi-chip modules, and IEEE work continues on large-scale cryogenic integration.

The blockers are unchanged and severe: cryogenic overhead at 4 K costs roughly 10²–10³ W of room-temperature power per watt removed; superconducting memory density is dismal, so you either keep DRAM warm (and pay enormous I/O energy across the thermal boundary) or you have almost no memory; and there is no fab ecosystem at anything like CMOS scale. Searches for 2026 SFQ-for-AI-datacenter programs return no credible industrial roadmap.

**Verdict for 2030:** No. Its future is as classical control logic *for quantum computers*, not as an AI substrate.

---

## 7. DNA data storage

**REPORTED**: Atlas Data Storage, spun out of Twist Bioscience in 2025, targets terabyte-scale DNA storage in 2026 with a stated ambition of 13 TB in a single drop of water [34]. Twist's long-term roadmap — a 150 nm synthesis chip — projects ~$100/TB.

**Honest skepticism**: current pricing is around **$100,000 per megabyte**, i.e. ~10¹¹ $/TB, against a survey threshold where 78% of enterprise storage buyers would adopt (below $1,000/TB). That is eight orders of magnitude of cost reduction required. Read/write latency is hours-to-days. And the density claims deserve arithmetic: at tape-comparable volumetric assumptions a 0.05 cm³ drop holds gigabytes, not terabytes — the 13 TB figure assumes near-theoretical molecular packing.

**Verdict for 2030:** Not an AI-compute technology at all. A plausible cold-archive niche for regulatory/genomic data late in the decade, at best.

---

## 8. Biological computing

**CONFIRMED**: On 6 August 2026, Cortical Labs, NUS Medicine, and datacenter operator DayOne switched on a prototype rack of 20 CL1 units in Singapore — the first "biological datacenter" [32]. Each CL1 holds ~800,000 lab-grown human neurons on a multielectrode array with 59 input channels, draws ~25 W (800–1,000 W per rack), and keeps neurons alive up to six months via onboard life support [33]. A ~120-unit Melbourne facility is planned (**REPORTED**). Switzerland's **FinalSpark** runs a remote platform of 16 brain organoids and claims ~10⁶× lower energy than digital chips (**REPORTED**, and effectively unfalsifiable given no comparable workload).

**Honest skepticism**: 59 electrodes is the entire I/O bandwidth to 800,000 neurons — roughly the interface of a 1970s minicomputer. Neurons die in six months. There is no programming model, no training algorithm competitive with SGD, no reproducibility across biological samples, and no benchmark on any task a GPU is used for. This is a superb neuroscience instrument and a genuinely novel research platform. It is not computing infrastructure.

**Verdict for 2030:** No AI-datacenter role. Watch it as neuroscience, and for what it teaches about learning rules.

---

## 9. Wafer-scale, processing-in-memory, and reconfigurable dataflow — the boring winners

These three share a property the exotic paradigms lack: they are made of transistors, in existing fabs, with existing supply chains.

**Wafer-scale (Cerebras).** **CONFIRMED**: WSE-3 is 4 trillion transistors, 900,000 cores, 44 GB on-wafer SRAM, 46,225 mm². **REPORTED**: WSE-3 Turbo doubles compute to 250 PFLOPS per wafer at the same silicon; the CS-4, announced 18 August 2026, ties three wafers in parallel and delivers >4,400 tokens/s/user on gpt-oss-120B, claimed up to 30× faster than GPU solutions; Cerebras runs OpenAI's GPT-5.6 Sol at up to 750 tokens/s; the company IPO'd in May 2026 at roughly $26–27B [37]. The lesson: the winning "post-Moore" move so far was not new physics but refusing to cut the wafer — eliminating off-package data movement, which is where the joules were.

**Processing-in-memory.** **REPORTED**: at Hot Chips 2026 Samsung laid out a three-phase HBM roadmap that progressively moves logic and compute into memory, culminating in "zHBM" — DRAM stacked directly on the processor [38]. SK hynix showed a 16-layer, 48 GB HBM4 at CES 2026 with Q3 2026 mass production, and continues to demo AiM/AiMX PIM accelerators [39]. Industry estimates put PIM's energy-efficiency advantage at "dozens of times" for memory-bound operations. The strategic split is notable: Samsung is betting PIM succeeds HBM; SK hynix is betting HBM stays the standard.

**Reconfigurable dataflow / CGRA.** **REPORTED**: SambaNova's SN50 RDU — a coarse-grained reconfigurable architecture, fifth generation — targets models up to 10T parameters and 10M-token context, chaining operations into continuous dataflow to avoid repeated memory round-trips; the SN40L combined on-chip SRAM, HBM, and DDR in a three-tier hierarchy and reported 129 tokens/s/user on Llama 3.1 405B [40]. FPGA-style reconfigurability has not "revived" so much as been absorbed: the winning form is coarse-grained and AI-specific, not LUT-level.

**Verdict for 2030:** PIM is the highest-probability entrant (I would put it near-certain in some form, given it ships inside HBM). Wafer-scale is already deployed. CGRA persists as a differentiated niche against a dominant GPU incumbent.

---

## 10. The physics that actually constrains everything

Landauer's bound at 300 K is 2.87×10⁻²¹ J per erased bit. A real 8-bit MAC in leading-edge CMOS costs on the order of 0.1–1 pJ — roughly **10⁷ to 10⁸ times** the thermodynamic floor. So the interesting fact is not that we are near a physical limit; it is that we are nowhere near it, and something else is binding.

That something else is **data movement**. In GPUs the majority of energy is spent moving bits, not multiplying them [41]. Designers now budget in picojoules per bit (identical to milliwatts per Gb/s), and as clusters scale from tens of thousands to hundreds of thousands of accelerators, interconnect power becomes disproportionately architecture-defining [41]. A *Nature Electronics* 2026 review of co-packaged optics for HPC and AI makes the same argument from the optics side [41].

This reframes the whole list. Every paradigm above is really a bet on one of three propositions:

- **Move data more cheaply** (photonic interconnect, co-packaged optics, wafer-scale, PIM). This is where the real money and near-term deployments are.
- **Don't move data at all** (analog in-memory, PIM, memristors, spintronics). Second most likely to matter.
- **Change what a computation costs** (thermodynamic, reversible, neuromorphic, biological). Highest ceiling, longest odds, least evidence.

Analyses of CMOS energy-efficiency limits [42] suggest conventional digital has perhaps 1–2 orders of magnitude of headroom left through voltage scaling, specialization, and lower precision — which is enough to keep GPUs winning through 2030 unless an alternative delivers 10× on a *real* production workload, not a benchmark.

---

## What people are underestimating (labeled analysis)

**ANALYSIS — The interconnect/compute split inside photonics is the whole story, and most coverage blurs it.** "Photonic computing company raises $500M" reads as optical matrix multiplication funding. It almost never is. Ayar Labs, Celestial AI, and Lightmatter's Passage line are *networking* companies whose product is bandwidth per joule per millimeter of package edge. That business is enormous and near-certain. Optical compute is a different, much harder, much smaller business — and Lightmatter's own product emphasis has drifted toward Passage while Envise stays a research narrative [4][5]. **Underestimated:** how much of the photonics investment thesis is really a copper-replacement thesis.

**ANALYSIS — Wafer-scale proved the winning post-Moore move is packaging, not physics.** Cerebras did not invent a new device. It refused to dice the wafer, keeping 44 GB of SRAM one hop from 900,000 cores. The resulting advantage — token-generation latency that GPUs structurally cannot match — comes from deleting off-chip data movement. Samsung's zHBM endpoint is the same insight applied vertically [38]. **Underestimated:** the next decade of gains is likely 3D integration and memory co-location, and it will be delivered by memory companies, not by exotic-device startups.

**ANALYSIS — Thermodynamic computing is a bet on the shape of future models, not on hardware.** TSUs sample from energy-based distributions. If the frontier stays autoregressive transformers, TSUs are a solution looking for a workload. If diffusion, energy-based models, or Bayesian/uncertainty-aware inference become economically central, TSUs are extremely well-placed. Extropic's own examples are all denoising/generative-image shaped. **Underestimated:** the algorithm-hardware coupling risk cuts both ways, and the DoC's $75M LOI [17] suggests at least one serious institutional buyer thinks the model-shape bet is worth hedging.

**ANALYSIS — The ADC/DAC tax is the analog killer, and it is not going away by itself.** Every analog scheme — optical, memristive, capacitive, thermodynamic — must eventually return digital numbers. Converter energy scales super-linearly with resolution and roughly linearly with sample rate, and it does not benefit from the physics that makes the analog core efficient. EnCharge's capacitor approach and the 2026 electro-optic analog memory work [14] are attacking this correctly by keeping more of the pipeline analog and reducing conversion frequency. **Underestimated:** judge any analog claim by asking where the converters are and how often they fire. Claims that omit converter energy are not comparable to GPU numbers.

**ANALYSIS — Neuromorphic and biological computing are being evaluated against the wrong benchmark, in both directions.** Critics dismiss them for losing to GPUs on transformer inference, which was never the claim. Boosters cite brain energy efficiency, which is not achievable through 59 electrodes. The correct frame for neuromorphic is microwatt always-on sensing, where Innatera and SynSense are winning real sockets [30][31]; the correct frame for Cortical Labs is neuroscience instrumentation. **Underestimated:** both fields would be better served by dropping the datacenter framing entirely.

**ANALYSIS — Reversible computing's milestone is more important than its numbers.** A 1.41× recovery factor on a shift register is unimpressive as a product and significant as physics: it is the first *net* energy recovery in a commercial CMOS process [22][23]. Every prior demonstration lost more in the resonator than it saved. That threshold crossing is what makes the research program legitimate. **Underestimated:** the frequency-energy tradeoff means this technology's natural home is where clock speed does not matter — which is a real and growing category (always-on, battery, space) but not AI.

**ANALYSIS — The most likely 2030 outcome is unexciting and worth saying plainly.** AI datacenters in 2030 will be GPUs and GPU-like ASICs, with optical interconnect between and within racks, HBM with increasing amounts of compute inside it, and wafer-scale systems occupying a meaningful latency-sensitive niche. Analog, thermodynamic, reversible, neuromorphic, and biological compute will collectively be a rounding error in deployed FLOPs. That is not a reason to ignore them — the option value is asymmetric and the physics arguments are sound — but a forecast that has several of them mainstream by 2030 is not supported by anything demonstrated as of September 2026.

---

## Key numbers table

| Paradigm | Leading org | Best demonstrated number | Status label | Funding / scale | In AI datacenters by 2030? |
|---|---|---|---|---|---|
| Analog optical compute | Microsoft AOC | 256 weights/pass, 4,096 time-multiplexed; ~20 ns loop; 99.8% MNIST [1] | CONFIRMED (hardware) / SPECULATION (500 TOPS/W) | Microsoft Research | Unlikely (niche possible) |
| Photonic interconnect | Ayar Labs, Marvell/Celestial, Lightmatter | 800 Gbps/fiber, 16λ bidirectional, BER <10⁻⁹; Passage L20 6.4 Tbps [4][5] | REPORTED / shipping | Ayar $870M total, $3.75B val; Celestial acquired ~$3.25B [8][10] | **Yes — already arriving** |
| Photonic NPU (TFLN) | Q.ANT | Deployed at LRZ + JSC; 100× vs own gen-1; claimed 30× energy eff. [11][12] | CONFIRMED (deployment) / REPORTED (perf) | IONOS cloud partnership, May 2026 | Niche, ~25% |
| Photonic tensor core (academic) | Various | 65.5 TOPS @ 78 W, 4× 128×128 cores [7] | CONFIRMED | Academic | Research |
| Thermodynamic sampling | Extropic | X0: dozens of p-bits, room temp; 10,000× from Z1 *simulation* [16] | CONFIRMED (X0) / SPECULATION (10,000×) | $75M DoC LOI, Jul 2026 [17] | ~15%, high variance |
| Digital thermodynamic | Normal Computing | CN101 taped out Aug 2025, standard CMOS; ~1000× claimed [19][21] | REPORTED | CN201 2026, CN301 2027 | ~20% |
| Reversible/adiabatic | Vaire | 1.77× capacitor array, 1.41× adder, ~50% recycling, 22 nm [22][23] | CONFIRMED | Seed/Series A scale | No |
| Analog in-memory (edge) | EnCharge | 200+ TOPS @ 8.25 W; >40 TOPS/W; ~20× perf/W [24] | CONFIRMED (shipping) | Launched May 2025 | Edge yes; DC ~30% |
| Analog in-memory (PCM) | IBM HERMES | 35M PCM cells / 17M params; near-software accuracy [27] | CONFIRMED (research) | IBM Research | Research |
| Neuromorphic (scale) | Intel Hala Point | 1.15B neurons, 1,152 Loihi 2, 6RU [28] | CONFIRMED | Intel Labs | No |
| Neuromorphic (edge) | Innatera, SynSense | Pulsar MCU; Speck vision SoC [30][31] | CONFIRMED (shipping) | Innatera $21M; SynSense $27.7M | Sensor edge yes |
| Superconducting SFQ | NIST / academia | >100 GHz potential; qubit control demos [43] | CONFIRMED (lab) | Government/academic | No |
| DNA storage | Atlas Data Storage | Target TB-scale 2026; ~$100k/MB today [34] | REPORTED / SPECULATION | Twist spin-out | No (archive niche) |
| Biological | Cortical Labs CL1 | 20 units, ~800k neurons each, 59 electrodes, 25 W, 6-mo life [32][33] | CONFIRMED | Singapore rack Aug 2026 | No |
| Memristor / RRAM | Academic + IBM | 5-bit conductance control; fault-tolerant analog compute [35] | CONFIRMED (lab) | Academic | Research |
| Spintronics / MRAM CIM | Nature Elec. 2025 | Lossless parallel STT-MRAM digital CIM macro [36] | CONFIRMED (lab) | Academic + Qualcomm patents | ~15% (as weight memory) |
| Wafer-scale | Cerebras | 4T transistors, 900k cores, 44 GB SRAM; >4,400 tok/s/user [37] | CONFIRMED (shipping) | IPO May 2026, ~$26–27B | **Yes — already deployed** |
| Processing-in-memory | Samsung, SK hynix | HBM4 16-hi 48 GB, Q3 2026 MP; zHBM roadmap [38][39] | REPORTED / roadmap | Memory-industry capex | **Yes, high probability** |
| CGRA / dataflow | SambaNova | SN50: 10T params, 10M context; 129 tok/s Llama 405B [40] | REPORTED | Private | Niche, persists |
| Physics floor | — | Landauer 2.87×10⁻²¹ J/bit @300K; real MAC ~10⁷–10⁸× that [42] | CONFIRMED | — | — |

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
