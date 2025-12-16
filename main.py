import json
import os
from src.fine_tune import fine_tune_model
from src.classify import classify_message
from src.utils import load_jsonl

def main():
    # Load training and validation data
    train_data = load_jsonl(os.path.join('src', 'data', 'treino.jsonl'))
    validation_data = load_jsonl(os.path.join('src', 'data', 'teste.jsonl'))

    print(f"✅ Carregados {len(train_data)} exemplos de treino")
    print(f"✅ Carregados {len(validation_data)} exemplos de teste")

    # Fine-tune the model
    fine_tune_model(train_data, validation_data)
   
    # Classify messages from validation data
    for message in validation_data:
        category = classify_message(message['prompt'])
        expected = message['completion']
        print(f"Message: {message['prompt']}")
        print(f"  Predicted: {category} | Expected: {expected}")
        print()

if __name__ == "__main__":
    main()