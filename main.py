import gradio as gr
import whisper

def greet(name):
    return "Hello " + name + "!"

def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result["text"]

with gr.Blocks() as demo:
    gr.Audio()
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

demo.launch(server_name="0.0.0.0", server_port=7860)