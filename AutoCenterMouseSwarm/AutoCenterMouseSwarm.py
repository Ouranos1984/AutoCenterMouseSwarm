import ctypes
import time
from threading import Thread
import keyboard  # Bibliothèque pour capturer globalement les frappes de touches
import tkinter as tk

# Constantes
USER32 = ctypes.windll.user32
SCREEN_WIDTH = USER32.GetSystemMetrics(0)
SCREEN_HEIGHT = USER32.GetSystemMetrics(1)
WINDOW_SIZE = 200

class MouseRestrictor:
    def __init__(self):
        self.active = False
        self.running = True
        self.debug_window = None
        self.debug_text = None
        self.debug_info = None

        # Centrer la fenêtre sur l'écran
        self.x_center = (SCREEN_WIDTH - WINDOW_SIZE) // 2
        self.y_center = (SCREEN_HEIGHT - WINDOW_SIZE) // 2

        # Afficher les messages de démarrage
        print("F1: Activer/Désactiver la restriction du curseur")
        print("F2: Ouvrir la fenêtre de débogage")
        print("F4: Quitter l'application")
        print("Restriction désactivée")

        # Configurer les raccourcis clavier globaux
        keyboard.add_hotkey('F1', self.toggle_restriction)
        keyboard.add_hotkey('F2', self.open_debug_window)
        keyboard.add_hotkey('F4', self.stop)

        # Initialiser Tkinter
        self.main_window = tk.Tk()
        self.main_window.withdraw()  # Cacher la fenêtre principale de Tkinter

        # Initialiser le suivi de l'inactivité de la souris
        self.last_mouse_position = None
        self.last_move_time = time.time()
        self.center_count = 0

        # Démarrer le thread de surveillance de l'inactivité de la souris
        self.monitor_thread = Thread(target=self.monitor_mouse_inactivity)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

        self.print_message("Script initialisé")

    def toggle_restriction(self, event=None):
        self.print_message("Touche F1 pressée")
        if self.active:
            self.deactivate()
        else:
            self.activate()

    def activate(self):
        print("Activation de la restriction")
        self.active = True
        self.update_clip()
        self.center_cursor()
        print("Restriction activée")

    def deactivate(self):
        print("Désactivation de la restriction")
        self.active = False
        self.release_clip()
        print("Restriction désactivée")

    def update_clip(self):
        print("Mise à jour de la zone de restriction")
        x1 = self.x_center
        y1 = self.y_center
        x2 = x1 + WINDOW_SIZE
        y2 = y1 + WINDOW_SIZE

        rect = ctypes.wintypes.RECT(x1, y1, x2, y2)
        ctypes.windll.user32.ClipCursor(ctypes.byref(rect))

    def release_clip(self):
        print("Libération de la zone de restriction")
        ctypes.windll.user32.ClipCursor(None)

    def print_message(self, message):
        if self.debug_text:
            self.debug_text.insert(tk.END, message + '\n')
            self.debug_text.see(tk.END)  # Faire défiler vers le bas pour voir le dernier message

    def open_debug_window(self):
        self.print_message("Touche F2 pressée")
        if not self.running:
            return
        if self.debug_window is None or not self.debug_window.winfo_exists():
            self.show_debug_window()

    def show_debug_window(self):
        self.print_message("Ouverture de la fenêtre de débogage")
        self.debug_window = tk.Toplevel(self.main_window)
        self.debug_window.title("Fenêtre de Débogage")

        self.debug_text = tk.Text(self.debug_window, wrap='word')
        self.debug_text.pack(expand=True, fill='both')

        self.debug_info = tk.Label(self.debug_window, text="", anchor="w", justify="left")
        self.debug_info.pack(fill='x')

        self.debug_window.protocol("WM_DELETE_WINDOW", self.on_debug_window_close)

    def update_debug_info(self):
        if self.debug_info:
            elapsed_time = time.time() - self.last_move_time

            debug_info_text = (
                f"Statut de la restriction: {'Activée' if self.active else 'Désactivée'}\n"
                f"Temps écoulé depuis le dernier mouvement: {elapsed_time:.2f} secondes\n"
                f"Nombre de recentrages: {self.center_count}\n"
            )

            self.debug_info.config(text=debug_info_text)

    def on_debug_window_close(self):
        self.print_message("Fermeture de la fenêtre de débogage")
        self.debug_window.destroy()
        self.debug_window = None
        self.debug_info = None

    def stop(self):
        print("Touche F4 pressée")
        self.running = False
        self.release_clip()
        print("Application arrêtée")
        if self.debug_window:
            self.debug_window.destroy()
        self.main_window.destroy()
        exit()

    def center_cursor(self):
        self.print_message("Recentrage du curseur")
        USER32.SetCursorPos(self.x_center + WINDOW_SIZE // 2, self.y_center + WINDOW_SIZE // 2)
        self.center_count += 1

    def monitor_mouse_inactivity(self):
        self.print_message("Démarrage de la surveillance de l'inactivité de la souris")
        while self.running:
            if self.active:
                current_position = ctypes.wintypes.POINT()
                USER32.GetCursorPos(ctypes.byref(current_position))
                current_position = (current_position.x, current_position.y)
                if self.last_mouse_position != current_position:
                    self.last_mouse_position = current_position
                    self.last_move_time = time.time()
                elif time.time() - self.last_move_time > 0.25:
                    self.print_message("Inactivité détectée, recentrage du curseur")
                    self.center_cursor()
                    self.last_move_time = time.time()
            self.update_debug_info()
            time.sleep(0.01)  # Augmenter encore la fréquence de vérification

if __name__ == "__main__":
    app = MouseRestrictor()
    tk.mainloop()  # Exécuter la boucle principale de Tkinter
