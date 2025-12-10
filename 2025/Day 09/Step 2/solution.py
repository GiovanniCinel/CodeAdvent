# Questa soluzione l'ho ottenuta modificando una mia idea con Gemini in quanto la mia idea non era sufficientemente efficente,
# dunque viste le dimensioni di input con il mio hardware non riuscivo a raggiungere un risultato. Ottimizzando con Gemini il codice
# richiede un tempo accettabile per arrivare al risultato.


import sys

def solve_theater_from_file(filename):
    points = []
    
    # Lettura del file input.txt
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if ',' in line:
                    x, y = map(int, line.split(','))
                    points.append((x, y))
    except FileNotFoundError:
        print(f"Errore: Il file '{filename}' non è stato trovato.")
        return

    n = len(points)
    if n < 2:
        print("Errore: Non ci sono abbastanza punti nel file.")
        return

    # Costruzione degli spigoli (Edges) del poligono
    # Ogni punto è collegato al successivo, l'ultimo si collega al primo
    edges = []
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        edges.append((p1, p2))

    max_area = 0

    # Iterazione su tutte le coppie di punti rossi (O(N^2))
    # N = 500 => ~125.000 coppie, molto veloce per Python
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            
            x1, y1 = p1
            x2, y2 = p2
            
            # Calcolo coordinate del rettangolo
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            
            # Calcolo area (inclusiva delle tessere bordo)
            width = max_x - min_x + 1
            height = max_y - min_y + 1
            area = width * height
            
            # OTTIMIZZAZIONE:
            # Se l'area non supera il record attuale, non facciamo i calcoli geometrici costosi
            if area <= max_area:
                continue

            # --- VERIFICA 1: Intersezioni ---
            # Un rettangolo valido NON deve essere attraversato da nessun muro verde.
            # I bordi del rettangolo possono toccare i muri, ma i muri non possono
            # passare "in mezzo" al rettangolo.
            intersects_interior = False
            for edge in edges:
                (ex1, ey1), (ex2, ey2) = edge
                
                # Normalizziamo le coordinate dell'edge
                e_min_x, e_max_x = min(ex1, ex2), max(ex1, ex2)
                e_min_y, e_max_y = min(ey1, ey2), max(ey1, ey2)
                
                if ex1 == ex2: # Spigolo Verticale del poligono
                    # Controlla se la X dell'edge è STRETTAMENTE tra le X del rettangolo
                    if min_x < ex1 < max_x:
                        # E se c'è sovrapposizione verticale
                        if max(min_y, e_min_y) < min(max_y, e_max_y):
                            intersects_interior = True
                            break
                else: # Spigolo Orizzontale del poligono
                    # Controlla se la Y dell'edge è STRETTAMENTE tra le Y del rettangolo
                    if min_y < ey1 < max_y:
                        # E se c'è sovrapposizione orizzontale
                        if max(min_x, e_min_x) < min(max_x, e_max_x):
                            intersects_interior = True
                            break
            
            if intersects_interior:
                continue

            # --- VERIFICA 2: Point in Polygon (Ray Casting) ---
            # Anche se non interseca i muri, il rettangolo potrebbe essere totalmente fuori
            # (es. nello spazio vuoto di una forma a "U").
            # Verifichiamo se il centro del rettangolo è dentro il poligono.
            
            mid_x = (min_x + max_x) / 2.0
            mid_y = (min_y + max_y) / 2.0
            
            inside = False
            for edge in edges:
                (ex1, ey1), (ex2, ey2) = edge
                
                # Ray Casting orizzontale verso destra
                # Ci interessano solo i lati non orizzontali del poligono
                if ey1 != ey2:
                    # Verifica se la Y del punto interseca il range Y dell'edge
                    if (ey1 > mid_y) != (ey2 > mid_y):
                        # Calcola intersezione X
                        # Per linee verticali (ex1==ex2) è semplice, altrimenti calcolo pendenza
                        if ex1 == ex2:
                            intersect_x = ex1
                        else:
                            # Formula retta passante per 2 punti
                            intersect_x = (ex2 - ex1) * (mid_y - ey1) / (ey2 - ey1) + ex1
                            
                        if mid_x < intersect_x:
                            inside = not inside
            
            if inside:
                max_area = area

    print(f"L'area del rettangolo valido più grande è: {max_area}")

if __name__ == "__main__":
    solve_theater_from_file("input.txt")