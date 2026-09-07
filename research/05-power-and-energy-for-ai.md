# Powering AI: The Electrical Engineering and Energy Side (as of September 2026)

*Research brief compiled 2026-09-07. Claims are tagged CONFIRMED (primary source or multiple independent reports), REPORTED (single credible outlet or company claim not independently verified), or SPECULATION (forecast, analyst opinion, or this author's inference).*

---

## TL;DR

- **Gigawatt campuses are real, but "GW" is mostly nameplate.** Only a handful of sites draw ~1 GW today: xAI Colossus (Memphis/Southaven, ~2 GW nameplate), Amazon Rainier (New Carlisle, ~1.2 GW operational, 2.25 GW at build-out), Microsoft Fairwater Atlanta (340 MW → 700+ MW by end-2026), Meta Prometheus (Ohio, ~1 GW, 2026). Stargate Abilene, the most-hyped, was at ~300 MW in April 2026 and its planned 2 GW expansion was cancelled [1][2].
- **The bottleneck has moved from chips to electrons and copper.** Gas-turbine backlogs: GE Vernova 116 GW (booking 2031 slots), Siemens Energy 69 GW (3+ year lead times). Power transformers 128 weeks; GSUs 144 weeks; some units 4 years [26][28][48].
- **Forecasts are enormous and probably inflated.** Grid Strategies: +166 GW US peak by 2030, ~90 GW from data centers, but utilities may overstate by 40% [18]. ERCOT's large-load queue hit 474 GW (5x its record peak) before Gov. Abbott paused approvals in August 2026 [25].
- **Gas won the 2025-2028 window.** Nearly every new GW-class campus (Stargate, Colossus, Hyperion, Prometheus) uses on-site or dedicated gas; fuel cells (Bloom: 2.8 GW Oracle master agreement) are the fast-deploy alternative [30]. Nuclear is 2027 (Crane restart) at the earliest and 2030-2035 for SMRs.
- **Inside the building, the architecture is being rewritten:** 800 VDC distribution (Nvidia Kyber, 2027), solid-state transformers stepping 34.5 kV AC directly to 800 V DC, GaN/SiC power stages at 97-98% efficiency, 140-600 kW liquid-cooled racks [41][42][44].
- **Political backlash is now the binding constraint in several states.** PJM capacity prices went from $29 to $329/MW-day in three auctions; ~64% of the jump attributed to data centers; 500+ local bans; Texas, Michigan, Pennsylvania candidates of both parties endorsing moratoria [23][55][59].

---

## 1. The gigawatt campuses: what is actually energized

| Campus | Owner / tenant | Nameplate plan | Operating (latest) | Power source | Status tag |
|---|---|---|---|---|---|
| Stargate Abilene, TX | Oracle/Crusoe for OpenAI | 1.2 GW (2.1 GW expansion cancelled) | ~300 MW (Apr 2026); 4 of 8 buildings live; buildings 3-4 slipped 9+ months | On-site gas turbines + grid | CONFIRMED partial; expansion cancellation REPORTED [1][2] |
| Stargate other US sites (Shackelford TX 2.0 GW, Doña Ana NM 2.2 GW, Milam TX 1.2 GW, Port Washington WI 1.3 GW, Saline MI 1.4 GW, Lordstown OH <0.3 GW) | Vantage, STACK, SB Energy, Related | ~9 GW total | 0 MW; all target Q4 2028; Doña Ana pushed to 2029 after gas pipeline permit blocked | Mostly on-site gas microgrids; WI/MI grid | REPORTED [1][21] |
| xAI Colossus 1+2, Memphis TN / Southaven MS | xAI | 2 GW across three buildings, 555k GPUs, ~$18B in GPUs | ~1+ GW; ramping through Q3 2026 | 59 unpermitted gas turbines (up to 495 MW) at Southaven; Solaris JV turbines targeting 1.1 GW by Q2 2027; Tesla Megapacks (~$1B cumulative); TVA/MLGW grid | Capacity REPORTED; turbine permit violations REPORTED (SELC/NAACP litigation) [3][4][5] |
| Meta Prometheus, New Albany OH | Meta | ~1 GW | Coming online 2026 | Behind-the-meter gas (Williams) under "tents"; nuclear later via Vistra/Oklo/TerraPower | CONFIRMED plan [7][8] |
| Meta Hyperion, Richland Parish LA | Meta (20%) / Blue Owl (80%) JV | 1.5 GW end-2027 → 2 GW → 5 GW stretch; $28.8B phase-1 dev cost | Under construction | Entergy: 3 CCGTs (2.26 GW, $3.24B, COD Dec 2028-Jun 2029) approved; "Project Evest" 5.3 GW CCGT + 600 MW BESS + 4 GW renewables ($12.9B) filed Mar 2026, LPSC vote Nov 2026 | CONFIRMED (regulatory filings) [6] |
| Microsoft Fairwater Atlanta, GA | Microsoft | 700+ MW IT end-2026; 1.5 GW full build | 340 MW (Oct 2025), 150k+ GB200s | Grid-only: dual 230 kV feeds from Georgia Power, **no UPS, no gensets** | CONFIRMED [9][10] |
| Microsoft Fairwater Wisconsin | Microsoft | $7.3B two-building campus | Phase 1 ramping 2026 | Grid (We Energies) | REPORTED [11] |
| Amazon Project Rainier, New Carlisle IN | AWS for Anthropic | 2.25 GW grid draw, 32 buildings, $11B+ | ~1.18 GW (two 590 MW phases, Jan & Dec 2025); 767 MW expansion late 2027 | Grid (I&M/AEP, PJM); $185M 345 kV substations for 1.1 GW by Dec 2026; 878 diesel gensets (2.4 GW standby) | CONFIRMED [12][13] |
| Google (Armstrong/Haskell TX, Pine Island MN, Jackson County AL) | Google | $40B Texas program | Phased | Co-located AES generation (TX); Xcel 1.9 GW wind/solar/storage (MN); 1 GW demand response across 5 utilities | CONFIRMED [14][66] |

Two engineering contrasts stand out. **Microsoft Fairwater Atlanta dropped UPS and diesel entirely**, arguing that "4×9 availability at 3×9 cost" is achievable by treating a dual-fed 230 kV grid connection as the resiliency layer; 140 kW/rack direct-to-chip liquid cooling with a closed loop (600k gallons one-time fill per building) [9][10]. **Amazon Rainier went the opposite way**: air-cooled, chiller-free, PUE 1.15, but with 878 × 2.75 MW diesel generators as backup [12]. Both are grid-fed; the gas-first sites (Stargate, Colossus, Hyperion) are the ones with the slipped schedules and litigation.

Cost of speed: Distilled/Cleanview estimates Crusoe's behind-the-meter Abilene model at ~$19.2B per GW all-in versus ~$9.5B per GW for a grid-connected Texas campus, a >100% premium [2]. (REPORTED; single analysis.)

---

## 2. Load growth forecasts: the numbers and their reliability

**Global (IEA).** Data centre electricity demand grew ~17% in 2025 to roughly 485 TWh, and IEA's updated projection is ~950 TWh by 2030 (~3% of global electricity). AI-focused data centres grew ~50% in 2025 and are expected to triple by 2030. Data centres are expected to account for roughly half of *US* demand growth to 2030 [15][16]. CONFIRMED (IEA).

**US (LBNL, Dec 2024).** 176 TWh in 2023 (4.4% of US consumption) → 325-580 TWh in 2028 (6.7-12%) [17]. CONFIRMED but aging; the 2024 report predates the GW-campus wave.

**US peak (Grid Strategies, Nov 2025).** Utility-filed five-year forecasts sum to +166 GW of peak by 2030, six times the 2022 forecast, with ~90 GW (55%) attributed to data centers. Grid Strategies itself flags that utilities may be overstating data center demand by up to 40% because developers shop identical projects to multiple utilities and use "unrealistically high load factors" [18][19][20]. CONFIRMED numbers; the 40% caveat is the report's own.

**PJM.** Summer peak from ~154 GW (2025) to ~210 GW (2036); nearly all of the +5.25 GW increase in the 2027/28 forecast is data centers; a 15 GW capacity shortfall possible by 2030 [24][55].

**Delivered capacity (SemiAnalysis).** ~20 GW of new US data center capacity energized in 2026, ~30 GW expected in 2027. SemiAnalysis rebuts the Bloomberg/Sightline claim that only ~5 GW of 12 GW planned for 2026 was under construction, saying its tracked hyperscaler forecasts moved <1% in six months and that real projects had prepaid for equipment slots; the "delays" were phantom announcements never funded [21][22]. REPORTED, competing analyses. Both sides agree on specific slips: Nebius NJ (4 → 11 months), Oracle/STACK NM (2029).

**Reconciling:** 20-30 GW/year of *delivered* IT capacity is consistent with ~50-60 GW of new US peak by 2030, i.e., well under the 90-166 GW utility-forecast range. The forecast gap is the "phantom load" problem, and it matters because utilities are building gas plants and transmission against the high number.

---

## 3. Interconnection queues and grid delays

- US generation/storage interconnection queues held ~2,600 GW in early 2026; PJM+ERCOT alone >300 GW across ~1,500 projects. Renewables and storage are 77% of PJM's queue and 87% of ERCOT's; gas projects move faster, and gas entries to ERCOT's queue rose ~150% month-over-month after the One Big Beautiful Bill Act cut renewable credits [24]. CONFIRMED (Carbon Direct, May 2026).
- Large-load side: **ERCOT received 198 GW of large-load applications in Q1 2026 alone**; the queue reached ~474 GW, ~90% data centers, >5x Texas' record peak. On Aug 3-5, 2026, Gov. Abbott directed a pause of ERCOT's "Batch Zero" review pending audits of on-site generation, water, and subsidies; duration indefinite [25]. CONFIRMED.
- Time-to-power: AI projects entering service in 2025 averaged >7 years from queue entry, ~3 years to an interconnection agreement and ~4 years to energization; active projects in load-growth zones face 3-4 year waits [24][67]. REPORTED.
- The constraint has shifted from queue processing to physical delivery: substations, 345/500 kV lines, and equipment. MISO's Louisiana transmission package for Hyperion alone is $3.4B (three 500 kV lines at $0.5-1.2B each) [6].

---

## 4. Behind-the-meter gas: turbines, fuel cells, and the shortage

**Turbine OEM backlogs (CONFIRMED, company filings):**
- **GE Vernova**, Q2 2026: gas turbine backlog + slot reservations 116 GW (53 GW firm backlog + 63 GW reservations), guided to 125 GW by year-end; taking reservations for 2031 deliveries; ~20% of customers are data centers; shipping ~20 GW/yr, targeting 30 GW/yr by 2030. Indicative pricing ~$790/kW heavy-duty, ~$950/kW HA combined-cycle, ~$1,800/kW aeroderivative. Electrification orders for data centers >$5B YTD [26][27].
- **Siemens Energy**, fiscal Q3 (Jun 2026): 69 GW backlog, 15 GW new orders in the quarter, 6 GW shipped, lead times 3+ years, "booked out" to FY2028 with 2029-2030 filling. Expanding medium turbines from 80 to ~100 units/yr by 2028 and large from 35 to 50 units in 2027. Grid Technologies (transformers/switchgear) backlog €51B. CEO Bruch: addressable market could hit 120 GW/yr, half in the US; a quarter of turbines sold now go to data centers [28][29].
- Mitsubishi Power is the third major supplier; all three combined can ship roughly 60-70 GW/yr globally against demand estimates of 100-120 GW/yr. SPECULATION on exact gap; the direction is CONFIRMED by both OEMs' expansion plans.

**Consequences:** Aeroderivatives and reciprocating engines (Solaris, VoltaGrid, Caterpillar) fill the gap at higher $/kW and lower efficiency; xAI's Southaven site is the extreme case, 59 turbines (up to 495 MW) operated without Clean Air Act permits, double what xAI disclosed, now in NAACP/SELC litigation [4][5][69]. REPORTED.

**Fuel cells as the "55-day" alternative (CONFIRMED, press releases):** Bloom Energy signed a master agreement with Oracle for up to 2.8 GW of solid-oxide fuel cells (1.2 GW contracted), delivered one system in 55 days; Brookfield committed up to $5B to deploy Bloom SOFCs at AI sites; AEP signed a $2.65B/1 GW offtake; Bloom is doubling manufacturing from 1 to 2 GW/yr by end-2026 [30][31]. Project Jupiter (NM) is planned around ~2.45 GW of fuel cells after its gas pipeline was blocked [2]. Fuel cells avoid NOx permitting and cooling water but run ~$3,000-4,000/kW installed and still burn gas (SPECULATION on price; Bloom does not publish).

---

## 5. Nuclear

**Restarts (CONFIRMED):**
- **Crane Clean Energy Center (TMI-1)**, 835 MW, Constellation → Microsoft 20-year PPA. $1B DOE loan (Nov 2025). FERC transmission waiver June 1, 2026; NRC milestones cleared July 2026; targeting mid/H2 2027, a year ahead of the original 2028. 600 permanent staff. Local opposition (Three Mile Island Alert) litigating water withdrawals; "almost all of 440 public comments" opposed [32][33][34].
- Palisades (MI) and Duane Arnold (IA, NextEra, ~615 MW for Google) are the other restarts; Duane Arnold is targeted ~2028-2029. REPORTED.

**Existing-fleet PPAs (CONFIRMED):** Meta-Vistra 2.1 GW (Perry, Davis-Besse) plus 433 MW uprates; Meta-Constellation (Clinton); Amazon-Talen (Susquehanna, 1.92 GW); Microsoft-Constellation. These move existing electrons to data centers rather than adding supply, which is why they irritate ratepayer advocates.

**SMR / advanced reactor deals (CONFIRMED signed; timelines REPORTED/SPECULATION):**

| Buyer | Developer | Capacity | Site | First power target |
|---|---|---|---|---|
| Meta | Oklo | 1.2 GW (16+ × 75 MW Aurora) | Pike County, OH | "as early as 2030" |
| Meta | TerraPower | 690 MW firm, rights to 2.8 GW total (8 Natrium, 345 MW each + 1.2 GW/5h storage) | Wyoming | "as early as 2032" |
| Google | Kairos Power | 500 MW fleet; Hermes 2 50 MW via TVA | TN | 2030 |
| Google | Elementl Power | 3 × 600 MW sites | TBD | 2030s |
| Amazon | X-energy / Energy Northwest | 960 MW (12 × Xe-100) | WA | 2030s |
| Amazon | Dominion | SMR at North Anna | VA | TBD |
| Google | Commonwealth Fusion (ARC) | 200 MW | Chesterfield, VA | early 2030s |

SMR Intel counts ~9.8 GW across 13 hyperscaler nuclear deals; exactly one (Crane) is under construction [35][36][7]. TerraPower holds an NRC construction permit for Kemmerer; Kairos is building Hermes 1/2; Oklo has no license yet. Realistic first SMR electrons for an AI campus: 2030-2032, i.e., after the current capex cycle. Nuclear is a 2030s answer to a 2026 problem.

---

## 6. Fusion timelines

- **Helion / Microsoft (Orion, 50 MW, Malaga WA, 2028 PPA).** Ground broken July 2025; assembly building complete, generator-building earthwork underway June 2026; first fusion company with state licenses to build a plant; Polaris reached 150M °C (75% of commercial target) in Feb 2026; $465M Series G at $15.5B valuation (June 2026) [37][38]. Status: CONFIRMED construction; 2028 power delivery is SPECULATION with low probability by any external physics benchmark (no net electricity has been demonstrated).
- **Commonwealth Fusion SPARC.** First of 18 HTS TF magnets installed Jan 2026; first plasma slipped to late 2026/2027; Q>1 targeted 2027; ARC 400 MWe in Virginia (Dominion) "early 2030s." Google has a 200 MW ARC offtake [39][40]. CONFIRMED hardware progress; dates REPORTED.
- Bottom line: fusion contributes 0 MW to AI before 2030. Its relevance now is as a capital sink and an option on the 2035+ mix.

---

## 7. Batteries, solar, and load flexibility

- **On-site storage for training transients.** GPU clusters swing hundreds of MW in milliseconds between all-reduce and compute phases. xAI has bought ~$1B of Tesla Megapacks; SpaceX (now merged with xAI operations) bought $329M in H1 2026 [3][64]. Nvidia's Vera Rubin reference design pushes energy storage into rack-level shelves (Delta's 660 kW in-row power rack includes 480 kW of battery backup) to shave grid-visible transients [41]. CONFIRMED products; deployed scale REPORTED.
- **Grid-scale.** Google/Xcel Pine Island: 1.4 GW wind + 200 MW solar + 300 MW long-duration storage bundled with the data center [66]. Meta's Evest filing pairs 5.3 GW gas with 600 MW BESS and 4 GW renewables [6]. Tesla's Brookshire TX Megapack plant (late 2026) adds US supply [64].
- **Demand response is the cheapest new "capacity."** Google has 1 GW of contractual demand response with I&M, TVA, Entergy Arkansas, Minnesota Power, and DTE, curtailing or shifting ML workloads to get faster interconnection [14]. Duke Nicholas Institute: 76 GW of new load could be absorbed if it curtails 0.25% of hours; 1-2% peak reduction cuts rates 0.5-2.8% [63]. EPRI DCFlex expanded to nine demo sites; a March 2026 UK test had a 96-GPU Blackwell Ultra cluster drop power 30% in <40 s across 22 dispatch events; the 96 MW Emerald AI "Aurora" flex-designed site in Manassas VA targets late 2026 [62]. CONFIRMED demos; scaling to GW-class training runs unproven.
- Tesla/Sunrun/Renew Home framework claims 16 GW of aggregated home battery + thermostat capacity marketed at data-center-driven markets [65]. REPORTED; largely a VPP relabel.

---

## 8. Transformers, switchgear, and the "boring" shortage

Wood Mackenzie / POWER / pv magazine data (CONFIRMED surveys, mid-2025 to mid-2026):
- Power transformers: **128 weeks** average; GSUs **144 weeks**; some large units 3-4 years. Prices since 2019: power transformers +77%, GSUs +45%, distribution up to +95%. 2025 shortfall: 30% power, 10% distribution. Demand since 2019: GSUs +274%, substation transformers +116% [48][49].
- Switchgear: 40% shortfall in HV switchgear, 25% breakers, 20% MV switchgear (Reuters/WoodMac 2025). Practical 2026 lead times: MV switchgear 52-104 weeks; HV breakers ~125 weeks; 25-50 MVA substation transformers 85-110 weeks; >3 MW diesel gensets 90-110 weeks; large UPS 40-80 weeks [48][50].
- Supply response: ~$1.8B of North American expansions (Hitachi Energy $1B+ South Boston VA, largest US plant by 2028; Siemens Energy $150M Charlotte, early 2027; Eaton $340M SC, 2027; Prolec GE $300M+). Siemens Energy Grid Technologies targeting +50% capacity by 2030 [28][48]. Headwinds: 50% copper tariffs, Section 232 steel, GOES electrical steel scarcity, FEOC rules on Chinese content.
- Dissent: some brokers say standard substation units can be had in 12-14 months and the "shortage" is partly hoarding and speculative orders [48]. SemiAnalysis makes the same point: real projects prepaid their slots [21].

---

## 9. Inside the building: 800 VDC, solid-state transformers, wide-bandgap silicon, liquid cooling

**Why 800 VDC (CONFIRMED, Nvidia/OCP/IEEE):** A 1 MW rack at 54 V DC would need ~200 kg of copper busbar per rack; 415/480 VAC → 54 V multi-stage conversion loses ~5% end-to-end. Moving to 800 VDC distribution cuts current roughly in half vs. 400 V, carries ~85% more power per conductor than 415 VAC, reduces copper ~45%, and improves end-to-end efficiency ~5% [42][43]. Nvidia's Kyber rack (576 Rubin Ultra GPUs, ~600 kW+; 1 MW-class successors) ships in 2027 with 800 VDC as the reference [41][43].

**Ecosystem (CONFIRMED at GTC 2026, March):** 80+ companies. Silicon: Infineon, Navitas, onsemi, STMicro, TI, ROHM, EPC, Innoscience, MPS, Renesas, Power Integrations. Power systems: ABB, Eaton, GE Vernova, Hitachi Energy, Mitsubishi Electric, Schneider, Siemens, Vertiv, Delta, Heron Power. Operators: Microsoft, Google (via OCP), CoreWeave, Oracle, Lambda, Nebius, Together [41][44]. Eaton's "Beam Rubin DSX" and Vertiv's 800 VDC line ship H2 2026; Delta's 660 kW in-row power racks are released [42].

**Solid-state transformers (REPORTED products, early deployment):** The key new component converts 34.5 kV or 13.8 kV AC directly to 800 V DC in one SiC-based stage, eliminating the LV transformer + rectifier chain. Heron Power (Heron Link, $140M Series B, Feb 2026, a16z/Breakthrough), Eaton (via Resilient Power acquisition, Aug 2025), DG Matrix (named MGX reference SST), Delta, ABB, Siemens, Hitachi Energy, and a Navitas/EPFL demo are all in the race; SolarEdge targets 99% efficiency [46][47][41]. Open issues: DC arc-fault protection, standards (OCP/ODCC/IEC), galvanic isolation, and MTBF of 3.3 kV SiC at scale. SPECULATION: SSTs will be in single-digit percent of 2027 deployments; the 2026-2027 mainstream is conventional MV transformers feeding 800 VDC rectifier cabinets.

**SiC and GaN (CONFIRMED product announcements):** GaN dominates 800 V primary stages (650 V-rated devices in three-level topologies); SiC (1,200-3,300 V) takes the MV/SST front end. Navitas' 800 V → 50 V 10 kW platform hits 98.5% peak; its 800 V → 6 V single-stage board hits 96.5% at 2,100 W/in³, skipping the 48 V bus entirely; partner boards reach 98.2% at 2,500 W/in³ for 800 V → 12 V [45][41]. The direct-to-6 V shift matters because Rubin-class packages want 2,000-3,000 A delivered inside a ~30×30 mm footprint.

**Liquid cooling (CONFIRMED):** GB300 NVL72 ~130-163 kW/rack; Vera Rubin NVL72/NVL144 ~250-370 kW (2026); Rubin Ultra NVL576/Kyber 600 kW+ (2027). Direct-to-chip with CDUs is the baseline; Nvidia specifies 45 °C warm-water inlet to eliminate chillers; Fairwater runs closed loops at 140 kW/rack; six Stargate sites use closed-loop to avoid evaporative water [51][52][9][1]. Winter-storm damage to Abilene's liquid-cooling gear was cited in the expansion cancellation [1].

---

## 10. HVDC and transmission

- HVDC's data-center relevance is indirect: it is the only practical way to move multi-GW blocks of remote generation (SunZia 3.5 GW wind, in service 2026; Champlain Hudson 1.25 GW hydro to NYC, 2026) into load pockets, and city-center infeeds like Hitachi/Adani's Mumbai link (Mar 2026) show the template for dense-load regions [53][54]. Hitachi Energy is expanding US HVDC and transformer manufacturing ($1B+) and has announced data-center-specific "energy park" collaborations (X Labs, OpenAI) [48][53]. CONFIRMED projects; a US "HVDC-to-campus" link remains SPECULATION.
- HVDC converter valves compete with SSTs and EV inverters for the same high-voltage SiC/IGBT supply; no public shortage figure exists, but lead times track the transformer market (48-60 months for the largest units, per Hitachi commentary) [53].

---

## 11. Electricity prices and political backlash

**PJM (CONFIRMED, auction reports):** Capacity clearing price $28.92/MW-day (2024/25) → ~$270 (2025/26) → $329.17 (2026/27) → $333.44 (2027/28, at the FERC-negotiated cap; would have cleared 60% higher, ~$531, uncapped). Reserve margin 14.8% vs. 20% target, the lowest ever. Total 2025/26 capacity payments ~$16B across 67M people. The market monitor attributes ~63-64% of the price increase (~$9.3B) to data centers [55][56][57][58]. SemiAnalysis models a ~15% household bill increase in PJM for 2026 vs. a no-AI counterfactual, ~$25-30/month from capacity alone; ERCOT, by contrast, saw only 11-17% forward price increases with a comparable buildout because it has no capacity market [23]. Pepco DC bills rose ~$21/month in June 2025; some analysts project +$70/month by 2028 [57]. The 2028/29 PJM auction (July 2026) ran without the cap; results not captured here.

**Politics (CONFIRMED, multiple outlets):** 300+ state bills in 30+ states in the first six weeks of 2026 (large-load tariffs in 18+ states, moratoria in 11, tax-credit rollbacks in VA/GA/OK/IN) [60]. Maine's statewide moratorium passed the legislature and was vetoed (Apr 2026) [61]. Texas paused approvals (Aug 2026) [25]. TIME reports 500+ local bans, 150 in August alone, and a 12-point swing against data centers Mar-Jul 2026; Republican candidates in TX (Paxton), MI (Rogers), PA (Garrity), FL (Donalds), OH (Husted, Ramaswamy) have adopted moratorium or "pay your own power" positions [59]. Louisiana's Hyperion approval passed with a dissent over no-bid gas plants and Walmart's estimate that 48% of the 30-year revenue requirement lands on other ratepayers if Meta exits at year 15 [6].

---

## 12. What people are underestimating (analysis)

*Labeled analysis; these are inferences, not reported facts.*

1. **The load-factor lie.** Utilities model data centers at 85-95% load factors; training clusters actually swing 30-50% of nameplate on sub-second timescales, and inference fleets follow diurnal demand. Rack-level storage (Delta, Nvidia's reference) and contractual DR (Google's 1 GW) mean the *grid-visible* peak per GW of IT will fall through 2027. Utilities that build 2028 gas plants to the 2025 forecast will over-build; that is a ratepayer risk, not a hyperscaler risk, because tariffs like Entergy's 70 MW/80% floors only cover part of the exposure.

2. **The gas premium is bigger than the schedule gain.** Behind-the-meter gas costs roughly 2x per GW versus grid-fed (Crusoe/Abilene $19B/GW vs. $9.5B/GW), needs Clean Air Act permits that are now being litigated (xAI), and locks in $/MWh 2-3x a nuclear PPA for 20 years. The sites that shipped fastest and cleanest in 2025-26 (Fairwater Atlanta, Rainier) were grid-fed in utility territories that had spare 230/345 kV headroom. "Bring your own power" is a Texas/Louisiana/Mississippi strategy, not a universal one.

3. **800 VDC is a copper story before it is an efficiency story.** The 5% efficiency gain is real but secondary. At 1 MW/rack, 54 V busbars are physically impossible; 800 VDC halves conductor mass and lets a GW campus save on the order of 100+ tonnes of copper amid 50% tariffs. The unresolved part is protection: DC arc faults at 800 V do not self-extinguish, and there is no mature standard for DC breakers at rack scale. Expect incidents in 2027-28 deployments.

4. **Solid-state transformers will be gated by SiC yield, not by demand.** Every SST needs dozens of 3.3 kV SiC MOSFETs; that die supply is shared with HVDC valves, EV traction, and grid-forming inverters. A 1 GW campus on SSTs is a very large fraction of one year's global HV-SiC output. The vendors listing "seamless Nvidia compatibility" have mostly shipped pilots.

5. **Reserve margin, not energy, is the near-term PJM problem.** PJM's 14.8% reserve margin with data centers at ~40% of capacity cost means one bad summer week (or one large plant retirement) turns a price problem into a reliability event. The politically obvious fix, forcing large loads to be interruptible or to bring capacity, is exactly what the DCFlex/Google DR work enables; the industry will adopt flexibility because regulators will require it, not because it is cheaper.

6. **The nuclear deals are mostly option contracts.** 9.8 GW of "committed" advanced nuclear has one project under construction (Crane) and zero licensed SMRs for AI. The realistic 2026-2030 nuclear contribution is ~3-4 GW of restarts and uprates (Crane, Palisades, Duane Arnold, Vistra uprates). SMR PPAs matter for 2032+ and for financing the developers, not for the current capex cycle.

7. **Forecast inflation and politics compound.** The 474 GW ERCOT queue and 166 GW Grid Strategies number are the numbers voters hear. They drive both over-building (which raises rates) and moratoria (which delay real projects). The industry has an incentive to publish smaller, firmer numbers and to accept take-or-pay tariffs; the first hyperscaler to do so publicly will get faster interconnects.

8. **Turbine backlogs will unwind partly through cancellation.** GE Vernova's 63 GW of "slot reservations" are deposits, not firm orders. If 2027-28 demand disappoints (AI capex correction, moratoria), reservations get sold to utilities and the 2031 queue shortens fast. The 2026 backlog is a ceiling on ambition, not a floor on deliveries.

---

## 13. Key numbers table

| Metric | Value | Date | Tag | Source |
|---|---|---|---|---|
| Global data centre electricity | ~485 TWh (2025) → ~950 TWh (2030) | 2026 | CONFIRMED | [15][16] |
| US data center share | 4.4% (2023) → 6.7-12% (2028); 325-580 TWh | Dec 2024 | CONFIRMED | [17] |
| US 5-yr peak growth (utility filings) | +166 GW by 2030; ~90 GW data centers; up to 40% overstated | Nov 2025 | CONFIRMED | [18][19] |
| US data center capacity energized | ~20 GW (2026); ~30 GW expected (2027) | Jun 2026 | REPORTED | [22] |
| ERCOT large-load queue | 474 GW (~90% data centers); 198 GW applied Q1 2026 | Aug 2026 | CONFIRMED | [25] |
| PJM+ERCOT generation queue | >300 GW, ~1,500 projects; 3-4 yr waits | May 2026 | CONFIRMED | [24] |
| GE Vernova gas backlog + reservations | 116 GW; 125 GW guided; 2031 slots | Jul 2026 | CONFIRMED | [26] |
| Siemens Energy gas backlog | 69 GW; 3+ yr lead; €51B grid backlog | Aug 2026 | CONFIRMED | [28] |
| Power transformer lead time | 128 wks avg; GSU 144 wks; up to 4 yrs | 2025-26 | CONFIRMED | [48][49] |
| HV switchgear shortfall | 40%; MV switchgear 52-104 wks | 2025-26 | CONFIRMED | [48][50] |
| PJM capacity price | $28.92 → $329.17 → $333.44/MW-day (cap) | Dec 2025 | CONFIRMED | [55][56] |
| PJM capacity cost attributed to DCs | ~$9.3B (63-64%) of 2025/26 | 2025 | CONFIRMED | [23][58] |
| Crane (TMI-1) restart | 835 MW; mid/H2 2027; $1B DOE loan | Aug 2026 | CONFIRMED | [32][33] |
| Hyperscaler nuclear deals | ~9.8 GW, 13 deals, 1 under construction | May 2026 | REPORTED | [35] |
| Meta nuclear | 6.6 GW (Vistra 2.1 + Oklo 1.2 + TerraPower up to 2.8); 2030-2032 | Jan 2026 | CONFIRMED | [7] |
| Hyperion phase 1 | $28.8B; 1.5 GW end-2027; 5 GW stretch; Evest 5.3 GW CCGT $12.9B | May 2026 | CONFIRMED | [6] |
| Colossus | 2 GW, 555k GPUs, ~$18B; 59 unpermitted turbines (495 MW) | Jul 2026 | REPORTED | [3][4] |
| Stargate Abilene | 1.2 GW plan; ~300 MW live; 2.1 GW expansion cancelled | Apr 2026 | REPORTED | [1] |
| Fairwater Atlanta | 340 MW → 700+ MW (2026); no UPS/gensets; 140 kW/rack | Jun 2026 | CONFIRMED | [9] |
| Rainier | ~1.18 GW live; 2.25 GW build; 878 gensets | Jun 2026 | CONFIRMED | [12] |
| Bloom / Oracle fuel cells | up to 2.8 GW (1.2 GW firm); 55-day deploy | Apr 2026 | CONFIRMED | [30] |
| Google demand response | 1 GW across 5 utilities | Mar 2026 | CONFIRMED | [14] |
| 800 VDC benefits | ~5% efficiency; ~45% less copper; 85% more power/conductor | Mar 2026 | CONFIRMED | [42] |
| GaN 800 V → 6 V stage | 96.5% peak, 2,100 W/in³; 800→12 V 98.2% | Mar 2026 | CONFIRMED | [41][45] |
| Rack power | GB300 ~163 kW; Vera Rubin 250-370 kW; Kyber 600 kW+ (2027) | 2026 | CONFIRMED | [51][43] |
| Helion Orion | 50 MW, 2028 PPA; $15.5B valuation | Jun 2026 | REPORTED | [37][38] |
| CFS SPARC | first plasma late 2026/2027; Q>1 2027; ARC 400 MWe early 2030s | 2026 | REPORTED | [39][40] |
| State bills | 300+ in 30+ states (6 weeks); 500+ local bans | 2026 | CONFIRMED | [59][60] |

---

## Sources

1. Epoch AI, "OpenAI Stargate: where the US sites stand," 2026-04-17. https://epoch.ai/publications/openai-stargate-where-the-us-sites-stand
2. Distilled, "OpenAI's Stargate data centers are taking longer and costing more than its competitors'," Jun 2026. https://www.distilled.earth/p/openais-stargate-data-centers-are
3. Introl, "xAI Colossus hits 2 GW: 555,000 GPUs, $18B," Jan 2026. https://introl.com/blog/xai-colossus-2-gigawatt-expansion-555k-gpus-january-2026
4. Technology.org, "xAI ran 59 unpermitted gas turbines for Colossus 2 near Memphis," 2026-07-15. https://www.technology.org/2026/07/15/xai-59-unpermitted-gas-turbines-southaven-colossus-2/
5. Southern Environmental Law Center, "xAI built an illegal power plant to power its data center," 2026. https://www.selc.org/news/xai-built-an-illegal-power-plant-to-power-its-data-center/
6. MeasuredAI, "Meta's Hyperion Louisiana data center cluster: the power playbook," 2026-05-08. https://measuredai.substack.com/p/meta-gw-louisiana-data-center
7. TechCrunch, "Meta signs deals with three nuclear companies for 6-plus GW of power," 2026-01-09. https://techcrunch.com/2026/01/09/meta-signs-deals-with-three-nuclear-companies-for-6-plus-gw-of-power/
8. TechCrunch, "Mark Zuckerberg says Meta is building a 5GW AI data center," 2025-07-14. https://techcrunch.com/2025/07/14/mark-zuckerberg-says-meta-is-building-a-5gw-ai-data-center
9. MeasuredAI, "Microsoft's Fairwater Atlanta: a grid-only gigawatt AI data center," 2026-06-02. https://measuredai.substack.com/p/microsoft-fairwater-atlanta-data-center
10. DCD, "Microsoft launches Atlanta Fairwater AI data center: two stories, no UPS or gen-sets," Nov 2025. https://www.datacenterdynamics.com/en/news/microsoft-launches-atlanta-fairwater-data-center-two-stories-no-ups-or-gen-sets/
11. Microsoft Source, "From Wisconsin to Atlanta: Microsoft connects datacenters to build its first AI superfactory," Nov 2025. https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/
12. MeasuredAI, "AWS New Carlisle data center campus: Project Rainier," 2026-06-16. https://measuredai.substack.com/p/aws-new-carlisle-data-center-campus
13. CNBC, "Amazon opens $11 billion AI data center Project Rainier in Indiana," 2025-10-29. https://www.cnbc.com/2025/10/29/amazon-opens-11-billion-ai-data-center-project-rainier-in-indiana.html
14. Google, "Google signed 1 GW of data center demand response," 2026-03-19. https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/demand-response-data-center-milestone/
15. IEA, "Electricity 2026 – Demand," 2026. https://www.iea.org/reports/electricity-2026/demand
16. IEA, "Energy and AI – Energy demand from AI," 2025 (updated 2026). https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
17. DCD, "DOE: Data centers consumed 4.4% of US power in 2023, could hit 12% by 2028" (LBNL 2024 report), Dec 2024. https://www.datacenterdynamics.com/en/news/doe-data-centers-consumed-44-of-us-power-in-2023-could-hit-12-by-2028/
18. Canary Media, "Data-center power forecasts climb to unreachable heights," 2025-11-18. https://www.canarymedia.com/articles/data-centers/data-center-power-forecasts-climb-to-unreachable-heights
19. Grid Strategies, "Power demand forecasts revised up for third year running, led by data centers," Nov 2025. https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf
20. Utility Dive, "Some load forecasts using 'unrealistically high load factors': Grid Strategies VP," 2026. https://www.utilitydive.com/news/some-load-forecasts-using-unrealistically-high-load-factors-grid-strateg/805927/
21. SemiAnalysis, "Stop saying half of 2026 US datacenter capacity is canceled," 2026-06-18. https://newsletter.semianalysis.com/p/stop-saying-half-of-2026-us-datacenter
22. RealClear AI, "SemiAnalysis says 20 gigawatts of data-center capacity came online in 2026," 2026-06-11. https://www.realclear.ai/blog/semianalysis-20-gigawatts-2026
23. SemiAnalysis, "Are AI datacenters increasing electric bills for American households?," 2026-03-03. https://newsletter.semianalysis.com/p/are-ai-datacenters-increasing-electric
24. Carbon Direct, "AI meets the grid: interconnection queue analysis in PJM and ERCOT," May 2026. https://www.carbon-direct.com/research-and-reports/ai-meets-the-grid-interconnection-queue-analysis-in-pjm-and-ercot
25. Utility Dive, "Facing an estimated 474 GW of interconnection requests, Texas hits pause on data centers," Aug 2026. https://www.utilitydive.com/news/texas-hits-pause-data-center-interconnections/827046/
26. Utility Dive, "GE Vernova gas turbine backlog climbs to 116 GW," 2026-07-23. https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/
27. GE Vernova, "First quarter 2026 financial results," 2026-04-22. https://www.gevernova.com/news/press-releases/ge-vernova-reports-first-quarter-2026-financial
28. Utility Dive, "Siemens Energy's gas turbine backlog nears 70 GW as company expands manufacturing," 2026-08-10. https://www.utilitydive.com/news/siemens-gas-turbine-backlog-nears-70-gw-as-company-expands-manufacturing/827390/
29. S&P Global, "Siemens Energy lifts global gas turbine outlook on data center demand," 2026-06-30. https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/063026-siemens-energy-lifts-global-gas-turbine-outlook-on-data-center-demand
30. Bloom Energy, "Bloom Energy and Oracle expand strategic partnership to deploy up to 2.8 GW," 2026-04-13. https://investor.bloomenergy.com/press-releases/press-release-details/2026/Bloom-Energy-and-Oracle-Expand-Strategic-Partnership-to-Deploy-up-to-2-8-GW-to-Accelerate-AI-Infrastructure-Build-Out/default.aspx
31. DCD, "Bloom Energy signs $5bn partnership with Brookfield," 2025-2026. https://www.datacenterdynamics.com/en/news/bloom-energy-signs-5bn-partnership-with-brookfield-to-deploy-fuel-cell-tech-across-ai-data-centers/
32. Pennsylvania Capital-Star, "Concern persists as former Three Mile Island nuclear plant progresses toward 2027 restart," Jul 2026. https://penncapital-star.com/energy-environment/concern-persists-as-crane-nuclear-plant-progresses-toward-2027-restart/
33. The National, "Microsoft-backed Three Mile Island reboot meets data centre backlash," 2026-08-21. https://www.thenationalnews.com/future/technology/2026/08/21/pennsylvania-three-mile-island-crane/
34. NucNet, "Constellation secures $1 billion federal loan for Three Mile Island restart," 2025-11-03. https://www.nucnet.org/news/constellation-secures-usd1-billion-federal-loann-for-three-mile-island-restart-11-3-2025
35. SMR Intel, "Every nuclear-powered data center deal (2026)," May 2026. https://smrintel.com/nuclear-data-center-deals/
36. EnkiAI, "Google nuclear 2026: 1,800 MW Elementl Power deal," 2026. https://enkiai.com/sustainability-initiatives/data-center/google-nuclear-2026-1800-mw-elementl-power-deal/
37. TechCrunch, "Fusion startup Helion hits blistering temps as it races toward 2028 deadline," 2026-02-13. https://techcrunch.com/2026/02/13/fusion-startup-helion-hits-blistering-temps-as-it-races-toward-2028-deadline/
38. DCD, "Helion begins work at fusion plant, expects to deliver power to Microsoft by 2028," Jul 2025. https://www.datacenterdynamics.com/en/news/helion-begins-work-at-fusion-plant-expects-to-deliver-power-to-microsoft-by-2028/
39. The Fusion Report, "Commonwealth Fusion Systems: a hot start for 2026," 2026. https://thefusionreport.com/commonwealth-fusion-systems-a-hot-start-for-2026/
40. Wikipedia, "SPARC (tokamak)," accessed 2026-09-07. https://en.wikipedia.org/wiki/SPARC_(tokamak)
41. Power Electronics News, "Nvidia GTC 2026: power from grid to GPU," Mar 2026. https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/
42. IEEE Spectrum, "Data center DC embraces 800V power shift," 2026-03-24. https://spectrum.ieee.org/data-center-dc
43. DCD, "Nvidia prepares data center industry for 1MW racks and 800-volt DC power architectures," 2025. https://www.datacenterdynamics.com/en/news/nvidia-prepares-data-center-industry-for-1mw-racks-and-800-volt-dc-power-architectures/
44. HPCwire, "NVIDIA, partners drive next-gen efficient gigawatt AI factories in buildup for Vera Rubin," Oct 2025. https://www.hpcwire.com/off-the-wire/nvidia-partners-drive-next-gen-efficient-gigawatt-ai-factories-in-buildup-for-vera-rubin/
45. Semiconductor Today, "Navitas debuts 800V–6V DC–DC power delivery board at NVIDIA GTC," 2026-03-17. https://www.semiconductor-today.com/news_items/2026/mar/navitas-170326.shtml
46. Power Electronics News, "Real-world SSTs target AI data centers and grid modernization," 2026. https://www.powerelectronicsnews.com/real-world-solid-state-transformers-overcome-barriers-to-meet-adoption-needs-of-ac-and-dc-networks/
47. Data Center Richness, "Solid state transformers could reshape AI infrastructure," 2026. https://datacenterrichness.substack.com/p/solid-state-transformers-could-reshape
48. POWER Magazine, "Transformers in 2026: shortage, scramble, or self-inflicted crisis?," 2026-01-02. https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/
49. pv magazine USA, "U.S. transformer market faces severe supply constraints as lead times extend to four years," 2026-05-11. https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/
50. Terrapin Construction Group, "Switchgear, transformer, and generator lead times in 2026," 2026-06-10. https://terrapincg.com/news/switchgear-transformer-generator-lead-times-2026
51. Schneider Electric, "Data center power density: planning liquid-cooled AI data centers around grid and power constraints," 2026-07-28. https://blog.se.com/datacenter/2026/07/28/data-center-power-density-planning-liquid-cooled-ai-data-centers-around-grid-and-power-constraints/
52. Supermicro, "Support for NVIDIA Vera Rubin NVL72, HGX Rubin NVL8 and expanded liquid-cooled rack-scale manufacturing," 2026. https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Support-for-Upcoming-NVIDIA-Vera-Rubin-NVL72-HGX-Rubin-NVL8-and-Expanded-Rack-Scale-Manufacturing-Capacity-for-Liquid-Cooled-AI-Solutions/default.aspx
53. Latitude Media, "As load woes grow, Hitachi Energy doubles down on HVDC in the US," 2026. https://www.latitudemedia.com/news/as-load-woes-grow-hitachi-doubles-down-on-hvdc-in-the-u-s/
54. Hitachi Energy, "Hitachi and Adani switch on HVDC city center infeed for more than 20 million people in Mumbai," 2026-03. https://www.hitachienergy.com/news-and-events/press-releases/2026/03/hitachi-and-adani-switch-on-hvdc-city-center-infeed-for-more-than-20-million-people-in-mumbai
55. Enel North America, "PJM 2027/2028 capacity auction results," Dec 2025. https://www.enelnorthamerica.com/insights/blogs/pjm-2027-2028-capacity-auction-results
56. PJM, "2027/2028 Base Residual Auction Report," 2025-12-17. https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2027-2028/2027-2028-bra-report.pdf
57. IEEFA, "Projected data center growth spurs PJM capacity prices by factor of 10," 2025. https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10
58. Utility Dive, "Data centers were 40% of PJM capacity costs in last auction: market monitor," 2025. https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951/
59. TIME, "Data center panic: Republicans scramble to join backlash," 2026-08-25. https://time.com/article/2026/08/25/data-centers-republican-reset-midterms/
60. MultiState, "State data center legislation in 2026 tackles energy and tax issues," 2026-02-20. https://www.multistate.us/insider/2026/2/20/state-data-center-legislation-in-2026-tackles-energy-and-tax-issues
61. Built In, "States push data center moratoriums as AI growth surges," 2026. https://builtin.com/articles/state-data-center-moratoriums
62. EPRI, "EPRI's DCFlex initiative expands to nine demonstration sites," Feb 2026. https://www.epri.com/about/media-resources/press-release/rBbBPmK6zVt6eXN9rGQlWLMRwHRHQWIS
63. Utility Dive, "Data centers are ready to negotiate flexibility for speed," 2026. https://www.utilitydive.com/news/data-centers-flexibility-utilities-speed-to-power/822588/
64. CNBC, "SpaceX ramps up Tesla Megapack purchases in Q2 to power its AI data centers," 2026-08-05. https://www.cnbc.com/2026/08/05/spacex-tesla-megapack-ai-data-centers.html
65. Electrek, "Tesla, Sunrun team up on 16 GW virtual power plant for data centers," 2026-06-24. https://electrek.co/2026/06/24/tesla-sunrun-16gw-vpp-data-centers/
66. Yahoo Finance / Reuters, "Google signs AES, Xcel supply deals to meet data-center energy needs," 2025-2026. https://finance.yahoo.com/news/xcel-energy-power-google-data-142326416.html
67. Data Center Knowledge, "Why AI data center projects face years of delays after approval," 2026. https://www.datacenterknowledge.com/energy-power-supply/why-ai-data-center-projects-face-years-of-delays-after-approval
68. mgrid, "Data center grid delays put 50% of 2026 AI capacity at risk" (Bloomberg/Sightline claim), 2026-01-15. https://mgrid.org/2026/01/15/data-center-grid-delays-50-percent-2026-ai-capacity-risk/
69. Tech Insider, "NAACP sues xAI: 27 illegal gas turbines at Colossus 2," 2026. https://tech-insider.org/xai-colossus-2-naacp-lawsuit-illegal-gas-turbines-memphis-2026/
