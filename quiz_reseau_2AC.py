import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

quiz_questions = [
    {"question": " As tu besoin d'un réseau informatique pour Partager une imprimante? ", "options": ["Oui", "Non"],"answer": "Oui"},
    {"question": " Dans la topologie en bus si le câble central subit une rupture, quelle sera son influence sur le réseau? ","options": ["Le réseau continue à fonctionner", "Le réseau tombe en panne"],"answer": "Le réseau tombe en panne"},
    {"question": " Qu'elle est la topologie qui a des problèmes de collision  ?","options": ["Topologie en bus", "Topologie en anneau"], "answer": "Topologie en anneau"},
    {"question": " Dans la topologie en étoile quel est le matériel qui envoie le message à l’ordinateur concernée uniquement  ?","options": ["Switch", "HUB"], "answer": "Switch"},
    {"question": " Une imprimante peut être connectée directement au Hub  ?","options": ["Vrai", "Faux"], "answer": "Vrai"}
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz sur réseau informatique")

        # information de l'etudiant
        self.student_name = tk.StringVar()
        self.student_class = tk.StringVar()

        # Nom et Classe
        tk.Label(root, text="Nom de l'étudiant :", font=("Arial", 12)).pack(pady=5)
        self.name_entry = tk.Entry(root, textvariable=self.student_name, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        tk.Label(root, text="Classe :", font=("Arial", 12)).pack(pady=5)
        self.class_entry = tk.Entry(root, textvariable=self.student_class, font=("Arial", 12))
        self.class_entry.pack(pady=5)

        self.start_button = tk.Button(
            root, text="Commencer le Quiz",
            font=("Arial", 12, "bold"),
            bg="#2ecc71", fg="white",
            padx=15, pady=10,
            width=20, height=2,
            relief="raised",
            borderwidth=3,
            cursor="hand2",
            command=self.start_quiz  # Action du bouton
        )
        self.start_button.pack(pady=10)

    def start_quiz(self):
        if not self.student_name.get() or not self.student_class.get():
            messagebox.showwarning("Erreur", "Veuillez entrer votre nom et votre classe.")
            return

        # Cacher les entrées et le bouton
        self.name_entry.pack_forget()
        self.class_entry.pack_forget()
        self.start_button.pack_forget()

        #Afficher les donnees de l'etudiant
        self.student_info_label = tk.Label(
            self.root, text=f"Étudiant: {self.student_name.get()} | Classe: {self.student_class.get()}",
            font=("Arial", 12, "bold")
        )
        self.student_info_label.pack(pady=10)

        # Initialiser les variables du quiz
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.options_buttons = []
        for i in range(2):
            btn = tk.Button(self.root, text="", font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.options_buttons.append(btn)

        self.load_question()

    def load_question(self):
        question_data = quiz_questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        for i, opt in enumerate(question_data["options"]):
            self.options_buttons[i].config(text=opt)

    def check_answer(self, i):
        question_data = quiz_questions[self.current_question]
        if question_data["options"][i] == question_data["answer"]:
            self.score += 1
        self.current_question += 1

        if self.current_question < len(quiz_questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        student_name = self.student_name.get()
        student_class = self.student_class.get()
        messagebox.showinfo("Résultat", f"{student_name}, votre score : {self.score} / {len(quiz_questions)}")

        # Générer un PDF avec le résultat
        self.generate_pdf(student_name, student_class, self.score)

    def generate_pdf(self, name, student_class, score):
        file_name = f"Resultat_{name}.pdf"
        c = canvas.Canvas(file_name, pagesize=letter)
        c.setFont("Helvetica", 14)

        c.drawString(100, 700, f"Nom de l'étudiant : {name}")
        c.drawString(100, 670, f"Classe : {student_class}")
        c.drawString(100, 640, f"Score obtenu : {score} / {len(quiz_questions)}")
        c.drawString(100, 600, "Félicitations pour votre participation !")

        c.save()
        messagebox.showinfo("PDF généré", f"Le fichier {file_name} a été enregistré.")


# Lancer l'application
root = tk.Tk()
app = QuizApp(root)
root.mainloop()