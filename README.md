# Pixel Runner

Pixel Runner es un juego de plataformas desarrollado utilizando Pygame. El objetivo es controlar un personaje que debe esquivar obstáculos y recolectar puntos mientras se mueve por el escenario. El juego utiliza sprites, animaciones y detección de colisiones para crear una experiencia fluida.

## Requisitos

- Python 3.x
- Pygame (`pip install pygame`)
- Biblioteca asyncio (incluida en Python 3.5+)

## Archivos necesarios

Asegúrate de tener los siguientes recursos en los directorios especificados:

### Directorios:
- **graphics/**
  - `Sky.png`: Fondo del cielo.
  - `ground.png`: Imagen del suelo.
  - **Player/**: Contiene sprites para el jugador:
    - `player_walk_1.png`
    - `player_walk_2.png`
    - `jump.png`
    - `player_stand.png`
  - **Fly/**: Sprites para los enemigos voladores:
    - `Fly1.png`
    - `Fly2.png`
  
- **audio/** 
  - `jump.mp3`: Sonido para el salto.
  - `music.wav`: Música de fondo del juego.

- **font/**
  - `Pixeltype.ttf`: Fuente utilizada para mostrar el puntaje y otros textos.

## Características

### 1. **Jugador**
El jugador es controlado por el teclado y tiene animaciones para caminar y saltar. Utiliza gravedad y detección de colisiones para interactuar con el entorno.

- **Movimiento**: El personaje se mueve usando las teclas de espacio para saltar.
- **Gravedad**: Se aplica un efecto de gravedad, y el jugador solo puede saltar cuando está en el suelo.
- **Sonido**: Un efecto de sonido se reproduce al saltar.

### 2. **Obstáculos**
El juego cuenta con enemigos de tipo `snail` y `fly`, cada uno con su propia animación y comportamiento.

- Los obstáculos se generan aleatoriamente a intervalos regulares.
- Los enemigos se mueven de derecha a izquierda, y desaparecen cuando salen de la pantalla.
- Si el jugador colisiona con un obstáculo, el juego termina.

### 3. **Puntuación**
El juego registra el tiempo que el jugador sobrevive, que es la puntuación. Se muestra en la parte superior de la pantalla.

### 4. **Pantalla de inicio y final**
- **Pantalla de inicio**: Al iniciar el juego, se muestra una pantalla con un mensaje para comenzar el juego.
- **Pantalla de fin**: Cuando el jugador choca con un obstáculo, se muestra la puntuación final y el jugador puede reiniciar presionando cualquier tecla.

## Instalación y ejecución

1. Instala las dependencias de Pygame:

    ```bash
    pip install pygame
    ```

2. Coloca los archivos de recursos (imágenes, sonidos, y fuente) en los directorios correspondientes.

3. Ejecuta el juego:

    ```bash
    python main.py
    ```

## Estructura del código

### Clases principales:

- **Player**: Clase que representa al jugador, maneja las entradas del teclado, la gravedad y las animaciones.
- **Obstacle**: Clase que define los obstáculos, con diferentes tipos (fly y snail) y su comportamiento en pantalla.

### Funciones:

- **displayScore()**: Muestra la puntuación actual en la pantalla.
- **collisionSprite()**: Detecta colisiones entre el jugador y los obstáculos.

### Eventos:

- **obstacle_timer**: Genera nuevos obstáculos en la pantalla a intervalos regulares.
- **snail_animation_timer** y **fly_animation_timer**: Controlan las animaciones de los enemigos.

## Controles

- **Tecla Espacio**: Hace que el jugador salte.
- **Cualquier tecla**: Reinicia el juego cuando termina.
