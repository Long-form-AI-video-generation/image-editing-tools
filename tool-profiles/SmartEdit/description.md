# SmartEdit 

**SmartEdit** is an advanced multimodal instruction-based image editing framework developed by Tencent ARC.  
It combines **Large Language Models (LLMs)**, **vision encoders**, and **diffusion models** to perform complex, precise image edits guided entirely by natural-language instructions.

## Features
- Two-stage training pipeline:
  - **Stage-1:** Text alignment (LLM tuning using CC12M).
  - **Stage-2:** SmartEdit training integrating vision + diffusion modules.
- Integrates **Vicuna**, **LLaVA**, and **diffusion-based editing models**.
- Provides:
  - Dataset processing scripts  
  - Training scripts  
  - Inference demos  
  - Evaluation on benchmarks like Reason-Edit, RefCOCO, COCOStuff.

## Capabilities
SmartEdit can:
- Perform fine-grained edits (change objects, colors, textures).
- Maintain global scene consistency.
- Understand complex instructions involving relationships and reasoning.

## High-level Requirements
- PyTorch 2.1.0 + CUDA 11.8  
- FlashAttention  
- LLaVA & Vicuna checkpoints  
- Stable Diffusion / InstructDiffusion model weights  
- Diffusers-format converted diffusion models

## Quick Start
1. Install dependencies.  
2. Download checkpoints into `checkpoints/`.  
3. Prepare/edit datasets using provided scripts.  
4. Train Stage-1, then Stage-2.  
5. Run inference via scripts under `test/`.

