
<img width="64" height="64" alt="animation-timer" src="https://github.com/user-attachments/assets/0a2913f9-fa36-4bcc-85ca-91234bf96860" />

# Animation Timer

(c) Charlie Martínez – Quirinux GNU/Linux, GPLv2  

![animationtimer](https://github.com/user-attachments/assets/57fb3431-93c4-44fa-b0dd-9d493c4389c7)


## 🇪🇸 Español  
**Animation Timer** es una aplicación gráfica, multilingüe y offline para registrar tiempos y fotogramas en animaciones manuales o tradicionales, especialmente útil para docentes o animadores.  

Además incluye un **visor de CSV** independiente para abrir o imprimir mediciones exportadas.  

✅ Características:

- Medición automática de tiempo y fotogramas  
- Selector de FPS: 4, 8, 12, 24  
- Tabla con resumen por medición, con acumulado total  
- Exportación directa a CSV en el escritorio  
- Visor independiente de CSV con opción de impresión  
- Interfaz en múltiples idiomas: Español, Inglés, Alemán, Francés, Italiano, Portugués y Gallego  
- Sin conexión a Internet (no requiere pip)  
- Ideal para sistemas basados en Debian y para su uso en educación  

🔧 Requisitos:

```bash
sudo apt install python3-tk
```

▶️ Ejecutar la aplicación principal:

```bash
git clone https://github.com/quirinux-so/animation-timer.git
cd animation-timer
python3 animationtimer.py
```

▶️ Ejecutar el visor de CSV (opcional):

```bash
python3 visorcsv.py
```

🔄 El botón de idioma cambia la interfaz de forma cíclica entre los idiomas disponibles.  
🖨️ El visor incluye opción de impresión directa mediante `lpr`.  

📦 Instalación en Quirinux (opcional):

```bash
su root
apt install quirinux-animationtimer
```

También disponible desde el **Centro de Software de Quirinux**.  
🔗 https://repo.quirinux.org/pool/main/q/quirinux-animationtimer

### ⚠️ Aviso legal  
Este proyecto forma parte del ecosistema **Quirinux**, pero es compatible con cualquier distribución moderna de GNU/Linux.  
Publicado bajo licencia **GPLv2**.  

Autor: Charlie Martinez <cmartinez@quirinux.org>

ℹ️ Más información:  
🔗 [https://www.quirinux.org/aviso-legal](https://www.quirinux.org/aviso-legal)

---

## 🇬🇧 English  
**Animation Timer** is a graphical, multilingual, and offline app to register time and frames for manual or traditional animation workflows — ideal for educators or animators.  

It also includes a standalone **CSV viewer** to open or print exported measurements.  

✅ Features:

- Automatic time and frame recording  
- FPS selector: 4, 8, 12, 24  
- Summary table per measurement with cumulative totals  
- Direct export to desktop in CSV format  
- Standalone CSV viewer with print option  
- Multilingual interface: Spanish, English, German, French, Italian, Portuguese, Galician  
- Offline-friendly (no pip required)  
- Designed for Debian-based systems  

🔧 Requirements:

```bash
sudo apt install python3-tk
```

▶️ Run the main application:

```bash
git clone https://github.com/quirinux-so/animation-timer.git
cd animation-timer
python3 animationtimer.py
```

▶️ Run the optional CSV viewer:

```bash
python3 visorcsv.py
```

🔄 The language button cycles through available languages.  
🖨️ Viewer includes direct print option using `lpr`.  

📦 Install on Quirinux (optional):

```bash
su root
apt install quirinux-animationtimer
```

Also available from the **Quirinux Software Center**.  
🔗 https://repo.quirinux.org/pool/main/q/quirinux-animationtimer

### ⚠️ Legal notice  
This project is part of the **Quirinux** ecosystem but compatible with any modern GNU/Linux distribution.  
Released under the **GPLv2 license**.  

Author: Charlie Martinez <cmartinez@quirinux.org>

ℹ️ More info:  
🔗 [https://www.quirinux.org/aviso-legal](https://www.quirinux.org/aviso-legal)
