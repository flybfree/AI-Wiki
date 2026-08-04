# Summary: 2026-08-03_11-07-20Z_AComparativeAnalysisofMLPandKolmogorov_ArnoldNetwo.md
Saved: 2026-08-03 23:53
Source: 2026-08-03_11-07-20Z_AComparativeAnalysisofMLPandKolmogorov_ArnoldNetwo.md
Model: None

---

## Summary  
The paper seeks to compare multilayer perceptrons (MLPs) and Kolmogorov‑Arnold networks (KANs) for detecting faster‑than‑Nyquist BPSK signals in an additive white Gaussian noise (AWGN) channel, emphasizing both performance and computational efficiency. It creates a large Monte Carlo dataset of nearly four million labeled windows using a time‑packing factor of 0.8 and signal‑to‑noise ratios ranging from seven to ten decibels. The study shows that KANs can achieve markedly lower bit error rates than MLPs while consuming far fewer parameters, indicating superior parameter efficiency for this detection task.

## Key Contributions  
- [Finding 1] KANs outperform MLPs in BER for FTN BPSK detection under AWGN.  
- [Finding 2] The best‑performing KAN uses a hidden width of four with a spline grid size five, whereas the top MLP employs a hidden width of thirty two.  
- [Finding 3] The KAN’s bit error rate at ten dB is approximately one‑eighth that of the MLP (7 × 10⁻⁶ vs. 1.3 × 10⁻⁴), representing an improvement of about eighteen point six times lower BER.

## Methodology  
The authors generate a synthetic dataset by simulating FTN BPSK channels with inter‑symbol interference, labeling each window as correct or incorrect based on detector output. They train both MLP and KAN models using this data, varying the hidden layer width (32 for MLP) and spline grid dimensions (4 × 5 for KAN). Width sweeping is performed to identify the configurations that yield the lowest BER while keeping parameter counts low.

## Results  
At a signal‑to‑noise ratio of ten decibels, the selected MLP attains a bit error rate of 1.3 × 10⁻⁴, whereas the KAN reaches 7 × 10⁻⁶. This corresponds to an eighteen point six times lower BER and uses only one eighth of the hidden width required by the MLP.

## Significance  
These findings demonstrate that data‑driven neural networks can be both more accurate and far more parameter‑efficient for FTN signaling detection, offering a practical advantage for real‑time high‑speed communication systems where latency and resource constraints are critical. The results suggest that KANs may replace traditional MLPs in such applications without sacrificing performance.

## Related Concepts  
Faster‑than‑Nyquist signaling, inter‑symbol interference, BPSK modulation, AWGN channel, BCJR detector, multilayer perceptron (MLP), Kolmogorov‑Arnold network (KAN), Monte Carlo simulation, bit error rate (BER).
