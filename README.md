# company-hero
test company hero

# Requisitos Funcionais

- Seu serviço deve ser acessível através de uma API
- Seu serviço deve aceitar o nome de uma cidade como parâmetro e, a partir disso, retornar uma playlist de acordo com a temperatura atual na cidade fornecida
- Se a temperatura:
    - Estiver acima de 25ºC, o serviço deverá sugerir músicas Pop
    - Estiver entre 10ºC e 25ºC, o serviço deverá sugerir músicas de Rock
    - Estiver abaixo de 10ºC, o serviço deverá sugerir músicas clássicas

# Requisitos Não Funcionais

O seu serviço deve ser construído com atenção aos seguintes aspectos:

- Latência
- Resiliência
- Segurança
- Escalabilidade

# Tecnologias Utilizadas

- Justificativa de padrão de API: A combinação de AWS Lambda com AWS API Gateway foi escolhida por permitir escalabilidade automática, reduzir custos (pagamento apenas por uso), simplificar a implementação de APIs, diminuir a manutenção de infraestrutura e integrar-se facilmente com outros serviços AWS. Essa abordagem serverless é ideal para criar serviços eficientes e de fácil gestão.

- Justificativa de linguagem de programação: A escolha de Python para o serviço pode ser justificada pela sua facilidade de uso, com uma sintaxe simples e clara, que acelera o desenvolvimento e a manutenção do código. Além disso, Python oferece uma vasta gama de bibliotecas e ferramentas que otimizam o processo de desenvolvimento. Sua popularidade garante uma comunidade ativa, facilitando o suporte e a resolução de problemas. Por fim, Python é totalmente compatível com AWS Lambda, garantindo uma integração eficiente e desempenho otimizado.

- Uso de serviços terceiros: No projeto, o uso da API de Weather para obter a temperatura da cidade e da API do Spotify para buscar playlists foi escolhido por diversas razões. A API de Weather permite acessar dados meteorológicos precisos e atualizados, essencial para funcionalidades dependentes das condições climáticas. Já a API do Spotify fornece um acesso eficiente a uma vasta coleção de playlists, enriquecendo a aplicação com opções musicais diversificadas. Ambas as APIs são bem documentadas, confiáveis e amplamente usadas, garantindo robustez e facilidade na integração com o serviço.

# Utilização

https://documenter.getpostman.com/view/1717476/2sA3XPBgqh#f6e28b58-6424-4ca7-a856-7a07839dd8b9

# Documentação

## Arquitetura de código

A escolha pela arquitetura clean no projeto visa melhorar a manutenibilidade, escalabilidade e testabilidade do código. Essa abordagem organiza o código em camadas bem definidas, separando responsabilidades e promovendo o princípio da separação de preocupações. Isso facilita a compreensão e a modificação do código sem afetar outras partes do sistema. Além disso, permite uma integração mais simples com serviços externos e a substituição de componentes internos sem grandes refatorações, resultando em um desenvolvimento mais eficiente e sustentável a longo prazo.

/company-hero
|-- handler.py -> handler main da lambda
|-- dependencies.py -> Injeção de dependências
|   |-- /application -> Possui todos os usecases(endpoints) para atender a API
|   |-- /config -> Configurações globais do projeto, como chaves de API e URLs externas
|   |-- /domain -> Regra de négocio entidades e interfaces paraa conversar com repositório
|   |-- /external -> Comunicação com base de dados externas
|   |-- /infra -> implementação de Models e Repositorios
|   |-- /services -> Serviços de pacotes utilizados (utilizando somente requests para API)
|   |-- /tests -> Testes unitários e de integração
|-- requirements.txt -> Pacotes utilizados do Python
|-- serverless.yml -> Arquivo de configuração para utilização do serviço de deploy escolhido (Infra as Code)
|-- README.md
