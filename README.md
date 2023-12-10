
# ID2223 Lab2

## Description
This lab is about Text Transcription using Transformers to your Mother Tongue. The overall framework of this lab is shown as follows.  
<img alt="Framework" src="https://github.com/wenjianma/ID2223Lab2/old_tools/1.png"/>
### Task 1
The file framework of this repo:
```markdown
UI/
|app.py ------------------------------------------------- Gradio UI file
|requirements.txt --------------------------------------- Requirement file we need in UI
|crawler.py --------------------------------------------- Web Crawler
|audio_reader.py ---------------------------------------- Audio Reader
old_tools/ ---------------------------------------------- Old version
README.md  ---------------------------------------------- Readme file
whisper_mandarin_feature_pipeline.ipynb ----------------- Feature pipeline of whisper_mandarin
whisper_mandarin_training_pipeline.ipynb ---------------- Training pipeline of whisper_mandarin
```

In this task, we first fine-tune a pretrained  transformer model [Whisper provided by openai](https://openai.com/research/whisper) for mandarin.

Then, we build and run an inference pipeline with a [Gradio UI on Hugging Face Spaces](https://huggingface.co/spaces/Dengty/Mandarin) for our model. 
In this Gradio UI, we realize the following functions.
1. Speak to Search.User can speak into the microphone about the video they want to search on Youtube.
2. Crawl Video. Then, the web crawler implemented by us will return a URL to the video.
3. Transcription. The audio of this video will be transcribed into text.

### Task 2
In this task, we first explore how can we improve the model performance. We think in the following two approaches.
First approach is model-centric approach, which is about tuning hyperparamters, changing the fine-tuning model architecture.
Second approach is data-centric approach, which is about identifying new data sources enabling to train a better model.
#### Model-Centric Approach
1. Tuning hyperparameters. 



####  Data-Centric Approach


## Contributor
This repo is contributed by [Tianyu Deng](https://github.com/dengty1998) and [Wenjian Ma](https://github.com/wenjianma)