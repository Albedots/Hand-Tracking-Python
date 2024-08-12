# HandTracking using CV and AI
Projeto criado na **Semana do Python** da **Empowerdata**. O programa realiza a captura de imagem da sua webcam varias vezes por segundo (reproduzindo um vídeo) e ira realizar o trackeamento visual das suas mãos quando forem mostradas a câmera OBS: O tracking só ira ser realizado quando as mãos forem mostradas nitidamente a câmera e o script tiver 80% de certeza que capturou suas mãos.

## Funcionalidades
- **Captura de tela**: O script ira tirar varias fotos por segundo, usando a camera do dispositivo, gerando um video.
- **Tracking**: Apos a analise e fidelidade das imagens o script ira trackear visualmente suas mãos quando tiver 80% de certeza de certeza que a imagem contém alguma mão. OBS: Funciona com no maximo 2 mãos.

## Dependências
- **Interpretador Python**
- **Bibliotecas**: opencv-python, mediapipe, cvzone

## Instalação
- Clone o repositório
- Certifique-se de ter o **Python** instalado em seu sistema e/ou **Interpretador** Python. Projeto testado na versão 3.x do Python.
- Instale as bibliotecas necessárias usado o `pip`
```bash
    pip install opencv-python mediapipe cvzone
```
- Ou instale as dependências do `requirements.txt` usando:
```bash
    pip install -r requirements.txt
```

## Uso
Execulte o arquivo `main.py`, usando o interpretador **Python** ou um **IDE**

## Contribuição
Sinta-se a vontade para contribuir ao projeto, crie um fork no seu perfil e envie um pull request com sua melhorias e/ou correções.