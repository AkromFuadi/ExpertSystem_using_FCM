import tkinter as tk
from tkinter import messagebox

class SistemPakar(tk.Tk):
    def __init__(self):
        super().__init__()

        self.gejala = {
            'G1' : '\nApakah anda merasa cemas, takut, menghindar atau meningkatnya kesiagaan?',
            'G2' : '\nAdakah bukti penyakit fisik dari medis?',
            'G3' : '\nAdakah bukti penyakit fisik dari medis setelah\nmenggunakan atau mengkonsumsi suatu zat\n(misalnya, obat-obatan yang disalahgunakan, narkotika, toksin atau antibody)?',
            'G4' : '\nApakah muncul rasa panik dan cemas berulang tak terduga selama 1 bulan?',
            'G5' : '\nApakah muncul rasa panik dan cemas yang berasal\ndari perasaan ketika berada di tempat umum?',
            'G6' : '\nApakah muncul rasa cemas atau prasangka buruk sebelum berada di tempat umum?',
            'G7' : '\nApakah anda cemas ketika berpisah dari orang atau\nsosok yang akrab sejak masa kanak-kanak\n(orang tua, saudara, dan teman)?',
            'G8' : '\nApakah anda takut dihina dan dipermalukan dalam situasi sosial atau di tempat umum?',
            'G9' : '\nApakah anda takut akan objek atau benda tertentu\n(misal, bulu kucing, ketinggian, ulat)?',
            'G10' : '\nApakah pikiran cemas akan anggota tubuh atau situasi yang dirasa kurang\n(contoh, cuci tangan berulang-ulang secara berlebihan setiap, selalu was-was\nakan keadaan pintu yang seolah-olah belum terkunci, dan lain-lain)?',
            'G11' : '\nApakah anda merasa cemas dan khawatir selama lebih dari 6 bulan?',
            'G12' : '\nApakah kecemasan anda disebabkan trauma berat\n(contoh, pelecehan seksual,kecelakaan, penyakit berat, dan lain-lain)?',
            'G13' : '\nApakah anda selalu mengingat kejadian yang berhubungan dengan peristiwa traumatik\n(contoh, pelecehan seksual, kecelakaan, penyakit berat, dan lain-lain)?',
            'G14' : '\nApakah lamanya lebih dari 1 bulan?',
            'G15' : '\nAdakah perasaan cemas ketika berada di lingkungan, pekerjaan, status yang baru\n(contoh, merantau, baru menikah, menduduki jabatan yang baru)?',
            'G16' : '\nGangguan cemas yang tidak disebutkan di atas?'
        }

        self.rules = {
            'R1' : {'G1': True, 'G2': True, 'result': 'Anda mungkin mengalami : Gangguan cemas akibat penyakit umum.'},
            'R2' : {'G1': True, 'G3': True, 'result': 'Anda mungkin mengalami : Gangguan cemas akibat zat adiktif.'},
            'R3' : {'G1': True, 'G4': True, 'G5': True, 'result': 'Anda mungkin mengalami : Gangguan panik dengan Agorafobia.'},
            'R4' : {'G1': True, 'G4': True, 'result': 'Anda mungkin mengalami : Gangguan panik tanpa Agorafobia.'},
            'R5' : {'G1': True, 'G6': True, 'result': 'Anda mungkin mengalami : Agorafobia tanpa riwayat panik.'},
            'R6' : {'G1': True, 'G7': True, 'result': 'Anda mungkin mengalami : Gangguan cemas akan perpisahan.'},
            'R7' : {'G1': True, 'G8': True, 'result': 'Anda mungkin mengalami : Fobia sosial (gangguan cemas sosial).'},
            'R8' : {'G1': True, 'G9': True, 'result': 'Anda mungkin mengalami : Fobia spesifik.'},
            'R9' : {'G1': True, 'G10': True, 'result': 'Anda mungkin mengalami : Gangguan obsesif dan kompulsif.'},
            'R10' : {'G1': True, 'G11': True, 'G12': True, 'G13': True, 'result': 'Anda mungkin mengalami : Gangguan cemas menyeluruh (General Anxiety Disorder).'},
            'R11' : {'G1': True, 'G11': True, 'G12': True, 'result': 'Anda mungkin mengalami : Gangguan stress pasca traumatik (Post Traumatic Stress Disorder).'},
            'R12' : {'G1': True, 'G14': True, 'result': 'Anda mungkin mengalami : Gangguan stress akut.'},
            'R13' : {'G1': True, 'G15': True, 'result': 'Anda mungkin mengalami : Gangguan penyesuaian.'},
            'R14' : {'G1': True, 'G16': True, 'result': 'Anda mungkin mengalami : Gangguan cemas yang tidak terinci.'},
            'R15' : {'G1': False, 'result': 'Anda mungkin mengalami : Bukan gangguan cemas (gejala takut, cemas, atau menghindar yang tidak bermakna secara klinis).'}
        }

        self.current_question = None
        self.user_answers = {}

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="\nSISTEM PAKAR DIAGNOSA GANGGUAN\nKECEMASAN (ANXIETY DISORDER)\nMENGGUNAKAN FORWARD CHAINING", font=("Times New Roman", 21))
        self.label.pack(pady=10)

        self.label = tk.Label(self, text="Dibuat oleh:\n\n1). Rayhan B. N. (082011233050)\n2). Akrom F. (082011233079)", font=("Times New Roman", 12))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self, text="Mulai Konsultasi", command=self.show_question, font=("Times New Roman", 14))
        self.start_button.pack(pady=10)

        self.answer_frame = tk.Frame(self)
        self.answer_frame.pack(pady=20)

    def show_question(self):
        if not self.current_question:
            self.current_question = iter(self.gejala)

        self.start_button.destroy()

        try:
            gejala_key = next(self.current_question)
            self.label.config(text=self.gejala[gejala_key], font=("Times New Roman", 16))

            self.answer_frame.destroy()
            self.answer_frame = tk.Frame(self)
            self.answer_frame.pack(pady=20)

            self.yes_button = tk.Button(self.answer_frame, text="Ya", command=lambda: self.save_answer(gejala_key, True), font=("Times New Roman", 12))
            self.yes_button.grid(row=0, column=0, padx=10)

            self.no_button = tk.Button(self.answer_frame, text="Tidak", command=lambda: self.save_answer(gejala_key, False), font=("Times New Roman", 12))
            self.no_button.grid(row=0, column=1, padx=10)

        except StopIteration:
            self.evaluate_rules()

    def save_answer(self, gejala_key, answer):
        self.user_answers[gejala_key] = answer
        next_question = self.get_next_question(gejala_key, answer)
        if next_question:
            self.current_question = iter([next_question])
        else:
            self.evaluate_rules()
        self.show_question()

    def get_next_question(self, gejala_key, answer):
        if gejala_key == 'G1' and answer == True:
            return 'G2'
        elif gejala_key == 'G1' and not answer == True:
            return None  
        elif gejala_key == 'G2' and answer == True:
            return None
        elif gejala_key == 'G2' and not answer == True:
            return 'G3'
        elif gejala_key == 'G3' and answer == True:
            return None
        elif gejala_key == 'G3' and not answer == True:
            return 'G4'
        elif gejala_key == 'G4' and answer == True:
            return 'G5'
        elif gejala_key == 'G4' and not answer == True:
            return 'G6'
        elif gejala_key == 'G5' and answer == True:
            return None
        elif gejala_key == 'G5' and not answer == True:
            return None
        elif gejala_key == 'G6' and answer == True:
            return None
        elif gejala_key == 'G6' and not answer == True:
            return 'G7'
        elif gejala_key == 'G7' and answer == True:
            return None
        elif gejala_key == 'G7' and not answer == True:
            return 'G8'
        elif gejala_key == 'G8' and answer == True:
            return None
        elif gejala_key == 'G8' and not answer == True:
            return 'G9'
        elif gejala_key == 'G9' and answer == True:
            return None
        elif gejala_key == 'G9' and not answer == True:
            return 'G10'
        elif gejala_key == 'G10' and answer == True:
            return None
        elif gejala_key == 'G10' and not answer == True:
            return 'G11'
        elif gejala_key == 'G11' and answer == True:
            return 'G12'
        elif gejala_key == 'G11' and not answer == True:
            return 'G14'
        elif gejala_key == 'G12' and answer == True:
            return 'G13'
        elif gejala_key == 'G12' and not answer == True:
            return None
        elif gejala_key == 'G13' and answer == True:
            return None
        elif gejala_key == 'G13' and not answer == True:
            return None
        elif gejala_key == 'G14' and answer == True:
            return None
        elif gejala_key == 'G14' and not answer == True:
            return 'G15'
        elif gejala_key == 'G15' and answer == True:
            return None
        elif gejala_key == 'G15' and not answer == True:
            return 'G16'
        elif gejala_key == 'G16' and answer == True:
            return None
        elif gejala_key == 'G16' and not answer == True:
            return None

        return None
    
    def evaluate_rules(self):
        for rule in self.rules.values():
            match = True
            for gejala, value in rule.items():
                if gejala == 'result':
                    continue
                if self.user_answers.get(gejala) != value:
                    match = False
                    break

            if match:
                messagebox.showinfo("HASIL DIAGNOSA", rule['result'])
                self.destroy()
                break
        else:
            result = messagebox.showinfo("HASIL DIAGNOSA", "Tidak ditemukan hasil berdasarkan jawaban Anda.")
            if result == 'ok':
                self.destroy()

if __name__ == "__main__":
    app = SistemPakar()
    app.title("TUGAS AKHIR KECERDASAN BUATAN")
    app.geometry("825x400")
    app.mainloop()