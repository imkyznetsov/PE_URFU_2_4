from transformers import pipeline
model = pipeline(model="seara/rubert-base-cased-russian-sentiment")
model("Привет, ты мне нравишься!")
# [{'label': 'positive', 'score': 0.9818321466445923}]
