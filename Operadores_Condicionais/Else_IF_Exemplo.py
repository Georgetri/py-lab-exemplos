idade = 35
renda_mensal = 4000
score_credito = 720
tempo_emprego = 2  # em anos

if idade >= 18:
    if renda_mensal >= 3000:
        if score_credito >= 700:
            if tempo_emprego >= 2:
                print("Empréstimo aprovado: perfil excelente.")
            else:
                print("Empréstimo aprovado com ressalvas: tempo de emprego curto.")
        elif 600 <= score_credito < 700: # o score de crédito está entre 600 e 699
            print("Empréstimo pendente: solicitação em análise devido ao score médio.")
        else:
            print("Empréstimo negado: score de crédito muito baixo.")
    elif 1500 <= renda_mensal < 3000: # Tem renda entre 1500 e 2999
        if score_credito >= 650 and tempo_emprego >= 3:
            print("Empréstimo aprovado com limite reduzido.")
        else:
            print("Empréstimo negado: renda e score insuficientes.")
    else:
        print("Empréstimo negado: renda muito baixa.")
else:
    print("Empréstimo negado: idade mínima não atingida.")

#
# public class AnaliseCredito {
#     public static void main(String[] args) {
#         int idade = 35;
#         double rendaMensal = 4000;
#         int scoreCredito = 720;
#         int tempoEmprego = 2; // em anos
#
#         if (idade >= 18) {
#             if (rendaMensal >= 3000) {
#                 if (scoreCredito >= 700) {
#                     if (tempoEmprego >= 2) {
#                         System.out.println("Empréstimo aprovado: perfil excelente.");
#                     } else {
#                         System.out.println("Empréstimo aprovado com ressalvas: tempo de emprego curto.");
#                     }
#                 } else if (scoreCredito >= 600 && scoreCredito < 700) {
#                     System.out.println("Empréstimo pendente: solicitação em análise devido ao score médio.");
#                 } else {
#                     System.out.println("Empréstimo negado: score de crédito muito baixo.");
#                 }
#             } else if (rendaMensal >= 1500 && rendaMensal < 3000) {
#                 if (scoreCredito >= 650 && tempoEmprego >= 3) {
#                     System.out.println("Empréstimo aprovado com limite reduzido.");
#                 } else {
#                     System.out.println("Empréstimo negado: renda e score insuficientes.");
#                 }
#             } else {
#                 System.out.println("Empréstimo negado: renda muito baixa.");
#             }
#         } else {
#             System.out.println("Empréstimo negado: idade mínima não atingida.");
#         }
#     }
# }
