# SmartEdit Architecture Overview

SmartEdit integrates **LLMs**, **multimodal encoders**, and **diffusion models** into a unified editing system.  
Its architecture has three major components:

---

## 1. Textual Alignment (Stage-1)

Purpose: improve LLM understanding of editing-related textual descriptions.

- Uses Vicuna backbone  
- Trained on CC12M-caption-style data  
- Output: text-aware LLM aligned for downstream editing tasks  

Scripts:
- `scripts/TrainStage1_7b.sh`
- `scripts/TrainStage1_13b.sh`

---

## 2. Multimodal Interaction Layer (LLaVA + Q-Former)

SmartEdit uses a **LLaVA-inspired architecture** that binds vision features to the LLM.

Pipeline:
1. Image → Vision Encoder
2. Vision features → Q-Former
3. Q-Former → LLM multimodal tokens

This allows the LLM to reason about the image and understand instructions jointly.

---

## 3. Diffusion Editing Module (InstructDiffusion / Stable Diffusion)

A fine-tuned diffusion model performs pixel-level edits.

- Requires converting SD / InstructDiffusion checkpoints to diffusers format
- Accepts LMM-generated conditioning
- Produces the edited image

---

## Data Flow (Simplified)

1. **Image** → Vision Encoder  
2. **Instruction** → Vicuna LLM  
3. LLaVA/Q-Former fuses both  
4. LMM produces guidance embedding  
5. Guidance passes into **diffusion model**  
6. **Edited image output**

---

## Extensibility

SmartEdit supports:
- Replacing LLM backbones  
- Replacing diffusion base models  
- New dataset integration  
- Custom inference logic  

