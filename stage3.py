def classificar_violencia(target_type, action_type, hallmark, repeticao=False):

    resultado = []

    #Regra 1: HS
    if target_type == "PROTECTED_GROUP" and hallmark == "DEHUMANIZATION":
        resultado.append ("Hate Speech")
    
    #Regra 2: DS
    if hallmark in ["DEHUMANIZATION", "GLORIFICATION_OF_VIOLENCE", "ACCUSATION_IN_MIRROR"]:
        resultado.append("Dangerous Speech")

    #Regra 3: VA
    if target_type == "INDIVIDUAL_REFERENCE" and action_type == "INSULT":
        resultado.append ("Verbal Agression")

    #Regra 4: TS
    if action_type == "INSULT" and target_type != "PROTECTED_GROUP":
        resultado.append("Toxic Speech")

    #Regra 5: Repetição
    if repeticao and target_type == "INDIVIDUAL_REFERENCE":
        resultado.append("Cyberbullying")

    # Se nenhuma regra bater:
    if not resultado:
        resultado.append("Benign")
    
    return resultado

exemplos = [
    { "texto": "Gays são o que as vacas deixam para trás...",
        "target_type": "PROTECTED_GROUP",
        "action_type": "DELEGITIMIZATION",
        "hallmark": "DEHUMANIZATION"
        },
        {"texto": "@user vc não entende porra nenhuma mesmo!!!!",
     "target_type": "INDIVIDUAL_REFERENCE",
     "action_type": "INSULT",
     "hallmark": "SANCTION_SPEECH"},

    {"texto": "Eu tenho pena de você não ter sido da época do grande General Pinochet",
     "target_type": "INDIVIDUAL_REFERENCE",
     "action_type": "GLORIFICATION_OF_VIOLENCE",
     "hallmark": "DEHUMANIZATION"},

    {"texto": "As conquistas das mulheres em esportes muitas vezes são subestimadas",
     "target_type": "PROTECTED_GROUP",
     "action_type": "PRAISE",
     "hallmark": "NONE"},

     {"texto": "@maria sua idiota, já falei isso mil vezes!!!!",
     "target_type": "INDIVIDUAL_REFERENCE",
     "action_type": "INSULT",
     "hallmark": "SANCTION_SPEECH",
     "repeticao": True},
]

for ex in exemplos:
    resultado = classificar_violencia(ex["target_type"], ex["action_type"], ex["hallmark"], ex.get("repeticao", False))
    print(f"Texto: {ex['texto']}")
    print(f"Classificação: {resultado}\n")