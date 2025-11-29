# My Exploration of SmartEdit 

> **Note:** I gathered the information in this document from the official [arXiv paper](https://arxiv.org/abs/2312.06739) and [GitHub repository](https://github.com/TencentARC/SmartEdit). I have not practically tested this model myself. 

**SmartEdit** is an advanced multimodal instruction-based image editing framework developed by Tencent ARC. I noted that it was selected as a **CVPR-2024 Highlight**, titled *"SmartEdit: Exploring Complex Instruction-based Image Editing with Multimodal Large Language Models"*.

Based on the research paper, I learned that it combines **Large Language Models (LLMs)**, **vision encoders**, and **diffusion models** to perform complex, precise image edits guided entirely by natural-language instructions.

## Features
According to the documentation, the framework includes the following features:
- **Two-stage training pipeline:**
  - **Stage-1:** Textual alignment (LLM tuning using **CC12M** dataset).
  - **Stage-2:** SmartEdit training integrating vision + diffusion modules.
- **Integration of powerful backbones:** The paper states it uses **Vicuna (7B/13B)**, **LLaVA**, and **InstructDiffusion** (based on Stable Diffusion v1.5).
- **Comprehensive Toolset:** The repository provides:
  - Dataset processing scripts for **InstructPix2Pix**, **MagicBrush**, **RefCOCO**, and **LISA**.
  - Training scripts for both 7B and 13B models.
  - Inference demos for understanding and reasoning scenes.
  - Evaluation on their custom **Reason-Edit** benchmark.

## Capabilities
The authors demonstrate that SmartEdit can:
- Perform fine-grained edits (change objects, colors, textures).
- Maintain global scene consistency.
- Understand complex instructions involving relationships and reasoning (e.g., "Add a smaller elephant").

## High-level Requirements
I noted the following requirements:
- PyTorch 2.1.0 + CUDA 11.8  
- FlashAttention  
- **Vicuna-1.1-7B/13B** checkpoints
- **LLaVA-1.1-7B/13B** weights
- **InstructDiffusion** (v1-5-pruned-emaonly-adaption-task.ckpt) converted to diffusers format.
