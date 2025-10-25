Hoiaaa, para ejecutar este programa necesitaras tener installada la version mas reciente de python, tienes que añadirla al PATH y permitir instalar como administrador
para windows 64 bits:
https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe

cuando ya tengas instalado python abre la terminal como administrador y copia el siguiente código para instalar openai:

pip install openai==0.28

tiene que ser la version 0.28 porque estamos trabajando con gpt 3.5 turbo y las versiones mas recientes ya no lo admiten

Tambien instalaremos la libreria de streamlit

pip install streamlit