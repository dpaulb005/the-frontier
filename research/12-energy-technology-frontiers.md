# Energy Technology Frontiers, 2026: Everything Except the Datacenter

*Research brief — compiled 2026-09-07.*

**Labeling convention.** **CONFIRMED** = a verifiable event, shipped product, certified measurement, or signed contract. **REPORTED** = credible press or analyst account, or company guidance not independently verified. **SPECULATION** = forward projection, contested claim, or my own inference.

---

## TL;DR

1. The frontier moved from *invention* to *manufacturing*. Sodium-ion left the lab at GWh scale, perovskite tandems entered pilot production, enhanced geothermal is about to sell its first commercial electron, and the first US advanced-reactor construction permit in 40+ years was issued. Almost nothing here is a new physical principle; nearly all of it is a factory.
2. **Grid storage is scaling faster than any energy technology in history.** BNEF forecasts ~158 GW / 459 GWh of global deployments in 2026, up ~41% from a record ~112 GW in 2025. LFP is ~90% of it. **CONFIRMED (forecast is REPORTED)** [1][2]
3. **Batteries got cheap enough to be boring.** Global lithium-ion pack prices fell 8% to a record **$108/kWh** in 2025; stationary-storage packs fell **45% in one year to $70/kWh**, now the cheapest segment. **CONFIRMED** [3]
4. **Sodium-ion crossed the threshold.** CATL's Naxtra entered GWh-scale production in 2026, reportedly at ~$19/kWh at the cell level vs ~$55-60/kWh for LFP, alongside a 60 GWh supply agreement with HyperStrong. **REPORTED** [4][5]
5. **Solar had its first down year on record.** BNEF projects ~649 GW in 2026 vs ~655 GW in 2025 — the first contraction since records began in 2000 — driven entirely by China cooling ~14%. Non-China installs grow to ~308 GW. **REPORTED** [6][7]
6. **Perovskite tandems hit 35.5% certified cell efficiency** (LONGi, July 2026), while shipping modules land at 26-28%. The lab-to-module gap, not the record, is the story. **CONFIRMED** [8][9]
7. **Fusion slipped; the hardware and money did not.** SPARC first plasma moved to 2027 (~75% built); Helion's Polaris reached 150 million °C; private funding exceeds **$13B**. Nobody is within 12 months of grid electricity. **REPORTED** [10][11][12]
8. **Enhanced geothermal goes commercial this quarter.** Fervo's Cape Station Phase I (100 MW) is expected to deliver power in late 2026, at ~$7,000/kW falling toward a targeted $3,000/kW, backed by a 396 MW Google PPA. **REPORTED** [13][14]
9. **Transmission is the binding constraint.** ~2,600 GW sits in US interconnection queues; ~14 GW withdraw per 1 GW built; PJM capacity prices went from $28.92 to $329.17/MW-day across two delivery years. **REPORTED** [15][16]
10. **Hydrogen's correction is complete.** 33+ GW cancelled, 60-70% wiped from hydrogen equities, Air Products' $3.1B charge, CF Industries' $51M impairment. What survives is industrial feedstock, not an energy carrier. **REPORTED** [17][18]

---

## 1. Batteries: the cost curve ate the technology debate

The 2025 BNEF Battery Price Survey — the industry's reference series — put global volume-weighted average lithium-ion pack prices at **$108/kWh, down 8% year-over-year**, with three details that matter more than the headline [3]:

- **Stationary storage packs collapsed to $70/kWh, a 45% single-year drop**, making grid storage the *cheapest* battery segment for the first time. BEV packs averaged $99/kWh.
- **LFP packs averaged $81/kWh vs NMC at $128/kWh.** LFP is no longer the budget option; it's the default.
- **Geography dominates chemistry**: China averaged $84/kWh, while North America ran 44% higher and Europe 56% higher. **CONFIRMED**

BNEF projects a further ~3% decline in 2026 to just under $105/kWh [3]. **REPORTED**

That happened *despite* rising lithium and cobalt prices — overcapacity and competition beat raw materials. **SPECULATION:** this decoupling is underrated. Battery cost is now primarily a function of factory utilization and competitive intensity, not commodity markets — which makes cost forecasts far more robust than the 2022 lithium spike suggested.

### Sodium-ion: from perpetual "next year" to actual production

CATL's chief scientist Wu Kai stated the company resolved core manufacturing challenges, with large-scale sodium-ion production from Q4 2026 [4]. The Naxtra product line reached GWh-scale, paired with a reported **60 GWh supply agreement with HyperStrong** — the largest sodium-ion deal recorded. Specs: **up to 175 Wh/kg**, passing China's latest national EV traction-battery safety standard [4][5]. **REPORTED**

Cost claims deserve care. Circulated figures put Naxtra cells at **~$19/kWh vs ~$55-60/kWh for LFP cells** [5]. **SPECULATION** — that gap is implausibly large for a lower-density chemistry with a less mature supply chain, and likely reflects a strategic price or favorable accounting boundary rather than sustainable full cost. The sober read is HiNa GM Li Shujun's forecast of **cost parity with lithium in 2027-2028** [19] — i.e. sodium is not yet cheaper like-for-like. **REPORTED**

Where sodium wins today: cold-climate performance, grid storage where volumetric density is irrelevant, and as a lithium-price hedge. Changan is fielding a commercial sodium-ion EV on CATL cells [4]. **REPORTED**

### Solid-state: 2026 is the pilot-line year, not the product year

The consistent picture across all four major programs is *pilot manufacturing*, not vehicles:

| Company | 2026 status | Target |
|---|---|---|
| Toyota | Japanese government certification to begin solid-state production; Idemitsu sulfide-electrolyte pilot plants | ~2027-2028 commercialization |
| QuantumScape | "Cobra" separator process equipment installed on automated line, San Jose; QSE-5 customer samples | 2027-2028 mass production window |
| Samsung SDI | Sulfide "S-line" pilot; ~900 Wh/L prototypes demonstrated | ~2027 limited production, premium first |
| Factorial | Honda demonstration line running | Late 2020s |

**REPORTED** [20][21]

**SPECULATION:** solid-state slipped roughly one product cycle behind 2023 guidance, and sodium-ion plus cheap LFP has quietly eaten much of its low-end rationale. Its surviving case is premium range and fast charge, not cost — and BYD's megawatt charging on liquid-electrolyte cells attacks even that.

### Charging: the megawatt era arrived for real

- **BYD** deployed **10,000+ flash-charging stations across 325 cities** in China (targeting 20,000 by end-2026), on a 1,000 V / **1 MW (1,000 kW)** Super e-Platform delivering ~400 km in 5 minutes on Han L / Tang L. A second-generation unit at up to **2,100 kW** is in development, with ~3,000 stations planned for Europe by end-2026 and 6,000 outside China. **REPORTED** [22][23]
- **Heavy trucks**: the **Megawatt Charging System** international specification **IEC TS 63379 was published 9 February 2026** (CharIN), enabling up to **3.75 MW at 1,250 V / 3,000 A**. Scania made MCS commercially available from early 2026 (first iteration ~1,000 A / up to 750 kW); Milence and partners target ~1,700 high-performance charging points across 10 EU states by 2027. **CONFIRMED (spec), REPORTED (rollout)** [24][25]

This is the year charging stopped being the reason not to buy an electric truck and started being a grid-interconnection problem instead.

---

## 2. Grid storage: the boom nobody's pricing correctly

BNEF forecasts **158 GW / 459 GWh** of global non-pumped-hydro storage in 2026, a **41% increase** on 2025's record ~112 GW [1]. IEA's parallel accounting: **108 GW added in 2025, +40% on 2024, with installed capacity now 11× 2021 levels** [2]. China added ~167 GWh in 2025 and is expected to add ~203.5 GWh in 2026 [1]. **REPORTED**

The Chinese policy story is counterintuitive and important. **Document 136 (February 2025) scrapped the mandate** requiring new wind and solar to co-locate storage — and Chinese storage kept growing anyway, shifting from mandate-driven to market-driven. In June 2026 China set a **300 GW new-type energy storage target for 2030** under the 15th Five-Year Plan [26]. **REPORTED**

**SPECULATION:** removing the mandate was bullish, not bearish. Mandated storage was built to satisfy paperwork and often sat idle; market-driven storage gets cycled, which generates revenue data, which unlocks project finance. Ember's framing — "from scale to utilization" — is right [26].

### Long duration: iron-air finally has hardware in the dirt

Form Energy's **Cambridge, Minnesota** project with Great River Energy — **1.5 MW / 150 MWh, 100-hour duration** — is the first commercial deployment of iron-air, manufactured at Form Factory 1 in Weirton, West Virginia, and expected fully operational in 2026 (slipped from a late-2025 target) [27][28]. Follow-on projects are slated in New York, Georgia, and Virginia. **REPORTED**

The headline number: **Google and Xcel Energy announced (24 February 2026) intent to develop a 300 MW / 30 GWh iron-air system** — a duration and scale with no lithium-ion analogue [29]. **REPORTED**

**SPECULATION:** iron-air's real test isn't chemistry, it's whether a 100-hour asset can be dispatched and paid for in markets designed around 4-hour resources. The 1.5 MW / 150 MWh ratio tells you the physics: iron-air is enormously energy-dense per dollar and enormously power-poor. It is a seasonal-adjacent hedge, not a peaker, and most market rules can't yet see the difference.

---

## 3. Solar: record efficiency, first-ever volume decline

Two facts sit awkwardly together.

**Fact one: the technology is accelerating.** LONGi announced **35.5% certified (ESTI) efficiency for a crystalline silicon-perovskite tandem cell** on 14 July 2026 — up a stepladder from 33.9% (Nov 2023) → 34.6% (Jun 2024) → 34.85% → 35.2% → 35.5%. Theoretical tandem limit is ~43% [8][9]. **CONFIRMED**

Commercial modules are far behind: **Oxford PV's 26.9% module efficiency** (60-cell residential format, Fraunhofer CalLab certified), with first commercial tandem modules from Oxford PV and LONGi expected in H2 2026 at **26-28%** [30]. LONGi's back-contact (BC/ACM) technology — conventional silicon, not tandem — is in volume production at its **21 GW Xixian** cell project [8]. **REPORTED**

**Fact two: volumes are falling for the first time ever.** BNEF projects **~649 GW in 2026 vs ~655 GW in 2025** — the first annual contraction in records back to 2000. IEA's more conservative series shows ~540 GW in 2026 vs ~585 GW in 2025. China is the entire cause: down ~14% to ~341 GW (~52% of global), while non-China installs grow to ~308 GW with India and Africa accelerating [6][7]. Module prices have stabilized and modestly recovered after two years of below-cost selling, driven by silver costs and coordinated Chinese self-regulation [6]. **REPORTED**

**SPECULATION:** this is a demand-shape correction inside China's tariff reform (post-Document 136 market pricing), not a technology or cost failure — and it is probably healthy. Modest price recovery is what lets Chinese manufacturers fund the capital-intensive, currently unprofitable tandem transition; a perpetual price war would have starved perovskite commercialization. The number to watch in 2027 is not efficiency records but **certified outdoor degradation data on tandem modules over 24+ months**. Durability is perovskite's entire commercial risk, and no lab record addresses it.

---

## 4. Wind: a contraction, and a 20 MW machine

- **Offshore wind build contracted by roughly a third in 2025**, adding only ~8.1 GW, after three years of growth — delays in mainland China and France, plus a temporary US standstill under political headwinds [31]. **REPORTED**
- 2026 looks like a rebound: **~18.8 GW forecast to reach full operation globally (10.8 GW excluding China)**, potentially the second-highest year on record after 2021 [32]. **REPORTED**
- **China installed and grid-connected the world's first 20 MW offshore turbine** (Goldwind, Fujian, January 2026), generating >80 GWh/year — enough for ~44,000 households, with batch installation to follow [33][34]. **CONFIRMED**
- Global wind installations overall hit an all-time high, with Chinese turbine suppliers taking the leading share [35]. **REPORTED**

**SPECULATION:** the 20 MW machine matters less as engineering than as a signal. Western OEMs retreated from turbine-size escalation in 2023-2025 because warranty losses destroyed margins; Chinese OEMs did not. Expect Chinese turbines to dominate every market without a policy wall against them by 2030.

---

## 5. Fusion: the schedule slipped, the money didn't

**The tokamak line.** Commonwealth Fusion Systems is **~75% complete on SPARC construction**, with first plasma now targeted for **2027** (originally 2025) and Q>1 "as fast as humanly possible" thereafter [10]. Google has signed a **200 MW PPA for CFS's first ARC plant in Virginia**, expected early 2030s [12]. **REPORTED**

**The pulsed line.** Helion's **Polaris** reached **150 million °C** — roughly three-quarters of what the company believes a commercial plant requires — while racing a **2028 deadline** to deliver **50 MW to Microsoft** under the world's first fusion PPA. Helion raised **$465M in June 2026** [11][12]. **REPORTED**

**Public and international.**
- **China's EAST** sustained steady-state high-confinement plasma for **1,066 seconds** (up from its own 403 s record in 2023) and demonstrated stable operation beyond the conventional Greenwald density limit [36][37]. **CONFIRMED**
- **ITER**: the revised baseline pushes start of research operations to ~**2034-2035**, D-D with full magnetic energy in 2036, and **D-T fuel to 2039**, with ~€5B in additional cost [38][39]. **CONFIRMED**
- **DOE Milestone-Based Fusion Development Program**: eight companies selected, ~$46M federal for the initial 18 months — against which awardees have collectively raised **>$350M in new private funding**. Thea Energy became the first awardee to complete its final major design review [40][41]. **REPORTED**

**Money.** Private fusion investment exceeds **$13B**, with **17 startups above $100M each**: Pacific Fusion ~$900M milestone-gated Series A, TAE ~$1.79B, Zap ~$338M, Focused Energy $240M (June 2026) [42][12]. **REPORTED**

**SPECULATION — the honest 2026 read:** no fusion device has delivered net electricity to a grid, and none will within 12 months. But three things genuinely changed since 2023: (a) HTS magnets went from research object to supply chain, (b) fusion acquired *creditworthy offtakers* (Microsoft, Google) which changes the financing structure from grant to project finance, and (c) China's EAST results show state programs advancing on confinement physics at a pace that makes ITER's 2039 D-T date look institutionally, not technically, determined. The plausible risk is not that fusion fails — it's that the first working machines are Chinese and the 2028 PPAs get quietly renegotiated.

---

## 6. Fission: permits, not startups

The most consequential US nuclear event of 2026 was administrative. The **NRC approved TerraPower's Kemmerer construction permit on 4 March 2026** — the first construction permit for an advanced commercial reactor in over 40 years — with **nuclear construction beginning 23 April 2026**. Natrium will supply up to **500 MW** to Rocky Mountain Power [43]. **CONFIRMED**

Elsewhere:
- **Kairos Power** began nuclear construction on **Hermes II** (~50 MW demo, Oak Ridge TN), tied to a Google offtake, with the low-power demo targeted operational in 2026 [43][44]. **REPORTED**
- **X-energy / Dow Long Mott**: NRC environmental review completed October 2025, final safety evaluation December 2025, permit decision expected H1 2026 [43]. **REPORTED**
- **NuScale** remains the only NRC design-certified SMR; its Idaho pilot was scrapped after the offtaker withdrew. NuScale/ENTRA1/TVA launched a 6 GW deployment program (September 2025) [44]. **REPORTED**
- **Restarts beat new builds**: the Crane Clean Energy Center (former Three Mile Island Unit 1) targets **H2 2027** under Microsoft offtake — ahead of essentially every new-build SMR, which mostly target 2030+ [44]. **REPORTED**

**SPECULATION:** restarts and uprates will deliver more incremental US nuclear electricity through 2030 than every SMR program combined. SMRs are a 2030s technology being financed with 2020s enthusiasm. The valuable output of the current SMR wave may be regulatory precedent — the Kemmerer permit is reusable in a way the reactor itself is not.

---

## 7. Geothermal: the quiet winner

**Fervo Energy** is the most underrated company in energy right now. **Cape Station Phase I (100 MW)** in Milford, Utah is expected to send power to the grid in late 2026 — which would make it the **first enhanced geothermal system in the US to reach commercial operation**. Phase II adds **400 MW by 2028**. Fervo raised **$206M** in additional financing [13][45]. **REPORTED**

The economics are the story:
- Phase I: **~$7,000/kW**
- Phase II: **~$5,500/kW**
- Fervo's stated target: **~$3,000/kW**, via longer laterals and standardized 50 MW plant blocks [13]

Offtake: **a 396 MW PPA with Google** — the largest enhanced-geothermal PPA ever — reported to sit inside a framework of **up to 3 GW** [14][46]. **CONFIRMED (396 MW), REPORTED (3 GW framework)**

**Superhot rock** remains earlier. **Quaise Energy** raised **$134M** in an initial Series B close (July 2026), bringing total funding to ~$230M, aiming for the world's first superhot geothermal plant (Oregon site), using MIT-derived millimeter-wave drilling to reach **300-500 °C** rock. It is approaching ~1 km depth at its Central Texas test site — the deepest millimeter-wave penetration achieved [47][48]. **REPORTED**

**SPECULATION:** Fervo has proven that horizontal drilling plus multi-stage fracturing — 20 years of shale learning curve — transfers to hot dry rock. That is a learning-rate argument, not a resource argument, and learning rates are what make technologies cheap. At $3,000/kW with a 90%+ capacity factor, EGS becomes the cheapest firm clean power in the western US.

---

## 8. Grid, transmission, and power electronics

**The bottleneck, quantified.** As of early 2026, **~2,600 GW** of generation and storage sits in US interconnection queues, with median wait times approaching five years and some large-load requests facing far worse. **For every ~1 GW that reached commercial operation in 2025, ~14 GW withdrew** [15][16]. PJM capacity prices for the 2026-27 delivery year cleared at **$329.17/MW-day**, more than 10× the **$28.92/MW-day** of 2024-25 [16]. **REPORTED**

**Grid-enhancing technologies moved from optional to expected.** FERC Order 1920 requires planners to formally evaluate GETs — dynamic line rating (DLR), advanced power flow control, advanced conductors — against conventional builds. **PJM became the first RTO to fully implement Ambient-Adjusted Ratings in March 2026**; MISO and NYISO are not expected until 2028 [49][50]. **REPORTED**

**Big iron is moving too.** **Grain Belt Express** — 800 miles, **5 GW HVDC**, four states, ~$11B — awarded **$1.7B in EPC contracts to Quanta and Kiewit**, with Phase 1 (Kansas-Missouri) construction targeted to start in 2026. It would be the largest transmission line in US history [51][52]. **REPORTED** Advanced-conductor supply is expanding in parallel (Prysmian's Williamsport, PA expansion roughly doubling certain US advanced-conductor capacity) [51].

**Power electronics.** The automotive-grade power-semiconductor market is forecast to exceed **$20B by 2026**, with SiC holding >70% of that segment, as **800 V EV platforms** go mainstream — the enabling condition for megawatt charging [53]. SiC also dominates the multi-kV **solid-state transformer** stage now being pulled into commercial reality by 800 V DC distribution architectures [54]. Notably, **SiC and GaN oversupply is expected to persist** despite EV and AI demand [55]. **REPORTED**

**SPECULATION:** wide-bandgap oversupply is a gift downstream. Cheap SiC makes solid-state transformers, MW chargers, and grid-forming inverters ordinary rather than exotic — the same pattern cheap lithium cells produced for storage. Grid-forming inverter mandates are the likely sleeper regulatory fight of 2027.

---

## 9. Hydrogen: the correction is finished; what's left is real

The numbers tell a clean story of a hype cycle completing:
- **Air Products** took a **$3.1B charge** (May 2025) retreating from aggressive clean-hydrogen investment [17]. **CONFIRMED**
- **CF Industries** cancelled its Donaldsonville green hydrogen electrolyzer project (February 2026), taking a **$51M impairment**, after concluding it could not generate sufficient returns [17]. **CONFIRMED**
- **33 European hydrogen projects cancelled or halted in 2024 alone**, ~3.6 GW of planned electrolyzer capacity (LCP Delta) [18]. **REPORTED**
- Aggregate 2025-26 correction: **33+ GW of projects cancelled** and **60-70% wiped from hydrogen equity valuations** [18]. **REPORTED**
- Green hydrogen production costs remain **~$3.00-6.00/kg**, roughly **2-5×** grey hydrogen [18]. **REPORTED**

The cause is not technology but the absence of **bankable offtake** — the most-cited reason for cancellation [18]. **SPECULATION:** hydrogen's surviving market is where it is a *molecule input* (ammonia, refining, possibly direct-reduced iron), not an energy carrier. Everywhere hydrogen competes with an electron on a wire — cars, home heating, most power generation — it has lost, and 2026 is the year that stopped being controversial.

---

## 10. Electrification and the frontier's edge

**Electric vehicles.** IEA projects **23 million electric car sales in 2026 (~28% of global sales)**, after **>20 million in 2025 (+20%, ~1 in 4 new cars)** [56]. Chinese automakers supplied **~60%** of the world's electric cars; Europe and North America ~15% each. China's 2025 production of 16 million electric cars **exceeded domestic demand by 20%**, doubling exports to a record **>2.5 million** — and Q1 2026 exports more than doubled again year-over-year, offsetting weaker domestic sales [56][57]. **REPORTED**

**Heat pumps.** Global sales fell ~2% in 2025 but stabilized, continuing into Q1 2026. **Europe returned to growth: +11% in 2025 (first growth since 2022), driven by Germany at +55% in H1; ~2.9 million domestic units sold across 21 European countries (+13%); Q1 2026 up 17% year-over-year.** US sales fell ~13% in 2025 but heat pumps **outsold gas boilers for the fourth consecutive year**, with slight Q1 2026 recovery [58][59]. **REPORTED**

**Space-based solar.** Pre-commercial but no longer purely theoretical: Caltech's SSPD-1 beamed measurable power from LEO to Pasadena; **JAXA's OHISAMA demonstrated ~1 kW orbit-to-ground microwave transmission** to Yokohama, with a further METI/JAXA flight demo in FY2026; **Aetherflux** ($60M Series A) booked a Falcon 9 rideshare for a 2026 laser power-beaming demo while pivoting toward orbital datacenters (first LEO node targeted Q1 2027); China is building a 2 km ground test array in Chongqing [60][61]. **REPORTED**

**SPECULATION:** that pivot is the tell. Space solar's economics never closed against $0.02/kWh terrestrial solar plus $70/kWh storage. The only payers are markets where terrestrial alternatives are forbidden (forward bases, lunar) or where the *payload*, not the power, is the product. Treat space-solar-for-the-grid claims through 2035 as SPECULATION at best.

---

## What people are underestimating

**1. Stationary storage at $70/kWh outweighs any chemistry announcement. [SPECULATION, high confidence]**
A 45% single-year drop making grid storage cheaper than EV packs inverts a decade of assumptions. Grid storage was supposed to be the hand-me-down market for EV cell overcapacity; it is now the price leader, which means it will start pulling cell *design* toward its own requirements (cycle life, C-rate, thermal) rather than accepting automotive castoffs.

**2. Fervo, not fusion, is the 2026 firm-power story. [SPECULATION]**
A 100 MW EGS plant delivering power this quarter, with a credible $3,000/kW roadmap and a 396 MW Google PPA, is a *this-decade* firm clean resource — and gets perhaps 5% of fusion's attention. The learning-curve case is strong precisely because the technique is borrowed from shale, which already proved it can cut drilling costs 10× through repetition.

**3. Solar's first-ever volume decline will be misread as decline. [SPECULATION]**
It is a Chinese policy transition (Document 136 market pricing) landing in one calendar year, plus a deliberate price-floor effort. Non-China installs still grow. Extrapolating a solar plateau from 2026 will look badly wrong by 2028.

**4. The interconnection queue is the real frontier, and it is institutional. [SPECULATION]**
14 GW withdrawn per 1 GW built is not a physics, materials, or cost problem. GETs add capacity in months at a fraction of new-build cost — yet PJM only fully implemented ambient-adjusted ratings in March 2026, with MISO and NYISO not expected until 2028. The gap between "technically available" and "procedurally permitted" holds most of the achievable 2027-2030 gigawatts.

**5. Sodium-ion's importance is optionality, not cost. [SPECULATION]**
Even if $19/kWh is marketing, sodium at rough parity by 2027-2028 permanently caps lithium's pricing power — removing the tail risk that made every long-range battery cost forecast hedge upward.

**6. China's EAST results should be reframing fusion geopolitics. [SPECULATION]**
1,066 seconds of steady-state H-mode plus operation beyond the Greenwald density limit are confinement-physics results from a state program with a successor device (BEST) in build — not startup press releases. Western discourse is organized around private milestones and a 2039 ITER D-T date; neither frame accommodates a Chinese state program moving faster than both.

**7. Solid-state is losing the race it was supposed to win. [SPECULATION]**
Every major program sits at pilot line in 2026 with production in 2027-2028, while BYD delivers 400 km in 5 minutes on liquid-electrolyte cells today and LFP packs sit at $81/kWh. Solid-state's remaining moat is energy density for aviation and premium long-range — a real market, but not the one it was promised.

**8. Restarts beat SMRs to the meter, and the follow-on is unplanned. [SPECULATION]**
Crane Clean Energy Center lands H2 2027 versus SMRs at 2030+. But recently-shuttered reactors are a finite pipeline. The 2028-2030 window — restarts exhausted, SMRs not yet arrived — is an under-planned gap.

---

## Key numbers

| Metric | Value | Date / basis | Label |
|---|---|---|---|
| Li-ion pack price, global avg | **$108/kWh** (−8% YoY) | BNEF 2025 survey | CONFIRMED |
| Stationary storage pack price | **$70/kWh** (−45% YoY) | BNEF 2025 survey | CONFIRMED |
| LFP vs NMC pack price | **$81 vs $128/kWh** | BNEF 2025 survey | CONFIRMED |
| 2026 pack price forecast | **<$105/kWh** (−3%) | BNEF | REPORTED |
| CATL Naxtra sodium cell cost | **~$19/kWh** (vs $55-60 LFP) | 2026 press | SPECULATION |
| Sodium/lithium cost parity | **2027-2028** | HiNa (Li Shujun) | REPORTED |
| Global storage 2026 | **158 GW / 459 GWh** (+41%) | BNEF | REPORTED |
| China 2030 storage target | **300 GW** | 15th Five-Year Plan, Jun 2026 | CONFIRMED |
| LFP share of storage | **~90%** | IEA 2026 | REPORTED |
| Form Energy first commercial | **1.5 MW / 150 MWh, 100 h** | Cambridge, MN | REPORTED |
| Google–Xcel iron-air | **300 MW / 30 GWh** | 24 Feb 2026 | REPORTED |
| Tandem cell record | **35.5%** (ESTI certified) | LONGi, 14 Jul 2026 | CONFIRMED |
| Tandem module (commercial) | **26.9%** module / 26-28% shipping | Oxford PV, Fraunhofer CalLab | CONFIRMED |
| Global solar 2026 | **~649 GW** (vs 655 in 2025) | BNEF | REPORTED |
| China solar 2026 | **~341 GW** (−14%, ~52% of world) | BNEF | REPORTED |
| Largest offshore turbine | **20 MW**, grid-connected | Goldwind, Fujian, Jan 2026 | CONFIRMED |
| SPARC first plasma | **2027** (~75% built) | CFS | REPORTED |
| Helion Polaris temperature | **150 million °C** | Feb 2026 | REPORTED |
| CFS ARC PPA | **200 MW to Google, early 2030s** | CONFIRMED (contract) | CONFIRMED |
| EAST steady-state record | **1,066 seconds** | CAS, Jan 2025→2026 | CONFIRMED |
| ITER D-T operation | **2039** (research ops ~2034-35) | ITER baseline | CONFIRMED |
| Private fusion investment | **>$13B**; 17 firms >$100M each | 2026 | REPORTED |
| First advanced reactor permit | **4 Mar 2026**, TerraPower Kemmerer | NRC | CONFIRMED |
| Fervo Cape Station Ph. I | **100 MW**, grid power late 2026 | Fervo | REPORTED |
| Fervo capex | **$7,000/kW → $5,500/kW → $3,000/kW target** | Fervo | REPORTED |
| Fervo–Google PPA | **396 MW** (framework rptd. to 3 GW) | 2026 | CONFIRMED / REPORTED |
| US interconnection queue | **~2,600 GW**; ~14 GW withdrawn per 1 GW built | early 2026 | REPORTED |
| PJM capacity price | **$329.17/MW-day** (vs $28.92 in 2024-25) | 2026-27 delivery year | CONFIRMED |
| Grain Belt Express | **800 mi, 5 GW HVDC, ~$11B**; $1.7B EPC awarded | construction start 2026 | REPORTED |
| MCS standard | **IEC TS 63379, published 9 Feb 2026**; 3.75 MW / 1,250 V / 3,000 A | CharIN/IEC | CONFIRMED |
| BYD flash charging | **1 MW**, 400 km in 5 min; 10,000+ stations, 325 cities | 2026 | REPORTED |
| Global EV sales 2026 | **23 million (~28% share)** | IEA | REPORTED |
| China EV exports | **>2.5 million (2025, doubled)**; Q1'26 more than doubled again | IEA | REPORTED |
| European heat pump sales | **+11% in 2025; +17% Q1 2026** | IEA / EHPA | REPORTED |
| Green H2 cost | **$3.00-6.00/kg** (2-5× grey) | 2026 | REPORTED |
| H2 project cancellations | **33+ GW**; 60-70% equity value wiped | 2025-26 | REPORTED |

---

## Sources

1. Energy-Storage.News, "BloombergNEF forecasts 158GW of global energy storage deployments in…" — https://www.energy-storage.news/bloombergnef-forecasts-158gw-of-global-energy-storage-deployments-in-2026/ (2026)
2. IEA, "Global Energy Review 2026 — Technology: Battery storage" — https://www.iea.org/reports/global-energy-review-2026/technology-battery-storage (2026)
3. BloombergNEF, "Lithium-Ion Battery Pack Prices Fall to $108 Per Kilowatt-Hour,…" — https://about.bnef.com/insights/clean-transport/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour-despite-rising-metal-prices-bloombergnef/ (9 Dec 2025)
4. CarNewsChina, "CATL to mass-produce sodium-ion batteries in 2026, targets 600…" — https://carnewschina.com/2026/05/30/catl-to-mass-produce-sodium-ion-batteries-in-2026-targets-600-km-range/ (30 May 2026)
5. BatteryTechOnline, "How CATL moved sodium-ion batteries from lab chemistry to…" — https://www.batterytechonline.com/design-manufacturing/how-catl-moved-sodium-ion-batteries-from-lab-chemistry-to-gwh-scale-reality (2026)
6. pv magazine USA, "BNEF sees 2026 solar slowdown with China slowing, the…" — https://pv-magazine-usa.com/2025/12/22/bnef-sees-2026-solar-slowdown-with-china-slowing-the-world-growing/ (22 Dec 2025)
7. IEA, "Global Energy Review 2026 — Technology: Solar PV and…" — https://www.iea.org/reports/global-energy-review-2026/technology-solar-pv-and-wind (2026)
8. LONGi, "35.5%! LONGi Once Again Breaks World Record for Crystalline…" — https://www.longi.com/en/news/crystalline-silicon-perovskite-tandem-solar-cell-new-world-efficiency-2026/ (15 Jul 2026)
9. pv magazine, "Longi sets new world record with 35.5%-efficient perovskite-silicon tandem…" — https://www.pv-magazine.com/2026/07/15/longi-sets-new-world-record-with-35-5-efficient-perovskite-silicon-tandem-cell/ (15 Jul 2026)
10. Commonwealth Fusion Systems, Technology — https://cfs.energy/technology/ (accessed Sep 2026)
11. TechCrunch, "Fusion startup Helion hits blistering temps as it races…" — https://techcrunch.com/2026/02/13/fusion-startup-helion-hits-blistering-temps-as-it-races-toward-2028-deadline/ (13 Feb 2026)
12. Fortune, "Sam Altman, Helion Energy milestone, doubters, grid power 2028" — https://fortune.com/2026/02/13/sam-altman-fusion-helion-energy-milestone-doubters-grid-power-2028/ (13 Feb 2026)
13. CNBC, "Fervo Energy's enhanced geothermal project aims to power data…" — https://www.cnbc.com/2026/09/05/fervo-energys-enhanced-geothermal-project-aims-to-power-data-center-boom.html (5 Sep 2026)
14. Canary Media, "Fervo and Google sign world's largest deal for next-gen…" — https://www.canarymedia.com/articles/geothermal/fervo-google-deal-next-gen-geothermal (2026)
15. LBNL Energy Markets & Planning, "Queued Up: 2026 Edition" — https://emp.lbl.gov/publications/queued-2026-edition-characteristics (2026)
16. Ascend Analytics, "Can US Interconnection Queues Survive Data Center-Driven Load Growth?" — https://www.ascendanalytics.com/blog/large-load-interconnection-queues-data-center-grid-access (2026)
17. EnkiAI, "Hydrogen Cancellations 2026: A Viability Gap Exposed" — https://enkiai.com/biggest-hydrogen-project-cancellations-in-2025-and-2024/ (2026)
18. Green Fuel Journal, "Green Hydrogen Challenges in 2026: Why Projects Are Failing…" — https://www.greenfueljournal.com/post/green-hydrogen-challenges-in-2026-why-projects-are-failing-reality-check (2026)
19. CnEVPost, "Hina Battery exec predicts sodium battery costs will fall…" — https://cnevpost.com/2026/04/01/hina-battery-exec-sodium-battery-costs-fall-to-match-lithium/ (1 Apr 2026)
20. QuantumScape, Form 10-Q FY2026 (SEC) — https://www.sec.gov/Archives/edgar/data/0001811414/000119312526177161/qs-20260331.htm (Q1 2026)
21. EEPower, "Solid-State Batteries Race to Mass Production" — https://eepower.com/tech-insights/solid-state-batteries-race-to-mass-production/ (2026)
22. CnEVPost, "BYD begins large-scale deployment of megawatt flash charging facilities" — https://cnevpost.com/2026/02/24/byd-begins-large-scale-deployment-megawatt-flash-charging-facilities/ (24 Feb 2026)
23. Drive Tesla Canada, "BYD surpasses 10,000 flash charging stations in six months,…" — https://driveteslacanada.ca/news/byd-10000-flash-charging-stations-2026-expansion/ (2026)
24. Wikipedia, Megawatt Charging System (IEC TS 63379, published 9 Feb 2026) — https://en.wikipedia.org/wiki/Megawatt_Charging_System (accessed Sep 2026)
25. Scania Group, "Megawatt charging – all you need to know about…" — https://www.scania.com/group/en/home/electrification/e-mobility-hub/megawatt-charging-all-you-need-to-know-about-mcs.html (2026)
26. Ember, "From scale to system: navigating the next phase of…" — https://ember-energy.org/latest-insights/from-scale-to-system-navigating-the-next-phase-of-chinas-battery-storage/ (Jul 2026)
27. Form Energy, "Great River Energy and Form Energy break ground on…" — https://formenergy.com/great-river-energy-and-form-energy-break-ground-on-first-of-its-kind-multi-day-energy-storage-project/ (2025-2026)
28. Latitude Media, "Form's first 100-hour batteries are hitting the grid" — https://www.latitudemedia.com/news/forms-first-100-hour-batteries-are-hitting-the-grid/ (Oct 2025)
29. Utility Dive, "World's 'largest' grid battery part of Google-Xcel Energy agreement" — https://www.utilitydive.com/news/worlds-largest-grid-battery-part-of-google-xcel-energy-agreement/813793/ (24 Feb 2026)
30. Earth Energy Log, "Perovskite-silicon tandem solar cells 2026: the commercial timeline" — https://earthenergylog.com/articles/perovskite-tandem-solar-2026 (2026)
31. RenewableUK EnergyPulse, "Global offshore wind pipeline in 2025: a year in…" — https://www.renewableuk.com/energypulse/blog/global-offshore-wind-pipeline-in-2025-a-year-in-review/ (2026)
32. RenewableUK EnergyPulse, "Global offshore wind pipeline June 2026" — https://www.renewableuk.com/energypulse/reports/global-offshore-wind-pipeline-june-2026/ (Jun 2026)
33. CGTN, "New record: China installs world's first 20-megawatt offshore wind…" — https://news.cgtn.com/news/2026-01-13/New-record-China-installs-world-s-first-20MW-offshore-wind-turbine-1JTZt5OzIha/p.html (13 Jan 2026)
34. Interesting Engineering, "World's biggest 20-MW offshore wind turbine now powers China's…" — https://interestingengineering.com/energy/wind-turbine-powers-china-grid (2026)
35. BloombergNEF, "Chinese Turbine Suppliers Seize the Spotlight as Global Wind…" — https://about.bnef.com/insights/clean-energy/chinese-turbine-suppliers-seize-the-spotlight-as-global-wind-power-installations-hit-all-time-high-bloombergnef-report-shows/ (2026)
36. Chinese Academy of Sciences, "Chinese 'Artificial Sun' Sets New Record in Milestone Step Toward Fusion Power Generation" (EAST, 1,066 s) — https://english.cas.cn/newsroom/cas_media/202501/t20250121_899052.shtml (21 Jan 2025)
37. Physics World, "China's Experimental Advanced Superconducting Tokamak smashes fusion confinement record" — https://physicsworld.com/a/chinas-experimental-advanced-superconducting-tokamak-smashes-fusion-confinement-record/ (2025-2026)
38. NucNet, "New schedule for delayed fusion project sees initial operation…" — https://www.nucnet.org/news/new-schedule-for-delayed-fusion-project-sees-initial-operation-in-2035-6-5-2024 (2024, baseline still current)
39. Max Planck Institute for Plasma Physics, "New ITER schedule" — https://www.ipp.mpg.de/5434926/ITER_baseline_2024 (2024)
40. US DOE, "DOE Announces Selectees for $107 Million Fusion Innovation Research…" — https://www.energy.gov/articles/us-department-energy-announces-selectees-107-million-fusion-innovation-research-engine (2025-2026)
41. The Fusion Report, "Thea Energy Becomes First DOE Milestone Program Awardee to…" — https://thefusionreport.substack.com/p/thea-energy-becomes-first-doe-milestone (2026)
42. TNW, "17 fusion startups have now raised over $100M each,…" — https://thenextweb.com/news/fusion-startups-13-billion-private-funding-race-commercial-energy (2026)
43. Nuclear Innovation Alliance, "U.S. Nuclear Energy Project Tracker Update – May 2026" — https://nuclearinnovationalliance.org/index.php/us-nuclear-energy-project-tracker-update-may-2026 (May 2026)
44. SMR Intel, "State of Small Modular Reactors 2026 — Annual Intelligence…" — https://smrintel.com/state-of-smr-2026/ (2026)
45. Fervo Energy, "Fervo Energy Secures $206 Million In New Financing To…" — https://fervoenergy.com/fervo-secures-new-financing-to-accelerate-development/ (2026)
46. Blockspace, "Fervo signs up to 3 GW Google geothermal framework:…" — https://blockspace.media/insight/fervo-google-geothermal-framework-3-gw/ (2026)
47. BusinessWire, "Quaise Energy Raises $134 Million in Initial Close of…" — https://www.businesswire.com/news/home/20260707844187/en/ (7 Jul 2026)
48. Canary Media, "Quaise looks to advance 'superhot' geothermal power" — https://www.canarymedia.com/articles/geothermal/quaise-superhot-geothermal-power-plant-oregon (2026)
49. US DOE Office of Electricity, "Grid-Enhancing Technologies Improve Existing Power Lines" — https://www.energy.gov/oe/grid-enhancing-technologies-improve-existing-power-lines (accessed Sep 2026)
50. Enline, "FERC, Dynamic Line Rating, and Grid Enhancing Technologies in…" — https://enline.energy/articles/ferc-dynamic-line-rating-grid-enhancing-technologies-2026 (2026)
51. Grain Belt Express / Invenergy, "Grain Belt Express Awards $1.7B to U.S. Contractors Quanta…" — https://grainbeltexpress.com/grain-belt-express-awards-1-7b-to-u-s-contractors-quanta-and-kiewit-to-build-largest-transmission-line-in-u-s-history/ (2025-2026)
52. T&D World, "Transforming the U.S. Grid: The Impact and Engineering of…" — https://www.tdworld.com/overhead-transmission/article/55324933/transforming-the-us-grid-the-impact-and-engineering-of-the-grain-belt-express-hvdc-line (2026)
53. Utmel, "SiC and GaN in 2026: How SiC and GaN…" — https://www.utmel.com/blog/categories/powersupply/sic-and-gan-in-2026-how-sic-and-gan-power-devices-are-redefining-ai-data-centers-and-800v-evs (2026)
54. Power Electronics News, "Real-World SSTs Target AI Data Centers and Grid Modernization" — https://www.powerelectronicsnews.com/real-world-solid-state-transformers-overcome-barriers-to-meet-adoption-needs-of-ac-and-dc-networks/ (2026)
55. AutoTech News, "SiC, GaN Oversupply to Persist Despite EV and AI…" — https://autotech.news/sic-gan-oversupply-to-persist-despite-ev-and-ai-demand/ (2026)
56. IEA, "Global EV Outlook 2026 — Executive summary" — https://www.iea.org/reports/global-ev-outlook-2026/executive-summary (2026)
57. IEA, "Global EV Outlook 2026 — Manufacturing and trade" — https://www.iea.org/reports/global-ev-outlook-2026/manufacturing-and-trade (2026)
58. IEA, "Heat Pump Monitor 2026 — Key findings" — https://www.iea.org/reports/heat-pump-monitor-2026/key-findings (2026)
59. European Heat Pump Association, "Why heat pump sales are growing again" — https://ehpa.org/news-and-resources/news/why-heat-pump-sales-are-growing-again/ (2026)
60. SpaceNews, "Space-based solar power startup Aetherflux enters orbital data center…" — https://spacenews.com/space-based-solar-power-startup-aetherflux-enters-orbital-data-center-race/ (2026)
61. New Atlas, "Aetherflux: Space solar startup aims for 2026 laser power…" — https://newatlas.com/energy/laser-beamed-space-solar-power-aetherflux-2026-test/ (2026)

---

*Compiled 2026-09-07. Where a figure appears in multiple sources with conflicting values (notably global solar 2026: BNEF ~649 GW vs IEA ~540 GW), both are given rather than reconciled — the divergence is mostly DC-vs-AC accounting and differing China assumptions, and is itself informative about forecast uncertainty.*
