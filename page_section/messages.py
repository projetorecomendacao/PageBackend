class Options():
        INTERVIEW = [
            ["Participante", "Participante"],
            ["Cuidador Formal", "Cuidador Formal"],
            ["Familiar", "Familiar"]
        ]

        GENDER = [
            ["M", "Masculino"],
            ["F", "Feminino"]
        ]

        CHOICES = [
            ["S", "Sim"],
            ["N", "Não"]
        ]

        LOSTWEIGHT =[
            ["Não","Não"],
            ["Não sabe","Não sabe"],
            ["Mais de 3 KG", "Mais de 3 Kg"],
            ["Entre 1 e 3 KG", "Entre 1 e 3 KG"],
        ]

        PROBLEMS =[
            ["N","Não"],
            ["E","Estresse Psicológico"],
            ["D", "Doença Aguda"],
            ["I", "Internação"],
            ["K", "Estresse Psicológico e Doença Aguda"],
            ["W", "Estresse Psicológico e Internação"],
            ["Y", "Doença Aguda e Internação"],
            ["Z", "Todos"]
        ]

        need_investigation_question = "Necessita Investigação?"

        questions = ["questões"]
        questions.insert(1, "1. O(A) senhor(a) considera que sua memória é tão boa quanto antes?")
        q02 = ["2. Memória"]
        q02.insert(1,"2. Memória - Pontuação: (0 a 7)")
        questions.insert(2,q02)
        q03 = ["3. Linguagem, função executiva e atenção"]
        q03.insert(1,"3. Linguagem, função executiva e atenção - Pontuação: (0 a 100)")
        questions.insert(3, q03)
        q04 = ["4. Habilidade visuoespacial"]
        q04.insert(1,"4. Habilidade visuoespacial - Pontuação: (0 a 4)")
        questions.insert(4,q04)
        q05 = ["5. Praxia"]
        q05.insert(1,"5. Praxia - Pontuação: (0 a 3)")
        questions.insert(5, q05)
        q06 = ["6. Memória"]
        q06.insert(1,"6. Memória - Pontuação: (0 a 7)")
        questions.insert(6, q06)
        q07 = ["7. Que idade o(a) senhor(a) sente ter?"]
        q07.insert(1, "Por quê?")
        q07.insert(2, "O(a) idoso(a) sente-se mais velho do que realmente é?")
        questions.insert(7, q07)
        q08 = ["8. É perceptível uma visão mais negativa da velhice]?"]
        q08.insert(1,"8. Aspectos Positivo do Envelhecimento")
        q08.insert(2,"8. Aspectos Negativos do Envelhecimento")
        questions.insert(8, q08)
        questions.insert(9, "9. De modo geral o(a) senhor(a) está satisfeito com a vida?")
        questions.insert(10, "10. O(A) senhor(a) se sente triste com frequência?")
        questions.insert(11, "11. O(A) senhor(a) abandonou muitas das coisas que fazia ou gostava de fazer?")
        questions.insert(12, "12. O(A) senhor(a) tem medo que algum mal vá lhe acontecer?")
        questions.insert(13, "13. O(A) senhor(a) se sente impaciente e agitado(a) com frequência?")
        questions.insert(14, "14. O(A) senhor(a) tem dificuldade em se concentrar?")
        questions.insert(15, "15. O(A) senhor(a) tem problemas de visão?")
        questions.insert(16, "16. O(A) senhor(a) tem dificuldade de ouvir o que as pessoas falam?")
        questions.insert(17, "17. O(A) senhor(a) tem dificuldade para sentir o sabor dos alimentos?")
        questions.insert(18, "18. O(A) senhor(a) considera ruim o funcionamento dos seus sentidos?")
        questions.insert(19, "19. O(A) senhor(a) considera que o funcionamento dos seus sentidos afeta sua capacidade de interagir com \
                   outras pessoas?")
        questions.insert(20, "20. O(A) senhor(a) necessita de ajuda para Fazer compras?")
        questions.insert(21, "21. O(A) senhor(a) necessita de ajuda para Usar meios de transporte?")
        questions.insert(22, "22. O(A) senhor(a) necessita de ajuda para Preparar a própria comida?")
        questions.insert(23, "23. O(A) senhor(a) necessita de ajuda para Usar o telefone?")
        questions.insert(24, "24. O(A) senhor(a) necessita de ajuda para Vestir-se?")
        questions.insert(25, "25. O(A) senhor(a) necessita de ajuda para Tomar banho?")
        questions.insert(26, "26. O(A) senhor(a) acredita que está desnutrido?")
        questions.insert(27, "27. O(A) senhor(a) tem lesões na região bucal ou algum outro problema que provoque dificuldades de \
                   mastigação?")
        questions.insert(28, "28. O(A) senhor(a) faz menos de três refeições por dia?")
        questions.insert(29, "29. Nos últimos 3 meses, o(a) senhor(a) Diminuiu sua ingesta alimentar sem motivo?")
        questions.insert(30, "30. Nos últimos 3 meses, o(a) senhor(a) Perdeu peso sem motivo aparente?")
        questions.insert(31, "31. Nos últimos 3 meses passou por algum estresse psicológico, doença aguda ou internações?")
        questions.insert(32, "32. Índice de Massa Corporal (peso[kg]/ estatura[m2]) =  kg/m2) igual ou menor que 22 kg/m2?")
        questions.insert(33, "33. O(A) senhor(a) tem histórico familiar (1º grau) de DCV (infarto, derrama e/ou angina) ?")
        q34 = ["34. O(a) senhor(a) tem hipertensão arterial descontrolada? [Pontuar como sim quando PA auto referida for \
                   superior a 140/90 mmHg ou caso o(a) idoso(a) não saiba informar.]"]
        q34.insert(1,"34. Desconhece os valores da PA?")
        questions.insert(34, q34)
        q35=["35. O(A) senhor(a) tem diabetes? Se sim, está descontrolada? [Pontuar como sim quando glicemia em jejum \
           verificada em último exame for superior a 100 mg/dL, respectivamente, ou caso o(a) idoso(a) não saiba informar]."]
        q35.insert(1,"35. Desconhece os valores de glicemia?" )
        questions.insert(35,q35)
        q36=["36. O(A) senhor(a) tem colesterol alterado? [Pontuar como sim quando CT e HDL forem verificados em último \
                   exame como superior a 200 mg/dL e 60mg/dL, respectivamente, ou caso o(a) idoso(a) não saiba informar]."]
        q36.insert(1,"36. Desconhece os valores de CT e HDL?")
        questions.insert(36,q36)
        questions.insert(37, "37. O(A) senhor(a) fuma ou é ex-fumante?")
        questions.insert(38, "38. O(A) senhor(a) pratica mais de 150 minutos de exercícios físicos por semana?")
        questions.insert(39, "39. O(A) senhor(a) considera que sua alimentação é saudável?")
        q40 = ["40. Na última semana, o(a) senhor(a) ingeriu bebidas alcoólicas? Assinale a resposta equivalente, considerando as seguintes \
                   referências] Homens: Mais do que 14 doses de destilado (350 ml), 7 taças de vinho (2 litros) ou 14 latas\
                   de cerveja (5 litros) Mulheres: Mais do que 7 doses de destilado (175 ml), 3 e ½ taças de vinho (1 litro)\
                   ou 7 latas de cerveja (2,5 litros)"]
        q40.insert(1,"40. Quantidade de Alcool Ingerido")
        questions.insert(40,q40)
        questions.insert(41, "41. IMC para obesidade: ≥27 Kg/m2 [Verificar na questão 18]")
        q42 = ["42. Nos últimos 5 anos, algum médico ou outro profissional de saúde já disse que o(a) senhor(a) tem:"]
        q42.insert(1, "a) Doença do coração (angina, infarto ou ataque cardíaco)?")
        q42.insert(2, "b) Pressão alta/ hipertensão?")
        q42.insert(3, "c) Derrame/AVC/Isquemia?")
        q42.insert(4, "d) Diabetes Mellitus?")
        q42.insert(5, "e) Tumor maligno/ Câncer?")
        q42.insert(6, "f) Asma/Bronquite/Enfisema?")
        q42.insert(7, "g) Osteoporose?")
        q42.insert(8, "h) Reumatismo?")
        q42.insert(9, "i) Tendinite?")
        q42.insert(10, "j) Problemas de circulação?")
        q42.insert(11, "k) Depressão?")
        q42.insert(12, "l)Outra?")
        questions.insert(42, q42)

        q43 = ["43. O(A) senhor(a) tem algum dos seguintes problemas de saúde:"]
        q43.insert(1, "a) Dor de cabeça?")
        q43.insert(2, "b) Dor nas costas ou em outra parte do corpo?")
        q43.insert(3, "c) Alergia?")
        q43.insert(4, "d) Problema emocional?")
        q43.insert(5, "e) Tontura?")
        q43.insert(6, "f) Dificuldades para dormir?")
        q43.insert(7, "g) Incontinência urinária/perda de urina")
        q43.insert(8, "h)Outro?")
        questions.insert(43, q43)

        questions.insert(44, "44. Quantidade de diagnósticos (doenças):")
        questions.insert(45, "45. [Solicitar as bulas dos medicamentos utilizados pelo(a) senhor(a) e fazer registro legível dos \
                   respectivos nomes e classes terapêuticas]")
        questions.insert(46, "46. Nos últimos 6 meses, a quantidade de medicamentos que o(a) senhor(a) toma aumentou muito?")
        questions.insert(47, "47. O(A) senhor(a) sabe para que serve todos os seus medicamentos?")
        questions.insert(48, "48. Os medicamentos que o(a) senhor(a) faz uso foram prescritos por médicos diferentes?")
        questions.insert(49, "49. O(A) senhor(a) toma os medicamentos de acordo com as orientações médicas?")
        questions.insert(50, "50. O(A) senhor(a) alguma vez já deixou de tomar os medicamentos?")
        questions.insert(51, "51. O(A) senhor(a) tem o costume de tomar remédios por conta própria?")
        questions.insert(52, "52. Verificar na lista de medicamentos potencialmente inapropriados para idosos brasileiros \
                  (anexada ao PAGe) se o(a) idoso(a) toma algum dos medicamentos citados na mesma. [Caso sim, pontue ao lado\
                   e os deixe destacados na lista]")
        questions.insert(53, "53. Cálculo do risco para reações adversas. [Verifique as respostas das questões 30 e 38. Circule e cruze\
                   as informações na tabela abaixo. Em seguida, verifique os registros da questão 31 e assinale ao lado se \
                   o(a) idoso(a) utiliza uma quantidade de medicamentos superior ao valor indicado na tabela] ")
        q54=["54. O(A) senhor(a) tem: cônjuge?"]
        q54.insert(1,"54. O(A) senhor(a) tem: Mãe?" )
        q54.insert(2,"54. O(A) senhor(a) tem: Pai?" )
        q54.insert(3,"54. O(A) senhor(a) tem quantos irmãos?" )
        q54.insert(4,"54. O(A) senhor(a) tem quantos filhos?" )
        q54.insert(5,"54. O(A) senhor(a) tem quantos netos?" )
        questions.insert(54,q54)
        questions.insert(55, "55. O(A) senhor(a) encontra familiares e/ou amigos com frequência?")
        questions.insert(56, "56. O(A) senhor(a) participa de decisões importantes da sua família?")
        questions.insert(57, "57. O(A) senhor(a) se sente satisfeito(a) com o relacionamento afetivo que tem com os seus familiares?")
        questions.insert(58, "58. O(A) senhor(a) tem ajuda de alguém se precisar de dinheiro?")
        questions.insert(59, "59. O(A) senhor(a) pode contar com alguém para ajuda-lo(a) a resolver problemas?")
        questions.insert(60, "60. O(A) senhor(a) tem pessoas com quem possa se divertir e relaxar?")
        questions.insert(61, "61. O(A) senhor(a) participa de eventos sócio-culturais, tais como: peças de teatro, cinema, universidade\
                   aberta a terceira idade, centro de convivência, festas, ligados à religião, etc).")
        questions.insert(62, "62. O(A) senhor(a) é acompanhado regularmente por serviços de saúde?")
        questions.insert(63, "63. Na casa do(a) senhor(a):[Ambiente interno] Os móveis são estáveis?")
        questions.insert(64, "64. Na casa do(a) senhor(a): Há objetos e/ou tapetes soltos nas áreas de circulação?")
        questions.insert(65, "65. Na casa do(a) senhor(a): O piso é escorregadio (ex. encerado, molhado)?")
        questions.insert(66, "66. Na casa do(a) senhor(a): As escadas possuem corrimão em ambos os lados? (Colocar sim se a casa não tive escadas)")
        questions.insert(67, "67. Na casa do(a) senhor(a): As escadas/ degraus são iluminados adequadamente? (Colocar sim se a casa não tive escadas)")
        questions.insert(68, "68. Na casa do(a) senhor(a): Os degraus são adequados (tamanho, rebordos, largura e \
                   padronagem, etc)? (Colocar sim se a casa não tive escadas)")
        questions.insert(69, "69. Na casa do(a) senhor(a): Há tapetes antiderrapantes (fora e dentro box)?")
        questions.insert(70, "70. O(A) senhor(a) costuma: Subir em banquetas ou cadeiras para alcançar \
                   objetos altos?")
        questions.insert(71, "71. O(A) senhor(a) costuma:  Deixa as luzes apagadas quando se levanta à noite")
        questions.insert(72, "72. O(A) senhor(a) costuma: Utiliza calçados seguros e adequados (solado \
                   antiderrapante, bem ajustados e firmes no pé, sem saltos, etc)?")
        questions.insert(73,"73. O(A) senhor(a) está satisfeito com As calçadas do seu bairro são bem cuidadas \
                   (pavimentadas, lisas e sem buracos)?")
        questions.insert(74,"74. O(A) senhor(a) está satisfeito com o acesso ao transporte público no seu bairro?")
        questions.insert(75, "75. O(A) senhor(a) está satisfeito com o acesso ao comércio no seu bairro?")
        questions.insert(76, "76. O(A) senhor(a) está satisfeito com a facilidade e prazer em andar (a pé/ com \
                   cadeira de rodas/bengala/andador) no seu bairro?")
        questions.insert(77, "77. O(A) senhor(a) está satisfeito com o acesso à diversão no seu bairro (restaurantes,\
                   cinema, clubes, etc.)?")
        questions.insert(78, "78. O(A) senhor(a) está satisfeito com a segurança quanto à ameaça da criminalidade no\
                   seu bairro?")
        questions.insert(79, "79. O(A) senhor(a) tem medo de alguém próximo/do seu convívio?")
        questions.insert(80, "80. O(A) senhor(a) se sente só ou abandonado?")
        questions.insert(81, "81. Alguém tem falado com o(a) senhor(a) de forma que se sinta constrangido(a) ou desrespeitado(a)?")
        questions.insert(82, "82. Alguém tem agredido o(a) senhor(a) fisicamente?")
        questions.insert(83, "83. O(A) senhor(a) tem passado necessidade de roupas, alimentação, medicamentos ou outras?")
        questions.insert(84, "84. Alguém tem usado o dinheiro do(a) senhor(a) sem a sua autorização?")
        questions.insert(85, "85. Alguém do seu convívio já tocou o corpo do(a) senhor(a) sem o seu consentimento?")
        questions.insert(86, "86. O(A) senhor(a) está deixando de cuidar da sua própria saúde e/ou segurança?")
        q87 =["87. O(A) senhor(a) sofreu alguma queda nos últimos 12 meses?" ]
        q87.insert(1,"87. Se sofreu quedas, quantas?  [Se não, pontue também a resposta “não” na próxima questão e vá \
                      para a questão 90] [Se não, pule as próximas duas questões].")
        questions.insert(87, q87)
        q88 = ["88. O(A) senhor(a) sofreu alguma fratura decorrente destas quedas?"]
        q88.insert(1,"Se sim, quais?")
        questions.insert(88,q88)
        questions.insert(89, "89. O que o(a) senhor(a) estava fazendo quando sofreu essa(s) queda(s)? [Investigar atividade realizada, \
                   local, horário do dia, tipo de calçado, riscos ambientais etc]")
        questions.insert(90, "90. [Avaliação de força de MMII] – Peça ao(a) idoso(a) para levantar-se de uma cadeira sem ajuda. Assinale \
                   ao lado se o(a) idoso(a) conseguiu realizar a tarefa.")
        questions.insert(91, "91. [Avaliação de equilíbrio] Peça ao(a) idoso(a) para permanecer em pé em uma única perna, sem apoio dos\
                   membros superiores, durante 5 segundos. Assinale ao lado se o(a) idoso(a) consegue realizar a tarefa.")
        questions.insert(92, "92. Idade >75 anos [Ver em dados de identificação]")
        questions.insert(93, "93. Gênero feminino [Ver em dados de identificação]")
        questions.insert(94, "94. Alterações cognitivas [Pontuação negativa em Fluência Verbal em Funções Cognitivas]")
        questions.insert(95, "95. Comprometimento AVDs [Pontuação > 4 em Capacidade Funcional]")
        questions.insert(96, "96. Déficit Visual [Ver questão 15]")
        questions.insert(97, "97. Riscos domésticos [Ver questões 63 a 69]")
        questions.insert(98, "98. Riscos comportamentais [Ver questões 70 a 72]")
        questions.insert(99, "99. Inatividade [Ver questão 38]")
        questions.insert(100, "100. Acidente Vascular Encefálico prévio [Ver questão 42]")
        questions.insert(101, "101. Faz uso de medicações psicotrópicas, em especial benzodiazepínicos, OU uso contínuo de 5 ou mais \
                    medicações (polifarmácia) [Ver questão 45]")
        questions.insert(102, "102. Apresenta alguma das doenças a seguir: hipertensão tontura/ vertigem, Parkinson, amputação de \
                    membros inferiores, convulsões, artrite, osteoporose, incontinência, diabetes, neuropatia, hipotensão \
                    postural [Ver questões 42 e 43]")

        PROBLEMS =[
            ["N","Não"],
            ["E","Estresse Psicológico"],
            ["D", "Doença Aguda"],
            ["I", "Internação"],
            ["K", "Estresse Psicológico e Doença Aguda"],
            ["W", "Estresse Psicológico e Internação"],
            ["Y", "Doença Aguda e Internação"],
            ["Z", "Todos"]
        ]

        INCOME =[
            ["BPC","BPC"],
            ["Até um salário mínimo","Até um salário mínimo"],
            ["Entre 1 e 2 salários mínimos", "Entre 1 e 2 salários mínimos"],
            ["Entre 2 e 3 salários mínimos", "Entre 2 e 3 salários mínimos"],
            ["Entre 3 e 4 salários mínimos", "Entre 3 e 4 salários mínimos"],
            ["Entre 4 e 5 salários mínimos", "Entre 4 e 5 salários mínimos"],
            ["Entre 5 e 10 salários mínimos", "Entre 5 e 10 salários mínimos"],
            ["mais de 10 salários mínimos", "mais de 10 salários mínimos"]
        ]

        MARITALSTATUS =[
            ["Solteiro(a)","Solteiro(a)"],
            ["Casado(a)/União Estável","Casado(a)/União Estável"],
            ["Separado(a)/Divorciado(a)", "Separado(a)/Divorciado(a)"],
            ["Viúvo(a)", "Viúvo(a)"],
        ]

        SCHOOL =[
            ["analfabeto","analfabeto"],
            ["ensino fundamental (incompleto)","ensino fundamental (incompleto)"],
            ["ensino fundamental (completo)", "ensino fundamental (completo)"],
            ["ensino médio (incompleto)", "ensino médio (incompleto)"],
            ["ensino médio (completo)", "ensino médio (completo)"],
            ["ensino superior (incompleto)", "ensino superior (incompleto)"],
            ["ensino superior (completo)", "ensino superior (completo)"],
            ["ensino supeiror (com pós-graduação)", "ensino supeiror (com pós-graduação)"],
        ]


        LIVEWITH= [
            ["sozinho","sozinho"],
            ["somente com o cônjuge","somente com o cônjuge"],
            ["com o cônjuge e filhos", "com o cônjuge e filhos"],
            ["com o cônjuge, filhos e netos", "com o cônjuge, filhos e netos"],
            ["com o cônjuge e netos", "com o cônjuge e netos"],
            ["com filho(s)", "com filho(s)"],
            ["com filho(s) e netos", "com filho(s) e netos"],
            ["com netos", "com netos"],
            ["outros", "outros"],
        ]


