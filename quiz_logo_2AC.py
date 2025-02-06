import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

quiz_questions = [
    {"question": "Quelle commande permet d'avancer de 100 pas en Logo ?", "options": ["AV 100", "RECULE 100"], "answer": "AV 100"},
    {"question": "Que fait la commande TD 90 en Logo ?", "options": ["Tourne la tortue vers la droite de 90°", "Tourne la tortue vers la gauche de 90°"], "answer": "Tourne la tortue vers la droite de 90°"},
    {"question": "Quelle commande est utilisée pour effacer tout l’écran ?", "options": ["EFFACE", "NETTOIE"], "answer": "NETTOIE"},
    {"question": "Que fait la commande RE en Logo ?", "options": ["Recule la tortue", "Répète une action"], "answer": "Recule la tortue"},
    {"question": "Quelle commande permet de lever le stylo pour que la tortue se déplace sans dessiner ?", "options": ["STYLOLEVE", "STYLOBAISSE"], "answer": "STYLOLEVE"},
    {"question": "Comment répéter une action en Logo ?", "options": ["REPETE nombre [commande]", "BOUCLE nombre [commande]"] , "answer": "REPETE nombre [commande]"},
    {"question": "Quelle commande permet de changer la couleur du stylo ?", "options": ["STYLOCOULEUR", "COULEURPEN"], "answer": "STYLOCOULEUR"},
    {"question": "Quel est l’effet de la commande STP en Logo ?", "options": ["Stoppe l’exécution du programme", "Efface l’écran"], "answer": "Stoppe l’exécution du programme"},
    {"question": "Comment faire tourner la tortue vers la gauche de 45° ?", "options": ["TG 45", "TD 45"], "answer": "TG 45"},
    {"question": "Quelle commande est utilisée pour afficher un message à l’écran ?", "options": ["AFFICHE", "ECRIS"], "answer": "AFFICHE"}
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz sur Logo")

        self.student_name = tk.StringVar()
        self.student_class = tk.StringVar()

        tk.Label(root, text="Nom de l'étudiant :", font=("Arial", 12)).pack(pady=5)
        self.name_entry = tk.Entry(root, textvariable=self.student_name, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        tk.Label(root, text="Classe :", font=("Arial", 12)).pack(pady=5)
        self.class_entry = tk.Entry(root, textvariable=self.student_class, font=("Arial", 12))
        self.class_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Commencer le Quiz", font=("Arial", 12, "bold"), bg="#ff69b4", fg="white", padx=15, pady=10, width=20, height=2, relief="raised", borderwidth=3, cursor="hand2", command=self.start_quiz)
        self.start_button.pack(pady=10)

    def start_quiz(self):
        if not self.student_name.get() or not self.student_class.get():
            messagebox.showwarning("Erreur", "Veuillez entrer votre nom et votre classe.")
            return

        self.name_entry.pack_forget()
        self.class_entry.pack_forget()
        self.start_button.pack_forget()

        self.student_info_label = tk.Label(self.root, text=f"Étudiant: {self.student_name.get()} | Classe: {self.student_class.get()}", font=("Arial", 12, "bold"))
        self.student_info_label.pack(pady=10)

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.options_buttons = []
        for i in range(2):
            btn = tk.Button(self.root, text="", font=("Arial", 12), bg="#ff69b4", fg="white", padx=10, pady=5, width=20, relief="raised", borderwidth=2, command=lambda i=i: self.check_answer(i))
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

root = tk.Tk()
app = QuizApp(root)
root.mainloop()

