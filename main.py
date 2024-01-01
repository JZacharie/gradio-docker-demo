import gradio as gr

with gr.Blocks() as demo:
    gr.Audio()

demo.launch(server_name="0.0.0.0", server_port=7860)