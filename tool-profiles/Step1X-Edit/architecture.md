# Architecture Overview — Step1X-Edit

## 1. Introduction

Step1X-Edit is built on a dual-module architecture that integrates:

1. **A Multimodal Large Language Model (MLLM)** for semantic reasoning, instruction interpretation, and multi-turn editing control.
2. **A Diffusion Transformer (DiT)** for high-fidelity image synthesis and precise visual manipulation.

The architecture is designed to support **general-purpose, instruction-based image editing**, preserving semantic consistency and visual identity while enabling complex transformations through natural language.

---

## 2. Core Architectural Components

### 2.1 Multimodal Large Language Model (MLLM)

The MLLM functions as the **semantic controller**, responsible for understanding the user’s instruction and interpreting how it should modify the input image.

#### Responsibilities:
- Understand free-form, natural-language editing instructions  
- Fuse vision and text signals  
- Create a **latent edit embedding** that encodes:
  - edit type  
  - region focus  
  - semantic constraints  
  - multi-turn history dependencies  
- Ensure semantic consistency during multi-step edits  

The MLLM contains approximately **7B parameters** and handles the reasoning aspects that guide the diffusion model.

---

### 2.2 Diffusion Transformer (DiT)

The DiT acts as the **visual generator**, applying the edits encoded by the MLLM’s latent embedding.

#### Core capabilities:
- High-fidelity image rendering  
- Identity and structure preservation  
- Region-targeted visual modification  
- Semantic alignment with instructions  
- Multi-turn refinement  

The diffusion backbone contains **~12B parameters** and supports resolutions such as **512×512** and **1024×1024**.

---

### 2.3 Latent Edit Embedding (Bridge Module)

This intermediate module translates the MLLM’s output into a format compatible with the DiT.

#### Functions:
- Project semantic embeddings to diffusion conditioning tensors  
- Provide spatially aware edit cues  
- Enable instruction-gated modulation of diffusion layers  
- Maintain cross-modal alignment  

This module ensures that the MLLM and DiT operate in a fully integrated manner.

---

## 3. End-to-End Editing Pipeline

Step1X-Edit processes an edit request through the following stages:

### **Step 1 — Input Encoding**
- Image is converted into vision embeddings  
- Instruction is tokenized  
- Previous editing history is optionally included for multi-turn edits  

### **Step 2 — Semantic Reasoning (MLLM)**
- Cross-attention between text + image  
- Instruction interpretation  
- Edit reasoning  
- Output: **latent edit embedding**  

### **Step 3 — Embedding Transformation**
- Projection layers reshape the edit embedding into diffusion-compatible form  
- Spatial and semantic cues extracted  

### **Step 4 — Controlled Diffusion Editing**
- The DiT performs guided denoising  
- Embedding modulates diffusion steps  
- Identity preservation constraints applied  
- Region-level attention allows targeted modifications  

### **Step 5 — Decoding**
- Final latent is decoded into an edited image  
- Ensures high detail, semantic accuracy, and consistency  

---

## 4. Multi-Turn Editing Mechanism

The architecture supports iterative edits using a **self-consistent editing memory** that stores:

- prior image states  
- previous instructions  
- semantic history embeddings  

This enables:
- correction of prior outputs  
- progressive refinement  
- stability across multiple edits  

The **v1p2-preview** version enhances this via a more advanced “reasoning-edit” mode for handling complex requests.

---

## 5. Model Variants

### **Step1X-Edit v1.1**
- Standard pipeline  
- Strong identity preservation  
- Good general-purpose editing accuracy  

### **Step1X-Edit v1p2-preview**
- Enhanced reasoning capabilities  
- Better spatial grounding  
- More consistent region-level accuracy  

---

## 6. Efficiency and Optimization

### **FP8 Quantization**
Reduces VRAM usage while maintaining visual quality.

### **Offloading Support**
Allows running parts of the model on CPU for limited VRAM setups.

### **Optimized Attention**
Compatibility with FlashAttention for faster inference.

---

## 7. Strengths

- Integrated reasoning and diffusion pipeline  
- Excellent semantic alignment  
- High-level identity preservation  
- Region-level edit precision  
- Multi-turn conversational editing  
- Fully open-source  
- Training, inference, and evaluation code available  

---

## 8. Limitations

- High memory requirements (40–50GB recommended)  
- Heavy diffusion backbone  
- No official ComfyUI support currently  
- More demanding than LoRA-based editing models like ICEdit  

---

