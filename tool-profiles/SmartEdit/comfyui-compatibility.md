# SmartEdit × ComfyUI Compatibility Assessment

## Summary
SmartEdit is **partially compatible** with ComfyUI —  
**Diffusion checkpoints work**, but **the LLM + multimodal pipeline does NOT run inside ComfyUI** without custom nodes.

---

## ComfyUI Strengths
- Node-based diffusion workflows  
- Fully supports **diffusers-format Stable Diffusion checkpoints**  
- Good for inference-only pipelines (img2img, inpainting, LoRAs, etc.)

---

## Compatible Components
✔ Diffusion models (after conversion to diffusers)  
✔ Basic prompt-driven editing  
✔ Mask-based editing  
✔ Using SmartEdit’s diffusion checkpoint purely inside ComfyUI  

---

## NOT Compatible Out of the Box
✘ SmartEdit’s LLaVA multimodal encoder  
✘ Vicuna LLM reasoning  
✘ Q-Former multimodal token mapping  
✘ SmartEdit Stage-1 or Stage-2 training  
✘ Passing arbitrary LMM-guidance embeddings directly into ComfyUI  

ComfyUI does not orchestrate large LMM inference or multimodal reasoning.

---

## Possible Workarounds
### **1. Hybrid Workflow (Recommended)**
- Run SmartEdit LMM reasoning *outside* ComfyUI (Python script).
- Export:
  - refined text prompts  
  - or conditioning tensors  
- Feed these into ComfyUI for diffusion editing.

### **2. Custom ComfyUI Nodes (Advanced)**
Implement:
- LLaVA inference node  
- Vicuna LLM reasoning node  
- SmartEdit guidance node  

This requires significant engineering.

### **3. Diffusion Only Mode**
Use only the SmartEdit diffusion checkpoint inside ComfyUI.

---

## Conclusion
**SmartEdit is not natively compatible with ComfyUI**,  
but you *can* use its **diffusion model** inside ComfyUI, and optionally integrate guidance externally.

