# The Frontier, Report 11: Brain-Computer Interfaces, Neurotech, and AI-Biology Convergence

*Research date: 7 September 2026. Claims are labeled **CONFIRMED** (primary source, peer review, or regulatory record), **REPORTED** (credible secondary reporting, company announcement, or preprint), or **SPECULATION** (my inference or forward projection).*

---

## TL;DR

1. **Implanted BCIs crossed from demo to clinical pipeline.** Neuralink is in the mid-20s for implanted participants, Synchron is running/preparing the first pivotal trial for an implantable BCI, Precision Neuroscience has a cleared 510(k) device and a Medtronic distribution channel, and Paradromics has FDA approval to start a speech-restoration trial. No implanted BCI has yet received full FDA market approval.
2. **Speech decoding is the killer app**, not cursor control. The 2025 UCSF/Berkeley streaming brain-to-voice work put latency at ~80 ms, and every serious player — Neuralink, Paradromics, UCSF, Stanford — has converged on it.
3. **Non-invasive got a real product.** Meta's Neural Band (sEMG wristband) shipped as consumer hardware in late 2025, the first mass-market neural-adjacent input device, backed by a *Nature* paper on cross-subject generalization without calibration.
4. **Money is loud, biology is slow.** Neuralink raised at ~$9B; Merge Labs launched with $252M and no device. Isomorphic Labs slipped its first-in-human from end-2025 to 2026.
5. **The first credibly AI-discovered drug is in Phase III** — Insilico's rentosertib, in China, for idiopathic pulmonary fibrosis, with Phase IIa results in *Nature Medicine*.
6. **AI diagnosis benchmarks are spectacular and unregulated.** MAI-DxO reported 85.5% on NEJM CPC cases vs ~20% for physicians — an unpublished, non-deployed result on a benchmark that is not clinical practice.
7. **Where AI has actually shipped in medicine is boring**: ~1,451 FDA-authorized AI-enabled devices, ~76% radiology, ~0.6% pathology, plus ambient documentation scribes that are not regulated as devices at all.
8. **Genome-scale foundation models arrived** (Evo 2, 9T base pairs, published in *Nature* in 2026), and AI-designed proteins are producing real wet-lab wins (Retro/OpenAI's RetroSOX/RetroKLF reprogramming factors).
9. **Personalized gene editing is the strongest single data point for compression** — baby KJ went from diagnosis to bespoke base editor in about six months, and the FDA has agreed to a platform-style trial protocol.
10. **Verdict on "AI compresses a decade of biology into years":** true and demonstrated for *design and prediction*; false so far for *validation, manufacturing, trials, and reimbursement*. The bottleneck moved, it did not disappear.

---

## 1. Implanted BCIs: the 2026 state of play

### Neuralink

**REPORTED:** Neuralink has reached roughly 26 implanted participants across its trials as of mid-2026, up from about a dozen at the start of the year [4]. The company closed a $650M round at a ~$9B valuation [1][3].

**CONFIRMED:** The core PRIME/CONVOY studies target cursor and robotic-arm control in people with severe paralysis. **REPORTED:** Neuralink's speech program (decoding intended phonemes and resynthesizing the user's pre-injury voice) received FDA Breakthrough Device Designation in May 2025 [8].

**REPORTED:** Blindsight — a visual-cortex stimulating implant intended to give low-resolution vision to people who have lost both eyes and optic nerve function — is targeted for first-in-human in 2026, with an international arm involving Cleveland Clinic Abu Dhabi [1][5].

**SPECULATION:** Blindsight is the highest-variance thing in the field. Cortical stimulation for vision has a long history of low-resolution phosphene results (Second Sight, Orion); Neuralink's advantage is channel count, not a solved neuroscience problem. Expect "the participant perceived structured phosphenes" rather than "the participant read text" for at least the first two years.

### Synchron

**CONFIRMED/REPORTED:** Synchron's endovascular Stentrode is delivered through the jugular vein — no craniotomy — and it holds the first FDA IDE for a permanently implanted BCI (the COMMAND study). It raised a ~$200M Series D in late 2025 and is moving into a pivotal trial in 2026, the study that would support a PMA [7][9].

**SPECULATION:** Synchron's lower bandwidth is a real ceiling for speech, but its surgical profile is the reason it is likely to be first to market. Being first to an FDA-approved implantable BCI matters more for reimbursement precedent than for capability.

### Precision Neuroscience

**CONFIRMED:** Precision's Layer 7 Cortical Interface — a thin-film surface array that sits on the cortex without penetrating it — received 510(k) clearance in April 2025 for temporary (≤30 day) intraoperative use [7].

**REPORTED:** In January 2026 Precision announced a partnership with Medtronic to integrate Layer 7 with the StealthStation surgical navigation platform [7].

**SPECULATION (labeled analysis):** This is the most underrated regulatory move in the sector. Precision built a revenue-generating, cleared product out of the *diagnostic* use of its array while the therapeutic implant matures, and it now rides an installed base of neurosurgical navigation systems. Clinical data accrues as a byproduct of paid procedures.

### Paradromics

**CONFIRMED:** In November 2025 the FDA approved Paradromics' clinical study of its Connexus device for speech restoration in people with severe paralysis [6]. Paradromics had previously done a brief intraoperative human implant in 2025.

---

## 2. Non-invasive and adjacent

### Meta Neural Band

**CONFIRMED:** Meta published its wrist-based sEMG neuromotor interface work in *Nature* (2025), reporting cross-participant generalization — decoding gestures and handwriting from surface EMG with no per-user calibration, using models trained on thousands of participants [11].

**CONFIRMED:** The Meta Neural Band shipped 30 September 2025 bundled with Meta Ray-Ban Display glasses at $799 [10].

**Labeled analysis:** This is not a brain-computer interface — it reads motor neuron output at the muscle, not cortex. But it is the only neural-adjacent interface with a consumer install base, and the generalization-without-calibration result is the scientifically important part: it is the "foundation model" moment for biosignals.

### Merge Labs

**REPORTED:** Merge Labs, co-founded by Sam Altman, emerged from stealth in January 2026 with a $252M seed round in which OpenAI wrote the largest check; other backers include Bain Capital Ventures and Gabe Newell [12][13]. The approach: non-implanted, using ultrasound plus engineered molecular reporters/actuators rather than electrodes. It signed a multi-year license for Butterfly Network's ultrasound-on-chip technology [14].

**SPECULATION:** Merge is a research bet, not a device company, and the molecular half (gene-delivered ultrasound-sensitive reporters) implies gene therapy regulatory risk on top of device risk. A $252M seed at zero clinical evidence is a statement about the price of optionality on "high-bandwidth non-invasive," not about technical readiness. Timeline to human data: 2029+.

### Academic speech decoding

**CONFIRMED:** Littlejohn, Anumanchipalli et al., *Nature Neuroscience*, March 2025: a streaming brain-to-voice neuroprosthesis decoding in 80 ms increments, synthesizing intelligible speech in the participant's pre-injury voice, with accuracy matching the earlier non-streaming pipeline [15][16].

**Labeled analysis:** Latency was the last psychological barrier. Offline decoders that produced text minutes later were assistive tech; a sub-100 ms voice loop is conversation. The remaining problems are electrode longevity, generalization beyond single participants, and the fact that essentially all published results come from a handful of individuals.

---

## 3. AI in clinical medicine

### What is actually authorized

**CONFIRMED:** The FDA's AI-enabled device list reached **1,451 authorizations** through end-2025, with 221 in 2023, 253 in 2024, and a record 295 in 2025. Radiology accounts for ~1,104 devices (~76%); pathology for about 9 (~0.6%) [17][18].

**Labeled analysis:** The distribution is the story. Thirty years of AI device authorization is overwhelmingly image triage and measurement — narrow, deterministic, single-task tools. Almost none are generative or LLM-based. The gap between "AI passes medical licensing exams" and "AI is a regulated diagnostic" remains close to total.

### Benchmarks

**REPORTED:** Microsoft AI's MAI-DxO orchestrator, paired with OpenAI o3, solved 85.5% of 304 NEJM clinicopathological conference cases restructured as the interactive Sequential Diagnosis Benchmark (SDBench), versus a mean ~20% for 21 US/UK physicians tested without references or colleagues [19][20]. Not peer-reviewed at the time of the announcement, and not deployed.

**CONFIRMED:** OpenAI's HealthBench, built with input from 262 physicians across 60 countries, comprises 5,000 realistic multi-turn health conversations graded against physician-written rubrics [21].

**Labeled analysis:** The 20% physician figure is not a measurement of physician competence — the clinicians were denied textbooks, colleagues, and search, which is not how medicine is practiced. The honest reading: LLM orchestration is now superhuman at *retrieval-heavy differential diagnosis on written vignettes*, a real and useful skill, and says nothing about physical exam, uncertainty under time pressure, or liability.

### Ambient documentation

**CONFIRMED/REPORTED:** Ambient scribes (Abridge, Nuance DAX, Ambience, Suki) are the fastest-adopted clinical AI in history, and they sit **outside** the FDA device perimeter because they document rather than diagnose [18].

**Labeled analysis (what people underestimate):** The scribes are the wedge. They put an always-listening LLM into the exam room with clinician trust and a billing justification. Every diagnostic suggestion feature later added to that surface arrives on infrastructure already deployed at scale — and largely outside device regulation until it makes a claim.

---

## 4. AI drug discovery

### Isomorphic Labs

**REPORTED:** Isomorphic slipped its first human trials from "end of 2025" to 2026, with lead oncology and immunology candidates approaching first-in-human [22][23]. It co-developed AlphaFold 3 with DeepMind and runs its own Isomorphic Drug Design Engine (IsoDDE). It has partnerships with Novartis and Eli Lilly and raised $600M in 2025.

### Insilico Medicine

**CONFIRMED:** Rentosertib (ISM001-055), a TNIK inhibitor for idiopathic pulmonary fibrosis with both target and molecule generated by AI, published Phase IIa results in *Nature Medicine* (2025) [24].

**REPORTED:** Insilico initiated a Phase III trial in July 2026 — randomized, double-blind, placebo-controlled, ~320 IPF patients across China [25]. Separately, an inhaled formulation received China CDE IND clearance in April 2026, Insilico's 13th pipeline program to reach the clinic [26]. Rentosertib holds FDA Orphan Drug Designation (2023) and CDE Breakthrough Therapy Designation (May 2025).

**Labeled analysis:** This is the single most important data point in AI drug discovery, and it is Chinese-regulated. Rentosertib is the first molecule with an AI-nominated *target* and AI-generated *chemistry* to reach Phase III. If it reads out positive, the "AI drugs fail at the same rate" critique loses its strongest empirical footing. If it fails, it will be because target biology was wrong — which is exactly the part AI is worst at.

### Open models

**CONFIRMED:** Boltz-2 (MIT + Recursion, MIT-licensed, June 2025) predicts structure *and* binding affinity, reported to approach FEP-level accuracy at ~1000x lower cost [27][28]. Chai Discovery released Chai-1/Chai-2 in the same open/openish lane. AlphaFold 3 was published in *Nature* (2024) with initially restricted access, later opened for academic use.

**Labeled analysis:** The interesting inversion of 2025-26 is that the open-weight structure/affinity stack (Boltz, Chai) is close enough to the closed stack (AlphaFold 3, IsoDDE) that structure prediction has commoditized. Value has moved to proprietary *experimental data* — which is why Recursion, Xaira, and Isomorphic all invest in wet labs, and why Recursion's own post-Boltz-2 messaging emphasizes data generation over model architecture.

### Xaira and the capital picture

**REPORTED:** Xaira launched in 2024 with over $1B, anchored by ARCH and Foresite with David Baker involved; it has produced no clinical candidate publicly as of 2026 [29]. Recursion (post-Exscientia merger) has cut pipeline programs and reduced headcount, with several clinical readouts failing to justify its earlier valuation.

**Labeled analysis:** The sector's honest scorecard is: many INDs, several Phase I/II readouts, one Phase III (rentosertib), zero approvals attributable to end-to-end AI discovery. The measurable win is *speed to candidate* (Insilico's ~18 months target-to-IND vs a 4-6 year norm) — a genuine compression of the earliest, cheapest phase.

---

## 5. Protein, genome, and gene editing

### Foundation models for biology

**CONFIRMED:** Evo 2 (Arc Institute, NVIDIA, Stanford), trained on ~9.3 trillion DNA base pairs across all domains of life, published in *Nature* in 2026 [30][31]. It predicts variant pathogenicity — >90% accuracy on BRCA1 variant classification without task-specific training — and generates sequences at genome scale. Trained on ~2,000 H100s, roughly 150x the compute of AlphaFold and about 2x ESM3.

**CONFIRMED:** ESM3 (EvolutionaryScale) generated esmGFP, a fluorescent protein ~58% identical to the nearest natural sequence, estimated to represent hundreds of millions of years of simulated evolutionary distance.

**CONFIRMED:** OpenCRISPR-1 (Profluent) is an LLM-generated gene editor with no natural counterpart, released under a permissive license, with editing activity comparable to SpCas9 in human cells.

### Personalized editing

**CONFIRMED:** KJ Muldoon, born with severe CPS1 deficiency, received a bespoke LNP-delivered base editor at CHOP/Penn beginning February 2025, with follow-up doses in March and April 2025 [32][33]. He was discharged after 307 days [34].

**REPORTED:** One year on, the CHOP/Penn team is building a platform trial; the FDA has agreed to a protocol that could enroll as few as five patients across at least three genetic variants [35]. MIT Technology Review named base-edited personalized therapy a 2026 Breakthrough Technology [36].

**Labeled analysis:** KJ is the clearest existence proof of compression anywhere in this report — roughly six months from diagnosis to a one-patient drug, a timeline that is normally a decade. But note what did the compressing: not a large language model. It was pre-existing base-editing chemistry, LNP delivery, cheap sequencing, and a regulator willing to treat the *platform* rather than the *product* as the unit of review. The lesson is regulatory-architectural as much as computational.

### Approved editing therapies

**CONFIRMED:** Casgevy (exa-cel), the first approved CRISPR therapy, remains approved in the US/UK/EU for sickle cell disease and transfusion-dependent beta thalassemia, with slow real-world uptake driven by cost (~$2.2M) and the burden of myeloablative conditioning. **REPORTED:** In-vivo base editing programs (Verve, Beam) have advanced human data for PCSK9 and AATD, moving editing away from ex-vivo transplant logistics.

---

## 6. Longevity and cell reprogramming

**REPORTED:** OpenAI built **GPT-4b micro**, a small protein-engineering model, for Retro Biosciences (Sam Altman is Retro's principal investor, having put in $180M). Retro used it to design SOX2 and KLF4 variants — RetroSOX and RetroKLF — reporting >50-fold increases in pluripotency marker expression and improved DNA repair during reprogramming; >30% of designed SOX2 variants and nearly half of KLF4 variants outperformed wild type in screens [37][38].

**CONFIRMED-ish caveat:** As of mid-2026 this remains a company/OpenAI write-up and preprint rather than a peer-reviewed publication [39].

**REPORTED:** Altos Labs remains the best-capitalized player (~$3B launch, Bezos-backed) and has published partial reprogramming work in vivo; NewLimit (Brian Armstrong) raised a $130M Series B in 2025 for epigenetic reprogramming of hepatocytes and T cells.

**Labeled analysis:** Reprogramming is where AI-designed proteins have their cleanest wet-lab win, because the assay is fast, cheap, and quantitative — exactly the conditions under which generative design compounds. Contrast with oncology, where the assay is a three-year trial. **Prediction (SPECULATION):** AI-biology compression will be visibly real first in domains with cell-level readouts (reprogramming, enzyme engineering, antibody affinity maturation) and visibly absent in domains gated by organism-level endpoints.

---

## 7. Organoid intelligence

**REPORTED:** Cortical Labs shipped the CL1 — ~200,000 lab-grown human neurons on a CMOS multi-electrode array with a closed-loop "biological intelligence operating system" — as a ~$35,000 developer unit, plus remote "Wetware-as-a-Service" access [40][41]. FinalSpark runs a comparable remote neuroplatform in Switzerland.

**Labeled analysis:** Organoid intelligence is, for now, a drug-discovery and neuroscience instrument wearing a computing costume. The Pong result (DishBrain, 2022) demonstrated adaptation, not computation at useful scale. The near-term real market is disease modeling and neurotoxicity screening. The compute story requires solving culture lifespan, yield, and I/O bandwidth, none of which have a Moore's-law analog. **SPECULATION:** No credible general-purpose biological compute product before 2030; the ethics literature will outpace the capability by a wide margin.

---

## 8. The "AI compresses a decade of biology into years" thesis

### Evidence for

- **Structure prediction is solved enough to be infrastructure.** AlphaFold 2/3, Boltz-2, Chai — a problem that consumed 50 years is now an API call, and the open-weight versions are near-parity.
- **Target-to-IND timelines have genuinely halved or better.** Insilico's ~18-month, ~$3M target-to-preclinical-candidate figure for rentosertib is documented and now carried into Phase III.
- **Design spaces are being explored that humans could not enumerate.** esmGFP, OpenCRISPR-1, RetroSOX — proteins with no natural analog, functional on first synthesis.
- **Genome-scale prediction is here.** Evo 2 does zero-shot variant effect prediction across all domains of life.
- **N-of-1 medicine went from thought experiment to discharged patient in one year.**
- **Diagnosis benchmarks fell fast.** MAI-DxO's 85.5% on NEJM CPCs is a step change over 2023-era results.

### Evidence against

- **Clinical failure rates have not moved.** The published analyses of AI-discovered molecules show good Phase I safety rates but Phase II efficacy rates in line with historical norms — because Phase II failure is a *target biology* problem, and AI mostly improves *chemistry*.
- **Timelines still slip.** Isomorphic's first-in-human moved a full year. Neuralink's Blindsight has slipped repeatedly.
- **Regulatory clocks are unmoved.** A pivotal BCI trial takes years regardless of decoder quality. Nothing about a foundation model changes the enrollment rate of a rare-disease trial.
- **Zero approvals.** No drug discovered end-to-end by AI has market approval anywhere as of September 2026.
- **The FDA device record is unglamorous** — 76% radiology triage — after 30 years.
- **Benchmarks are not clinics.** MAI-DxO is unpublished, undeployed, and evaluated on retrospective written cases.
- **Wet-lab throughput is the binding constraint.** Generative models produce more candidates than any organization can synthesize and assay; the queue is now physical.
- **Replication and data quality problems persist.** Much AI-bio evidence is company blog posts and preprints, not peer review — including two of the flagship results in this report (MAI-DxO, GPT-4b micro).

### My read (SPECULATION, labeled analysis)

The thesis is directionally correct but misdescribed. AI has compressed the *hypothesis-generation* half of biology by roughly an order of magnitude, and has compressed the *validation* half by approximately zero. Because validation was always the expensive part — Eroom's law is a clinical-trials law, not a chemistry law — the aggregate compression of "biology" is far smaller than the compression of the parts people can see on Twitter.

The correct forecast is therefore not "a decade in a year" but **a barbell**: in domains where the experiment is a cell assay measured in days, expect 5-20x speedups and they are already visible. In domains where the experiment is a human being measured in years, expect 1.0-1.3x — coming from better patient selection and trial design, not from better molecules. The gap between those two numbers will be the defining frustration of biotech in the late 2020s, and it will be misread as AI failing when it is actually AI succeeding at the half of the problem it can reach.

---

## What people are underestimating

*(All labeled analysis / SPECULATION.)*

1. **Reimbursement, not regulation, is the BCI bottleneck.** Everyone watches the FDA. But the first approved implantable BCI faces a CMS coverage question with no precedent, for a population of tens of thousands. A device that works and is not reimbursed is a research program. Synchron's low-surgical-burden profile is as much a reimbursement strategy as a safety one.
2. **The ambient scribe is a Trojan horse.** The most consequential clinical AI deployment of this decade is unregulated, already in thousands of exam rooms, and one product decision away from making diagnostic suggestions.
3. **Speech decoding will hit an ethics wall before a technical one.** Once decoders generalize across users, "did you intend to say that" becomes a legal question. Neural data privacy law (Colorado, California, Chile) exists but is untested against a device that reconstructs inner speech.
4. **China is where AI drug discovery will be proven or disproven first.** Rentosertib's Phase III is Chinese. Faster enrollment, lower trial cost, and a regulator granting breakthrough status to AI-derived molecules mean the first definitive readout on the thesis will likely not be American.
5. **Open-weight bio models have quietly outrun the biosecurity framework.** Evo 2 can generate genome-scale sequences; OpenCRISPR-1 is downloadable. Screening obligations sit with DNA synthesis providers, a voluntary chokepoint. This is the least-defended part of the whole stack.
6. **The wet-lab is the new GPU shortage.** Compute is abundant; robotic assay capacity, cell lines, and primary human tissue are not. Expect "cloud labs" to become a strategically contested asset the way data centers did.
7. **Neuralink's valuation is priced on Blindsight, not on cursor control.** Motor BCI is a small market with strong non-invasive competition. Vision restoration is a large market with no competition. The $9B is an option on the harder program.
8. **The most underrated result of the period is Meta's calibration-free sEMG generalization,** because it proves biosignal foundation models transfer across bodies. That principle, applied to invasive recordings, is what makes a BCI a product rather than a per-patient science project.

---

## Key numbers

| Item | Value | Label |
|---|---|---|
| Neuralink implanted participants (mid-2026) | ~26 | REPORTED |
| Neuralink valuation / last round | ~$9B / $650M | REPORTED |
| Synchron Series D (Nov 2025) | ~$200M | REPORTED |
| Merge Labs seed (Jan 2026) | $252M | REPORTED |
| Meta Neural Band + Ray-Ban Display price | $799 | CONFIRMED |
| Streaming brain-to-voice decode latency | 80 ms | CONFIRMED |
| FDA AI-enabled device authorizations (cumulative, end-2025) | 1,451 | CONFIRMED |
| — new in 2025 | 295 | CONFIRMED |
| — radiology share | ~76% (1,104) | CONFIRMED |
| — pathology share | ~0.6% (9) | CONFIRMED |
| MAI-DxO (with o3) on SDBench NEJM cases | 85.5% vs ~20% physicians | REPORTED |
| HealthBench | 5,000 conversations, 262 physicians, 60 countries | CONFIRMED |
| Rentosertib Phase III enrollment target | ~320 patients, China | REPORTED |
| Insilico pipeline programs in clinic | 13 | REPORTED |
| Evo 2 training data | ~9.3T DNA base pairs, 2,000 H100s | CONFIRMED |
| Evo 2 BRCA1 variant classification | >90% accuracy | CONFIRMED |
| RetroSOX/RetroKLF pluripotency marker gain | >50x | REPORTED |
| Baby KJ: hospital days to discharge | 307 | CONFIRMED |
| CHOP/Penn planned platform trial size | as few as 5 patients, ≥3 variants | REPORTED |
| Cortical Labs CL1 | ~200,000 neurons, ~$35,000 | REPORTED |
| Approved drugs discovered end-to-end by AI | 0 | CONFIRMED |
| Approved implantable BCIs (FDA, market) | 0 | CONFIRMED |

---

## Sources

1. Roic News, "Neuralink Secures $650M Funding, Advances Blindsight," 28 Jan 2026 — https://www.roic.ai/news/neuralink-secures-650m-funding-advances-blindsight-vision-technology-toward-human-trials-01-28-2026
2. Neuralink — https://neuralink.com/
3. TSG Invest, "Neuralink Stock: $9B Valuation," 2026 — https://tsginvest.com/neuralink/
4. Basenor, "Neuralink Reaches 26th Patient," 2026 — https://www.basenor.com/blogs/news/neuralink-reaches-26th-patient-in-ongoing-brain-computer-interface-trials
5. Neurapod, "Neuralink Blindsight Trial: What to Expect," 2026 — https://www.neurapod.com/blog/neuralink-blindsight-human-trials-what-to-expect
6. STAT News, "FDA approves Paradromics' BCI trial for speech restoration," 20 Nov 2025 — https://www.statnews.com/2025/11/20/fda-approves-paradromics-bci-trial-for-speech-restoration/
7. Beyond Tomorrow, "Brain-Computer Interface Clinical Trials Accelerate in 2026" — https://beyondtmrw.org/article/brain-computer-interface-clinical-trials-accelerate-in-2026
8. Press.farm, "Neuralink Human Trials 2026" — https://press.farm/neuralink-human-trials-2026-patient-progress-telepathy-app/
9. TechTimes, "Synchron Brain Implant Targets 2026 Pivotal Trial," 6 Jun 2026 — https://www.techtimes.com/articles/317929/20260606/synchron-brain-implant-targets-2026-pivotal-trial-first-fda-approved-bci.htm
10. VR/AR Wiki, "Meta Neural Band" — https://vrarwiki.com/wiki/Meta_Neural_Band
11. Meta, "Reality Labs Research on Wrist-Based sEMG published in Nature," 2025 — https://www.meta.com/blog/reality-labs-surface-emg-research-nature-publication-ar-glasses-orion/
12. Tom's Hardware, "Sam Altman raises $252 million for BCI venture," Jan 2026 — https://www.tomshardware.com/peripherals/wearable-tech/sam-altman-raises-usd252-million-for-brain-computer-interface-venture-but-merge-labs-is-still-in-an-early-research-phase
13. MassDevice, "OpenAI invests in Sam Altman's Merge Labs BCI startup," 2026 — https://www.massdevice.com/openai-invests-money-in-sam-altmans-merge-labs-bci-startup/
14. StockTitan, "Merge Labs and Butterfly Network partner," Jan 2026 — https://www.stocktitan.net/news/BFLY/merge-labs-and-butterfly-network-partner-to-advance-ultrasound-based-h1d0ix3tmo7p.html
15. Littlejohn et al., "A streaming brain-to-voice neuroprosthesis to restore naturalistic communication," *Nature Neuroscience*, Mar 2025 — https://www.nature.com/articles/s41593-025-01905-6
16. UC Berkeley, "Brain-to-voice neuroprosthesis restores naturalistic speech," 2025 — https://vcresearch.berkeley.edu/news/brain-voice-neuroprosthesis-restores-naturalistic-speech
17. AuntMinnie, "Radiology dominates thirty years of FDA AI device approvals," 2026 — https://www.auntminnie.com/imaging-informatics/artificial-intelligence/article/15830219/radiology-dominates-thirty-years-of-fda-ai-device-approvals
18. PDP Spectra, "AI Medical Devices and FDA in 2026: SaMD, PCCP," 2026 — https://pdpspectra.com/blog/ai-medical-devices-fda-2026/
19. Microsoft AI, "The Path to Medical Superintelligence," 2025 — https://microsoft.ai/news/the-path-to-medical-superintelligence/
20. PYMNTS, "Microsoft Pushes Toward 'Medical Superintelligence,'" 2026 — https://www.pymnts.com/artificial-intelligence-2/2026/microsoft-pushes-toward-medical-superintelligence-in-healthcare/
21. OpenAI, HealthBench — https://openai.com/index/healthbench/
22. Clinical Trials Arena, "Isomorphic Labs prepares to launch trials for AI-designed drugs" — https://www.clinicaltrialsarena.com/news/isomorphic-labs-prepares-trials-ai-designed-drugs/
23. MedPath, "Isomorphic Labs Pushes Back AI-Designed Drug Clinical Trials to 2026" — https://trial.medpath.com/news/isomorphic-labs-pushes-back-ai-designed-drug-clinical-trials-to-2026
24. Insilico Medicine, "Nature Medicine Publication of Phase IIa Results of Rentosertib" — https://insilico.com/news/tnrecuxsc1-insilico-announces-nature-medicine-publi
25. Insilico Medicine, "Insilico Initiates Phase III Clinical Trial for Rentosertib," Jul 2026 — https://insilico.com/news/xmjsn4l091-insilico-initiates-phase-iii-clinical-tr
26. TipRanks, "Insilico Wins China IND Nod for Inhaled Rentosertib," Apr 2026 — https://www.tipranks.com/news/company-announcements/insilico-medicine-wins-china-ind-nod-for-ai-discovered-ipf-drug-rentosertib
27. Recursion, "MIT and Recursion Release Boltz-2" — https://ir.recursion.com/news-releases/news-release-details/mit-and-recursion-release-boltz-2-next-generation-ai-model
28. Recursion, "Beyond Boltz-2: Toward More Powerful Drug Discovery Tools" — https://www.recursion.com/news/beyond-boltz-2-toward-more-powerful-drug-discovery-tools
29. On Healthcare, "The AI Drug Discovery Capital Stack in 2026" — https://www.onhealthcare.tech/p/the-ai-drug-discovery-capital-stack
30. Brixia/Arc et al., "Genome modelling and design across all domains of life with Evo 2," *Nature*, 2026 — https://www.nature.com/articles/s41586-026-10176-5
31. Arc Institute, Evo tools page — https://arcinstitute.org/tools/evo
32. CHOP, "World's First Patient Treated with Personalized CRISPR Gene Editing Therapy" — https://www.chop.edu/news/worlds-first-patient-treated-personalized-crispr-gene-editing-therapy-childrens-hospital
33. Wikipedia, "KJ Muldoon" — https://en.wikipedia.org/wiki/KJ_Muldoon
34. Inside Precision Medicine, "First Personalized CRISPR Patient Baby KJ Discharged" — https://www.insideprecisionmedicine.com/topics/precision-medicine/first-personalized-crispr-gene-editing-therapy-patient-baby-kj-discharged/
35. CHOP Research Institute, "A Year After First-in-World Gene-Editing Therapy, CHOP-Penn Team Aims to Scale the Science," 2026 — https://www.research.chop.edu/cornerstone-blog/a-year-after-first-in-world-gene-editing-therapy-chop-penn-team-aims-to-scale-the-science
36. MIT Technology Review, "Base-edited baby: 10 Breakthrough Technologies 2026," 12 Jan 2026 — https://www.technologyreview.com/2026/01/12/1129999/gene-editing-base-edited-baby-personalized-drugs-2026-breakthrough-technology/
37. OpenAI, "Accelerating life sciences research with Retro Biosciences" — https://openai.com/index/accelerating-life-sciences-research-with-retro-biosciences/
38. BioPharmaTrend, "OpenAI and Retro Biosciences Report 50x Pluripotency Marker Expression Gains" — https://www.biopharmatrend.com/news/potential-breakthrough-in-cell-reprogramming-as-openai-and-retro-biosciences-report-50x-pluripotency-marker-expression-gains-1357/
39. Longevity.Technology, "OpenAI sheds new light on longevity research" — https://longevity.technology/news/openai-sheds-new-light-on-longevity-research/
40. Cortical Labs, CL1 — https://corticallabs.com/cl1
41. ABC News, "Melbourne start-up launches 'biological computer' made of human brain cells," Mar 2025 — https://www.abc.net.au/news/science/2025-03-05/cortical-labs-neuron-brain-chip/104996484
