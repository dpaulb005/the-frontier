# Robotics and Embodied AI, September 2026: Where AI Meets Electronics

*Research brief compiled 2026-09-07. Every claim is tagged CONFIRMED (primary source or multiple credible outlets), REPORTED (single outlet, secondary, or company claim not independently verified), or SPECULATION (forecast, rumor, or analyst extrapolation). Inline [n] citations map to the Sources list.*

---

## TL;DR

- **Foundation models for robots have gone from research demos to a product category in 18 months.** Google DeepMind (Gemini Robotics 1.5 → On-Device 2 → Gemini Robotics 2 and ER 2 in July 2026), Physical Intelligence (π0.6 → π*0.6 with RL-from-experience → π0.7 in April 2026), NVIDIA (GR00T N1.6, open weights), Figure (Helix 02, a three-tier 1 kHz / 200 Hz / semantic stack), Skild and Generalist have converged on the same recipe: a vision-language backbone plus an action expert, trained on heterogeneous cross-embodiment data, increasingly fine-tuned with autonomous experience. [1][2][3][4][5][6][7][8]
- **Money is enormous and front-loaded.** Skild AI $14B (Jan 2026), Figure $39B (Sept 2025, no new priced round), Apptronik ~$5.3B (Feb 2026), Generalist $3B (Aug 2026), Physical Intelligence reportedly raising ~$1B again; Anduril $61B (May 2026, talks at $100B), Shield AI $12.7B (Mar 2026). Unitree's Shanghai STAR IPO on 19 Aug 2026 closed its first day up 460% at a market cap near US$50B. [9][10][11][8][12][13][14][15]
- **Humanoid shipments are real but Chinese, cheap, and mostly not yet doing production work.** 19,100 humanoids shipped globally in 1H 2026 (+272% YoY), 97% from Chinese vendors, AgiBot (44%) and Unitree (31%) dominating. Full-year 2026 is projected at ~60,000 units and only ~$1.6B revenue: an average selling price in the mid-$20K range, which tells you most of these are G1-class research/education/entertainment machines, not factory workers. [16][15]
- **Western humanoids are in single-digit-to-tens-of-units factory pilots.** Figure 03 entered BMW Spartanburg's logistics hall on 30 June 2026 for parts sequencing; Agility has Digit at Toyota Canada (7 units), Mercado Libre, GXO, and Amazon and is going public via a $2.5B SPAC; Apptronik Apollo pilots at Mercedes, GXO, Jabil; Boston Dynamics' electric Atlas is in production with 2026 units "fully committed" to Hyundai's RMAC and Google DeepMind. Hyundai's plan is 25,000+ Atlas units, but starting in 2028 at $130–140K per unit. [17][18][19][20][21][22]
- **Tesla Optimus has missed every public target.** Zero robots doing "useful work" as of January 2026 by Musk's own admission, V3 reveal slipped repeatedly, Fremont production starting "late July or August" with output "literally impossible to predict." No 2026 unit target exists. [23]
- **Autonomous vehicles are the one embodied-AI segment at true commercial scale.** Waymo: 14 US cities, >500,000 paid rides/week, ~4,000 vehicles, 200M+ autonomous miles, 4M+ miles/week, chasing 1M rides/week by year end, Munich announced. Baidu Apollo Go passed 100M cumulative rides in 1H 2026 with vehicles at ~RMB 200K. Tesla crossed 1M unsupervised miles across six Texas/Florida cities plus 45 registered Cybercabs in Austin, and immediately drew an NHTSA probe over self-certification of a car with no pedals. Zoox began charging in Las Vegas in August 2026. [24][25][26][27][28][29]
- **Defense autonomy is the highest-revenue, fastest-compounding corner.** Anduril did ~$2.1B revenue in 2025 and won a US Army contract worth up to $20B; Shield AI's Hivemind was selected for the Air Force CCA program; Ukraine builds "well over three million" drones a year, projected seven million in 2026. The battlefield lesson is not "full autonomy": it is terminal-guidance autonomy that lifts hit rates from 10–20% to 70–80% while keeping humans in the loop. [13][14][30][31]
- **The bottleneck has shifted from "can the model do it once" to "can the hardware do it 10,000 times."** Actuator fatigue (harmonic-drive flexsplines), dexterous hands, tactile sensing, and battery runtime (Figure 03: 5 h on 2.3 kWh) are the binding constraints. Musk's own phrase: "it will move as fast as the least lucky, slowest, dumbest part in the entire 10,000." [23][32][33]
- **Realistic timeline:** narrow, structured-environment humanoid work (tote moving, sequencing, machine tending) at hundreds-to-low-thousands of Western units by end-2027; tens of thousands of Chinese units mostly in research, education, retail and entertainment; home robots in 2026–27 are teleop-assisted learning platforms, not autonomous appliances. General-purpose household autonomy without remote humans in the loop is a 2029+ question. (Analysis.)

---

## 1. Vision-Language-Action foundation models: the state of the stack

### Google DeepMind Gemini Robotics
**CONFIRMED.** Gemini Robotics 1.5 (25 Sept 2025) introduced a two-model agentic system: Gemini Robotics-ER 1.5 as a "high-level brain" for planning and tool use (including Google Search), and Gemini Robotics 1.5 as the VLA that executes. Its headline contribution was motion transfer across embodiments: skills trained on ALOHA 2 transferred to Apptronik's Apollo humanoid and Franka bi-arm systems without specialization. ER 1.5 shipped via the Gemini API; the VLA stayed with trusted testers. [1]

**CONFIRMED.** Gemini Robotics On-Device 2 (model card dated 30 July 2026) is built on Gemini Robotics 1.5 technology plus Gemma on-device models, trained on TPUs, and is evaluated "primarily on standing bi-arm manipulation." Reported generalization on novel platforms: 53.3% success on SO101 (vs 6.7% for v1) and 75.6% on Dexmate (vs 33.3%). DeepMind explicitly scopes out mobile platforms and whole-body control. The original On-Device model (June 2025) was the first VLA offered for fine-tuning, adapting with 50–100 demonstrations. [2][34]

**CONFIRMED (existence), REPORTED (details).** In July 2026 DeepMind announced Gemini Robotics 2 ("whole body intelligence to robots") and Gemini Robotics ER 2 ("video understanding, task orchestration, and multi-robot collaboration"). The model page lists Agile Robots, Apptronik and Boston Dynamics as research partners, and says Robotics 2 is "available for testing," ER 2 is in AI Studio, and On-Device 2 is "available for deployment." Boston Dynamics separately committed to integrating Gemini Robotics models into Atlas. [35][36][21]

### Physical Intelligence (π)
**CONFIRMED.** π0.6 (model card 17 Nov 2025) is a 5B-parameter VLM plus action expert, trained with "Knowledge Insulation" (the backbone predicts FAST action tokens while the action expert predicts continuous actions, with no gradient flowing back). With 5 denoising steps and 3 cameras it produces an action chunk in 63 ms on one H100. It folds laundry "out of the box" and fully assembles a box 20% of the time. [3]

**CONFIRMED.** π*0.6 with RECAP (RL with Experience & Corrections via Advantage-conditioned Policies, 17 Nov 2025) adds a three-stage loop of demonstrations, expert corrections, and autonomous RL. Claimed result: "more than doubles the throughput on some of the hardest tasks, and can decrease failure rates by 2x or more." Demonstrations: espresso service from 5:30 am to 11:30 pm, folding 50 novel laundry items in a new home, assembling 59 chocolate boxes in a factory. [4]

**CONFIRMED.** π0.7 (16 Apr 2026) is pitched as "a steerable model with emergent capabilities": compositional generalization, operating unfamiliar kitchen appliances, and folding laundry on a bimanual UR5e that had no laundry data for that embodiment. It ingests demonstrations from multiple morphologies, human video, and autonomous RL episodes, using contextual annotations so suboptimal data can be included. Parameter count not disclosed. [5]

**REPORTED.** TechCrunch reported in March 2026 that PI was in talks to raise roughly $1B again; a July 2026 Anthropic–PI rumor circulated without confirmation. Treat any valuation you see as unverified. [37]

### NVIDIA GR00T
**CONFIRMED.** GR00T N1.6 (15 Dec 2025; showcased at CES 2026) is a 3B open model on Hugging Face. Architecture: an internal Cosmos-2B VLM variant with flexible-resolution encoding, a diffusion transformer twice as deep as N1.5 (32 vs 16 layers), and the top four VLM layers unfrozen during pretraining. Training data: "several thousand hours of teleoperated data" across bimanual YAM arms, AgiBot Genie-1, Unitree G1 loco-manipulation, and simulated Galaxea R1 Pro, 300K steps at batch size 16,384. NVIDIA claims it beats N1.5 in sim and on real YAM, Genie-1 and G1 robots. [6] NVIDIA has since pushed models into Hugging Face's LeRobot (July 2026), JetPack 7.2 for Jetson, and "agent skills" for physical-AI research (June 2026). [38]

### Figure Helix 02
**CONFIRMED (company claims).** Helix 02 (27 Jan 2026) is a three-tier stack: System 0 is a 10M-parameter network at 1 kHz for balance, contact and coordination (replacing, per Figure, 100,000+ lines of hand-coded C++); System 1 is a transformer at 200 Hz over head cameras, palm cameras, tactile sensors and proprioception driving all joints; System 2 is the semantic/language layer. Trained on 1,000+ hours of joint-level retargeted human motion data and 200,000+ parallel simulation environments. Demo: a four-minute continuous dishwasher unload-navigate-load-start sequence, plus pill extraction and syringe dosing. Figure followed with living-room (Mar 2026) and bedroom (May 2026) tidying demos, and on 25 Aug 2026 announced "Index," described as "the world's largest and most diverse physical dataset." On 3 Sept 2026 Figure signed with Nscale for up to 100,000 GPUs on NVIDIA's Vera Rubin platform. [7][39][40]

### Skild AI and Generalist
**CONFIRMED.** Skild AI raised a $1.4B Series C at >$14B (14 Jan 2026), led by SoftBank with NVIDIA, Macquarie and 1789 Capital, more than tripling its $4.5B valuation from summer 2025; >$2B raised total. Product: the "Skild Brain," a retrofit foundation model for many robot types and tasks. Strategic investors include LG, Schneider Electric and Salesforce Ventures. [9]

**CONFIRMED.** Generalist (founded 2024 by ex-DeepMind researchers Pete Florence and Andy Zeng and ex-Boston Dynamics engineer Andrew Barry) raised $600M in 2026 ($400M led by Radical Ventures in June, $200M extension led by 8VC), reaching $3B in August. Its Gen 1.5 model reportedly learns new tasks from 3–12 second video demonstrations. [8]

### Tesla FSD / Optimus stack
**CONFIRMED.** FSD v14.3.9 is rolling out with "collision evasion" features; a v15 architecture targeting 24-hour robotaxi operation is expected around October 2026. Tesla's balance sheet shows "AI infrastructure" at $10.8B gross as of 30 June 2026, up from $6.8B at year-end 2025. Tesla's public claim that Optimus shares the FSD vision stack is not independently verifiable; The Register quoted reporting that Optimus "doesn't have any autonomous capabilities at all" as of January 2026, which contrasts with Figure and Atlas demos. [28][41][22]

### Analysis: what has actually changed in the models
Three things are new since 2024. First, cross-embodiment transfer works well enough that every vendor now claims it (DeepMind on Apollo/ALOHA/Franka, π0.7 on UR5e, GR00T across four robot families). Second, RL from autonomous experience (π*0.6 RECAP) is producing the first credible throughput and reliability gains rather than just task-diversity gains. Third, the "three-speed brain" architecture (a fast whole-body controller, a mid-rate visuomotor policy, a slow reasoning model) has become the de facto standard from Figure to DeepMind's ER/VLA split. What has not changed: every flagship demo still has a 20–80% success band on hard tasks, and nobody publishes MTBF or hours-between-interventions in deployment.

---

## 2. Humanoids: production claims versus deployed reality

### Tesla Optimus
**CONFIRMED.** Musk's January 2025 target of "roughly 10,000" Optimus units in 2025 was missed entirely; in January 2026 he acknowledged zero robots doing useful work in Tesla factories. The V3 reveal slipped from Q1 2026 to "probably middle of this year." Fremont's Model S/X line ended in early May 2026 after 610,000+ combined units and was converted to Optimus; production was to begin "late July or August" with output "quite slow." Musk declined a 2026 volume target, calling the rate "literally impossible to predict" across 10,000 unique parts. A second Optimus line at Giga Texas is reported for ~summer 2027. Tesla's Q2 2026 production report and 10-Q carry no Optimus line item. [23][41]
**SPECULATION.** Press and fan sites cite a $20–30K target price and long-run 10M-unit ambitions; none of this is in an SEC filing. [42]

### Figure
**CONFIRMED.** Figure 02 contributed to 30,000 BMW vehicles in 2025; Figure 03 (launched Oct 2025) arrived at BMW Spartanburg Hall 52 on 30 June 2026 for the "sequencing" use case, running Helix 02 and performing loco-manipulation (pulling carts while placing parts). Figure's own post describes a single robot in the new use case. [17]
**REPORTED.** Secondary sources cite a 40-unit Figure 03 fleet at Spartanburg, 350+ units built, BotQ going from 1 unit/day to 1 unit/hour in four months, 12,000 units/year current capacity with a 100,000 target, a Catalyst Brands logistics deployment in Reno, and a Brookfield "Project Go-Big" home-data program spanning 100,000 residential units. Figure 03 specs: 61 kg, 20 kg payload, 1.2 m/s, 2.3 kWh battery, ~5 h runtime, inductive charging, seventh-gen hands with 20+ DoF and fingertip tactile sensing to ~3 g. Figure's $39B Series C (Sept 2025) remains the last priced round; secondary marketplaces in mid-2026 quoted shares below that mark. [40][43][44]

### Boston Dynamics Atlas and Hyundai
**CONFIRMED.** Electric Atlas entered production in early 2026, with all 2026 units committed to Hyundai's Robotics Metaplant Application Center and Google DeepMind; 56 DoF, dual hot-swap batteries, IP67, -20 to 40 °C. Hyundai plans 25,000+ Atlas units across its plants starting at Metaplant America (Georgia) in 2028 and Kia Georgia in 2029, a 30,000-unit/year robot factory, and a Hyundai Mobis US actuator plant at 350,000 units/year from 2028. Early unit cost is estimated at $130–140K, falling to ~$30K past 50,000 cumulative units. [21][22][20]
**REPORTED.** Korean union resistance to deployment without a labor agreement. [45]

### Agility Robotics
**CONFIRMED.** Digit is at Toyota Motor Manufacturing Canada (seven robots, Feb 2026), Mercado Libre (San Antonio), GXO and Amazon, reportedly nine customer facilities. Agility announced a $2.5B SPAC merger with Churchill Capital Corp XI on 24 June 2026, filed a confidential S-4 on 14 July, opened a Fremont facility in July, and CEO Peggy Johnson has said consumer humanoids remain far off. [18][46]

### Apptronik
**CONFIRMED.** $520M Series A extension (11 Feb 2026) bringing the Series A to $935M+ and total capital to ~$1B, led by B Capital, Google, Mercedes-Benz and PEAK6 with AT&T Ventures, John Deere and QIA; TechCrunch put post-money at ~$5.3B. Pilots at Mercedes-Benz Berlin, GXO and Jabil (which also manufactures Apollo); Apollo 2 is live; Apptronik is a Gemini Robotics partner. [19][36]

### 1X NEO
**CONFIRMED.** NEO: $20,000 or $499/month, 30 kg, 22 DoF hands, tendon drive, Jetson Thor, 22 dB. First US deliveries promised by end of 2026, international from 2027; 1X says the first 10,000-unit batch sold out in five days and targets 100,000 units/year by end-2027 with a second plant in San Carlos. The catch: NEO relies on scheduled remote "1X Expert" teleoperation for tasks it cannot do, raising in-home camera privacy questions; early units are doing simple logistics in 1X's own factory to generate training data. 1X's own guidance was 60–70% autonomous operation in 2026 rising to 95%+ by 2028. [47][48][49]

### China: Unitree, AgiBot, UBTech, Galbot
**CONFIRMED.** Unitree listed on Shanghai's STAR Market on 19 Aug 2026: 40.45M shares at RMB 150.80 raised ~RMB 6.1B (~US$904M); the stock closed its first day at RMB 845, up 460%, for a market cap of ~RMB 342B (~US$50B) after touching RMB 445B intraday. 2025: revenue RMB 1.70B (tripled YoY), adjusted profit RMB 591M, 5,511 humanoids shipped, humanoids 51.8% of revenue, ~44% overseas. Q1 2026 net profit fell 52.6% YoY. Store prices: R1 $4,900, G1 $13,500, H2 $29,900, H2 Plus $100,000. [15][50]
**CONFIRMED (analyst data).** Smart Analytics Global: 1H 2026 global humanoid shipments 19,100 (+272%), AgiBot 8,400 (44%, +562%), Unitree 5,900 (31%), Galbot ~900, UBTech ~700, Leju ~600; Chinese vendors 97% of supply, China 85% of demand; industrial/commercial share rose to >70% from ~50%; full-year 2026 forecast ~60,000 units and ~$1.6B revenue. Omdia put 2025 shipments at ~15,000. [16][15]
**REPORTED.** AgiBot cumulative production 15,000 by June 2026; UBTech Walker S2 orders >RMB 800M from BYD, Geely, FAW-VW, Audi FAW, BAIC, Foxconn and SF Express, and 13,361 U1 preorders by end-June; Galbot raised RMB 2.5B in March 2026 at >RMB 20B post-money and holds a RMB 236M CATL procurement order. TrendForce sizes China's 2026 humanoid market at RMB 15B, growing "at least 60%" in 2027. [50][51]
**ANALYSIS.** Forbes' August 2026 argument that China's shipment lead "doesn't matter yet" is directionally right: at ~$27K implied ASP, most units are G1-class platforms bought by universities, integrators, rental/entertainment operators and showrooms. That said, the SAG data showing industrial/commercial share above 70% and UBTech's automotive order book mean the "toys" framing is aging fast. [52][16]

---

## 3. Autonomous vehicles: the segment that actually scaled

### Waymo
**CONFIRMED.** 14 US cities as of 1 Sept 2026 (Phoenix, SF, LA, Austin, Atlanta, Miami, Dallas, Houston, San Antonio, Orlando, Nashville, plus Denver, San Diego and Tampa); >500,000 paid rides/week; ~4,000 vehicles (a June 2026 recall covered "nearly 4,000"); 200M+ fully autonomous miles and 4M+ miles/week; stated goal of 1M weekly rides by end-2026; Munich announced 25 Aug 2026 with London and Tokyo in development; sixth-gen driver on the Zeekr "Ojai" and Hyundai Ioniq 5; freeway service resumed July 2026. Ridership went from 50,000/week (May 2024) to 500,000/week (March 2026). [24][25][53][54]
**CONFIRMED.** Friction is rising with scale: an NHTSA investigation after a child-collision incident (Aug 2026), a school-bus probe, a San Francisco service pause after a power outage, the SF mayor pushing for stricter rules, the Uber partnership ending in Phoenix, and reports of test-driver injuries. [53]

### Tesla Robotaxi and Cybercab
**CONFIRMED.** Unsupervised (no in-car monitor) service in Austin, Dallas, Houston (from 18 Apr 2026), Miami, Orlando and Tampa (July 2026); SF Bay Area still carries a safety monitor under California rules. Unsupervised miles: 380,000 at late July, 1,000,000 by 3 Sept 2026. Roughly 200 vehicles operate without oversight per press reports. Cybercab (no wheel, no pedals) launched public rides in Austin on 3–6 Sept 2026 with 45 units registered in Texas; NHTSA opened a probe within hours over Tesla's self-certification to FMVSS rather than seeking an exemption, since "existing standards remain in force." Tesla is polling customers about buying and operating Cybercab fleets. [28][27][29]
**ANALYSIS.** One million unsupervised miles is roughly what Waymo now drives in about two days. Tesla's pace of city additions is impressive; its scale is not yet.

### Zoox, Baidu, Pony, WeRide
**CONFIRMED.** Zoox received final federal approval for its purpose-built vehicle (30 July 2026), began charging in Las Vegas (5 Aug), added airport service (3 Sept), and operates in SF, Austin and Miami with Dallas, Phoenix and DC being mapped; it issued a software recall after a smoke-confusion incident. [55]
**CONFIRMED.** Baidu Apollo Go passed 100M cumulative rides in 1H 2026, launched full commercial service in Dubai on 1 Apr 2026, holds a Hong Kong pilot license, and has a Lyft partnership for Germany/UK in 2026; sixth-gen vehicles cost ~RMB 200K and one remote operator now covers >10 vehicles. [26][56]
**REPORTED.** Pony.ai targets 20+ cities by end-2026 and ~1,000 Middle East robotaxis by 2028; WeRide targets ~1,000 Middle East robotaxis by end-2027. Both are mostly China plus Gulf deployments. [57]

---

## 4. Drones and defense autonomy

**CONFIRMED.** Anduril raised $5B at $61B (13 May 2026), doubling from $30.5B in mid-2025, on ~$2.1B 2025 revenue; it won a US Army contract worth up to $20B (Mar 2026), acquired ExoAnalytic (space surveillance), and in July 2026 was reported in talks at $100B. Shield AI raised $1.5B Series G at $12.7B (Mar 2026, Advent and JPMorgan), up 140% from $5.3B, with a further $500M from Blackstone; its Hivemind autonomy stack was selected for the Air Force Collaborative Combat Aircraft program alongside Anduril's Fury, and it is acquiring Aechelon. Shield projects >80% revenue growth in 2026. [13][14][58]

**CONFIRMED.** Ukraine produces "well over three million" unmanned systems a year across air, ground and sea, with seven million projected for 2026. Late-2025 interceptor programs use optical navigation and visual target lock with edge processing and no radio link, defeating EW. [31]
**REPORTED.** Autonomous terminal guidance raises FPV engagement success from ~10–20% to ~70–80%. Breaking Defense's August 2026 corrective: the "wrong lessons" are that the best single drone wins, that full autonomy is the goal (operators prefer being in the loop because fully autonomous systems confuse friendly and enemy drones), that manufacturing volume is the bottleneck, that drones replace soldiers, and that buying hardware solves the problem. The right lesson is an operator-engineer-manufacturer feedback loop that fields changes "in weeks rather than years." [30]
**ANALYSIS.** The Ukraine data flywheel is the most mature embodied-AI flywheel on Earth: millions of units, real outcome labels, week-scale iteration. It is also the clearest proof that partial autonomy with human target selection, not end-to-end autonomy, is what wins on cost and reliability today.

---

## 5. Warehouse and logistics

**CONFIRMED.** Amazon crossed 1M deployed robots (July 2025, millionth unit in Japan) and released DeepFleet, a generative model that improves fleet travel efficiency ~10%; 75% of global deliveries are robot-assisted; next-gen sites (Shreveport first) carry 10x the robots. Vulcan (May 2025) is Amazon's first robot with force-feedback touch, stowing and picking ~75% of item types, with 2026 rollouts to more US and German sites. A next-gen Proteus with plain-language voice commands was shown in London on 4 June 2026. Amazon says 700,000+ employees have been upskilled. [59][60][61]
**REPORTED.** Analysts expect the fleet to approach 1.5M, roughly Amazon's headcount; Agility's Digit continues limited work in Amazon facilities. [62][18]
**ANALYSIS.** The warehouse is where "robots" already outnumber the hype: mobile bases plus arms with touch, running on a closed data loop across hundreds of identical sites, at unit economics nobody in humanoids can match yet.

---

## 6. Simulation, world models, and the real-world data flywheel

**CONFIRMED.** Genie 3 (5 Aug 2025): real-time interactive worlds at 720p/24 fps, consistency for "several minutes," promptable world events, tested with the SIMA agent; DeepMind lists limits including short interaction horizons and weak multi-agent modeling; a June 2026 update is featured on DeepMind's site. NVIDIA Cosmos (Predict 7B/14B, Transfer, Reason) is Apache-2.0 and self-hostable, with Cosmos 3 ("omnimodal world models for physical AI," two-tower MoT) published June 2026; world models need roughly 8–32x the GPU compute of a similarly sized LLM (Cosmos-Predict 7B at 720p needs ~70–80 GB VRAM, ~0.4 fps on H100). GR00T N1.6 is trained on synthetic data from the Isaac GR00T Blueprint, and Helix 02 used 200,000+ parallel sim environments. [63][64][6][7]
**REPORTED.** DeepMind has shown Genie-3-style world-model training from ~62 hours of robot data achieving zero-shot transfer to new labs with 16x faster latent-space inference than pixel baselines. [65]

**Data flywheel, by strategy (CONFIRMED unless noted):**
- Teleoperation at scale: GR00T N1.6's "several thousand hours"; Figure's Index dataset and Brookfield home-data program (reported 100,000 residential units); 1X's paid teleop "Expert" sessions double as data collection. [6][39][40][48]
- Human video and motion capture: Helix 02's 1,000+ hours of retargeted human motion; π0.7 and Skild both train on human video. [7][5][9]
- Autonomous RL in deployment: π*0.6 RECAP's espresso, laundry and box-assembly runs. [4]
- Compute: Figure's 100,000-GPU Nscale deal; Tesla's $10.8B AI infrastructure line. [39][41]

---

## 7. Hardware bottlenecks: actuators, hands, touch, batteries

**CONFIRMED / REPORTED.** Industry analyses (PatSnap, IDTechEx, Bank of America) converge on the same list: actuator reliability under sustained duty cycles is the primary bottleneck, because harmonic-drive flexsplines fatigue under exactly the cyclic loads walking and lifting impose; high-precision planetary roller screws are in short supply; dexterous hands and tactile perception remain below human level even as motors exceed human muscle in power density. Hyundai Mobis' 350,000-actuator plant and Figure's in-house seventh-gen hands (20+ DoF, ~3 g tactile threshold) show where vertical integration is happening. Batteries: Figure 03 gets ~5 h from 2.3 kWh; Atlas and Unitree rely on hot-swap packs. Rodney Brooks' critique that vision-heavy training cannot substitute for feeling contact remains unanswered in public deployment data. [32][33][20][43][21]
**ANALYSIS.** Cost curves are the tell: Hyundai's $130–140K early Atlas cost versus Unitree's $13,500 G1 is not a 10x difference in ambition, it is a difference in actuator torque density, hand complexity and expected duty cycle. The cheap humanoids are cheap because they are not built to run three shifts.

---

## 8. Realistic timelines (ANALYSIS)

| Milestone | Realistic window | Basis |
|---|---|---|
| Western humanoids doing paid, narrow factory/logistics tasks at 100s of units | 2026–2027 | BMW, Toyota, Mercedes, GXO pilots; BotQ and Atlas production. [17][18][19][21] |
| 10,000+ Western humanoids in production work | 2028–2029 | Hyundai's 2028 start; Figure's 12K/yr capacity is not the same as demand. [20][40] |
| Chinese humanoid shipments >100K/yr | 2027–2028 | 60K forecast for 2026 at +270% growth; ASP falling. [16] |
| Home humanoid with meaningful autonomy without remote humans | 2029+ | 1X's own 95%+ autonomy target is 2028; teleop is the launch product. [48][49] |
| Robotaxi at 1M rides/week (Waymo) | End of 2026 (stated goal) | 500K/week Sept 2026, 2x in ~6 months historically. [24][25] |
| Tesla unsupervised fleet at Waymo's current scale | Not before 2028 | 1M unsupervised miles vs Waymo's 4M+/week. [28][53] |
| Optimus at 10K+ units/year | Unknowable; no company target exists | Musk declined to forecast. [23] |

---

## What people are underestimating (ANALYSIS)

1. **RL-from-deployment is the real story, not bigger VLAs.** π*0.6's 2x throughput and 2x failure reduction came from autonomous experience and corrections, not from more parameters. The vendor that first runs this loop across hundreds of paying sites gets a compounding advantage that model size cannot buy. [4]
2. **The Chinese "toy" shipments are a data flywheel too.** 19,100 units in six months, most with cameras and open SDKs in labs and integrators, produce an enormous long tail of embodiment data that Unitree and AgiBot can license or absorb, and GR00T N1.6 already trains on AgiBot Genie-1 and Unitree G1 data. [16][6]
3. **Teleoperation-as-product is a feature, not a scandal.** 1X's remote Expert mode is the most honest go-to-market in the segment: it ships the hardware, bills for outcomes, and collects the exact data needed to remove the human. Expect Figure and others to copy it quietly. [48][49]
4. **Regulators, not models, will set the AV rate of growth from here.** Within one week in September 2026: an NHTSA Cybercab probe, a Waymo child-collision investigation, an SF mayor calling for stricter rules. Deployment curves will be shaped by these more than by v15 or the sixth-gen driver. [29][53]
5. **Actuator supply is the Nvidia-GPU moment of 2027–2028.** Hyundai Mobis at 350,000 actuators/year and Chinese reducer makers are the only volume sources on the horizon; a 30-DoF humanoid at 100K units/year needs 3M actuators. Whoever owns reducers, roller screws and tactile skins owns the margin. [20][32]
6. **Defense is funding the general-purpose stack.** Anduril's $20B Army ceiling and Shield AI's CCA win are paying for edge-autonomy software, perception under EW and manufacturing automation that will flow back into civilian robotics faster than the reverse. [58][14]
7. **The Western humanoid valuation gap is a bet on autonomy quality, not on shipments.** Figure at $39B has shipped hundreds; Unitree at ~$50B market cap has shipped over 10,000 and is profitable. If Helix-class autonomy does not show up as measurable OEE on factory floors by 2027, the gap closes from the top down. [44][15]

---

## Key numbers

| Metric | Value | Status | Source |
|---|---|---|---|
| Global humanoid shipments, 1H 2026 | 19,100 (+272% YoY) | Confirmed (SAG) | [16] |
| 2026 humanoid shipment forecast | ~60,000 units, ~$1.6B revenue | Speculation (SAG) | [16] |
| Chinese share of humanoid supply | 97% | Confirmed (SAG) | [16] |
| Unitree 2025 humanoids shipped / revenue / adj. profit | 5,511 / RMB 1.70B / RMB 591M | Confirmed (prospectus) | [15] |
| Unitree IPO first-day close / market cap | +460% / ~RMB 342B (~US$50B) | Confirmed | [15] |
| Unitree G1 / H2 list price | $13,500 / $29,900 | Confirmed | [15] |
| Figure valuation (last priced) | $39B (Sept 2025) | Confirmed | [44] |
| Figure 02 BMW contribution 2025 | 30,000 vehicles | Confirmed (company) | [17] |
| Skild AI valuation | $14B (Jan 2026) | Confirmed | [9] |
| Apptronik valuation / capital raised | ~$5.3B / ~$1B | Confirmed | [19] |
| Generalist valuation | $3B (Aug 2026) | Reported | [8] |
| Agility SPAC | $2.5B (June 2026) | Confirmed | [46] |
| Hyundai Atlas plan | 25,000+ units from 2028; $130–140K early unit cost | Confirmed | [20] |
| 1X NEO price / first batch | $20K or $499/mo; 10,000 units | Confirmed (company) | [47][48] |
| Optimus 2025 units doing useful work | 0 (Musk, Jan 2026) | Confirmed | [23] |
| Waymo paid rides/week | >500,000 (Sept 2026) | Confirmed | [24] |
| Waymo cities / fleet / miles | 14 / ~4,000 / 200M+ autonomous | Confirmed | [24][53][54] |
| Tesla unsupervised miles | 1M (3 Sept 2026) | Confirmed (company) | [28] |
| Cybercabs registered in Texas | 45 | Confirmed | [29] |
| Baidu Apollo Go cumulative rides | >100M (1H 2026) | Reported | [26] |
| Anduril valuation / 2025 revenue | $61B / ~$2.1B | Confirmed / Reported | [13][58] |
| Shield AI valuation | $12.7B | Confirmed | [14] |
| Ukraine drone production | >3M/yr; 7M projected 2026 | Confirmed (Atlantic Council) | [31] |
| Amazon robots deployed | >1M (July 2025) | Confirmed | [59] |
| π0.6 inference | 63 ms/action chunk on one H100 | Confirmed | [3] |
| GR00T N1.6 | 3B params, open weights | Confirmed | [6] |
| Helix 02 System 0 | 10M params at 1 kHz | Confirmed (company) | [7] |
| Gemini On-Device 2 novel-platform success | 53.3% (SO101), 75.6% (Dexmate) | Confirmed (model card) | [2] |

---

## Sources

1. Google DeepMind, "Gemini Robotics 1.5 brings AI agents into the physical world," 25 Sept 2025. https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/
2. Google DeepMind, "Gemini Robotics On-Device 2 Model Card," 30 July 2026. https://deepmind.google/models/model-cards/gemini-robotics-on-device-2/
3. Physical Intelligence, "π0.6 Model Card," 17 Nov 2025. https://website.pi-asset.com/pi06star/PI06_model_card.pdf
4. Physical Intelligence, "π*0.6: A VLA that Learns from Experience," 17 Nov 2025. https://www.pi.website/blog/pistar06
5. Physical Intelligence, "π0.7: a Steerable Model with Emergent Capabilities," 16 Apr 2026. https://www.pi.website/blog/pi07
6. NVIDIA GEAR Lab, "GR00T N1.6," 15 Dec 2025. https://research.nvidia.com/labs/gear/gr00t-n1_6/
7. Figure AI, "Introducing Helix 02: Full-Body Autonomy," 27 Jan 2026. https://www.figure.ai/news/helix-02
8. TechCrunch, "Robotics startup Generalist reaches $3B valuation, sources say," 25 Aug 2026. https://techcrunch.com/2026/08/25/robotics-startup-generalist-reaches-3b-valuation-sources-say/
9. TechCrunch, "Robotics software maker Skild AI hits $14B valuation," 14 Jan 2026. https://techcrunch.com/2026/01/14/robotic-software-maker-skild-ai-hits-14b-valuation/
10. Business Wire, "Skild AI Raises $1.4B, Now Valued Over $14B," 14 Jan 2026. https://www.businesswire.com/news/home/20260114335623/en/
11. CNBC, "Apptronik raises $520 million at $5 billion valuation for Apollo robot," 11 Feb 2026. https://www.cnbc.com/2026/02/11/apptronik-raises-520-million-at-5-billion-valuation-for-apollo-robot.html
12. TechCrunch, "Physical Intelligence is reportedly in talks to raise $1B, again," 27 Mar 2026 (via TechCrunch tag index). https://techcrunch.com/tag/physical-intelligence/
13. TechCrunch, "Anduril raises $5B, doubling its valuation to $61B," 13 May 2026; "Anduril reportedly in talks at $100B," 24 July 2026 (tag index). https://techcrunch.com/tag/anduril/
14. TechCrunch, "Defense startup Shield AI lands $12.7B valuation, up 140%, after US Air Force deal," 26 Mar 2026. https://techcrunch.com/2026/03/26/defense-startup-shield-ai-lands-12-7b-valuation-up-140-after-u-s-air-force-deal/
15. Tim Harper, "Humanoid Robots in 2026: Unitree's IPO and the Race to Make Robots Useful" (citing Unitree prospectus, SSE/Xinhua first-day data, Omdia), Aug 2026. https://timharper.net/humanoid-robots-2026-unitree-physical-ai/
16. Humanoids Daily, "Global Humanoid Shipments Surge 272% in 1H 2026 as AGIBOT Overtakes Unitree" (Smart Analytics Global data), Aug 2026. https://www.humanoidsdaily.com/news/global-humanoid-shipments-surge-272-in-1h-2026-as-agibot-overtakes-unitree
17. Figure AI, "F.03 Arrives at BMW," 30 June 2026. https://www.figure.ai/news/f-03-at-bmw
18. TechCrunch, "Toyota contracts seven Agility humanoid robots for Canadian factory," 19 Feb 2026; Agility Robotics newsroom. https://www.agilityrobotics.com/news
19. The Robot Report, "Apptronik brings in another $520M to ramp up Apollo production," Feb 2026. https://www.therobotreport.com/apptronik-brings-in-another-520m-to-ramp-up-apollo-production/
20. Korea Herald, "Hyundai Motor Group to deploy 25,000 Atlas robots across factories," 20 May 2026. https://www.koreaherald.com/article/10741955
21. The Register, "Boston Dynamics' humanoid robot is already in mass production," 6 Jan 2026. https://www.theregister.com/2026/01/06/boston_dynamics_atlas_production/
22. Automate.org, "CES 2026: Boston Dynamics Set to Ship First Atlas Humanoids This Year," Jan 2026. https://www.automate.org/robotics/industry-insights/boston-dynamics-to-begin-production-on-redesigned-atlas-humanoid-in-2026
23. Electrek, "Tesla pushes Optimus V3 reveal later this year - again," 22 Apr 2026. https://electrek.co/2026/04/22/tesla-optimus-production-fremont-model-sx-line/
24. Waymo blog, "Denver, San Diego, and Tampa launch," 1 Sept 2026; "Houston opens to all," 20 Aug 2026; "Munich," 25 Aug 2026. https://waymo.com/blog/
25. TechCrunch, "Waymo's skyrocketing ridership in one chart," 27 Mar 2026. https://techcrunch.com/2026/03/27/waymo-skyrocketing-ridership-in-one-chart/
26. BCC Media, "Robotaxi Enters the Fast Lane: Baidu's Apollo Go, Pony.ai, and WeRide," 2026. https://bccmedianews.com/?p=6474
27. Teslarati, "Tesla expands Unsupervised Robotaxi service to two new cities," 18 Apr 2026. https://www.teslarati.com/tesla-expands-unsupervised-robotaxi-service-two-new-cities/
28. Teslarati, "Tesla crosses major Unsupervised Self-Driving milestone," 6 Sept 2026. https://www.teslarati.com/tesla-crosses-major-unsupervised-self-driving-milestone/
29. TechCrunch, "Feds launch investigation into Tesla's Cybercab deployment," 4 Sept 2026; "TechCrunch Mobility: Tesla Cybercab hits the road — and a snag," 6 Sept 2026. https://techcrunch.com/2026/09/04/feds-launch-investigation-into-teslas-cybercab-deployment/
30. Breaking Defense, "Everyone is learning the wrong lessons from Ukraine's drone war," Aug 2026. https://breakingdefense.com/2026/08/everyone-is-learning-the-wrong-lessons-from-ukraines-drone-war/
31. Atlantic Council, "The coming compute war in Ukraine," 16 Mar 2026. https://www.atlanticcouncil.org/content-series/the-big-story/the-coming-compute-war-in-ukraine/
32. PatSnap, "Humanoid robot engineering challenges for industry," 2026. https://www.patsnap.com/resources/blog/articles/humanoid-robot-engineering-challenges-for-industry/
33. PatSnap Eureka, "Humanoid Robot Dexterous Manipulation 2026." https://www.patsnap.com/resources/blog/rd-blog/humanoid-robot-dexterous-manipulation-2026-patsnap-eureka/
34. Google DeepMind, "Gemini Robotics On-Device brings AI to local robotic devices," June 2025. https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/
35. Google DeepMind blog index, "Gemini Robotics 2" and "Gemini Robotics ER 2," July 2026. https://deepmind.google/discover/blog/
36. Google DeepMind, Gemini Robotics model family page (partners: Agile Robots, Apptronik, Boston Dynamics), accessed 7 Sept 2026. https://deepmind.google/models/gemini-robotics/
37. TechCrunch, Physical Intelligence coverage index (Jan–July 2026). https://techcrunch.com/tag/physical-intelligence/
38. NVIDIA blog, robotics tag (LeRobot models 6 July 2026; JetPack 7.2, 1 June 2026; agent skills, 3 June 2026). https://blogs.nvidia.com/blog/tag/robotics/
39. Figure AI newsroom ("Introducing Index," 25 Aug 2026; Nscale 100,000-GPU partnership, 3 Sept 2026; Helix 02 home demos, Mar/May 2026). https://www.figure.ai/news
40. Sacra, "Figure AI valuation, funding & news," 2026. https://sacra.com/c/figure-ai/
41. Tesla Inc., Form 10-Q for quarter ended 30 June 2026 (AI infrastructure $10.823B gross). https://www.sec.gov/Archives/edgar/data/0001318605/000162828026049270/tsla-20260630.htm
42. Tesery, "Tesla Optimus 3 Production Timeline," 2026 (fan/retail site; treat as speculation). https://www.tesery.com/blogs/news/elon-musk-reveals-aggressive-production-timeline-for-tesla-optimus-3
43. The Uncanny Squad, "Figure 03 & Helix AI," 2026. https://www.theuncannysquad.com/blog/figure-03-helix-ai-why-you-should-know
44. Teahose, "Figure AI Valuation (2026): $39B," 2026. https://www.teahose.com/guides/figure-ai-valuation
45. TechTimes, "Hyundai Commits 25,000 Atlas Robots to Own Factories: Union Blocks Deployment Without Labor Deal," 22 May 2026. https://www.techtimes.com/articles/317005/20260522/
46. TechCrunch, "Agility announces $2.5 billion SPAC merger," 24 June 2026; "Agility Robotics goes public; CEO says consumer robots far off," 5 July 2026 (tag index). https://techcrunch.com/tag/agility-robotics/
47. 1X Technologies, "NEO Home Robot," accessed 7 Sept 2026. https://www.1x.tech/discover/neo-home-robot
48. Notebookcheck, "1X NEO: Household robot set to launch by the end of 2026 – but with a controversial catch," 2026. https://www.notebookcheck.net/1X-NEO-Household-robot-set-to-launch-by-the-end-of-2026-but-with-a-controversial-catch.1295772.0.html
49. heise online, "1X to deliver humanoid household robot Neo to US customers in 2026," 8 May 2025. https://www.heise.de/en/news/1X-to-deliver-humanoid-household-robot-Neo-to-US-customers-in-2026-11287205.html
50. TrendForce, "China's Humanoid Robot Market to Reach CNY 15 Billion in 2026," 19 Aug 2026. https://www.trendforce.com/presscenter/news/20260819-13189.html
51. DIGITIMES, "Galbot's fast rise marks new wave in China's humanoid robot race," 21 Aug 2026. https://www.digitimes.com/news/a20260821PD225/humanoid-robot-2026.html
52. Forbes, John Koetsier, "China's Humanoid Robot Lead Is Misleading. Here's Why," 10 Aug 2026. https://www.forbes.com/sites/johnkoetsier/2026/08/10/
53. TechCrunch, Waymo coverage index (recall of nearly 4,000 robotaxis 18 June 2026; freeway return 29 July; NHTSA probe Aug 2026; Munich 25 Aug; Denver/San Diego/Tampa 1 Sept). https://techcrunch.com/tag/waymo/
54. Road to Autonomy, "Waymo Accelerates Multi-City Rollout and Targets 1M Weekly Rides," 2026. https://www.roadtoautonomy.com/waymo-accelerates-multi-city-rollout/
55. TechCrunch, Zoox coverage index (federal approval 30 July 2026; paid rides 5 Aug; airport 3 Sept). https://techcrunch.com/tag/zoox/
56. Wikipedia, "Apollo Go," accessed 7 Sept 2026. https://en.wikipedia.org/wiki/Apollo_Go
57. CNBC, "'Robotaxi has reached a tipping point': Baidu, Nvidia...," 20 Nov 2025. https://www.cnbc.com/2025/11/20/global-robotaxi-race-heats-up-between-us-and-chinese-rivals.html
58. Benzinga, "Anduril And Shield AI: A Massive Bet On Autonomous Warfare," June 2026. https://www.benzinga.com/markets/private-markets/26/06/53235906/
59. TechCrunch, "Amazon deploys its one millionth robot, releases generative AI model," 1 July 2025. https://techcrunch.com/2025/07/01/amazon-deploys-its-one-millionth-robot-releases-generative-ai-model
60. CNBC, "Amazon says new warehouse robot can 'feel' items," 7 May 2025. https://www.cnbc.com/2025/05/07/meet-amazons-robot-vulcan-the-first-with-a-sense-of-touch.html
61. GCN, "Amazon's warehouse fleet crossed 1 million robots...," 2026. https://gcn.com/amazon-s-warehouse-fleet-crossed-million/20362/
62. Real Investment Advice, "Amazon Has Over One Million Robots!," 2 July 2025. https://realinvestmentadvice.com/resources/blog/amazon-has-over-one-million-robots/
63. Google DeepMind, "Genie 3: A new frontier for world models," 5 Aug 2025. https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/
64. Spheron, "GPU Infrastructure Behind World Models: Genie 3, Marble, and Real-Time Interactive AI," 17 June 2026; NVIDIA, "Cosmos 3: Omnimodal World Models for Physical AI," arXiv 2606.02800, June 2026. https://www.spheron.network/blog/gpu-infrastructure-world-models-2026/
65. Introl, "World Models Race 2026" (Genie 3 robotics transfer claim; secondary). https://introl.com/blog/world-models-race-agi-2026
66. IEEE Spectrum robotics index (Aug 2026: "Do We Need Superhuman Humanoid Robots?", "Is Shipyard Welding the Right First Job for Humanoid Robots?"). https://spectrum.ieee.org/topic/robotics/
67. arXiv 2510.03342, "Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer," Oct 2025. https://arxiv.org/abs/2510.03342
68. Hugging Face, "nvidia/GR00T-N1.6-3B." https://huggingface.co/nvidia/GR00T-N1.6-3B
