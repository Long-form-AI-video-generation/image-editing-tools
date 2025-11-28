# My Evaluation of ICEdit‑ComfyUI Official Workflow

In this document, I evaluate ComfyUI compatibility with ICEdit by describing the required nodes, installation steps I took, and my usage guidance. I highlight which ComfyUI nodes I found ICEdit integrates with, the limitations I encountered, and the model and plugin configurations I recommend for reliable operation.


## ComfyUI Workflow

- I found that I can directly load images using the **DiptychCreate** node.
- I observed that images processed by other ComfyUI nodes can also be used; in this case, the DiptychCreate node’s loaded image is ignored.
- I noted that the DiptychCreate node must load an image to prevent workflow errors.


## Installation

### Prerequisites
I first installed ComfyUI with the following commands:
```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
pip install -r requirements.txt
```

In addition, I needed to install [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials) and [ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use).


### Installation Methods
#### 1. ComfyUI-Manager Installation
1. I installed [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager) with the following commands:

```bash
   cd custom_nodes
   git clone https://github.com/ltdrdata/ComfyUI-Manager comfyui-manager
   ```
2. I launched ComfyUI:
```bash
   cd ..	# Make sure you are in the ComfyUI root directory
   python main.py
```


3. I opened the ComfyUI Manager, selected Install via Git URL, and input the URL:
```bash
   https://github.com/hayd-zju/ICEdit-ComfyUI-official.git`
```
4. Then I installed it and just waited a minute.

#### 2. Manual Installation

1.  I cloned this repository into the `custom_nodes` directory inside ComfyUI:
```bash
   cd custom_nodes
   git clone https://github.com/hayd-zju/ICEdit-ComfyUI-official.git
```
2. I launched ComfyUI:
```bash
   cd ..	# Make sure you are in the ComfyUI root directory
   python main.py
```

#### 3. Installation through Git URL
1. I opened the ComfyUI Manager, selected Install via Git URL, and input the URL:
```bash
   https://github.com/hayd-zju/ICEdit-ComfyUI-official.git`
```
2. Then I installed it and just waited a minute.

## Usage
1. Download Required Models: I found that if I can connect to Huggingface, I don't need to download the weights. Otherwise, I need to download the weights to local.
    - [Flux.1-fill-dev](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev).
    - [ICEdit-normal-LoRA](https://huggingface.co/RiverZ/normal-lora/tree/main).
    
2. Use workflow example in `06-Workflow-Examples/ICEdit`: I found I can directly drag the JSON file onto the ComfyUI interface.
