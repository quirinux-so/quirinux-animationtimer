# Animation Timer <img width="32" alt="animation-timer" src="https://github.com/user-attachments/assets/0a2913f9-fa36-4bcc-85ca-91234bf96860" />

**Autor / Author:** Charlie Martínez – Quirinux GNU/Linux®  
**Licencia / License:** GPLv2.0

![Animation Timer Screenshot](https://github.com/user-attachments/assets/0de05420-1c91-4d41-93bf-193ce2ba0987)

---

## 🧭 Descripción general / Overview

**ES:**  
`Animation Timer` es una aplicación gráfica, multilingüe y sin conexión, diseñada para registrar tiempos y fotogramas en procesos de animación manual o tradicional. Es especialmente útil en entornos educativos o para animadores profesionales.

Además, incluye un visor de archivos CSV independiente para consultar o imprimir las mediciones exportadas. 

**EN:**  
`Animation Timer` is a graphical, multilingual, and offline application designed to log time and frames for manual or traditional animation workflows. It is especially useful for educators and professional animators.

Additionally, it includes a standalone CSV viewer for reading or printing exported measurements.

---

## ✔️ Características / Features

**ES:**
- Registro automático de tiempo y fotogramas  
- Selector de FPS: 4, 8, 12, 24  
- Tabla resumen por medición con totales acumulados  
- Exportación directa al escritorio en formato CSV  
- Visor independiente de CSV con opción de impresión  
- Interfaz disponible en: Español, Inglés, Alemán, Francés, Italiano, Portugués y Gallego  
- Uso completamente offline (no requiere conexión ni dependencias externas)  
- Optimizado para sistemas basados en Debian

**EN:**
- Automatic time and frame logging  
- FPS selector: 4, 8, 12, 24  
- Summary table per session with cumulative totals  
- Direct export to the desktop in CSV format  
- Standalone CSV viewer with print capability  
- Interface available in: Spanish, English, German, French, Italian, Portuguese, and Galician  
- Fully offline operation (no internet or pip required)  
- Designed for Debian-based systems

---

## 📋 Requisitos / Requirements

**ES**  
Instalar la siguiente dependencia antes de ejecutar:  

**EN:**  
Install the following dependency before running:


    su root
    apt install python3-tk

---

## ▶️ Ejecución / How to Run

**ES:**  
Aplicación principal:  

**EN:**  
Main application:

    git clone https://github.com/quirinux-so/quirinux-animationtimer.git
    cd quirinux-animationtimer/usr/local/bin
    python3 animation-timer.py

**ES:**  
Visor de CSV (opcional):  

**EN:**  
CSV viewer (optional):

    python3 csv-viewer.py

---

## 📦 Instalación alternativa / Optional Installation (Quirinux)

**ES:**  
Disponible como paquete oficial `.deb` desde el repositorio de Quirinux o desde el Centro de Software.

**EN:**  
Available as an official `.deb` package via the Quirinux repository or Software Center.

**Comando / Command:**

(sangría para simular bloque de código)

    su root
    apt install quirinux-animationtimer

**Repositorio / Repository:**  
[https://repo.quirinux.org/pool/main/q/quirinux-animationtimer](https://repo.quirinux.org/pool/main/q/quirinux-animationtimer)

---

## ⚖️ Aviso legal / Legal Notice

**ES:**  
Este proyecto forma parte del ecosistema **Quirinux**, pero es compatible con cualquier distribución moderna de GNU/Linux.  
Distribuido bajo los términos de la licencia **GPLv2**.

**EN:**  
This project is part of the **Quirinux** ecosystem but remains compatible with any modern GNU/Linux distribution.  
Released under the terms of the **GPLv2 license**.

**Autor / Author:** Charlie Martínez  
📧 <cmartinez@quirinux.org>

**Más información / More information:**  
[https://www.quirinux.org/aviso-legal](https://www.quirinux.org/aviso-legal)
