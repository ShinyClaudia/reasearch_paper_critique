from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generate_critique(text):
    if len(text) > 3000:
        text = text[:3000]

    summary = summarizer(text, max_length=250, min_length=100, do_sample=False)[0]['summary_text']

    research_gap = "The paper could explore emerging trends in the domain, such as transformer-based architectures."
    suggestions = "Improve clarity in the methodology section and provide more comparative evaluations."

    return {
        "summary": summary,
        "research_gap": research_gap,
        "suggestions": suggestions
    }