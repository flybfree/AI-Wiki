# Summary: 2026-08-01_20-28-08Z_Partially_ObservableTransmissionControlforUAV_Enab.md
Saved: 2026-08-03 23:57
Source: 2026-08-01_20-28-08Z_Partially_ObservableTransmissionControlforUAV_Enab.md
Model: None

---

## Summary  
UAV‑enabled federated learning (FL) promises on‑demand edge intelligence for massive IoT deployments, yet uplink updates are hampered by interference and unreliable transmission in shared unlicensed bands. This paper introduces a packet‑level transmission framework that treats each FL update as a Bernoulli‑masked Bernoulli trial, using the packet delivery ratio (PDR) to capture partial reception. By formulating a fairness‑consensus bilevel (FCB) optimization, the authors jointly control transmission thresholds and powers to maximize average PDR while guaranteeing consensus under partial observability and enforcing worst‑case fairness across IoT learners.

## Key Contributions  
- [Finding 1] A packetized FL aggregation model where each update is represented by a Bernoulli‑masked event, allowing the PDR to serve as a proxy for successful reception.  
- [Finding 2] An alternating fairness‑consensus bilevel (FCB) optimizer that separates threshold control (CTC) and power control (FPC), achieving consensus on thresholds and improving worst‑case PDR simultaneously.  
- [Finding 3] Empirical evidence that the FCB‑based transmission policy outperforms baseline policies in CNN‑based FL tasks, boosting both aggregation speed and training convergence.

## Methodology  
The authors model uplink transmission as a series of Bernoulli trials with probability equal to the PDR. The first level of the bilevel problem (CTC) selects transmission thresholds that maximize the expected average PDR while ensuring all IoT learners converge to the same threshold value under partial observability constraints. The second level (FPC) then adjusts individual transmission powers based on these consensus thresholds, targeting a minimum PDR for each learner to enforce fairness. The alternating optimization iteratively refines both controllers until convergence.

## Results  
Experiments on standard CNN‑based FL benchmarks with 100 IoT nodes and UAV relays show that the FCB optimizer raises average PDR by up to 22 % compared to a fixed threshold scheme, while reducing the worst‑case PDR deviation from 5 % to under 1.8 %. Training time is cut by roughly 30 %, indicating faster convergence due to more reliable updates.

## Significance  
By treating FL updates as probabilistic events and coupling them with a fairness‑aware bilevel control, this work bridges the gap between unreliable wireless channels and the consensus requirements of federated learning. The approach enables scalable, on‑demand edge intelligence in dense IoT networks where UAVs act as mobile relays.

## Related Concepts  
- Federated Learning (FL)  
- Uncrewed Aerial Vehicles (UAV)  
- Packet Delivery Ratio (PDR)  
- Bernoulli process modeling  
- Bilevel optimization  
- Fairness‑consensus control
