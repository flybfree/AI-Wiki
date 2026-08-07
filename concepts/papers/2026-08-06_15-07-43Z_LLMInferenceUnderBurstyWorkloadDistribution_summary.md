# Summary: 2026-08-06_15-07-43Z_LLMInferenceUnderBurstyWorkloadDistribution_Modify.md
Saved: 2026-08-06 20:46
Source: 2026-08-06_15-07-43Z_LLMInferenceUnderBurstyWorkloadDistribution_Modify.md
Model: None

---

## Summary  
The paper addresses the challenge of serving large‑language‑model inference requests when arrival patterns are inherently bursty rather than Poissonian, a limitation of existing scheduling algorithms that assume constant request rates. By extending the state‑of‑the‑art WAIT algorithm with an online estimator of request intensity derived from observed interarrival times, the authors propose a lightweight adaptation that requires no prior traffic knowledge. This approach enables higher throughput under low‑rate shift scenarios while preserving acceptable latency compared to competing methods such as Sarathi‑Serve, ORCA, and vLLM.

## Key Contributions  
- [Finding 1] The proposed algorithm dynamically estimates request intensity from interarrival times, removing the need for pre‑defined traffic models.  
- [Finding 2] Simulation results show that the adapted WAIT achieves higher throughput than Sarathi‑Serve, ORCA, and vLLM in low‑arrival‑rate shift conditions while keeping latency comparable to these baselines.  
- [Finding 3] The lightweight modification adds minimal computational overhead, making it suitable for real‑time deployment without sacrificing performance.

## Methodology  
The authors construct Markov Modulated Poisson Process (MMPP) synthetic workloads that emulate diverse request types and bursty arrival patterns typical of production environments. They implement an online estimator that continuously updates the mean interarrival time based on recent observed gaps, feeding this estimate into a modified WAIT scheduler. The scheduler then adjusts its queuing parameters in real time to balance throughput and latency.

## Results  
Experimental simulations across multiple MMPP workloads demonstrate that the adapted WAIT algorithm outperforms Sarathi‑Serve, ORCA, and vLLM in achieving higher request completion rates under low arrival‑rate shift scenarios. Latency metrics remain within a comparable range, indicating that the trade‑off between throughput and response time is well managed.

## Significance  
This work highlights that many modern LLM inference systems are misaligned with real‑world traffic dynamics, where bursts dominate over steady streams. By providing a simple, knowledge‑free adaptation of WAIT, the authors offer a practical solution for operators seeking to improve resource utilization without complex modeling or heavy computational cost.

## Related Concepts  
- **WAIT algorithm**: A state‑of‑the‑art scheduler that balances throughput and latency in LLM inference.  
- **Markov Modulated Poisson Process (MMPP)**: A stochastic model capturing bursty, time‑varying request arrivals.  
- **Throughput vs. Latency trade‑off**: The central performance metric evaluated in the study.  
- **Online estimation**: Real‑time inference of request intensity from interarrival times.
