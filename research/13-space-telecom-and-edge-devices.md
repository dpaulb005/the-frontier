# The Frontier #13 — Space, Telecom, and Edge AI Hardware
### State of play as of 7 September 2026

**Labels:** **[CONFIRMED]** = primary source or uncontested first-party event; **[REPORTED]** = credible press, possibly single-source; **[SPECULATION]**/**[ANALYSIS]** = my inference.

---

## TL;DR

1. **Starship flew V3 twice and still has not refueled in orbit.** Flight 13 (24 July 2026) was the second V3 flight; ship-to-ship propellant transfer is the gating item for everything lunar and Martian, now targeted for late 2026 [REPORTED]. [1][6]
2. **NASA restructured Artemis, on the record.** Artemis II flew crewed around the Moon over ~10 days in April 2026 [CONFIRMED]; NASA's own mission page now describes **Artemis III (2027) as a low-Earth-orbit demonstration** of the SpaceX and Blue Origin landers, with the **first crewed landing on Artemis IV in 2028** [CONFIRMED]. The "return to the Moon" moved by redefinition rather than by a slip announcement. [7][8]
3. **Direct-to-device stopped being a demo.** Starlink D2C runs 650+ operational satellites with a reported ~16M unique carrier-partner users; AST SpaceMobile is FCC-authorized for up to 248 satellites and flying Block 2 BlueBirds on Falcon 9 [REPORTED/CONFIRMED]. [2][3]
4. **Amazon Leo (ex-Kuiper) is real, behind, and got a regulatory reprieve.** 396 production satellites launched as of July 2026 against a 3,236-satellite design; the FCC **waived** the "half the constellation by July 2026" milestone in June 2026 but will temporarily demote the spectral priority of satellites launched after it [CONFIRMED]. Enterprise beta is live; early consumer service is anticipated during 2026. [4]
5. **China is the volume story.** Guowang and Qianfan together are consuming an estimated 70+ launches in 2026, with a combined few hundred satellites on orbit against ITU deadlines — deployment rate, not technology, is the binding constraint [REPORTED]. [5]
6. **Orbital datacenters went from meme to funded.** Starcloud raised $170M at ~$1.1B and filed for an 88,000-satellite, ~20 GW compute constellation; Google's Project Suncatcher targets prototype TPU satellites in early 2027 [REPORTED]. Physics is plausible; economics rest entirely on Starship-class launch cost. [9][10]
7. **6G now has hard dates.** 3GPP approved the Release 21 timeline in June 2026: first functional freeze March 2027, 80% checkpoint March 2028, second functional freeze June 2028, stage-3 freeze December 2028, **full code freeze March 2029** — meaning the first 6G specifications land in early 2029 [CONFIRMED]. Commercial 6G is a 2030 story, not a 2028 one. [11][12]
8. **OpenAI's hardware slipped a year.** The Jony Ive-designed, screen-free, pocket device won't ship before end of February 2027, and it will not be called "io" after the iyO trademark suit [REPORTED]. [13]
9. **Smart glasses are the consumer AI form factor that actually shipped.** Meta has Ray-Ban Display ($799, neural wristband), Oakley Meta, and from June 2026 its own $299 Meta Glasses; Apple's non-display N50 glasses are now a late-2027 story [CONFIRMED/REPORTED]. [14][15][17]
10. **The memory squeeze is the biggest under-covered consumer-tech story.** A reported ~130% combined DRAM+SSD price surge through 2026 translates to roughly +17% PC and +13% smartphone prices [REPORTED]. AI datacenter capex is now directly taxing consumer hardware. [16]

---

## A. SPACE

### A1. Starship V3 and the refueling gate

Starship V3 — taller ship, new engines, and crucially the docking hardware and quick-disconnect plumbing needed for propellant transfer — flew Flight 13 on 24 July 2026, the 13th integrated test and second V3 flight [REPORTED]. [1][6]

The single most important number in the American space program right now is zero: **the number of times two Starships have docked in orbit and moved propellant** [CONFIRMED — by absence]. The demonstration is currently NET late 2026 [REPORTED]. [6] Everything downstream depends on it: roughly **ten tanker launches** are needed to fill a propellant depot sufficiently for one Starship HLS lunar landing [REPORTED], and NASA's lunar landing program manager has said publicly that the autonomous transfer flights will have to be done "more than once or twice or three times" before crewed Artemis missions proceed [REPORTED]. [6] The transfer itself is planned to work by docking two vehicles in LEO and using a pressure differential to push propellant from one into the other. [6]

**[SPECULATION]** The demo will succeed technically well before the *cadence* exists to make it useful. Transferring propellant once is an engineering milestone; doing it ten-plus times inside a boiloff-limited window with rapid pad turnaround is an industrial one. That gap is where Artemis schedules go to die.

### A2. Starlink at scale

Starlink's scale is now unambiguous: approximately **10,413 satellites on orbit (10,397 operational) as of June 2026** [CONFIRMED], **more than 12 million subscribers as of June 2026** — up from 10.3 million in March 2026, i.e. roughly 1.7M net adds in a quarter [CONFIRMED] — and **$11.4B revenue with $4.4B operating income in 2025**, making it SpaceX's largest business by a wide margin [CONFIRMED]. [2] That operating margin (~39%) is the number that matters: Starlink is no longer a capex story, it is a cash generator funding Starship. More striking still is the mobile side: Direct-to-Cell reportedly passed 650 operational satellites by April 2026, with ~16M unique users touched through carrier partners (T-Mobile, KDDI, Optus, One NZ, Rogers, Telstra and others) and a target of ~25M active by year-end [REPORTED]. [2][3]

V3 satellites — spec'd at roughly 10x downlink and 24x uplink capacity versus V2 Mini, and too large for Falcon 9 — are the payload that makes Starship economically necessary rather than merely impressive [REPORTED]. [2] Laser inter-satellite links carry the large majority of Starlink traffic and are what make ocean, polar and aviation markets viable without ground-station buildout [CONFIRMED].

### A3. Amazon Leo, AST SpaceMobile, and the challengers

**Amazon Leo** (renamed from Project Kuiper in November 2025) entered enterprise beta in April 2026 with terminal tiers up to ~1 Gbps and named partners including Verizon, AT&T, Vodafone, JetBlue and NASA [REPORTED]. [4] As of July 2026 it had launched **396 production satellites** (plus 2 earlier prototypes) toward a **3,236-satellite** constellation across three shells at 590/610/630 km in 98 planes [CONFIRMED]. [4] The FCC's original "half the constellation by 30 July 2026" milestone was **waived** in June 2026; the penalty is that satellites launched after the milestone date get temporarily demoted spectral priority — a meaningful but survivable cost [CONFIRMED]. [4] Amazon has begun international distribution deals (e.g. Herotel in South Africa, July 2026), and early service is anticipated during 2026 [CONFIRMED]. [4]

Secondary trackers circulate wildly inconsistent Leo counts (210, 241, 365); 396 is the figure tied to launch manifests [ANALYSIS].

**AST SpaceMobile** received FCC authorization on 21 April 2026 to provide direct-to-smartphone broadband in the US **with up to 248 satellites**, an order that also covers its arrangement to use the AT&T-operated FirstNet public-safety spectrum for first responders [CONFIRMED]. [3] Block 2 BlueBirds — physically enormous phased arrays built for roughly double Block 1 peak speeds — began flying on Falcon 9 in June 2026 (BlueBird 8-10), with BlueBird 11-13 following in August [REPORTED]. [3] A **botched launch complicated the 2026 deployment ramp** [REPORTED], which matters more than the headline approval: AST's constellation is small-N, so each vehicle lost is a material fraction of service capability. The company reports agreements with roughly 60 mobile networks including AT&T, Verizon and Vodafone; beta service with AT&T/FirstNet was targeted for H1 2026 and commercial service awaits roughly 45-60 satellites, nominally 2027 [REPORTED]. [3]

**[SPECULATION]** Starlink D2C and AST are not really competing on the same axis. Starlink optimizes for *coverage-of-last-resort* at low bandwidth across a huge installed satellite base; AST optimizes for *actual broadband to an unmodified phone* from far fewer, far larger satellites. If AST's Block 2 arrays perform, the interesting competitive question in 2027 is whether SpaceX responds with a large-aperture D2C satellite that only Starship can loft.

### A4. Chinese megaconstellations

Guowang (state-backed) and Qianfan/Thousand Sails (Shanghai-backed, export-oriented) are why China's launch rate is climbing steeply: an estimated 45 launches consumed in 2025 and 70+ projected for 2026, batches going up every two to three weeks across four launch sites [REPORTED]. [5] On-orbit counts remain modest against plans — roughly 177 Guowang (late July 2026) and ~200 Qianfan (June 2026) versus combined ambitions above 29,000 satellites and hard ITU milestones. [5]

**[SPECULATION]** China's constraint has flipped from "can we build satellites cheaply" (CGTN claims a >96% Qianfan cost reduction [REPORTED]) to "can we launch them fast enough." Until a reusable Chinese booster is flying at cadence, the ITU deadlines will be met by paperwork and partial deployments rather than full constellations.

### A5. Orbital datacenters

The most vertiginous change since 2025 is that "put the datacenter in orbit" acquired real balance sheets.

- **Starcloud** (formerly Lumen Orbit) flew Starcloud-1 with an NVIDIA H100 in November 2025, raised a $170M Series A at ~$1.1B in March 2026, and filed with the FCC in February 2026 for an 88,000-satellite, ~20 GW constellation; Starcloud-2, with a Blackwell-class cluster, is slated for late 2026 [REPORTED]. NVIDIA is supplying radiation-tolerant inference hardware and frameworks [REPORTED]. [9][10]
- **Google Project Suncatcher** (announced November 2025) proposes tight formations of TPU-carrying solar satellites linked by free-space optical laser, prototypes targeted early 2027 [REPORTED]. [10]
- **Axiom Space** launched its first orbital datacenter nodes in January 2026 on Kepler's optical relay network [REPORTED]. [9]

The pitch: continuous carbon-free solar at multiples of terrestrial yield in the right orbit, no land/water/grid-interconnect queue. The documented objections are consistent across sources [CONFIRMED]: thermal rejection in vacuum is hard (radiators, not chillers, under strict mass-to-area constraints); radiation hardening of TPUs/GPUs needs shielding plus error correction; launch cost for power-dense payloads; optical ground links degrade with cloud, fog and aerosols; and debris/deorbit compliance in crowded LEO. [10]

**[SPECULATION]** Space compute makes sense first for workloads that are *generated* in space (Earth observation, SAR, constellation telemetry) — reduce-before-downlink — and only much later for training frontier models. The 20 GW filings are option value on launch cost, not a plan. Watch the radiator area per megawatt figure; it's the number that decides whether this is a business or a press release.

### A6. Artemis, CLPS, and the Moon

Artemis II flew a nearly 10-day voyage around the Moon in April 2026 with Wiseman, Glover, Koch and Hansen, travelling 252,756 miles from Earth — the first crewed flight of Orion and a human distance record [CONFIRMED]. [7]

NASA then restructured the sequence, and now says so on its own mission pages [CONFIRMED]: **Artemis III (2027) is a low-Earth-orbit demonstration** evaluating the SpaceX and Blue Origin human landing systems and the rendezvous/docking operations a surface mission requires; **Artemis IV (2028) carries the first crewed landing**, with crew transferring from Orion to a commercial lander. NASA has standardized the SLS configuration from Artemis IV onward and states an intent to sustain roughly one mission per year thereafter, and frames the 2028 landing date as having "remained consistent since mid-2025." [7][8]

**[SPECULATION]** The restructuring is the honest engineering call given HLS maturity — neither Starship HLS nor Blue Moon Mk2 will be crew-rated before 2028 — but the framing is generous. A LEO lander demo is not what "Artemis III" meant in 2024. And the 2028 landing date is downstream of a propellant-transfer campaign that has not started: ten-plus tanker flights per mission, needing to be flown several times in demonstration first. My base case for boots on the Moon is **2029-2030** [SPECULATION], with a real (not trivial) chance China's 2030 crewed-landing target lands within the same window.

CLPS continues as the low-cost, high-variance arm: Firefly's Blue Ghost 1 (March 2025) remains its cleanest success [CONFIRMED], with Intuitive Machines, Astrobotic, Blue Origin and Firefly flying or preparing missions across 2026.

### A7. Launch cost trends

Falcon 9 list price sits near $70M for ~17-18 t to LEO (~$3,000-4,000/kg), rideshare near $6,000/kg for smallsats [CONFIRMED, published pricing]. Starship's marginal cost is the open question: SpaceX aspires to sub-$100/kg at high cadence [REPORTED]; realistic near-term figures are more likely $500-1,500/kg [SPECULATION]. Even the pessimistic end is a 3-5x reduction — the assumption underwriting orbital datacenters, V3 Starlink and lunar architecture alike.

---

## B. TELECOM

### B1. The 6G calendar is now fixed

3GPP approved Release 21 timelines in June 2026 [CONFIRMED]. [11] The shape:

- **Rel-20** (studies, running from H2 2025 over roughly 21 months): 6G requirements, use cases, architecture; simultaneously the third phase of 5G-Advanced.
- **Rel-21** (normative): the first actual 6G specifications for RAN and Core, spread across TSG RAN, SA and CT. Approved milestones [CONFIRMED]: **first functional freeze March 2027**, **80% checkpoint March 2028**, **second functional freeze June 2028**, **stage-3 freeze December 2028**, **full code freeze March 2029** — putting the first 6G specs in early 2029. [11]
- **ITU-R IMT-2030**: 3GPP submits its radio interface technologies to ITU-R WP5D for evaluation; technology proposals are due early 2029 with final specifications by mid-2030. [12]
- **Checkpoints to watch**: WRC-27 (October-November 2027), which allocates the spectrum 6G will actually use, and the 2028 Los Angeles Olympics, historically a showcase deadline that pulls pre-standard deployments forward. [11]

**[SPECULATION]** That means first commercial 6G networks in 2030 at the earliest, with meaningful coverage 2032+. Any vendor marketing "6G" hardware before 2029 is selling 5G-Advanced with a new sticker. The genuinely new items in the 6G basket — integrated sensing and communication (ISAC), AI-native air interface, and NTN-as-a-first-class-citizen — are the ones worth tracking, because they change what the network *is for*, not just how fast it is.

### B2. AI-native RAN and Open RAN

The industry's actual 2026 activity is not 6G; it is stuffing accelerators into the RAN. AI-RAN (NVIDIA's ARC/Aerial with SoftBank, Nokia and others) runs RAN L1 and AI inference on shared GPU infrastructure, monetizing idle cell-site compute [REPORTED]. Open RAN has settled into a less revolutionary reality: real deployments (AT&T/Ericsson, Vodafone, Rakuten) but consolidation around a few vendors rather than the open marketplace promised [REPORTED].

**[SPECULATION]** AI-RAN is a *cost* story (one box, two workloads) masquerading as a *revenue* story (edge inference marketplaces). The revenue thesis needs latency-sensitive inference demand that does not yet exist at the cell site — most inference is content in a regional datacenter 20 ms away, or on the device itself.

### B3. Direct-to-device and NTN

3GPP NTN (Rel-17 onward) is the standards spine under both Starlink D2C and AST. The 2026 state: NB-IoT NTN is broadly commercial, NR-NTN is deploying, and the industry fight is over *spectrum* — whether D2D uses terrestrial MNO spectrum (Starlink/T-Mobile, AST/AT&T) or dedicated MSS spectrum (the EchoStar/SpaceX spectrum transactions, Apple/Globalstar) [REPORTED].

**[SPECULATION]** The endgame is that satellite connectivity becomes an invisible tier of the carrier plan, priced at zero, used for messaging and emergency by 99% of users and for real bandwidth by ships, planes, and remote industry. That kills the standalone satellite-phone market and makes constellation operators into wholesale capacity vendors — a lower-margin business than the current narratives assume.

### B4. Terahertz

Sub-THz (100-300 GHz) research continues at Nokia Bell Labs, NTT Docomo, Samsung and in the EU Hexa-X-II program, with lab demos in the hundreds of Gbps [REPORTED]. **[SPECULATION]** THz will not be a 6G coverage layer; its realistic near-term uses are fixed wireless backhaul, datacenter interconnect and short-range sensing. Anyone promising THz to a handset is describing 7G.

---

## C. EDGE AND CONSUMER AI HARDWARE

### C1. The OpenAI device

Status: **delayed to 2027** [REPORTED]. OpenAI has indicated its first hardware won't ship before the end of February 2027, versus an original end-of-2026 goal. [13] It will not carry the "io" name after the iyO trademark litigation. Reported design: pocket-sized, screen-free, always-listening, context-aware, in a $200-$300 range, built around an ambient-assistant interaction model.

**[SPECULATION]** This reads as a hard-problems delay, not a manufacturing one. A screen-free ambient device needs three unsolved things: conversational latency (pushing toward on-device models), multi-day battery with always-on sensing, and a social contract for a live microphone in a shared room — a design and policy problem, not a silicon one. Meta partly solved the third by putting the device on your face where others can see it; a pocket puck has no such affordance. Roughly even odds on another slip past 2027.

### C2. Smart glasses became the fight

**Meta** is furthest along, and moved from partner-branded to own-branded hardware in 2026. The lineup now spans Ray-Ban Meta (since 2023), Oakley Meta HSTN and Vanguard (2025), **Meta Ray-Ban Display** — the first with an integrated display plus the sEMG Neural Band wristband, launched at $799 with a 600x600, ~20° FoV, up-to-5,000-nit monocular display [CONFIRMED] [14] — and, from **23 June 2026, Meta's own-brand "Meta Glasses" at $299** [CONFIRMED]. [15] Cumulative Ray-Ban Meta sales reportedly passed 2M units by early 2026, with as many as four further models reportedly planned across 2026 (codenames Modelo, Luna, an RBM2 refresh, Mojito) plus an AI pendant [REPORTED]. Handwriting input via the Neural Band was on the 2026 roadmap [REPORTED]. **Orion**, the binocular AR prototype with silicon-carbide waveguides, remains a research vehicle — Meta has acknowledged it was too expensive to manufacture for consumers and pivoted to Ray-Ban Display instead [CONFIRMED]. [15]

**Apple** has reportedly deprioritized the Vision-family cheap headset in favor of **N50**, a display-free, audio-and-camera, Siri-driven glasses product now targeted for roughly late 2027, with "Vision Air" pushed to 2028 or later [REPORTED]. [17] Price talk is $200-$500.

**Google/Samsung** shipped **Galaxy XR** (formerly Project Moohan) on 21 October 2025 at $1,799, the first Android XR device, with European and Canadian market expansion during 2026 [CONFIRMED]. [18] Google's glasses partnerships (Warby Parker, Gentle Monster, Kering) target 2026-2027 products.

**[SPECULATION]** The 2026 lesson: *display-free camera-and-audio glasses with a good assistant* is the volume product; heads-up display glasses are the enthusiast tier. Apple arriving in 2027 with a display-free design validates Meta's read of the market — but arriving two years late into a category where Meta owns the eyewear-brand relationships is a weak position by Apple's own standards.

### C3. On-device models and the NPU race

Silicon, 2026 vintage [REPORTED, benchmark-derived]:

- **Qualcomm Snapdragon X2 Elite / Elite Extreme**: 80 TOPS Hexagon NPU; reported to beat Apple M5 and Intel Panther Lake on AI benchmark composites, and in some tests to beat Apple on general performance for the first time. [19]
- **Intel Panther Lake (Core Ultra 3)**: ~50 TOPS NPU, ~180 TOPS platform-wide (CPU+GPU+NPU), on 18A. [19]
- **Apple M5 / A19 Pro**: Apple moved neural acceleration *into every GPU core* rather than scaling the discrete Neural Engine, and does not publish a comparable NPU TOPS figure. M5 Max offers up to 614 GB/s unified memory and 128 GB capacity. [19]

**[SPECULATION]** TOPS is now close to meaningless as a comparison metric, and Apple's refusal to play the number game is the tell. For local LLM inference, the binding constraint is **memory bandwidth and capacity**, not multiply-accumulate throughput. A 614 GB/s, 128 GB machine runs models an 80-TOPS, 32 GB machine simply cannot load. Expect marketing to pivot from TOPS to "tokens/sec at Q4" during 2027.

On models: Gemini Nano ships across Pixel and increasingly third-party Android via ML Kit GenAI APIs; Apple's Foundation Models framework exposes its ~3B on-device model to third-party developers [CONFIRMED]; and the open small-model tier (Qwen, Gemma, Llama, Phi, SmolLM) has made 3-8B models genuinely useful at 4-bit on a phone [CONFIRMED]. Siri's rebuild — App Intents-driven, able to take actions in apps, and reportedly leaning on Google Gemini for some server-side reasoning — was targeted at spring 2026 and is still being refined, with the glasses timeline explicitly gated on it [REPORTED]. [17]

### C4. The memory shock

This is the story that touches every device in this section. AI datacenter demand pulled fab capacity toward HBM, starving conventional DRAM and NAND. Reported effects [REPORTED]: [16]

- DRAM contract prices up roughly 125% and NAND up ~234% across the cycle, with Q2 2026 quarter-over-quarter jumps near 60% moderating to 13-18% (DRAM) and 10-15% (NAND) in Q3 2026.
- Gartner's estimate: ~130% combined DRAM+SSD price surge by end-2026 vs 2025, pushing PC prices +17% and smartphone prices +13%.
- NVIDIA's reported ~$500B memory supply commitment with SK Hynix locked up future capacity ahead of consumer buyers.
- No meaningful relief expected before late 2027.

**[SPECULATION]** Second-order effects to watch: (1) base RAM/storage configs stop increasing or *regress* on mid-range phones and laptops — the first time in two decades; (2) on-device AI gets squeezed exactly when it needs more memory, because a 7B model at 4-bit wants 4-6 GB of headroom; (3) the "AI PC" upsell becomes harder to justify when the same money buys a device with less RAM than last year's. AI capex is now visibly regressive: datacenter buildouts are raising the price of consumer computing.

---

## What people are underestimating

**[ANALYSIS — all items are my judgment, not reporting]**

1. **Orbital refueling is a cadence problem, not a docking problem.** The public conversation treats the first successful transfer as the milestone. It isn't — the milestone is the tenth transfer inside a boiloff-limited window. Pad turnaround and tanker production rate are the real constraints, and neither is demonstrated.

2. **Space compute will arrive through Earth observation, not AI training.** Everyone models orbital datacenters as "cheaper GPU-hours." The near-term winner is reducing petabytes of SAR and hyperspectral data to kilobytes before downlink, where the alternative isn't a terrestrial datacenter — it's not getting the data at all. That's a real business today at small scale.

3. **The memory shock is the most consequential consumer-tech event of 2026 and is being covered as a PC-enthusiast story.** A 13-17% across-the-board price rise in phones and PCs sustained for two years outweighs any AI feature shipped this year. It suppresses upgrade cycles, shrinks base configurations, and directly constrains on-device AI.

4. **6G's real content is non-terrestrial and sensing, not speed.** The bandwidth story is exhausted; nobody needs 1 Tbps to a handset. The reason to care about Rel-21 is that satellite access and radar-like environmental sensing become native network functions. That reshapes who the network operators' competitors are — SpaceX becomes a peer, not a partner.

5. **Direct-to-device commoditizes satellite operators faster than it enriches them.** Once every carrier plan includes satellite messaging at no incremental cost, constellation operators are wholesale capacity vendors competing on price, with enormous capex and short satellite lifetimes. The consumer surplus is huge; the producer surplus is contested.

6. **Meta has quietly built a distribution moat that Apple cannot buy.** EssilorLuxottica owns Ray-Ban, Oakley, Persol, and most of the world's optical retail. Meta's partnership with them is the single most underrated strategic asset in consumer hardware. Apple's 2027 glasses will be excellent and will lack a place to sell prescription lenses.

7. **The screen-free ambient device category may not exist.** The OpenAI device, Humane's failure, and Rabbit's failure share an assumption: that voice-plus-context can replace a screen. The evidence so far is that it can't for output density, and that a device without a screen ends up needing a phone anyway. Glasses work because they *add* a display and a socially legible camera. A puck does neither.

8. **Chinese constellations will meet ITU deadlines nominally and fail them practically** — enough satellites in enough planes to preserve filings, far short of service capability. The interesting date is not 2026 or 2027 but whenever a reusable Chinese first stage reaches cadence; that's the step change.

9. **Artemis has become a schedule-management exercise rather than a program.** Restructuring Artemis III into a LEO demo preserved the "Artemis III in 2027" headline while moving the landing. Expect further redefinition. The competitive framing against China's 2030 crewed-landing target is now genuinely close.

10. **The NPU TOPS race is already over and everyone is still running it.** Memory bandwidth and capacity determine what models a device can run. Apple's architecture bets on that; the TOPS leaders are optimizing a metric that stopped predicting user-visible capability around the time 4-bit 7B models became good.

---

## Key numbers

| Item | Value | Date | Label |
|---|---|---|---|
| Starship integrated test flights / orbital propellant transfers | 13 / **0** | Sep 2026 | REPORTED [1][6] |
| Starlink satellites on orbit / operational | 10,413 / 10,397 | Jun 2026 | CONFIRMED [2] |
| Starlink subscribers | >12M (10.3M in Mar 2026) | Jun 2026 | CONFIRMED [2] |
| Starlink 2025 revenue / operating income | $11.4B / $4.4B | 2025 | CONFIRMED [2] |
| Starlink D2C satellites operational | 650+ | Apr 2026 | REPORTED [2] |
| Amazon Leo production satellites launched | 396 | Jul 2026 | CONFIRMED [4] |
| Amazon Leo FCC half-constellation milestone | waived Jun 2026; spectral priority demoted | Jun 2026 | CONFIRMED [4] |
| AST SpaceMobile FCC authorization | up to 248 satellites | 21 Apr 2026 | CONFIRMED [3] |
| Guowang satellites on orbit | ~177 | late Jul 2026 | REPORTED [5] |
| Qianfan satellites on orbit | ~200 | Jun 2026 | REPORTED [5] |
| Starcloud Series A / valuation | $170M / $1.1B | Mar 2026 | REPORTED [9] |
| Starcloud FCC filing | 88,000 sats / ~20 GW | Feb 2026 | REPORTED [9] |
| Artemis III | LEO lander demo, 2027 | restructured 2026 | CONFIRMED [7] |
| Artemis crewed landing | Artemis IV, 2028 | restructured 2026 | CONFIRMED [7] |
| Tanker flights per Starship HLS lunar mission | ~10 | 2026 | REPORTED [6] |
| 3GPP Rel-21 full code freeze | Mar 2029 | approved Jun 2026 | CONFIRMED [11] |
| First 6G specifications available | early 2029 | approved Jun 2026 | CONFIRMED [11] |
| OpenAI device ship date | not before end Feb 2027 | Feb 2026 | REPORTED [13] |
| Meta Ray-Ban Display price | $799 | Sep 2025 | CONFIRMED [14] |
| Meta own-brand "Meta Glasses" price | $299 | 23 Jun 2026 | CONFIRMED [15] |
| Apple N50 glasses target | ~late 2027 | Feb 2026 | REPORTED [17] |
| NPU: Snapdragon X2 Elite Extreme / Panther Lake | 80 / ~50 TOPS (~180 platform) | 2026 | REPORTED [19] |
| Apple M5 Max memory bandwidth | up to 614 GB/s | 2026 | REPORTED [19] |
| DRAM + SSD price surge to end-2026 | ~130% combined | 2026 | REPORTED [16] |
| Resulting PC / smartphone price rise | +17% / +13% | 2026 | REPORTED [16] |

---

## Sources

1. Space.com — SpaceX stacks Starship V3, completes fueling test — https://www.space.com/space-exploration/launches-spacecraft/spacex-stacks-starship-v3-rocket-completes-major-fueling-test-ahead-of-debut-launch (2026)
2. Wikipedia — Starlink (sat counts, subscribers, 2025 revenue/op income) — https://en.wikipedia.org/wiki/Starlink (accessed Sep 2026); Starlink Direct to Cell brief — https://starlink.com/public-files/DIRECT_TO_CELL_SERVICE_FEB_25.pdf; KeepTrack — D2C status — https://keeptrack.space/deep-dive/starlink-direct-to-cell (2026)
3. SpaceNews — FCC clears AST SpaceMobile constellation (248 sats, 21 Apr 2026) — https://spacenews.com/fcc-clears-ast-spacemobile-constellation-as-launch-setback-clouds-ramp-up/ (2026); Spaceflight Now — Block 2 BlueBird launch — https://spaceflightnow.com/2026/06/16/live-coverage-spacex-to-launch-3-block-2-bluebird-satellites-for-ast-spacemobile/ (16 Jun 2026)
4. Wikipedia — Amazon Leo (396 sats Jul 2026, FCC waiver Jun 2026, 3,236-sat design) — https://en.wikipedia.org/wiki/Amazon_Leo (accessed Sep 2026); Fierce Network — Amazon Leo enterprise beta — https://www.fierce-network.com/broadband/amazon-leo-previews-its-satellite-broadband-enterprises (2026)
5. KeepTrack — China launch cadence and constellations 2026 — https://keeptrack.space/deep-dive/china-launch-cadence-2025-2026 (2026); China in Space — mega-constellations — https://www.china-in-space.com/p/chinas-mega-constellations-mega-article (2026)
6. Wikipedia — Starship Propellant Transfer Demonstration (NET late 2026; ~10 tanker launches per HLS mission) — https://en.wikipedia.org/wiki/Starship_Propellant_Transfer_Demonstration (accessed Sep 2026)
7. NASA — Moon to Mars / Artemis (Artemis II Apr 2026; Artemis III 2027 LEO lander demo; Artemis IV 2028 landing) — https://www.nasa.gov/humans-in-space/artemis/ (accessed Sep 2026)
8. CSIS — What Comes Next for Artemis? — https://www.csis.org/analysis/what-comes-next-artemis (2026); NASA — adds mission to Artemis lunar program, updates architecture — https://www.nasa.gov/news-release/nasa-adds-mission-to-artemis-lunar-program-updates-architecture (2026)
9. Fierce Network — Space data centers: Starcloud, SpaceX and Project Suncatcher explained — https://www.fierce-network.com/cloud/space-data-centers-starcloud-spacex-and-project-suncatcher-explained (2026)
10. Data Center Frontier — Google and NVIDIA test space data centers — https://www.datacenterfrontier.com/site-selection/article/55328204/when-the-cloud-leaves-earth-google-and-nvidia-test-space-data-centers-for-the-orbital-ai-era (2026)
11. IEEE ComSoc — 3GPP approves Release 21 timelines (freezes Mar 2027 / Mar 2028 / Jun 2028 / Dec 2028 / Mar 2029) — https://techblog.comsoc.org/2026/06/16/3gpp-approves-timelines-for-release-21-which-will-specify-6g-ran-and-5g-advanced/ (16 Jun 2026)
12. 3GPP — Rel-20 planning and progress in TSG SA — https://www.3gpp.org/news-events/3gpp-news/sa-rel20 ; ITU-R IMT-2030 timeline discussion — https://techblog.comsoc.org/2025/07/22/itu-r-wp5d-imt-2030-submission-evaluation-guidelines-vs-6g-specs-in-3gpp-release-20-21/
13. MacRumors — OpenAI's Jony Ive-designed device delayed to 2027 — https://www.macrumors.com/2026/02/10/openais-jony-ive-designed-device-delayed-to-2027/ (10 Feb 2026); 9to5Mac — won't be called io — https://9to5mac.com/2026/02/10/jony-ives-ai-hardware-is-delayed-to-2027-and-wont-be-called-io/ (10 Feb 2026)
14. Meta — Meta Ray-Ban Display AI glasses (Connect 2025) — https://www.meta.com/blog/meta-ray-ban-display-ai-glasses-connect-2025/ (Sep 2025)
15. Wikipedia — Ray-Ban Meta ($299 Meta Glasses Jun 2026, Orion pivot) — https://en.wikipedia.org/wiki/Ray-Ban_Meta (accessed Sep 2026)
16. Tom's Hardware — Memory price surge begins to cool — https://www.tomshardware.com/pc-components/ram/memory-price-surge-begins-to-cool-as-consumers-hit-affordability-limit-ai-demand-still-keeps-dram-and-nand-prices-climbing-through-q3-2026 (2026); NAND Research — Memory & Flash Crisis update — https://nand-research.com/memory-flash-crisisc-update-march-2026/ (Mar 2026)
17. AppleInsider — Apple eyes 2027 for AI smart glasses built around context — https://appleinsider.com/articles/26/02/17/apple-eyes-2027-for-ai-smart-glasses-built-around-context-not-screens (17 Feb 2026)
18. Android Central — Samsung Galaxy XR — https://www.androidcentral.com/gaming/virtual-reality/samsung-galaxy-xr (2026)
19. Windows Central — Snapdragon X2 Elite Extreme vs Panther Lake (Signal65 lab report) — https://www.windowscentral.com/hardware/qualcomm/snapdragon-x2-elite-extreme-intel-amd-tests-signal65 (2026); Tom's Guide — Apple M5 vs Panther Lake vs Snapdragon X2 — https://www.tomsguide.com/computing/apple-m5-vs-intel-vs-amd-vs-snapdragon-x2-which-chip-wins (2026)
