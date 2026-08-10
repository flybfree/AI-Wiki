# Summary: 2026-08-07_17-28-33Z_RIS_AidedmmWaveLocalizationUnderCross_LinkInterfer.md
Saved: 2026-08-09 23:17
Source: 2026-08-07_17-28-33Z_RIS_AidedmmWaveLocalizationUnderCross_LinkInterfer.md
Model: None

---

## Summary  
The paper tackles the challenge of user equipment (UE) localization in reconfigurable intelligent surface (RIS)-assisted millimeter‑wave networks when direct base‑station links are unavailable, especially under cross‑link interference. It introduces a beam‑domain fingerprint framework that maps received signal‑to‑noise ratios across predefined RIS reflection states to UE azimuth and range without requiring channel state information, and it extends this approach to realistic SINR fingerprints with an interference‑limited calibration strategy. The study evaluates four machine‑learning regressors under both clean and interference conditions, demonstrating the framework’s robustness.

## Key Contributions  
- [Finding 1] A beam‑domain fingerprint can localize UE using only SNR measurements across a small set of RIS reflection states, eliminating the need for CSI.  
- [Finding 2] The framework is extended to cross‑link interference scenarios by forming an SINR fingerprint and applying an interference‑to‑noise ratio (INR)‑constrained calibration that preserves physical interpretability.  
- [Finding 3] K‑nearest neighbors (KNN) achieves the lowest angle MAE of 0.37° and range MAE of 4 cm under clean conditions, while still performing reasonably under interference; however, angle estimation degrades more than range due to asymmetric encoding.

## Methodology  
The authors define a set of RIS reflection states that produce distinct SNR patterns for different UE locations. These SNRs are used as features to train offline ML regressors (including KNN) that predict azimuth and range. For the interference case, the received SINR is combined with an INR‑constrained calibration to generate a physical fingerprint. The system simulates 28 GHz operation on a 20×20 RIS array, generating training data for both clean and interference scenarios before evaluating four regressors.

## Results  
Under clean conditions, KNN yields angle MAE = 0.37° and range MAE = 4 cm, outperforming other models (MAE ≈ 1–2°). When a cross‑link interferer is present, the same model’s MAEs rise to angle MAE = 1.4° and range MAE = 7.6 cm; alternative regressors suffer larger degradation. The simulation confirms that interference disproportionately impacts azimuth estimation because location information is encoded asymmetrically in the beam‑domain fingerprint.

## Significance  
This work provides a CSI‑free, robust localization solution for 6G RIS networks where direct links are scarce and cross‑link interference is common. By leveraging only SNR measurements and an INR‑aware calibration, it reduces hardware complexity and improves reliability, which is critical for seamless user experience in dense urban environments.

## Related Concepts  
- Reconfigurable Intelligent Surface (RIS)  
- Millimeter‑wave (mmWave) communications  
- Beam‑domain fingerprinting  
- Machine learning regression (KNN)  
- Signal‑to‑noise ratio (SNR), signal‑to‑interference‑plus‑noise ratio (SINR), interference‑to‑noise ratio (INR)  
- Angular and range estimation error metrics (MAE)
