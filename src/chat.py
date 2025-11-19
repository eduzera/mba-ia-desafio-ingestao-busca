from search import search_prompt

def main():
    question = input("Faça sua pergunta:\n")

    if not question.strip():
        print("Por favor, insira uma pergunta válida.")
        return

    print("-"*40)
    print("PERGUNTA:", question)
    
    chain = search_prompt(question=question)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    print("RESPOSTA:", chain.content)
    print("-"*40)
    
if __name__ == "__main__":
    main()