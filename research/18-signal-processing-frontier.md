# The Signal Processing Frontier (September 2026)

*Thesis under test: "Classical DSP is a mature/stale discipline where AI foundation-model approaches are only beginning to be applied, and a fast-moving builder can find high-value niches."*

Evidence labels used throughout: **CONFIRMED** (primary source: paper, filing, vendor release), **REPORTED** (secondary reporting, vendor claims not independently verified, market-research estimates), **SPECULATION** (my analysis/extrapolation).

---

## TL;DR

1. **The thesis is half right.** Classical DSP is mature but not stale: the *algorithms* (FFT, IIR/FIR, Kalman, adaptive filters, CS) are settled, but the *tooling* and *workflow* around them are ossified (MATLAB + Simulink, vendor-locked FPGA flows, bench instruments with 1990s UX). That workflow gap, not the math, is where a builder wins.
2. **Foundation models have already taken over speech, audio codecs, ASR, and speech-to-speech.** Whisper is no longer the default; 12.5 Hz neural codecs (Mimi) are the substrate of a whole voice-AI industry; DL-reconstruction MRI is FDA-cleared and clinically routine. These are *not* open niches.
3. **Time-series foundation models (TSFMs) are real but modest.** Chronos-2, TimesFM-2.5, Toto 2.0, Moirai 2.0 beat Seasonal Naive by roughly a third on GIFT-Eval/fev-bench; a May 2026 operational study finds supervised specialists still win on physically constrained systems and recommends *routing* between model classes rather than one universal model [1][3][7].
4. **Physiological-signal FMs are the most over-claimed area.** Two independent 2025-26 EEG benchmarks find foundation models give 0.9-1.2% gains over small CNNs and that "larger FMs do not necessarily yield better generalization" [8][9]. PPG/ECG FMs (Apple, AnyPPG) look stronger because the data is 100x larger.
5. **RF/wireless is the most *active* and *least consolidated* frontier.** IQFM (Jun 2025), Radio-FM (Aug 2026), CSI-JEPA (May 2026), SpectrumFM, EMind, WavesFM, a dedicated IEEE JSTSP special issue (May 2026 deadline) - many papers, no winner, no shared corpus, and the best-funded startup (DeepSig) has raised only ~$14M total [16][17][19][22][57].
6. **Machine learning is now in production in the hardest real-time physics pipelines**: Aframe was deployed into the LIGO-Virgo-KAGRA production search on 28 Aug 2025 and reported a candidate 11.6 s after merger; DINGO-BNS does full neutron-star parameter estimation in ~1 s (Nature, Mar 2025) [25][26].
7. **The "AI-native instrument" category just opened.** Liquid Instruments raised $50M (co-led by Keysight, May 2026) and shipped GenInst Studio (Jul 2026): natural language -> validated FPGA instrument on Moku hardware. Keysight itself only has ADS copilots, not scope copilots [46][47].
8. **Edge hardware consolidated fast**: Qualcomm bought Edge Impulse (Mar 2025), Ambiq IPO'd (Sep 2025, NYSE: AMBQ), Syntiant filed for a ~$300M IPO after buying Knowles' consumer mics, Innatera's Pulsar spiking chip is in production at <1 mW always-on [36][37][38][39].
9. **The hiring problem is real and structural**: US EE enrollment down ~90% relative to CS since the 1980s; 44% of orgs report difficulty hiring analog engineers, 33% RF; 3 retirees per 1-2 new grads [45]. Any tool that lets a non-DSP engineer do DSP work sells into this.
10. **Best builder bets (details in the Top-10 section)**: LLM-driven DSP-to-FPGA/HLS codegen with hardware-in-the-loop verification; an open RF/IQ foundation model + open corpus; signal-analysis copilots on top of commodity scopes/SDRs; vertical anomaly-detection for DAS/vibration; and DDSP-based real-time audio tooling.

---

## 1. State of the field

### 1.1 Where classical DSP still dominates (CONFIRMED unless noted)

- **Filters, FFT, resampling, mixing, sync, PLLs**: untouched. Every neural receiver, codec, and TSFM still sits behind a classical front end (AGC, decimation, framing, STFT/mel). NVIDIA's neural receiver only replaces channel estimation, equalization and demapping; sync, FFT/OFDM and LDPC decoding remain conventional [20].
- **State estimation**: Kalman/IMM filters remain the production default in automotive radar tracking. KalmanNet variants beat the KF under model mismatch and non-Gaussian noise, but a radar-tracking study found KalmanNet "underperforms IMM filters in velocity/acceleration and especially uncertainty calibration, raising safety concerns"; the research trend is hybrid (Recursive KalmanNet keeps analytic covariance propagation) [51].
- **Compressed sensing / sparse recovery**: alive as a *theory*, but in the one place it reached mass deployment (MRI) it has been overtaken by learned reconstruction: GE AIR Recon DL got expanded FDA clearance (Oct 2025), Siemens Deep Resolve is FDA-cleared, and a 2025 neuroradiology study shows DL halving scan time at equal quality [50].
- **Wavelets**: survive mainly as inductive bias inside networks (e.g. wavelet-driven masked reconstruction for PPG FMs, Jan 2026) rather than as standalone pipelines [12].
- **Real-time constraints**: anything with a microsecond deadline on an MCU, DSP core or FPGA fabric is still hand-written fixed-point C/HDL.

### 1.2 Where deep learning has already won (CONFIRMED)

- **Speech recognition**: "Whisper is no longer the default answer" in 2026; NVIDIA Parakeet TDT (RTFx >2,000), Canary-Qwen 2.5B, Mistral Voxtral (4B, Apache-2.0, streaming, Feb 2026), Qwen3-ASR, Kyutai STT, Moonshine for edge [29][62].
- **Audio codecs for AI**: Mimi (Kyutai) runs at 12.5 Hz frames, ~1.1 kbps, 80 ms latency, and is the substrate for Moshi; the whole 2025-26 low-frame-rate codec literature (FlexiCodec, U-Codec, DualCodec) exists to feed audio LLMs [27]. Caveat: for human-to-human calls, Opus is still the sensible default (REPORTED) [27].
- **Speech-to-speech**: full-duplex models at ~200 ms (Moshi), PersonaPlex at 205 ms with 100% interruption success on Full-Duplex-Bench vs 60.6% for Moshi and 43.9% for Gemini Live (REPORTED from paper claims) [28].
- **Denoising / enhancement / separation**: dominated by DL; ICASSP 2026 (Barcelona, May 2026, >4,500 accepted papers) is saturated with diffusion-based enhancement and speech-FM adaptation [56].
- **Imaging**: full AI ISP (Chips&Media + Visionary.ai) shown at CES 2026; DL MRI recon in clinical routine [35][50].
- **Bioacoustics**: Perch 2.0 (14,597 species) and NatureLM-audio are the standard tooling for ecological monitoring [52].

### 1.3 Tools landscape

- **MATLAB**: still the default in signal processing and controls because of Simulink and toolboxes; >51,000 companies use it (REPORTED, Enlyft). MathWorks shipped **MATLAB Copilot** (Oct 7, 2025; expanded in R2026a), so "LLM in the loop" is now an incumbent feature, not a startup moat [44]. Consensus that MATLAB usage peaked ~2015 and declines as grads arrive Python-native (REPORTED) [60-ish; see Sources].
- **Python**: SciPy/NumPy for offline; JAX gives GPU FFT-convolution 1.5-20x over SciPy but has known numerical/perf gaps vs scipy.signal (open JAX issues) (CONFIRMED) [see Sources].
- **GNU Radio**: 3.10.12 (Feb 2025) is the stable line; **GNU Radio 4 hit RC1 on 22 Mar 2026** with a modern-C++ rewrite, compile-time block merging (2-10x speedups, "tens of GS/s" in fused pipelines), and a reflection system that makes blocks self-describing - which is exactly what an LLM agent wants to drive [43].
- **FPGA/HLS**: Vitis/Vivado HLS remain the path; LLM-for-HDL is a hot benchmark area (ResBench Mar 2025, FPGAgent Aug 2026, "Benchmarking LLMs for Verilog Design Flows" Jul 2026), but correctness and resource-efficiency remain the gaps [32].
- **Silicon**: AMD Versal RF (14-bit, 32 GSPS, 18 GHz RF-ADC, 80 TOPS DSP) shipping since Nov 2025, presented at Hot Chips 2026 - but targeted at A&D/T&M with no hobbyist pricing [41]. Edge: ADI MAX78000/78002 (M4 + CNN accelerator, microjoule inference), TI, NXP, Ambiq Apollo, Syntiant NDP, Innatera Pulsar [36][40].
- **Cheap entry points**: RTL-SDR Blog V3/V4 + Raspberry Pi 5 is the documented hobbyist stack; RFSoC 4x2 is $2,499 academic-only; ZCU208 is $17,658 [42][60].

### 1.4 Why DSP is hard to hire (CONFIRMED stats, from Quilter's 2026 compilation of IEEE/BLS/Electronic Design data)

- US EE enrollment down ~90% relative to CS since the 1980s; ~20,000 EE grads/year, fewer than half enter engineering roles.
- ~50% of US engineers are over 50; 3 retirees per 1-2 new grads.
- Hardest to fill: analog 44%, embedded 43%, RF 33%; average hire takes 58-62 days [45].
- SPECULATION: DSP sits at the intersection of the three hardest buckets (analog intuition + embedded + RF/comm theory), and the skill is learned mostly through apprenticeship on proprietary toolchains, not open-source repos. This is why an "expert-in-a-box" product has real pull.

---

## 2. AI meets signals

### 2.1 Time-series foundation models (CONFIRMED results, my synthesis)

| Model | Org / date | Notes |
|---|---|---|
| Chronos-2 | Amazon, Oct 2025 | Zero-shot univariate + multivariate + covariates via group attention; SOTA on fev-bench, GIFT-Eval, Chronos-II. GIFT-Eval WQL win rate 79.8%, skill 46.6% vs TimesFM-2.5 70.0%/42.4% [1][6] |
| TimesFM-2.5 | Google, 2025 | 200M params; #1 on GIFT-Eval before Chronos-2 [6] |
| Toto 2.0 | Datadog, 14 May 2026 | 4M-2.5B params, Apache-2.0; trained on observability + synthetic data only; tops BOOM (2,807 series, 350M points) at every size; ensemble tops GIFT-Eval [4][5] |
| Moirai 2.0 | Salesforce, Feb 2026 | Decoder-only, quantile loss; 30x smaller than Moirai-1.0-Large, 2x faster; "performance plateaus with increasing parameter count" [2] |
| Sundial | Tsinghua | GIFT-Eval WQL win rate only 14.4% [6] |
| TimeGPT | Nixtla | Closed API; no public GIFT-Eval entry |

Limitations that matter for builders:
- The best FMs reduce error vs Seasonal Naive by only about a third on fev-bench; a widely read critique argues this means "the amount of learnable structure in benchmark problems is fairly limited" [7].
- Short-history yearly/quarterly/monthly series: compare to Naive before trusting the FM [7].
- **"Assessing the Operational Viability of FMs for TS Forecasting" (May 2026)**: FMs win on transferable periodic structure and cold-start; supervised specialists win on physically constrained processes; a "Complexity Router" that assigns each series to a model class beats a universal FM on both accuracy and inference cost [3].
- Calibration of FM probabilistic outputs is questioned (PMC 2026) [see Sources].
- SPECULATION: TSFMs are a commodity layer now (Apache-2.0 weights from four vendors). Value is in routing, domain data (Datadog's edge is *its* telemetry), and wrapping - not in training another one.

### 2.2 Physiological signals

- **PPG/ECG** (CONFIRMED): Apple's AHMS foundation model used ~20M PPG segments from ~141K participants over ~3 years (ICLR 2024; ML research post Feb 2025) [11]. AnyPPG (Nov 2025) is ECG-guided, trained on >100,000 hours, and ran the first PPG phenome-wide screen across 1,468 disease phenotypes [12]. Pulse-PPG (IMWUT 2025) is an open, field-trained PPG FM [13]. Wavelet- and statistical-prior masked models (Jan 2026) continue.
- **Acoustic health** (CONFIRMED): Google HeAR trained on 300M+ 2-second clips; open weights on Hugging Face; Salcit's Swaasa uses it for TB screening in India [14][15].
- **EEG/brain** (CONFIRMED, negative): EEG-FM-Benchmark compares 12 open EEG FMs (LaBraM, BENDR, NeuroGPT, CBraMod, EEGPT, BIOT...) vs 9 DL baselines and 7 classical ML across 13 datasets: linear probing often underperforms, from-scratch CNN/Transformers "remain competitive," and "larger FMs do not necessarily yield better generalization" [8]. "Are Large Brainwave Foundation Models Capable Yet?" (Jul 2025) finds 0.9-1.2% gains over traditional architectures at 1000x the parameters [9]. A critical review (2025) documents inconsistent evaluation protocols and fixed 10-20 montages limiting LaBraM/NeuroLM [10]. IEEE SPM published a brain-to-content survey (vol. 41 no. 6) [57].
- SPECULATION: PPG/ECG FMs work because consumer wearables created 100K-participant datasets; EEG FMs stall because clinical EEG is small, heterogeneous in montage, and noisy. The asymmetry is data, not architecture.

### 2.3 RF / wireless / radar

- **IQ foundation models** (CONFIRMED papers, REPORTED numbers): IQFM (Jun 2025) - contrastive SSL on over-the-air multi-antenna IQ; 99.67% modulation accuracy with one label per class; 65.45% AoA; LoRA-adapted RF fingerprinting 96.05% [16]. Radio-FM (6 Aug 2026) - 15 datasets across modulation/radar/comm, SOTA on 13/15 benchmarks, strong few-shot [17]. Also SpectrumFM, EMind, WavesFM, LWM, WirelessGPT, LatentWave/WirelessJEPA; a comprehensive survey (Aug 2026) lists Transformers as the dominant backbone [18].
- **WiFi CSI sensing**: IEEE 802.11bf standardizes sensing measurements; CSI-JEPA (May 2026) claims +10.6 pp mean accuracy over supervised transformer baselines and positions itself as a "protocol-compatible sensing primitive" [19].
- **Neural receivers**: NVIDIA's Sionna-trained receiver replaces channel estimation + equalization + demapping with <1 ms latency on an A100 via TensorRT at ~0.7 dB cost under strict latency [20]. DeepSig demonstrated an AI-native air interface on NVIDIA Aerial at MWC 2025 and an Open RAN base station on DGX Spark at MWC26 with SRS and the AI-RAN Alliance (Feb 2026); OmniSIG now embedded in PCTEL's SeeHawk Scout [21].
- **Funding reality** (REPORTED): DeepSig, the category's oldest company, has raised ~$14.4M across 8 rounds, latest ~$10M in Feb 2025, with NTIA grants among sources [22]. The IEEE JSTSP special issue on wireless FMs closed submissions May 15, 2026 [57].
- **Automotive radar**: raw-ADC datasets enabled end-to-end nets (ADCNet, T-FFTRadNet); 2026 work learns spatial structure from pre-beamforming per-antenna range-Doppler data via cross-modal supervision [55]. Arbe pivoted to industrial/off-road "Physical AI" radar in Mar 2026 (REPORTED) - a sign that the automotive 4D radar market is harder than pitched [55].
- **Data scarcity** (CONFIRMED): RadioML 2018.01 (24 modulations, 2048 IQ samples each) is still the most-used dataset; SigMF is the metadata standard; every RF FM paper trains on a different private or mixed corpus [see Sources].

### 2.4 Vibration, industrial, DAS, seismic

- Predictive maintenance is production-grade (Augury, Tractian); 2026 deployments report +3-8 OEE points and 20-40% maintenance cost reduction (REPORTED, vendor/integrator claims) [54].
- **DAS**: market estimates range from ~$0.87B (2026) to $2.8B (2026) depending on the analyst - treat as REPORTED and inconsistent; pipeline monitoring ~35% of demand; VIAVI launched an edge-AI DAS interrogator head (Mar 2026) [24].
- **SeisLM** (Oct 2024) is a wav2vec2-style FM on worldwide 3-channel seismograms; 2026 work adapts vision FMs to seismic denoising; spectral-boosted FNOs cut frequency bias 40% in 3D seismic wavefield modeling (REPORTED) [23][34].

### 2.5 Gravitational waves / astronomy (CONFIRMED)

- **Aframe** deployed into LVK production 28 Aug 2025; first to report S250830m at 11.6 s post-merger; AMPLFI does ML parameter estimation for public alerts. ML now spans every stage of detection [25].
- **DINGO-BNS** (Nature, 5 Mar 2025): full BNS characterization in ~1 s vs ~1 h for the fastest classical method [26].
- CERN hosted "AI for Gravitational Waves" May 2026; YOLO-style detection of glitches in time-frequency data is routine in detector characterization [see Sources].

### 2.6 Audio, DDSP, neural operators, learned ISP

- **DDSP**: "DDSP Guitar Amp" (ICASSP 2025 oral) matches black-box baselines at <10% of ops per sample [33]; NablAFx (2025) provides a differentiable gray/black-box audio-effects framework; known optimization pathologies in sinusoidal/FM parameter learning remain [see Sources].
- **Neural operators / PINNs**: unified PINN+NO framing (Jan 2026); exactly conservative PINOs (2025); SC-FNO (ICLR 2025); PINOs for in-situ acoustic absorber characterization (Apr 2026) [34]. SPECULATION: NOs are replacing *inner loops* of solvers (forward models in inversion), not the solvers themselves.
- **Learned ISP**: first "full AI ISP" at CES 2026; the argument is that shrinking pixels push optics past their limit and only neural restoration pushes back (Jun 2026 preprint) [35].
- **Implicit neural representations**: no prominent 2025-26 signal-domain breakthroughs surfaced in this search (REPORTED absence).

### 2.7 LLMs as DSP engineers / SDR agents (CONFIRMED papers, early-stage)

- **SignalLLM** (Sep 2025): first general-purpose LLM agent framework for SP; RAG-decomposed subtasks + code synthesis; demonstrated on radar detection, HAR, text compression, with gains mainly in few/zero-shot [30].
- **RadioMaster** (Jun 2026): multi-agent "intent-to-air" radio signal generation on top of GNU Radio-style pipelines [31].
- **LLM Agents as 6G Orchestrator**, RRC-layer emulation (Jan 2026), RFAmpDesigner (AAAI'25) [31].
- **HDL/HLS**: ResBench (56 problems, resource-aware), FPGAgent (Aug 2026, autonomous HLS generation + verification), CorrectHDL (HLS as reference for agentic HDL) [32].
- Incumbents: MATLAB Copilot (Oct 2025), Keysight ADS Chat/Copilot (Dec 2025), Liquid Instruments GenInst Studio (Jul 2026) [44][46][47].

### 2.8 Edge / neuromorphic / TinyML (CONFIRMED)

- Qualcomm acquired Edge Impulse (10 Mar 2025) [37]. Ambiq IPO: 4.6M shares at $24, $97.2M net, 280M+ devices shipped, Q2'25 revenue $17.9M [38]. Syntiant bought Knowles' consumer MEMS mic unit ($114.4M), revenue jumped to $271.8M in 2025, filed S-1 for a ~$300M IPO (Jul 2026), 20M+ NDPs shipped [39].
- Innatera Pulsar: hybrid analog/digital SNN + INT8 CNN engine, 0.5 mW typical/10 mW max, 384 KB, TSMC 28 nm, production Q2 2025, est. <$5 in volume [36]. BrainChip Akida Pico, SynSense Xylo target always-on audio/biosignal. Neuromorphic patent filings rose 401% in 2025 (REPORTED, Patsnap) [61].
- ADI MAX78000/78002: M4F + RISC-V + CNN accelerator, "1/100th the power" claim (vendor) [40].

---

## 3. Builder opportunities

### Top 10 concrete things a fast builder could ship in 6-12 months (labeled ANALYSIS / SPECULATION)

1. **DSP-to-FPGA agent with hardware-in-the-loop verification.** Why now: FPGAgent/CorrectHDL show agentic HLS is feasible but correctness is the gap; GR4's self-describing blocks and Liquid's GenInst prove the demand pattern. Tools: Vitis HLS, cocotb/Verilator, a $300 Artix/Zynq board farm, Claude/GPT-class models. Who pays: A&D primes, T&M vendors, radar/SDR startups paying $200K+ per FPGA engineer they cannot hire [32][43][45][46].
2. **Open RF/IQ foundation model + open multi-source IQ corpus (SigMF-native).** Why now: 6+ competing academic models, none open at scale, RadioML 2018 still the benchmark; JSTSP special issue means reviewers want a standard. Tools: RTL-SDR/Pluto/USRP capture fleet, JEPA/masked-recon pretraining, Hugging Face release. Who pays: spectrum regulators (NTIA grants fund DeepSig), defense SIGINT, telecom O-RAN vendors [16][17][22].
3. **Signal-analysis copilot for commodity scopes/SDRs.** Why now: Keysight has copilots for ADS but not instruments; R&S/Tek have none public; GenInst is Moku-only. Tools: SCPI/VISA drivers, PyVISA, sigrok, a vision-language model on screenshots plus raw-capture DSP tools. Who pays: hardware startups with 1 EE and 10 firmware engineers [46][47].
4. **DAS / fiber-sensing event classifier as a service.** Why now: interrogators now embed edge AI (VIAVI Mar 2026), pipeline monitoring is 35% of a multi-billion market, but labels are rare and per-site. Tools: SeisLM-style SSL on DAS strain-rate, few-shot adaptation. Who pays: pipeline operators, telcos with dark fiber, rail [23][24].
5. **Vibration/acoustic anomaly detection on <$5 neuromorphic or CNN-MCU silicon.** Why now: Pulsar/MAX78000/Ambiq make always-on inference at <1 mW real; Augury proves willingness to pay. Tools: Edge Impulse (now Qualcomm), ADI ai8x tooling, Innatera Talamo. Who pays: OEMs of pumps/HVAC/compressors [36][40][54].
6. **PPG/ECG analytics layer on open FMs for non-Apple wearables.** Why now: AnyPPG/Pulse-PPG are open; FDA 510(k) precedent (AliveCor, Apple) shows the path is validation, not novelty. Tools: PhysioNet, MIMIC waveforms, on-device distillation. Who pays: ring/patch OEMs without ML teams; must budget 12-18 months for clearance [12][13][48].
7. **Cough/breath acoustic screening built on HeAR.** Why now: open weights, proven TB use case in India, benchmark literature emerging (cough regression benchmark, Jun 2026). Tools: HeAR embeddings + linear heads. Who pays: NGOs, public health programs, telehealth [14][15].
8. **DDSP-based real-time audio tools (amp/pedal modeling, room correction, hearing-aid tuning).** Why now: <10% compute vs black-box at equal quality makes MCU deployment viable. Tools: NablAFx, JUCE, ESP32-S3/Cortex-M55. Who pays: guitar-gear OEMs, hearables [33].
9. **TSFM router product for industrial telemetry.** Why now: four Apache-2.0 TSFMs exist; the May 2026 study shows routing beats any single model on accuracy and cost. Tools: Chronos-2/Toto 2.0/Moirai 2.0 + statsforecast baselines + a feature-based router. Who pays: SCADA/historian vendors, utilities [1][3][4].
10. **Open SAR/InSAR change-detection pipeline on Sentinel-1 + commercial VHR.** Why now: ICEYE/Umbra/Capella open datasets, WV-Net shows 10M-image SSL works, IEEE GRSS 2025 contest used Umbra/Capella. Tools: STAC, torchgeo, WV-Net weights. Who pays: insurers, infrastructure monitors, defense analysts [59].

Honorable mentions (SPECULATION): EMI/EMC debugging assistant (Engentica has an early build; near-field scanning + spectrum analyzer + LLM) [53]; OPM-MEG real-time decoding tooling as wearable MEG leaves the lab [58]; LLM-driven GNU Radio 4 flowgraph synthesis once GR4 is stable [43].

### Hardware enablers (CONFIRMED)

- Versal RF: 32 GSPS/18 GHz single-chip, shipping (A&D pricing) [41]. RFSoC 4x2 at $2,499 for academics only [42]. Raspberry Pi 5 + RTL-SDR V4/HackRF/Pluto is the sub-$300 stack [60]. Innatera Pulsar (<$5 est.), MAX78000, Ambiq Apollo for edge [36][38][40]. Phone sensors: HeAR and PPG FMs are explicitly designed for phone/watch capture [11][14].

---

## 4. Where the thesis is wrong (honest counterpoints)

1. **"Only beginning to be applied" is false for audio, speech, imaging, MRI, GW astronomy and ASR.** These are years past the tipping point and dominated by well-funded labs (Google, NVIDIA, Kyutai, Mistral, GE/Siemens). A small team will not out-model them [20][25][29][50].
2. **Incumbents already ship LLM features.** MATLAB Copilot (Oct 2025), Keysight ADS copilots (Dec 2025), Liquid Instruments GenInst (Jul 2026), Qualcomm/Edge Impulse. The "AI-native instrument" wedge is real but was taken by a Series-C company with Keysight's money [44][46][47].
3. **Foundation-model gains are small in the domains a small team can afford.** EEG FMs: +0.9-1.2% [9]. TSFMs: ~1/3 error reduction vs Seasonal Naive, worse on short histories, and supervised specialists win on physically constrained systems [3][7]. Moirai 2.0 explicitly reports plateauing with scale [2].
4. **Classical still wins where safety/calibration matters.** IMM filters over KalmanNet in automotive tracking due to uncertainty calibration [51]. Neural receivers cost ~0.7 dB under latency constraints [20]. Opus over neural codecs for actual phone calls [27].
5. **Data scarcity is the binding constraint, not modeling.** RF has no shared corpus beyond RadioML; DAS labels are per-site; EEG montages are inconsistent. Apple's advantage is 141K consented participants, not architecture [8][11][16].
6. **Regulatory friction is real and slow.** >1,000 FDA AI-enabled devices exist, mostly radiology and mostly 510(k), and wearable-cardiac clearance is tied to validated sensitivity/specificity against a reference standard, not to the algorithm [48]. Butterfly's gestational-age tool took until Mar 2026 [49].
7. **The RF FM market is capital-starved**: DeepSig at ~$14M total after nearly a decade suggests buyers (telcos, DoD) pay slowly and via grants [22].
8. **Real-time/edge deployment is unforgiving**: sub-millisecond deadlines on MCUs still mean fixed-point C; FM-sized models do not fit. The winners at the edge are tiny CNNs and SNNs, not transformers [36][40].

Net: the thesis holds for **RF/IQ, DAS/industrial, EEG-adjacent tooling, DSP codegen and instrument UX**; it fails for **speech/audio/imaging/ASR/MRI** and for anyone hoping to win by training a bigger model.

---

## 5. Key numbers

| Metric | Value | Label | Src |
|---|---|---|---|
| Chronos-2 GIFT-Eval WQL win rate / skill | 79.8% / 46.6% (TimesFM-2.5: 70.0% / 42.4%) | CONFIRMED | [1][6] |
| TSFM error reduction vs Seasonal Naive (fev-bench) | ~1/3 | REPORTED | [7] |
| Toto 2.0 sizes / BOOM benchmark | 4M-2.5B params / 2,807 series, 350M points | CONFIRMED | [4][5] |
| Moirai 2.0 vs 1.0-Large | 30x smaller, 2x faster, 36M-series corpus | CONFIRMED | [2] |
| EEG FM gain over traditional DL | 0.9-1.2% | CONFIRMED | [9] |
| Apple PPG FM dataset | ~20M segments, ~141K participants, ~3 years | CONFIRMED | [11] |
| AnyPPG training data | >100,000 hours; 1,468 phenotypes screened | CONFIRMED | [12] |
| HeAR pretraining | 300M+ two-second clips | CONFIRMED | [14] |
| IQFM one-shot modulation accuracy | 99.67% | REPORTED (paper) | [16] |
| Radio-FM | SOTA on 13/15 benchmarks, 15 pretraining datasets | REPORTED (paper) | [17] |
| NVIDIA neural receiver | <1 ms on A100; ~0.7 dB penalty under latency limit | CONFIRMED | [20] |
| Aframe production deployment | 28 Aug 2025; 11.6 s alert latency | CONFIRMED | [25] |
| DINGO-BNS inference | ~1 s vs ~1 h classical | CONFIRMED | [26] |
| Mimi codec | 12.5 Hz, ~1.1 kbps, 80 ms latency | CONFIRMED | [27] |
| Full-duplex S2S latency | Moshi ~200 ms; OpenAI Realtime ~320 ms; cascaded 400-800 ms | REPORTED | [28] |
| Parakeet TDT throughput | RTFx >2,000 | REPORTED | [29] |
| DDSP guitar amp compute | <10% ops/sample vs black-box | CONFIRMED | [33] |
| Innatera Pulsar power | 0.5 mW typ / 10 mW max; est. <$5 | CONFIRMED / REPORTED | [36] |
| Ambiq IPO | $24/share, $97.2M net, 280M+ devices | CONFIRMED | [38] |
| Syntiant 2025 revenue | $271.8M (from $13.6M in 2024) | REPORTED | [39] |
| Versal RF ADC | 14-bit, 32 GSPS, 18 GHz; 80 TOPS DSP | CONFIRMED | [41] |
| RFSoC 4x2 / ZCU208 price | $2,499 (academic) / $17,658 | CONFIRMED | [42] |
| GNU Radio 4 RC1 | 22 Mar 2026; 2-10x from block merging | CONFIRMED | [43] |
| Liquid Instruments Series C | $50M, co-led by Keysight, 2 May 2026 | CONFIRMED | [46] |
| DeepSig total raised | ~$14.4M | REPORTED | [22] |
| FDA AI-enabled devices | >1,000 cumulative, radiology largest | REPORTED | [48] |
| EE hiring difficulty | analog 44%, embedded 43%, RF 33% | CONFIRMED (survey) | [45] |
| ICASSP 2026 accepted papers | >4,500 | CONFIRMED | [56] |
| DAS market 2026 | $0.87B-$2.8B (analyst spread) | REPORTED | [24] |

---

## Sources

1. Chronos-2: From Univariate to Universal Forecasting, arXiv 2510.15821 (17 Oct 2025) - https://arxiv.org/abs/2510.15821
2. Moirai 2.0: When Less Is More for Time Series Forecasting, arXiv 2511.11698 (Nov 2025, v-final 3 Feb 2026) - https://arxiv.org/abs/2511.11698
3. Assessing the Operational Viability of Foundation Models for Time Series Forecasting, arXiv 2605.24381 (May 2026) - https://arxiv.org/abs/2605.24381
4. Datadog, "Toto 2.0: Time series forecasting enters the scaling era" (14 May 2026) - https://www.datadoghq.com/blog/ai/toto-2/
5. This Time is Different: An Observability Perspective on TSFMs (Toto/BOOM), arXiv 2505.14766 (May 2025; NeurIPS 2025) - https://arxiv.org/abs/2505.14766
6. AI Horizon Forecast, "Time Series Foundation Models: strengths and limitations" (GIFT-Eval table) (2026) - https://aihorizonforecast.substack.com/p/time-series-foundation-models-a-deep ; Pebblous TimesFM report - https://blog.pebblous.ai/report/timesfm-industrial-forecasting/en/
7. "Against Time-Series Foundation Models" (2026) - https://shakoist.substack.com/p/against-time-series-foundation-models ; calibration study, PMC13460289 (2026)
8. EEG-FM-Benchmark (GitHub, 2026) - https://github.com/Dingkun0817/EEG-FM-Benchmark
9. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-tuning, arXiv 2507.01196 (Jul 2025) - https://arxiv.org/abs/2507.01196
10. EEG Foundation Models: A Critical Review, arXiv 2507.11783 (2025) - https://arxiv.org/html/2507.11783v3
11. Apple, Large-scale Training of Foundation Models for Wearable Biosignals (ICLR 2024; research post Feb 2025) - https://machinelearning.apple.com/research/large-scale-training
12. AnyPPG, arXiv 2511.01747 (Nov 2025) - https://arxiv.org/abs/2511.01747 ; Wavelet-Driven Masked Multiscale Reconstruction for PPG FMs, arXiv 2601.12215 (Jan 2026)
13. Pulse-PPG, Proc. ACM IMWUT (2025) - https://dl.acm.org/doi/10.1145/3749494
14. Google HeAR model card - https://developers.google.com/health-ai-developer-foundations/hear/model-card ; weights https://huggingface.co/google/hear
15. Google blog, HeAR cough disease detection / Salcit Swaasa - https://blog.google/innovation-and-ai/technology/health/ai-model-cough-disease-detection/
16. IQFM: A Wireless Foundational Model for I/Q Streams, arXiv 2506.06718 (Jun 2025) - https://arxiv.org/abs/2506.06718
17. Radio-FM: A Foundation Model for Radio Signal Representation Learning, arXiv 2608.05793 (6 Aug 2026) - https://arxiv.org/abs/2608.05793
18. A Comprehensive Survey of Wireless Foundation Models for AI-Native 6G, arXiv 2608.14694 (Aug 2026) - https://arxiv.org/html/2608.14694 ; SpectrumFM arXiv 2505.06256; EMind arXiv 2508.18785; WavesFM arXiv 2504.14100
19. CSI-JEPA, arXiv 2605.14171 (May 2026) - https://arxiv.org/html/2605.14171v1 ; 802.11bf overview arXiv 2207.04859
20. NVIDIA, "Real-Time Neural Receivers Drive AI-RAN Innovation" (3 Sep 2024) - https://developer.nvidia.com/blog/real-time-neural-receivers-drive-ai-ran-innovation/
21. DeepSig at MWC26 (BusinessWire, 27 Feb 2026) - https://www.businesswire.com/news/home/20260227259448/en/ ; MWC 2025 demo - https://businesswire.com/news/home/20250225210062/en/
22. DeepSig funding (Tracxn/CB Insights, 2026) - https://tracxn.com/d/companies/deepsig/__27oYMu-a6eyvGUCNv-sZu3kSQCgDRGwXfGtmjWNu4LU/funding-and-investors
23. SeisLM: a Foundation Model for Seismic Waveforms, arXiv 2410.15765 (Oct 2024) - https://arxiv.org/abs/2410.15765
24. DAS market: SNS Insider via GlobeNewswire (15 May 2026) - https://www.globenewswire.com/news-release/2026/05/15/3295983/0/en/ ; Persistence MR ($2.8B 2026) - https://www.persistencemarketresearch.com/market-research/distributed-acoustic-sensing-market.asp
25. UMN/MIT, first real-time ML search for BBH (Aframe deployed 28 Aug 2025) - https://cse.umn.edu/mifa/news/umn-and-mit-launch-first-real-time-machine-learning-search-colliding-black-holes ; https://github.com/ML4GW/aframe
26. DINGO-BNS, Nature (5 Mar 2025) via ScienceDaily - https://www.sciencedaily.com/releases/2025/03/250305134808.htm
27. Kyutai Mimi (HF) - https://huggingface.co/kyutai/mimi ; codec explainer - https://kyutai.org/codec-explainer/ ; Forasoft codec survey (Opus remark) - https://www.forasoft.com/learn/audio-for-video/articles-audio/neural-audio-codecs-lyra-encodec-soundstream
28. Spheron, S2S latency comparison (2026) - https://www.spheron.network/blog/speech-to-speech-gpu-cloud-moshi-sesame-csm-hertz-dev/ ; PersonaPlex arXiv 2602.06053 (Feb 2026)
29. Northflank, best open STT 2026 - https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks ; MarkTechPost (23 Jul 2026) - https://www.marktechpost.com/2026/07/23/best-open-speech-recognition-asr-models-in-2026-wer-languages-latency-and-license-compared/
30. SignalLLM, arXiv 2509.17197 (Sep 2025) - https://arxiv.org/abs/2509.17197
31. RadioMaster, arXiv 2606.01862 (Jun 2026) - https://arxiv.org/abs/2606.01862 ; LLM Agents as 6G Orchestrator arXiv 2410.03688; RFAmpDesigner arXiv 2605.10093
32. ResBench arXiv 2503.08823 (Mar 2025); FPGAgent arXiv 2608.23630 (Aug 2026); CorrectHDL arXiv 2511.16395; Benchmarking LLMs for Verilog Design Flows arXiv 2607.22759 (Jul 2026)
33. DDSP Guitar Amp, arXiv 2408.11405 (ICASSP 2025 oral) - https://arxiv.org/abs/2408.11405 ; NablAFx arXiv 2502.11668
34. Learning PDE Solvers with Physics and Data (PINN+NO unifying view), arXiv 2601.14517 (Jan 2026); PINO for sound absorbers arXiv 2604.07412 (Apr 2026)
35. PetaPixel, "World's first full AI-based ISP" (18 Jan 2026) - https://petapixel.com/2026/01/18/a-look-at-the-worlds-first-full-ai-based-image-signal-processor/ ; Neural ISP in the small-pixel era arXiv 2606.07675
36. XPU.pub, Innatera Pulsar (22 Jul 2025) - https://xpu.pub/2025/07/22/innatera-pulsar/
37. Qualcomm to acquire Edge Impulse (10 Mar 2025) - https://www.qualcomm.com/news/releases/2025/03/qualcomm-to-bolster-ai-and-iot-capabilities-with-edge-impulse-ac
38. Ambiq Micro Form 8-K, IPO and Q2 2025 results (Sep 2025) - https://www.sec.gov/Archives/edgar/data/1500412/000095017025113025/ambq-ex99_1.htm
39. Syntiant S-1 (Jul 2026) - https://www.sec.gov/Archives/edgar/data/1718728/000119312526296426/ck0001718728-20260706.htm ; OCBJ "Syntiant eyes $300M IPO"
40. ADI MAX78000 product page - https://www.analog.com/en/products/max78000.html
41. AMD, "Now Shipping: Versal RF Series" (Nov 2025) - https://www.amd.com/en/blogs/2025/now-shipping-versal-rf-series.html ; ServeTheHome, Versal RF at Hot Chips 2026
42. Real Digital RFSoC 4x2 - https://www.realdigital.org/hardware/rfsoc-4x2 ; DigiKey ZCU208 listing
43. GNU Radio 4 RC1 (22 Mar 2026) - https://www.gnuradio.org/news/2026-03-22-gr4-release-candidate-1/ ; GR4 community stewardship (21 May 2026)
44. MathWorks launches MATLAB Copilot (7 Oct 2025) - https://www.mathworks.com/company/newsroom/mathworks-launches-generative-ai-powered-matlab-copilot-to-boost-productivity-and-accelerate-development-for-engineers-scientists-and-researchers.html
45. Quilter, "The Electrical Engineer Shortage Is Structural" (2026) - https://www.quilter.ai/blog/hardware-engineers-shortage-2026
46. Liquid Instruments Series C (2 May 2026) - https://liquidinstruments.com/news-updates/series-c/ ; GenInst Studio (14 Jul 2026) - https://liquidinstruments.com/news-updates/liquid-instruments-puts-first-ai-powered-instrument-creation-in-the-hands-of-every-engineer/
47. Keysight AI-powered assistants for ADS (16 Dec 2025) - https://www.keysight.com/us/en/about/newsroom/news-releases/2025/1216_pr26-017-keysight-accelerates-electronic-design-productivity-with-secure-ai-powered-assistants.html
48. IntuitionLabs, FDA AI medical device list stats (2026) - https://intuitionlabs.ai/articles/fda-ai-medical-device-tracker
49. Butterfly Network, FDA clearance for blind-sweep GA tool (30 Mar 2026) - https://www.businesswire.com/news/home/20260330456365/en/
50. GE AIR Recon DL expanded FDA clearance (Oct 2025) - https://www.diagnosticimaging.com/view/mri-deep-learning-software-from-ge-healthcare-gets-expanded-fda-clearance ; DL MRI halves scan time, Radiology Advances (2025) - https://academic.oup.com/radadv/article/2/5/umaf029/8240289
51. Recursive KalmanNet, arXiv 2506.11639 (Jun 2025) - https://arxiv.org/abs/2506.11639 ; Emergent Mind summary of NN-aided KF incl. automotive radar comparison
52. Perch 2.0 (arXiv 2512.03219); Foundation Models for Bioacoustics comparative review, arXiv 2508.01277 / Ecological Informatics 2026
53. Engentica AI-driven EMI/EMC tool (everythingRF, 2025) - https://www.everythingrf.com/news/details/20708-engentica-introduces-ai-driven-emi-and-emc-troubleshooting-tool-for-pcb-design
54. TEEPTRAK, predictive maintenance ML deployment 2026 - https://teeptrak.com/en/predictive-maintenance-ml-deployment-2026/ ; Augury Machine Health - https://www.augury.com/machine-health/
55. Awesome-Radar-Perception (raw-ADC datasets) - https://github.com/Radar-Camera-Fusion/Awesome-Radar-Perception ; pre-beamforming radar learning arXiv 2604.01921 (Apr 2026); Arbe FAQ/2026 pivot - https://arberobotics.com/faqs/
56. ICASSP 2026 accepted papers (Barcelona, 4-8 May 2026) - https://cmsworkshops.com/ICASSP2026/papers/accepted_papers.php ; Paper Digest highlights
57. IEEE JSTSP Special Issue on Wireless Foundation Models (deadline 15 May 2026) - https://signalprocessingsociety.org/events/ieee-jstsp-special-issue-wireless-foundation-models-ai-native-6g-and-beyond ; Brain Foundation Models survey arXiv 2503.00580 / IEEE SPM
58. OPM-FLUX pipeline (bioRxiv, Apr 2026) - https://www.biorxiv.org/content/10.64898/2026.04.24.720604v1.full ; Quantum Insider on quantum sensing (2 Mar 2026)
59. WV-Net SAR foundation model, arXiv 2406.18765; Capella open SAR dataset on AWS; OSSDD Sentinel-1 ship dataset arXiv 2608.01963
60. SDRstore, best SDR for Raspberry Pi (2026) - https://www.sdrstore.eu/best-sdr-for-raspberry-pi-rtl-sdr-ads-b-ais-satellites-remote-monitoring/ ; Second Talent NumPy vs MATLAB 2026 - https://www.secondtalent.com/resources/numpy-vs-matlab-usage-popularity-and-performance/ ; JAX vs SciPy signal issues https://github.com/jax-ml/jax/issues/31619
61. Patsnap, neuromorphic chip patents surge 401% in 2025 - https://www.patsnap.com/resources/blog/articles/neuromorphic-computing-chip-patents-surge-401-in-2025/
62. AssemblyAI, best open-source STT 2026 - https://www.assemblyai.com/blog/top-open-source-stt-options-for-voice-applications
