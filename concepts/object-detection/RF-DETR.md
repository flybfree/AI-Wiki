---
title: "RF-DETR: Real-Time Object Detection Transformer"
type: concept
created: "2026-09-29"
updated: "2026-09-29"
tags: [computer-vision, object-detection, transformers, real-time-inference, roboflow, open-source]
---

# RF-DETR: Real-Time Object Detection Transformer

## Executive Summary

RF-DETR is Roboflow's real-time transformer-based object-detection family. It is designed primarily for **fine-tuning on fixed-label custom datasets**, rather than zero-shot open-vocabulary detection. The architecture uses a DINOv2 vision-transformer backbone and neural architecture search (NAS) to find accuracy/latency trade-offs for detection models. The same `rfdetr` ecosystem also exposes instance-segmentation and preview keypoint models.

The practical case for RF-DETR is strongest when a custom detector needs better accuracy than a small YOLO baseline while retaining real-time inference on an NVIDIA deployment target. The official latency figures are TensorRT/FP16 measurements on an NVIDIA T4 at batch size 1; they should be treated as vendor benchmark conditions, not guaranteed end-to-end application latency.

## What the name means

- **DETR** means *DEtection TRansformer*: a detector that predicts a set of objects using transformer-based set prediction rather than a conventional anchor-grid pipeline.
- **RF-DETR** is Roboflow's real-time DETR family, developed as a lightweight specialist detector for custom-domain fine-tuning.
- **NAS** means *neural architecture search*: the training/search process explores architecture choices to discover useful accuracy-latency points instead of relying only on manually scaled model sizes.

## Model family

The official detection table currently reports the following models:

| Model | Parameters | Resolution | COCO AP50:95 | RF100-VL AP50:95 | T4 latency | License |
|---|---:|---:|---:|---:|---:|---|
| RF-DETR-N | 30.5M | 384×384 | 48.4 | 57.7 | 2.3 ms | Apache 2.0 |
| RF-DETR-S | 32.1M | 512×512 | 53.0 | 60.2 | 3.5 ms | Apache 2.0 |
| RF-DETR-M | 33.7M | 576×576 | 54.7 | 61.2 | 4.4 ms | Apache 2.0 |
| RF-DETR-L | 33.9M | 704×704 | 56.5 | 62.2 | 6.8 ms | Apache 2.0 |
| RF-DETR-XL | 126.4M | 700×700 | 58.6 | 62.9 | 11.5 ms | PML 1.0 |
| RF-DETR-2XL | 126.9M | 880×880 | 60.1 | 63.2 | 17.2 ms | PML 1.0 |

Roboflow reports that the COCO measurements were evaluated on the full `val2017` split and that the latency measurements used an NVIDIA T4, TensorRT, FP16, and batch size 1. The figures are therefore useful for comparing the published family under one protocol, but not for predicting PyTorch, CPU, Apple Silicon, or application-level latency.

## Architecture and training approach

RF-DETR's research contribution is a weight-sharing NAS approach that searches architecture choices and produces accuracy-latency Pareto curves for a target dataset. The paper positions this as an alternative to fine-tuning a large vision-language model when the task is a fixed-label detection problem.

The public package is built around a DINOv2 vision-transformer backbone and a detection-transformer design. DETR-style set prediction can avoid the traditional dependence on a separate non-maximum-suppression stage, although the complete deployment pipeline still includes preprocessing, model execution, decoding, and application-specific filtering.

The important distinction is task scope:

- **RF-DETR:** supervised, closed-vocabulary detection after fine-tuning.
- **GroundingDINO / YOLO-World-style systems:** better suited to text-conditioned or open-vocabulary discovery.
- **YOLO and RT-DETR:** direct practical baselines for the same fixed-label detection problem.

## Fine-tuning and dataset support

RF-DETR supports custom object-detection and segmentation training through the Python package or Roboflow's cloud workflow. The documentation supports COCO-style and YOLO-style dataset layouts, validation/evaluation, checkpoint loading, and training controls such as early stopping, multi-GPU DDP, gradient checkpointing, and memory optimization.

Minimal example:

```python
from rfdetr import RFDETRMedium

model = RFDETRMedium()
model.train(
    dataset_dir="path/to/dataset",
    epochs=100,
    batch_size=4,
    output_dir="output/rfdetr-medium",
)
```

The exact image resolution must satisfy the selected checkpoint's architectural block-size constraints. Resolution and batch size are the main practical controls for training memory. The official documentation recommends a CUDA-capable GPU for normal fine-tuning; low-memory systems may require a smaller model, smaller batch, gradient accumulation, or checkpointing.

## Deployment formats

The package documents export and deployment paths for:

- ONNX
- TensorRT
- TFLite and LiteRT
- OpenVINO
- ExecuTorch, including mobile backends
- Native CoreML

Install the corresponding package extra before export, for example `rfdetr[tensorrt]` or `rfdetr[onnx]`. TensorRT export builds from ONNX and is the most relevant path for NVIDIA production inference.

## Licensing and openness

The core `rfdetr` package and RF-DETR-N/S/M/L models are Apache 2.0 according to the project documentation and package metadata. RF-DETR-XL and RF-DETR-2XL are distributed through the Plus components under Roboflow's Platform Model License 1.0.

This is not one uniform license across the entire family. For commercial redistribution or a permissive local deployment, review the exact checkpoint and dependency license before selecting an XL/2XL model. The Apache designation applies to the core package and the explicitly Apache-licensed model variants; it does not automatically extend to every Roboflow Plus component.

## Comparison with practical alternatives

| System | Best fit | Main trade-off |
|---|---|---|
| RF-DETR | Custom fixed-label detection where accuracy and latency both matter | Transformer deployment and TensorRT assumptions need validation |
| YOLO family | Broad tooling, fast iteration, edge deployment, mature ecosystem | License and post-processing vary by implementation; accuracy depends heavily on variant and dataset |
| RT-DETR | Open end-to-end DETR baseline for real-time detection | Usually requires its own deployment and training stack; results depend on version and backend |
| GroundingDINO | Text-conditioned/open-vocabulary detection | More expensive and generally not the first choice for high-throughput fixed-label inference |
| YOLO-World-style models | Promptable/open-vocabulary workflows | Open-vocabulary flexibility can trade off against specialist fixed-label accuracy and latency |

RF-DETR should be compared against a matched YOLO and/or RT-DETR baseline on the user's own data. COCO AP alone does not decide the deployment winner.

## Practical recommendation

For a first evaluation, train and benchmark:

1. RF-DETR-S
2. RF-DETR-M
3. RF-DETR-L
4. A comparable YOLO baseline
5. RT-DETR if an end-to-end transformer baseline is useful

Record at minimum:

- mAP50 and mAP50:95
- per-class precision and recall
- small/medium/large-object performance
- false positives and missed detections on real production scenes
- preprocessing, inference, decode, and end-to-end latency separately
- GPU memory and sustained throughput
- performance under the exact export/runtime path

For an NVIDIA GPU, RF-DETR-M is the sensible default starting point; RF-DETR-S is the safer latency/throughput baseline; RF-DETR-L is the accuracy-first Apache-licensed option. There is no local benchmark result yet in this wiki for the user's hardware, so these should remain candidates until tested against the actual camera workload.

## Limitations and open questions

- The headline latency numbers are vendor-reported T4/TensorRT/FP16/batch-1 measurements.
- CPU and Apple Silicon performance should not be inferred from the T4 table.
- The model is not a zero-shot detector; custom classes require supervised training.
- Dataset quality, label consistency, object scale, occlusion, and domain shift may dominate differences between detector families.
- The published model table separates Apache-licensed standard models from PML-licensed Plus models.
- The current wiki does not contain a local RF-DETR accuracy, VRAM, or end-to-end throughput benchmark.

## Sources

- [RF-DETR source repository](https://github.com/roboflow/rf-detr)
- [RF-DETR paper — Neural Architecture Search for Real-Time Detection Transformers](https://arxiv.org/abs/2511.09554)
- [ICLR 2026 OpenReview entry](https://openreview.net/forum?id=qHm5GePxTh)
- [RF-DETR training documentation](https://github.com/roboflow/rf-detr/blob/develop/docs/learn/train/index.md)
- [RF-DETR FAQ and export formats](https://github.com/roboflow/rf-detr/blob/develop/docs/faq.md)
- [RF-DETR package metadata and Apache license](https://github.com/roboflow/rf-detr/blob/develop/pyproject.toml)
- [Roboflow100-VL benchmark paper](https://media.roboflow.com/rf100vl/rf100vl.pdf)

## Revision history

- 2026-09-29 — Created from the RF-DETR repository, documentation, benchmark tables, package metadata, and ICLR 2026 paper materials.
