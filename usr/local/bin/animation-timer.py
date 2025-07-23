import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import os
from pathlib import Path
import subprocess  # Importa subprocess para ejecutar el comando

class AnimationTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animation Timer")
        self.root.geometry("1000x600")  # Ajusta el ancho de la ventana para mostrar todas las columnas
        self.root.configure(bg='#fef9f3')
        self.running = False
        self.total_seconds = 0
        self.total_frames = 0
        self.measurement_count = 0
        self.accumulated_frames = 0
        self.accumulated_seconds = 0
        self.current_lang = 'es'

        self.translations = {
            "es": {"Tiempo": "Tiempo", "Frames": "Fotogramas", "subtitle": "Hecho por Charlie Martínez para Quirinux.org, GPLv2.0", "Medición": "Medición", "FPS": "FPS", "Segundos": "Segundos", "Fotogramas": "Fotogramas", "Fotogramas totales": "Fotogramas totales", "Tiempo total": "Tiempo total", "Exportar": "Exportar", "Iniciar": "Iniciar", "Parar": "Parar", "Abrir CSV": "Abrir CSV"},
            "pt": {"Tiempo": "Tempo", "Frames": "Fotogramas", "subtitle": "Feito por Charlie Martínez para Quirinux.org, GPLv2.0", "Medición": "Medição", "FPS": "FPS", "Segundos": "Segundos", "Fotogramas": "Fotogramas", "Fotogramas totales": "Fotogramas totais", "Tiempo total": "Tempo total", "Exportar": "Exportar", "Iniciar": "Iniciar", "Parar": "Parar", "Abrir CSV": "Abrir CSV"},
            "it": {"Tiempo": "Tempo", "Frames": "Fotogrammi", "subtitle": "Fatto da Charlie Martínez per Quirinux.org, GPLv2.0", "Medición": "Misurazione", "FPS": "FPS", "Segundos": "Secondi", "Fotogramas": "Fotogrammi", "Fotogramas totales": "Fotogrammi totali", "Tiempo total": "Tempo totale", "Exportar": "Esportare", "Iniciar": "Inizia", "Parar": "Ferma", "Abrir CSV": "Apri CSV"},
            "de": {"Tiempo": "Zeit", "Frames": "Bilder", "subtitle": "Gemacht von Charlie Martínez für Quirinux.org, GPLv2.0", "Medición": "Messung", "FPS": "FPS", "Segundos": "Sekunden", "Fotogramas": "Bilder", "Fotogramas totales": "Gesamtbilder", "Tiempo total": "Gesamtzeit", "Exportar": "Exportieren", "Iniciar": "Start", "Parar": "Stop", "Abrir CSV": "CSV öffnen"},
            "fr": {"Tiempo": "Temps", "Frames": "Images", "subtitle": "Fait par Charlie Martínez pour Quirinux.org, GPLv2.0", "Medición": "Mesure", "FPS": "FPS", "Segundos": "Secondes", "Fotogramas": "Images", "Fotogramas totales": "Images totales", "Tiempo total": "Temps total", "Exportar": "Exporter", "Iniciar": "Démarrer", "Parar": "Arrêter", "Abrir CSV": "Ouvrir CSV"},
            "en": {"Tiempo": "Time", "Frames": "Frames", "subtitle": "Made by Charlie Martínez for Quirinux.org, GPLv2.0", "Medición": "Measurement", "FPS": "FPS", "Seconds": "Seconds", "Frames": "Frames", "Total Frames": "Total Frames", "Total Time": "Total Time", "Export": "Export", "Start": "Start", "Stop": "Stop", "Open CSV": "Open CSV"}
        }

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Animation Timer", font=("Arial", 20), bg='#fef9f3', fg='#0e1726')
        self.title_label.pack(pady=10)

        self.subtitle_label = tk.Label(self.root, text=self.translations[self.current_lang]["subtitle"], font=("Arial", 10), bg='#fef9f3', fg='#0e1726')
        self.subtitle_label.pack(pady=5)

        self.container = tk.Frame(self.root, bg='#3e2723', bd=10, relief=tk.RIDGE)
        self.container.pack(pady=10)

        self.tiempo_label = tk.Label(self.container, text=self.translations[self.current_lang]["Tiempo"], font=("Arial", 16), bg='#5d4037', fg='#fef9f3')
        self.tiempo_label.grid(row=0, column=0, padx=5, pady=5)

        self.contador_label = tk.Label(self.container, text="00:00", font=("Arial", 16), bg='#5d4037', fg='#fef9f3', width=10)
        self.contador_label.grid(row=0, column=1, padx=5, pady=5)

        self.frames_label = tk.Label(self.container, text=self.translations[self.current_lang]["Frames"], font=("Arial", 16), bg='#5d4037', fg='#fef9f3')
        self.frames_label.grid(row=1, column=0, padx=5, pady=5)

        self.frames_display = tk.Label(self.container, text="0", font=("Arial", 16), bg='#5d4037', fg='#fef9f3', width=10)
        self.frames_display.grid(row=1, column=1, padx=5, pady=5)

        self.control_panel = tk.Frame(self.root, bg='#fef9f3')
        self.control_panel.pack(pady=10)

        self.fps_label = tk.Label(self.control_panel, text="FPS", font=("Arial", 12), bg='#fef9f3', fg='#0e1726')
        self.fps_label.grid(row=0, column=0, padx=5, pady=5)

        self.fps_selector = ttk.Combobox(self.control_panel, values=[4, 8, 12, 24], font=("Arial", 12), state="readonly")
        self.fps_selector.current(0)
        self.fps_selector.grid(row=0, column=1, padx=5, pady=5)

        self.start_stop_btn = tk.Button(self.control_panel, text=self.translations[self.current_lang]["Iniciar"], font=("Arial", 12), bg='#6d4c41', fg='#fef9f3', command=self.start_timer)
        self.start_stop_btn.grid(row=0, column=2, padx=5, pady=5)

        self.change_lang_btn = tk.Button(self.control_panel, text=self.current_lang.upper(), font=("Arial", 12), bg='#6d4c41', fg='#fef9f3', command=self.change_language)
        self.change_lang_btn.grid(row=0, column=3, padx=5, pady=5)

        self.results_frame = tk.Frame(self.root)
        self.results_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.results_table = ttk.Treeview(self.results_frame, columns=("measurement", "fps", "seconds", "frames", "total_frames", "total_time"), show="headings")
        self.results_table.heading("measurement", text=self.translations[self.current_lang]["Medición"])
        self.results_table.heading("fps", text=self.translations[self.current_lang]["FPS"])
        self.results_table.heading("seconds", text=self.translations[self.current_lang]["Segundos"])
        self.results_table.heading("frames", text=self.translations[self.current_lang]["Fotogramas"])
        self.results_table.heading("total_frames", text=self.translations[self.current_lang]["Fotogramas totales"])
        self.results_table.heading("total_time", text=self.translations[self.current_lang]["Tiempo total"])

        for col in self.results_table["columns"]:
            self.results_table.column(col, width=150, minwidth=150, anchor='center')

        self.results_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.results_table.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.results_table.configure(yscrollcommand=self.scrollbar.set)

        # Create a container for the bottom buttons and center them
        self.button_frame = tk.Frame(self.root, bg='#fef9f3')
        self.button_frame.pack(pady=10)

        self.export_btn = tk.Button(self.button_frame, text=self.translations[self.current_lang]["Exportar"], font=("Arial", 12), bg='#6d4c41', fg='#fef9f3', command=self.export_to_csv)
        self.export_btn.pack(side=tk.LEFT, padx=5)

        self.open_csv_btn = tk.Button(self.button_frame, text=self.translations[self.current_lang]["Abrir CSV"], font=("Arial", 12), bg='#6d4c41', fg='#fef9f3', command=self.open_csv)
        self.open_csv_btn.pack(side=tk.LEFT, padx=5)

    def start_timer(self):
        if self.running:
            self.running = False
            self.start_stop_btn.configure(text=self.translations[self.current_lang]["Iniciar"])
            self.record_measurement()
        else:
            self.reset_display()
            self.running = True
            self.start_stop_btn.configure(text=self.translations[self.current_lang]["Parar"])
            self.update_timer()

    def update_timer(self):
        if self.running:
            self.total_seconds += 1
            fps = int(self.fps_selector.get())
            self.total_frames = self.total_seconds * fps

            minutes = self.total_seconds // 60
            seconds = self.total_seconds % 60
            formatted_time = f"{minutes:02d}:{seconds:02d}"

            self.contador_label.configure(text=formatted_time)
            self.frames_display.configure(text=self.total_frames)

            self.root.after(1000, self.update_timer)

    def reset_display(self):
        self.total_seconds = 0
        self.total_frames = 0
        self.contador_label.configure(text="00:00")
        self.frames_display.configure(text="0")

    def record_measurement(self):
        self.measurement_count += 1
        fps = int(self.fps_selector.get())
        self.accumulated_frames += self.total_frames
        self.accumulated_seconds += self.total_seconds

        total_time = f"{self.accumulated_seconds // 60:02d}:{self.accumulated_seconds % 60:02d}"

        self.results_table.insert("", "end", values=(self.measurement_count, fps, self.total_seconds, self.total_frames, self.accumulated_frames, total_time))

    def change_language(self):
        languages = list(self.translations.keys())
        current_index = languages.index(self.current_lang)
        next_index = (current_index + 1) % len(languages)
        self.current_lang = languages[next_index]
        self.apply_translations()

    def apply_translations(self):
        self.tiempo_label.configure(text=self.translations[self.current_lang]["Tiempo"])
        self.frames_label.configure(text=self.translations[self.current_lang]["Frames"])
        self.subtitle_label.configure(text=self.translations[self.current_lang]["subtitle"])
        self.start_stop_btn.configure(text=self.translations[self.current_lang]["Iniciar"] if not self.running else self.translations[self.current_lang]["Parar"])
        self.change_lang_btn.configure(text=self.current_lang.upper())
        self.export_btn.configure(text=self.translations[self.current_lang]["Exportar"])
        self.open_csv_btn.configure(text=self.translations[self.current_lang]["Abrir CSV"])

        self.results_table.heading("measurement", text=self.translations[self.current_lang]["Medición"])
        self.results_table.heading("fps", text=self.translations[self.current_lang]["FPS"])
        self.results_table.heading("seconds", text=self.translations[self.current_lang]["Segundos"])
        self.results_table.heading("frames", text=self.translations[self.current_lang]["Fotogramas"])
        self.results_table.heading("total_frames", text=self.translations[self.current_lang]["Fotogramas totales"])
        self.results_table.heading("total_time", text=self.translations[self.current_lang]["Tiempo total"])

        for col in self.results_table["columns"]:
            self.results_table.column(col, width=150, minwidth=150, anchor='center')

    def get_desktop_path(self):
        try:
            with open(Path.home() / '.config/user-dirs.dirs') as file:
                lines = file.readlines()
                for line in lines:
                    if 'XDG_DESKTOP_DIR' in line:
                        desktop_path = line.split('=')[1].strip().replace('$HOME', str(Path.home())).replace('"', '')
                        return Path(desktop_path)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo determinar el directorio del escritorio: {e}")
        return Path.home() / 'Desktop'

    def export_to_csv(self):
        desktop = self.get_desktop_path()
        file_path = desktop / "mediciones.csv"
        headers = ["Medición", "FPS", "Segundos", "Fotogramas", "Fotogramas totales", "Tiempo total"]

        data = []
        for row in self.results_table.get_children():
            data.append(self.results_table.item(row)["values"])

        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(data)
            messagebox.showinfo("Éxito", f"Datos exportados exitosamente a {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar el archivo: {e}")

    def open_csv(self):
        try:
            subprocess.run(["visorcsv"], check=True)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el visor de CSV: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimationTimerApp(root)
    root.mainloop()
