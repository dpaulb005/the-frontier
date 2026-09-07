# Countering Drones That Have No Radio Link (September 2026)

*How to build against fiber-optic-controlled and fully autonomous drones.
Companion to brief 19 (fiber-optic drone comms) and brief 17 (RF frontier).
Claims labeled **CONFIRMED** / **REPORTED** / **SPECULATION**.*

---

## 0. The reframe: there is nothing to jam

Jamming means raising the noise floor in a receiver's passband until the
link's error rate becomes unusable. It presupposes a receiver in the
electromagnetic spectrum. A fiber-controlled drone's receiver is a photodiode
at the end of a waveguide; a fully autonomous drone has no command receiver at
all. Neither presents a channel to attack. Spoofing has the same problem: with
no RF command link and (on inertially guided airframes) no satellite
navigation dependence, there is no signal to imitate.

So the question "how do I jam it" has no answer. The buildable question is:
**how do I detect, track, classify, and physically stop an aircraft that emits
nothing.** That decomposes into a kill chain where four of the five stages are
sensing and computation, and only the last is an effector:

```
DETECT  →  TRACK  →  CLASSIFY  →  DECIDE  →  DEFEAT
   \___________ signal processing ___________/     \_ legally gated _/
```

The commercial and engineering leverage is almost entirely on the left side.
That is also the side a small team can actually build.

---

## 1. The legal gate, first, because it determines what you can sell

This is not a footnote. In the United States, operating a defeat mechanism
against a drone is a federal crime for nearly everyone. Jamming violates the
Communications Act; damaging or destroying an aircraft implicates 18 U.S.C.
§ 32; intercepting the control link implicates the Wiretap Act and the
Computer Fraud and Abuse Act. A drone is legally an aircraft.

Authority to *mitigate* has historically been confined to a small set of
federal agencies under 6 U.S.C. § 124n (DOJ and DHS, with parallel DoD and DOE
authorities), for defined covered facilities and assets. **CONFIRMED** [1][2]

**What changed in 2026, and why it matters commercially.** The Safer Skies Act
provisions in the FY2026 NDAA amended § 124n to extend counter-UAS mitigation
authority to state, local, tribal, and territorial law enforcement and
correctional agencies — contingent on DOJ training and certification, and
requiring FAA notification within five minutes of activating a mitigation
system for real-time deconfliction. DHS issued implementing regulation at
6 CFR Part 124, published in the Federal Register on 6 July 2026.
**CONFIRMED** [1][3][4]

**The implication for a builder.** The buyer set for *defeat* just expanded
from a handful of federal agencies to potentially thousands of law enforcement
and corrections agencies — but each buyer now needs certification, training,
FAA coordination tooling, and an auditable decision record. Meanwhile
*detection* has never required any of this: observing and classifying an
aircraft is lawful. **Analysis:** the certification bottleneck is itself the
opportunity. The compliance and coordination layer around mitigation is
software, sells to the expanded buyer set, and requires no weapon. Lawfare has
written specifically on this bottleneck [5]. **SPECULATION** on the business
conclusion; the statutory facts are confirmed.

Outside the US, rules differ and are generally more permissive for military
users and stricter for civil ones. Anything in this brief that touches
mitigation is a "sell to an authorized operator" business, not a
"deploy it yourself" business.

---

## 2. Detection: the actual engineering problem

With RF direction-finding removed from the toolkit, four modalities remain.
None is sufficient alone. All four are signal-processing problems, which is
the cross-reference to brief 18.

### 2.1 Radar

The workhorse for cueing, and the hardest to do well against this target set.
The physics is unfriendly: small drones are **low, slow, and small** — the
classic LSS problem. Radar cross-section is tiny, velocity is low enough to
fall inside the ground-clutter Doppler notch, and altitude is low enough that
clutter dominates. A building behind the drone reflects far more energy than
the drone does, and at meter-scale range resolution you cannot separate them
geometrically. **CONFIRMED** [6][7]

What works:

- **Micro-Doppler.** Rotating propellers produce a periodic Doppler modulation
  distinct from birds and ground traffic. This is the single most useful
  discriminant in the entire counter-drone problem and it is a pure
  signal-processing result: the blade rate, blade count, and rotor count are
  recoverable from the spectrogram, which gives both classification and, in
  some work, airframe identification. **CONFIRMED** [8][9]
- **Clutter suppression beyond simple SNR thresholding.** A Doppler
  signal-to-clutter ratio detector outperforms conventional SNR detection on
  small drones by using both amplitude and Doppler information; sparse
  methods such as orthogonal matching pursuit with learned environmental
  clutter dictionaries suppress site-specific clutter. **CONFIRMED** [6][10]

**Builder note.** Commodity automotive radar chipsets and software-defined
radar on RFSoC-class hardware put a micro-Doppler research platform within a
small team's reach. The differentiator is not the front end; it is the clutter
model and the classifier. See brief 17 §4 for hardware and costs.

### 2.2 Acoustics

The modality that suits this threat best, and the one that got real product
attention in 2026 precisely because of fiber drones.

Acoustic sensing is **passive** — the sensor emits nothing, so it does not
reveal the defended site, which matters when the attacker is also hunting
emitters. It works on anything with a propeller regardless of control link.
Netline launched SonicScan in June 2026 marketed explicitly on detecting
drones controlled by fiber-optic links or flying autonomously; Hall Lidar
launched the UDL-64 in April 2026 for 3D acoustic tracking of exactly the
targets that defeat radar, RF and optical. **REPORTED** [11][12]

Physics constraints, stated honestly: range is short (hundreds of metres
typically, degrading fast with wind and background noise), and fiber drones
are *louder* than equivalent RF drones because the spool adds mass and
propeller loading — a rare case where the threat's countermeasure helps you.
**CONFIRMED** on the mass/noise link (brief 19 §4).

**The methodological trap that will waste six months of your time.** Published
acoustic drone-detection accuracies are widely inflated by **session-level
data leakage**: when training and test splits are drawn from the same
recording session, the model learns the session's microphone response, ambient
noise floor and wind conditions rather than the drone. Held-out-session
evaluation drops accuracy substantially. The EchoHawk paper (June 2026) is
built around this warning and provides a reproducible pipeline with correct
splits. **CONFIRMED** [13]

**Analysis:** this is the single most actionable technical detail in this
brief. If you build an acoustic classifier, your train/test split must be by
session, site, and hardware unit — never by random shuffle of clips. Any
vendor quoting accuracy without stating its split protocol should be assumed
to be quoting a leaked number.

### 2.3 Electro-optical and infrared

Confirmation and identification, rarely primary detection. Once radar or
acoustics cues a bearing, a slewable EO/IR head classifies the object, and
this is where the "is it a bird, a bag, or a munition" decision is actually
made. Modern small-object detectors handle the recognition; the hard parts
are the gimbal control loop, keeping a small fast object in a narrow field of
view, and thermal performance at night and through weather. Passive, so it
does not reveal the site.

### 2.4 Passive RF (still useful, in an inverted role)

Counter-intuitively, RF sensing does not become worthless — it becomes a
*negative* discriminant. An airborne track with a propeller micro-Doppler
signature and **no** associated RF emission is, by elimination, either fiber
controlled or autonomous, and therefore more likely hostile than a hobbyist.
Absence of emission is information. **SPECULATION**, but it follows directly
from the sensor physics.

### 2.5 Fusion is the product

No single modality gives an actionable track. The product is the fusion layer:
associate radar plumes, acoustic bearings and EO/IR detections into one track,
maintain identity through clutter and occlusion, and output a classification
with a calibrated confidence and a decision record. Published guidance and
vendor architecture both converge on radar + EO/IR + acoustics + AI
classification as the answer to fiber drones. **CONFIRMED** [11][14][15]

This is a Kalman/multi-hypothesis tracking problem wrapped around several
learned classifiers — squarely classical estimation plus modern ML, which is
brief 18's thesis in operational form.

---

## 3. Defeat: categories, tradeoffs, and why you probably should not build one

For completeness, the effector options against a non-emitting drone are all
physical. These are published system categories, not build guidance.

| Category | Mechanism | Strengths | Limits |
|---|---|---|---|
| High-power microwave | Induces currents in onboard electronics, forcing reset or component failure | Wide beam, multiple targets per shot, works regardless of control link | Large power and cooling, fratricide against friendly electronics, short range, expensive |
| Laser | Thermal damage to airframe or optics | Precise, deep magazine | Line of sight, weather, dwell time per target, high cost |
| Kinetic interceptor drone | Airframe-to-airframe collision | Cheap per shot, magazine scales, proven at volume | Requires very good terminal guidance, one target per round |
| Guns and programmable-fuze ammunition | Fragmentation | Mature, fast | Collateral risk, short range |
| Nets and entanglement | Rotor fouling, capture | Non-destructive, evidence preserved | Very short range, single target |

High-power microwave is the category most specifically associated with fiber
drones, because it attacks the airframe's electronics rather than its link —
Epirus's Leonidas is repeatedly cited on this basis, and the US Marine Corps
funded a microwave-based fiber-optic defeat effort reported in August 2026.
The UK opened a market engagement in April 2026 for anti-fiber technologies.
**REPORTED** [16][17][18]

**Why a small team should not start here.** Every option above is capital
intensive, export controlled, legally gated to the buyer set in §1, and sold
through defense procurement cycles measured in years. The sensing side has
none of those properties and is a prerequisite for all of them: an effector
without a track is useless, and whoever owns the track owns the system
architecture. **SPECULATION**, moderate-to-high confidence.

---

## 4. What to actually build

Ranked by ratio of achievable-in-12-months to defensible-once-built.

1. **A held-out-session-honest acoustic detection and direction-finding
   stack.** Multi-microphone array, micro-Doppler-analogous spectral features,
   bearing estimation, classifier with correct split protocol. The field is
   full of inflated numbers; being the one vendor whose accuracy survives a
   new site is a real moat. Hardware cost is in the hundreds of dollars per
   node — Ukrainian networks reportedly field 14,000+ sensors at under $500
   each. **REPORTED** [11]
2. **The fusion and track-management layer**, sensor-agnostic, ingesting
   third-party radar and EO/IR. This is where the defensibility is, because
   it accumulates site-specific tuning data and becomes the integration point.
3. **Micro-Doppler classification as a library.** Blade-rate extraction and
   airframe typing from radar spectrograms, sold to radar OEMs who have good
   front ends and mediocre classifiers.
4. **The compliance and coordination layer for the newly authorized buyers**:
   certification workflow, FAA five-minute notification, rules-of-engagement
   decision trees, auditable engagement records. No weapon, no export control,
   and the buyer set just expanded by orders of magnitude.
5. **An open, correctly-split acoustic and radar dataset for non-emitting
   drones.** Same logic as the RF corpus argument in brief 17 §5: the field
   has no shared benchmark, and whoever publishes the credible one is cited by
   everyone who follows.

**What not to build:** RF jammers (inert against this threat and a shrinking
share of a growing market, per brief 17), and anything requiring you to hold
mitigation authority you do not have.

---

## Sources

1. 6 U.S.C. § 124n — https://uscode.house.gov/view.xhtml?req=%28title%3A6+section%3A124n+edition%3Aprelim%29
2. DHS, "Counter-Unmanned Aircraft Systems (C-UAS)" — https://www.dhs.gov/science-and-technology/counter-unmanned-aircraft-systems-c-uas
3. Federal Register, "Counter-UAS Authority for State, Local, Tribal, and Territorial Law Enforcement and Correctional Agencies," 6 Jul 2026 — https://www.federalregister.gov/documents/2026/07/06/2026-13609/counter-uas-authority-for-state-local-tribal-and-territorial-law-enforcement-and-correctional
4. eCFR, 6 CFR Part 124 — https://www.ecfr.gov/current/title-6/chapter-I/part-124
5. Lawfare, "The Counter-UAS Certification Bottleneck" — https://www.lawfaremedia.org/article/the-counter-uas-certification-bottleneck
6. "Improved Radar Detection of Small Drones Using Doppler Signal-to-Clutter Ratio (DSCR) Detector" — https://www.researchgate.net/publication/370700807_Improved_Radar_Detection_of_Small_Drones_Using_Doppler_Signal-to-Clutter_Ratio_DSCR_Detector
7. "Radar Challenges and Solutions for Drone Detection" — https://www.researchgate.net/publication/393207946_Radar_Challenges_and_Solutions_for_Drone_Detection
8. "Micro-Doppler-Coded Drone Identification," arXiv:2402.04368 — https://arxiv.org/pdf/2402.04368
9. "Micro-Doppler Signature Detection and Recognition of UAVs Based on OMP Algorithm" — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10535593/
10. "Introduction to Drone Detection Radar with Emphasis on Automatic Target Recognition," arXiv:2307.10326 — https://arxiv.org/pdf/2307.10326
11. UASweekly, "Netline Launches SonicScan Acoustic Drone Detection System," 16 Jun 2026 — https://uasweekly.com/2026/06/16/30612/
12. Unmanned Systems Technology, "Hall Lidar Unveils Acoustic Sensing Drone Detection & Stealth Monitoring Technology," Apr 2026 — https://www.unmannedsystemstechnology.com/2026/04/hall-lidar-unveils-acoustic-sensing-drone-detection-stealth-monitoring-technology/
13. "EchoHawk: A Reproducible Acoustic Pipeline for Drone Detection, Classification, and Direction-Finding, with a Cautionary Study of Session-Level Data Leakage," arXiv:2606.29589, Jun 2026 — https://arxiv.org/pdf/2606.29589
14. US Army, "Fiber Optic Drones: Posing a Significant C-UAS Challenge" — https://www.army.mil/article/287737/fiber_optic_drones_posing_a_significant_c_uas_challenge
15. UAV Defence, "What Detection Technologies Can Stop a Fiber-Optic Drone?" — https://uav-defence.com/what-detection-technologies-can-stop-a-fiber-optic-drone-radar-acoustic-and-ai-methods-compared/
16. TechTimes, "Marines Fund Fiber-Optic Defeat System," 10 Aug 2026 — https://www.techtimes.com/articles/323754/20260810/one-microwave-burst-dozens-drones-down-marines-fund-fiber-optic-defeat-system.htm
17. Defence Blog, "UK launches anti-fibre-optic drone program," Apr 2026 — https://defence-blog.com/uk-launches-anti-fibre-optic-drone-program/
18. Warrior Maven, "New ForceField Counter-Drone System Targets Fiber-Optic Threats" — https://warriormaven.com/news/air/new-forcefield-counter-drone-system-targets-fiber-optic-threats
