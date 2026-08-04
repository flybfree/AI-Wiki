# Summary: 2026-08-03_11-07-20Z_AComparativeAnalysisofMLPandKolmogorov_ArnoldNetwo.md
Saved: 2026-08-04 00:46
Source: 2026-08-03_11-07-20Z_AComparativeAnalysisofMLPandKolmogorov_ArnoldNetwo.md
Model: None

---

## Summary  
The paper aims to compare multilayer perceptrons (MLP) and Kolmogorov‑Arnold networks (KAN) for detecting faster‑than‑Nyquist BPSK signals in AWGN. It seeks a data‑driven approach that balances performance with computational efficiency, given the high memory demands of classical detectors like BCJR. The study uses a large Monte Carlo dataset and evaluates hidden layer widths and spline grid sizes to find optimal configurations. Results show KAN attains significantly lower BER with far fewer parameters than MLP.  

## Key Contributions  
- Finding 1: KAN achieves a bit error rate of \(7\times10^{-6}\) at SNR = 10 dB, which is an order of magnitude better than the best MLP ( \(1.3\times10^{-4}\) ).  
- Finding 2: The optimal KAN configuration uses hidden width four and spline grid size five, while the best MLP uses hidden width thirty two, indicating superior parameter efficiency.  
- Finding 3: KAN requires only one‑eighth of the MLP’s hidden width to achieve comparable performance, demonstrating a dramatic reduction in computational load.  

## Methodology  
The authors generate nearly four million labeled FTN BPSK windows with time‑packing factor 0.8 under AWGN for SNR values from 7 to 10 dB. They train both an MLP and a KAN using this dataset, varying hidden layer dimensions (MLP: width 32; KAN: width 4) and spline grid resolution (KAN: size 5). Training is performed with standard back‑propagation for the MLP and gradient‑based optimization of the spline basis functions for the KAN. The decision metric is the bit error rate across the test set.  

## Results  
At SNR = 10 dB, the best MLP yields a BER of \(1.3\times10^{-4}\), whereas the selected KAN achieves \(7\times10^{-6}\), an eighteen‑point‑six‑times improvement. The KAN’s configuration uses only one‑eighth the hidden width of the MLP while delivering superior performance, confirming its parameter efficiency.  

## Significance  
This work provides a practical alternative to classical sequence detectors for FTN signaling, offering high detection accuracy with minimal computational resources. By showing that KAN can outperform MLP in both BER and parameter usage, it supports future low‑power communication systems where latency and energy consumption are critical.  

## Related Concepts  
- Faster‑than‑Nyquist (FTN) signaling  
- Multilayer Perceptron (MLP)  
- Kolmogorov‑Arnold Network (KAN)  
- Bit error rate (BER)  
- AWGN channel  
- BCJR detector
