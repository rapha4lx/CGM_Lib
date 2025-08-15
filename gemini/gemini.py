from google import genai
from google.genai import types

def set_credentials(api_key):
    global client
    client = genai.Client(api_key=api_key)

def get_model_list():
    for model in client.models.list():
        print(model)

def start_chat(system_instruction=None, model_name='gemini-2.0-flash-001'):
    pass

def send_simple_question(model='gemini-2.0-flash-001', question=None, temperature=0, top_p=0.95,
                         top_k=20, candidate_count=1, seed=5, max_output_token=150, presence_penalty=0.0,
                         frequency_penalty=0.0):
    if question is None:
        print("Erro: the content of send_simple_question is None")
        return None

    config = types.GenerateContentConfig(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        candidate_count=candidate_count,
        seed=seed,
        max_output_tokens=max_output_token,
        stop_sequences=['STOP!'],
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
    )

    return client.models.generate_content(model=model, contents=question, config=config)

def send_question_context(model='gemini-2.0-flash-001', context=None, question=None, temperature=0,
                          top_p=0.95, top_k=20, candidate_count=1, seed=5, max_output_token=150,
                          presence_penalty=0.0, frequency_penalty=0.0):
    if client is None:
        print("ERRO: Client not configured, Call the start_chat() function first")
        return None

    if context is None or question is None:
        print("ERRO: context or question is None in send_question_context")
        return None

    config = types.GenerateContentConfig(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        candidate_count=candidate_count,
        seed=seed,
        max_output_tokens=max_output_token,
        stop_sequences=['STOP!'],
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
    )

    response = client.models.generate_content(
        model=model,
        contents=question,
        config=config,
    )

def send_advanced_question(model='gemini-2.0-flash-001', question=None, temperature=0, top_p=0.95,
                           top_k=20, candidate_count=1, seed=5, max_output_token=150, presence_penalty=0.0,
                           frequency_penalty=0.0, response_mime_type='application/json',response_json_schema=None):
    if question is None:
        print("Erro: the content of send_simple_question is None")
        return None

    if response_json_schema is None:
        print("ERRO: json_schema cannot be None")

    config = types.GenerateContentConfig(
        response_mime_type=response_mime_type,
        response_json_schema=response_json_schema,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        candidate_count=candidate_count,
        seed=seed,
        max_output_tokens=max_output_token,
        stop_sequences=['STOP!'],
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
    )

    return client.models.generate_content(model=model, contents=question, config=config)



