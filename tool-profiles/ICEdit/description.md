# ICEdit: Instruction-Based Image Editing System

ICEdit is a state-of-the-art, instruction-driven image editing system developed by the authors of the **In-Context Edit** paper (NeurIPS 2025). It is designed to facilitate **high-quality, multi-turn image edits** by following natural language instructions while remaining **resource-efficient**. Leveraging tiny LoRAs and Mixture-of-Experts (MoE) variants, ICEdit achieves fine-grained, identity-preserving modifications with minimal computational overhead, making it suitable for both research and production settings.

---

## Overview

ICEdit provides a **production-ready, instruction-following image editor** that is:

- **Lightweight and efficient:** LoRA-centric design enables fast fine-tuning and inference with low resource consumption.  
- **Multi-turn capable:** Supports iterative, step-wise edits based on sequential instructions while maintaining consistency across edits.  
- **Integration-ready:** Ships with an **official ComfyUI workflow**, enabling seamless integration into reproducible, node-based pipelines.  
- **Accessible for exploration:** Includes a **Gradio demo** with a LoRA scaling slider for real-time experimentation and adjustment of edit strength.

The system is designed for instruction-based editing tasks including **color and attribute adjustments**, **style transfers that preserve identity**, and **other guided modifications**. It automatically resizes input images to a width of 512 pixels, ensuring compatibility with the underlying models.

---

## Key Features

1. **Instructional Editing**
   - Executes edits according to **natural language instructions**.  
   - Supports **multi-turn interactions**, allowing iterative refinement of images while retaining coherence and identity.

2. **LoRA-Based Editing**
   - Employs **small, parameter-efficient LoRAs** to perform fine-grained identity and style edits.  
   - Ensures rapid inference and training with minimal computational cost.

3. **MoE-LoRA Capability**
   - Provides an **optional Mixture-of-Experts checkpoint** for enhanced editing capability.  
   - Enables a specialized inference path for complex edits requiring higher model capacity.

4. **Official ComfyUI Workflow**
   - Fully integrated into **ComfyUI**, facilitating reproducible and modular editing pipelines.  
   - Registered in the **Comfy Registry**, allowing immediate adoption into existing workflows.

5. **Interactive Gradio Demo**
   - Enables quick exploration of edit parameters and LoRA scaling in real time.  
   - Supports iterative experimentation with multi-turn instruction sequences.

6. **Automatic Input Resizing**
   - Input images are resized to **width 512** automatically, standardizing processing and preserving model fidelity.  

7. **Supported Tasks**
   - Instruction-based **color and attribute edits**  
   - **Style transfers** with identity preservation  
   - Multi-turn, **iterative edits** guided by sequential instructions

