import io

def crear_html_agenda(lista_principal):
    # Crear el contenido HTML
    contenido_html = '''
    <!DOCTYPE html>
    <html>
    <head>
      <title>Agenda de la Reunión</title>
    </head>
    <body>
      <h1>Agenda</h1>
      <h2>Participantes</h2>
      <ul>
    '''

    # Agregar los participantes a la lista
    for participante in lista_principal[1]:
        contenido_html += f'    <li>{participante}</li>\n'

    # Continuar con el contenido HTML
    contenido_html += '''
      </ul>
      <h2>Apartados</h2>
      <ol>
    '''

    # Agregar los apartados a la lista numerada
    for apartado in lista_principal[2]:
        contenido_html += f'    <li>{apartado}</li>\n'

    # Continuar con el contenido HTML
    contenido_html += '''
      </ol>
      <h2>Puntos</h2>
      <ul>
    '''

    # Agregar los puntos a la lista
    for punto in lista_principal[3]:
        contenido_html += f'    <li>{punto}</li>\n'

    # Continuar con el contenido HTML
    contenido_html += '''
      </ul>
      <h2>Discusiones</h2>
      <ol>
    '''

    # Agregar las discusiones a la lista numerada
    for discusion in lista_principal[4]:
        contenido_html += f'    <li>{discusion}</li>\n'

    # Finalizar el contenido HTML
    contenido_html += '''
      </ol>
    </body>
    </html>
    '''

    # Crear el archivo HTML
    with io.open('archivo.html', 'w', encoding='utf-8') as archivo:
        archivo.write(contenido_html)


    print('El archivo HTML se ha creado correctamente.')
