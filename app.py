from typing import Any

import gradio as gr
from PIL import Image
from transformers import pipeline


MODEL_ID = "google/vit-base-patch16-224"
TOP_K = 5

classifier = pipeline(
    task="image-classification",
    model=MODEL_ID,
)


def classify_image(image: Image.Image | None) -> dict[str, float]:
    """Return the top predictions and their confidence scores."""
    if image is None:
        raise ValueError("Primero cargá una imagen para clasificar.")

    predictions: list[dict[str, Any]] = classifier(image.convert("RGB"), top_k=TOP_K)
    return {
        prediction["label"]: prediction["score"]
        for prediction in predictions
    }


demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil", label="Cargá una imagen"),
    outputs=gr.Label(num_top_classes=TOP_K, label="Predicciones"),
    title="Clasificador de imágenes con ViT",
    description=(
        "Subí una imagen para clasificarla con "
        f"`{MODEL_ID}`. Se muestran las {TOP_K} clases más probables."
    ),
)


if __name__ == "__main__":
    demo.launch()
