# My Overview of SmartEdit Architecture

> **Note:** I gathered the information in this document from the official [arXiv paper](https://arxiv.org/abs/2312.06739) and [GitHub repository](https://github.com/TencentARC/SmartEdit). I have not practically tested this model myself.

Based on my review of these resources, I found that SmartEdit integrates **LLMs**, **multimodal encoders**, and **diffusion models** into a unified editing system.  
I noted that the architecture is described as having three major components:

---

## 1. Textual Alignment (Stage-1)

Purpose: I found this improves LLM understanding of editing-related textual descriptions.

- **Backbone:** Uses **Vicuna-1.1 (7B or 13B)**.
- **Data:** Trained on **CC12M** caption-style data.
- **Output:** A text-aware LLM aligned for downstream editing tasks.

Scripts I noted:
- `scripts/TrainStage1_7b.sh`
- `scripts/TrainStage1_13b.sh`

---

## 2. Multimodal Interaction Layer (LLaVA + Q-Former)

I found SmartEdit uses a **LLaVA-inspired architecture** that binds vision features to the LLM.

Pipeline I traced:
1. **Image** → Vision Encoder (CLIP-based)
2. **Vision features** → **Q-Former** (from BLIP-2 style architecture)
3. **Q-Former** → LLM multimodal tokens

**New Tokens:** I discovered that SmartEdit expands the vocabulary by adding:
- `<im_start>` and `<im_end>`
- A special `img` token for system messages.
- **32 new tokens** (`<img_0>` to `<img_31>`) to summarize image and text information for the conversation system.

I observed this allows the LLM to reason about the image and understand instructions jointly.

---

## 3. Diffusion Editing Module (InstructDiffusion)

I found a fine-tuned diffusion model performs pixel-level edits.

- **Base Model:** Uses **InstructDiffusion** (initialized from Stable Diffusion v1.5).
- **Process:** Requires converting the `.ckpt` to diffusers format using `convert_original_stable_diffusion_to_diffusers.py`.
- **Mechanism:** Accepts LMM-generated conditioning (the 32 image summary tokens) to guide the generation.

---

## 4. Data Flow (Simplified)

I summarized the data flow as follows:

1. **Image** → Vision Encoder  
2. **Instruction** → Vicuna LLM  
3. LLaVA/Q-Former fuses both using the **32 special tokens**  
4. LMM produces guidance embedding  
5. Guidance passes into **InstructDiffusion**  
6. **Edited image output**

---

## 5. Extensibility

I found SmartEdit supports:
- Replacing LLM backbones (7B vs 13B)
- Evaluation on custom benchmarks like **Reason-Edit**
- Integration of various datasets (InstructPix2Pix, MagicBrush, LISA)
