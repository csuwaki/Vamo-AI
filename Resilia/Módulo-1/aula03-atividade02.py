nome = "Lis"
animal_de_estimacao = "Afonso"
comida_favorita = "a baiana, com muito cheiro verde e dendê"
pais_que_quer_visitar = "Peru"
idade = 27
altura = 1.70

texto = "🔅🔅🔅 Mini Bio 🔅🔅🔅\nOlá, eu sou {nome}!👋\nTenho {idade} anos e {altura:.2f} m de altura.\nA minha comida favorita é {comida} e um país que tenho muita vontade de visitar é o {pais}.\nAinda não tenho um pet, mas meu sonho é ter um cachorro caramelo cujo nome será {pet}.🐶" 

print(texto.format(nome = nome, pet = animal_de_estimacao, comida = comida_favorita,
      pais = pais_que_quer_visitar, idade = idade, altura = altura))