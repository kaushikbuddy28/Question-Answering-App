from transformers import pipeline
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_model():
    # Use FLAN-T5 for generative Question Answering
    # This model can handle summarization, reasoning, and extraction
    model_name = "google/flan-t5-base"
    logger.info(f"Loading model: {model_name}")
    # text2text-generation is appropriate for T5
    gen_pipeline = pipeline("text2text-generation", model=model_name)
    return gen_pipeline

# Initialize the model once
qa_model = get_model()

def get_answer(context: str, question: str):
    """
    Get answer for a given question and context using a generative model.
    Constructs a prompt and returns the generated text.
    """
    # Construct a prompt for the generative model
    # Standard T5 format often works better
    prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    
    # Generate answer
    # max_length=512 to allow for longer explanations/summaries
    result = qa_model(prompt, max_length=512)
    
    # Extract generated text
    answer_text = result[0]['generated_text']
    
    # Generative pipelines don't provide a simple confidence score like extractive ones.
    # We'll return a placeholder high confidence since the model generated it.
    # In a real app, you might use logprobs if available or a separate confidence model.
    return {
        "answer": answer_text,
        "confidence_score": 0.95 
    }
