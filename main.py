import streamlit as st
from icalendar import Calendar, Event
from datetime import datetime


# crear la aplicación de Streamlit
st.set_page_config(page_title="Eventastic", page_icon="📆")

st.title('Eventastic! 📆')
st.markdown('*Crea eventos para los miembros de tu comunidad y boostea su productividad!*')

# obtener los detalles del evento del usuario

now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

text_col, date_col = st.columns(2)

with text_col:

    name = st.text_input('Nombre del evento')
    desc = st.text_area('Descripción del evento', height=404)

with date_col:

    start_date = st.date_input('Fecha de inicio del evento')
    start_time = st.time_input('Hora de inicio del evento',now)
    end_date = st.date_input('Fecha de fin del evento')
    end_time = st.time_input('Hora de fin del evento',now)
    loc = st.text_input('Ubicación del evento')
    link = st.text_input('Enlace del evento')

# convertir las fechas a objetos datetime
start = datetime.combine(start_date, start_time)
end = datetime.combine(end_date, end_time)

# crear el objeto evento
evento = Event()
evento.add('summary', name)
evento.add('description', desc)
evento.add('location', loc)
evento.add('url', link)
evento.add('dtstart', start)
evento.add('dtend', end)

# crear el objeto calendario y agregar el evento
calendario = Calendar()
calendario.add_component(evento)

# obtener el archivo .ics como bytes
archivo_ics = calendario.to_ical()

# agregar un botón para descargar el archivo .ics
st.download_button(label='Descargar evento',
                   data=archivo_ics,
                   file_name='evento.ics',
                   mime='text/calendar')