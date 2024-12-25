from transformers import pipeline

def classify_images():
    # You'll need to: pip install transformers[vision]
    classifier = pipeline("image-classification")
    
    # You can use image URLs or local file paths
    images = [
        "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg",
        "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-dog.jpg"
    ]
    
    print("\nImage Classification Examples:")
    for image in images:
        results = classifier(image)
        print(f"\nImage: {image}")
        print("Predictions:")
        for result in results[:3]:  # Show top 3 predictions
            print(f"- {result['label']}: {result['score']:.3f}")

if __name__ == "__main__":
    classify_images()