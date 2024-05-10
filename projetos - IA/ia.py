import google.generativeai as genai

# Substitua API-KEY por sua API KEY
api_key = 'API-KEY'
genai.configure(api_key=api_key)

generation_config = {
    'candidate_count': 1,
    'temperature': 0.5,
}

safety_settings = {
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL': 'BLOCK_NONE',
    'DANGEROUS': 'BLOCK_NONE',
}

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=generation_config,
                              safety_settings=safety_settings)

chat = model.start_chat(history=[])

print('Olá, seja bem vindo ao assistente virtual Aizen.2', "\n")
nome = input('Qual o seu nome? ')

opcoes = ['Relacionamentos', 'Infomação Sobre Saúde', 'Reflexões', 'Sintomas', 'Ideias de Passa Tempo', 'Suporte Emocional', 'Indicações de Livros e Filmes']
print(f'Olá {nome}, o que gostaria de fazer? ')
for i, opcao in enumerate(opcoes, 1):
    print(f"{i}-{opcao} ")
escolha = int(input('Digite o número da sua escolha: '))
escolha = opcoes[escolha - 1]

if escolha == 'Relacionamentos':
    relacionamento = input('Sobre que tipo de relacionamento você deseja conversar, ' + (nome) + '? ' + '\n')
    response = chat.send_message('Atue como um profissinal em relacionamentos e me diga o que é bom para esse tipo de situação de relacionamento ' + (relacionamento) + 'e me dê dica, como amigo, sobre o que fazer')
    print('Resposta:', response.text, '\n')
    duvida = input("Deseja mais alguma informação sobre o assunto, " + (nome) + "? ['sim' 'não']? ")
    if duvida == 'sim':
        response = chat.send_message('Poderia me dar mais alguma informação sobre? ' + '\n')
        print('Resposta: ', response.text, '\n')
    elif duvida == 'não':
        print('Tudo bem, espero ter conseguido ajudar, até mais')

elif escolha == 'Infomação Sobre Saúde':
    informacao = input('Qual informação sobre a saúde você deseja, ' + (nome) + '? ' + '\n')
    response = chat.send_message('Atue como especialista e fale-me sobre informação da saúde pedida' + (informacao) + 'e me indique 2 sites que podem me ajudar nessa respectiva dúvida perguntada e 1 site sobre nutrição que possa me ajudar nesse quesito' )
    print('Resposta: ', response.text, '\n')

elif escolha == 'Reflexões':
    reflexoes = input('O que está te deixando tão pensativo, ' + (nome) + '?' + '\n')
    response = chat.send_message('Atue como um profissional da psicologia e me ajude nessa reflexão ' + (reflexoes) + 'e me indique 2 livros que podem me ajudar nessa dúvida ou situação')
    print('Resposta: ', response.text, '\n')
    
elif escolha == 'Sintomas':
    sintoma = input('Qual sintoma você está sentindo, ' + (nome) + '?' + '\n')
    response = chat.send_message('Atue como um profissional da saúde e me indique algo bom para melhorar esse sintoma: ' + (sintoma) + '. Recomende o tratamento e no final me diga isso: Consulte um profissional médico para obter um diagnóstico preciso.')
    print('Resposta: ', response.text, '\n')
    duvida = input('Deseja mais alguma informação sobre o assunto, ' + (nome) + "? ['sim' 'não']: ")
    if duvida == 'sim':
        response = chat.send_message('Poderia me informar mais algum sintoma? ' + '\n')
        print('Resposta: ', response.text, '\n')
    elif duvida == 'não':
        print('Consulte um profissional médico para obter um diagnóstico preciso.')

elif escolha == 'Ideias de Passa Tempo':
    passatempo = input('Poderia me dar um exemplo do que você gosta? Se quiser algo novo posso sugerir também, ' + (nome) + ':' + '\n')
    response = chat.send_message('Seja um profissional sobre coisas legais para passar o tempo ou arrumar um hobbie, caso eu te dê um exmplo do que gosto me indique algo relevante sobre:' + (passatempo) + '. Ou caso eu peça que sugira algo novo me dê 3 ideias boas de novos passa tempos')
    print('Resposta: ', response.text, '\n')

elif escolha == 'Suporte Emocional':
    response = chat.send_message('Estou precisando de '+ (escolha) +', Me ajude em poucas palavras e converse comigo como se fosse um amigo ' + '\n')
    print("Resposta:", response.text, '\n')
    emocional = input('Escreva...?' + '\n')

    while emocional != 'fim':
        response = chat.send_message(emocional)
        print("Resposta:", response.text, '\n')
        emocional = input('Escreva...?' + '\n')

elif escolha == 'Indicações de Livros e Filmes':
    indicacao = input('Diga-me o gênero que você mais gosta e te indicarei os melhores filmes e livros do que você pedir, ' + (nome) + ':' + '\n')
    response = chat.send_message('Procure por 3 filmes e 3 livros e onde posso encontrar os filmes para assistir e onde posso encontrar os livros para ler, mais bem elogiados por esse gênero que pedi: ' + (indicacao) + '. E no final me deseja um ótimo dia.')
    print('Resposta: ', response.text, '\n')
