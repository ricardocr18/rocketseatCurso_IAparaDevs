import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def prepare_training_file(data, filename):
    """Prepara arquivo JSONL no formato correto para fine-tuning"""
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            # Formato para fine-tuning de classificação
            training_example = {
                "messages": [
                    {"role": "system", "content": "Você é um assistente que classifica mensagens de clientes em 'venda' ou 'suporte'."},
                    {"role": "user", "content": item['prompt']},
                    {"role": "assistant", "content": item['completion']}
                ]
            }
            f.write(json.dumps(training_example, ensure_ascii=False) + '\n')
    return filename

def fine_tune_model(training_data, validation_data):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Preparar arquivos temporários
    train_file_path = 'temp_train.jsonl'
    val_file_path = 'temp_validation.jsonl'
    
    prepare_training_file(training_data, train_file_path)
    prepare_training_file(validation_data, val_file_path)
    
    print("📤 Enviando arquivo de treinamento...")
    # Upload training file
    with open(train_file_path, 'rb') as f:
        training_file = client.files.create(
            file=f,
            purpose='fine-tune'
        )
    
    print("📤 Enviando arquivo de validação...")
    # Upload validation file
    with open(val_file_path, 'rb') as f:
        validation_file = client.files.create(
            file=f,
            purpose='fine-tune'
        )
    
    print(f"✅ Arquivo de treino: {training_file.id}")
    print(f"✅ Arquivo de validação: {validation_file.id}")
    
    print("🚀 Iniciando fine-tuning...")
    # Create fine-tuning job
    fine_tune_job = client.fine_tuning.jobs.create(
        training_file=training_file.id,
        validation_file=validation_file.id,
        model=os.getenv("MODEL_NAME"),
        hyperparameters={
            "n_epochs": 3
        }
    )
    
    print(f"✅ Job de fine-tuning criado: {fine_tune_job.id}")
    print(f"📊 Status: {fine_tune_job.status}")
    
    # Limpar arquivos temporários
    os.remove(train_file_path)
    os.remove(val_file_path)
    
    return fine_tune_job

def main():
    from src.utils import load_jsonl
    
    training_data = load_jsonl(os.path.join('src', 'data', 'treino.jsonl'))
    validation_data = load_jsonl(os.path.join('src', 'data', 'teste.jsonl'))

    print(f"✅ Carregados {len(training_data)} exemplos de treino")
    print(f"✅ Carregados {len(validation_data)} exemplos de validação")

    fine_tune_response = fine_tune_model(training_data, validation_data)
    print(f"\n🎯 Fine-tuning job ID: {fine_tune_response.id}")

if __name__ == "__main__":
    main()