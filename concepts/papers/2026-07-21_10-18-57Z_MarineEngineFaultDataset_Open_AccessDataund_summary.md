# Summary: 2026-07-21_10-18-57Z_MarineEngineFaultDataset_Open_AccessDataunderContr.md
Saved: 2026-07-24 00:43
Source: 2026-07-21_10-18-57Z_MarineEngineFaultDataset_Open_AccessDataunderContr.md
Model: None

---

## Summary  
The Marine Engine Fault Dataset (MEFD) is an open‑access collection of multi‑sensor time‑series from a turbocharged three‑cylinder marine diesel engine that records both normal reference operation and five deliberately induced fault scenarios. By coupling controlled physical interventions with systematic measurement across the 30–90 % load range, the authors create a benchmark that enables reliable anomaly detection, fault diagnosis, degradation modelling, and condition‑monitoring studies for maritime machinery.

## Key Contributions  
- **Finding 1:** The dataset provides a physically coherent reference record spanning low to high loads, establishing a stable baseline for comparison with fault‑induced anomalies.  
- **Finding 2:** Five distinct fault classes—cooling‑water pump cavitation, compressor air‑filter clogging, air‑cooler fouling, injection‑valve nozzle blockage, and turbine degradation via exhaust restriction—are reproduced with reproducible response patterns that can be linked to subsystem failure.  
- **Finding 3:** The release includes both raw sensor streams and structured metadata, allowing seamless integration into existing machine‑learning pipelines for predictive maintenance without re‑experimentation.

## Methodology  
The authors designed a closed‑loop testbed where the engine is first run under a reference performance program that varies load from 30 % to 90 %. After stabilization, each fault scenario is introduced sequentially: cavitation reduces pump flow, clogging restricts compressor airflow, fouling increases thermal resistance of the air cooler, nozzle blockage limits injection efficiency, and exhaust restriction raises turbine back‑pressure. All interventions are logged with synchronized sensor data (operating torque, coolant temperature, pressure differentials, flow rates, combustion quality indices). The dataset is stored as a single CSV archive with a companion JSON manifest.

## Results  
Reference measurements remain physically consistent across the load spectrum, while fault signatures show progressive degradation: cavitation manifests as rapid pressure spikes and coolant temperature rise; clogging yields gradual torque loss and increased exhaust pressure; fouling produces steady‑state thermal drift; nozzle blockage causes intermittent combustion quality drops; turbine restriction leads to high‑frequency vibration. The dataset includes 12 hours of data per scenario, yielding over 70 GB of time‑series ready for analysis.

## Significance  
MEFD fills a critical gap in marine‑engine predictive‑maintenance literature by offering a controlled, open benchmark that can be directly compared to proprietary datasets. Its systematic fault injection and multi‑load operation enable researchers to evaluate the robustness of anomaly detectors under realistic operating conditions, accelerating the development of condition‑based monitoring systems for ships and offshore platforms.

## Related Concepts  
- Predictive maintenance  
- Fault diagnosis  
- Condition‑monitoring  
- Anomaly detection  
- Multi‑sensor time‑series analysis  
- Open‑access benchmark datasets  
- Turbocharged marine diesel engines
