# SmartEdit Anime Editing Workflow

A practical workflow for applying SmartEdit to anime-style image editing.

---

## Goals
- Maintain anime line-art consistency  
- Preserve proportions and stylization  
- Perform semantically controlled edits (color changes, expressions, accessories, lighting)

---

## 1. Choose the Right Model
SmartEdit works best with:
- Anime-fine-tuned diffusion models (if available)  
- Or standard SD models + style-preserving masks  

Convert models to diffusers format using the provided script.

---

## 2. Prepare Inputs
- High-quality anime source image  
- Optional masks for protecting lines or faces  
- Clear instruction prompt  
  Example:  
  *“Change hair to pastel pink and add a blue ribbon. Keep pose and expression unchanged.”*

---

## 3. (Optional) Use SmartEdit LMM Guidance
Run SmartEdit’s LLaVA + Vicuna pipeline to:
- Refine the instruction  
- Create multimodal conditioning  
- Improve edit precision  

---

## 4. Diffusion Editing
Use the SmartEdit diffusion component to apply the edit:
- Strong masks → preserve key linework  
- Lower CFG scale → maintain style  
- Higher denoise strength → major changes  

---

## 5. Post-Processing
- Light sharpening  
- Line reinforcement  
- Color correction  
- Optional secondary controlled pass for refinement  

---

## Tips
- Anime images require stronger structure-preserving constraints.  
- Use shorter, explicit prompts for more consistent outputs.  
- For batch workflows, automate:  
  - LMM reasoning → diffusion editing → post-process

