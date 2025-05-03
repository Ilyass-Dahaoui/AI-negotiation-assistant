import gradio as gr
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("ilyass31/AI-negotiation-assistant", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("ilyass31/AI-negotiation-assistant")

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device_map="auto")

def generate_response(prompt, max_tokens, temperature):
    output = pipe(prompt, max_new_tokens=max_tokens, temperature=temperature, do_sample=True)
    return output[0]["generated_text"]

iface = gr.Interface(
    fn=generate_response,
    inputs=[
        gr.Textbox(lines=10, label="Negotiation Scenario Prompt"),
        gr.Slider(100, 2048, step=50, value=1000, label="Max New Tokens"),
        gr.Slider(0.1, 1.0, step=0.1, value=0.7, label="Temperature")
    ],
    outputs=gr.Textbox(label="Generated Response"),
    title="🧠 AI Negotiation Assistant",
    description="Use this tool to generate negotiation planning aids like Island of Agreement tables and Stakeholder Maps."
)

# Launch
iface.launch()
