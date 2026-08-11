---
title: H3-metal – Native MiniMax-H3 inference for Apple Silicon
date: 2026-08-11
url: https://github.com/antirez/h3.c
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://github.com/antirez/h3.c
source_feed: Hacker News
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-08-11 00:04
---

# H3-metal – Native MiniMax-H3 inference for Apple Silicon

## Full Article

h3-metal
Native MiniMax-H3 inference for Apple Silicon. The project is being built as a
sequence of working vertical slices: deterministic host/model metadata first,
then portable Metal block parity, prompt encoding, prompt-to-video/audio, and
first/last-frame conditioning and then ordered references.
Prompt-to-video/audio, first/last-frame conditioning, and ordered Ref2VA
image/video/audio references work end to end. The current work is incremental
H3-specific Metal performance and memory optimization on M3 Max and M5 Max.
Tutorial
1. Build and inspect the model
The examples assume that the Hugging Face snapshot is in
./MiniMax-H3
and
that FFmpeg and FFprobe are available on
PATH
.
make -j8
mkdir -p outputs
./h3 --info -d ./MiniMax-H3
--info
checks the model layout and prints the selected Metal device without
mapping all weights or generating media. Run
./h3 --help
for the complete CLI
reference.
Without
-p
, the same binary starts an Iris-style interactive session:
./h3 -d ./MiniMax-H3 --width 512 --height 512 --steps 6
Type a prompt to generate a numbered video. The session keeps the exact BF16
prompt conditioning, prepared DiT, and video decoder in memory, so repeating a
prompt with another seed avoids loading and encoding them again. Useful commands
are
!status
,
!seed random
,
!seconds 2
,
!show
,
!save output.mp4
, and
!cache
. Use
!help
for the full, short list.
First/last-frame conditioning is persistent in the session:
h3> !first opening.png
h3> !last ending.png
h3> The camera moves slowly around the subject.
Use
!first clear
or
!last clear
to remove an anchor. Generated videos are
written to the session directory printed at startup.
For a general Ref2VA conditioning image, use
!ref-image PATH
instead. Images
are appended in order and exposed to the model as
<Picture 1>
,
<Picture 2>
,
and so on; filenames have no meaning to the model.
h3> !ref-image person.png
h3> Make the person shown in Picture 1 wave to the camera.
!refs
lists the current order,
!ref-remove N
removes one entry, and
!refs clear
removes them all. Ref2VA references cannot be mixed with
!first
/
!last
anchors.
2. Make a first fast video
Start with the validated balanced preset. It generates 22 frames at 24 fps
(about 0.92 seconds), displays the evolving middle-video frame after every
denoising transition in a supported graphical terminal, and prints phase
timings:
./h3 --profile \
  -d ./MiniMax-H3 \
  -p
"
A red fox walks through fresh snow in a pine forest. Medium tracking shot, natural winter light, realistic fur, soft footsteps and wind.
"
\
  --width 512 --height 512 \
  --frames 22 --steps 20 \
  --layers 45 --reuse 2 \
  --show \
  -o outputs/fox-fast.mp4
This is deliberately not the most aggressive configuration:
--steps 20
performs the default 20 denoising passes.
--reuse 2
computes 11 fresh denoiser velocities instead of all 20 and
extrapolates the skipped transitions.
--layers 45
runs 45 of the 50 transformer blocks, reducing both time and
unified-memory use.
--show
is optional. It supports Kitty/Ghostty and
iTerm2/WezTerm/Konsole graphical protocols. It loads a resident preview VAE,
displays one representative middle-video frame after every Euler transition,
and then displays all final frames. Display dimensions default to 2x so the
image has its intended logical size on macOS Retina screens; use
--zoom 1
on a non-HiDPI display. This adds preview decode time and roughly 10 GiB of
temporary model residency; runs without
--show
are unchanged.
--profile
is optional and does not select a different generation path.
The first process invocation also pays model loading and filesystem-cache
costs. Compare performance using repeated runs, and alternate variants when
the machines are warming up because this workload is sensitive to thermal
throttling.
For a very short iteration, request four denoising passes directly:
./h3 --profile \
  -d ./MiniMax-H3 \
  -p
"
A red fox walks through fresh snow in a pine forest. Medium tracking shot, natural winter light, realistic fur.
"
\
  --width 512 --height 512 --frames 22 \
  --steps 4 --layers 50 --reuse 1 \
  --show \
  -o outputs/fox-four-step.mp4
--steps N
always means exactly N denoising passes. Four through seven passes
use the same schedule that won the low-budget comparison; increasing from 4
to 7 progressively improves detail and motion. Keep
--reuse 1
at such small
budgets so every requested pass runs the model.
--show
displays one preview
after each pass.
Several tail-heavy schedules were evaluated because most visible cleanup
happens late in a long run. They preserved too few early composition updates
and produced woven texture, weak motion, or clipped colors. The retained mode
uses the released linear base grid with one terminal point. On the 512-square,
22-frame fox test, the selected four-pass result had 0.556 full-video SSIM
against a 29-pass reference; an independent surfer test measured 0.547. The
four-pass denoise took about 3.5 seconds on M5 Max, versus 26.4 seconds for the
reference.
3. Move toward reference quality
Change one control at a time when evaluating quality. First restore all layers,
then all denoiser evaluations, and finally raise the default 20-pass schedule
to the slower 50-pass reference:
./h3 --profile \
  -d ./MiniMax-H3 \
  -p
"
A red fox walks through fresh snow in a pine forest. Medium tracking shot, natural winter light, realistic fur, soft footsteps and wind.
"
\
  --width 512 --height 512 \
  --frames 22 --steps 50 \
  --layers 50 --reuse 1 \
  -o outputs/fox-close.mp4
The defaults are
--steps 20 --layers 50 --reuse 1
; keep
--steps 50
explicit for this close path. It performs 50 complete 50-block denoiser
forwards and is much more expensive than the default, but is the right oracle
when a fast mode changes the subject, anatomy, motion, or composition.
Numerical pixel identity with MLX is not expected because the random-number and
execution engines differ; the depicted content and motion should agree.
4. Choose a speed/quality preset
These controls are independent unless noted otherwise:
Control
Slow reference
Default
Aggressive
Main impact
Denoising passes
--steps 50
--steps 20
--steps 4..7
The number always names actual denoising passes.
Whole denoiser reuse
--reuse 1
--reuse 2
--reuse 3
At 20 steps: 20, 11, or 8 fresh DiT evaluations.
Active DiT blocks
--layers 50
--layers 45
--layers 40
Fewer blocks reduce compute and resident transformer weights.
Core residual reuse
--core-reuse 1
--core-reuse 4
--core-reuse 6
Refreshes patch/head work every step but runs the expensive core less often.
Token reduction
off
optional
--token-reduction
Pairs horizontal video tokens inside middle blocks; faster but may change composition.
Internal canvas
output size
384x384
for 512 square output
320x320
Runs DiT/VAE smaller, then upscales with vImage.
On M5,
--use-int8-row-fc2
uses one activation scale per FC2 row and a single
full-width TensorOps product. It is optional because it is less numerically
conservative than grouped int8. It reduced complete denoiser forwards by about
2.6% in reciprocal tests. Matched four-step fox and surfer videos kept the same
subjects, setting, and motion (full-video SSIM 0.919 and 0.828). In the
interactive session, use
!int8-row-fc2 on
.
--reuse
and
--core-reuse
are mutually exclusive. Layer thinning can be
combined with either one.
To make the first command faster while keeping its output resolution, add
token reduction:
./h3 --profile \
  -d ./MiniMax-H3 \
  -p
"
A surfer riding inside a sharp blue ocean wave, one rider and one white board, realistic spray.
"
\
  --width 512 --height 512 --frames 22 --steps 20 \
  --layers 45 --reuse 2 --token-reduction \
  -o outputs/surfer-fast.mp4
At the validated 512 square shape, token reduction cut the
45 layers + reuse 2
denoise profile from 16.69 to 12.60 seconds on the IT M5 Max. Independent
fox and surfer renders stayed coherent, but composition can diverge more from
the close path.
For an aggressive preview, render internally at 320 square and upscale to the
requested 512 square output:
./h3 --profile \
  -d ./MiniMax-H3 \
  -p
"
A red fox walking through snow, realistic, tracking shot.
"
\
  --width 512 --height 512 \
  --render-width 320 --render-height 320 \
  --frames 22 --steps 20 --layers 40 --reuse 3 \
  -o outputs/fox-aggressive.mp4
This combination produced a clean, recognizable 22-frame fox in validation,
but loses fine detail and can change framing. Do
not
add
--token-reduction
to both
--layers 40
and
--reuse 3
: that tested combination produced color
ringing, outlines, and ghosted limbs.
As an alternative to whole-velocity reuse, this keeps the timestep-dependent
patch and output heads fresh at every transition:
./h3 --profile \
  -d ./MiniMax-H3 \
  -p
"
A surfer riding a blue ocean wave.
"
\
  --width 512 --height 512 --frames 22 --steps 20 \
  --layers 45 --core-reuse 4 \
  -o outputs/surfer-core-reuse.mp4
Use
--core-reuse 6
only as an aggressive preview. Values above 6 are not
exposed because validation lost subject fidelity.
5. Pick resolution and duration
Width and height must each be multiples of 32, at least 32, and their product
must not exceed
768 * 1344
pixels. Those are mechanical limits, not a promise
that every tiny canvas has good model quality. H3-Base is a 768p model.
Canvas
Current guidance
512x512
Safest development size; repeatedly validated with multiple prompts.
768x768
Validated close-quality square output; substantially more expensive.
1344x768
,
768x1344
Released 768p-class landscape/portrait limit.
1024x768
,
768x1024
Valid 4:3 and 3:4 768p-class canvases.
384x384
internal to
512x512
Validated fast-quality scaling point.
320x320
internal to
512x512
Validated aggressive scaling point.
256x256
Native fast-preview canvas with automatic low-resolution RoPE adaptation.
For a fast native 256-square preview:
./h3 -d ./MiniMax-H3 \
  -p
"
A red fox walks through fresh snow in a pine forest.
"
\
  --width 256 --height 256 \
  --frames 22 --steps 20 \
  --layers 50 --reuse 1 \
  -o outputs/fox-256.mp4
At 256 square, H3 has only an
8x8
effective spatial-token grid, so it has less
room for fine detail and complex composition. H3 automatically halves spatial
RoPE coordinates at exactly 256 square. This removed repeating lattice
artifacts in long fox renders and stayed coherent on an independent portrait,
without adding tokens or runtime. Use
--use-reference-rope
to restore the
released/MLX coordinates for parity checks. Keep token reduction off at this
size. Native 128 square remains unsupported: its
4x4
token grid did not
recover a recognizable subject even with adjusted RoPE.
--render-width
and
--render-height
must be set together, must have the same
aspect ratio as the output, and cannot exceed the output dimensions. The model
and VAE use the internal size; terminal frames and the encoded video retain the
requested output size.
H3 emits 24 fps and aligns frame requests upward to
5 + 17*n
:
Use
--seconds N
for a duration-oriented request, or
--frames N
for direct
frame control; the two options are mutually exclusive. Fractional seconds are
accepted. Seconds are converted at 24 fps and then rounded upward to the next
legal H3 temporal shape, so
--seconds 10
produces 243 frames (10.125 seconds).
Frames
Approximate video duration
22
0.917 seconds
39
1.625 seconds
56
2.333 seconds
107
4.458 seconds
243
10.125 seconds
362
15.083 seconds
Short clips are useful for development. The released workflow is intended for
roughly 4–15 second videos. A request such as
--frames 23
is rounded up to 39
frames rather than producing an arbitrary temporal shape.
6. Improve the prompt
A short prompt works, but the released system expects a Context-IR-like
description. State the subject, action, setting, camera, lighting/style, and
desired sound. For example:
Scene: a single red fox in a snow-covered pine forest at dawn.
Action: the fox walks steadily left to right and looks toward the camera once.
Camera: medium-height lateral tracking shot, 50 mm lens, stable framing.
Look: photorealistic fur, cold blue ambient light, warm sunrise rim light.
Audio: soft footsteps in snow, light wind through pine branches, no music.
Keep identity and object counts explicit when they matter.
--seed N
controls
the native random stream; the default is 42. Compare options with the same
prompt, seed, resolution, frame count, and step count.
7. Preview frames and diagnose performance
--show
displays a representative frame after every denoising transition,
followed by all frames from the completed video. Like Iris, it advertises 2x
display dimensions by default for Retina terminals;
--zoom N
changes that
factor without resizing the generated video or the encoded terminal image.
--frames-dir DIR
writes final callback frames as PPM files. Intermediate
--show
previews are not written there.
-o ''
disables MP4 encoding; combine it with
--frames-dir
when FFmpeg is
unavailable.
--profile
reports phase wall time, Metal encoding/wait time, peak live
tensor storage, cumulative allocation, and dispatch counts.
For example:
./h3 --profile -d ./MiniMax-H3 -p
"
A hummingbird hovering over red flowers.
"
\
  --width 512 --height 512 --frames 22 --steps 20 \
  --layers 45 --reuse 2 --frames-dir outputs/hummingbird-frames \
  -o
'
'
8. Add image, video, and audio references
First/last-frame anchors select the FL2VA path:
./h3 -d ./MiniMax-H3 -p
"
The fox keeps walking through the snow.
"
\
  --width 512 --height 512 --frames 22 --steps 20 \
  --layers 45 --reuse 2 \
  --first-frame fox.png --last-frame fox-later.png \
  -o outputs/fox-anchored.mp4
Ordered references select the distinct Ref2VA checkpoint. Use the flag matching
the media semantics:
#
One image reference.
./h3 -d ./MiniMax-H3 -p
"
Use the animal and setting in the reference.
"
\
  --width 512 --height 512 --frames 22 --steps 20 \
  --ref-image fox.png -o outputs/fox-reference.mp4
#
Continue a clip but ignore its soundtrack.
./h3 -d ./MiniMax-H3 -p
"
Continue the motion in this clip.
"
\
  --width 512 --height 512 --frames 22 --steps 20 \
  --ref-silent-video fox.mp4 -o outputs/fox-video-reference.mp4
#
Preserve the clip's embedded audio.
./h3 -d ./MiniMax-H3 -p
"
Continue this audiovisual scene.
"
\
  --width 512 --height 512 --frames 56 --steps 20 \
  --ref-video fox-with-audio.mp4 -o outputs/fox-video-audio.mp4
#
Replace a video's soundtrack explicitly.
./h3 -d ./MiniMax-H3 -p
"
Continue the scene with the supplied music.
"
\
  --width 512 --height 512 --frames 56 --steps 20 \
  --ref-video-audio silent-fox.mp4 replacement.wav \
  -o outputs/fox-replaced-audio.mp4
#
An ordered image plus standalone audio reference.
./h3 -d ./MiniMax-H3 -p
"
Use the animal and music from the references.
"
\
  --width 512 --height 512 --frames 56 --steps 20 \
  --ref-image fox.png --ref-audio music.wav \
  -o outputs/fox-image-audio.mp4
Reference flags may be repeated and their command-line order is preserved.
Standalone audio must accompany an image or video reference. Audio references
must be 2–15 seconds; at most three audio inputs are accepted and their total
decoded duration is capped at 15 seconds.
Tests and runtime requirements
make
test
make parity
make test
runs the deterministic host suite and, when the ignored MLX fixture
is installed under
misc/fixtures/
, compiles the Metal source at runtime and
checks a complete toy H3 block against named MLX outputs. Runtime compilation is
intentional: it follows Iris and does not require Xcode's optional offline Metal
toolchain. The test covers both an F32 diagnosis path and the production BF16
storage path; wide BF16 matrix products and SDPA use cached MPSGraph graphs, with
direct Metal correctness fallbacks.
make parity
runs only those Metal/MLX
checks.
FFmpeg and FFprobe must be available on
PATH
for media inputs and MP4 output
(
H3_FFMPEG
and
H3_FFPROBE
may select explicit executables). Generated RGB24 and
32 kHz stereo F32 PCM are fed through concurrent pipes; no intermediate
uncompressed media file is created.
Implementation and performance notes
The remainder documents the implementation behind the tutorial presets and the
environment variables retained for exact A/B diagnosis.
Sampler and DiT controls
The default sampler uses the released shifted video/audio schedule.
--steps
always names the number of denoising passes, with terminal zero added after the
last pass. Whole-denoiser reuse evaluates the first and last pass plus every
requested interval, then extrapolates skipped video and audio velocities on
their independent schedules. With very small step counts, keep
--reuse 1
.
For the low-budget path, the released linear base grid won against
actual-video-sigma linear spacing,
quadratic and cubic warps, exact 30-point tail subsets, mild power warps,
zero-order held full-grid velocities, linear velocity extrapolation, and RES.
The more tail-heavy candidates often sharpened the subject but damaged motion
or left a repetitive woven background; sparse RES and long extrapolation
intervals failed much more visibly.
Layer thinning ranks the checkpoint's actual AdaLN gates while protecting
structurally important first and final blocks. Unused weights and schedule
tensors are not retained, so
--layers 45
and
--layers 40
reduce both
transformer time and unified-memory use. Core reuse holds the previous full
transformer residual while refreshing the patch projection and timestep-aware
head; it remains mutually exclusive with whole-velocity reuse.
Exact DiT fusions
Every active DiT block fuses its attention residual gate with the following MLP
AdaLN. The rounded BF16 residual is still written exactly, but the same row is
kept in threadgroup memory for normalization, eliminating one dispatch and one
global reread. Away from token-reduction boundaries, the MLP residual gate also
produces the next block's attention AdaLN and carries that normalized state
across the loop.
H3_DISABLE_FUSED_GATE_ADALN=1
and
H3_DISABLE_FUSED_CROSS_BLOCK_ADALN=1
restore the two-kernel oracles.
The final audio/video AdaLN kernels bind directly to offsets in the residual
stream, avoiding two slice blits and 18.8 MiB of scratch at 512x512 (29.4 MiB
at the 864-class benchmark shape).
H3_DISABLE_FUSED_FINAL_SLICE=1
restores the copy-plus-AdaLN oracle at load.
The BF16 final heads then apply AdaLN while loading their 16x16 projection
tiles, preserving the standalone rounding and accumulation order while
removing another equally sized normalized activation. The two optimizations
together save 37.5/58.9 MiB.
H3_DISABLE_FUSED_FINAL_HEAD=1
restores the
offset-AdaLN-plus-linear oracle at load.
Token-reduction internals
--token-reduction
is an independent aggressive DiT mode. After block 3 it
pairs adjacent horizontal target-video tokens while leaving text, audio,
conditions, and reference tokens exact. The complete full-resolution state is
kept as a bypass. During the first ten noisy evaluations it restores before
block 40; subsequent detail-forming evaluations restore before block 30. Each
token returns as its original value plus the update learned by its pair, so
within-pair detail is not discarded.
The pooling kernel writes only true-pair baselines into a dense tail of the
already allocated attention scratch buffer; odd-width singleton tokens need no
baseline. The full bypass uses the oversized QKV tail when it fits, with a
guarded dedicated fallback only for reference-heavy layouts. Common text-only
canvases therefore add no activation arena at any token-grid width. Pooling
also snapshots both source tokens while their BF16 values are already in
registers, avoiding a separate full-hidden blit and redundant source read. The
same entry kernel keeps each pooled row in threadgroup memory and emits the
first reduced block's attention AdaLN, eliminating another global residual read.
At the restore boundary, the first full-resolution attention AdaLN is fused
into expansion: a 10.5 KiB threadgroup row avoids a global residual reread while
still writing the exact bypass needed by the following residual branch.
On a thermal-balanced 512x512x22, 19-forward IT M5 Max A/B this reduced denoise
time from 39.13 to 28.06 seconds (28.3%). Final video/audio latent relative L2
was 5.56%/15.14%. First/middle/last fox frames retained one clean muzzle,
coherent legs, and sharp fur; an independent surfer remained consistent with
one rider and board through the wave spray. It changes composition and is
therefore opt-in rather than the close-reference default.
H3_TOKEN_REDUCTION_BLOCKS
can override the later
4:30
interval;
H3_TOKEN_REDUCTION_EARLY=STEPS:END
overrides the early schedule and
0
disables it.
H3_DISABLE_TOKEN_REDUCTION=1
provides an in-context exact oracle.
H3_DISABLE_FUSED_TOKEN_POOL_ADALN=1
and
H3_DISABLE_FUSED_TOKEN_ADALN=1
independently restore the two-kernel entry and
exit boundaries for diagnosis.
Token reduction composes cleanly with the validated
--layers 45 --reuse 2
settings: on the same 512 benchmark it reduced that profile from 16.69 to
12.60 seconds (24.5% marginal), and independent fox and surfer renders stayed
coherent. Do not combine it with both
--layers 40
and
--reuse 3
; that
6.47-second experiment produced chromatic ringing and ghosted limbs despite
acceptable latent norms.
Internal canvas and video VAE
--render-width
and
--render-height
run the model and VAE on a lower
same-aspect internal canvas, then high-quality vImage-scale RGB frames to the
requested output size before callbacks, terminal display, and encoding. This is an
explicit quality/speed tradeoff: a measured 384-to-512 prompt render reduced
M5 DiT time by 33% and video-VAE time by 18% while retaining a clean,
recognizable photorealistic result. Both values must be multiples of 32; the
exact output canvas remains the default.
For square 512 output, 384 is the fast-quality point and 320 is the validated
aggressive point. The latter produced a coherent walking fox and repeated at
8.02 seconds of DiT versus about 15.82 seconds natively. Native 256 uses the
same-cost spatial-RoPE adaptation described above; it remains a fast composition
preview rather than a substitute for a 512- or 768-class final render.
The video VAE automatically chooses a 256-320 pixel spatial tile from the
requested canvas geometry, minimizing repeated overlap work while keeping peak
storage bounded.
H3_VAE_TILE_PIXELS=256
restores the original conservative
tile plan for close-reference diagnosis.
Weight residency and streamed prompt encoding
On M5-class GPUs, persistent transformer weights are mapped directly from their
safetensor shards instead of copied into anonymous shared buffers. This keeps
the 37 GiB model file-backed/reclaimable and slightly improves total transformer
time; M3 uses the faster copied-buffer path.
H3_ZERO_COPY_WEIGHTS=0
disables
the M5 selection for diagnostics.
The streamed Qwen text encoder preallocates a small ring of future layer
buffers and fills them on eight I/O workers while Metal executes the current
layer. The default ring depth is two layers on M3/older hardware and three on
M5, where the target machine has 128 GiB.
H3_QWEN_PREFETCH=0
restores the
single-layer synchronous reference path; values 1-8 select the worker count,
and
H3_QWEN_PREFETCH_DEPTH=1
through
6
overrides the ring depth.
Metal 4 and TensorOps paths
M5 GPUs automatically use native BF16 Metal 4/TensorOps for the DiT QKV and
attention-output projections at sequence lengths up to 2,048. The compact
Morton schedule routes Q/K/V directly into head-major attention inputs, avoids
three MPSGraph input transposes, and is byte-identical to the portable path. It
improves a complete 512x512 50-block forward by about 2% across repeated IT/US
M5 Max runs. For 2,049-3,072 rows, including 864x480, two row-offset Morton
dispatches preserve the efficient tile geometry and improve the complete
forward by about 2% in balanced runs. Still larger sequences stay on MPSGraph.
H3_NAX=0
disables TensorOps for exact A/B diagnosis. The selection is guarded
at runtime and falls back to the unchanged portable library if compilation is
unavailable.
H3_NAX=1
forces the broader native BF16 linear path. It passes the complete
50-block MLX fixture, but remains opt-in: exact-shape microbenchmarks favor its
128-row tile while full DiT runs currently favor MPSGraph scheduling. This
keeps a working NAX integration available for later quantized/fused kernels
without making a benchmark regression the default.
H3_NAX=mlp
selects a more specialized Metal 4 path: paired FC1 gate/up
TensorOps tiles apply SwiGLU in threadgroup memory and write only the
14,336-wide activated intermediate, then FC2 also stays on TensorOps.
H3_DISABLE_NAX_MLP=1
keeps the MPSGraph MLP in a context created this way for
same-process A/B testing. The path is deliberately opt-in because scheduling
depends on the OS GPU stack: the primary macOS 26.5.2 M5 Max gained 1.3-2.0%
in isolated real-weight MLP runs but lost about 1-3% in a complete 50-block forward,
while an otherwise identical macOS 26.5

## Metadata
- **Source**: [Original Article](https://github.com/antirez/h3.c)
