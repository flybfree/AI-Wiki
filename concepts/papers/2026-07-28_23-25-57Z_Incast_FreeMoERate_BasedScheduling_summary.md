# Summary: 2026-07-28_23-25-57Z_Incast_FreeMoERate_BasedScheduling.md
Saved: 2026-07-29 22:17
Source: 2026-07-28_23-25-57Z_Incast_FreeMoERate_BasedScheduling.md
Model: None

---

## Summary  
The paper investigates the hidden performance degradation caused by the conventional round‑robin (RR) scheduler used in MoE architectures and shows that it can trigger an exponential incast problem when many expert subnetworks compete for a single physical link. By introducing a proactive, rate‑based scheduling framework that is explicitly designed to avoid fabric oversubscription, the authors demonstrate that MoE traffic can be routed without incast while preserving high link utilization and lowering collective completion time (CCT). This work bridges a long‑standing bottleneck in large language model deployment with a hardware‑friendly solution.

## Key Contributions  
- [Finding 1] The exponential incast phenomenon is identified as a previously unknown effect of RR scheduling on MoE traffic, where the cumulative load overwhelms the fabric and causes severe throughput loss.  
- [Finding 2] A proactive fair scheduling framework is proposed that dynamically balances expert traffic based on per‑expert request rates, preventing oversubscription and eliminating incast.  
- [Finding 3] The framework is implemented in NIC hardware and validated through extensive simulations showing complete incast removal, near‑100 % link utilization, and a measurable reduction in CCT.

## Methodology  
The authors first model MoE traffic as a set of expert subnetworks sharing a common physical link. They analyze the RR scheduler’s behavior under high concurrency, deriving an exponential growth of incast that scales with the number of experts. Building on this analysis, they design a rate‑based algorithm that assigns packets to the least‑loaded expert while respecting per‑expert request rates, ensuring fair and non‑overlapping routing. The scheduling logic is embedded in a programmable NIC fabric, allowing real‑time enforcement without software latency.

## Results  
Simulations with both synthetic MoE workloads (varying numbers of experts) and real‑world LLM inference traffic confirm that the rate‑based scheduler eliminates incast entirely. Link utilization remains at 98–100 % across all test cases, while CCT is reduced by roughly 30 % compared with RR. The hardware implementation incurs negligible overhead (<2 µs per packet), validating its practicality for high‑throughput MoE inference.

## Significance  
MoE models dominate modern LLMs, yet their deployment on shared fabrics is hampered by incast and suboptimal scheduling. By removing the exponential incast bottleneck and preserving near‑full link utilization, this work enables faster, more reliable LLM serving at scale, directly addressing a critical scalability issue in AI infrastructure.

## Related Concepts  
MoE (Mixture of Experts), round‑robin scheduling, incast, collective completion time (CCT), NIC offloading, rate‑based fairness, fabric oversubscription.
