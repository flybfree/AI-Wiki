# Summary: 2026-07-15_18-56-46Z_Real_TimeDetectionofChargeJumpsinSuperconductingQu.md
Saved: 2026-07-23 23:44
Source: 2026-07-15_18-56-46Z_Real_TimeDetectionofChargeJumpsinSuperconductingQu.md
Model: None

---

## Summary  
The paper introduces an online, in‑the‑loop detector for charge jumps in superconducting qubits that operates with a latency of only a few microseconds. By employing a dilated causal convolutional neural network (DCCNN) and converting the model to FPGA firmware on the QICK platform, the authors achieve detection performance comparable to the established offline χ² algorithm while eliminating per‑qubit hyperparameter tuning. This real‑time capability transforms charge‑jump detection from a post‑hoc diagnostic into an active control primitive that can respond to radiation‑induced events as they occur. The contribution therefore bridges quantum error mitigation and quantum sensing by providing a low‑latency, scalable detection mechanism.

## Key Contributions  
- [Finding 1] A dilated causal convolutional neural network (DCCNN) is implemented on FPGA with a per‑inference latency of 6.19 µs, enabling real‑time charge‑jump detection in the control loop.  
- [Finding 2] The DCCNN’s detection efficiency matches that of the offline χ² algorithm (0.843 ± 0.022 vs. 0.866 ± 0.020) across a charge range of |Δq| ∈ [0.1, 0.5] e at a matched false‑positive rate.  
- [Finding 3] The solution requires no per‑qubit hyperparameter tuning, making it deployable on the QICK platform without extensive calibration.

## Methodology  
The authors generated synthetic Ramsey tomography scans from qubit templates measured at Fermilab’s NEXUS underground site and fed them into a DCCNN trained to classify charge‑jump events. The trained model was then translated to FPGA firmware using hls4ml with ap_fixed\<16,6⟩ quantization. This approach allowed the network to run directly on the Zynq UltraScale+ RFSoC ZCU216, preserving the low latency and limited resource footprint required for in‑the‑loop operation.

## Results  
Experimental runs demonstrated that the DCCNN achieved a per‑inference latency of 6.19 µs on the ZCU216 while delivering detection efficiencies within 0.022 of the χ² baseline. The false‑positive rate remained comparable, confirming that the online detector performs as well as the traditional offline method without sacrificing speed or accuracy.

## Significance  
By moving charge‑jump detection into the control loop, this work enables adaptive quantum protocols that can mitigate radiation errors in real time and repurpose qubits for particle‑detection sensing. The low latency and hardware‑friendly implementation make it a practical step toward fault‑tolerant quantum computing and advanced quantum instrumentation.

## Related Concepts  
Superconducting qubits, charge jumps, Ramsey tomography, χ² algorithm, convolutional neural network, dilated causal CNN, FPGA inference, hls4ml, QICK platform, radiation‑induced errors, quantum error mitigation, quantum sensing.
