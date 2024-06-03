from django.shortcuts import render
import plotly.graph_objs as go

def index(request):
    return render(request, 'index.html', {})


def chart_view(request):
    # Datos para el gráfico
    x_data = [1, 2, 3, 4, 5]
    y_data = [10, 15, 13, 18, 20]

    # Crear el gráfico
    fig = go.Figure(data=go.Scatter(x=x_data, y=y_data))

    # Configurar el diseño del gráfico
    fig.update_layout(title='Gráfico de Ejemplo', xaxis_title='Eje X', yaxis_title='Eje Y')

    # Convertir el gráfico a HTML
    graph_html = fig.to_html(full_html=False, default_height=500, default_width=700)

    # Renderizar la plantilla con el gráfico
    return render(request, 'chart.html', {'graph': graph_html})