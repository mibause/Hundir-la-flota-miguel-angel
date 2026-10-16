# Hundir la flota

Juego de Hundir la flota de 1 jugador vs la máquina, hecho en Python.

## Objetivo

Gana quien encuentre y hunda primero todos los barcos del oponente.

## Tablero y símbolos

El tablero tiene 10 filas y 10 columnas. Las coordenadas empiezan en 0 y terminan en 9.

- `_`: casilla vacía o todavía no disparada.
- `O`: parte de un barco.
- `X`: Barco tocado.
- `A`: disparo al agua.

## Flota y turnos

Cada jugador tiene seis barcos: tres de tamaño 2, dos de tamaño 3 y uno de tamaño 4. Los barcos se colocan al azar, en horizontal o vertical.

En cada ronda, primero eliges una fila y una columna para disparar al tablero de la máquina. Después, la máquina dispara a una casilla de tu tablero que todavía no haya elegido. La partida termina cuando todos los barcos de uno de los tableros han sido alcanzados.

## Cómo jugar

Desde la carpeta del proyecto, ejecuta:

```powershell
python Archivo_python.py
```

Cuando el programa lo pida, introduce primero la fila y luego la columna.
