import streamlit as st
import pathlib
from PIL import Image
import google.generativeai as genai

# Configure the API key directly in the script
API_KEY = 'AIzaSyAx7mN0Nb34bZWyjcCBIZx6PTYicyAv95g'
genai.configure(api_key=API_KEY)

# Generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Safety settings
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

# Model name
MODEL_NAME = "gemini-1.5-pro-latest"

# Framework selection (e.g., Tailwind, Bootstrap, etc.)
framework = "Regular CSS use flex grid etc"  # Change this to "Bootstrap" or any other framework as needed

# Create the model
model = genai.GenerativeModel(
    model_name=MODEL_NAME,
    safety_settings=safety_settings,
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(history=[])

# Function to send a message to the model
def send_message_to_model(message, image_path):
    image_input = {
        'mime_type': 'image/jpeg',
        'data': pathlib.Path(image_path).read_bytes()
    }
    response = chat_session.send_message([message, image_input])
    return response.text

# Streamlit app
def main():
    st.title("Gemini 1.5 Pro, UI to Code 👨‍💻 ")
    st.subheader('Hecho por ❤️ by Johan Morales')

    uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            # Load and display the image
            image = Image.open(uploaded_file)
            st.image(image, caption='Imagen subida.', use_column_width=True)

            # Convert image to RGB mode if it has an alpha channel
            if image.mode == 'RGBA':
                image = image.convert('RGB')

            # Save the uploaded image temporarily
            temp_image_path = pathlib.Path("temp_image.jpg")
            image.save(temp_image_path, format="JPEG")

            # Generate UI description
            if st.button("Code UI"):
                st.write("🧑‍💻 Mirando tu UI...")
                prompt = "Describa esta interfaz de usuario con todo detalle. Cuando hagas referencia a un elemento de la interfaz de usuario, escribe su nombre y su cuadro delimitador en el formato: [nombre del objeto (y_min, x_min, y_max, x_max)]. Describe también el color de los elementos."
                description = send_message_to_model(prompt, temp_image_path)
                st.write(description)

                # Refine the description
                st.write("🔍 Afinando la descripción con la comparación visual...")
                refine_prompt = f"Compare los elementos de interfaz de usuario descritos con la imagen proporcionada e identifique los elementos que falten o las imprecisiones. Describa también el color de los elementos. Proporcione una descripción refinada y precisa de los elementos de la interfaz de usuario basándose en esta comparación. Esta es la descripción inicial: {description}"
                refined_description = send_message_to_model(refine_prompt, temp_image_path)
                st.write(refined_description)

                # Generate HTML
                st.write("🛠️ Generando sitio web...")
                html_prompt = f"Cree un archivo HTML basado en la siguiente descripción de UI, utilizando los elementos de UI descritos en la respuesta anterior. Incluya {framework} CSS en el archivo HTML para dar estilo a los elementos. Asegúrese de que los colores utilizados son los mismos que los de la interfaz de usuario original. La interfaz de usuario debe ser adaptable y orientada a dispositivos móviles, y debe ser lo más parecida posible a la interfaz de usuario original. No incluyas explicaciones ni comentarios. Evita usar ``html. y ``` al final. SÓLO devuelva el código HTML con CSS en línea. Esta es la descripción refinada: {refined_description}"
                initial_html = send_message_to_model(html_prompt, temp_image_path)
                st.code(initial_html, language='html')

                # Refine HTML
                st.write("🔧 Refinando sitio web...")
                refine_html_prompt = f"Valide el siguiente código HTML basándose en la descripción y la imagen de la interfaz de usuario y proporcione una versión refinada del código HTML con {framework} CSS que mejore la precisión, la capacidad de respuesta y la adherencia al diseño original. SÓLO devuelva el código HTML refinado con CSS en línea. Evite utilizar ```html. y ``` al final. Aquí está el HTML inicial: {initial_html}"
                refined_html = send_message_to_model(refine_html_prompt, temp_image_path)
                st.code(refined_html, language='html')

                # Save the refined HTML to a file
                with open("index.html", "w") as file:
                    file.write(refined_html)
                st.success("Se ha creado el archivo HTML 'index.html'.")

                # Provide download link for HTML
                st.download_button(label="Descargar HTML", data=refined_html, file_name="index.html", mime="text/html")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
