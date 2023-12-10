from googleapiclient.discovery import build
import gradio as gr
import crawler
import audio_reader


iface = gr.Interface(
    fn=audio_reader.transcribe_audio,
    inputs=gr.Audio(label="Speak into the microphone"),
    outputs="text",
    live=True,
)

custom_interface = gr.Interface(
    fn=crawler.audio_downloader,
    inputs=gr.Textbox(placeholder="The URL of Youtube Video"),
    outputs="audio"
)

hf_interface = gr.load(
    "models/Wenjian12581/whisper-small-mandarin", title=None)

combined_interface = gr.TabbedInterface(interface_list=[
                                        iface, custom_interface, hf_interface], tab_names=['Speak to Search', 'Crawl Audio', 'Transcription'])

combined_interface.launch()
