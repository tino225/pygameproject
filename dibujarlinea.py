import math
from vision import*
def draw_linee(start_pos, end_pos, parent, colisiones, width=1):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx = x2 - x1
    dy = y2 - y1
    distance = int(math.hypot(dx, dy))
    angle = math.atan2(dy, dx)

    for i in range(0, distance, 20):
        x = int(x1 + math.cos(angle) * i)
        y = int(y1 + math.sin(angle) * i)
        culo((x, y), parent, colisiones)
    
    # Si el ancho es mayor que 1, dibujar instancias adicionales
    if width > 1:
        for offset in range(1, width):
            for i in range(distance):
                x_offset = int(x1 + math.cos(angle) * i)
                y_offset = int(y1 + math.sin(angle) * i)
                
                # Agregar instancias arriba y abajo de la línea principal
                culo((x_offset, y_offset + offset), parent, colisiones)
                culo((x_offset, y_offset - offset), parent, colisiones)



def draw_line(start_pos, end_pos, parent, colisiones, width=1):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx = x2 - x1
    dy = y2 - y1
    distance = int(math.hypot(dx, dy))
    angle = math.atan2(dy, dx)

    for i in range(0, distance, 20):
        x = int(x1 + math.cos(angle) * i)
        y = int(y1 + math.sin(angle) * i)
        culo((x, y), parent, colisiones)
    
    # Si el ancho es mayor que 1, dibujar instancias adicionales
    if width > 1:
        for offset in range(1, width):
            for i in range(distance):
                x_offset = int(x1 + math.cos(angle) * i)
                y_offset = int(y1 + math.sin(angle) * i)
                
                # Agregar instancias arriba y abajo de la línea principal
                culo((x_offset, y_offset + offset), parent, colisiones)
                culo((x_offset, y_offset - offset), parent, colisiones)

