# Fiber-Optic Drone Control: State of the Art and Applications (September 2026)

*Claims labeled **CONFIRMED** (primary or multiply-sourced), **REPORTED**
(single credible outlet, not independently verified), **SPECULATION**
(projection or analysis). Companion to brief 17 on the RF frontier, which
treats fiber drones only as a counter-signal to RF-defeat businesses.*

---

## TL;DR

1. **The technology is a spool of hair-thin glass, not a radio.** Current
   production drones carry 10-50 km of G.657.A2 bend-insensitive single-mode
   fiber at roughly 0.26 mm outer diameter, unspooled in flight. There is no
   radio emission to jam, detect, or direction-find. **CONFIRMED** [1][2]
2. **Scale is enormous and mostly Russian.** Russia doubled fiber FPV output
   to more than 50,000 units per month by September 2025 and reportedly
   consumes ~13 million km of fiber annually for drones. Combined Russian and
   Ukrainian consumption ran 50-60 million km in 2025. **REPORTED** [1][3]
3. **Ukraine trails structurally because it does not draw its own fiber.**
   It imports the glass and assembles spools; Russia draws domestically at
   Saransk and partners with China. 352,000 fiber FPVs were delivered to
   Ukrainian forces from July 2025 onward. **REPORTED** [3][4]
4. **The single most interesting fact: AI datacenters and drone warfare are
   now bidding for the same fiber.** G.657.A2 is the preferred fiber for
   dense datacenter cabling *and* for tight drone spools. Chinese fiber went
   from ~$2.33/km (Jan 2025) to ~$5.83/km (Jan 2026); Western G.657.A2 quoted
   at $33-35/km in March 2026. A delivered 50 km spool went from ~$300 to
   ~$2,500, an eightfold rise. **REPORTED** [1]
5. **Range reached 50 km in service.** Ukrainian operators have struck rear-area
   storage sites at that range; Russia has reportedly fielded 40-mile-class
   optical drones with Chinese collaboration. **REPORTED** [2][5]
6. **The costs are physical, not electronic.** Spool mass displaces warhead
   mass, the drone is heavier and louder, the cable snags in woodland and
   urban terrain, and a single sharp kink ends the mission. Flight paths must
   be planned around the cable. **CONFIRMED** [6][7]
7. **The counter is sensing and hard kill, never jamming.** With no emission
   to attack, defeat has shifted to radar plus electro-optical/infrared plus
   acoustics with AI classification, then high-power microwave, guns, nets,
   or lasers. The US Army has published on the C-UAS problem it creates; the
   UK opened a market engagement in April 2026 specifically for anti-fiber
   technologies; the US Marine Corps funded a microwave defeat effort. **CONFIRMED** [7][8][9]
8. **The architecture is already hybridizing.** Ukrainian units fielded dual
   fiber-plus-radio drones in March 2026 that fall back to RF when the cable
   breaks, for about $60 extra per airframe. **REPORTED** [10]
9. **Civilian use is real but narrow**: inspection where radio does not
   propagate or is not permitted — mines, tunnels, sewers, ship hulls,
   substations, offshore platforms, chemical plants. Persistent tethered
   drones for hours-long 4K inspection with zero spectrum contention are in
   pilot or limited production. **REPORTED** [11][12]
10. **Analytical call: fiber is a transitional technology, squeezed from both
    ends.** Datacenter demand is raising its unit cost while onboard autonomy
    is removing the need for any link at all. It wins where terminal guidance
    is not yet good enough and the environment is RF-hostile. That window is
    real now and closing. **SPECULATION**

---

## 1. How it actually works

A fiber-controlled first-person-view drone replaces the radio downlink and
uplink with a physical optical fiber paid out from a spool as the aircraft
flies. Video comes back down the glass and control goes up it. The relevant
engineering facts:

**The fiber.** G.657.A2 is a bend-insensitive single-mode fiber standardized
for tight-radius routing. Bend insensitivity is the whole reason it works
here: the fiber must be wound onto a small spool and pay out under tension
without macrobend loss destroying the link budget. Outer diameter on fielded
spools is about 0.26 mm [1][2]. **CONFIRMED**

**The dispensing problem is the hard part.** The spool must pay out from the
*inside* without back-tension spikes, twisting, or tangling, across a flight
that changes speed and direction. This is the actual intellectual property in
a fiber drone; the electro-optics are commodity. Spool quality is what
separates a 5 km effective range from a 20 km one on identical glass.
**SPECULATION**, though consistent with the reported gap between nominal
spool length and achieved range.

**Link properties.** Because the channel is a waveguide, the drone emits
nothing. This defeats not only jamming but also the entire passive side of
electronic warfare: no direction-finding on the operator, no RF signature to
cue a counter-drone system, no spectrum deconfliction between friendly
drones. That last point is underrated — massed RF FPV operations interfere
with each other, and fiber links do not. **CONFIRMED** [7][13]

## 2. Scale and supply chain

| Metric | Value | Date | Label | Source |
|---|---|---|---|---|
| Russian fiber FPV output | >50,000/month (doubled) | Sep 2025 | REPORTED | [3] |
| Russian drone fiber consumption | ~13M km/year | Mar 2026 | REPORTED | [1] |
| Combined RU+UA fiber consumption | 50-60M km | 2025 | REPORTED | [1] |
| Russian share of global fiber output | ~10% | 2026 | REPORTED | [1] |
| Ukrainian fiber FPVs delivered | 352,000 | since Jul 2025 | REPORTED | [4] |
| Ukrainian FPV production (all types) | ~4.5M planned 2026 | 2026 | REPORTED | [3] |
| Ukrainian fiber FPV manufacturers | 35+ | 2026 | REPORTED | brief 17 |
| Fielded spool length | 10-50 km | 2026 | CONFIRMED | [1][2] |
| Fiber outer diameter | 0.26 mm | 2026 | CONFIRMED | [2] |

**The asymmetry that matters.** Russia draws its own fiber at Saransk and
co-produces spools with China. Ukraine imports glass and assembles. In a war
of attrition over a consumable, owning the upstream draw tower is a
structural advantage, and it is the reason Ukrainian production has trailed
despite comparable assembly capacity [3][4]. **REPORTED**

## 3. The AI datacenter collision

This is the part that connects to the rest of this collection and that almost
no defense coverage notices.

G.657.A2 is the preferred fiber for high-density datacenter cabling for
exactly the reason it is preferred for drone spools: it tolerates tight bends
without loss. AI datacenter buildout is therefore bidding directly against
drone spool production for the same product from the same draw towers.

Documented price movement [1]:

- Chinese fiber: ~16 yuan (~$2.33)/km in Jan 2025 → ~40 yuan (~$5.83)/km in Jan 2026
- Western G.657.A2: quoted $33-35/km, Mar 2026
- Delivered 50 km spool: ~$300 → ~$2,500, an eightfold rise
- Corning optical division: +71% Q4 net earnings; $6B fiber supply agreement with Meta

**Analysis.** A 50 km spool of bare fiber at $35/km is $1,750 before
spooling, sheathing, packaging, import, and wartime markup — which is most of
the delivered $2,500. The consumable has become the dominant cost of the
munition. When a one-way attack drone's link costs more than its airframe,
the economic logic that made fiber attractive starts to invert. This is a
genuine, documented case of AI infrastructure demand reshaping a battlefield.
**SPECULATION** on the inversion; the price figures are **REPORTED**.

## 4. Limitations

- **Mass budget.** The spool displaces warhead. Larger spools directly reduce
  munition load [6]. A 50 km spool is a substantial fraction of a small FPV's
  payload.
- **Acoustic signature.** Heavier airframe means higher propeller loading and
  more noise, which matters because acoustic detection is one of the few
  counters that works [6].
- **Terrain.** Woodland and urban environments snag, kink, and cut the fiber.
  A single sharp bend ends the mission. Operators fly deliberate,
  cable-aware paths rather than optimal ones [6][7].
- **One-way.** The cable is expended. It is not recoverable and it litters
  the battlespace with tens of millions of kilometers of glass filament, an
  environmental and eventually agricultural problem [6].
- **Speed and maneuver.** Payout tension constrains aggressive maneuvering
  and terminal dive profiles relative to a free-flying RF drone. **SPECULATION**

## 5. Counter-fiber: why the C-UAS market is being rebuilt

The entire installed base of RF-defeat counter-drone equipment — jammers,
spoofers, RF direction finders — is inert against a fiber drone. There is no
emission. This is why brief 17 concludes that a pure RF-defeat business is
entering a shrinking share of a growing market.

What replaces it:

**Detection.** Radar for the airframe, electro-optical and infrared for
visual identification and tracking through clutter, acoustics for the
propeller signature, all fused with machine-learning classification [7][14].
This is a sensing-and-classification problem, which is to say a
signal-processing problem — see brief 18. It is also the durable half of the
counter-drone business.

**Defeat.** With soft kill unavailable, the options are all physical:
high-power microwave (Epirus Leonidas is cited as defeating fiber drones by
inducing currents in onboard electronics directly), guns, nets, interceptor
drones, and lasers [8][14].

**Institutional signals.** The US Army published an article specifically
framing fiber drones as a significant C-UAS challenge [7]. UK Defence
Innovation opened a market engagement in April 2026 for detecting and
defeating fiber-controlled drones [9]. The US Marine Corps funded a
microwave-based fiber defeat system [8]. Axon Vision's ForceField is marketed
on passive sensing against fiber threats [15]. **CONFIRMED** that the
requirement is live and funded.

## 6. Civilian and industrial applications

The military case dominates coverage, but the physics generalizes to any
environment where radio does not work or is not allowed:

- **Underground and enclosed inspection**: mines, tunnels, sewers, ship
  hulls, ballast tanks. Radio does not propagate; fiber does not care [11].
- **High-EMI industrial**: high-voltage substations, offshore platforms,
  certain chemical plants, where RF is either swamped or prohibited [12].
- **Persistent tethered observation**: a powered tether plus fiber gives
  hours of uninterrupted high-bitrate video with zero spectrum contention —
  event security, border towers, disaster response, incident command [11][12].
- **Spectrum-denied or spectrum-crowded civil settings**: stadiums, airports,
  and any site where transmitting is a licensing problem.

Note the distinction between two different products that share a name: the
expendable payout-spool drone (military, one-way) and the persistent powered
tether (civilian, recoverable, often with power over the tether). They share
the optical link and almost nothing else. **CONFIRMED** [11][12]

## 7. Where this goes

Two forces are squeezing fiber control from opposite directions.

**From above, cost.** AI datacenter fiber demand has raised spool cost ~8x
and shows no sign of reversing before late 2027 given announced supply
agreements [1]. Every dollar added to the link is a dollar not spent on
warhead, seeker, or airframe.

**From below, autonomy.** The purpose of the link is to get a human's
judgment to the terminal phase. Onboard machine vision that performs terminal
guidance removes the need for any link — no radio to jam, no cable to snag,
no spool to buy [16]. Ukrainian and Russian programs are both pursuing this,
and the reporting frames it explicitly as the response to being "stripped of
reliable radio links and priced out of fiber optics" [16].

The hybrid dual-channel drone fielded in March 2026 is the intermediate step:
fiber primary, radio fallback, roughly $60 extra [10]. Expect the same
architecture with autonomy as the third fallback, then autonomy as primary.

**Analytical conclusion (SPECULATION, moderate confidence).** Fiber-optic
control is a real, effective, and currently expanding technology that solves
the jamming problem completely and creates a genuine counter-drone crisis.
It is also transitional. It wins in the window where electronic warfare has
defeated radio control but onboard autonomy is not yet good enough for
terminal guidance. That window opened around 2024 and is closing as vision
models get small enough and cheap enough to run on a disposable airframe. The
durable investment is not in fiber; it is in the sensing and classification
stack that counters *anything* that flies, which is where brief 17's advice
to build sensing and cueing rather than jamming comes from.

## Sources

1. DroneXL, "Ukraine Fiber Optic Spool Prices Jump More Than Eightfold As AI Data Center Demand Squeezes Drone Supply," 11 May 2026 — https://dronexl.co/2026/05/11/ukraine-fiber-optic-spool-price-ai-data-center-demand/
2. UNITED24 Media, "Ukraine Sends 50-Km Fiber-Optic FPVs Into Russian Rear Storage Sites," 2026 — https://united24media.com/war-in-ukraine/ukraine-sends-50-km-fiber-optic-fpvs-into-russian-rear-storage-sites-to-hit-hidden-armor-21500
3. Ukrainska Pravda, "Drone shortages and severed links: why Ukraine still trails on fibre-optic UAV production," 25 Jan 2026 — https://www.pravda.com.ua/eng/articles/2026/01/25/8017810/
4. Atlantic Council, "Fiber-optic drones have emerged as critical kit for both Russia and Ukraine" — https://www.atlanticcouncil.org/blogs/ukrainealert/fiber-optics-drones-have-emerged-as-critical-kit-for-both-russia-and-ukraine/
5. Tom's Hardware, "Russia has reportedly improved the range of its jam-proof optical drones to over 40 miles," 2026 — https://www.tomshardware.com/peripherals/cables-connectors/russia-has-reportedly-improved-the-range-of-its-jam-proof-optical-drones-to-over-40-miles-purported-chinese-russian-collaborative-production-imagery-reveals-dramatically-increased-tethered-drone-range
6. Militarnyi / Ptashka Drones 50 km range report, 2026 — https://militarnyi.com/en/news/ptashka-drones-achieves-50-km-range-with-successful-fiber-optic-drone-use/
7. US Army, "Fiber Optic Drones: Posing a Significant C-UAS Challenge" — https://www.army.mil/article/287737/fiber_optic_drones_posing_a_significant_c_uas_challenge
8. TechTimes, "One Microwave Burst, Dozens of Drones Down: Marines Fund Fiber-Optic Defeat System," 10 Aug 2026 — https://www.techtimes.com/articles/323754/20260810/one-microwave-burst-dozens-drones-down-marines-fund-fiber-optic-defeat-system.htm
9. Defence Blog, "UK launches anti-fibre-optic drone program," Apr 2026 — https://defence-blog.com/uk-launches-anti-fibre-optic-drone-program/
10. DroneXL, "Ukraine's Fiber Optic FPV Drones Now Switch to Radio When the Cable Snaps," 23 Mar 2026 — https://dronexl.co/2026/03/23/ukraine-fiber-optic-fpv-drones-radio-cable/ ; The Defense Post, 23 Mar 2026 — https://thedefensepost.com/2026/03/23/ukraine-fiber-optics-radio-drones/
11. M2 Optics, "What is a Tethered Fiber Optic Drone?" — https://www.m2optics.com/blog/draft-what-is-a-tethered-fiber-optic-drone
12. Omnitron Systems, "Fiber Optic Drones: Advantages, Applications, and Integration" — https://www.omnitron-systems.com/blog/fiber-optic-drones-advantages-applications-and-integration
13. Akran IQ, "Fiber-Optic Drones Explained: Why Militaries Are Ditching RF Control Links" — https://akraniq.com/blog/fiber-optic-drones-explained-military-rf-jamming
14. UAV Defence, "What Detection Technologies Can Stop a Fiber-Optic Drone? Radar, Acoustic and AI Methods Compared" — https://uav-defence.com/what-detection-technologies-can-stop-a-fiber-optic-drone-radar-acoustic-and-ai-methods-compared/
15. Warrior Maven, "New ForceField Counter-Drone System Targets Fiber-Optic Threats" — https://warriormaven.com/news/air/new-forcefield-counter-drone-system-targets-fiber-optic-threats
16. GlobalSecurity, "Ukraine UAV - Autonomous Guidance: The Rise of the Machines" — https://www.globalsecurity.org/military/world/ukraine/uav-autonomy.htm ; Beechat Network, "How modern drones overcome jamming: Fibre Optics, AI Autonomy, and Frequency Hopping," 5 Jan 2026 — https://beechat.network/2026/01/05/how-modern-drones-overcome-jamming-fibre-optics-ai-autonomy-and-frequency-hopping/
