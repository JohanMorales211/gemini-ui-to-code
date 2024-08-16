# Gemini UI to Code Streamlit App

**Convierte tus diseños UI en código HTML funcional con la potencia de la IA de Google Gemini! 🚀**

Esta aplicación Streamlit, impulsada por la avanzada tecnología de Google Gemini, te permite transformar imágenes de diseños de interfaz de usuario en código HTML limpio y eficiente. Olvídate de la tediosa tarea de traducir manualmente tus diseños a código, ¡deja que la IA haga el trabajo pesado por ti! 🤖

![Imagen de Google Gemini](https://zenuradio.com/wp-content/uploads/2024/05/Gemini-scaled-1.jpg)

## Características Clave ✨

* **Conversión Inteligente:** Analiza imágenes de diseños UI y genera el código HTML correspondiente.
* **Personalización:** Selecciona el modelo Gemini que mejor se adapte a tus necesidades.
* **Soporte para Frameworks CSS:**  Indica a Gemini que utilice el framework CSS de tu preferencia (ej. Tailwind, Bootstrap).
* **Descripción Detallada:** Obtiene una descripción completa de la UI, incluyendo nombres de elementos,  cuadros delimitadores y colores.
* **Refinamiento Inteligente:** Gemini refina la descripción y el código HTML generado para una mayor precisión y  fidelidad al diseño original.
* **Adaptabilidad:** Genera código HTML adaptable y optimizado para dispositivos móviles.
* **Descarga Sencilla:** Descarga el código HTML generado con un solo clic.

## Instalación 🛠️

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

## Ejecutando la Aplicación ▶️

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
python -m streamlit run app.py
```

## Configuración ⚙️

Antes de ejecutar la aplicación, necesitas configurar tu clave API de Google Gemini en el archivo `app.py`. 

1. **Crea un archivo `.env`** en la misma carpeta que `app.py`.
2. **Agrega la siguiente línea al archivo `.env`**:

   ```
   API_KEY=tu_clave_api_de_google
   ```

   Reemplaza `tu_clave_api_de_google` con tu clave API real.

También puedes seleccionar el modelo Gemini que deseas utilizar e incluso indicarle a Gemini que utilice un framework CSS específico.

## Cómo Funciona 🔄

1. **Sube tu Imagen:**  Selecciona la imagen de tu diseño UI que deseas convertir a código.
2. **Generar Código:** Haz clic en el botón "Code UI".  La IA analizará la imagen y generará una descripción detallada de la interfaz, seguida del código HTML.
3. **Refinamiento Automático:** La IA  refinará la descripción y el código HTML para una mayor precisión.
4. **Descarga tu HTML:** Descarga el código HTML final, listo para ser utilizado en tu proyecto.

## Dependencias 📦

* **Streamlit:**  Framework para crear aplicaciones web interactivas para Machine Learning y Data Science.
* **Pillow (PIL):**  Librería para procesamiento de imágenes.
* **google-generativeai:** Librería para acceder a la API de Google Gemini.

## Ejemplo de Código HTML Generado 📄

El código HTML generado incluye CSS en línea para un estilo visual similar al diseño original. Aquí tienes un ejemplo:

```html
<!DOCTYPE html>
<html lang="en">
... (Código HTML completo) ...
</html>
```

---

<div align="center">
  <p>Creado con ❤️ por <a href="https://github.com/JohanMorales211" target="_blank">Johan Morales</a></p>
  <img src="https://media.giphy.com/media/SWoSkN6DxTszq/giphy.gif" width="200" alt="Animación de código">
</div>

---
```
