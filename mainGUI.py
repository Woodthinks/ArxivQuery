import gradio as gr
import pandas as pd

query_keys = ["ti (Title)", "au (Author)", "abs (Abstract)", "co (Comment)", "jr (Journal Reference)", "cat (Subject Category)", "rn (Report Number)", "id (Id (use id_list instead))", "all (A combined search of all the above"]

context = []

def add_item():

def del_item():
    context.pop()

with gr.Blocks(title="Visual Arxiv Query") as demo:
    gr.Markdown("# Visual Arxiv Query")

    with gr.Row(): 
        with gr.Group():
            with gr.Column():
                keys = gr.Dropdown(choices=query_keys, label = "Query Keys",interactive=True)
                rules = gr.Dropdown(choices=["AND", "OR", "NOT"], label = "Query Rules", interactive=True)    
            with gr.Column():
                words = gr.Textbox(label = "Keywords")  
                with gr.Row():
                    add_button
                    del_button = gr.Button("Delete One Byword",variant="primary")

        with gr.Column():
            for id, c in context:
                with gr.Row():
                    gr.Markdown("")
                    gr.Markdown("")
                    gr.Markdown("")

    # for i in range(2):
    #     with gr.Row():
    #         gr.Markdown(f"# {title[i]}")
    #         Title = gr.Text(f"{title[i]}",scale=10)
    #         download_button = gr.Button("Download",min_width=200,scale=1)
    

if __name__ == "__main__":
    demo.launch()