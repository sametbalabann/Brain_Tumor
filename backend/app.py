import gradio as gr
import os
import uuid
from PIL import Image
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from predict import predict_image

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

def classify(image):
    path = None
    try:
        filename = f"{uuid.uuid4()}.jpg"
        path = os.path.join(UPLOAD_DIR, filename)
        image.save(path)

        label, confidence = predict_image(path)
        return f"Tahmin: {label} - Güven: {confidence:.2f}"
    except Exception as e:
        print("❌ Hata:", str(e))
        return f"HATA: {str(e)}"
    finally:
        if path and os.path.exists(path):
            os.remove(path)

with gr.Blocks(css="""
    #main-box {
        max-width: 600px;
        margin: auto;
    }

    #submit-btn {
        background-color: #c2410c !important; /* turuncu */
        color: white !important;
        border-radius: 6px;
    }

    #clear-btn {
        background-color: #4b5563 !important; /* koyu gri */
        color: white !important;
        border-radius: 6px;
    }
""") as demo:
    with gr.Column(elem_id="main-box"):
        gr.Markdown("## 🧠 Beyin Tümörü Tespiti\nMRI görüntüsünü yükleyin, tahmin et butonuna basın.")

        image_input = gr.Image(type="pil", label="MRI Görüntüsü Yükle")

        with gr.Row():
            submit_btn = gr.Button("Submit", elem_id="submit-btn")
            clear_btn = gr.Button("Clear", elem_id="clear-btn")

        result_output = gr.Textbox(label="Tahmin Sonucu")

    submit_btn.click(fn=classify, inputs=image_input, outputs=result_output)
    clear_btn.click(fn=lambda: (None, ""), outputs=[image_input, result_output])

demo.launch(share=True)



