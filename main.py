import keyboard
import os


def iniciar_questionario():
    print("\nBem-vindo ao questionário sobre Mieloma Múltiplo")
    print("Este questionário foi criado para ajudar na conscientização e fornecer informações importantes sobre esta "
          "condição.")
    print("\nEscolha uma das opções abaixo para continuar:")
    print("1 - Começar o questionário")
    print("2 - Sair")

    while True:
        escolha = input("\nDigite sua opção (1 ou 2): ")
        if escolha == "1":
            print("\nÓtimo! Vamos começar o questionário.")
            break
        elif escolha == "2":
            print("\nObrigado por visitar! Até breve.")
            break
        else:
            print("\nOpção inválida. Por favor, escolha 1 para começar ou 2 para sair.")


iniciar_questionario()


def main():
    running = 1

    while running == 1:

        count = 0

        result = input("Pergunta 1: Você sente dores ósseas persistentes? (S/N) ").lower()
        if result == "s":
            count += 1

        result = input("Pergunta 2: Você tem sentido fraqueza e fadiga constante? (S/N) ").lower()
        if result == "s":
            count += 1

        result = input("Pergunta 3: Você tem tido infecções frequentes ou recorrentes? (S/N) ").lower()
        if result == "s":
            count += 1

        result = input("Pergunta 4: Você teve perda de peso não intencional? (S/N) ").lower()
        if result == "s":
            count += 1

        result = input("Pergunta 5: Você foi diagnosticado(a) com anemia? (S/N) ").lower()
        if result == "s":
            count += 1

        result = input("Pergunta 6: Você foi diagnosticado(a) com hipercalcemia? (S/N) ").lower()
        if result == "s":
            count += 1

        if count >= 3:
            print("\nAtenção: você apresenta múltiplos sintomas associados ao mieloma múltiplo.")
            print("Recomenda-se que você consulte um médico para uma avaliação mais detalhada.")
        else:
            print("\nParece que você apresenta poucos sintomas comuns ao mieloma múltiplo.")
            print("Se os sintomas persistirem ou se intensificarem, procure orientação médica.")

        print("\n1 - Novo Diagnostico ")
        result = input("2 - Sair ")

        if result == "2":
            running = 0
        print("\n")


if __name__ == '__main__':
    main()
