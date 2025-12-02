# AI Image Editing Tools Research

> **A comprehensive evaluation and comparison of open-source AI image editing tools for anime-style workflows and ComfyUI integration**

[![Research Status](https://img.shields.io/badge/Status-Active-success)]()
[![Tools Evaluated](https://img.shields.io/badge/Tools%20Evaluated-6-blue)]()
[![ComfyUI Compatible](https://img.shields.io/badge/ComfyUI-Compatible-orange)]()

---

## Project Overview

This repository contains a **systematic research initiative** evaluating open-source AI image editing tools for their effectiveness in anime-style image generation workflows. The research focuses on instruction-based editing capabilities, ComfyUI integration potential, and practical usability for long-form video generation pipelines.

### Research Objectives

- **Evaluate** cutting-edge AI image editing tools for anime workflow compatibility
- **Compare** tools across multiple dimensions: quality, performance, integration ease
- **Document** technical architectures, capabilities, and limitations
- **Recommend** optimal tools for specific use cases and workflow requirements
- **Provide** reproducible ComfyUI workflow examples and integration guides

### Research Methodology

This research employs a **documentation-driven approach**, combining:

1. **Repository Analysis** — Deep dive into official GitHub repositories
2. **Academic Paper Review** — Analysis of arXiv papers and technical documentation
3. **Compatibility Assessment** — Evaluation of ComfyUI integration potential
4. **Comparative Analysis** — Structured multi-dimensional comparison matrices
5. **Workflow Examples** — Collection and organization of practical usage patterns

---

## 📁 Repository Structure

The repository follows a **sequential workflow organization** for optimal navigation:

```
image-editing-tools/
│
├── 📄 README.md                    # This file - project overview and navigation
│
├── 📂 docs/                        # Research documentation
│   └── overview.md                 # Detailed research methodology and scope
│
├── 📂 evaluations/                 # Per-tool technical evaluations
│   ├── ICEdit/                     # Instruction-based Collaborative Editing
│   ├── Step1X-Edit/                # Step-by-step instruction editing
│   ├── SmartEdit/                  # Smart instruction-based editing
│   ├── Fluxtapoz/                  # ComfyUI-native Flux editing nodes
│   ├── SeqImageLoader/             # Sequential image processing utility
│   └── ImageMagick/                # Classic image manipulation integration
│
├── 📂 analysis/                    # Comparative analysis and decision matrices
│   └── comparison-matrix.md        # Side-by-side tool comparison
│
├── 📂 recommended-tools/           # Final recommendations and rationale
│   └── recommended_tools.md        # Curated tool selection with justification
│
├── 📂 examples-workflow/           # ComfyUI workflow examples (JSON)
│   ├── ICEdit/                     # ICEdit workflow examples
│   ├── Step1X-Edit/                # Step1X-Edit workflow examples
│   ├── Fluxtapoz/                  # Fluxtapoz workflow examples
│   ├── SeqImageLoader/             # SeqImageLoader workflow examples
│   └── ImageMagick/                # ImageMagick workflow examples
│
├── 📂 media/                       # Media assets and test images
│   └── tools/                      # Per-tool asset organization
│
└── 📂 scripts/                     # Repository automation utilities
    ├── normalize-names-external.py # Workflow filename normalization script
    └── workflow-metadata.yaml      # Metadata mapping for workflows
```

---

## 🛠️ Tools Evaluated

### Instruction-Based Editing Models

| Tool | Type | ComfyUI Support | Anime Fit | Status |
|------|------|-----------------|-----------|--------|
| **[ICEdit](evaluations/ICEdit/)** | Instruction-based collaborative editing | ✅ Custom nodes available | ⭐⭐⭐⭐ High | Evaluated |
| **[Step1X-Edit](evaluations/Step1X-Edit/)** | Step-by-step instruction editing | ✅ Custom nodes available | ⭐⭐⭐⭐ High | Evaluated |
| **[SmartEdit](evaluations/SmartEdit/)** | Smart instruction-based editing | ❌ No integration | ⭐⭐⭐ Medium | Evaluated |

### ComfyUI-Native Utilities

| Tool | Type | Primary Function | Anime Fit | Status |
|------|------|------------------|-----------|--------|
| **[Fluxtapoz](evaluations/Fluxtapoz/)** | ComfyUI custom nodes | Flux model editing workflows | ⭐⭐⭐⭐⭐ Excellent | Evaluated |
| **[SeqImageLoader](evaluations/SeqImageLoader/)** | ComfyUI utility | Sequential image processing | ⭐⭐⭐⭐ High | Evaluated |
| **[ImageMagick](evaluations/ImageMagick/)** | Classic tool integration | Image transformation | ⭐⭐⭐ Medium | Evaluated |

---

## Quick Start

### Exploring the Research

1. **Start with the overview**: Read [`docs/overview.md`](docs/overview.md) for detailed research context
2. **Review tool evaluations**: Browse [`evaluations/`](evaluations/) for in-depth tool analysis
3. **Compare tools**: Check [`analysis/comparison-matrix.md`](analysis/comparison-matrix.md) for side-by-side comparison
4. **See recommendations**: Review [`recommended-tools/recommended_tools.md`](recommended-tools/recommended_tools.md) for final selections

### Using Workflow Examples

All workflow examples are located in [`examples-workflow/`](examples-workflow/) organized by tool:

```bash
# Example: View ICEdit workflows
ls examples-workflow/ICEdit/

# Example: Load a workflow in ComfyUI
# Simply drag and drop the JSON file into ComfyUI interface
```

### Normalizing Workflow Filenames

The repository includes a normalization utility to maintain consistent workflow naming:

```bash
# Preview proposed filename changes
python3 scripts/normalize-names-external.py --verbose

# Apply standardized naming (creates backups)
python3 scripts/normalize-names-external.py --apply
```

**Canonical filename pattern**: `{tool}--{purpose}--v{major}.json`

**Example**: `ICEdit--basic-editing--v1.json`

---

## Evaluation Criteria

Tools are evaluated across **8 key dimensions**:

1. **Edit Quality & Fidelity** — Identity preservation, structure maintenance, texture realism
2. **Localized Editing Support** — Mask-based and region-specific editing capabilities
3. **Instruction Compliance** — Accuracy in following textual prompts
4. **Anime Workflow Fit** — Suitability for anime-style images and multi-frame edits
5. **ComfyUI Integration** — Ease of integration into ComfyUI workflows
6. **Performance & Latency** — Inference speed and GPU requirements
7. **Ease of Installation** — Setup simplicity and documentation quality
8. **Model Extensibility** — Support for fine-tuning and multi-step pipelines

---

## Documentation Standards

### Workflow Metadata Conventions

For machine-parsable and stable workflow management, the repository follows these conventions:

**External Metadata File** (`scripts/workflow-metadata.yaml`):
```yaml
workflows:
  example_workflow.json:
    tool: ToolName
    purpose: workflow-purpose
    version: "1.0"
```

**Canonical Filename Pattern**:
```
{tool}--{purpose}--v{major}.json
```

**Examples**:
- `ICEdit--basic-editing--v1.json`
- `Fluxtapoz--regional-editing--v1.json`
- `Step1X-Edit--teacache--v1.json`

### Media Asset Management

- Store media under `media/tools/{ToolName}/`
- Include `README.md` describing sources, licensing, and usage
- Avoid committing large model weights (use external storage or `git-lfs`)
- Reference remote URLs in `manifest.json` when applicable


---


## 🔗 Related Resources

- **ComfyUI**: [Official Repository](https://github.com/comfyanonymous/ComfyUI)
- **ICEdit**: [Paper](https://arxiv.org/abs/2305.06474) | [Repository](https://github.com/salesforce/ICEdit)
- **Step1X-Edit**: [Repository](https://github.com/step1x/edit)
- **Fluxtapoz**: [ComfyUI Custom Nodes](https://github.com/logtd/ComfyUI-Fluxtapoz)

