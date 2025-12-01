from model_loader import get_answer

def test_qa():
    context = "Hugging Face is a technology company based in New York and Paris."
    question = "Where is Hugging Face based?"
    
    print(f"Context: {context}")
    print(f"Question: {question}")
    
    result = get_answer(context, question)
    
    print("Result:", result)
    
    assert "New York and Paris" in result["answer"]
    print("Test Passed (Real Model)!")

if __name__ == "__main__":
    test_qa()
