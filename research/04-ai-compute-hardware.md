# AI Compute Hardware Frontier — State of Play, September 2026

*Research brief. Date: 2026-09-07. Status labels: **CONFIRMED** = vendor statement, filing, or press release; **REPORTED** = credible trade press / analyst reporting not yet vendor-confirmed; **RUMOR** = single-source or unverifiable.*

---

## TL;DR

- **Nvidia's Vera Rubin is in full production** (Nvidia, 26 Aug 2026) and ramping at CoreWeave, Google Cloud, Azure, OCI and Nebius. Q2 FY27 revenue was $96.2B (+106% YoY), data center $89.0B, Q3 guide $108B [1]. Rubin: 50 PF NVFP4 inference, 288 GB HBM4, 22 TB/s, 336B transistors on two N3P reticle dies; the rack was renamed **NVL72** (72 packages / 144 dies) from "NVL144" [2].
- **The roadmap cadence is explicit**: Rubin (H2 2026, ~130 kW Oberon racks) → Rubin CPX (end 2026) → Rubin Ultra in the **600 kW Kyber rack, 800 VDC** (H2 2027, 1 TB HBM4E, 100 PF/package, 15 EF/rack) → **Feynman (2028)**, all-CPO, paired with the Rosa CPU, on TSMC CoPoS packaging [3][4][5][6].
- **AMD's MI455X/Helios is the first credible rack-scale alternative**: 40 PF FP4, 432 GB HBM4, 23.3 TB/s per GPU on eight TSMC N2 compute dies; 72-GPU Helios rack at 2.9 EF, 31 TB HBM4, UALink-over-Ethernet scale-up. AMD says high-volume H2 2026; SemiAnalysis reported the real mass ramp is Q2 2027 [7][8][9].
- **Hyperscaler silicon is now real, not aspirational**: Google Ironwood (TPU v7) GA April 2026 with a 9,216-chip / 42.5 EF FP8 superpod and a split-architecture TPU 8t/8i successor; AWS Trainium3 GA (2.52 PF FP8, 144 GB) with Trainium4 adopting NVLink Fusion; Microsoft Maia 200 (10 PF FP4, 216 GB, 750 W) live in Iowa; Meta MTIA 300 in production with a new chip every ~6 months [10][11][12][13][14][15].
- **Inference-specialist silicon crossed into commercial reality in 2026**: Nvidia paid $20B to license Groq and shipped the Groq 3 LPU (500 MB SRAM, Samsung SF4, 256-LPU LPX rack); Cerebras IPO'd on 14 May 2026 at $56B (closed day one ~$66B) on $510M 2025 revenue; Etched delivered its first customer rack and raised $700M at $21B; SambaNova raised $1B at $11B; Tenstorrent Blackhole Galaxy reached GA [16][17][18][19][20][21].
- **Memory and packaging are the binding constraints.** HBM4 entered mass production in Feb 2026 (SK hynix ~70% of Nvidia's Rubin HBM4; Samsung >30% of the HBM market); 12-Hi HBM4 stacks are $500–600+, a 55–70% premium over HBM3E, and HBM3E itself rose ~20% for 2026. TSMC CoWoS goes from ~75–80k wafers/month (end-2025) to 120–140k (end-2026) yet the supply gap only narrows from ~20% to ~10% [22][23][24][25][26][27].
- **Process**: TSMC N2 in volume since Q4 2025; N2P H2 2026; **A16 slipped to 2027**; A13/A12 in 2029 without High-NA EUV [28][29].
- **Capex**: Big-4 2026 guidance sums to ~$600–650B (vs $388B in 2025); with Oracle, FY26 exceeds $690B and calendar-2026 approaches $800B including finance leases. Incremental debt funds ~32% of capex; Alphabet did an $84.75B equity raise in June 2026 [30][31][32].
- **Epoch trends**: frontier training compute +5×/yr since 2020; AI chip perf/$ +49%/yr; training cost +3.5×/yr (Grok 4 ≈ $500M); LLM inference prices at constant capability fall 9×–900×/yr depending on benchmark [33][34][35].
- **What's underestimated**: the shift from chip FLOPS to *rack and campus power-delivery* (600 kW → 1 MW racks, 800 VDC) as the real gating factor; memory pricing as a margin killer for non-Nvidia silicon; and the fact that most "2026 shipping" claims from startups are first-rack milestones, not gigawatts.

---

## 1. Nvidia: Blackwell Ultra → Rubin → Rubin Ultra → Feynman

### 1.1 Where shipments actually are (CONFIRMED)
Nvidia's Q2 FY2027 results (26 Aug 2026): revenue $96.2B (+106% YoY, +18% QoQ), data center $89.0B (+117% YoY), Q3 guidance $108B ±2% at 74% gross margin. The release states *"Vera Rubin, now in full production"* with deployments ramping at CoreWeave, Google Cloud, Microsoft Azure, OCI and Nebius, and cites "over $500 billion of third-party capital" mobilized for AI-infrastructure financing [1]. Blackwell Ultra (GB300 NVL72, 288 GB HBM3E, ~130–140 kW/rack) remains the volume product through 2026 while Rubin ramps [4].

### 1.2 Vera Rubin NVL72 (CONFIRMED — CES, Jan 2026)
Per Nvidia's CES 2026 launch [2]:
- **Rubin GPU**: 50 PFLOPS NVFP4 inference, 35 PFLOPS NVFP4 training; 336B transistors across two reticle-sized TSMC 3nm dies; 288 GB HBM4 at **22 TB/s** (2.8× Blackwell); NVLink 6 at 3.6 TB/s per GPU; NVLink-C2C 1.8 TB/s. Nvidia claims 8× inference perf/W vs Blackwell.
- **Vera CPU**: 88 custom "Olympus" Arm cores, 176 threads, up to 1.5 TB LPDDR5X at 1.2 TB/s.
- **Rack**: 72 Rubin packages (144 dies) + 36 Vera; 3.6 EF NVFP4 inference, 2.5 EF training; 20.7 TB HBM4 at 1.6 PB/s; 54 TB LPDDR5X; 220 trillion transistors. Nvidia now counts packages, so the rack is branded **NVL72** (formerly NVL144). Tray assembly time fell from 100 minutes to 6 (cable-free trays).
- **Ecosystem chips**: NVLink 6 switch (400G SerDes, liquid-cooled), ConnectX-9 (1.6 Tb/s), BlueField-4 (64-core Grace), Spectrum-6 CPO switches (SN6800 409.6 Tb/s; SN6810 102.4 Tb/s).
- **Rack power**: ~120–130 kW+ in the Oberon rack, per Introl's analysis; Blackwell-generation cooling vendors already demonstrate 250 kW racks at 40 °C inlet [3].

### 1.3 Rubin CPX (CONFIRMED — announced Sept 2025, available end-2026)
A GDDR7-based "context" GPU for prefill/long-context inference: 30 PF NVFP4, 128 GB GDDR7, 3× attention throughput vs GB300. The Vera Rubin NVL144 CPX rack (144 CPX + 144 Rubin dies) is rated at 8 EF NVFP4, 100 TB fast memory, 1.7 PB/s; Nvidia's marketing claim is "$5B token revenue per $100M invested" [5].

### 1.4 Rubin Ultra / Kyber (CONFIRMED roadmap; specs REPORTED)
- **CONFIRMED (GTC 2025/2026)**: Rubin Ultra ships H2 2027 in the **Kyber** rack — vertical blades, four pods of 18 blades, ~**600 kW**, fully liquid-cooled, 800 VDC distribution, two rack footprints per system (compute + sidecar) [3][4].
- **REPORTED specs**: four reticle-sized compute dies per package, ~100 PF NVFP4 per package, **1 TB HBM4E**, NVLink 7 (~10.8 TB/s per GPU), 576 dies / 144 packages per rack, ~15 EF NVFP4 and ~365 TB total memory per rack — roughly 14× GB300 NVL72 [4][6].
- **REPORTED (GTC 2026, SemiAnalysis)**: with the package-count naming, the single Kyber rack is "Rubin Ultra NVL144" (all-copper scale-up); "NVL576" describes a multi-rack NVLink domain stitched with co-packaged optics; **Feynman "NVL1152"** = 8 Kyber racks, "all CPO" per Jensen Huang. GTC 2026 also introduced Attention-FFN Disaggregation (attention on GPUs, FFN on LPUs) and a 256-CPU "Vera ETL256" rack [36].

### 1.5 Feynman (CONFIRMED date; details REPORTED)
Feynman is on the roadmap for 2028 with the Rosa CPU, NVLink 8, BlueField-5, 3D stacking, and pervasive co-packaged optics [4][6]. TrendForce reports TSMC's CoPoS (panel-level CoWoS) qualification completed June 2026, pilot mid-2027, mass production 2028–29 **with Feynman as lead customer** [26]. Claims of "LP40 memory" for Feynman in secondary roundups appear to conflate the Groq LP40 chip and should be treated as **RUMOR** [6][36].

### 1.6 Groq inside Nvidia (CONFIRMED)
Nvidia's ~$20B deal (Dec 2025) was an IP license plus hiring of Jonathan Ross and Sunny Madra, not a full acquisition; GroqCloud continued independently and reportedly raised $650M in June 2026 [16][21]. The **Groq 3 LPU ("LP30")**: 500 MB SRAM, 1.2 PF FP8, Samsung SF4 (4 nm); the **LPX rack** holds 256 LPUs (128 GB aggregate SRAM, ~40 PB/s aggregate bandwidth), sits beside a Vera Rubin NVL72, and targets 1,500 tok/s per user for agentic decode; Nvidia claims 35× throughput/MW for the pairing. Racks were "already in production" at Hot Chips (Aug 2026); an Artificial Analysis benchmark measured 3,431 output tok/s on a 100K-context Gemma 4 31B workload, ~4× the next-fastest endpoint (REPORTED). A successor **LP40 on TSMC N3P with NVLink** is planned [16][17][36].

---

## 2. AMD: MI350 → MI400 / Helios

- **MI350/MI355X** (shipping since mid-2025): 288 GB HBM3E, ~10 PF FP4 — the baseline AMD uses for MI455X comparisons [8].
- **MI455X (CONFIRMED, Hot Chips Aug 2026)**: 40.26 PF MXFP4, 20.13 PF MXFP8/FP6, 315 TF FP16; **432 GB HBM4** (12 stacks) at **23.3 TB/s**; 8 "accelerator complex" dies on **TSMC N2** with N3P fabric/cache/IO dies in a CoWoS-L package; 256 WGPs, 192 MB L2; UALink-over-Ethernet scale-up 3.6 TB/s per GPU (3.2 TB/s measured); scale-out 190 GB/s [8]. This is the first volume AI accelerator with N2 compute dies — ahead of Nvidia, whose Rubin is on N3P.
- **Helios rack (CONFIRMED)**: 72 MI455X + 96-core EPYC "Venice" + Pensando Vulcano 800G NICs, 44OU ORW-HPR chassis (18 compute trays, 6 switch trays); 2.9 EF FP4, 31 TB HBM4, 1.7 PB/s, 260 TB/s scale-up, 43 TB/s scale-out; each GPU carries 18× 800G UALoE adapters [7]. Family: MI430X (HPC/FP64), MI440X (8-way), MI450 (64-GPU systems) [9].
- **Timing**: AMD (Forrest Norrod, Feb 2026) — "highly confident of ramping Helios in high volume in the second half of the year," and denies thermal issues. SemiAnalysis (**REPORTED**) — engineering samples and low-volume production H2 2026, mass ramp Q2 2027 [9]. Helios is in qualification at hyperscalers but no cloud lists UALink instances as of mid-2026 (REPORTED) [37].
- **Customers (CONFIRMED, Oct 2025 announcements)**: OpenAI's 6 GW multi-year MI450 agreement (first 1 GW H2 2026) and Oracle's 50,000-GPU MI450 deployment beginning Q3 2026. A ~$5.25M Helios rack price circulating in secondary coverage is **RUMOR** [38].

---

## 3. Hyperscaler custom silicon

### 3.1 Google TPU v7 Ironwood and TPU 8t/8i
- **Ironwood (CONFIRMED, GA 22 Apr 2026)**: 4,614 TF FP8 per chip, 192 GB HBM3E at 7.37 TB/s, 9.6 Tb/s ICI, 9,216-chip superpod = 42.5 EF FP8 and ~1.77 PB HBM [10][39]. SemiAnalysis: Anthropic's ~1M-TPU deal splits into ~400k TPUv7 bought directly through Broadcom (~$10B of racks) and ~600k rented via GCP (~$42B RPO); external TPU users now include Meta and xAI; TPU TCO estimated 30–52% below GB300 at like-for-like utilization (REPORTED) [40]. TrendForce projects Google TPU shipments +40% in 2026, the largest of any CSP [39].
- **TPU v8 (REPORTED, with conflicts)**: Google split the eighth generation into **8t** (training, co-designed with Broadcom, codename "Sunfish") and **8i** (inference, co-designed with MediaTek, "Zebrafish"). One report gives 8t pods of 9,600 chips / 2 PB HBM / 121 EF FP4 and 8i pods of 1,152 chips with 288 GB HBM + 384 MB SRAM (11.6 EF FP8), both GA "later in 2026" [11]; another has both on TSMC 2nm with late-2027 GA and Anthropic's deal expanding to **3.5 GW in 2027** [12]. Treat pod specs and dates as unresolved.

### 3.2 AWS Trainium3 / Trainium4
- **Trainium3 (CONFIRMED, GA Dec 2025)**: TSMC N3P; 2.52 PF FP8, 144 GB HBM3E at 4.9 TB/s (9.6 Gbps pins); Trn3 UltraServer = 144 chips, 362 PF FP8, NeuronSwitch-v1, <10 µs inter-chip latency; UltraCluster 3.0 to 1M chips [13][41]. SemiAnalysis: scale-up is PCIe Gen6-switched (1.2 TB/s/chip) rather than proprietary SerDes; MXFP4 (not NVFP4) support; LNC=8 only from mid-2026 [41]. Project Rainier: >500k Trainium2 for Anthropic [13].
- **Trainium4 (CONFIRMED targets, no date)**: ≥6× FP4, 3× FP8, 4× memory bandwidth vs Trn3, and **NVLink Fusion** support (448G BiDi), with a parallel UALink 224G path reported [13][41].

### 3.3 Microsoft Maia 200 (CONFIRMED, 26 Jan 2026)
TSMC 3nm, >140B transistors, >10 PF FP4, >5 PF FP8, 216 GB HBM3E at 7 TB/s, 272 MB SRAM, 750 W; two-tier Ethernet scale-up at 2.8 TB/s bidirectional to 6,144 accelerators. Microsoft claims 30% better perf/$ than its latest fleet hardware, 3× the FP4 of Trainium3, and FP8 above TPU v7. Inference-only; live in US Central (Iowa), US West 3 (Phoenix) next; serves GPT-5.2-class models for Foundry and M365 Copilot [14].

### 3.4 Meta MTIA (CONFIRMED)
Meta's March 2026 disclosure: **MTIA 300** in production for ranking/recommendation training (216 GB HBM3E, two network chiplets with six 800G RDMA NICs each = 1.2 TB/s I/O); **MTIA 400** finished lab testing and is deploying (GenAI + R&R); **MTIA 450** mass deployment early 2027 (2× HBM bandwidth); **MTIA 500** in 2027 (25× MX4 FLOPS and 4.5× HBM bandwidth vs MTIA 300); a new chip roughly every six months on a chiplet platform; "hundreds of thousands" of MTIA chips already deployed. Meta announced a Broadcom co-development partnership on 14 Apr 2026 [15][42]. Trade-press codenames (Iris, Santa Barbara, Olympus) and a 40–44% TCO advantage are **REPORTED** [43].

### 3.5 OpenAI × Broadcom
**CONFIRMED (13 Oct 2025)**: 10 GW of OpenAI-designed accelerators with Broadcom Ethernet networking, deployments starting H2 2026 and completing by end-2029 [44]. **REPORTED**: TSMC 3nm; a June 2026 public unveiling under the name "Jalapeño"; CoWoS allocation competition with Nvidia/Apple that could push first volume into 2027 [45][46]. The chip name is single-sourced and should be treated as **RUMOR** until OpenAI/Broadcom confirm.

---

## 4. Inference-specialist silicon

| Company | 2026 status | Label |
|---|---|---|
| **Cerebras** | IPO 14 May 2026 (Nasdaq: CBRS) at $185, raised $5.5B, $56.4B fully diluted, closed day one at $311 (~$66B); 2025 revenue $510M (+76%), net profit $237.8M; customers OpenAI, G42, AWS; Series H $1B at ~$23B in Feb 2026. Flagship remains WSE-3; no WSE-4 has been announced. | CONFIRMED [18][19][21] |
| **Groq / Nvidia** | See §1.6. LP30 racks in production; Q3 2026 shipments. | CONFIRMED [16][17] |
| **Etched (Sohu)** | TSMC N4P A0 silicon; "first racks ship this summer"; first customer rack delivered by Aug 2026; >$1B contracts; $700M at $21B led by Jane Street (Aug 2026), ~$800M total; targets "gigawatt-scale path in 2027." | CONFIRMED funding; shipments REPORTED [20][21][47] |
| **SambaNova (SN50)** | Frontier SN50 system targeting H2 2026; $1B Series F first close at $11B (Jul 2026); JPMorgan, SoftBank named. | REPORTED [20][21] |
| **Tenstorrent** | Blackhole Galaxy servers GA 28 Apr 2026: 32 chips per 6U at ~$110K, 664 TF FP8 per chip, 180 MB SRAM + GDDR6; 5+ neocloud partners. | REPORTED [20] |
| **d-Matrix** | Corsair (digital in-memory compute) shipping; Raptor (3D-DRAM) next; Series C $275M (Nov 2025). | REPORTED [20] |
| **Positron** | "Asimov" tape-out late 2026; Atlas running on OCI. | REPORTED [20] |

Chipstrat's July 2026 assessment is the right frame: "every entry above is a first-rack or first-sample milestone, not a gigawatt figure," and SRAM-only architectures (Cerebras, Groq) face capacity limits on frontier-scale MoE weights — which is exactly why Nvidia pairs LPUs with HBM GPUs via disaggregation rather than replacing them [20][36].

---

## 5. Memory: HBM3E → HBM4 → HBM4E

- **Timing (CONFIRMED)**: Samsung announced HBM4 mass production on 12 Feb 2026; SK hynix started the same month at M16/M15X [22][23]. Micron is shipping HBM4 samples/volume but with a minority share.
- **Allocation (REPORTED)**: SK hynix supplies ~two-thirds to ~70% of Nvidia's Rubin HBM4 (up from >50% expected); Samsung >30% of the 2026 HBM market after reaching price parity with SK hynix (it had previously discounted HBM3E ~30%); Micron ~8% [22][24].
- **Prices (REPORTED)**: 12-Hi HBM4 (36 GB) at **$500–600+ per stack**, a 55–70% premium over 12-Hi HBM3E (~$300–380); HBM3E contract prices rose ~20% for 2026 despite HBM4's arrival, driven by H200 China exports, Ironwood (8 stacks/chip) and Trainium3 (4 stacks/chip). 2026 HBM revenue mix ≈ 55% HBM4 / 45% HBM3E. Server DRAM contract prices rose 60–70% in Q1 2026; suppliers moved to quarterly contracts [24][25][27].
- **Capacity**: SK hynix says its entire 2026 HBM supply is sold out; Samsung is raising HBM capacity ~50% in 2026 (~250k wafers/month by year-end); Micron's CEO says shortages extend beyond 2026 [27]. OpenAI's Stargate LOI for **900k DRAM wafers/month** (~40% of global output) through 2029 is the single largest demand signal (CONFIRMED LOI; scale interpretation REPORTED) [27].
- **Next**: Rubin Ultra uses **HBM4E** at 1 TB per package (16-Hi), 2027 [6]; MI455X already uses 12 HBM4 stacks per package [8].

---

## 6. Foundry and packaging

- **TSMC nodes (CONFIRMED, April 2026 roadmap)**: N2 in volume since Q4 2025 (Kaohsiung); N2P volume H2 2026; N2X (frontside power) ongoing; **A16 with Super Power Rail backside power slipped from 2026 to 2027**; N2U in 2028 (+3–4% perf or −8–10% power); A14 next, then A13 (optical shrink) and A12 (2nd-gen nanosheet) in 2029 — explicitly **without High-NA EUV** [28][29]. Practical consequence: Rubin/Rubin Ultra are N3P-class; the first N2 accelerators are AMD's MI455X (2026) and, per reports, Google's TPU v8 (2027) [8][12].
- **CoWoS (REPORTED, TrendForce)**: ~75–80k wafers/month at end-2025 → 120–140k by end-2026 (ASE/SPIL adding 20–25k; OSATs collectively 50–60k); the supply–demand gap narrows only from ~20% to ~10% by end-2026, and CoWoS-L/S is fully booked by Nvidia, Google, Amazon, MediaTek [25][26]. Nvidia is also developing **CoWoP** (chip-on-wafer-on-PCB, substrate-less) with SPIL [25]. **CoPoS** (panel) qualified June 2026, pilot mid-2027, mass 2028–29 for Feynman [26].

---

## 7. Interconnect: NVLink, UALink, Ultra Ethernet

- **NVLink 6**: 3.6 TB/s per Rubin GPU; NVLink 7 ~10.8 TB/s for Rubin Ultra (REPORTED) [2][6]. **NVLink Fusion** now has Arm, Fujitsu, Qualcomm, AWS (Trainium4) and Lightmatter as announced participants — the significant one being AWS, which means Nvidia's fabric will link non-Nvidia accelerators inside the largest cloud [13][37][48].
- **UALink (CONFIRMED)**: 1.0 spec (Apr 2025) = 200G/lane, up to 1,024 accelerators, IEEE P802.3dj PHY; **2.0 spec published 7 Apr 2026** adding in-network compute, a chiplet spec, manageability, and 400G readiness. Consortium chair: 1.0 silicon reaches labs H2 2026, products 2027 [49][50]. AMD's MI455X ships with UALink-over-Ethernet (UALoE) rather than native UALink switches — the pragmatic bridge [7][8].
- **Ultra Ethernet**: UEC spec 1.0 (June 2025), current 1.0.3 (Aug 2026); Trainium3, Maia 200 and Helios all use Ethernet-family scale-out, and Maia's scale-up is Ethernet-based [14][51]. Broadcom's Scale-Up Ethernet / ESUN effort with Meta and OpenAI is the competing scale-up path (REPORTED) [37].

---

## 8. Co-packaged optics and photonic interconnect

- **Nvidia (CONFIRMED)**: Quantum-X Photonics InfiniBand switches began shipping late 2025/early 2026; Spectrum-X Photonics Ethernet switches ship H2 2026 (Spectrum-6 SN6800 409.6 Tb/s, SN6810 102.4 Tb/s); Nvidia claims ~3.5× better power efficiency vs pluggables [2][52]. Roadmap: copper stays inside racks; CPO handles inter-rack NVLink domains for Rubin Ultra "NVL576" and *all* scale-up in Feynman [36].
- **Ayar Labs**: TeraPHY optical I/O chiplets at 8 Tbps per port, 10 ns latency; production partnership with Alchip/TSMC (Sept 2025); ~15k units shipped by end-2024 with a 100M+/yr target by 2028; a $500M Series E (Mar 2026) and a 1,024-accelerator Wiwynn reference design at OFC 2026 are **REPORTED** [53][52].
- **Lightmatter**: Passage M1000 3D photonic interposer (114 Tbps), L200/L200X CPO engines (32–64 Tbps) entering customer integrations via GlobalFoundries/ASE/Amkor; joined the NVLink Fusion ecosystem in 2026; $4.4B valuation [48].
- **Celestial AI** was acquired by Marvell (Dec 2025, ~$3.25B) and Marvell bought XConn for UALink/CXL switching (**REPORTED**) [37].

---

## 9. Rack power density and 800 VDC

- Density ladder: H100 HGX ~40 kW → GB200/GB300 NVL72 120–140 kW → Vera Rubin NVL72 ~130 kW+ → **Kyber 600 kW (2027)** → >1 MW "on the horizon" for Feynman-era (2028) [3][4][54].
- **800 VDC (CONFIRMED)**: Nvidia's architecture eliminates rack-level AC/DC conversion; the same wire gauge carries 157% more power than 415 VAC; supports racks "beyond 1 MW"; ecosystem of 80+ companies including Infineon, STMicro, TI, Navitas (silicon), Delta, Flex, LITEON (power), and ABB, Eaton, GE Vernova, Schneider, Siemens, Vertiv (systems). MGX-compatible 800 VDC power racks ship H2 2026; full-scale 800 VDC data centers coincide with Kyber in 2027, with Nvidia claiming up to ~30% TCO reduction and Introl citing ~5% end-to-end efficiency gain and up to 70% lower maintenance cost [3][54][55]. Microsoft and Google publicly back the 800 VDC direction [55].
- Kyber requires full liquid cooling with no fans and two rack footprints per 600 kW system; cooling vendors' current validated ceiling is ~250 kW at 40 °C inlet [3].

---

## 10. Capex, compute growth, and cost per token

### 10.1 AI capex (CONFIRMED guidance; totals are analyst sums)
| Company | 2025 actual | 2026 guidance (Feb) | Mid-year revision |
|---|---|---|---|
| Amazon | $125B | ~$200B | — |
| Alphabet | $91B | $175–185B | $180–190B (Jul) |
| Meta | $72B | $115–135B | $125–145B (Jul) |
| Microsoft | $90B (FY) | $110–120B+ | $37.5B in latest quarter |
| Oracle | — | ~$50B (+136%) | $523B RPO |
| **Big-4 total** | **$388B** | **$600–640B (+62%)** | — |

Five-company FY26 capex exceeds $690B (+80%); calendar-2026 approaches **$800B** including finance leases and prepayments. FCF is near zero or negative for all but Alphabet and Microsoft; incremental debt rose from 9% of capex (FY24) to 32% (LTM mid-2026); Amazon placed a $25B bond and Alphabet raised $84.75B in equity in June 2026 (the largest corporate equity raise on record) [30][31][32]. Nvidia separately cites >$500B of third-party AI-infrastructure capital [1].

### 10.2 Compute growth (Epoch AI, updated Feb 2026)
Frontier training compute grows **5×/yr** (doubling every 5.2 months); AI chip performance per dollar +49%/yr; memory bandwidth +28%/yr; energy efficiency +34%/yr; frontier training cost +3.5×/yr, with Grok 4 (Jul 2025) at ~$500M and $1B+ runs expected by 2026. The top-1 model was projected to pass 1e26 FLOP around Jan 2026. Epoch's 2030 analysis puts 2e29 FLOP runs as feasible, with power (1–5 GW single campus) the binding constraint [33][34][35][56]. Secondary analyses expect growth to decelerate toward 3–4×/yr from 2026 as power and packaging bind [57].

### 10.3 Cost per token
Epoch's constant-capability analysis finds inference prices falling **9×–900×/yr** depending on benchmark, ~40×/yr for GPT-4-level GPQA performance, with a caveat that the fastest declines are recent and may not persist [35]. Trade sources put GPT-4-class performance at ~$0.40/M tokens in 2026 vs ~$20 in late 2022, Gemini 3.1 Flash at $0.10/$0.40 (input/output), and expect 3–5×/yr declines through 2027 before tapering (REPORTED) [58]. Hardware-side drivers in 2026: NVFP4 (5× Blackwell inference per Rubin GPU), disaggregated prefill/decode (CPX, LPU), and per-rack HBM bandwidth up 2.8× generation-on-generation [2][5][36].

---

## What people are underestimating (analysis)

1. **Power delivery, not FLOPS, is the 2027 gate.** Kyber's 600 kW racks need 800 VDC, full immersion/DLC, and two footprints per system; the validated cooling ceiling today is ~250 kW. Rubin Ultra timing therefore depends on Vertiv/Schneider/Eaton/Delta more than on TSMC. Sites designed for 130 kW Oberon racks cannot be retrofitted trivially — expect a bifurcated installed base and a wave of "Rubin Ultra-ready" greenfield builds.
2. **Memory is the margin story.** HBM4 at $500–600+ per stack × 8 stacks (Rubin) or 12 stacks (MI455X) means $4–7k of memory per package, before HBM4E at 16-Hi. Non-Nvidia silicon competes on TCO, and HBM pricing parity (Samsung catching SK hynix) removes a cost lever hyperscaler ASICs quietly relied on. Watch Meta's LPDDR-based MTIA recommendation parts and Nvidia's GDDR7 CPX as memory-cost arbitrage.
3. **The "NVL144 → NVL72" rename hides a real change**: Nvidia now counts packages, so NVL576 no longer means one rack — it means an optically stitched multi-rack domain. Comparisons across GTC 2025 and 2026 slides are apples-to-oranges; Feynman "NVL1152" is 8 racks.
4. **Nvidia is disaggregating its own GPU.** CPX (prefill), Rubin (decode/training), LPU (low-latency FFN), Vera ETL256 (CPU racks): the product is no longer a GPU but a heterogeneous rack portfolio, which raises the software bar for every challenger to "match a *system*," not a chip.
5. **AMD's real ramp is probably Q2 2027**, but N2 compute dies plus 432 GB HBM4 make MI455X the first accelerator to beat Nvidia on memory capacity and node — the OpenAI 6 GW and Oracle 50k orders give it a guaranteed floor.
6. **Startup shipping claims are first-rack milestones.** Etched, SambaNova and Tenstorrent are all real in 2026, but gigawatt-scale is 2027+; Cerebras' $66B valuation prices in OpenAI-scale inference volume it has not yet shown outside G42.
7. **Google's TPU v8 split is the most important architectural signal**: the largest non-Nvidia fleet is abandoning a unified chip, mirroring Nvidia's CPX/LPU move — and Anthropic's 3.5 GW is the largest single non-Nvidia commitment anywhere.
8. **The capex is increasingly debt- and equity-funded.** With 32% of capex from incremental debt and negative FCF at three of five hyperscalers, 2027 guidance is the first real test of whether the curve plateaus; CoWoS at 120–140k wpm is roughly what $700–800B/yr can consume.

---

## Key numbers table

| Metric | Value | Status | Src |
|---|---|---|---|
| Nvidia Q2 FY27 data center revenue | $89.0B (+117% YoY); Q3 guide $108B | CONFIRMED | [1] |
| Rubin GPU | 50 PF NVFP4, 288 GB HBM4, 22 TB/s, 336B xtors, N3P | CONFIRMED | [2] |
| Vera Rubin NVL72 rack | 3.6 EF FP4, 20.7 TB HBM4, 1.6 PB/s, ~130 kW | CONFIRMED | [2][3] |
| Rubin CPX | 30 PF NVFP4, 128 GB GDDR7, end-2026 | CONFIRMED | [5] |
| Rubin Ultra / Kyber | 100 PF/pkg, 1 TB HBM4E, 576 dies, 15 EF, 600 kW, H2 2027 | REPORTED | [4][6] |
| Feynman | 2028, Rosa CPU, NVLink 8, all-CPO, CoPoS | REPORTED | [4][26][36] |
| Groq 3 LPU / LPX | 500 MB SRAM, 1.2 PF FP8, SF4; 256 LPUs/rack | CONFIRMED | [16][36] |
| AMD MI455X | 40.3 PF FP4, 432 GB HBM4, 23.3 TB/s, N2 dies | CONFIRMED | [8] |
| AMD Helios | 72 GPU, 2.9 EF, 31 TB HBM4, 1.7 PB/s; volume H2 2026 (AMD) / Q2 2027 (SemiAnalysis) | CONFIRMED / REPORTED | [7][9] |
| Google Ironwood | 4.6 PF FP8, 192 GB, 7.37 TB/s; 9,216 pod 42.5 EF; GA Apr 2026 | CONFIRMED | [10][39] |
| Google TPU 8t/8i | Split training/inference; Broadcom/MediaTek; 2026 vs 2027 GA disputed | REPORTED | [11][12] |
| AWS Trainium3 | 2.52 PF FP8, 144 GB HBM3E, 4.9 TB/s; 144-chip 362 PF | CONFIRMED | [13][41] |
| AWS Trainium4 | ≥6× FP4, NVLink Fusion | CONFIRMED (no date) | [13] |
| Microsoft Maia 200 | 10 PF FP4, 216 GB HBM3E, 750 W, 3nm | CONFIRMED | [14] |
| Meta MTIA | 300 in prod; 400 deploying; 450/500 in 2027; chip every ~6 mo | CONFIRMED | [15][42] |
| OpenAI–Broadcom | 10 GW, H2 2026–2029 | CONFIRMED | [44] |
| Cerebras IPO | $5.5B raised, $56.4B → ~$66B day one; 2025 rev $510M | CONFIRMED | [18][19] |
| Etched | $700M at $21B; first rack delivered | CONFIRMED / REPORTED | [21][47] |
| HBM4 12-Hi price | $500–600+/stack (+55–70% vs HBM3E) | REPORTED | [24] |
| HBM3E 2026 price change | ~+20% | REPORTED | [25] |
| SK hynix share of Nvidia HBM4 | ~67–70% | REPORTED | [22] |
| TSMC CoWoS | 75–80k wpm (2025) → 120–140k (end-2026); gap 20%→10% | REPORTED | [25][26] |
| TSMC A16 | Volume 2027 (slipped from 2026) | CONFIRMED | [28][29] |
| UALink 2.0 | Published 7 Apr 2026; 1.0 silicon labs H2 2026 | CONFIRMED | [49] |
| Nvidia CPO switches | Quantum-X early 2026; Spectrum-X H2 2026; SN6800 409.6 Tb/s | CONFIRMED | [2][52] |
| 800 VDC | MGX power racks H2 2026; full-scale with Kyber 2027; 80+ partners | CONFIRMED | [54][55] |
| Big-4 2026 capex | $600–650B (vs $388B 2025); ~$800B CY26 incl. leases w/ Oracle | CONFIRMED guidance | [30][31][32] |
| Frontier training compute growth | 5×/yr (Epoch, Feb 2026) | CONFIRMED (Epoch) | [33] |
| AI chip perf/$ growth | +49%/yr | CONFIRMED (Epoch) | [33] |
| Inference price decline (const. capability) | 9×–900×/yr; ~40×/yr GPT-4-level | CONFIRMED (Epoch) | [35] |

---

## Sources

1. Nvidia, "NVIDIA Announces Financial Results for Second Quarter Fiscal 2027," 26 Aug 2026 — https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
2. ServeTheHome, "NVIDIA Launches Next-Generation Rubin AI Compute Platform at CES 2026," Jan 2026 — https://www.servethehome.com/nvidia-launches-next-generation-rubin-ai-compute-platform-at-ces-2026/
3. Introl, "NVIDIA Vera Rubin: 600kW Racks by 2027," 25 Sep 2025 — https://introl.com/blog/nvidia-vera-rubin-gpu-600kw-racks-2027
4. Tom's Hardware, "Nvidia shows off Rubin Ultra with 600,000-Watt Kyber racks, coming in 2027," Mar 2025 — https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-rubin-ultra-with-600-000-watt-kyber-racks-and-infrastructure-coming-in-2027
5. Nvidia Newsroom, "NVIDIA Unveils Rubin CPX," 9 Sep 2025 — https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference
6. VRLA Tech, "NVIDIA GPU Roadmap 2026-2030: Rubin, Rubin Ultra, Feynman," 11 Jun 2026 — https://vrlatech.com/nvidia-gpu-roadmap-2026-2030/
7. ServeTheHome, "AMD Helios MI400 System Architecture at Hot Chips 2026," 24 Aug 2026 — https://www.servethehome.com/amd-helios-mi400-system-architecture-at-hot-chips-2026/
8. ServeTheHome, "AMD MI400 GPU at Hot Chips 2026," 24 Aug 2026 — https://www.servethehome.com/amd-mi400-gpu-at-hot-chips-2026/
9. The Next Platform, "AMD Says Helios Racks And MI400 Series GPUs On Track For 2H 2026," 23 Feb 2026 — https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199
10. TNW, "Google launches Ironwood TPU and previews eighth-gen split," 22 Apr 2026 — https://thenextweb.com/news/google-ironwood-tpu-inference-cloud-next
11. HyperFRAME Research, "Google Cloud Next 2026: TPU 8t and 8i," 22 Apr 2026 — https://hyperframeresearch.com/2026/04/22/google-cloud-next-2026-google-cloud-bifurcates-the-ai-future-specialized-tpu-8t-and-8i-architectures-signal-the-end-of-general-purpose-silicon/
12. Doolpa, "Google Ironwood GA, TPU 8 split," Apr 2026 — https://doolpa.com/news/google-ironwood-tpu-general-availability-tpu-8-split-cloud-next-april-2026
13. Amazon, "Trainium3 UltraServers now available," Dec 2025 — https://www.aboutamazon.com/news/aws/trainium-3-ultraserver-faster-ai-training-lower-cost
14. Microsoft, "Maia 200: The AI accelerator built for inference," 26 Jan 2026 — https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/
15. Meta, "Expanding Meta's Custom Silicon to Power Our AI Workloads," 11 Mar 2026 — https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/
16. Techzine, "Nvidia's Groq 3 LPU targets agentic AI inference at GTC 2026," 17 Mar 2026 — https://www.techzine.eu/news/infrastructure/139653/nvidias-groq-3-lpu-targets-agentic-ai-inference-at-gtc-2026/
17. Tom's Hardware, "Hot Chips 2026: Nvidia presents Groq 3 LPX architecture… LP30-based rack already in production," Aug 2026 — https://www.tomshardware.com/tech-industry/semiconductors/nvidia-presents-groq-3-lpx-architecture-and-unveils-its-first-third-party-inference-benchmark
18. TechCrunch, "Cerebras raises $5.5B, then stock pops 108%," 14 May 2026 — https://techcrunch.com/2026/05/14/cerebras-raises-5-5b-kicking-off-2026s-ipo-season-with-a-bang/
19. Cerebras, "Cerebras Systems Announces Pricing of Initial Public Offering," 13 May 2026 — https://www.cerebras.ai/press-release/cerebras-systems-announces-pricing-of-initial-public-offering
20. Chipstrat (Austin Lyons), "The Next Trillion-Dollar Chip Company," 15 Jul 2026 — https://www.chipstrat.com/p/the-next-trillion-dollar-chip-company
21. New Market Pitch, "AI Chip Market Funding News (September 2026)" — https://newmarketpitch.com/blogs/news/ai-chip-funding-news
22. TrendForce, "SK hynix Reportedly to Supply About Two-Thirds of NVIDIA HBM4," 28 Jan 2026 — https://www.trendforce.com/news/2026/01/28/news-sk-hynix-reportedly-to-supply-about-two-thirds-of-nvidia-hbm4-samsung-targets-early-delivery/
23. Malay Mail/AFP, "Samsung launches mass production of HBM4," 12 Feb 2026 — https://www.malaymail.com/amp/news/money/2026/02/12/samsung-launches-mass-production-of-industryleading-hbm4-ai-memory-chips-as-demand-surges/208989
24. Silicon Analysts, "HBM Pricing & Market Share (2026)," rev. 14 Aug 2026 — https://siliconanalysts.com/tools/hbm-analysis
25. TrendForce, "TSMC's CoWoS-L/S Reportedly Fully Booked," 8 Dec 2025 — https://www.trendforce.com/news/2025/12/08/news-tsmcs-cowos-l-s-reportedly-fully-booked-osat-partners-step-up-with-ases-cowop-in-focus/
26. TrendForce, "TSMC CoWoS Supply-Demand Gap Seen Narrowing from 20% to 10% by End-2026," 15 Jun 2026 — https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/
27. Introl, "South Korea's HBM4 Moment," 7 Jan 2026 — https://introl.com/blog/south-korea-hbm4-stargate-memory-supercycle-2026
28. TrendForce, "TSMC Latest Roadmap: A12, A13 for 2029 Without High-NA EUV; A16 Delayed to 2027," 23 Apr 2026 — https://www.trendforce.com/news/2026/04/23/news-tsmc-unveils-latest-roadmap-a12-a13-set-for-2029-without-high-na-euv-a16-volume-production-delayed-to-2027/
29. Tom's Hardware, "TSMC begins quietly volume production of 2nm-class chips," Q4 2025 — https://www.tomshardware.com/tech-industry/semiconductors/tsmc-begins-quietly-volume-production-of-2nm-class-chips-first-gaa-transistor-for-tsmc-claims-up-to-15-percent-improvement-at-iso-power
30. Data Center Richness, "Hyperscalers Plan $630 Billion in 2026 CapEx," 6 Feb 2026 — https://datacenterrichness.substack.com/p/hyperscalers-plan-630-billion-in
31. Futurum, "AI Capex 2026: The $690B Infrastructure Sprint," 12 Feb 2026 — https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/
32. FactSet, "Hyperscalers Tap External Financing as AI Capex Outruns Cash Flow," 23 Jul 2026 — https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow
33. Epoch AI, "Trends in Artificial Intelligence," updated 5 Feb 2026 — https://epoch.ai/trends
34. Epoch AI, "Training compute costs are doubling every eight months," data to Nov 2025 — https://epoch.ai/data-insights/cost-trend-large-scale
35. Epoch AI, "LLM inference price trends," 12 Mar 2025 — https://epoch.ai/data-insights/llm-inference-price-trends
36. SemiAnalysis, "GTC 2026 – The Inference Kingdom Expands," 24 Mar 2026 — https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands
37. Introl, "Marvell's $540M XConn Acquisition Signals AI Interconnect," 2026 — https://introl.com/blog/marvell-xconn-acquisition-cxl-ualink-infrastructure-2026
38. Tech Insider, "AMD Advancing AI 2026: Helios Rack Hits $5.25M," 2026 — https://tech-insider.org/amd-advancing-ai-2026/
39. TrendForce, "Google Unveils 7th-Gen TPU Ironwood with 9,216-Chip Superpod," 7 Nov 2025 — https://www.trendforce.com/news/2025/11/07/news-google-unveils-7th-gen-tpu-ironwood-with-9216-chip-superpod-taking-aim-at-nvidia/
40. SemiAnalysis, "Google TPUv7: The 900lb Gorilla In the Room," 28 Nov 2025 — https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the
41. SemiAnalysis, "AWS Trainium3 Deep Dive," 4 Dec 2025 — https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential
42. Meta Engineering, "MTIA 300: Meta's First Training Chip with Built-in NICs," 24 Aug 2026 — https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
43. Electronics Weekly, "Meta prepares to fab its third custom datacentre chip," Jul 2026 — https://www.electronicsweekly.com/news/business/meta-2026-07/
44. Broadcom, "OpenAI and Broadcom Announce Strategic Collaboration to Deploy 10 Gigawatts," 13 Oct 2025 — https://investors.broadcom.com/news-releases/news-release-details/openai-and-broadcom-announce-strategic-collaboration-deploy-10
45. Michael Bommarito wiki, "OpenAI–Broadcom custom AI chip partnership," updated 24 Aug 2026 — https://michaelbommarito.com/wiki/ai-hardware/openai-broadcom-partnership/
46. AIbase, "OpenAI and Broadcom Collaborate on 10GW Custom Chips," 2026 — https://news.aibase.com/news/24040
47. Etched, company site (Sohu status, funding) — https://www.etched.com/
48. Lightmatter, company site (Passage M1000/L200, NVLink Fusion) — https://lightmatter.co/
49. The Register, "UALink delivers 2.0 spec before v1.0 silicon ships," 7 Apr 2026 — https://www.theregister.com/on-prem/2026/04/07/ualink-delivers-20-spec-before-v-10-silicon-ships/5228485
50. Wikipedia, "UALink" — https://en.wikipedia.org/wiki/UALink
51. Ultra Ethernet Consortium (spec 1.0.3, Aug 2026) — https://ultraethernet.org/
52. Next Waves Insight, "Photonic Compute Hits Production: Lightmatter, Ayar Labs, and CPO Are Now Shipping," 2026 — https://nextwavesinsight.com/photonic-compute-production-lightmatter-ayar-labs/
53. Contrary Research, "Ayar Labs Business Breakdown" — https://research.contrary.com/company/ayar-labs
54. Nvidia Technical Blog, "Building the 800 VDC Ecosystem for Efficient, Scalable AI Factories," 13 Oct 2025 — https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/
55. Wccftech, "NVIDIA Ditches AC Power For 800 VDC AI Factories… Backed By Microsoft, Google and 80 Ecosystem Firms For 2H 2026" — https://wccftech.com/nvidia-800-vdc-platforms-break-past-traditional-power-distros-to-scale-up-performance/
56. Epoch AI, "Can AI scaling continue through 2030?," 20 Aug 2024 — https://epoch.ai/blog/can-ai-scaling-continue-through-2030
57. Deluair, "Frontier AI training cost trajectory 2026" — https://deluair.com/consultancy/insights/frontier-ai-training-cost-2026
58. Introl, "Inference Unit Economics: The True Cost Per Million Tokens" — https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide
