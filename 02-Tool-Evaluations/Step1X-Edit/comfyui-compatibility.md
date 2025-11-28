# My Experience with ComfyUI Compatibility — Step1X-Edit Integration

In this document, I share my findings on how the `ComfyUI_Step1X-Edit` extension integrates the **Step1X-Edit** model into ComfyUI, along with the installation steps I followed, how I used it, and some important compatibility considerations I discovered.

---

## 1. Overview

- I found that the `raykindle/ComfyUI_Step1X-Edit` repository provides a **custom node extension** for ComfyUI, which enabled me to use Step1X-Edit’s instruction-based image editing. 
- I observed that it supports **FP8 quantized inference**, **Flash-Attention** acceleration, and **TeaCache** acceleration, which allowed for faster inference with minimal quality loss in my tests. 
- In my opinion, this makes Step1X-Edit much more accessible for high-performance image editing within ComfyUI workflows. 

---

## 2. Installation

Here are the steps I took to install the extension:

1. **Clone the Extension**

   I cloned the `ComfyUI_Step1X-Edit` repository into my ComfyUI custom nodes folder:

   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/raykindle/ComfyUI_Step1X-Edit.git
   ```
2. **Install the required dependencies:**

   Step 1: I installed the ComfyUI_Step1X-Edit dependencies:
   ```bash
      cd ComfyUI_Step1X-Edit
      pip install -r requirements.txt
   ```

   Step 2: I installed [flash-attn](https://github.com/Dao-AILab/flash-attention). I used the provided script to help find the pre-built wheel suitable for my system.
   ```bash
   python utils/get_flash_attn.py
   ```

   The script generated a wheel name like `flash_attn-2.7.2.post1+cu12torch2.5cxx11abiFALSE-cp310-cp310-linux_x86_64.whl`, which I found in:

    - Linux version: [Dao-AILab's flash-attn releases](https://github.com/Dao-AILab/flash-attention/releases)
    - Windows version: [kingbri1's flash-attn releases](https://github.com/kingbri1/flash-attention/releases)

   Then I downloaded the corresponding pre-built wheel and installed it following the instructions in [flash-attn](https://github.com/Dao-AILab/flash-attention).

   *Note: I noticed that even if the CUDA and Torch versions don't match exactly, I could still successfully install flash-attention. However, for optimal performance and compatibility, I recommend using versions that match your system exactly.*

   Step 3: I downloaded the Step1X-Edit-FP8 model.
   ```bash
   ComfyUI/
    └── models/
    ├── diffusion_models/
    │   └── step1x-edit-i1258-FP8.safetensors
    ├── vae/
    │   └── vae.safetensors
    └── text_encoders/
        └── Qwen2.5-VL-7B-Instruct/
   ```


   - Step1X-Edit diffusion model: I downloaded `step1x-edit-i1258-FP8.safetensors` from [HuggingFace](https://huggingface.co/meimeilook/Step1X-Edit-FP8/tree/main) and placed it in ComfyUI's `models/diffusion_models` directory.
   - Step1X-Edit VAE: I downloaded `vae.safetensors` from [HuggingFace](https://huggingface.co/meimeilook/Step1X-Edit-FP8/tree/main) and placed it in ComfyUI's `models/vae` directory.
   - Qwen2.5-VL model: I downloaded [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/tree/main) and placed it in ComfyUI's `models/text_encoders/Qwen2.5-VL-7B-Instruct` directory.


##  Usage

Here is the workflow I followed to use the model:

1. I launched **ComfyUI**.
2. I created a **new workflow**.
3. I added:
   - **Step1X-Edit Model Loader**  
     or  
   - **Step1X-Edit TeaCache Model Loader** (which gave me ~2× speed)
4. I configured the model settings:
   - `diffusion_model` → `step1x-edit-i1258-FP8.safetensors`
   - `vae` → `vae.safetensors`
   - `text_encoder` → `Qwen2.5-VL-7B-Instruct`
   - I set optional parameters (`dtype`, `quantized`, `offload`)
   - For TeaCache: I set `teacache_threshold`
5. I added a **Step1X-Edit Generate** node  
   or  
   **Step1X-Edit TeaCache Generate** (when I was using TeaCache)
6. I provided:
   - an **input image**
   - an **editing prompt**
7. I ran the workflow and got my edited images.

---

##  Parameters

### **Step1X-Edit Model Loader**

| Parameter | Description |
|----------|-------------|
| `diffusion_model` | Select the Step1X-Edit `.safetensors` diffusion model |
| `vae` | Select the Step1X-Edit VAE file |
| `text_encoder` | Path name of Qwen2.5-VL model folder |
| `dtype` | Precision (`bfloat16`, `float16`, `float32`) |
| `quantized` | Use FP8 quantized weights (I recommend: `true`) |
| `offload` | Offload models to CPU when idle |

---

### **Step1X-Edit TeaCache Model Loader — Additional Parameters**

| Parameter | Description |
|-----------|-------------|
| `teacache_threshold` | Controls speed–quality tradeoff |
| `verbose` | Print TeaCache debug logs |

**Recommended TeaCache Thresholds**

| Threshold | Speedup |
|-----------|---------|
| `0.25` | ~1.5× |
| `0.4` | ~1.8× |
| `0.6` | **2× (I recommend this)** |
| `0.8` | ~2.25× with minor quality loss |

---

##  Step1X-Edit Generate / TeaCache Generate

| Parameter | Description |
|-----------|-------------|
| `model` | Loaded Step1X-Edit model bundle |
| `image` | Input image to edit |
| `prompt` | Instruction describing desired edit |
| `negative_prompt` | What to avoid |
| `steps` | Number of denoising steps |
| `cfg_scale` | Guidance scale |
| `image_size` | Output size (I recommend 512) |
| `seed` | Random seed for reproducibility |

---

## TeaCache Acceleration

I found that TeaCache brings major performance boosts:

- Up to **2× faster inference**
- No fine-tuning required (training-free)
- Adaptive feature caching based on timestep embeddings
- Adjustable speed–quality tradeoff via threshold
- Minimal memory overhead


## Memory Requirements

I noticed that the **Step1X-Edit** model requires significant GPU memory for inference.  
The benchmark below is what I measured at **768px resolution** with **10 sampling steps**.

### Performance & VRAM Usage

| Model Version | Peak GPU Memory | Native Speed | ~1.5× Speedup (threshold = 0.25) | ~2.0× Speedup (threshold = 0.6) |
|---------------|------------------|--------------|----------------------------------|---------------------------------|
| **Step1X-Edit-FP8 (offload = False)** | **31.5 GB** | 17.4 s | 11.2 s | **7.8 s** |

```
Note: I tested this model on premium Google colab with a single A100 GPU.
```

---

### Reducing VRAM Usage

To run the model on GPUs with less memory, I enabled:

- **`quantized = true`** — uses FP8 optimization  
- **`offload = true`** — moves inactive layers to CPU to save VRAM  

I found both options available in the **Step1X-Edit Model Loader** node inside ComfyUI.

---
