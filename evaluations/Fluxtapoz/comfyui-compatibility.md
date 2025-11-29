# My Assessment of ComfyUI-Fluxtapoz Compatibility

> **Note:** I gathered the information in this document from the official [GitHub repository](https://github.com/logtd/ComfyUI-Fluxtapoz). I have not practically tested these nodes myself.

## My Verdict: Fully Compatible
I found that **ComfyUI-Fluxtapoz** is explicitly designed as a set of **custom nodes for ComfyUI**. Therefore, it is natively compatible.

## Installation
I found that installation should follow the standard procedure for ComfyUI custom nodes:
1.  Clone the repository into the `custom_nodes` directory.
2.  Install requirements (if any are specified, though I didn't see a complex `requirements.txt` in the file list, standard dependencies are likely expected).

## Usage
I discovered that the repository provides several **example workflows** in the `example_workflows` directory to get started:
-   `example_rf_inversion_updated.json`
-   `example_rf_inversion_stylization.json`
-   `example_rf_edit_workflow_alternative.json`
-   `example_rf_fireflow.json`
-   `example_flow_edit.json`
-   `example_flux_regional.json`

**Note:** I put the example workflows in the `examples-workflow/Fluxtapoz` folder to make it easier to find them.

I recommend loading these JSON files directly into ComfyUI to understand how to connect the nodes.

## Requirements
I noted that since this is for **Flux**, you will need:
-   A working ComfyUI installation.
-   Flux model checkpoints (Dev or Schnell).
-   Sufficient VRAM to run Flux (typically 12GB+ recommended, though optimizations exist).
