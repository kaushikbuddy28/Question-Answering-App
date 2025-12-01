# Models Tried

This document logs the experimentation process for selecting the best Question Answering model.

## 1. distilbert-base-cased-distilled-squad
- **Link**: [Hugging Face](https://huggingface.co/distilbert-base-cased-distilled-squad)
- **Status**: ❌ Failed
- **Issues**:
  - Failed to handle uppercase inputs correctly (e.g., "WHAT IS AGE OF KAUSHIK" -> "MY NAME").
  - Low confidence scores on simple extraction tasks.

## 2. distilbert-base-uncased-distilled-squad
- **Link**: [Hugging Face](https://huggingface.co/distilbert-base-uncased-distilled-squad)
- **Status**: ❌ Failed
- **Issues**:
  - Better than cased version but still struggled with specific phrasing.
  - Extracted "KAUSHIK CHATURVEDI" correctly but failed on "WHAT IS MY NAME" with context "MY NAME IS KAUSHIK CHATURVEDI".

## 3. deepset/roberta-base-squad2
- **Link**: [Hugging Face](https://huggingface.co/deepset/roberta-base-squad2)
- **Status**: ❌ Failed
- **Issues**:
  - Powerful model but failed on the specific "WHAT IS MY NAME" test case (Score: ~0.83).
  - Extractive only, cannot handle summarization.

## 4. bert-large-uncased-whole-word-masking-finetuned-squad
- **Link**: [Hugging Face](https://huggingface.co/bert-large-uncased-whole-word-masking-finetuned-squad)
- **Status**: ✅ Passed (Extractive)
- **Performance**:
  - Highest accuracy on extraction tasks (Score: ~0.92).
  - Correctly identified "KAUSHIK CHATURVEDI" even with uppercase input.
- **Limitation**: Purely extractive, cannot summarize or reason.

## 5. google/flan-t5-base (Final Selection)
- **Link**: [Hugging Face](https://huggingface.co/google/flan-t5-base)
- **Status**: 🏆 Selected
- **Reasoning**:
  - **Generative Capability**: Can summarize and reason, unlike BERT/RoBERTa.
  - **Performance**: Correctly summarized "Effective Hours vs Gross Hours" and answered reasoning questions.
  - **Flexibility**: Handles natural language queries better.
- **Trade-offs**:
  - Slightly slower inference than DistilBERT.
  - Confidence scores are not as straightforward as extractive models (mocked or omitted in simple pipelines).

## Summary
We moved from lightweight extractive models (DistilBERT) to larger extractive models (BERT-Large) to solve accuracy issues. Finally, we switched to a generative model (FLAN-T5) to support summarization and reasoning capabilities requested by the user.
