---
base_model: unsloth/qwen3-14b-unsloth-bnb-4bit
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3
- climate
license: apache-2.0
language:
- en
new_version: Qwen/Qwen3-14B
pipeline_tag: text-generation
library_name: adapter-transformers
---

# DH-AI Negotiation Assistant

This model is a fine-tuned version of [`unsloth/qwen3-14b-unsloth-bnb-4bit`](https://huggingface.co/unsloth/qwen3-14b-unsloth-bnb-4bit) using [Unsloth](https://github.com/unslothai/unsloth) and the Hugging Face [TRL library](https://github.com/huggingface/trl) for accelerated training.

## Model Description

- **Base model:** `unsloth/qwen3-14b-unsloth-bnb-4bit`
- **Architecture:** Qwen3-14B (optimized with Unsloth)
- **Fine-tuned by:** [`ilyass31`](https://huggingface.co/ilyass31)
- **License:** Apache 2.0
- **Language:** English
- **Precision:** 4-bit quantization using `bnb` for efficient inference

## Use Case

This model is designed as an AI negotiation assistant, particularly for domains such as:

- Humanitarian negotiations
- Climate diplomacy
- Stakeholder mapping
- Mediation scenarios involving multi-party interests

It can generate:
- Islands of Agreement
- Stakeholder Influence Maps
- Negotiation strategies and recommendations



## Model Training
This model was fine-tuned using:

-QLoRA / LoRA adapters for efficient fine-tuning.
-4-bit quantized base model for memory efficiency during inference.
-Supervised fine-tuning using negotiation-based prompts and domain-specific responses.

## Training Hyperparameters
-Optimizer: AdamW
-Learning rate: 5e-5
-Batch size: 16
-Epochs: 3
-Warmup ratio: 0.1

## Limitations
-GPU Requirement: This model relies on GPU hardware, as Unsloth only supports CUDA devices.

## Citation 

If you use this model in your research or application, please cite the following:
@misc{ilyass31_dhai_negotiation_assistant_2025,
  author = {ilyas DAHAOUI},
  title = {DH-AI Negotiation Assistant},
  year = {2025},
  url = {https://huggingface.co/ilyass31/DH-AI-negotiation-assistant},
  note = {Accessed: 2025-05-03}
}