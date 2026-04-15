import streamlit as st

st.set_page_config(page_title="PORTAFOLIO VICTOR RIVAS", layout="centered")

if "actividades" not in st.session_state:
    st.session_state.actividades = []

# MENÚ


menu = st.sidebar.radio(
    "Menu:",
    ["Víctor, Rivas Jáuregui", "Proyectos",]
)
st.sidebar.markdown(
    '<hr style="border: 0.5px solid #cccccc; margin: 5px 0;">',
    unsafe_allow_html=True
)


# HOME

if menu == "Víctor, Rivas Jáuregui":

    st.title("PORTAFOLIO DE PROYECTOS") 
    linkedin_url = "https://www.linkedin.com/in/victor-benjamin-rivas-jauregui-832a5b315/" 
    st.markdown(
        f'<a href="{linkedin_url}" target="_blank">'
        '<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20"> Víctor Benjamín Rivas Jáuregui'
        '</a>',
        unsafe_allow_html=True
    )
    st.image("CV.png", use_container_width=True)

    st.write("**Tecnologías utilizadas:**")
    st.write("🟢 Power BI")
    st.write("🟢 Python")
    st.write("🟢 Streamlit")

# EJERCICIO 1


elif menu == "Proyectos":

    st.title("📝Dashboard Comercial de Ventas")
    
    st.write("""Este dashboard permite analizar el desempeño comercial a través del tiempo, visualizando ventas en soles y unidades. Incluye filtros por canal, modelo y periodo para facilitar la exploración de la información.

Presenta indicadores clave como ventas, descuentos, costos, utilidad y margen, permitiendo evaluar la rentabilidad y apoyar la toma de decisiones.
             
*Datos simulados con fines demostrativos.*""")
    
    linkedin_url = "https://app.powerbi.com/view?r=eyJrIjoiYzk4YjQ5YzktYzEzNC00ZDIyLWE1NTYtNzhjMDQ0MjE2ZjljIiwidCI6IjI3YjI1ZDUyLWM1ZWMtNDVkNC1iYmQ0LTYyMjJlMzk2NGEwOCIsImMiOjR9" 
    st.markdown(
        f'➡️<a href="{linkedin_url}" target="_blank">'
        '<img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" width="20"> Dashboard Comercial de Ventas'
        '</a>',
        unsafe_allow_html=True
    )

    st.title("📝Dashboard Hoja de Ruta")
    
    st.write("""Dashboard enfocado en la gestión de la hoja de ruta comercial, que permite monitorear visitas y llamadas realizadas por los asesores. Facilita la evaluación del rendimiento y el cálculo de comisiones.

*Datos simulados con fines demostrativos.*""")
    
    linkedin_url = "https://app.powerbi.com/view?r=eyJrIjoiYzY4MDRlYTAtOTc5Yy00MjVmLWFjZTktYTUxY2ViMjUyZTkzIiwidCI6IjI3YjI1ZDUyLWM1ZWMtNDVkNC1iYmQ0LTYyMjJlMzk2NGEwOCIsImMiOjR9" 
    st.markdown(
        f'➡️<a href="{linkedin_url}" target="_blank">'
        '<img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" width="20"> Dashboard Hoja de Ruta'
        '</a>',
        unsafe_allow_html=True
    )    

    st.title("📝Dashboard de Fallas")
    
    st.write("""Dashboard enfocado en el análisis de incidencias de garantías, que permite visualizar fallas, devoluciones, canjes y anulaciones por marca, periodo y modelo. Facilita la identificación de tendencias y el control de la calidad de los productos.

*Datos simulados con fines demostrativos.*""")
    
    linkedin_url = "https://app.powerbi.com/view?r=eyJrIjoiZTRmMTI4MzQtZmRmNy00MGFhLWJmM2UtZDc5MTU4MDRmNTJkIiwidCI6IjI3YjI1ZDUyLWM1ZWMtNDVkNC1iYmQ0LTYyMjJlMzk2NGEwOCIsImMiOjR9" 
    st.markdown(
        f'➡️<a href="{linkedin_url}" target="_blank">'
        '<img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" width="20"> Dashboard Hoja de Fallas'
        '</a>',
        unsafe_allow_html=True
    )    

