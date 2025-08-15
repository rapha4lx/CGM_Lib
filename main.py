import os
from dotenv import load_dotenv
import Json.json as modJson
import gemini.gemini as modGemini


# import smtp.smtp as CGMEmail

env = load_dotenv(dotenv_path="C:\\temp\\update\\.env", override=True)

"""
Example of how to use smtp functions from lib
"""
# EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
# EMAIL_PASS = os.getenv("EMAIL_PASS")

# if type(EMAIL_LOGIN) != str or type(EMAIL_PASS) != str:
#     exit()

# CGMEmail.setCredentials(EMAIL_LOGIN, EMAIL_PASS)

# CGMEmail.sendMsg("rferro.smf@gmail.com", message="test lib")

"""
Example of how to use Gemini abstraction
"""

# GEMMINI_API = os.getenv('GEMINI_API_KEY')

# modGemini.set_credentials(GEMMINI_API)
# response = modGemini.send_simple_question("How does AI work?")

# if not response is None:
#     print(response.text)

# response = modGemini.send_question_context(
#     system_instruction="""Você é um Agente de Extração de Dados de E-mail. Sua principal tarefa é analisar o corpo de e-mails recebidos, identificar a solicitação do usuário e extrair dados específicos quando solicitado.
#     Sua saída DEVE ser sempre um código numérico (ou uma mensagem de erro, se aplicável). Use o seguinte formato: `CODIGO`.
#     **Códigos de Saída e seus significados:**

#     * **1:** **Extração/solicitação/solicito** de **Ativos/base ergon/base/vinculos/pessoas/cadastro**. Este código deve ser usado quando a solicitação se refere a informações sobre status de funcionários (ativos, base ergon, base, cadastro). O dado deve indicar o status Ex: `1`
#     * **9999:** **Não Entendido/Erro**. O agente não conseguiu interpretar a solicitação ou extrair o dado. O dado pode ser uma breve explicação. Ex: `9999`

#     **Instruções para a Extração:**

#     * Priorize a **extração exata** do dado.
#     * Em caso de dúvidas na intenção ou extração, retorne `9999`.""",
#     question="quero")

# if not response is None:
#     print(response.text)

# response = modGemini.send_question_context(
#     system_instruction="""Você é um Agente de Extração de Dados de E-mail. Sua principal tarefa é analisar o corpo de e-mails recebidos, identificar a solicitação do usuário e extrair dados específicos quando solicitado.
#     Sua saída DEVE ser sempre um código numérico (ou uma mensagem de erro, se aplicável). Use o seguinte formato: `CODIGO`.
#     **Códigos de Saída e seus significados:**

#     * **1:** **Extração/solicitação/solicito** de **Ativos/base ergon/base/vinculos/pessoas/cadastro**. Este código deve ser usado quando a solicitação se refere a informações sobre status de funcionários (ativos, base ergon, base, cadastro). O dado deve indicar o status Ex: `1`
#     * **9999:** **Não Entendido/Erro**. O agente não conseguiu interpretar a solicitação ou extrair o dado. O dado pode ser uma breve explicação. Ex: `9999`

#     **Instruções para a Extração:**

#     * Priorize a **extração exata** do dado.
#     * Em caso de dúvidas na intenção ou extração, retorne `9999`.""",
#     question="quero")

# if not response is None:
#     print(response.text)