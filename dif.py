from pathlib import Path

path = Path("components/player/controls/Trickplay/Trickplay.bs")
text = path.read_text()

text = text.replace(
"""' Fixed preview box (object-fit: contain) so every aspect ratio renders at a
' consistent size — 4:3 gets pillarboxed, ultra-wide gets letterboxed.""",
"""' Fixed preview box (object-fit: contain).
' Every aspect ratio renders consistently: 4:3 content gets pillarbox,
' ultra-wide content gets letterbox."""
)

text = text.replace(
"""' Hard ceiling on the decoded mosaic regardless of server grid size (5x5 vs
' 10x10, etc.) — protects low-end devices even if the user never changes
' their Jellyfin trickplay grid setting.""",
"""' Maximum mosaic decode size regardless of server grid size (5x5, 10x10, etc.).
' Protects low-end devices without requiring Jellyfin server-side changes."""
)

text = text.replace(
"""' displayScale: SIEMPRE es el que ajusta a la caja fija. Nunca se reduce
' por temas de memoria -- esto es lo que el usuario VE.""",
"""' displayScale controls only the final on-screen size.
' It is independent from memory protection and always fits the preview box."""
)

text = text.replace(
"""' loadScale: solo protege memoria de decodificación. Puede ser MENOR
' que displayScale (Roku sobre-escala el resultado al width/height del
' Poster, perdiendo algo de nitidez en grids grandes, pero nunca
' afecta el tamaño ni la posición en pantalla).""",
"""' loadScale only controls decode memory usage.
' It may be lower than displayScale for large mosaics (for example 10x10 grids).
' Roku upscales the decoded texture to the display size, which may slightly
' reduce sharpness but does not affect layout or positioning."""
)

text = text.replace(
"""' Roku downscala DURANTE la decodificación, nunca carga el JPEG a tamaño
' completo en memoria de textura.""",
"""' Roku downscales during decoding, preventing the full JPEG size from
' being allocated as a texture in memory."""
)

text = text.replace(
"""' Offset del tile DENTRO de la caja fija -> esto es lo que genera el
' pillarbox (4:3) o letterbox (panorámico) automáticamente.""",
"""' Center the selected tile inside the fixed preview box.
' This naturally creates pillarbox for 4:3 content and letterbox for
' ultra-wide content."""
)

path.write_text(text)

