# Electrical & Electronic Engineering Frontiers in Semiconductors — 2026 Status Report

*Compiled 2026-09-07. Every substantive claim is labeled **CONFIRMED** (company primary source or peer-reviewed/conference paper), **REPORTED** (credible trade press, often supply-chain sourced and single-threaded), or **SPECULATION** (analysis or my own inference). Where the trade press and the vendor disagree, I say so.*

---

## TL;DR

1. **2nm is genuinely in production at three companies.** TSMC N2 entered volume production Q4 2025; Intel 18A is in HVM at Fab 52 (Arizona) with Panther Lake at retail from January 2026; Samsung SF2 is producing Exynos 2600, with the SF2P refresh reportedly crossing ~70% yield in January 2026 [1][6][13][47]. Leading-edge is a three-horse race for the first time since roughly 2017.
2. **The roadmap slipped and got longer.** At its 2026 North America Technology Symposium TSMC extended public visibility to 2029 — N2U (2028), A14 (2028), A12 and A13 (2029) — and A16 moved out toward 2027 in trade reporting [1][2]. The angstrom era is being paced by backside power and EUV cost, not by transistor physics.
3. **Backside power delivery is the real 2026-27 inflection.** Intel shipped PowerVia in an 18A product first; TSMC's answer, Super Power Rail (SPR), is a direct backside *contact to source/drain* — harder than a backside PDN, and worth ~8-10% speed or 15-20% power over N2P [4].
4. **High-NA EUV crossed into manufacturing — but not at TSMC.** Roughly 10 EXE-class systems are live at four customers, with Intel running High-NA layers in 18A Panther Lake production. TSMC is explicitly skipping High-NA through A16 and committing from A14 [10][12].
5. **CFET is lab-real and product-far.** TSMC showed a functional 101-stage monolithic CFET ring oscillator and a record 6T SRAM bitcell at IEDM 2025; imec cut bottom-pFET access resistance from 1753 to 378 Ω·µm at VLSI 2026 [16][18]. The nodes these map to are A7/A5/A3 — the 2030s.
6. **Packaging, not lithography, is the binding constraint on AI silicon.** TSMC CoWoS heads to ~120-140k wafers/month by end-2026 with 50-60k more at OSATs; 14-reticle CoWoS (~10 compute dies + 20 HBM stacks) is a 2028 target; hybrid-bond pitch is at ~6 µm in HVM [1][19][20].
7. **HBM4 is the 2026 memory war and HBM4E is already being spec'd around it.** 2048-bit interface, 1.5-2 TB/s per stack, up to 64 GB; HBM4E pushes 14-16 Gbps and 3.6-4 TB/s per stack with no unified JEDEC spec yet [21][22].
8. **Co-packaged optics is shipping, not demoing.** Broadcom Tomahawk 6-Davisson and NVIDIA Spectrum-X Photonics are in volume; both lean on TSMC COUPE optical engines. Optical-engine yield is the stated bottleneck [23][24].
9. **Agentic EDA became a product category in 2026.** Synopsys AgentEngineer, Cadence AuraStack, Siemens Fuse — all on NVIDIA's Nemotron/Agent Toolkit stack, with vendor-claimed 50x faster time-to-validated-RTL [37][38][39].
10. **China is scaling *around* EUV, not through it.** SMIC N+3 (5nm-class, DUV multipatterning) fabs Huawei's Ascend 950PR; Huawei announced its own HBM (HiZQ); CXMT targets HBM3E in 2026. Domestic immersion DUV entered limited production but remains multiple generations behind ASML [32][33][34].

---

## 1. Process nodes: what's actually in a fab right now

**TSMC.** N2 entered volume production in Q4 2025 and TSMC describes the strongest customer adoption in its history — 20+ tape-outs received against 70+ in the pipeline (**CONFIRMED**, company statements) [1]. Capacity is the interesting number: reporting puts combined Fab 20 (Hsinchu) + Fab 22 (Kaohsiung) N2 output near 90-100k wafers/month by early-to-mid 2026, targeting ~140k/month by year end, sold out through the year, at roughly $30k/wafer (**REPORTED**, supply-chain sourced and inconsistent across outlets — treat 140k as the optimistic end) [49]. Arizona does not have 2nm yet; Fab 21 phase 3 is a 2028-29 story (**REPORTED**).

The 2026 symposium roadmap is the most consequential public artifact of the year (**CONFIRMED** via TSMC's own release) [1]:
- **N2U** (2028): +3-4% speed or -8-10% power, 1.02-1.03x density over N2P.
- **A16** with Super Power Rail: 8-10% speed at iso-voltage, 15-20% power at iso-frequency, 1.07-1.10x density vs N2P [4]. TSMC's original guidance was H2 2026 production; trade coverage of the 2026 symposium places it in 2027 (**REPORTED**, and the single most important schedule question in the industry).
- **A14** (2028) with NanoFlex Pro, and the High-NA entry point [5][12].
- **A12** (2029), an A14 platform enhancement adding Super Power Rail; **A13** (2029), 6% area saving over A14 with backward-compatible design rules [1].

Note what the A13 number implies (**SPECULATION**): 6% area per node is not Moore's Law, it is amortization. TSMC is now selling design-rule *compatibility* as the headline feature, which tells you the customer pain is porting cost, not density.

**Intel.** 18A is in high-volume manufacturing at Fab 52; Panther Lake (Core Ultra Series 3) launched with broad availability January 2026, and Clearwater Forest / Xeon 6+ is guided to H1 2026 (**CONFIRMED**) [6][9]. 18A combines RibbonFET GAA with PowerVia backside power — Intel got backside power into a shipping product ahead of TSMC, which is the one unambiguous Intel process win of the decade. 14A is the existential node: Intel has **two prospective external customers evaluating test chips**, PDK 0.5 shipped in Q1 2026, and Intel says firm commitments should land in H2 2026 into H1 2027, with Ohio capex gated on them (**CONFIRMED** via earnings-call statements; **zero committed external 14A customers as of mid-2026**) [8]. Everything about Intel Foundry's 2027-2030 rests on that.

**Samsung.** SF2 is in mass production (Exynos 2600). Yield reporting is messy: roughly 40% on early SF2, 50-60% by late 2025, ~70% on the refined SF2P by January 2026 (**REPORTED**, not company-confirmed, and yield figures from Korean press have historically been unreliable in both directions) [13][47]. More telling is the strategic retreat: Samsung reportedly deprioritized SF1.4 to 2028-29 and is pouring resources into 2nm/4nm maturity instead (**REPORTED**) [13]. Samsung has taken delivery of at least two High-NA EXE:5200B units for its 2nm-class lines [12].

**Rapidus.** The most under-covered story. The IIM-1 pilot line in Chitose has been running since April 2025; 2nm GAA transistors on 300mm are hitting planned electrical characteristics; a pre-release 2nm PDK reached early customers in Q1 2026; NEDO approved the FY2026 budget covering both 2nm integration and a *chiplet/package* program (**CONFIRMED** via Rapidus/NEDO) [14]. No published yield, no signed volume customer among 60+ in discussion, mass production targeted 2027 (**REPORTED**) [15]. Rapidus' differentiator is not the node — it is single-wafer processing and short-TAT manufacturing, a genuinely different economic bet (**CONFIRMED** as strategy, **SPECULATION** as to whether it works).

---

## 2. Transistors: GAA now, CFET later, 2D materials sooner than expected

Nanosheet GAA is the shipping architecture at all three leading foundries. The next architectural step, CFET (nFET stacked directly on pFET), moved decisively from simulation to silicon in the last 18 months:

- **TSMC, IEDM 2025 (CONFIRMED):** first fully functional 101-stage monolithic CFET ring oscillator, plus the smallest reported 6T SRAM bitcell, with gate pitch pushed below 48 nm on a nanosheet-based monolithic CFET flow [18].
- **imec, IEDM 2024-2025 and VLSI 2026 (CONFIRMED):** functional monolithic CFETs with direct backside contact to the bottom pMOS source/drain; a revised backside contact module giving ~5x bottom-pFET drive current with access resistance falling from 1753 to 378 Ω·µm; an embedded MDI module allowing different channel orientations for the top nFET and bottom pFET [16][17].
- Intel's position (via Mauro Kobrinsky) is that backside power is the *most area-efficient* connectivity scheme for CFETs — i.e., BSPDN is not merely a power trick, it is a prerequisite for stacked devices [17].

DTCO studies target CFET at A7/A5/A3 nodes [16]. **SPECULATION:** first CFET in a shipping product lands 2031±2, and it will arrive with backside signal routing, not just backside power — the "flip FET"/dual-sided-signal work now appearing in the literature is the tell.

**2D materials moved faster than anyone's 2023 roadmap.** At VLSI 2026, imec + ASML + TSMC presented a 300mm integration route for complementary 2D FETs: MoS2 nFETs and WS2/WSe2 pFETs at **50 nm contacted poly pitch**, channel lengths down to 28 nm with a *single* EUV exposure, 94% of devices switching correctly, on/off ratio >10^5 (**CONFIRMED**, conference paper) [27][28]. That is the first time complementary 2D devices have been demonstrated at industry-relevant dimensions on industry-standard equipment. Carbon nanotube logic, by contrast, produced no comparable 2026 milestone — the CNT-vs-TMD race is effectively over for mainstream logic (**SPECULATION**).

---

## 3. Advanced packaging: where the money and the constraint both are

TSMC's CoWoS is the physical chokepoint on AI accelerator supply. Consensus supply-chain numbers: TSMC monthly CoWoS capacity rising from ~70k wafers (2025) to **120-140k by end-2026**, plus 50-60k at ASE/SPIL and Amkor, approaching ~200k/month industry-wide (**REPORTED**) [20]. TSMC's own roadmap targets **14-reticle CoWoS in 2028**, integrating ~10 large compute dies and 20 HBM stacks, with expansion beyond 14 reticles in 2029 (**CONFIRMED**) [1].

Hybrid bonding is the second axis. TSMC SoIC has moved from ~9 µm bond pitch in earlier volume to **~6 µm in HVM as of mid-2026**, with A14-on-A14 SoIC in 2029 promising 1.8x the die-to-die I/O density of N2-on-N2 (**CONFIRMED** for the roadmap claim; **REPORTED** for the current 6 µm figure) [1][19]. NVIDIA's Rubin generation combines CoWoS-L with SoIC — bridge-based lateral integration plus true 3D vertical stacking in one package (**REPORTED**).

Panel-level packaging (TSMC's CoPoS) and glass substrates remain 2027+ propositions: rectangular panels give better area utilization and glass reduces warpage, but panel toolsets do not yet match wafer-level placement precision (**REPORTED**) [20]. Intel's EMIB-T is reported to have yield problems (**REPORTED**, single-source) [20].

**Chiplets/UCIe:** the standard is mature and broadly adopted inside vertically integrated designs (AMD, Intel, NVIDIA, hyperscaler ASICs). What still does not exist in 2026 is a genuine *merchant* chiplet market — you cannot buy a third-party UCIe die off a catalogue and drop it into your package with predictable KGD, test, and thermal contracts (**SPECULATION**, but well-supported by the absence of any such transaction being publicized).

**Wafer-scale:** Cerebras remains the only shipping wafer-scale vendor. WSE-3 Turbo (46,225 mm², 4T transistors, ~900k cores, TSMC N5) roughly doubles WSE-3 frequency and performance on the same node; at Hot Chips 2026 Cerebras laid out the Nexus rack-scale architecture and stated that the CS-6-generation wafer will incorporate **stacked DRAM** — wafer-scale plus 3D memory integration (**CONFIRMED** via conference presentation) [40]. That is the single most interesting packaging claim of 2026: it implies hybrid bonding at wafer scale.

---

## 4. Memory: HBM4 now, 3D DRAM next decade

**HBM4 (CONFIRMED specs, REPORTED schedules):** 2048-bit interface (double HBM3E), 1.5-2 TB/s per stack, up to 64 GB, 16-Hi stacks. SK hynix declared HBM4 development complete with ~40% better power efficiency at 10 Gbps; Samsung and SK hynix both pulled schedules forward toward Q1 2026; Micron is sampling at up to 11 Gbps and targeting ~15k wafers/month of HBM4 by end-2026 [21]. Market share entering 2026: SK hynix ~62%, with Micron having passed Samsung (**REPORTED**).

**HBM4E:** 14-16 Gbps pin speed, 3.6-4.0 TB/s per stack. **There is no unified JEDEC HBM4E standard** — vendor specs diverge, which is itself the story: the base die is becoming a custom logic die fabbed on a foundry logic node, so HBM is drifting from a commodity toward a semi-custom product co-designed with the accelerator [22]. **SPECULATION:** this is how memory vendors claw back margin, and it structurally advantages whoever has foundry logic partnerships (SK hynix–TSMC) over whoever tries to do it in-house.

**3D DRAM.** Everyone agrees capacitor-over-bitline 6F2 planar DRAM is near the end. Samsung's path is VCT (vertical channel transistor) at 4F2, targeting 8-9 nm class by 2027-28; SK hynix calls its equivalent 4F2 VG (vertical gate) and has published a 30-year roadmap running 4F2 VG → 3D DRAM; Micron is reportedly skipping VCT and going straight at true 3D DRAM (**REPORTED**, with SK hynix's VLSI 2025 roadmap paper **CONFIRMED**) [29][30][31]. 4F2 buys roughly 30% die-area reduction over 6F2 [30]. **SPECULATION:** true 3D DRAM (stacked cell layers, NAND-like) does not reach volume before 2030; 4F2 VCT is the entire near-term story and will be sufficiently hard to keep DRAM supply tight.

**Emerging NVM and CXL.** GlobalFoundries has a 22FDX+ RRAM platform with volume production slated for 2026 and offers eFlash/MRAM/RRAM as a three-way embedded NVM menu (**CONFIRMED** vendor roadmap) [43]. HfO2-based FeRAM remains scientifically attractive (CMOS-compatible, scalable) and practically blocked by wake-up and fatigue behavior plus a <650 °C thermal budget requirement (**CONFIRMED** in the literature). CXL: 2.0 switches are in production at Marvell with **CXL 3.0 parts sampling around Q3 2026** (**REPORTED**) [50]. Memory *expansion* over CXL works and is deploying; memory *pooling* across hosts remains economically marginal — the latency and the switch BOM eat the stranded-capacity savings (**REPORTED/SPECULATION**).

---

## 5. Photonics, optical I/O, and the interconnect wall

This is the frontier that most visibly changed state in 2026: co-packaged optics stopped being a conference demo.

- **Broadcom** Tomahawk 6-Davisson, a 102.4 Tb/s CPO switch using TSMC COUPE optical engines, began shipping October 2025 (**CONFIRMED**) [24].
- **NVIDIA** stated on 31 May 2026 that Spectrum-X Ethernet Photonics switches (200 Gb/s SerDes) are in production, with CoreWeave, Lambda and OCI as early adopters (**CONFIRMED**) [24].
- TrendForce reports both are in volume ramp, with **optical-engine yield and advanced packaging capacity** as the expansion bottlenecks — not switch ASIC supply (**REPORTED**) [23].
- **TSMC COUPE**: the substrate-integrated generation is a 2026 production item, claiming 2x power efficiency and 10x latency reduction vs pluggable optics (**CONFIRMED** via TSMC symposium) [1].

The *next* step — optics on the accelerator package rather than the switch — is not yet in production. Ayar Labs raised a $500M Series E in March 2026 to fund TeraPHY volume production and showed a 1,024-accelerator rack-scale reference design with Wiwynn at OFC 2026; Lightmatter's Passage L200/L200X (32/64 Tb/s 3D CPO engines, GF + ASE/Amkor) enter customer chip integration in 2026 with production systems in 2027 (**CONFIRMED** for announcements, **REPORTED** for timing) [26]. **SPECULATION:** in-package optical I/O on GPUs is a 2027-28 volume event, and the gating factor is reliability/serviceability of the laser source, not bandwidth density.

---

## 6. Compute paradigms outside the CPU/GPU mainline

**Neuromorphic.** Intel's Hala Point (1.15B neurons, 1,152 Loihi 2, >380 trillion 8-bit synaptic ops/s, >15 TOPS/W on DNN inference) remains a research platform at Sandia, not a product [46]. The commercial motion is at the edge: BrainChip's Akida AKD1500 entered commercial production shipments on 30 June 2026 on GlobalFoundries 22FDX (**REPORTED**) [46]. SpiNNaker2 (SpiNNcloud) is selling systems into research and defense but has no volume commercial deployment. **Analysis:** neuromorphic in 2026 is a *sensor-adjacent, microwatt-class* business, not a datacenter business, and framing it as an AI-accelerator competitor keeps producing disappointment.

**Analog / in-memory compute.** IBM's 64-core mixed-signal AIMC chip (14 nm CMOS with BEOL phase-change memory, on-chip network, digital activation functions) remains the reference point (**CONFIRMED**, Nature Electronics) [35]; 2026 work in the same venue reports a fully integrated analogue *closed-loop* IMC accelerator for inverse matrix-vector multiplication built on SRAM [36]. The persistent blockers are unchanged: ADC/DAC energy and area dominate at useful precision, and device drift/variability forces periodic recalibration. **SPECULATION:** analog IMC's commercial beachhead will be always-on edge inference and closed-loop control (where the Nature Electronics 2026 result points), not transformer training.

**AI in chip design.** 2026 is when this became a shipping product category rather than a research claim. At DAC 2026, Synopsys (AgentEngineer, on NVIDIA Agent Toolkit + Nemotron 3 Ultra), Cadence (AuraStack AI Super Agent), and Siemens (Fuse self-verifying agents) all announced autonomous multi-step workflows (**CONFIRMED** vendor announcements) [37][38]. Synopsys claims verification closure from weeks to hours, up to **50x faster time-to-validated RTL with +20% coverage** (**REPORTED** — vendor-supplied benchmark, no independent replication) [38]. NVIDIA is both supplier and heaviest internal user, running agents across design and simulation with a re-architected PhysicsNeMo [39]. AlphaChip-style RL floorplanning is now a component inside these agent stacks rather than a standalone story. **Analysis:** the credible near-term value is in verification and formal coverage, which is where the drudgery and the ground-truth signal both live; PPA-optimizing agents remain harder to trust because the reward is slow and noisy.

---

## 7. Power and RF: the un-glamorous frontier that is actually binding

**Wide bandgap.** The GaN+SiC power semiconductor market is ~$6.8B in 2026, with SiC now the default for EV traction inverters and the industry transitioning 6-inch → 200 mm SiC and 8-inch GaN, which is collapsing device prices (**REPORTED**) [42]. **Ultra-wide bandgap** (Ga2O3, diamond, AlN) remains pre-commercial: Ga2O3 has the best growth economics (melt-grown bulk substrates) and the worst thermal conductivity; diamond has the opposite problem. Neither ships in volume in 2026 (**CONFIRMED** by absence).

**The demand driver has moved.** The 800 VDC transition in AI datacenters is the biggest new power-semiconductor market of the decade. At ~600 kW racks, going 54 V → 800 V cuts current ~15x and conductor resistive losses ~219x; SemiAnalysis puts the retrofit start at 2026-27 led by Google and Meta, with row-level HVDC sidecars, and estimates ~50 MW saved per 1 GW of IT load (~5%) (**REPORTED**, well-argued) [41]. Note the nuance: NVL72-class racks at 180-220 kW in late 2026/2027 can still be served by three-phase AC — 800 VDC is a 2027+ necessity, not a 2026 one [41].

**RF and 6G.** FR3 (7-24 GHz) is the practical 6G band and the 2026 silicon story: Skyworks and MediaTek showed FR3 + PC1 front-end work at MWC 2026 (**CONFIRMED**) [44]. Sub-THz (100-300 GHz) needs transistors with fT/fmax in the 500 GHz-1 THz range, which today means SiGe BiCMOS and InP; CMOS/RFSOI suffices to roughly 150 GHz for short range (**CONFIRMED** in the roadmap literature) [45]. GaN carries the power-amplifier load at base-station frequencies. **SPECULATION:** the 6G front-end will be won on *filter and switch integration density* in RFSOI, not on exotic sub-THz PAs, because band count is growing faster than form factor allows.

---

## 8. China

- **Logic:** SMIC's N+3, a 5nm-class node achieved with DUV multipatterning only, fabs Huawei's Ascend 950PR; SMIC plans to roughly double advanced capacity to ~70k wafers/month during 2026 (**REPORTED**) [32][33]. Each further generation costs exponentially more mask layers and yield.
- **Accelerators:** Huawei's Ascend 950 family launches through 2026 (950PR, then 950DT in Q4 2026 with 144 GB of HiZQ 2.0 at 4 TB/s), with Ascend 960/970 sketched for 2027/2028 (**CONFIRMED** via Huawei's own roadmap presentation) [32].
- **Memory:** Huawei announced **homegrown HBM** (HiZQ), and CXMT's roadmap claims HBM3E capability in 2026 (**REPORTED**) [32][33]. CXMT's 1z/G4 node is adequate for HBM3 and possibly HBM4 with heroic multipatterning; beyond that the economics break without EUV.
- **Lithography:** SMEE's SSA800-series 28 nm-class immersion DUV entered limited production, ~10 units sold, ~5 shipping in 2026 and ~20 in 2027, under evaluation at SMIC since September 2025; immersion DUV IP was reorganized into Yuliangsheng (SiCarrier-linked) while SMEE retained the EUV program. A Huawei/SiCarrier EUV *prototype* is reported in Shenzhen (**REPORTED**, unverified). Asia Times' assessment — roughly four generations behind ASML on DUV — is the sober read [34].

**Analysis:** the export-control regime has not stopped China from building competitive *systems*; it has made them expensive. The binding constraint on Ascend volume is HBM and packaging, not logic wafers, and that is exactly where CXMT's 2026 HBM3E claim matters most.

---

## What people are underestimating *(labeled analysis — my judgment, not sourced fact)*

1. **Power delivery and thermals are the real 2027 wall, not lithography.** A 14-reticle package with 10 compute dies and 20 HBM stacks is a 3-5 kW device on a substrate that must stay flat to microns. The industry has a credible transistor roadmap to 2029 and no credible answer for extracting 3 kW from a 100 cm² package without immersion or microfluidics. The 800 VDC transition is the visible part; the invisible part is on-package voltage regulation.
2. **Backside power is a *manufacturing* revolution disguised as a *device* one.** Wafer thinning to sub-micron silicon, bonding to a carrier, and doing lithography on the back of a wafer with front-side alignment is a new class of process control. Whoever gets backside *yield* right — not backside *devices* right — wins the angstrom era. Intel is ahead here and it is under-priced.
3. **HBM is de-commoditizing and nobody has repriced it.** Custom base dies fabbed on logic nodes mean HBM4E stacks are co-designed per customer. That kills the three-vendor commodity dynamic that has historically capped memory margins, and it makes memory supply a *design-cycle* dependency, not a purchasing one.
4. **The merchant chiplet market still does not exist, and its absence is load-bearing.** UCIe solved the electrical interface. Nobody solved known-good-die liability, thermal co-design contracts, or multi-vendor test. Until an actual company sells an actual chiplet to an actual unrelated customer at volume, "chiplet ecosystem" is a roadmap slide.
5. **2D materials are ahead of the schedule most people carry in their heads.** 50 nm CPP complementary 2D FETs on 300 mm with 94% yield and single-EUV-exposure patterning is not a physics demo; it is a process-integration demo. The plausible first insertion is not the logic channel — it is backend/backside devices and memory selectors, and that could happen before 2030.
6. **Agentic EDA's real effect is on the *number of designs*, not the cost of one design.** If verification closure genuinely drops from weeks to hours, the marginal cost of a derivative SKU collapses and the industry gets more custom silicon, not cheaper silicon. That is a demand shock to foundry capacity and packaging that nobody is modeling.
7. **A16 slipping matters more than N2 succeeding.** N2 was always going to work. Super Power Rail is where TSMC takes on genuine process risk for the first time in a decade, and it is the node where Intel's PowerVia head start could actually convert into customers.
8. **Neuromorphic and analog IMC keep being evaluated against the wrong benchmark.** Judged as datacenter accelerators they look like failures; judged as sub-milliwatt always-on perception they are already shipping in volume. The category error is costing the field credibility it doesn't deserve to lose.

---

## Key numbers

| Item | Value | Timing | Label |
|---|---|---|---|
| TSMC N2 volume production | started | Q4 2025 | CONFIRMED [1] |
| TSMC N2 tape-outs | 20+ received, 70+ pipeline | 2026 | CONFIRMED [1] |
| TSMC N2 capacity | ~90-100k wpm → ~140k wpm | early → end 2026 | REPORTED [49] |
| TSMC N2 wafer price | ~$30,000 | 2026 | REPORTED [49] |
| A16 vs N2P | +8-10% speed / -15-20% power / 1.07-1.10x density | 2026-27 | CONFIRMED [4] |
| N2U vs N2P | +3-4% speed or -8-10% power | 2028 | CONFIRMED [1] |
| A13 vs A14 | 6% area saving, backward-compatible rules | 2029 | CONFIRMED [1] |
| CoWoS capacity (TSMC) | ~70k → 120-140k wpm | 2025 → end 2026 | REPORTED [20] |
| CoWoS reticle limit | 14 reticles, ~10 dies + 20 HBM | 2028 | CONFIRMED [1] |
| SoIC hybrid bond pitch | ~9 µm → ~6 µm HVM | 2026 | REPORTED [19] |
| HBM4 | 2048-bit, 1.5-2 TB/s/stack, ≤64 GB, 16-Hi | 2026 | CONFIRMED [21] |
| HBM4E | 14-16 Gbps, 3.6-4.0 TB/s/stack | 2027+ | REPORTED (no JEDEC spec) [22] |
| High-NA EUV installed base | ~10 systems, 4 customers | Sept 2026 | REPORTED [10] |
| High-NA per-tool cost | ~$400M | 2026 | REPORTED [12] |
| Intel 14A external customers | 2 evaluating, 0 committed | mid-2026 | CONFIRMED [8] |
| Samsung SF2P yield | ~70% | Jan 2026 | REPORTED [13][47] |
| imec CFET bottom-pFET Rext | 1753 → 378 Ω·µm | VLSI 2026 | CONFIRMED [16] |
| 2D complementary FETs | 50 nm CPP, 28 nm Lg, 94% yield, >10^5 on/off | VLSI 2026 | CONFIRMED [27][28] |
| Cerebras WSE-3 Turbo | 46,225 mm², 4T transistors, ~900k cores, N5 | 2026 | CONFIRMED [40] |
| Hala Point | 1.15B neurons, 1,152 Loihi 2, >380T SOPS, >15 TOPS/W | research | CONFIRMED [46] |
| 800 VDC benefit @600 kW rack | ~15x lower current, ~219x lower I²R loss | 2026-27 retrofit | REPORTED [41] |
| GaN+SiC market | ~$6.8B | 2026 | REPORTED [42] |
| Huawei Ascend 950DT memory | 144 GB HiZQ 2.0 @ 4 TB/s | Q4 2026 | CONFIRMED (Huawei) [32] |
| SMIC advanced capacity | → ~70k wpm | during 2026 | REPORTED [33] |

---

## Sources

1. TSMC, "TSMC Debuts A13 Technology at 2026 North America Technology Symposium" — https://pr.tsmc.com/english/news/3302 (2026)
2. Tom's Hardware, "TSMC unveils process technology roadmap through 2029 — A12, A13, N2U announced, A16 slips to 2027" — https://www.tomshardware.com/tech-industry/semiconductors/tsmc-unveils-process-technology-roadmap-through-2029-a12-a13-n2u-announced-a16-slips-to-2027 (2026)
3. SemiEngineering, "TSMC Tech Symposium 2026, By The Numbers" — https://semiengineering.com/tsmc-tech-symposium-2026-by-the-numbers/ (2026)
4. TSMC, A16 Technology page — https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_A16 (accessed 2026-09-07)
5. TSMC, A14 Technology page — https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_A14 (accessed 2026-09-07)
6. Intel Newsroom, "Intel Unveils Panther Lake Architecture: First AI PC Platform Built on 18A" — https://newsroom.intel.com/client-computing/intel-unveils-panther-lake-architecture-first-ai-pc-platform-built-on-18a (2025-2026)
7. Tom's Hardware, "Intel's roadmaps examined — 14A, Nova Lake, Diamond Rapids & AI accelerator push" — https://www.tomshardware.com/tech-industry/semiconductors/intel-chip-roadmap-2026-2028 (2026)
8. Tom's Hardware, "Intel says it has two prospective customers for 14A" — https://www.tomshardware.com/tech-industry/semiconductors/intel-says-it-has-two-prospective-customers-for-14a-expects-to-hear-about-commitments-in-second-half-of-2026 (2026)
9. EE Times, "Intel's Confidence Shows As It Readies New Processors on 18A" — https://www.eetimes.com/intels-confidence-shows-as-it-readies-new-processors-on-18a/ (2026)
10. TrendForce, "ASML Advances High-NA EUV Toward HVM as 10 Systems Reportedly Go Live at 4 Customers" — https://www.trendforce.com/news/2026/09/01/news-asml-advances-high-na-euv-toward-high-volume-manufacturing-as-10-systems-reportedly-go-live-at-4-customers (2026-09-01)
11. TrendForce, "imec Secures ASML's Most Advanced EXE:5200 High-NA EUV for Sub-2nm; 4Q26 Qualification Target" — https://www.trendforce.com/news/2026/03/19/news-imec-secures-asmls-most-advanced-exe5200-high-na-euv-for-sub-2nm-4q26-qualification-target/ (2026-03-19)
12. TrendForce, "ASML's High-NA EUV for 2027-28: Which Giants Are Betting Big" — https://www.trendforce.com/news/2026/02/16/news-asmls-high-na-euv-for-2027-28-which-giants-are-betting-big-intel-samsung-sk-hynix-or-tsmc/ (2026-02-16)
13. Design&Reuse, "Samsung delays 1.4nm node, doubles down on 2nm process enhancement" — https://www.design-reuse.com/news/202528986-samsung-delays-1-4nm-node-doubles-down-on-2nm-process-enhancement/ (2026)
14. Rapidus, "NEDO Approves Rapidus' FY2026 Plan and Budget for 2nm Semiconductor Projects" — https://www.rapidus.inc/en/news_topics/information/nedo-approves-rapidus-fy2026-plan-and-budget-for-2nm-semiconductor-projects/ (2026)
15. Tom's Hardware, "Rapidus fab roadmap examined" — https://www.tomshardware.com/tech-industry/semiconductors/rapidus-fab-roadmap-examined (2026)
16. imec, "Performance boosters scale monolithic CFET across multiple logic technology nodes" — https://www.imec-int.com/en/articles/performance-boosters-scale-monolithic-cfet-across-multiple-logic-technology-nodes (2026)
17. SemiEngineering, "Powering CFETs From The Backside" — https://semiengineering.com/powering-cfets-from-the-backside/ (2026)
18. eeNews Europe, "IEDM: CFETs make progress at 5nm and 7angstrom" — https://www.eenewseurope.com/en/iedm-cfets-make-progress-at-5nm-and-7angstrom/ (2025-12)
19. Tom's Hardware, "The current state of Hybrid Bonding in 2026 — TSMC sits at 6 microns" — https://www.tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined (2026)
20. DigiTimes, "Podcast highlights: SoIC vs CoWoS, HBM5 hybrid bonding, and EMIB-T's yield problem" — https://www.digitimes.com/news/a20260904PD233/packaging-digitimes-expansion-2026-sram.html (2026-09-04)
21. EE Times, "The State of HBM4 Chronicled at CES 2026" — https://www.eetimes.com/the-state-of-hbm4-chronicled-at-ces-2026/ (2026-01)
22. SemiEngineering, "HBM4E Raises The Bar For AI Memory Bandwidth" — https://semiengineering.com/hbm4e-raises-the-bar-for-ai-memory-bandwidth/ (2026)
23. TrendForce, "NVIDIA and Broadcom Begin Volume Ramp of CPO Switches" — https://www.trendforce.com/presscenter/news/20260727-13151.html (2026-07-27)
24. EDN, "Where co-packaged optics (CPO) technology stands in 2026" — https://www.edn.com/where-co-packaged-optics-cpo-technology-stands-in-2026/ (2026)
25. SemiAnalysis, "Co-Packaged Optics (CPO) – Scaling with Light for the Next Wave of Interconnect" — https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling (2026)
26. The Register, "Ayar Labs raises $500M to mass-produce CPO chiplets" — https://www.theregister.com/2026/03/03/ayar_labs_500m/ (2026-03-03)
27. imec, "ASML, TSMC and imec bring industry-ready 2D-material transistors closer with breakthrough 300mm integration" — https://www.imec-int.com/en/press/asml-tsmc-and-imec-bring-industry-ready-2d-material-transistors-closer-breakthrough-300mm (2026-06)
28. Tom's Hardware, "imec, ASML, and TSMC fab complementary 2D-material transistors at 50nm pitch on a 300mm wafer" — https://www.tomshardware.com/tech-industry/semiconductors/imec-asml-and-tsmc-build-complementary-2d-material-transistors-at-50nm-pitch-on-a-300mm-wafer (2026-06)
29. DigiTimes, "SK Hynix unveils 30-Year DRAM roadmap with Vertical Gate, 3D stack" — https://www.digitimes.com/news/a20250611PD239/dram-roadmap-3d-performance (2025-06-11)
30. DigiTimes, "Samsung and SK Hynix reportedly accelerate VCT DRAM development as stepping stone to 3D DRAM" — https://www.digitimes.com/news/a20250620PD214/dram-samsung-sk-hynix-3d-development.html (2025-06-20)
31. SemiAnalysis, "The Memory Wall: Past, Present, and Future of DRAM" — https://newsletter.semianalysis.com/p/the-memory-wall (2025-2026)
32. TechPowerUp, "Huawei Unveils Homegrown HBM and Ascend 950, Bets on Massive SuperClusters" — https://www.techpowerup.com/341123/huawei-unveils-homegrown-hbm-and-ascend-950-bets-on-massive-superclusters (2025-09)
33. The Substrate, "Where China's AI chip supply chain stands in 2026" — https://www.the-substrate.net/p/where-chinas-ai-chip-supply-chain (2026)
34. Asia Times, "China's DUV lithography still lags ASML by four generations" — https://asiatimes.com/2026/07/chinas-duv-lithography-still-lags-asml-by-four-generations/ (2026-07)
35. Nature Electronics, "A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference" — https://www.nature.com/articles/s41928-023-01010-1 (2023)
36. Nature Electronics vol. 9 (2026), "A fully integrated analogue closed-loop in-memory computing accelerator ... based on SRAM" — https://www.nature.com/articles/s41928-025-01549-1 (2026)
37. Futurum Group, "Synopsys, Cadence, and Siemens Take Agentic Chip Design Autonomous at DAC" — https://futurumgroup.com/insights/synopsys-cadence-and-siemens-take-agentic-chip-design-autonomous-at-dac/ (2026-07)
38. Synopsys, "Synopsys Showcases Comprehensive Autonomous Engineering Workflows from Silicon to Systems, Developed with NVIDIA Technology" — https://news.synopsys.com/2026-07-26-Synopsys-Showcases-Comprehensive-Autonomous-Engineering-Workflows-from-Silicon-to-Systems,-Developed-with-NVIDIA-Technology (2026-07-26)
39. The Next Platform, "Nvidia Accelerates Chip Engineering With AI Agents" — https://www.nextplatform.com/hpc/2026/07/27/nvidia-accelerates-chip-engineering-with-ai-agents/5279125 (2026-07-27)
40. Tom's Hardware, "Hot Chips 2026: Cerebras lays out the future of wafer-scale AI" — https://www.tomshardware.com/tech-industry/artificial-intelligence/hot-chips-2026-cerebras-lays-out-the-future-of-wafer-scale-ai-nexus-system-architecture-triples-rack-scale-performance-cs-6-wafer-to-incorporate-stacked-dram (2026-08)
41. SemiAnalysis, "Inside the 800VDC Revolution – Part 1" — https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part (2026)
42. IDTechEx, "Power Electronics Market 2026-2036: Data Centers, Electric Vehicles, and Renewables" — https://www.idtechex.com/en/research-report/power-electronics-market/1152 (2026)
43. Mark LaPedus, "GlobalFoundries Rolls Out RRAM, SiGe Technologies" — https://marklapedus.substack.com/p/globalfoundries-rolls-out-rram-sige (2026)
44. GeneOnline, "Skyworks Solutions and MediaTek Showcase FR3 and PC1 RF Front-End Innovations for 6G at MWC 2026" — https://www.geneonline.com/skyworks-solutions-and-mediatek-showcase-fr3-and-pc1-rf-front-end-innovations-for-6g-at-mwc-2026/ (2026-03)
45. IDTechEx, "6G: Key Hardware Technologies and Future Development Roadmap" — https://www.idtechex.com/en/research-article/6g-key-hardware-technologies-and-future-development-roadmap/32034 (2026)
46. IDTechEx via Yahoo Finance, "Global Neuromorphic Computing & Sensing Market 2026-2036" — https://finance.yahoo.com/news/global-neuromorphic-computing-sensing-market-093000515.html (2026)
47. TrendForce, "Samsung Reportedly Achieves 30%+ Yield in SF2 Test Production" — https://www.trendforce.com/news/2025/02/07/news-samsung-reportedly-achieves-30-yield-in-sf2-test-production-set-for-q4-mass-prodution/ (2025-02-07)
48. TrendForce, "ASML Confirms First High-NA EUV EXE:5200 Shipment, Reportedly Prepping for Intel's 14A in 2027" — https://www.trendforce.com/news/2025/07/17/news-asml-confirms-first-high-na-euv-exe5200-shipment-reportedly-prepping-for-intels-14a-in-2027/ (2025-07-17)
49. EEWorld, "TSMC's initial 2nm (N2) production capacity ... potentially reaching 140,000 wafers by the end of 2026" — https://en.eeworld.com.cn/news/manufacture/eic716007.html (2026)
50. ServerMall, "CXL in 2026: Server Memory Expansion & Pooling" — https://servermall.com/blog/cxl-in-2026-memory-expansion-and-pooling/ (2026)
