programa {
  funcao inicio() {
    inteiro ano_atual, ano_nascimento, idade
    cadeia nome
    ano_atual = 2025
    escreva("Digite seu nome: ")
    leia(nome)
    escreva("Digite o ano do seu nascimento: ")
    leia(ano_nascimento)
    idade = ano_atual - ano_nascimento
    escreva(nome,", calculei a sua idade.\n")
    escreva("Sua idade é ", idade, " anos.")
  }
}
