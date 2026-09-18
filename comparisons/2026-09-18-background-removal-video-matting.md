# Review Smoke Screen Features — Background Removal / Video Matting Audit

Date: 2026-09-18

## Scope

This review came from the Active & Productive / BigBag foldables product-video problem: remove the baked grey studio background from a 1288×1608, 24 fps, ~4.7 s eyewear fold-motion clip while preserving glossy black frames, lenses, hinges, thin temples, highlights and temporal consistency.

Observed failures during the live benchmark:

- classical OpenCV / threshold / GrabCut-style masking was not production-usable
- frame-by-frame SAM3 polygon segmentation found the product, but produced hard/vector-like edges, grey contamination, unstable thin parts and temporal shape drift
- SAM3 Video Tracker was wired successfully in Roboflow Workflows, but could not run through the normal remote-step execution path
- VideoBGNinja and UnBG were rejected for this footage because the foreground became partially transparent / ghosted and lost product detail

The immediate requirement is therefore true product/object video segmentation or matting with stable temporal propagation and a soft/refined alpha edge.

## PUSH / benchmark candidates

### BEN2

Upstream: https://github.com/naufalso/BEN2

Classification: PUSH — BENCHMARK FIRST FOR PRODUCT VIDEO BACKGROUND REMOVAL

Why it matters:

- object-focused background erase / foreground segmentation rather than human-only portrait matting
- Confidence Guided Matting refinement
- documented 4K/object segmentation and edge-refinement goals
- includes a real `segment_video()` path
- can emit alpha-layer WebM
- ONNX model is available
- MIT license

Current AP acceptance benchmark:

1. Run the existing 1.5 s / 36-frame black fold clip.
2. Preserve lenses, bridge, hinge hardware and temple tips.
3. No grey studio spill inside the foreground.
4. No frame-to-frame mask redraw / jitter.
5. No transparency loss in black frame surfaces.
6. If clean, process the full ~4.7 s clip and composite on pure white.

Promotion remains blocked until this benchmark passes.

### BiRefNet

Upstream: https://github.com/ZhengPeng7/BiRefNet

Classification: PUSH — HIGH-RES OBJECT / MATTE REFINEMENT SPECIALIST

Why it matters:

- MIT license
- high-resolution dichotomous/object segmentation
- dedicated HR-matting model
- dynamic-resolution model
- foreground refinement path
- strong fit for product stills and difficult thin/high-contrast object boundaries

Likely role:

Use as a high-resolution product/still remover and as an edge-refinement candidate if BEN2 gives good temporal object retention but imperfect matte boundaries.

### Cutie

Upstream: https://github.com/hkchengrex/Cutie

Classification: PUSH — TEMPORAL VIDEO-OBJECT SEGMENTATION SPECIALIST

Why it matters:

- MIT license
- follow-up to XMem
- designed for better consistency, robustness and speed
- accepts an initial object mask and propagates it through video
- suitable for the exact failure mode seen with independent SAM3 masks: temporal silhouette drift

Likely role:

Stable object identity / mask propagation layer before a soft-alpha refinement stage.

Preferred future architecture:

```text
Video
  ↓
Initial object mask
  ↓
Cutie
  → stable temporal object mask
  ↓
BEN2 or BiRefNet / Lucida-style refinement
  → soft/refined alpha
  ↓
FFmpeg
  → transparent / white / branded background
```

### rembg

Upstream: https://github.com/danielgatis/rembg

Classification: PUSH — GENERAL BACKGROUND-REMOVAL UTILITY

Why it matters:

- MIT license
- CLI, Python library, HTTP server and Docker use
- CPU/GPU ONNX backends
- batch processing
- mask-only output
- alpha matting
- color decontamination
- RGB24 stream support designed to interoperate with FFmpeg
- useful as generic infrastructure for catalog stills and automation even if it is not the premium-video answer alone

Boundary:

Do not assume rembg frame-by-frame processing is temporally stable enough for fold-motion video without a dedicated propagation layer.

## PUSH / reference workstation

### ComfyUI-RMBG

Upstream: https://github.com/1038lab/ComfyUI-RMBG

Classification: PUSH / REFERENCE — MULTI-MODEL BACKGROUND-REMOVAL WORKSTATION

Why it matters:

Current repository integrates a broad removal / segmentation toolbox including:

- RMBG-2.0
- InSPyReNet
- BEN / BEN2
- BiRefNet
- SDMatte
- SAM / SAM2 / SAM3
- GroundingDINO
- mask enhancement / extraction / conversion utilities
- Lucida, described by the project as a BiRefNet fine-tune for transparent objects, camouflage, text/logos, glow/VFX and illustrations

The Lucida direction is particularly relevant to glossy / transparent eyewear and other difficult catalog objects.

Boundary:

Repository license is GPL-3.0. Treat this primarily as a workstation / reference / externally separated tool unless commercial distribution architecture has been reviewed for copyleft obligations.

## RETAIN / reference

### XMem

Upstream: https://github.com/hkchengrex/XMem

Classification: RETAIN / REFERENCE — LONG-TERM VIDEO-OBJECT MEMORY ARCHITECTURE

Useful for long videos and temporal segmentation, but Cutie is the newer preferred benchmark path.

### Track-Anything

Upstream: https://github.com/gaomingqi/Track-Anything

Classification: RETAIN / REFERENCE — INTERACTIVE VIDEO ROTOSCOPING / MASK BOOTSTRAP

Useful for generating or correcting first-frame / seed masks and interactive tracking workflows.

## WATCH / not core for object-product removal

### MatAnyone / MatAnyone 2

Upstreams:
- https://github.com/pq-yang/MatAnyone
- https://github.com/pq-yang/MatAnyone2

Classification: WATCH / REFERENCE — HUMAN VIDEO MATTING

Strengths:

- consistent memory propagation
- foreground + alpha video outputs
- soft matte emphasis rather than segmentation-like hard boundaries

Reasons not to make it core for AP eyewear:

- official scope is human video matting
- object-product footage is out of its intended domain
- S-Lab license permits non-commercial redistribution/use by default; commercial redistribution/use requires permission

## SKIP for current AP eyewear benchmark

### RobustVideoMatting

Reason:
High-quality temporal matting, but explicitly designed around human video matting. Wrong first-choice domain for glossy eyewear product motion.

### BackgroundMattingV2

Reason:
Human-focused matting and assumes background/reference conditions that do not match the current AP source clip.

### MODNet

Existing stack status: KEEP AS PORTRAIT-MATTING REFERENCE

Reason:
Useful real-time portrait matting implementation and custom-video pipeline, but explicitly portrait/human oriented. Not the preferred engine for product eyewear.

## Current implementation decision

Immediate benchmark order:

1. BEN2 on the existing 1.5 s black fold clip.
2. If object retention is good but temporal stability is weak, introduce Cutie propagation.
3. If temporal tracking is good but edges are still rough, benchmark BiRefNet / HR-matting refinement.
4. Evaluate Lucida through ComfyUI-RMBG for transparent/glossy-object edge cases.
5. Only after a clean 1.5 s result should the full ~4.7 s black motion be processed.
6. Reuse the resulting mask sequence for color variants only when frame geometry/timing is proven identical.

## Admission state

These are findings and benchmark candidates, not silent core promotion.

Per the stack admission policy:

- BEN2: source/fit review passes → benchmark required
- BiRefNet: source/fit review passes → benchmark required
- Cutie: source/fit review passes → benchmark required
- rembg: useful generic utility → benchmark / optional admission
- ComfyUI-RMBG: useful workstation/reference → GPL boundary retained
- MatAnyone series: reference/watch because of human-domain fit and commercial-license constraints

No model weights were downloaded and no new local dependencies were installed during this review.
