import base64
from io import BytesIO
import matplotlib_inline


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Title')
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('XLABEL')
    plt.ylabel('YLABEL')
    plt.tight_layout
    graph = get_graph()
    return graph