import gradio as gr

with gr.Blocks() as demo:
    gr.Audio()
    gr.BarPlot(
        value=simple,
        x="item",
        y="inventory",
        title="Simple Bar Plot",
        container=False,
    )
        
demo.launch(server_name="0.0.0.0", server_port=7860)