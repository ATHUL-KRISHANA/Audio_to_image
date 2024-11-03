# Speech-to-Image Generator

## Overview

Welcome to the Speech-to-Image Generator! This project leverages advanced speech recognition and deep learning technologies to transform spoken language into stunning visual representations. By converting audio input into text and then using a powerful image generation model, users can easily create images that illustrate their ideas.

## How It Works

### 1. Audio Input
- Users can record their speech using a microphone.
- The audio input is captured using the `pyaudio` library.
- Once recorded, the audio is processed to convert it into text using the `speech_recognition` library.

### 2. Text Processing
- The transcribed text serves as a prompt for the image generation process.
- This allows for diverse and contextually relevant image outputs based on the user's spoken words.

### 3. Image Generation
- The Stable Diffusion model from Hugging Face is employed to generate high-quality images from the provided text.
- This model uses advanced machine learning techniques to create visuals that align closely with the input description.

## Technical Challenges

One of the main challenges faced during the development of this project was the limitation of my local machine, which lacks a dedicated GPU. To efficiently run the Stable Diffusion model, I utilized Google Colab, which provides the necessary computational resources. The audio recording and text conversion processes were managed locally to streamline the workflow.

## Getting Started

To run the Speech-to-Image Generator on your own machine, follow these steps:

### Prerequisites
- Python 3.x
- Necessary libraries: `pyaudio`, `speech_recognition`, and `transformers` (for Stable Diffusion)


