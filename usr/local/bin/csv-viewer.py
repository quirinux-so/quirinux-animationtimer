import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import csv
import subprocess
import tempfile
import os
import sys
from pathlib import Path

class CSVViewerApp:
    def __init__(self, root, file_path=None):
        self.root = root
        self.root.title("Visor de CSV")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#fef9f3")
        self.font_color = "#0e1726"

        self.traducciones = {
            "español": {
                "titulo": "Visor de CSV",
                "descripcion": "Para abrir mediciones de Animation Timer",
                "btn_abrir": "Abrir archivo",
                "btn_imprimir": "Imprimir",
                "btn_idioma": "Español"
            },
            "ingles": {
                "titulo": "CSV Viewer",
                "descripcion": "To open Animation Timer measurements",
                "btn_abrir": "Open File",
                "btn_imprimir": "Print",
                "btn_idioma": "English"
            },
            "gallego": {
                "titulo": "Visor de CSV",
                "descripcion": "Para abrir medicións de Animation Timer",
                "btn_abrir": "Abrir arquivo",
                "btn_imprimir": "Imprimir",
                "btn_idioma": "Galego"
            },
            "aleman": {
                "titulo": "CSV-Viewer",
                "descripcion": "Zum Öffnen von Animation Timer Messungen",
                "btn_abrir": "Datei öffnen",
                "btn_imprimir": "Drucken",
                "btn_idioma": "Deutsch"
            },
            "frances": {
                "titulo": "Visionneuse de CSV",
                "descripcion": "Pour ouvrir des mesures d'Animation Timer",
                "btn_abrir": "Ouvrir le fichier",
                "btn_imprimir": "Imprimer",
                "btn_idioma": "Français"
            },
            "italiano": {
                "titulo": "Visualizzatore CSV",
                "descripcion": "Per aprire le misurazioni di Animation Timer",
                "btn_abrir": "Apri file",
                "btn_imprimir": "Stampa",
                "btn_idioma": "Italiano"
            },
            "portugues": {
                "titulo": "Visualizador de CSV",
                "descripcion": "Para abrir medições de Animation Timer",
                "btn_abrir": "Abrir arquivo",
                "btn_imprimir": "Imprimir",
                "btn_idioma": "Português"
            }
        }

        self.idioma_actual = "español"
        self.idiomas = list(self.traducciones.keys())

        self.titulo = tk.Label(root, text=self.traducciones[self.idioma_actual]["titulo"], font=("Arial", 18), bg="#fef9f3", fg=self.font_color)
        self.titulo.pack(pady=10)

        self.subtitulo = tk.Label(root, text="(c) Charlie Martinez - Quirinux, GPLv2.0", font=("Arial", 10), bg="#fef9f3", fg=self.font_color)
        self.subtitulo.pack(pady=(0, 10))

        self.descripcion = tk.Label(root, text=self.traducciones[self.idioma_actual]["descripcion"], bg="#fef9f3", fg=self.font_color)
        self.descripcion.pack(pady=10)

        self.btn_frame = tk.Frame(root, bg="#fef9f3")
        self.btn_frame.pack(pady=10)

        min_button_width = max(len(self.traducciones["frances"]["btn_abrir"]),
                               len(self.traducciones["frances"]["btn_imprimir"]),
                               len(self.traducciones["frances"]["btn_idioma"])) + 2

        self.btn_abrir = tk.Button(self.btn_frame, text=self.traducciones[self.idioma_actual]["btn_abrir"], command=self.abrir_archivo, width=min_button_width)
        self.btn_abrir.pack(side=tk.LEFT, padx=5)

        self.btn_imprimir = tk.Button(self.btn_frame, text=self.traducciones[self.idioma_actual]["btn_imprimir"], command=self.imprimir, width=min_button_width)
        self.btn_imprimir.pack(side=tk.LEFT, padx=5)

        self.btn_idioma = tk.Button(self.btn_frame, text=self.traducciones[self.idioma_actual]["btn_idioma"], command=self.cambiar_idioma, width=min_button_width)
        self.btn_idioma.pack(side=tk.LEFT, padx=5)

        self.table_text = scrolledtext.ScrolledText(root, wrap=tk.NONE)
        self.table_text.pack(fill=tk.BOTH, expand=True)

        self.current_file_path = file_path
        if self.current_file_path:
            self.mostrar_csv(self.current_file_path)

    def abrir_archivo(self):
        desktop_dir = self.get_desktop_dir()
        file_path = filedialog.askopenfilename(initialdir=desktop_dir, filetypes=[("Archivos CSV", "*.csv")])
        if file_path:
            self.current_file_path = file_path
            self.mostrar_csv(file_path)

    def get_desktop_dir(self):
        try:
            home = str(Path.home())
            with open(os.path.join(home, '.config/user-dirs.dirs')) as f:
                for line in f:
                    if 'XDG_DESKTOP_DIR' in line:
                        desktop_dir = line.split('=')[1].strip().replace('$HOME', home).strip('"')
                        return desktop_dir
        except Exception as e:
            pass
        return str(Path.home())

    def mostrar_csv(self, file_path):
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            column_widths = [max(len(cell) for cell in column) for column in zip(*rows)]
            table_text = ""
            for row in rows:
                table_text += "\t".join(cell.ljust(width + 2) for cell, width in zip(row, column_widths)) + "\n"
            self.table_text.delete(1.0, tk.END)
            self.table_text.insert(tk.END, table_text)

    def imprimir(self):
        if self.current_file_path:
            try:
                with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix=".txt", dir='/tmp') as temp_file:
                    table_text = self.table_text.get(1.0, tk.END).strip().split('\n')
                    for line in table_text:
                        cells = line.split('\t')
                        adjusted_line = " ".join(cells)
                        temp_file.write(adjusted_line + "\n")
                    temp_file_path = temp_file.name

                subprocess.run(["lpr", "-o", "scaling=75", temp_file_path], check=True)
                os.remove(temp_file_path)
                messagebox.showinfo("Imprimir", "El archivo se ha enviado a la impresora correctamente.")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"No se pudo imprimir el archivo. {str(e)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error inesperado al imprimir el archivo. {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "No hay archivo cargado para imprimir")

    def cambiar_idioma(self):
        idx = self.idiomas.index(self.idioma_actual)
        self.idioma_actual = self.idiomas[(idx + 1) % len(self.idiomas)]
        self.actualizar_textos()

    def actualizar_textos(self):
        self.titulo.config(text=self.traducciones[self.idioma_actual]["titulo"])
        self.descripcion.config(text=self.traducciones[self.idioma_actual]["descripcion"])
        self.btn_abrir.config(text=self.traducciones[self.idioma_actual]["btn_abrir"])
        self.btn_imprimir.config(text=self.traducciones[self.idioma_actual]["btn_imprimir"])
        self.btn_idioma.config(text=self.traducciones[self.idioma_actual]["btn_idioma"])

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    root = tk.Tk()
    app = CSVViewerApp(root, file_path)
    root.mainloop()
