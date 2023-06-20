from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from login_manager import login_manager
from tkinter.filedialog import asksaveasfilename, askopenfilename
import os
import mysql.connector
import subprocess


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.logged_in_user_id = None
        self.window.title("CodeQuests")
        self.window.configure(bg="#162334")
        self.window.minsize(1102, 618)
        self.window.maxsize(1102, 618)

        self.connection = mysql.connector.connect(host="localhost", user='root', passwd='', port='3306', database='users')
        self.c = self.connection.cursor()

        logo = ImageTk.PhotoImage(file="images/logo.png")

        self.window.iconphoto(False, logo)

        # Load images

        self.login_image = ImageTk.PhotoImage(file="images/loginb.png")
        self.signup_image = ImageTk.PhotoImage(file="images/signup.png")
        self.option_image = ImageTk.PhotoImage(file="images/options.png")
        self.exit_image = ImageTk.PhotoImage(file="images/exit.png")
        self.back_image = tk.PhotoImage(file="images/back.png")
        self.back_image2 = ImageTk.PhotoImage(file="images/backb.png")
        self.audio_image = ImageTk.PhotoImage(file="images/audiob.png")
        self.language_image = ImageTk.PhotoImage(file="images/languageb.png")
        self.info_image = ImageTk.PhotoImage(file="images/infob.png")
        self.project1img = ImageTk.PhotoImage(file="images/wordcap.png")
        self.project2img = ImageTk.PhotoImage(file="images/cttim.png")
        self.home()
    def home(self):
        self.window.minsize(1102,618)
        self.window.maxsize(1102,618)
        current_directory = os.getcwd()
        os.chdir(current_directory)
        lg_b_imgpath = os.path.join(current_directory, "images/signin.png")
        opt_bg_img = os.path.join(current_directory, "images/optionbg.png")
        og_bg_imgpath = os.path.join(current_directory, "images/test.png")

        self.login_bg_image = Image.open(lg_b_imgpath)
        self.option_bg_image = Image.open(opt_bg_img)
        original_bg_image = Image.open(og_bg_imgpath)

        self.canvas = tk.Canvas(self.window, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)


        resized_bg_image = original_bg_image.resize((1102, 618), Image.ANTIALIAS)

        self.canvas.bg_image = ImageTk.PhotoImage(resized_bg_image)
        self.menu_bg_image = ImageTk.PhotoImage(file="images/menu.png")

        bg_image_item = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.canvas.bg_image)

        
        button1 = tk.Button(self.canvas, image=self.login_image, borderwidth=0, padx=0, pady=0, bg="#162334",
                            activebackground="#162334", command=self.loginpage, highlightthickness=0)
        button1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        button4 = tk.Button(self.canvas, image=self.signup_image, borderwidth=0, padx=0, pady=0, bg="#162334",
                            activebackground="#162334", command=self.registerpage, compound="center")
        button4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        button2 = tk.Button(self.canvas, image=self.option_image, borderwidth=0, padx=0, pady=0, bg="#162334",
                            activebackground="#162334", command=self.option, compound="center")
        button2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        button3 = tk.Button(self.canvas, image=self.exit_image, borderwidth=0, padx=0, pady=0, bg="#162334",
                            activebackground="#162334", command=self.exit, compound="center")
        button3.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    def loginpage(self):
        def back():
            loginc.pack_forget()
            self.home()
        # Menu --------------------------------------------------------
        def menu():
            menu_directory = os.path.dirname(os.path.abspath(__file__))
            os.chdir(menu_directory)

            self.window.minsize(1102,600)
            self.window.maxsize(1102,600)
            query = f"SELECT username, scores FROM users WHERE id = {self.logged_in_user_id}"
            self.c.execute(query)
            result = self.c.fetchone()

            username = result[0] if result else "Default username"
            scores = result[1] if result else "Default scores"

            def psets_clicked():
                def wordcap(psets_canvas):

                    titleimg = ImageTk.PhotoImage(file="images/wordcapitalizationpset.png")
                    def back():
                        coding_frame.pack_forget()
                        nav_menu.pack_forget()
                        psets_clicked()
                    def check_solved_problem_set(user_id, problem_set):
                        query = "SELECT * FROM solved_pset_table WHERE user_id = %s AND problem_sets = %s"
                        self.c.execute(query, (user_id, problem_set))
                        result = self.c.fetchone()

                        if result:
                            return True
                        else:
                            return False
                        
                    def get_solved_problem_set(user_id, problem_set):
                        select_query = "SELECT solved_psets FROM users WHERE id = %s"
                        self.c.execute(select_query, (user_id,))
                        result = self.c.fetchone()
                        existing_problem_sets = result[0] if result else ""

                        # Concatenate the existing problem sets with the new problem set
                        updated_problem_sets = existing_problem_sets + problem_set + ","

                        # Update the "solved_psets" column with the concatenated value
                        update_query = "UPDATE users SET solved_psets = %s WHERE id = %s"
                        self.c.execute(update_query, (updated_problem_sets, user_id))
                        self.connection.commit()

                        # Insert the solved problem set into the "solved_pset_table"
                        insert_query = "INSERT INTO solved_pset_table (user_id, problem_sets) VALUES (%s, %s)"
                        self.c.execute(insert_query, (user_id, problem_set))
                        self.connection.commit()

                    problem_set = "wordcap"

                    psets_canvas.place_forget()
                    psets_canvas.grid_forget()
                    self.window.geometry("1600x900")
                    self.window.minsize(1600,900)
                    self.window.maxsize(1600,900)
                    current_directoryfile = os.getcwd()
                    previous_directoryfile = os.path.join(current_directoryfile, "..")

                    file_path = os.path.join(previous_directoryfile, "data.txt")

                    with open('login_status.txt', 'r') as file:
                        login_status = file.read()

                    # Check login status
                    if login_status == 'Logged in':
                        print("User is logged in")
                    else:
                        print("User is not logged in")

                    #images
                    script_directory = os.path.dirname(os.path.abspath(__file__))
                    os.chdir(script_directory)

                    def set_file_path(path):
                        global file_path
                        file_path = path
                
                    ### WIP ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    def run():
                        if file_path == '':
                            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
                            if not path.endswith('.py'):
                                path += '.py'
                        else:
                            path = file_path

                        with open(path, 'w') as file:
                            code = editor.get('1.0', END)
                            file.write(code)
                            set_file_path(path)

                        if file_path:
                            command = ["python", file_path]

                            # test cases
                            try:
                                expected_inputs = ["apPLe", "konjac", "cArL"]
                                desired_outputs = ["ApPLe", "Konjac", "CArL"]
                                testcasesint = 0
                                outputs = []
                                for value, desired_output in zip(expected_inputs, desired_outputs):
                                    output = subprocess.check_output(
                                        command,
                                        stderr=subprocess.STDOUT,
                                        universal_newlines=True,
                                        input=value
                                    )
                                    outputs.append(output.strip())

                                    lines = output.strip().split('\n')
                                    last_line = lines[-1]

                                    c_output.config(state=NORMAL)
                                    c_output.delete('1.0', END)
                                    c_output.insert(END, last_line)
                                    c_output.config(state=DISABLED)

                                    if last_line == desired_output:
                                        testcasesint += 1

                                    print(testcasesint)
                                    
                                    if testcasesint == len(expected_inputs):
                                        tc1.configure(image=None)
                                        tc1.configure(image=self.acceptedimg)
                                        score_value = 1
                                        if check_solved_problem_set(self.logged_in_user_id, problem_set):
                                            result = None
                                        else:
                                            query = "UPDATE users SET scores = scores + %s WHERE id = %s"
                                            self.c.execute(query, (score_value, self.logged_in_user_id))
                                            self.connection.commit()
                                            get_solved_problem_set(self.logged_in_user_id, problem_set)
                                            print("Congratulations! You have solved the problem set.")

                                    else:
                                        tc1.configure(image=None)
                                        tc1.configure(image=self.wrongoutputimg)

                            except subprocess.CalledProcessError as e:
                                output = e.output
                                c_output.config(state=NORMAL)
                                c_output.delete('1.0', END)
                                c_output.insert(END, output)
                                c_output.config(state=DISABLED)

                    capitalization = [
                        "Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.",
                        "Note, that during capitalization all the letters except the first one remains unchanged.",
                    ]

                    coding_frame = Frame(self.window, background="#2F496B")
                    coding_frame.pack(fill=BOTH, expand=True)
                    editor = Text(coding_frame, background="#182B44", fg="#FCCD60", height=45, font=("Cascadia Code", 10))
                    c_output = Text(coding_frame, font=("Cascadia Code", 10), background="#6DB5E7", state=DISABLED)

                    editor.pack(fill=BOTH)
                    c_output.pack(fill=BOTH)

                    # Navigation bar
                    nav_menu = Frame(self.window, background="#162334")
                    nav_menu.configure(width=500)

                    # Navigation bar buttons and labels
                    heading_label = Label(nav_menu, image=titleimg, background="#162334", fg="#F58219", font=("Arial", 24, "bold"))
                    heading_label.image = titleimg
                    heading_label.pack(padx=0, pady=50)

                    context_label = Label(nav_menu, text="", background="#162334", fg="#FFBD59", font=("Arial", 13), wraplength=450)
                    context_label.pack(padx=0, pady=20)

                    context_label2 = Label(nav_menu, text="", background="#162334", fg="#FFBD59", font=("Arial", 13), wraplength=450)
                    context_label2.pack(padx=0, pady=20)

                    context_label3 = Label(nav_menu, text="Input:  ", background="#162334", fg="#FFBD59", font=("Arial", 16, "bold"))
                    context_label3.pack(anchor="w", padx=40, pady=10)

                    context_label4 = Label(nav_menu, text="apPLe", background="#162334", fg="#FFBD59", font=("Arial", 13 ), justify="left", anchor="w", wraplength=500)
                    context_label4.pack(padx=0, pady=10)

                    context_label5 = Label(nav_menu, text="Ouput:", background="#162334", fg="#FFBD59", font=("Arial", 16, "bold"))
                    context_label5.pack(anchor="w", padx=40, pady=10)

                    context_label6 = Label(nav_menu, text="ApPLe", background="#162334", fg="#FFBD59", font=("Arial", 13))
                    context_label6.pack(padx=0, pady=10)

                    button1 = Button(nav_menu, image=self.button1img, background="#162334", bd=0, highlightthickness=0, activebackground="#162334", command=run)
                    button1.pack(padx=0, pady=50)

                    tc1 = Label(nav_menu, image="", background="#162334", fg="#FF5757", font=("Arial", 24, "bold"))
                    tc1.pack(padx=0,pady=10)

                    back_button = Button(nav_menu, image=self.back_buttonimg, bg="#162334", bd=0, activebackground="#2f4460", command=back)
                    back_button.pack(padx=0, pady=50, anchor="s")

                    context_label.configure(text=capitalization[0])
                    context_label2.configure(text=capitalization[1])


                    # gridding
                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)

                    #placements
                    coding_frame.grid(row=0, column=1, sticky='nsew')
                    nav_menu.grid(row=0, column=0, sticky='ns')
                    nav_menu.pack_propagate(0)
                    print("Clicked")

                def ctt():
                    titleimg = ImageTk.PhotoImage(file="images/ctt.png")
                    def back():
                        coding_frame.pack_forget()
                        nav_menu.pack_forget()
                        psets_clicked()
                    def check_solved_problem_set(user_id, problem_set):
                        query = "SELECT * FROM solved_pset_table WHERE user_id = %s AND problem_sets = %s"
                        self.c.execute(query, (user_id, problem_set))
                        result = self.c.fetchone()

                        if result:
                            return True
                        else:
                            return False
                        
                    def get_solved_problem_set(user_id, problem_set):
                        select_query = "SELECT solved_psets FROM users WHERE id = %s"
                        self.c.execute(select_query, (user_id,))
                        result = self.c.fetchone()
                        existing_problem_sets = result[0] if result else ""
                        
                        updated_problem_sets = existing_problem_sets + problem_set + ","

                        update_query = "UPDATE users SET solved_psets = %s WHERE id = %s"
                        self.c.execute(update_query, (updated_problem_sets, user_id))
                        self.connection.commit()

                        insert_query = "INSERT INTO solved_pset_table (user_id, problem_sets) VALUES (%s, %s)"
                        self.c.execute(insert_query, (user_id, problem_set))
                        self.connection.commit()

                    problem_set = "CTT"
                    psets_canvas.place_forget()
                    psets_canvas.grid_forget()
                    self.window.minsize(1600,900)
                    self.window.maxsize(1600,900)
                    current_directoryfile = os.getcwd()
                    previous_directoryfile = os.path.join(current_directoryfile, "..")
                    file_path = os.path.join(previous_directoryfile, "data.txt")

                    with open('login_status.txt', 'r') as file:
                        login_status = file.read()

                    # Check login status
                    if login_status == 'Logged in':
                        print("User is logged in")
                    else:
                        print("User is not logged in")

                    #images
                    script_directory = os.path.dirname(os.path.abspath(__file__))
                    os.chdir(script_directory)
                    
                    def set_file_path(path):
                        global file_path 
                        file_path = path

                    def run():
                        if file_path == '':
                            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
                            if not path.endswith('.py'):
                                path += '.py'
                        else:
                            path = file_path

                        with open(path, 'w') as file:
                            code = editor.get('1.0', END)
                            file.write(code)
                            set_file_path(path)

                        if file_path:
                            command = ["python", file_path]

                            try:
                                expected_inputsdenelle = ["5 6 7", "17 28 30", "1 2 3"]
                                expected_inputsjim = ["3 6 10", "99 16 8", "3 2 1"]
                                desired_outputs = ["1 1", "2 1", "1 1"]
                                testcases_solved = 0
                                outputs = []

                                for i in range(len(expected_inputsdenelle)):
                                    denelle_input = expected_inputsdenelle[i]
                                    jim_input = expected_inputsjim[i]
                                    expected_output = desired_outputs[i]

                                    user_output = subprocess.check_output(command, input=f"{denelle_input}\n{jim_input}\n", encoding='utf-8').strip()

                                    if user_output == expected_output:
                                        testcases_solved += 1
                                    outputs.append(user_output)

                                c_output.configure(state=NORMAL)
                                c_output.delete('1.0', END)
                                c_output.insert(END, '\n'.join(outputs))
                                c_output.configure(state=DISABLED)

                                if testcases_solved == len(expected_inputsdenelle):
                                    tc1.configure(image=None)
                                    tc1.configure(image=self.acceptedimg)
                                    score_value = 1

                                    if check_solved_problem_set(self.logged_in_user_id, problem_set):
                                        result = None
                                    else:
                                        query = "UPDATE users SET scores = scores + %s WHERE id = %s"
                                        self.c.execute(query, (score_value, self.logged_in_user_id))
                                        self.connection.commit()
                                        get_solved_problem_set(self.logged_in_user_id, problem_set)
                                        print("Congratulations! You have solved the problem set.")
                                else:
                                    tc1.configure(image=None)
                                    tc1.configure(image=self.wrongoutputimg)

                            except Exception as e:
                                c_output.configure(state=NORMAL)
                                c_output.delete('1.0', END)
                                c_output.insert(END, str(e))
                                c_output.configure(state=DISABLED)
                                
                        else:
                            print("No file path set.")


                    capitalization = [
                        "The rating of Denelle's challenge is the triplet a = (a[0], a[1], a[2]) and for Jim's challenge is the triplet b = (b[0], b[1], b[2])",
                        "The task is to the find their comparison points by comparing a[0] with b[0], a[1] with b[1], with a[2] with b[2]\n\nIf a[i] > b[i], then Denelle is awarded 1 point\nIf a[i] < b[i], then Jim is awarded 1 pont.\nIf a[i] = b[i], then neither person receives a point.",
                    ]

                    coding_frame = Frame(background="#2F496B")
                    coding_frame.pack(fill=BOTH, expand=True)
                    editor = Text(coding_frame, background="#182B44", fg="#FCCD60", height=45, font=("Cascadia Code", 10))
                    c_output = Text(coding_frame, font=("Cascadia Code", 10), background="#6DB5E7", state=DISABLED)

                    editor.pack(fill=BOTH)
                    c_output.pack(fill=BOTH)

                    nav_menu = Frame(self.window, background="#162334")
                    nav_menu.configure(width=500)

                    heading_label = Label(nav_menu, image=titleimg, background="#162334", fg="#F58219", font=("Arial", 24, "bold"))
                    heading_label.image = titleimg
                    heading_label.pack(padx=0, pady=50)

                    context_label = Label(nav_menu, text="", background="#162334", fg="#FFBD59", font=("Arial", 13), wraplength=450)
                    context_label.pack(padx=0, pady=20)

                    context_label2 = Label(nav_menu, text="", background="#162334", fg="#FFBD59", font=("Arial", 13), wraplength=450)
                    context_label2.pack(padx=0, pady=20)

                    context_label3 = Label(nav_menu, text="Input:  ", background="#162334", fg="#FFBD59", font=("Arial", 16, "bold"))
                    context_label3.pack(anchor="w", padx=40, pady=10)

                    context_label4 = Label(nav_menu, text="5 6 7\n3 6 10", background="#162334", fg="#FFBD59", font=("Arial", 13 ), justify="left", anchor="w", wraplength=500)
                    context_label4.pack(padx=0, pady=10)

                    context_label5 = Label(nav_menu, text="Ouput:", background="#162334", fg="#FFBD59", font=("Arial", 16, "bold"))
                    context_label5.pack(anchor="w", padx=40, pady=10)

                    context_label6 = Label(nav_menu, text="1 1", background="#162334", fg="#FFBD59", font=("Arial", 13))
                    context_label6.pack(padx=0, pady=10)

                    button1 = Button(nav_menu, image=self.button1img, background="#162334", bd=0, highlightthickness=0, activebackground="#162334", command=run)
                    button1.pack(padx=0, pady=10)

                    tc1 = Label(nav_menu, image="", background="#162334", fg="#FF5757", font=("Arial", 24, "bold"))
                    tc1.pack(padx=0,pady=10)

                    back_button = Button(nav_menu, image=self.back_buttonimg, bg="#162334", bd=0, activebackground="#2f4460", command=back)
                    back_button.pack(padx=0, pady=00, anchor="s")




                    context_label.configure(text=capitalization[0])
                    context_label2.configure(text=capitalization[1])

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)

                    coding_frame.grid(row=0, column=1, sticky='nsew')
                    nav_menu.grid(row=0, column=0, sticky='ns')
                    nav_menu.pack_propagate(0)
                
                def itr():
                    titleimg = ImageTk.PhotoImage(file="images/itr.png")
                    def back():
                        coding_frame.pack_forget()
                        nav_menu.pack_forget()
                        psets_clicked()
                    def check_solved_problem_set(user_id, problem_set):
                        query = "SELECT * FROM solved_pset_table WHERE user_id = %s AND problem_sets = %s"
                        self.c.execute(query, (user_id, problem_set))
                        result = self.c.fetchone()

                        if result:
                            return True
                        else:
                            return False

                    def get_solved_problem_set(user_id, problem_set):
                        select_query = "SELECT solved_psets FROM users WHERE id = %s"
                        self.c.execute(select_query, (user_id,))
                        result = self.c.fetchone()
                        existing_problem_sets = result[0] if result else ""

                        updated_problem_sets = existing_problem_sets + problem_set + ","

                        update_query = "UPDATE users SET solved_psets = %s WHERE id = %s"
                        self.c.execute(update_query, (updated_problem_sets, user_id))
                        self.connection.commit()

                        insert_query = "INSERT INTO solved_pset_table (user_id, problem_sets) VALUES (%s, %s)"
                        self.c.execute(insert_query, (user_id, problem_set))
                        self.connection.commit()

                    problem_set = "ITR"
                    psets_canvas.place_forget()
                    psets_canvas.grid_forget()
                    self.window.minsize(1600,900)
                    self.window.maxsize(1600,900)
                    current_directoryfile = os.getcwd()
                    previous_directoryfile = os.path.join(current_directoryfile, "..")
                    file_path = os.path.join(previous_directoryfile, "data.txt")
                    print(current_directoryfile)
                    with open('login_status.txt', 'r') as file:
                        login_status = file.read()

                    # Check login status
                    if login_status == 'Logged in':
                        print("User is logged in")
                    else:
                        print("User is not logged in")

                    #images
                    script_directory = os.path.dirname(os.path.abspath(__file__))
                    os.chdir(script_directory)

                    def set_file_path(path):
                        global file_path 
                        file_path = path

                    def run():
                        if file_path == '':
                            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
                            if not path.endswith('.py'):
                                path += '.py'
                        else:
                            path = file_path

                        with open(path, 'w') as file:
                            code = editor.get('1.0', END)
                            file.write(code)
                            set_file_path(path)

                        if file_path:
                            command = ["python", file_path]

                            try:
                                expected_inputs = ["3", "58", "1994"]
                                desired_outputs = ["III", "LVIII", "MCMXCIV"]
                                testcases_solved = 0
                                outputs = []

                                for i in range(len(expected_inputs)):
                                    input_num = expected_inputs[i]
                                    expected_output = desired_outputs[i]

                                    user_output = subprocess.check_output(command, input=f"{input_num}\n", encoding='utf-8').strip()

                                    if user_output == expected_output:
                                        testcases_solved += 1
                                    outputs.append(user_output)

                                c_output.configure(state=NORMAL)
                                c_output.delete('1.0', END)
                                c_output.insert(END, '\n'.join(outputs))
                                c_output.configure(state=DISABLED)

                                if testcases_solved == len(expected_inputs):
                                    tc1.configure(image=None)
                                    tc1.configure(image=self.acceptedimg)
                                    score_value = 1

                                    if check_solved_problem_set(self.logged_in_user_id, problem_set):
                                        result = None
                                    else:
                                        query = "UPDATE users SET scores = scores + %s WHERE id = %s"
                                        self.c.execute(query, (score_value, self.logged_in_user_id))
                                        self.connection.commit()
                                        get_solved_problem_set(self.logged_in_user_id, problem_set)
                                        print("Congratulations! You have solved the problem set.")
                                else:
                                    tc1.configure(image=None)
                                    tc1.configure(image=self.wrongoutputimg)

                            except Exception as e:
                                c_output.configure(state=NORMAL)
                                c_output.delete('1.0', END)
                                c_output.insert(END, str(e))
                                c_output.configure(state=DISABLED)

                        else:
                            print("No file path set.")

                    capitalization = [
                        "The task is to convert an integer to a Roman numeral.",
                        "The test cases are as follows:",
                        "Input: 3\nOutput: III",
                        "Input: 58\nOutput: LVIII",
                        "Input: 1994\nOutput: MCMXCIV"
                    ]

                    coding_frame = Frame(background="#2F496B")
                    coding_frame.pack(fill=BOTH, expand=True)
                    editor = Text(coding_frame, background="#182B44", fg="#FCCD60", height=45, font=("Cascadia Code", 10))
                    c_output = Text(coding_frame, font=("Cascadia Code", 10), background="#6DB5E7", state=DISABLED)

                    editor.pack(fill=BOTH)
                    c_output.pack(fill=BOTH)
                    print(current_directory)
                    nav_menu = Frame(self.window, background="#162334")
                    nav_menu.configure(width=500)

                    heading_label = Label(nav_menu, image=titleimg, background="#162334", fg="#F58219", font=("Arial", 24, "bold"))
                    heading_label.image = titleimg
                    heading_label.pack(padx=0, pady=50)

                    context_label = Label(nav_menu, text="", background="#162334", fg="#FFBD59", font=("Arial", 13), wraplength=450)
                    context_label.pack(padx=0, pady=20)

                    context_label2 = Label(nav_menu, text="", background="#162334", fg="#FFBD59", font=("Arial", 13), wraplength=450)
                    context_label2.pack(padx=0, pady=20)

                    context_label3 = Label(nav_menu, text="Input:  ", background="#162334", fg="#FFBD59", font=("Arial", 16, "bold"))
                    context_label3.pack(anchor="w", padx=40, pady=10)

                    context_label4 = Label(nav_menu, text="3\n58\n1994", background="#162334", fg="#FFBD59", font=("Arial", 13 ), justify="left", anchor="w", wraplength=500)
                    context_label4.pack(padx=0, pady=10)

                    context_label5 = Label(nav_menu, text="Ouput:", background="#162334", fg="#FFBD59", font=("Arial", 16, "bold"))
                    context_label5.pack(anchor="w", padx=40, pady=10)

                    context_label6 = Label(nav_menu, text="III\nLVIII\nMCMXCIV", background="#162334", fg="#FFBD59", font=("Arial", 13))
                    context_label6.pack(padx=0, pady=10)

                    button1 = Button(nav_menu, image=self.button1img, background="#162334", bd=0, highlightthickness=0, activebackground="#162334", command=run)
                    button1.pack(padx=0, pady=10)

                    tc1 = Label(nav_menu, image="", background="#162334", fg="#FF5757", font=("Arial", 24, "bold"))
                    tc1.pack(padx=0,pady=10)

                    back_button = Button(nav_menu, image=self.back_buttonimg, bg="#162334", bd=0, activebackground="#2f4460", command=back)
                    back_button.pack(padx=0, pady=00, anchor="s")

                    context_label.configure(text=capitalization[0])
                    context_label2.configure(text=capitalization[1])

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)

                    coding_frame.grid(row=0, column=1, sticky='nsew')
                    nav_menu.grid(row=0, column=0, sticky='ns')
                    nav_menu.pack_propagate(0)

                def back():
                    psets_canvas.pack_forget()
                    menu()
                ### WIP ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                current_directory = os.getcwd()
                script_dir = os.path.join(current_directory, 'IDEs', 'images')

                button1imgpath = os.path.join(current_directory, "images/Play.png")
                button1tk = Image.open(button1imgpath)
                self.button1img = ImageTk.PhotoImage(file=button1imgpath)

                button2imgpath = os.path.join(current_directory, "images/Save.png")
                button2tk = Image.open(button2imgpath)
                self.button2img = ImageTk.PhotoImage(file=button2imgpath)

                title2imgpath = os.path.join(current_directory, "images/wordcapitalization.png")
                title2tk = Image.open(title2imgpath)
                self.title2img = ImageTk.PhotoImage(file=title2imgpath)

                acceptedimgpath = os.path.join(current_directory, "images/Accepted.png")
                acceptedtk = Image.open(acceptedimgpath)
                self.acceptedimg = ImageTk.PhotoImage(file=acceptedimgpath)

                wrongoutputimgpath = os.path.join(current_directory, "images/wrongoutput.png")
                wrongoutputtk = Image.open(wrongoutputimgpath)
                self.wrongoutputimg = ImageTk.PhotoImage(file=wrongoutputimgpath)

                back_buttonimgpath = os.path.join(current_directory, "images/backb.png")
                back_buttontk = Image.open(back_buttonimgpath)
                self.back_buttonimg = ImageTk.PhotoImage(image=back_buttontk)
                
                menuc.pack_forget()
                loginc.pack_forget()

                self.window.minsize(1102,618)
                self.window.maxsize(1102,618)

                bg_image = Image.open("images/psetsbg.png")
                self.bg_photo = ImageTk.PhotoImage(bg_image)
                pset_image = Image.open("images/problemsetsimg.png")
                self.pset_img = ImageTk.PhotoImage(pset_image)
                wc_image = Image.open("images/wordcapitalizationpset.png")
                self.wc_img = ImageTk.PhotoImage(wc_image)
                ctt_image = Image.open("images/ctt.png")
                self.ctt_img = ImageTk.PhotoImage(ctt_image)
                itr_image = Image.open("images/itr.png")
                self.itr_img = ImageTk.PhotoImage(itr_image)
                backimage = Image.open("images/backb.png")
                self.back_buttonimg = ImageTk.PhotoImage(backimage)


                psets_canvas = tk.Canvas(self.window, highlightthickness=0, bg="#162334")
                psets_canvas.place(x=0, y=0, relwidth=1, relheight=1)
                psets_canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

                title = Label(psets_canvas, image=self.pset_img, bg="#162334")
                title.pack(padx=10, pady=50)

                pset1_button = Button(psets_canvas, image=self.wc_img, bg="#162334", bd=0, command=lambda: wordcap(psets_canvas), activebackground="#2f4460")
                pset1_button.pack(padx=10, pady=10)

                pset2_button = Button(psets_canvas, image=self.ctt_img, bg="#162334", bd=0, command=ctt, activebackground="#2f4460")
                pset2_button.pack(padx=10, pady=10)

                pset3_button = Button(psets_canvas, image=self.itr_img, bg="#162334", bd=0, command=itr, activebackground="#2f4460")
                pset3_button.pack(padx=10, pady=10)

                back_button = Button(psets_canvas, image=self.back_buttonimg, bg="#162334", bd=0, command=back, activebackground="#2f4460")
                back_button.place(relx=0.85, rely=0.9, anchor="se")

            def python_clicked():
                menu_directory = os.path.dirname(os.path.abspath(__file__))
                os.chdir(menu_directory)
                self.window.minsize(1600,900)
                self.window.maxsize(1600,900)
                current_directory = os.getcwd()

                introd = ImageTk.PhotoImage(file="images/introd.png")
                def back():
                    course_window.pack_forget()
                    nav_bar.pack_forget()
                    menu()

                def launch_py(script_name):
                    pass

                def pyintroduction():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'pythoncourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    python_logo = ImageTk.PhotoImage(file="images/python_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        python_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Lesson 1: Introduction"
                        lesson_content = [
                            ("Python is a programming language. It was created by Guido van Rossum and released in 1991.", None),
                            ("It is used for:", None),
                            ("- Web Development", None),
                            ("- Software Development", None),
                            ("- Mathematics", None),
                            ("- System Scripting", None),
                            ("Python is a versatile programming language that may be used to build online applications on a server, "
                            "workflows with other programs, and connections to database systems. It can handle massive amounts of data, "
                            "carry out difficult mathematical operations, read and alter files, and produce software that is suitable "
                            "for production. It can also be used for rapid prototyping.", None),
                            ("In this tutorial, Python will be written in a text editor for this session. Python can be written in an "
                            "Integrated Development Environment (IDE) like Thonny, PyCharm, NetBeans, or Eclipse. These IDEs are "
                            "especially helpful when managing bigger collections of Python files.", None)
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "Lesson 2: Let's Get Started!"
                        lesson_content = [
                            ("Many PCs and Macbooks or Macs will have python already installed.\n\nTo Check if you have python install on a Windows PC, search in the start bar for Python or run the following on the Command Line (cmd.exe)", None),
                            ("Just type \"python --version\" on your command line", None),
                            ("You can run a python file in your command line if you type \"python filename.py\"", None),
                            ("You can try a short amount of code in python if you type \"python\" or \"py\"", None),
                            ("After typing, you can now write your very first command! You can type \"print(\"Hello World!\")", "images/pythonlesson11st.png"),
                            ("Just like this!", None),
                            ("Whenever you're done with your python command, you can simply quit the python command line using: \"exit()\"", "images/exitcmd.png"),
                        ]
                        update_label(lesson2_title, *lesson_content)


                    def lesson3_clicked():
                        lesson3_title = "Lesson 3: Indentation"
                        lesson_content = [
                            ("Python indentation is an important one to remember in writing a Python program. Python is very sensitive in reading indentation. For example, when writing an if statement, you would need to put an indentation to tell the compiler that that line of code is INSIDE the if statement.\n\n Like this:", "images/indentation.png"),
                            ("Notice python uses : not like the other progamming languages, it uses { } (Curly Brackets).\n\n Just like in CPP or C++:", "images/indentation.png"),
                            ("For upcoming screenshots, these are examples that gives you an error if wrote it in your program", "images/pyindentation2.py.png"),
                            ("", "images/pyindentation3.png"),
                            ("These are all wrong for making Some of it would still run, but it's still wrong it wouldn't be inside the if statement."),
                            ("Remember to be careful with your indentation when it comes to writing your python program!", None),
                            (" ", None),
                        ]
                        update_label(lesson3_title, *lesson_content)

                    title2 = Label(lmenu, image=python_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = python_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Introduction", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Get Started!", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    lesson3_button = Button(lmenu, text="Indentation", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def pyvariablesc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'pythoncourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    python_logo = ImageTk.PhotoImage(file="images/python_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        python_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Lesson 1: Variables"
                        lesson_content = [
                                ("Python has no command for declaring a variable"
                                "\nA variable is created the moment you assign a value to it", "images/pyvariables1.png"),
                                ("In this example, the x is an integer, and y is a string."
                                " It does not need to be declared with any particular type, and can even change type after they have been set.", None),
                                ("Many Values to Multiple Variables", None),
                                ("Python allows you to assign values to multiple variables in one line:", "images/pyvariables3.png"),
                                ("Note: Make sure the number of variables matches the number of values, or else you will get an error.", None),
                                ("One Value to Multiple Variables", None),
                                ("And you can assign the same value to multiple variables in one line:", "images/pyvariables4.png"),
                                ("Unpack a Collection"
                                "\n\nIf you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.", "images/pyvariables5.png"),
                            ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "Casting"
                        lesson_content = [
                            ("If you want to specify the data type of a variable, this can be done with casting.", "images/pyvariables2.png"),
                            ("", None),
                        ]
                        update_label(lesson2_title, *lesson_content)


                    def lesson3_clicked():
                        lesson3_title = "Global Variables"
                        lesson_content = [
                            ("Variables that are created outside of a function (as in all of the examples above) are known as global variables."
                            " Global variables can be used by everyone, both inside of functions and outside.", None),
                            ("Example"
                            "\nCreate a variable outside of a function, and use it inside the function", "images/pyvariables6.png"),
                            ("If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function."
                            " The global variable with the same name will remain as it was, global and with the original value.", None),
                            ("The global Keyword"
                            "Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function."
                            "\n\nTo create a global variable inside a function, you can use the global keyword.", "images/pyvariables7.png"),
                        ]
                        update_label(lesson3_title, *lesson_content)

                    title2 = Label(lmenu, image=python_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = python_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Variables", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Casting", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    lesson3_button = Button(lmenu, text="Global Variables", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def pymathc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'pythoncourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    python_logo = ImageTk.PhotoImage(file="images/python_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        python_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Built-in Math Functions"
                        lesson_content = [
                            ("The min() and max() functions can be used to find the lowest or highest value in an iterable:", "images/pymath1.png"),
                            ("The abs() function returns the absolute (positive) value of the specified number:", "images/pymath2.png"),
                            ("The pow(x, y) function returns the value of x to the power of y (xy).", "images/pymath3.png"),
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "The Math Module"
                        lesson_content = [
                            ("Python has also a built-in module called math, which extends the list of mathematical functions."
                            "\n\nTo use it, you must import the math module:", "images/pymath4.png"),
                            ("When you have imported the math module, you can start using methods and constants of the module."
                            "\n\nThe math.sqrt() method at the example, returns the square root of a number:", None),
                            ("The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:"
                            ,"images/pymath5.png"),
                            ("The math.pi constant, returns the value of PI (3.14...):", "images/pymath6.png")
                        ]
                        update_label(lesson2_title, *lesson_content)

                    title2 = Label(lmenu, image=python_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = python_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Built-in Math Functions", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Math Library", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def pyconditionsc():

                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'pythoncourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    python_logo = ImageTk.PhotoImage(file="images/python_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        python_clicked()

                    def lesson1_clicked(): 
                        lesson1_title ="Python Conditions and If statements"
                        lesson_content = [
                            ("Python supports the usual logical conditions from mathematics:"
                            "\n\n - Equals: a == b"
                            "\n\n - Not Equals: a != b"
                            "\n\n - Less than: a < b"
                            "\n\n - Less than or equal to: a <= b"
                            "\n\n - Greater than: a > b"
                            "\n\n - Greater than or equal to: a >= b", None),
                            ("These conditions can be used in several ways, most commonly in \"if statements\" and loops."
                            "\n\nAn \"if statement\" is written by using the if keyword.", "images/pyconditions1.png"),
                            ("In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a."
                            " As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that \"b is greater than a\".", None)
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "Indentation"
                        lesson_content = [
                            ("Python relies on indentation (whitespace at the beginning of a line) to define scope in the code."
                            " Other programming languages often use curly-brackets for this purpose.", None),
                            ("If statement, without indentation (will raise an error):", "images/pyconditions2.png"),
                            ("Notice the little indicator below the \"print\" function, It's indicating an error thus without indentation the if statement wouldn't work and could lead to an error.", None),
                        ]
                        update_label(lesson2_title, *lesson_content)


                    def lesson3_clicked():
                        lesson3_title = "Elif"
                        lesson_content = [
                            ("The elif keyword is Python's way of saying \"if the previous conditions were not true, then try this condition\".", "images/pyconditions3.png"),
                            ("In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that \"a and b are equal\".", None),
                        ]
                        update_label(lesson3_title, *lesson_content)

                    def lesson4_clicked():
                        lesson4_title = "Else"
                        lesson_content = [
                            ("The else keyword catches anything which isn't caught by the preceding conditions.", "images/pyconditions4.png"),
                            ("In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that \"a is greater than b\".", None),
                            ("You can also have an else without the elif", None)
                        ]
                        update_label(lesson4_title, *lesson_content)

                    def lesson5_clicked():
                        lesson5_title = "Short Hand If"
                        lesson_content = [
                            ("If you have only one statement to execute, you can put it on the same line as the if statement.", "images/pyconditions5.png"),
                            ("This technique is known as Ternary Operators, or Conditional Expressions.", None),
                            ("You can also have multiple else statements on the same line:", "images/pyconditions6.png"),
                            ("And", None),
                            ("The and keyword is a logical operator, and is used to combine conditional statements:", "images/pyconditions7.png"),
                            ("Or", None),
                            ("The or keyword is a logical operator, and is used to combine conditional statements:", "images/pyconditions8.png"),
                            ("Not", None),
                            ("The not keyword is a logical operator, and is used to reverse the result of the conditional statement:", "images/pyconditions9.png"),
                            ("Nested If", None),
                            ("You can have if statements inside if statements, this is called nested if statements.", "images/pyconditions10.png"),
                            ("The pass Statement", None),   
                            ("if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error."
                            , "images/pyconditions11.png")
                        ]
                        update_label(lesson5_title, *lesson_content)

                    title2 = Label(lmenu, image=python_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = python_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="If Statements", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Indentations", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    lesson3_button = Button(lmenu, text="Elif Statements", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)

                    lesson4_button = Button(lmenu, text="Else", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson4_clicked, bd=0, activebackground="#243142")
                    lesson4_button.pack(padx=10, pady=10)
                    
                    lesson5_button = Button(lmenu, text="Short Hand", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson5_clicked, bd=0, activebackground="#243142")
                    lesson5_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def pyloopingc():

                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'pythoncourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    python_logo = ImageTk.PhotoImage(file="images/python_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        python_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Python For Loops"
                        lesson_content = [
                            ("A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)."
                            "\n\nThis is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages."
                            "\n\nWith the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.", "images/pylooping1.png"),
                            ("The for loop does not require an indexing variable to set beforehand.", None),
                            ("Looping Through a String", None),
                            ("Even strings are iterable objects, they contain a sequence of characters:", "images/pylooping2.png"),
                            ("The Break Statement", None),
                            ("With the break statement we can stop the loop before it has looped through all the items:", "images/pylooping3.png"),
                            ("The continue Statement", None),
                            ("With the continue statement we can stop the current iteration of the loop, and continue with the next:", "images/pylooping4.png"),
                            ("The range() Function", None),
                            ("To loop through a set of code a specified number of times, we can use the range() function,"
                            "The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.", "images/pylooping5.png"),
                            ("Note that range(6) is not the values of 0 to 6, but the values 0 to 5.", None),
                            ("The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):", None),
                            ("The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):", None),
                            ("Else in For Loop", None),
                            ("The else keyword in a for loop specifies a block of code to be executed when the loop is finished:", "images/pylooping6.png"),
                            ("Nested Loops", None),
                            ("A nested loop is a loop inside a loop."
                            "\nThe \"inner loop\" will be executed one time for each iteration of the \"outer loop\":", "images/pylooping7.png")
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "While Loops"
                        lesson_content = [
                            ("Python has two primitive loop commands:"
                            "\n\n - while loops"
                            "\n\n - for loops", None),
                            ("With the while loop we can execute a set of statements as long as a condition is true.", "images/pylooping8.png"),
                            ("The Break Statement", None),
                            ("With the break statement we can stop the loop even if the while condition is true:", "images/pylooping9.png")
                        ]
                        update_label(lesson2_title, *lesson_content)

                    title2 = Label(lmenu, image=python_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = python_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="For Loops", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="While Loops", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")


                def pyfunctionsc():
 
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'pythoncourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    python_logo = ImageTk.PhotoImage(file="images/python_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        python_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Functions"
                        lesson_content = [
                            ("A function is a block of code which only runs when it is called."
                            " You can pass data, known as parameters, into a function."
                            " A function can return data as a result.", None),
                            ("Creating a Function", None),
                            ('In Python a function is defined using the def keyword:', "images/pyfunctions1.png"),
                            ("Calling a Function", None),
                            ("To call a function, use the function name followed by parenthesis", "images/pyfunctions2.png"),
                            ("Arguments", None),
                            ("Information can be passed into functions as arguments."
                            " Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma."
                            "\n\nThe following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:", "images/pyfunctions3.png"),
                            ("Parameters or Arguments?", None),
                            ("\nThe terms parameter and argument can be used for the same thing: information that are passed into a function.", None),
                            ("From a function's perspective:"
                            "\nA parameter is the variable listed inside the parentheses in the function definition. An argument is the value that is sent to the function when it is called.", None),
                            ("Number of Arguments", None),
                            ("By default, a function must be called with the correct number of arguments."
                            " Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.", "images/pyfunctions4.png"),
                            ("Arbitrary Arguments, *args"
                            "\n\nIf you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition."
                            "\n\nThis way the function will receive a tuple of arguments, and can access the items accordingly:", "images/pyfunctions5.png"),
                        ]
                        update_label(lesson1_title, *lesson_content)

                    title2 = Label(lmenu, image=python_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = python_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Functions", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")


                def pyfilehandlingc():

                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'pythoncourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    python_logo = ImageTk.PhotoImage(file="images/python_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        python_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "File Handling"
                        lesson_content = [
                            ("The key function for working with files in Python is the open() function."
                            "\n\nThe open() function takes two parameters; filename, and mode.", None),
                            ("There are four different methods (modes) for opening a file:"
                            "\n\n - \"r\" - Read - Default value. Opens a file for reading, error if the file does not exist"
                            "\n\n - \"a\" - Append - Opens a file for appending, creates the file if it does not exist"
                            "\n\n - \"w\" - Write - Opens a file for writing, creates the file if it does not exist"
                            "\n\n - \"x\" - Create - Creates the specified file, returns an error if the file exists"
                            "\n\n - \"t\" - Text - Default value. Text mode"
                            "\n\n - \"b\" - Binary - Binary mode (e.g. images)", None),
                            ("To open a file for reading it is enough to specify the name of the file:", "images/pyfilehandling1.png"),
                            ("", "images/pyfilehandling2.png"),
                            ("Because \"r\" for read, and \"t\" for text are the default values, you do not need to specify them.", None)
                        ]
                        update_label(lesson1_title, *lesson_content)

                    title2 = Label(lmenu, image=python_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = python_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="File handling", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")


                def pyinheritancec():


                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'pythoncourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    python_logo = ImageTk.PhotoImage(file="images/python_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        python_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Python Inheritance"
                        lesson_content = [
                            ("Inheritance allows us to define a class that inherits all the methods and properties from another class."
                            " Parent class is the class being inherited from, also called base class."
                            " Child class is the class that inherits from another class, also called derived class.", None),
                            ("Create a Parent Class", None),
                            ("Create a class named Person, with firstname and lastname properties, and a printname method:", "images/pyinheritance1.png"),
                            ("Create a Child Class", None),
                            ("To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:", "images/pyinheritance2.png"),
                            ("Now the Student class has the same properties and methods as the Person class.", None)
                        ]
                        update_label(lesson1_title, *lesson_content)

                    title2 = Label(lmenu, image=python_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = python_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="File handling", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")


                def pydatastructuresc():



                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'pythoncourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    python_logo = ImageTk.PhotoImage(file="images/python_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        python_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "List"
                        lesson_content = [
                            ("Lists are used to store multiple items in a single variable."
                            " Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage."
                            "\n\nLists are created using square brackets:", "images/pyds1.png"),
                            ("To access the elements:", "images/pyds2.png"),
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked(): 
                        lesson2_title = "Tuples"
                        lesson_content = [
                            ("Tuples are used to store multiple items in a single variable."
                            "\n\nTuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage."
                            "\n\nA tuple is a collection which is ordered and unchangeable.", None),
                            ("Tuples are written with round brackets.", "images/pyds3.png"),
                        ]
                        update_label(lesson2_title, *lesson_content)

                    def lesson3_clicked(): 
                        lesson3_title = "Sets"
                        lesson_content = [
                            ("Sets are used to store multiple items in a single variable."
                            "\n\nSet is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage."
                            "\n\nA set is a collection which is unordered, unchangeable*, and unindexed.", "images/pyds4.png"),
                            ("", None),
                        ]       
                        update_label(lesson3_title, *lesson_content)

                    def lesson4_clicked(): 
                        lesson4_title = "Dictionary"
                        lesson_content = [
                            ("Dictionaries are used to store data values in key:value pairs."
                            "\n\nA dictionary is a collection which is ordered*, changeable and do not allow duplicates."
                            "\n\nDictionaries are written with curly brackets, and have keys and values:", "images/pyds5.png"),
                            ("", None),
                        ]  
                        update_label(lesson4_title, *lesson_content)

                    title2 = Label(lmenu, image=python_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = python_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="List", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)
                    
                    lesson2_button = Button(lmenu, text="Tuples", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)
                    
                    lesson3_button = Button(lmenu, text="Sets", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)

                    lesson4_button = Button(lmenu, text="Dictionaries", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson4_clicked, bd=0, activebackground="#243142")
                    lesson4_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")


                def pyalgorithmsc():
 



                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'pythoncourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    python_logo = ImageTk.PhotoImage(file="images/python_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        python_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Linear Search"
                        lesson_content = [
                            ("How Does Linear Search Algorithm Work?", None),
                            ("In Linear Search Algorithm, "
                            "\n\n - Every element is considered as a potential match for the key and checked for the same."
                            "\n\n - If any element is found equal to the key, the search is successful and the index of that element is returned."
                            "\n\n - If no element is found equal to the key, the search yields “No match found”."
                            "\n\nFor example: Consider the array arr[] = {10, 50, 30, 70, 80, 20, 90, 40} and key = 30", "images/pyalgo1.png"),
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked(): 
                        lesson2_title = "Binary Search"
                        lesson_content = [
                            ("How does Binary Search Algorithm Work?", None),
                            ("In this algorithm, "
                            "\n\n - Divide the search space into two halves by finding the middle index “mid”. "
                            "\n\n - Compare the middle element of the search space with the key. "
                            "\n\n - If the key is found at middle element, the process is terminated."
                            "\n\n - If the key is not found at middle element, choose which half will be used as the next search space."
                            "\n\n -- If the key is smaller than the middle element, then the left side is used for next search."
                            "\n\n -- If the key is larger than the middle element, then the right side is used for next search."
                            "\n\n - This process is continued until the key is found or the total search space is exhausted.", "images/pyalgo2.png")
                        ]
                        update_label(lesson2_title, *lesson_content)

                    def lesson3_clicked(): 
                        lesson3_title = "Bubble Sort"
                        lesson_content = [
                            ("Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order."
                            "Just like the movement of air bubbles in the water that rise up to the surface, each element of the array move to the end in each iteration. Therefore, it is called a bubble sort.", None),
                            ("How does Bubble Sort Algorithm Work?"
                            "\n\n - Starting from the first index, compare the first and the second elements."
                            "\n\n - If the first element is greater than the second element, they are swapped."
                            "\n\n - Now, compare the second and the third elements. Swap them if they are not in order."
                            "\n\n - The above process goes on until the last element.", "images/pyalgo3.png"),
                        ]           
                        update_label(lesson3_title, *lesson_content)

                    title2 = Label(lmenu, image=python_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = python_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Linear Search", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)
                    
                    lesson2_button = Button(lmenu, text="Binary Search", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)
                    
                    lesson3_button = Button(lmenu, text="Bubble Sort (python)", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")



                ### images title

                pythonpath = os.path.join(current_directory, "images/python.png")
                python = ImageTk.PhotoImage(file=pythonpath)

                beginnerpath = os.path.join(current_directory, "images/beginner.png")
                beginner = ImageTk.PhotoImage(file=beginnerpath)

                backbpath = os.path.join(current_directory, "images/backb.png")
                backb = ImageTk.PhotoImage(file=backbpath)

                intermediatepath = os.path.join(current_directory, "images/intermediate.png")
                intermediate = ImageTk.PhotoImage(file=intermediatepath)

                advancedpath = os.path.join(current_directory, "images/advanced.png")
                advanced = ImageTk.PhotoImage(file=advancedpath)

                ###

                ### images selection 1

                pythonsyntaxpath = os.path.join(current_directory, "images/pythonsyntax.png")
                pythonsyntax = ImageTk.PhotoImage(file=pythonsyntaxpath)

                cppvariablespath = os.path.join(current_directory, "images/variables.png")
                cppvariables = ImageTk.PhotoImage(file=cppvariablespath)

                cppmathpath = os.path.join(current_directory, "images/cppmath.png")
                cppmath = ImageTk.PhotoImage(file=cppmathpath)

                pythonconditionspath = os.path.join(current_directory, "images/pythonconditions.png")
                pythonconditions = ImageTk.PhotoImage(file=pythonconditionspath)

                cpploopingpath = os.path.join(current_directory, "images/cpplooping.png")
                cpplooping = ImageTk.PhotoImage(file=cpploopingpath)

                ###

                ### images selection 2

                pythonfunctionspath = os.path.join(current_directory, "images/pythonfunctions.png")
                pythonfunctions = ImageTk.PhotoImage(file=pythonfunctionspath)

                pythonfilehandlingpath = os.path.join(current_directory, "images/filehandling.png")
                pythonfilehandling = ImageTk.PhotoImage(file=pythonfilehandlingpath)

                cppinheritancepath = os.path.join(current_directory, "images/cppinheritance.png")
                cppinheritance = ImageTk.PhotoImage(file=cppinheritancepath)

                ###

                ### images selection 3

                cppdatastructurespath = os.path.join(current_directory, "images/cppdatastructures.png")
                cppdatastructures = ImageTk.PhotoImage(file=cppdatastructurespath)

                cppalgorithmspath = os.path.join(current_directory, "images/cppalgorithms.png")
                cppalgorithms = ImageTk.PhotoImage(file=cppalgorithmspath)

                ###


                nav_bar = Frame(self.window, bg="#182B44", height=30)
                nav_bar.pack(fill=X)

                nav_bar.grid_columnconfigure(0, weight=1)
                nav_bar.grid_columnconfigure(2, weight=1)

                nav_header = Label(nav_bar, image=python, bg="#182B44", fg="#00E69A", font=("Arial", 24, "bold"))
                nav_header.image = python
                nav_header.grid(row=0, column=1, pady=20)

                back_navbutt = Button(
                    nav_bar, image=backb, 
                    bg="#182B44", 
                    fg="#00E69A", 
                    font=("Arial", 24, "bold"), 
                    bd=0, 
                    highlightthickness=0, 
                    activebackground="#182B44", 
                    command=back
                    )
                back_navbutt.image = backb
                back_navbutt.grid(row=0, column=0, padx=50, pady=20, sticky="w")

                course_window = Canvas(self.window, bg="#162334", highlightthickness=0)
                course_window.pack(fill=BOTH,expand=True, anchor=CENTER)

                courses = Frame(course_window, bg="#162334")

                scrollbar = Scrollbar(course_window)
                scrollbar.pack(side=RIGHT, fill=Y)

                scrollbar.config(command=course_window.yview)
                course_window.config(yscrollcommand=scrollbar.set)

                course_title = Label(courses, image=beginner, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"))
                course_title.pack(anchor="w", padx=100, pady=50)

                courses_selection1 = Frame(courses, bg="#162334")
                courses_selection1.pack(fill="both", padx=200)

                course1 = Button(courses_selection1, image=introd, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=pyintroduction)
                course1.image = introd
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                course2 = Button(courses_selection1, image=cppvariables, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=pyvariablesc)
                course2.image = cppvariables
                course2.grid(row=0, column=1, columnspan=1, padx=50, pady=30)

                course3 = Button(courses_selection1, image=cppmath, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=pymathc)
                course3.image = cppmath
                course3.grid(row=0, column=2, columnspan=1, padx=50, pady=30)

                course4 = Button(courses_selection1, image=pythonconditions, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=pyconditionsc)
                course4.image = pythonconditions
                course4.grid(row=0, column=3, columnspan=1, padx=50, pady=30)

                course5 = Button(courses_selection1, image=cpplooping, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=pyloopingc)
                course5.image = cpplooping
                course5.grid(row=0, column=4, columnspan=1, padx=50, pady=30)

                diff_title = Label(courses, image=intermediate, bg="#162334", fg="#7FFFD4", font=("Arial", 24, "bold"))
                diff_title.image = intermediate
                diff_title.pack(anchor="w", padx=100, pady=50)

                courses_selection2 = Frame(courses, bg="#162334")
                courses_selection2.pack(fill="both", padx=200)

                course1 = Button(courses_selection2, image=pythonfunctions, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=pyfunctionsc)
                course1.image = pythonfunctions
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                course2 = Button(courses_selection2, image=pythonfilehandling, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=pyfilehandlingc)
                course2.image = pythonfilehandling
                course2.grid(row=0, column=1, columnspan=1, padx=50, pady=30)

                course3 = Button(courses_selection2, image=cppinheritance, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=pyinheritancec)
                course3.image = cppinheritance
                course3.grid(row=0, column=2, columnspan=1, padx=50, pady=30)

                diff2_title = Label(courses, image=advanced, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"))
                diff2_title.image = advanced
                diff2_title.pack(anchor="w", padx=100, pady=50)

                courses_selection3 = Frame(courses, bg="#162334")
                courses_selection3.pack(fill="both", padx=200)

                course1 = Button(courses_selection3, image=cppdatastructures, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=pydatastructuresc)
                course1.image = cppdatastructures
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                course2 = Button(courses_selection3, image=cppalgorithms, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=pyalgorithmsc)
                course2.image = cppalgorithms
                course2.grid(row=0, column=1, columnspan=1, padx=50, pady=30)

                # Change the image of course1 in courses_selection1
                course_window.create_window((0, 0), window=courses, anchor="nw")

                course_window.update_idletasks()
                course_window.config(scrollregion=course_window.bbox("all"))
            def cpp_clicked():
                menu_directory = os.path.dirname(os.path.abspath(__file__))
                os.chdir(menu_directory)
                self.window.minsize(1600,900)
                self.window.maxsize(1600,900)
                current_directory = os.getcwd()

                introd = ImageTk.PhotoImage(file="images/introd.png")
                def back():
                    course_window.pack_forget()
                    nav_bar.pack_forget()
                    menu()

                def cppintroduction():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'cppcourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    cpp_logo = ImageTk.PhotoImage(file="images/cpp_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def lesson1_clicked(): 
                        lesson1_title = "Lesson 1: Introduction"
                        lesson_content = [
                            ("C++ is a cross-platform language that can be used to create high-performance applications.", None),
                            ("C++ was developed by Bjarne Stroustrup, as an extension to the C language.", None),
                            ("C++ was developed as an extension of C, and both languages have almost the same syntax. The main difference between C and C++ is that C++ support classes and objects, while C does not.", None),
                            ("This tutorial will teach you the basics of C++. It is not necessary to have any prior programming experience.", None)
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "Lesson 2: Let's Get Started!"
                        lesson_content = [
                            ("To start using C++, you need two things:\n- A text editor, like Notepad, to write C++ code.\n- A compiler, like GCC, to translate the C++ code into a language that the computer will understand", None),
                            ("C++ Install IDE\nAn IDE (Integrated Development Environment) is used to edit AND compile the code. Popular IDE's include Code::Blocks, Eclipse, and Visual Studio. These are all free, and they can be used to both edit and debug C++ code.  ", None),
                            ("Note: Web-based IDE's can work as well, but functionality is limited. We will use Code::Blocks in our tutorial, which we believe is a good place to start. You can find the latest version of Codeblocks at http://www.codeblocks.org/. Download the mingw-setup.exe file, which will install the text editor with a compiler."
                            , None)
                        ]
                        update_label(lesson2_title, *lesson_content)


                    def lesson3_clicked():
                        lesson3_title = "Lesson 3: Syntaxes"
                        lesson_content = [
                            ("Let's break up the following code to understand it better:", "images/syntaxex.png"),
                            ("Line 1: #include <iostream> is a header file library that lets us work with input and output objects, such as cout (used in line 5). Header files add functionality to C++ programs." 
                            "\n\nLine 2: using namespace std means that we can use names for objects and variables from the standard library." 
                            "\n\nLine 3: A blank line. C++ ignores white space. But we use it to make the code more readable." 
                            "\n\nLine 4: Another thing that always appear in a C++ program, is int main(). This is called a function. Any code inside its curly brackets {} will be executed."
                            "\n\nLine 5: cout (pronounced \"see-out\") is an object used together with the insertion operator (<<) to output/print text. In our example it will output \"Hello World!\"."
                            "\n\nNote: Every C++ statement ends with a semicolon ;." 
                            "\n\nNote: The body of int main() could also been written as:int main () { cout << \"Hello World!\"; return 0; }"
                            "\n\nRemember: The compiler ignores white spaces. However, multiple lines makes the code more readable."
                            "\n\nLine 6: return 0 ends the main function."
                            "\n\nLine 7: Do not forget to add the closing curly bracket } to actually end the main function.", None),
                            ("\n\nOmitting Namespace" 
                            "\n\nYou might see some C++ programs that runs without the standard namespace library. The using namespace std line can be omitted and replaced with the std keyword, followed by the :: operator for some objects:", "images/omittingnamespace.png"),
                            ("It is up to you if you want to include the standard namespace library or not.", None),
                            ("", None),
                        ]
                        update_label(lesson3_title, *lesson_content)

                    def lesson4_clicked():
                        lesson4_title = "Lesson 4: Output"
                        lesson_content = [
                            ("C++ Output (Print Text)" "The cout object, together with the << operator, is used to output values/print text:", "images/cppoutput.png"),
                            ("You can add as many cout objects as you want. However, note that it does not insert a new line at the end of the output:", "images/cppoutput2.png"),
                            ("", None),
                        ]
                        update_label(lesson4_title, *lesson_content)
                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        cpp_clicked()

                    title2 = Label(lmenu, image=cpp_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = cpp_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Introduction", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Get Started!", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    lesson3_button = Button(lmenu, text="Syntaxes", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)

                    lesson4_button = Button(lmenu, text="Output", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson4_clicked, bd=0, activebackground="#243142")
                    lesson4_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def cppvariablesc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'cppcourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    cpp_logo = ImageTk.PhotoImage(file="images/cpp_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        cpp_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Declare Variables"
                        lesson_content = [
                            ("Variables are containers for storing data values." 
                            "\n\nIn C++, there are different types of variables (defined with different keywords), for example:" 
                            "\n- int - stores integers (whole numbers), without decimals, such as 123 or -123"
                            "\n- double - stores floating point numbers, with decimals, such as 19.99 or -19.99"
                            "\n- char - stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes"
                            "\n- string - stores text, such as \"Hello World\". String values are surrounded by double quotes"
                            "\n- bool - stores values with two states: true or false", None),
                            ("Declaring (Creating) Variables" 
                            "To create a variable, specify the type and assign it a value:"
                            "\n\nSyntax"
                            "type variableName = value;"
                            "Where type is one of C++ types (such as int), and variableName is the name of the variable (such as x or myName). The equal sign is used to assign values to the variable.", None),
                            ("To create a variable that should store a number, look at the following example:", None),
                            ("Example:"
                            "\nCreate a variable called myNum of type int and assign it the value 15:", "images/cppvariables.png")
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "Declare Multiple Variables"
                        lesson_content = [
                            ("To declare more than one variable of the same type, use a comma-separated list:", "images/cppmultivar.png"),
                            ("", None)
                        ]
                        update_label(lesson2_title, *lesson_content)


                    def lesson3_clicked():
                        lesson3_title = "Identifiers"
                        lesson_content = [
                            ("All C++ variables must be identified with unique names." 
                            "\n\nThese unique names are called identifiers." 
                            "\n\nIdentifiers can be short names (like x and y) or more descriptive names (age, sum, totalVolume)."
                            "\n\nNote: It is recommended to use descriptive names in order to create understandable and maintainable code:", None),
                            ("Example: ", "images/cppidentifier.png"),
                            ("", None),
                        ]
                        update_label(lesson3_title, *lesson_content)

                    def lesson4_clicked():
                        lesson4_title = "Constant"
                        lesson_content = [
                            ("When you do not want others (or yourself) to change existing variable values"
                            " use the const keyword (this will declare the variable as \"constant\""
                            " which means unchangeable and read-only):", "images/cppconstants.png"),
                            ("You should always declare the variable as constant when you have values that are unlikely to change", None),
                            ("", None),
                        ]
                        update_label(lesson4_title, *lesson_content)

                    title2 = Label(lmenu, image=cpp_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = cpp_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Declaring", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Multiple variables", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    lesson3_button = Button(lmenu, text="Identifiers", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)

                    lesson4_button = Button(lmenu, text="Constants", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson4_clicked, bd=0, activebackground="#243142")
                    lesson4_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def cppmathc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'cppcourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    cpp_logo = ImageTk.PhotoImage(file="images/cpp_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        cpp_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "C++ Math"
                        lesson_content = [
                            ("C++ has many functions that allows you to perform mathematical tasks on numbers." " ", None),
                            ("Max and Min" "\n\nThe max(x,y) function can be used to find the highest value of x and y:", None),
                            ("Example:", "images/cppmath1.png"),
                            ("C++ <cmath> Header" "\nOther functions, such as sqrt (square root), round (rounds a number) and log (natural logarithm), can be found in the <cmath> header file:", 
                            "images/cppmath2.png")
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "Other Math Functions"
                        lesson_content = [
                            ("A list of other popular Math function (from the <cmath> library) can be found in the table below:", "images/cmathtab1.png"),
                            ("", "images/cmathtab2.png"),
                            ("", "images/cmathtab3.png"),
                            ("", "images/cmathtab4.png"),
                            ("", "images/cmathtab5.png"),
                            ("", "images/cmathtab6.png")
                        ]
                        update_label(lesson2_title, *lesson_content)

                    title2 = Label(lmenu, image=cpp_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = cpp_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Declaring", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Multiple variables", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")
                    
                def cppconditionsc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'cppcourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    cpp_logo = ImageTk.PhotoImage(file="images/cpp_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        cpp_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "C++ Conditions and If Statements"
                        lesson_content = [
                            ("You already know that C++ supports the usual logical conditions from mathematics:" 
                            "\n\n - Less than: a < b " 
                            "\n - Less than or equal to: a <= b"
                            "\n - Greater than: a > b"
                            "\n - Greater than or equal to: a >= b"
                            "\n - Equal to a == b"
                            "\n - Not Equal to: a != b", None),
                            ("You can use these conditions to perform different actions for different decisions.", None),
                            ("C++ has the following conditional statements:"
                            "\n\n - Use if to specify a block of code to be executed, if a specified condition is true"
                            "\n - Use else to specify a block of code to be executed, if the same condition is false"
                            "\n - Use else if to specify a new condition to test, if the first condition is false"
                            "\n - Use switch to specify many alternative blocks of code to be executed", None),
                            ("The if Statement" "\n\n Use the if statement to specify a block of C++ code to be executed if a condition is true.", None),
                            ("Syntax", "images/cppconditions.png")
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "C++ Else"
                        lesson_content = [
                            ("Use the else statement to specify a block of code to be executed if the condition is false.", None),
                            ("Example:", "images/cppconditions2.png"),
                            ("Example Explained" "\n\nIn the example above, time (20) is greater than 18, so the condition is false. Because of this, we move on to the else condition and print to the screen \"Good evening\". If the time was less than 18, the program would print \"Good day\".", None),
                            ("", None)
                        ]
                        update_label(lesson2_title, *lesson_content)

                    def lesson3_clicked():
                        lesson3_title = "C++ Else if"
                        lesson_content = [
                            ("Use the else if statement to specify a new condition if the first condition is false.", None),
                            ("Example:", "images/cppconditions3.png"),
                            ("Example Explained" "\n\nIn the example above, time (22) is greater than 10, so the first condition is false. The next condition, in the else if statement, is also false, so we move on to the else condition since condition1 and condition2 is both false - and print to the screen \"Good evening\".\n\nHowever, if the time was 14, our program would print \"Good day.\"", None),
                            ("", None)
                        ]
                        update_label(lesson3_title, *lesson_content)

                    def lesson4_clicked():
                        lesson4_title = "Short Hand If Else"
                        lesson_content = [
                            ("There is also a short-hand if else, which is known as the ternary operator because it consists of three operands."
                            " It can be used to replace multiple lines of code with a single line."
                            " It is often used to replace simple if else statements:", None),
                            ("Example:", "images/cppconditions4.png"),
                            ("", None)
                        ]
                        update_label(lesson4_title, *lesson_content)

                    def lesson5_clicked():
                        lesson5_title = "C++ Switch Statements"
                        lesson_content = [
                            ("Use the switch statement to select one of many code blocks to be executed.", None),
                            ("Syntax:", "images/cppswitch.png"),
                            ("This is how it works:" 
                            "\n\n - The switch expression is evaluated once"
                            "\n - The value of the expression is compared with the values of each case"
                            "\n - If there is a match, the associated block of code is executed"
                            "\n - The break and default keywords are optional, and will be described later in this chapter", None),
                            ("The example below uses the weekday number to calculate the weekday name:", "images/cppswitch2.png"),
                            ("", "images/cppswitch3.png"),
                            ("", "images/cppswitch4.png"),
                            ("The break Keyword" 
                            "\n\n When C++ reaches a break keyword, it breaks out of the switch block."
                            "\n\n This will stop the execution of more code and case testing inside the block."
                            "\n\n When a match is found, and the job is done, it's time for a break. There is no need for more testing.", None),
                            ("A break can save a lot of execution time because it \"ignores\" the execution of all the rest of the code in the switch block.", None),
                            ("The default Keyword" 
                            "\n\n The default keyword specifies some code to run if there is no case match:", "images/cppswitch5.png")
                            
                        ]
                        update_label(lesson5_title, *lesson_content)

                    title2 = Label(lmenu, image=cpp_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = cpp_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = tk.Button(lmenu, text="C++ Conditions", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = tk.Button(lmenu, text="C++ Else", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)
                    
                    lesson3_button = tk.Button(lmenu, text="Else if Statement", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)
                    
                    lesson4_button = tk.Button(lmenu, text="Short Hand if..else", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson4_clicked, bd=0, activebackground="#243142")
                    lesson4_button.pack(padx=10, pady=10)

                    lesson5_button = tk.Button(lmenu, text="Switch Statements", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson5_clicked, bd=0, activebackground="#243142")
                    lesson5_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def cpploopingc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'cppcourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    cpp_logo = ImageTk.PhotoImage(file="images/cpp_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        cpp_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "For Loop"
                        lesson_content = [
                            ("When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop:", None),
                            ("Example:", "images/cpplooping1.png"),
                            ("Statement 1 is executed (one time) before the execution of the code block."
                            "\n\nStatement 2 defines the condition for executing the code block."
                            "\n\nStatement 3 is executed (every time) after the code block has been executed.", None),
                            ("Example Explained: "
                            "\n\nStatement 1 sets a variable before the loop starts (int i = 0)."
                            "\n\nStatement 2 defines the condition for the loop to run (i must be less than 5). If the condition is true, the loop will start over again, if it is false, the loop will end."
                            "\n\nStatement 3 increases a value (i++) each time the code block in the loop has been executed.", None),

                            ("Nested Loops"
                            "\n\nIt is also possible to place a loop inside another loop. This is called a nested loop."
                            "\n\nThe \"inner loop\" will be executed one time for each iteration of the \"outer loop\":", "images/cpplooping2.png"),

                            ("The foreach Loop"
                            "\nThere is also a \"for-each loop\" (introduced in C++ version 11 (2011), which is used exclusively to loop through elements in an array (or other data sets):"
                            "\nExample of a foreach Loop:", "images/cpplooping3.png")
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "While Loops"
                        lesson_content = [
                            ("The while loop loops through a block of code as long as a specified condition is true:", None),
                            ("In the example below, the code in the loop will run, over and over again, as long as a variable (i) is less than 5:", "images/cpplooping6.png")
                        ]
                        update_label(lesson2_title, *lesson_content)


                    title2 = Label(lmenu, image=cpp_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = cpp_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = tk.Button(lmenu, text="For Loop", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = tk.Button(lmenu, text="While Loop", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)
                    
                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def cppfunctionsc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'cppcourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    cpp_logo = ImageTk.PhotoImage(file="images/cpp_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        cpp_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Functions"
                        lesson_content = [
                            ("A function is a block of code which only runs when it is called."
                            " You can pass data, known as parameters, into a function."
                            " Functions are used to perform certain actions, and they are important for reusing code: Define the code once, and use it many times.", None),
                            ("Create a Function"
                            " C++ provides some pre-defined functions, such as main(), which is used to execute code. But you can also create your own functions to perform certain actions."
                            " To create (often referred to as declare) a function, specify the name of the function, followed by parentheses ():", "images/cppfunctions1.png"),
                            ("myFunction() is the name of the function"
                            "\nvoid means that the function does not have a return value. You will learn more about return values later in the next chapter", None),
                            ("Call a Function"
                            "\n\nDeclared functions are not executed immediately. They are \"saved for later use\", and will be executed later, when they are called."
                            "\nTo call a function, write the function's name followed by two parentheses () and a semicolon ;"
                            "\nIn the following example above, myFunction() is used to print a text (the action), when it is called:"
                            "\n\n A function can be called multiple times. ", None),
                            ("Function Declaration and Definition"
                            "\nA C++ function consist of two parts:"
                            "\n\n - Declaration: the return type, the name of the function, and parameters (if any)"
                            "\n\n - Definition: the body of the function (code to be executed)", None),   
                            ("Note: If a user-defined function, such as myFunction() is declared after the main() function, an error will occur", None),

                            ("However, it is possible to separate the declaration and the definition of the function - for code optimization."
                            "\n\nYou will often see C++ programs that have function declaration above main(), and function definition below main(). This will make the code better organized and easier to read:", "images/cppfunctions2.png")
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "Parameters and Arguments"
                        lesson_content = [
                            ("Information can be passed to functions as a parameter. Parameters act as variables inside the function."
                            " Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma:", "images/cppfunctions3.png"),
                            ("", None)
                        ]
                        update_label(lesson2_title, *lesson_content)

                    def lesson3_clicked():
                        lesson3_title = "Recursion"
                        lesson_content = [
                            ("Recursion is the technique of making a function call itself. This technique provides a way to break complicated problems down into simple problems which are easier to solve."
                            " Recursion may be a bit difficult to understand. The best way to figure out how it works is to experiment with it." 
                            " You may often see Recursion in some competitive programming book, or in any data structures lesson online."
                            " Recursion is one of the popular topics in programming", None),
                            ("Recursion Example", "images/cppfunctions4.png"),
                            ("Example Explained"
                            "\n\nWhen the sum() function is called, it adds parameter k to the sum of all numbers smaller than k and returns the result. When k becomes 0, the function just returns 0. When running, the program follows these steps:"
                            , "images/cppfunctions5.png"),
                        ]
                        update_label(lesson3_title, *lesson_content)

                    title2 = Label(lmenu, image=cpp_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = cpp_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = tk.Button(lmenu, text="Functons", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = tk.Button(lmenu, text="Functions Parameters", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)
                    
                    lesson3_button = tk.Button(lmenu, text="Recursion", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)
                    
                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def cppclassesc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'cppcourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    cpp_logo = ImageTk.PhotoImage(file="images/cpp_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        cpp_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "What is OOP?"
                        lesson_content = [
                            ("OOP stands for Object-Oriented Programming."
                            "\nWhile object-oriented programming involves constructing objects that include both data and functions, procedural programming involves developing procedures or functions that perform actions on the data."
                            , None),
                            ("Programming in an object-oriented manner has a number of benefits over procedural programming:"
                            "\n\n - OOP is faster and easier to execute"
                            "\n\n - OOP provides a clear structure for the programs"
                            "\n\n - OOP helps to keep the C++ code DRY \"Don't Repeat Yourself\", and makes the code easier to maintain, modify and debug"
                            "\n\n - OOP makes it possible to create full reusable applications with less code and shorter development time", None),
                            ("Tip: The \"Don't Repeat Yourself\" (DRY) principle is about reducing the repetition of code."
                            "You should extract out the codes that are common for the application, and place them at a single place and reuse them instead of repeating it.", None),

                            ("C++ What are Classes and Objects?"
                            "\n\nClasses and objects are the two main aspects of object-oriented programming."
                            "\n\nLook at the following illustration to see the difference between class and objects:", "images/cppclasses1.png"),

                            ("So, a class is a template for objects, and an object is an instance of a class"
                            "When the individual objects are created, they inherit all the variables and functions from the class."
                            "\n\nYou will learn much more about classes and objects in the next chapter.", None)
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "Classes and Objects"
                        lesson_content = [
                            ("C++ is an object-oriented programming language."
                            "\nEverything in C++ is associated with classes and objects, along with its attributes and methods. For example: in real life, a car is an object. The car has attributes, such as weight and color, and methods, such as drive and brake."
                            "Attributes and methods are basically variables and functions that belongs to the class. These are often referred to as \"class members\"."
                            "\n\nA class is a user-defined data type that we can use in our program, and it works as an object constructor, or a \"blueprint\" for creating objects.", None),
                            ("Create a Class"
                            "\n\nTo create a class, use the class keyword", "images/cppclasses2.png"),
                            ("Example Explained"
                            "\n\n - The class keyword is used to create a class called MyClass."
                            "\n\n - The public keyword is an access specifier, which specifies that members (attributes and methods) of the class are accessible from outside the class. You will learn more about access specifiers later."
                            "\n\n - Inside the class, there is an integer variable myNum and a string variable myString. When variables are declared within a class, they are called attributes."
                            "\n\n - At last, end the class definition with a semicolon ;.", None),
                            ("Create an Object"
                            "\nIn C++, an object is created from a class. We have already created the class named MyClass, so now we can use this to create objects."
                            "\n\n - To create an object of MyClass, specify the class name, followed by the object name."
                            "\n\n - To access the class attributes (myNum and myString), use the dot syntax (.) on the object:", "images/cppclasses3.png"),
                            ("", None),
                        ]  
                        update_label(lesson2_title, *lesson_content)

                    def lesson3_clicked():
                        lesson3_title = "Class Methods"
                        lesson_content = [
                            ("Methods are functions that belongs to the class."
                            "\n\nThere are two ways to define fnctions that belongs to a class:"
                            "\n\n - Inside class definition"
                            "\n\n - Outside class definition", None),
                            ("In the following example, we define a function inside the class, and we name it \"myMethod\".", None),
                            ("Note: You access methods just like you access attributes; by creating an object of the class and using the dot syntax (.):", None),
                            ("Inside Example", "images/cppclasses4.png"),
                            ("Outside Example", "images/cppclasses5.png"),
                        ]
                        update_label(lesson3_title, *lesson_content)

                    title2 = Label(lmenu, image=cpp_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = cpp_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = tk.Button(lmenu, text="OOP", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = tk.Button(lmenu, text="Classes and Objects", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)
                    
                    lesson3_button = tk.Button(lmenu, text="Class Methods", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)
                    
                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")


                def cppinheritancec():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'cppcourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    cpp_logo = ImageTk.PhotoImage(file="images/cpp_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        cpp_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Inheritance"
                        lesson_content = [
                            ("In C++, it is possible to inherit attributes and methods from one class to another. We group the \"inheritance concept\" into two categories:"
                            "\n\n - Derived Class(child) - the class that inherits from another class"
                            "\n\n - Base Class(parent) - the class being inherited from", None),
                            ("To inherit from a class, use the : symbol.", None),
                            ("In the example below, the Car class (child) inherits the attributes and methods from the Vehicle class (parent):", "images/cppinheritance1.png"),
                            ("", "images/cppinheritance2.png"),
                            ("Why And When To Use \"Inheritance\"?" 
                            "\n - It is useful for code reusability: reuse attributes and methods of an existing class when you create a new class.", None)
                        ]
                        update_label(lesson1_title, *lesson_content)

                    title2 = Label(lmenu, image=cpp_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = cpp_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = tk.Button(lmenu, text="Inheritance", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)
                    
                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")
                def cppdatastructuresc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'cppcourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    cpp_logo = ImageTk.PhotoImage(file="images/cpp_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        cpp_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Data Structures"
                        lesson_content = [
                            ("C/C++ arrays allow you to define variables that combine several data items of the same kind, but structure is another user defined data type which allows you to combine data items of different kinds.", None),
                            ("To define a structure, you must use the struct statement."
                            "The struct statement defines a new data type, with more than one member, for your program."
                            "The format of the struct statement is this:", "images/cppds1.png"),
                            ("The structure tag is optional and each member definition is a normal variable definition, such as int i; or float f; or any other valid variable definition."
                            "At the end of the structure's definition, before the final semicolon, you can specify one or more structure variables but it is optional.", None),
                            ("Accessing Structure Members"
                            "To access any member of a structure, we use the member access operator (.)."
                            "The member access operator is coded as a period between the structure variable name and the structure member that we wish to access."
                            "You would use struct keyword to define variables of structure type.", None),
                            ("Following is the example to explain usage of structure", "images/cppds2.png"),
                            ("", "images/cppds3.png"),
                            ("", "images/cppds4.png"),
                            ("", "images/cppds5.png"),
                            ("When the above code is compiled and executed, it produces the following result", "images/cppds6.png")
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked(): 
                        lesson2_title = "Structures as Function Arguments"
                        lesson_content = [
                            ("You can pass a structure as a function argument in very similar way as you pass any other variable or pointer."
                            "You would access structure variables in the similar way as you have accessed in the above example:", "images/cppds7.png"),
                            ("When the above code is compiled and executed, it produces the following result", "images/cppds8.png")
                        ]
                        update_label(lesson2_title, *lesson_content)

                    def lesson3_clicked(): 
                        lesson3_title = "Pointers to Structures"
                        lesson_content = [
                            ("You can define pointers to structures in very similar way as you define pointer to any other variable as follows", "images/cppds9.png"),
                            ("Now, you can store the address of a structure variable in the above defined pointer variable."
                            "To find the address of a structure variable, place the & operator before the structure's name as follows:", "images/cppds10.png"),
                            ("To access the members of a structure using a pointer to that structure, you must use the -> operator as follows", "images/cppds11.png"),
                            ("Let us re-write above example using structure pointer, hope this will be easy for you to understand the concept", "images/cppds12.png"),
                            ("", "images/cppds13.png"),
                            ("When the above code is compiled and executed, it produces the following result", "images/cppds14.png")
                        ]
                        update_label(lesson3_title, *lesson_content)

                    def lesson4_clicked(): 
                        lesson4_title = "The typedef Keyword"
                        lesson_content = [
                            ("There is an easier way to define structs or you could \"alias\" types you create. For example", "images/cppds15.png"),
                            ("Now, you can use Books directly to define variables of Books type without using struct keyword. Following is the example", "images/cppds16.png"),
                            ("You can use typedef keyword for non-structs as well as follows", "images/cppds17.png"),
                            ("x, y and z are all pointers to long ints.", None)
                        ]
                        update_label(lesson4_title, *lesson_content)

                    def lesson5_clicked(): 
                        lesson5_title = "Binary Tree"
                        lesson_content = [
                            ("In this tutorial, you will learn about binary tree and its different types. Also, you will find working examples of binary tree in C, C++, Java and Python.", None),
                            ("A binary tree is a tree data structure in which each parent node can have at most two children. Each node of a binary tree consists of three items:"
                            "\n\n - Data Item"
                            "\n\n - Address of left child"
                            "\n\n - Address of right child", "images/cppds18.png"),
                            ("Types of Binary Trees", None),
                            ("Full Binary Tree"
                            "\n\n - A full binary tree is a special type of binary tree in which every parent node/internal node has either two or no children.", "images/cppds19.png"),
                            ("Perfect Binary Tree"
                            "\n\n - A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level", "images/cppds20.png"),
                            ("Complete Binary Tree"
                            "\n\n - A complete binary tree is just like a full binary tree, but with two major differences."
                            "\n\n -- Every level must be completely filled"
                            "\n\n -- All the leaf elements must lean towards the left."
                            "\n\n -- The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.", "images/cppds21.png"),
                            ("Binary Tree Representation"
                            "\n\nA node of a binary tree is represented by a structure containing a data part and two pointsers to other structures of the same type.", "images/cppds22.png"),
                            ("", "images/cppds23.png")
                        ]
                        update_label(lesson5_title, *lesson_content)


                    title2 = Label(lmenu, image=cpp_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = cpp_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = tk.Button(lmenu, text="Data Structures", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = tk.Button(lmenu, text="Structures as Function Arguments", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)
                    
                    lesson3_button = tk.Button(lmenu, text="Pointers to Structures", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)
                    
                    lesson4_button = tk.Button(lmenu, text="The typedef Keyword", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson4_clicked, bd=0, activebackground="#243142")
                    lesson4_button.pack(padx=10, pady=10)
                    
                    lesson5_button = tk.Button(lmenu, text="Binary Tree", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson5_clicked, bd=0, activebackground="#243142")
                    lesson5_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def cppalgorithmsc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'cppcourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    cpp_logo = ImageTk.PhotoImage(file="images/cpp_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        cpp_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Bubble Sorting"
                        lesson_content = [
                            ("Bubble Sort is the simplest of the sorting techniques."
                            " In the bubble sort technique, each of the elements in the list is compared to its adjacent element. Thus if there are n elements in list A, then A[0] is compared to A[1], A[1] is compared to A[2] and so on."
                            "\n\nAfter comparing if the first element is greater than the second, the two elements are swapped then.", None),
                            ("Bubble Sort Technique"
                            "\n\nUsing the bubble sort technique, sorting is done in passes or iteration."
                            " Thus at the end of each iteration, the heaviest element is placed at its proper place in the list."
                            " In other words, the largest element in the list bubbles up.", None),
                            ("Algorithm: "
                            "\n - Step 1: For i = 0 to N-1 repeat Step 2"
                            "\n - Step 2: For J = i + 1 to N – I repeat"
                            "\n - Step 3: if A[J] > A[i]"
                            "\n -- Swap A[J] and A[i] \n [End of Inner for loop] \n [End if Outer for loop]"
                            "\n - Step 4: Exit", "images/cppalgo1.png"),
                            ("", "images/cppalgo2.png"),
                            ("", "images/cppalgo3.png"),
                            ("As shown in the illustration, with every pass, the largest element bubbles up to the last thereby sorting the list with every pass."
                            " As mentioned in the introduction, each element is compared to its adjacent element and swapped with one another if they are not in order."
                            "\n\nWhen we reach N-1 (where N is a total number of elements in the list) passes, we will have the entire list sorted.", None),
                            ("Bubble sort technique can be implemented in any programming language."
                            " We have implemented the bubble sort algorithm using C++ and Java language below.", None),
                            ("C++ Example", "images/cppalgo4.png"),
                            ("Output:", "images/cppalgo5.png")
                        ]
                        update_label(lesson1_title, *lesson_content)

                    title2 = Label(lmenu, image=cpp_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = cpp_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = tk.Button(lmenu, text="Bubble Sort", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                ### images title

                cpppath = os.path.join(current_directory, "images/c++.png")
                cpp = ImageTk.PhotoImage(file=cpppath)

                beginnerpath = os.path.join(current_directory, "images/beginner.png")
                beginner = ImageTk.PhotoImage(file=beginnerpath)

                backbpath = os.path.join(current_directory, "images/backb.png")
                backb = ImageTk.PhotoImage(file=backbpath)

                intermediatepath = os.path.join(current_directory, "images/intermediate.png")
                intermediate = ImageTk.PhotoImage(file=intermediatepath)

                advancedpath = os.path.join(current_directory, "images/advanced.png")
                advanced = ImageTk.PhotoImage(file=advancedpath)

                ###

                ### images selection 1

                pythonsyntaxpath = os.path.join(current_directory, "images/pythonsyntax.png")
                pythonsyntax = ImageTk.PhotoImage(file=pythonsyntaxpath)

                cppvariablespath = os.path.join(current_directory, "images/variables.png")
                cppvariables = ImageTk.PhotoImage(file=cppvariablespath)

                cppmathpath = os.path.join(current_directory, "images/cppmath.png")
                cppmath = ImageTk.PhotoImage(file=cppmathpath)

                pythonconditionspath = os.path.join(current_directory, "images/pythonconditions.png")
                pythonconditions = ImageTk.PhotoImage(file=pythonconditionspath)

                cpploopingpath = os.path.join(current_directory, "images/cpplooping.png")
                cpplooping = ImageTk.PhotoImage(file=cpploopingpath)

                ###

                ### images selection 2

                pythonfunctionspath = os.path.join(current_directory, "images/pythonfunctions.png")
                pythonfunctions = ImageTk.PhotoImage(file=pythonfunctionspath)

                cppclassespath = os.path.join(current_directory, "images/cppclasses.png")
                cppclasses = ImageTk.PhotoImage(file=cppclassespath)

                cppinheritancepath = os.path.join(current_directory, "images/cppinheritance.png")
                cppinheritance = ImageTk.PhotoImage(file=cppinheritancepath)

                ###

                ### images selection 3

                cppdatastructurespath = os.path.join(current_directory, "images/cppdatastructures.png")
                cppdatastructures = ImageTk.PhotoImage(file=cppdatastructurespath)

                cppalgorithmspath = os.path.join(current_directory, "images/cppalgorithms.png")
                cppalgorithms = ImageTk.PhotoImage(file=cppalgorithmspath)

                ###


                nav_bar = Frame(self.window, bg="#182B44", height=30)
                nav_bar.pack(fill=X)

                nav_bar.grid_columnconfigure(0, weight=1)
                nav_bar.grid_columnconfigure(2, weight=1)

                nav_header = Label(nav_bar, image=cpp, bg="#182B44", fg="#00E69A", font=("Arial", 24, "bold"))
                nav_header.image = cpp
                nav_header.grid(row=0, column=1, pady=20)

                back_navbutt = Button(
                    nav_bar, image=backb, 
                    bg="#182B44", 
                    fg="#00E69A", 
                    font=("Arial", 24, "bold"), 
                    bd=0, 
                    highlightthickness=0, 
                    activebackground="#182B44", 
                    command=back
                    )
                back_navbutt.image = backb
                back_navbutt.grid(row=0, column=0, padx=50, pady=20, sticky="w")

                course_window = Canvas(self.window, bg="#162334", highlightthickness=0)
                course_window.pack(fill=BOTH,expand=True, anchor=CENTER)

                courses = Frame(course_window, bg="#162334")

                scrollbar = Scrollbar(course_window)
                scrollbar.pack(side=RIGHT, fill=Y)

                scrollbar.config(command=course_window.yview)
                course_window.config(yscrollcommand=scrollbar.set)

                course_title = Label(courses, image=beginner, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"))
                course_title.pack(anchor="w", padx=100, pady=50)

                courses_selection1 = Frame(courses, bg="#162334")
                courses_selection1.pack(fill="both", padx=200)

                course1 = Button(courses_selection1, image=introd, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=cppintroduction)
                course1.image = introd
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                course2 = Button(courses_selection1, image=cppvariables, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=cppvariablesc)
                course2.image = cppvariables
                course2.grid(row=0, column=1, columnspan=1, padx=50, pady=30)

                course3 = Button(courses_selection1, image=cppmath, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=cppmathc)
                course3.image = cppmath
                course3.grid(row=0, column=2, columnspan=1, padx=50, pady=30)

                course4 = Button(courses_selection1, image=pythonconditions, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=cppconditionsc)
                course4.image = pythonconditions
                course4.grid(row=0, column=3, columnspan=1, padx=50, pady=30)

                course5 = Button(courses_selection1, image=cpplooping, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=cpploopingc)
                course5.image = cpplooping
                course5.grid(row=0, column=4, columnspan=1, padx=50, pady=30)

                diff_title = Label(courses, image=intermediate, bg="#162334", fg="#7FFFD4", font=("Arial", 24, "bold"))
                diff_title.image = intermediate
                diff_title.pack(anchor="w", padx=100, pady=50)

                courses_selection2 = Frame(courses, bg="#162334")
                courses_selection2.pack(fill="both", padx=200)

                course1 = Button(courses_selection2, image=pythonfunctions, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=cppfunctionsc)
                course1.image = pythonfunctions
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                course2 = Button(courses_selection2, image=cppclasses, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=cppclassesc)
                course2.image = cppclasses
                course2.grid(row=0, column=1, columnspan=1, padx=50, pady=30)

                course3 = Button(courses_selection2, image=cppinheritance, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=cppinheritancec)
                course3.image = cppinheritance
                course3.grid(row=0, column=2, columnspan=1, padx=50, pady=30)

                diff2_title = Label(courses, image=advanced, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"))
                diff2_title.image = advanced
                diff2_title.pack(anchor="w", padx=100, pady=50)

                courses_selection3 = Frame(courses, bg="#162334")
                courses_selection3.pack(fill="both", padx=200)

                course1 = Button(courses_selection3, image=cppdatastructures, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=cppdatastructuresc)
                course1.image = cppdatastructures
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                course2 = Button(courses_selection3, image=cppalgorithms, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=cppalgorithmsc)
                course2.image = cppalgorithms
                course2.grid(row=0, column=1, columnspan=1, padx=50, pady=30)

                # Change the image of course1 in courses_selection1
                course_window.create_window((0, 0), window=courses, anchor="nw")

                course_window.update_idletasks()
                course_window.config(scrollregion=course_window.bbox("all"))
            
            def java_clicked():
                menu_directory = os.path.dirname(os.path.abspath(__file__))
                os.chdir(menu_directory)
                self.window.minsize(1600,900)
                self.window.maxsize(1600,900)
                current_directory = os.getcwd()

                introd = ImageTk.PhotoImage(file="images/introd.png")
                def back():
                    course_window.pack_forget()
                    nav_bar.pack_forget()
                    menu()

                def launch_py(script_name):
                    pass

                def javaintroduction():

                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'javacourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    java_logo = ImageTk.PhotoImage(file="images/java_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        java_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "What is JAVA?"
                        lesson_content = [
                            ("Java is a popular programming language, created in 1995."
                            "\n\nIt is owned by Oracle, and more than 3 billion devices run Java.", None),
                            ("It is used for:"
                            "\n\n - Mobile applications (specially Android apps)"
                            "\n\n - Desktop applications"
                            "\n\n - Web applications"
                            "\n\n - Web servers and application servers"
                            "\n\n - Games"
                            "\n\n - Database connection"
                            "\n\n - And much, much more!", None),
                            ("Why use JAVA?"
                            "\n\n - Java works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc.)"
                            "\n\n - It is one of the most popular programming language in the world"
                            "\n\n - It has a large demand in the current job market"
                            "\n\n - It is easy to learn and simple to use"
                            "\n\n - It is open-source and free"
                            "\n\n - It is secure, fast and powerful"
                            "\n\n - It has a huge community support (tens of millions of developers)"
                            "\n\n - Java is an object oriented language which gives a clear structure to programs and allows code to be reused, lowering development costs"
                            "\n\n - As Java is close to C++ and C#, it makes it easy for programmers to switch to Java or vice versa", None),
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "Get Started!"
                        lesson_content = [
                            ("Java Install"
                            "\nSome PCs might have Java already installed."
                            "\n\nTo check if you have Java installed on a Windows PC, search in the start bar for Java or type the following in Command Prompt (cmd.exe):", "images/javaintro1.png"),
                            ("If java is installed, you will see the result shown above", None),
                            ("If you do not have Java installed on your computer, you can download it for free at oracle.com."
                            "\n\nNote: In this tutorial, we will write Java code in a text editor."
                            " However, it is possible to write Java in an Integrated Development Environment, such as IntelliJ IDEA, Netbeans or Eclipse, which are particularly useful when managing larger collections of Java files.", None),
                        ]
                        update_label(lesson2_title, *lesson_content)


                    def lesson3_clicked():
                        lesson3_title = "Quickstart"
                        lesson_content = [
                            ("In Java, every application begins with a class name, and that class must match the filename."
                            "\n\nLet's create our first Java file, called Main.java, which can be done in any text editor (like Notepad)."
                            "\n\nThe file should contain a \"Hello World\" message, which is written with the following code:", None),
                            ("Main.java", "images/javaintro2.png"),
                            ("Don't worry if you don't understand the code above - we will discuss it in detail in later chapters. For now, focus on how to run the code above.", None),
                            ("Save the code in Notepad as \"Main.java\". Open Command Prompt (cmd.exe), navigate to the directory where you saved your file, and type \"javac Main.java\":", "images/javaintro3.png"),
                            ("This will compile your code. If there are no errors in the code, the command prompt will take you to the next line. Now, type \"java Main\" to run the file:", "images/javaintro4.png"),
                            ("The output should read:", "images/javaintro5.png"),
                            ("Congratulations! You have written and executed your first Java program.", None)
                        ]
                        update_label(lesson3_title, *lesson_content)

                    def lesson4_clicked():
                        lesson4_title = "Syntax"
                        lesson_content = [
                            ("In the previous chapter, we created a Java file called Main.java, and we used the following code to print \"Hello World\" to the screen:", "images/javaintro2.png"),
                            ("Example Explained"
                            "Every line of code that runs in Java must be inside a class. In our example, we named the class Main. A class should always start with an uppercase first letter.", None),
                            ("Note: Java is case-sensitive: \"MyClass\" and \"myclass\" has different meaning.", None),
                            ("The name of the java file must match the class name."
                            " When saving the file, save it using the class name and add \".java\" to the end of the filename."
                            " To run the example above on your computer, make sure that Java is properly installed:"
                            " Go to the Get Started Chapter for how to install Java. The output should be:", None),
                            ("The main Method"
                            "\nThe main() method is required and you will see it in every Java program:", "images/javaintro6.png"),
                            ("Any code inside the main() method will be executed. Don't worry about the keywords before and after main. You will get to know them bit by bit while reading this tutorial.", None),
                            ("For now, just remember that every Java program has a class name which must match the filename, and that every program must contain the main() method.", None),
                            ("System.out.println()", None),
                            ("Inside the main() method, we can use the println() method to print a line of text to the screen:", "images/javaintro2.png"),
                            ("Note: The curly braces {} marks the beginning and the end of a block of code."
                            "\nSystem is a built-in Java class that contains useful members, such as out, which is short for \"output\"." 
                            "The println() method, short for \"print line\", is used to print a value to the screen (or a file)."
                            "\n\nDon't worry too much about System, out and println(). Just know that you need them together to print stuff to the screen."
                            "\n\nYou should also note that each code statement must end with a semicolon (;).", None)
                        ]
                        update_label(lesson4_title, *lesson_content)

                    title2 = Label(lmenu, image=java_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = java_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="What is JAVA?", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Get Started!", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    lesson3_button = Button(lmenu, text="Quickstart", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)

                    lesson4_button = Button(lmenu, text="Syntax", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson4_clicked, bd=0, activebackground="#243142")
                    lesson4_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def javavariablesc():

                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'javacourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    java_logo = ImageTk.PhotoImage(file="images/java_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        java_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Java Variables"
                        lesson_content = [
                            ("Variables are containers for storing data values.", None),
                            ("In Java, there are different types of variables, for example:"
                            "\n\n - String - stores text, such as \"Hello\". String values are surrounded by double quotes"
                            "\n\n - int - stores integers (whole numbers), without decimals, such as 123 or -123"
                            "\n\n - float - stores floating point numbers, with decimals, such as 19.99 or -19.99"
                            "\n\n - char - stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes"
                            "\n\n - boolean - stores values with two states: true or false", None),
                            ("Declaring (Creating) Variables"
                            "\n To create a variable, you must specify the type and assign it a value:", "images/javavariables1.png"),
                            ("Where type is one of Java's types (such as int or String), and variableName is the name of the variable (such as x or name)."
                            " The equal sign is used to assign values to the variable."
                            "\n\n To create a variable that should store text, look at the following example:", None),
                            ("Example"
                            "\n\n Create a variable called name of type String and assign it the value \"John\":", "images/javavariables2.png"),
                            ("To create a variable that should store a number, look at the following example:", "images/javavariables3.png"),
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked():
                        lesson2_title = "Declare Many Variables"
                        lesson_content = [
                            ("To declare more than one variable of the same type, you can use a comma-separated list:", "images/javavariables4.png"),
                            ("You can simply write:", "images/javavariables5.png"),
                            ("", None),
                        ]
                        update_label(lesson2_title, *lesson_content)

                    def lesson3_clicked():
                        lesson3_title = "Java Data Types"
                        lesson_content = [
                            ("As explained in the previous chapter, a variable in Java must be a specified data type:", "images/javavariables6.png"),
                            ("Data types are divided into two groups:"
                            "\n\n - Primitive data types - includes byte, short, int, long, float, double, boolean and char"
                            "\n\n - Non-primitive data types - such as String, Arrays and Classes (you will learn more about these in a later chapter)", None),
                            ("Primitive Data Types"
                            "\n\nA primitive data type specifies the size and type of variable values, and it has no additional methods."
                            "\n\nThere are eight primitive data types in Java:", "images/javavariables7.png"),
                        ]
                        update_label(lesson3_title, *lesson_content)

                    def lesson4_clicked():
                        lesson4_title = "Java Numbers"
                        lesson_content = [
                            ("Numbers"
                            "\n\nPrimitive number types are divided into two groups:"
                            "\n\nInteger types stores whole numbers, positive or negative (such as 123 or -456), without decimals. Valid types are byte, short, int and long. Which type you should use, depends on the numeric value."
                            "\n\nFloating point types represents numbers with a fractional part, containing one or more decimals. There are two types: float and double.", None),
                            ("Even though there are many numeric types in Java, the most used for numbers are int (for whole numbers) and double (for floating point numbers). However, we will describe them all as you continue to read.", None),
                            ("Integer Types"
                            "\n\nByte"
                            "\n\nThe byte data type can store whole numbers from -128 to 127. This can be used instead of int or other integer types to save memory when you are certain that the value will be within -128 and 127:"
                            , "images/javavariables8.png"),
                            ("Short"
                            "\n\nThe short data type can store whole numbers from -32768 to 32767:", "images/javavariables9.png"),
                            ("Int"
                            "\n\nThe int data type can store whole numbers from -2147483648 to 2147483647. In general, and in our tutorial, the int data type is the preferred data type when we create variables with a numeric value.", "images/javavariables10.png"),
                            ("Long"
                            "\n\nThe long data type can store whole numbers from -9223372036854775808 to 9223372036854775807. This is used when int is not large enough to store the value. Note that you should end the value with an \"L\":"
                            , "images/javavariables11.png"),
                            ("Floating Point Types"
                            "\n\nYou should use a floating point type whenever you need a number with a decimal, such as 9.99 or 3.14515."
                            "\n\nThe float and double data types can store fractional numbers. Note that you should end the value with an \"f\" for floats and \"d\" for doubles:"
                            , None),
                            ("Float Example:", "images/javavariables12.png"),
                            ("Double Example:", "images/Javavariables13.png"),
                            ("Use float or double?"
                            "\nThe precision of a floating point value indicates how many digits the value can have after the decimal point. The precision of float is only six or seven decimal digits, while double variables have a precision of about 15 digits. Therefore it is safer to use double for most calculations."
                            , None),
                            ("Scientific Numbers"
                            "\n\nA floating point number can also be a scientific number with an \"e\" to indicate the power of 10:", "images/javavariables14.png"),
                        ]
                        update_label(lesson4_title, *lesson_content)

                    title2 = Label(lmenu, image=java_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = java_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Java Variables", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Declare Many Variables", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    lesson3_button = Button(lmenu, text="Java Data Types", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)

                    lesson4_button = Button(lmenu, text="Java Numbers", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson4_clicked, bd=0, activebackground="#243142")
                    lesson4_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def javamathc():

                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'javacourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    java_logo = ImageTk.PhotoImage(file="images/java_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        java_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Java Math"
                        lesson_content = [
                            ("The Java Math class has many methods that allows you to perform mathematical tasks on numbers.", None),
                            ("Math.max(x,y)"
                            "\n\nThe Math.max(x,y) method can be used to find the highest value of x and y:", "images/javamath1.png"),
                            ("Math.min(x,y)"
                            "\n\nThe Math.min(x,y) method can be used to find the lowest value of x and y:", "images/javamath2.png"),
                            ("Math.sqrt(x)"
                            "\n\nThe Math.sqrt(x) method returns the square root of x:", "images/javamath3.png"),
                            ("Math.abs(x)"
                            "\n\nThe Math.abs(x) method returns the absolute (positive) value of x:", "images/javamath4.png"),
                            ("Random Numbers"
                            "\n\nMath.random() returns a random number between 0.0 (inclusive), and 1.0 (exclusive):", "images/javamath5.png"),
                            ("To get more control over the random number, for example, if you only want a random number between 0 and 100, you can use the following formula:", "images/javamath6.png"),
                        ]
                        update_label(lesson1_title, *lesson_content)

                    title2 = Label(lmenu, image=java_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = java_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Java Math", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")
                    
                def javaconditionsc():

                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'javacourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    java_logo = ImageTk.PhotoImage(file="images/java_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        java_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Java Conditions and If statements"
                        lesson_content = [
                            ("Java supports the usual logical conditions from mathematics:"
                            "\n\n - Equals: a == b"
                            "\n\n - Not Equals: a != b"
                            "\n\n - Less than: a < b"
                            "\n\n - Less than or equal to: a <= b"
                            "\n\n - Greater than: a > b"
                            "\n\n - Greater than or equal to: a >= b", None),
                            ("These conditions can be used in several ways, most commonly in \"if statements\" and loops."
                            "\n\nAn \"if statement\" is written by using the if keyword.", None),
                            ("In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a."
                            " As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that \"b is greater than a\".", None)
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked(): 
                        lesson2_title = "The if Statement"
                        lesson_content = [
                            ("Use the if statement to specify a block of Java code to be executed if a condition is true.", "images/javaconditions1.png"),
                            ("Note that if is in lowercase letters. Uppercase letters (If or IF) will generate an error."
                            "\n\nIn the example below, we test two values to find out if 20 is greater than 18. If the condition is true, print some text:", "images/javaconditions2.png"),
                            ("We can also test variables:", "images/javaconditions3.png"),
                            ("Example explained"
                            "\nIn the example above we use two variables, x and y, to test whether x is greater than y (using the > operator). As x is 20, and y is 18, and we know that 20 is greater than 18, we print to the screen that \"x is greater than y\".", None),
                            ("", None),
                        ]
                        update_label(lesson2_title, *lesson_content)

                    def lesson3_clicked(): 
                        lesson3_title = "The else Statement"
                        lesson_content = [
                            ("Use the else statement to specify a block of code to be executed if the condition is false.", "images/javaconditions4.png"),
                            ("Example:", "images/javaconditions5.png"),
                            ("Example explained"
                            "\n\nIn the example above, time (20) is greater than 18, so the condition is false. Because of this, we move on to the else condition and print to the screen \"Good evening\". If the time was less than 18, the program would print \"Good day\".", None)
                        ]
                        update_label(lesson3_title, *lesson_content)

                    def lesson4_clicked(): 
                        lesson4_title = "The else if Statement"
                        lesson_content = [
                            ("Use the else if statement to specify a new condition if the first condition is false.", "images/javaconditions6.png"),
                            ("Example:", "images/javaconditions7.png"),
                            ("Example explained"
                            "\n\nIn the example above, time (22) is greater than 10, so the first condition is false. The next condition, in the else if statement, is also false, so we move on to the else condition since condition1 and condition2 is both false - and print to the screen \"Good evening\"."
                            "\n\nHowever, if the time was 14, our program would print \"Good day.\"", None)
                        ]
                        update_label(lesson4_title, *lesson_content)

                    title2 = Label(lmenu, image=java_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = java_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Conditions", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="If statements", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    lesson3_button = Button(lmenu, text="Else statement", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson3_clicked, bd=0, activebackground="#243142")
                    lesson3_button.pack(padx=10, pady=10)

                    lesson4_button = Button(lmenu, text="Else if statement", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson4_clicked, bd=0, activebackground="#243142")
                    lesson4_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")
                    

                def javaloopingc():

                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'javacourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    java_logo = ImageTk.PhotoImage(file="images/java_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        java_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Java For Loop"
                        lesson_content = [
                            ("When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop", "images/javalooping1.png"),
                            ("Statement 1 is executed (one time) before the execution of the code block."
                            "\n\nStatement 2 defines the condition for executing the code block."
                            "\n\nStatement 3 is executed (every time) after the code block has been executed.", None),
                            ("The example below will print the numbers 0 to 4:", "images/javalooping2.png"),
                            ("Example Explained"
                            "\n\nStatement 1 sets a variable before the loop starts (int i = 0)."
                            "\n\nStatement 2 defines the condition for the loop to run (i must be less than 5). If the condition is true, the loop will start over again, if it is false, the loop will end."
                            "\n\nStatement 3 increases a value (i++) each time the code block in the loop has been executed.", None)
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked(): 
                        lesson2_title = "Nested Loops"
                        lesson_content = [
                            ("It is also possible to place a loop inside another loop. This is called a nested loop."
                            "\n\nThe \"inner loop\" will be executed one time for each iteration of the \"outer loop\":", "images/javalooping3.png"),
                        ]
                        update_label(lesson2_title, *lesson_content)

                    title2 = Label(lmenu, image=java_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = java_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Looping", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Nested Loops", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")
                    

                def javafunctionsc():

                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'javacourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    java_logo = ImageTk.PhotoImage(file="images/java_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        java_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Create a Method"
                        lesson_content = [
                            ("A method must be declared within a class."
                            " It is defined with the name of the method, followed by parentheses ()."
                            " Java provides some pre-defined methods, such as System.out.println(), but you can also create your own methods to perform certain actions:", "images/javafunctions1.png"),
                            ("Example Explained"
                            "\n\n - myMethod() is the name of the method"
                            "\n\n - static means that the method belongs to the Main class and not an object of the Main class. You will learn more about objects and how to access methods through objects later in this tutorial."
                            "\n\n - void means that this method does not have a return value. You will learn more about return values later in this chapter", None),
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked(): 
                        lesson2_title = "Call a Method"
                        lesson_content = [
                            ("To call a method in Java, write the method's name followed by two parentheses () and a semicolon;"
                            "\n\nIn the following example, myMethod() is used to print a text (the action), when it is called:", None),
                            ("Example"
                            "\nInside main, call the myMethod() method:", "images/javafunctions2.png"),
                            ("A method can also be called multiple times")            
                        ]
                        update_label(lesson2_title, *lesson_content)

                    title2 = Label(lmenu, image=java_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = java_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Create a Method", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Call a Method", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")
                    
                def javaclassesc():

                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'javacourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    java_logo = ImageTk.PhotoImage(file="images/java_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        java_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Java Classes/Objects"
                        lesson_content = [
                            ("Java is an object-oriented programming language."
                            "\n\nEverything in Java is associated with classes and objects, along with its attributes and methods. For example: in real life, a car is an object."
                            " The car has attributes, such as weight and color, and methods, such as drive and brake."
                            "\n\nA Class is like an object constructor, or a \"blueprint\" for creating objects.", None),
                            ("Create a Class"
                            "\n\nTo create a class, use the keyword class:"
                            "\n\nCreate a class named \"Main\" with a variable x:", "images/javaclass1.png"),
                            ("Remember from the Java Syntax chapter that a class should always start with an uppercase first letter, and that the name of the java file should match the class name.", None)
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked(): 
                        lesson2_title = "Create an Object"
                        lesson_content = [
                            ("In Java, an object is created from a class. We have already created the class named Main, so now we can use this to create objects."
                            "\n\nTo create an object of Main, specify the class name, followed by the object name, and use the keyword new:"
                            "\n\nExample"
                            "\n\nCreate an object called \"myObj\" and print the value of x:", "images/javaclass2.png"),
                            ("Multiple Objects"
                            "\n\nYou can create multiple objects of one class:"
                            "\n\nExample"
                            "\n\nCreate two objects of Main:", "images/javaclass3.png")
                        ]
                        update_label(lesson2_title, *lesson_content)

                    title2 = Label(lmenu, image=java_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = java_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Java Classes/Objects", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Create an Object", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def javadatastructuresc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'javacourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    java_logo = ImageTk.PhotoImage(file="images/java_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        java_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Types of Data Structures in Java"
                        lesson_content = [
                            ("Here is the list of some of the common types of data structures in Java:"
                            "\n\n - Array"
                            "\n\n - Linked List"
                            "\n\n - Stack"
                            "\n\n - Queue"
                            "\n\n - Binary Tree"
                            "\n\n - Binary Search Tree"
                            "\n\n - Heap"
                            "\n\n - Hashing"
                            "\n\n - Graph", None),
                            ("Here is the pictorial representation of types of java data structures", "images/javads1.png"),
                        ]
                        update_label(lesson1_title, *lesson_content)

                    def lesson2_clicked(): 
                        lesson2_title = "Further classification of types of Data Structures"
                        lesson_content = [
                            ("There are two types of Data Structures:"
                            "\n\n - Primitive Data Structures"
                            "\n\n - Non-primitive Data Structures", None),
                            ("Primitive data Structures are also called Primitive Data Types. byte, short,  int, float, char, boolean, long, and double are primitive Data types.", None),
                            ("Non-primitive data Structures – Non-primitive Data Structures are of two types:"
                            "\n\n - Linear Data Structures"
                            "\n\n - Non-Linear Data Structures", "images/javads2.png"),
                            ("Linear Data Structures – The elements arranged in a linear fashion are called Linear Data Structures. Here, each element is connected to one other element only. Linear Data Structures are as follows:", None),
                        ]
                        update_label(lesson2_title, *lesson_content)

                    title2 = Label(lmenu, image=java_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = java_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Data Structures in Java", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    lesson2_button = Button(lmenu, text="Further Classification", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson2_clicked, bd=0, activebackground="#243142")
                    lesson2_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                def javaalgorithmsc():
                    menuc.pack_forget()
                    nav_bar.pack_forget()
                    course_window.pack_forget()
                    self.window.minsize(1102, 618)
                    self.window.maxsize(1102, 618)
                    rmenu = Frame(self.window, bg="#162334")
                    lmenu = Frame(self.window, bg="#243142")
                    current_directory = os.getcwd()
                    script_dir = os.path.join(current_directory, 'courses', 'javacourses')
                    os.chdir(script_dir)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                    self.window.grid_rowconfigure(0, weight=1)
                    self.window.grid_columnconfigure(0, weight=0)
                    self.window.grid_columnconfigure(1, weight=1)
                    title = Label(
                        rmenu,
                        text="Select a Lesson!",
                        font=("Arial", 24, "bold"),
                        fg="#FF8D06",
                        bg="#162334",
                    )
                    title.pack(padx=10, pady=50)

                    scrollbar = Scrollbar(rmenu)
                    scrollbar.pack(side=RIGHT, fill=Y)

                    rframe = Canvas(
                        rmenu,
                        bg="#162334",
                        yscrollcommand=scrollbar.set,
                        highlightthickness=0,
                    )
                    rframe.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

                    scrollbar.config(command=rframe.yview)

                    content_frame = Frame(rframe, bg="#162334")
                    rframe.create_window((0, 0), window=content_frame, anchor=NW)

                    content_labels = []
                    imagetest = None

                    rframe.pack(fill=BOTH, expand=True)
                    def update_label(title_text, *content_texts):
                        nonlocal content_labels
                        title.config(text=title_text)

                        for label in content_labels:
                            label.destroy()

                        content_labels = []

                        for i, content_text in enumerate(content_texts):
                            if isinstance(content_text, tuple) and len(content_text) == 2:
                                text, image_path = content_text
                            else:
                                text, image_path = content_text, None

                            label_content = Label(
                                content_frame,
                                text=text,
                                font=("Arial", 14),
                                fg="#FFBD59",
                                bg="#162334",
                                justify="left",
                                wraplength=820,
                            )
                            label_content.pack(padx=5, pady=10)
                            content_labels.append(label_content)

                            if image_path is not None:
                                display_image(image_path)

                        if all(image_path is None for _, image_path in content_texts):
                            clear_image()

                        rframe.update_idletasks()
                        rframe.config(scrollregion=rframe.bbox("all"))

                    def display_image(*image_paths):
                        nonlocal content_labels
                        max_height = 500

                        for image_path in image_paths:
                            image = Image.open(image_path)
                            width, height = image.size
                            new_height = min(height, max_height)
                            new_width = int((new_height / height) * width)
                            image = image.resize((new_width, new_height))
                            photo = ImageTk.PhotoImage(image)
                            label = Label(content_frame, image=photo, background="#2F496B", highlightthickness=0)
                            label.image = photo
                            label.pack(padx=5, pady=10, anchor="center")
                            content_labels.append(label)

                    def clear_image():
                        if imagetest is not None:
                            imagetest.destroy()

                    java_logo = ImageTk.PhotoImage(file="images/java_logo.png")
                    backb = ImageTk.PhotoImage(file="images/backb.png")

                    def back():
                        rmenu.grid_forget()
                        lmenu.grid_forget()
                        java_clicked()

                    def lesson1_clicked(): 
                        lesson1_title = "Bubble Sort"
                        lesson_content = [
                            ("Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order."
                            "Just like the movement of air bubbles in the water that rise up to the surface, each element of the array move to the end in each iteration. Therefore, it is called a bubble sort.", None),
                            ("How does Bubble Sort Algorithm Work?"
                            "\n\n - Starting from the first index, compare the first and the second elements."
                            "\n\n - If the first element is greater than the second element, they are swapped."
                            "\n\n - Now, compare the second and the third elements. Swap them if they are not in order."
                            "\n\n - The above process goes on until the last element.", "images/javaalgo1.png"),
                            ("", "images/javaalgo2.png")
                        ]
                        update_label(lesson1_title, *lesson_content)

                    title2 = Label(lmenu, image=java_logo, font=("Arial", 24, "bold"), fg="#FF5757", bg="#243142")
                    title2.image = java_logo
                    title2.pack(padx=10, pady=30)

                    lesson1_button = Button(lmenu, text="Bubble Sorting", font=("Arial", 13, "bold"), fg="#FFBD59", bg="#243142", command=lesson1_clicked, bd=0, activebackground="#243142")
                    lesson1_button.pack(padx=10, pady=10)

                    back_button = Button(lmenu, image=backb, font=("Arial", 24, "bold"), bg="#243142", fg="#FF8D06", command=back, activebackground="#2f4460", bd=0)
                    back_button.image = backb
                    back_button.pack(padx=10, pady=50, anchor="s")

                    lmenu.configure(width=200, height=618)
                    lmenu.pack_propagate(0)
                    rmenu.grid(row=0, column=1, sticky="nsew")
                    lmenu.grid(row=0, column=0, sticky="ns")

                ### images title

                javapath = os.path.join(current_directory, "images/java_logo.png")
                java = ImageTk.PhotoImage(file=javapath)

                beginnerpath = os.path.join(current_directory, "images/beginner.png")
                beginner = ImageTk.PhotoImage(file=beginnerpath)

                backbpath = os.path.join(current_directory, "images/backb.png")
                backb = ImageTk.PhotoImage(file=backbpath)

                intermediatepath = os.path.join(current_directory, "images/intermediate.png")
                intermediate = ImageTk.PhotoImage(file=intermediatepath)

                advancedpath = os.path.join(current_directory, "images/advanced.png")
                advanced = ImageTk.PhotoImage(file=advancedpath)

                ###

                ### images selection 1

                pythonsyntaxpath = os.path.join(current_directory, "images/pythonsyntax.png")
                pythonsyntax = ImageTk.PhotoImage(file=pythonsyntaxpath)

                cppvariablespath = os.path.join(current_directory, "images/variables.png")
                cppvariables = ImageTk.PhotoImage(file=cppvariablespath)

                cppmathpath = os.path.join(current_directory, "images/cppmath.png")
                cppmath = ImageTk.PhotoImage(file=cppmathpath)

                pythonconditionspath = os.path.join(current_directory, "images/pythonconditions.png")
                pythonconditions = ImageTk.PhotoImage(file=pythonconditionspath)

                cpploopingpath = os.path.join(current_directory, "images/cpplooping.png")
                cpplooping = ImageTk.PhotoImage(file=cpploopingpath)

                ###

                ### images selection 2

                pythonfunctionspath = os.path.join(current_directory, "images/pythonfunctions.png")
                pythonfunctions = ImageTk.PhotoImage(file=pythonfunctionspath)

                cppclassespath = os.path.join(current_directory, "images/cppclasses.png")
                cppclasses = ImageTk.PhotoImage(file=cppclassespath)

                cppinheritancepath = os.path.join(current_directory, "images/cppinheritance.png")
                cppinheritance = ImageTk.PhotoImage(file=cppinheritancepath)

                ###

                ### images selection 3

                cppdatastructurespath = os.path.join(current_directory, "images/cppdatastructures.png")
                cppdatastructures = ImageTk.PhotoImage(file=cppdatastructurespath)

                cppalgorithmspath = os.path.join(current_directory, "images/cppalgorithms.png")
                cppalgorithms = ImageTk.PhotoImage(file=cppalgorithmspath)

                ###


                nav_bar = Frame(self.window, bg="#182B44", height=30)
                nav_bar.pack(fill=X)

                nav_bar.grid_columnconfigure(0, weight=1)
                nav_bar.grid_columnconfigure(2, weight=1)

                nav_header = Label(nav_bar, image=java, bg="#182B44", fg="#00E69A", font=("Arial", 24, "bold"))
                nav_header.image = java
                nav_header.grid(row=0, column=1, pady=20)

                back_navbutt = Button(
                    nav_bar, image=backb, 
                    bg="#182B44", 
                    fg="#00E69A", 
                    font=("Arial", 24, "bold"), 
                    bd=0, 
                    highlightthickness=0, 
                    activebackground="#182B44", 
                    command=back
                    )
                back_navbutt.image = backb
                back_navbutt.grid(row=0, column=0, padx=50, pady=20, sticky="w")

                course_window = Canvas(self.window, bg="#162334", highlightthickness=0)
                course_window.pack(fill=BOTH,expand=True, anchor=CENTER)

                courses = Frame(course_window, bg="#162334")

                scrollbar = Scrollbar(course_window)
                scrollbar.pack(side=RIGHT, fill=Y)

                scrollbar.config(command=course_window.yview)
                course_window.config(yscrollcommand=scrollbar.set)

                course_title = Label(courses, image=beginner, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"))
                course_title.pack(anchor="w", padx=100, pady=50)

                courses_selection1 = Frame(courses, bg="#162334")
                courses_selection1.pack(fill="both", padx=200)

                course1 = Button(courses_selection1, image=introd, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=javaintroduction)
                course1.image = introd
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                course2 = Button(courses_selection1, image=cppvariables, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=javavariablesc)
                course2.image = cppvariables
                course2.grid(row=0, column=1, columnspan=1, padx=50, pady=30)

                course3 = Button(courses_selection1, image=cppmath, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=javamathc)
                course3.image = cppmath
                course3.grid(row=0, column=2, columnspan=1, padx=50, pady=30)

                course4 = Button(courses_selection1, image=pythonconditions, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=javaconditionsc)
                course4.image = pythonconditions
                course4.grid(row=0, column=3, columnspan=1, padx=50, pady=30)

                course5 = Button(courses_selection1, image=cpplooping, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=javaloopingc)
                course5.image = cpplooping
                course5.grid(row=0, column=4, columnspan=1, padx=50, pady=30)

                diff_title = Label(courses, image=intermediate, bg="#162334", fg="#7FFFD4", font=("Arial", 24, "bold"))
                diff_title.image = intermediate
                diff_title.pack(anchor="w", padx=100, pady=50)

                courses_selection2 = Frame(courses, bg="#162334")
                courses_selection2.pack(fill="both", padx=200)

                course1 = Button(courses_selection2, image=pythonfunctions, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=javafunctionsc)
                course1.image = pythonfunctions
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                course3 = Button(courses_selection2, image=cppinheritance, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=javaclassesc)
                course3.image = cppinheritance
                course3.grid(row=0, column=2, columnspan=1, padx=50, pady=30)

                diff2_title = Label(courses, image=advanced, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"))
                diff2_title.image = advanced
                diff2_title.pack(anchor="w", padx=100, pady=50)

                courses_selection3 = Frame(courses, bg="#162334")
                courses_selection3.pack(fill="both", padx=200)

                course1 = Button(courses_selection3, image=cppdatastructures, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=javadatastructuresc)
                course1.image = cppdatastructures
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                course2 = Button(courses_selection3, image=cppalgorithms, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=javaalgorithmsc)
                course2.image = cppalgorithms
                course2.grid(row=0, column=1, columnspan=1, padx=50, pady=30)

                # Change the image of course1 in courses_selection1
                course_window.create_window((0, 0), window=courses, anchor="nw")

                course_window.update_idletasks()
                course_window.config(scrollregion=course_window.bbox("all"))

            def js_clicked():
                menu_directory = os.path.dirname(os.path.abspath(__file__))
                os.chdir(menu_directory)
                self.window.minsize(1600,900)
                self.window.maxsize(1600,900)
                current_directory = os.getcwd()

                introd = ImageTk.PhotoImage(file="images/introd.png")
                def back():
                    course_window.pack_forget()
                    nav_bar.pack_forget()
                    menu()

                def launch_py(script_name):
                    pass
                
                def jsintroduction():
                    launch_py('pyintroductory.py')

                def jsvariablesc():
                    launch_py('pyvariables.py')

                def jsmathc():
                    launch_py('pymath.py')
                    
                def jsconditionsc():
                    launch_py('pyconditions.py')

                def jsloopingc():
                    launch_py('pylooping.py')

                def jsfunctionsc():
                    launch_py('pyfunctions.py')

                def jsfilehandlingc():
                    launch_py('pyfilehandling.py')

                def jsinheritancec():
                    launch_py('pyinheritance.py')

                def jsdatastructuresc():
                    launch_py('pydatastructures.py')

                def jsalgorithmsc():
                    launch_py('pyalgorithms.py')

                ### images title

                jspath = os.path.join(current_directory, "images/js_logo.png")
                js = ImageTk.PhotoImage(file=jspath)

                beginnerpath = os.path.join(current_directory, "images/beginner.png")
                beginner = ImageTk.PhotoImage(file=beginnerpath)

                backbpath = os.path.join(current_directory, "images/backb.png")
                backb = ImageTk.PhotoImage(file=backbpath)

                intermediatepath = os.path.join(current_directory, "images/intermediate.png")
                intermediate = ImageTk.PhotoImage(file=intermediatepath)

                advancedpath = os.path.join(current_directory, "images/advanced.png")
                advanced = ImageTk.PhotoImage(file=advancedpath)

                ###

                ### images selection 1

                cppvariablespath = os.path.join(current_directory, "images/variables.png")
                cppvariables = ImageTk.PhotoImage(file=cppvariablespath)

                pythonconditionspath = os.path.join(current_directory, "images/pythonconditions.png")
                pythonconditions = ImageTk.PhotoImage(file=pythonconditionspath)

                cpploopingpath = os.path.join(current_directory, "images/cpplooping.png")
                cpplooping = ImageTk.PhotoImage(file=cpploopingpath)

                ###

                ### images selection 2

                pythonfunctionspath = os.path.join(current_directory, "images/pythonfunctions.png")
                pythonfunctions = ImageTk.PhotoImage(file=pythonfunctionspath)

                ###

                ### images selection 3

                cppdatastructurespath = os.path.join(current_directory, "images/cppdatastructures.png")
                cppdatastructures = ImageTk.PhotoImage(file=cppdatastructurespath)

                cppalgorithmspath = os.path.join(current_directory, "images/cppalgorithms.png")
                cppalgorithms = ImageTk.PhotoImage(file=cppalgorithmspath)

                ###


                nav_bar = Frame(self.window, bg="#182B44", height=30)
                nav_bar.pack(fill=X)

                nav_bar.grid_columnconfigure(0, weight=1)
                nav_bar.grid_columnconfigure(2, weight=1)

                nav_header = Label(nav_bar, image=js, bg="#182B44", fg="#00E69A", font=("Arial", 24, "bold"))
                nav_header.image = js
                nav_header.grid(row=0, column=1, pady=20)

                back_navbutt = Button(
                    nav_bar, image=backb, 
                    bg="#182B44", 
                    fg="#00E69A", 
                    font=("Arial", 24, "bold"), 
                    bd=0, 
                    highlightthickness=0, 
                    activebackground="#182B44", 
                    command=back
                    )
                back_navbutt.image = backb
                back_navbutt.grid(row=0, column=0, padx=50, pady=20, sticky="w")

                course_window = Canvas(self.window, bg="#162334", highlightthickness=0)
                course_window.pack(fill=BOTH,expand=True, anchor=CENTER)

                courses = Frame(course_window, bg="#162334")

                scrollbar = Scrollbar(course_window)
                scrollbar.pack(side=RIGHT, fill=Y)

                scrollbar.config(command=course_window.yview)
                course_window.config(yscrollcommand=scrollbar.set)

                course_title = Label(courses, image=beginner, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"))
                course_title.pack(anchor="w", padx=100, pady=50)

                courses_selection1 = Frame(courses, bg="#162334")
                courses_selection1.pack(fill="both", padx=200)

                course1 = Button(courses_selection1, image=introd, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=jsintroduction)
                course1.image = introd
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                course2 = Button(courses_selection1, image=cppvariables, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=jsvariablesc)
                course2.image = cppvariables
                course2.grid(row=0, column=1, columnspan=1, padx=50, pady=30)

                course4 = Button(courses_selection1, image=pythonconditions, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=jsconditionsc)
                course4.image = pythonconditions
                course4.grid(row=0, column=2, columnspan=1, padx=50, pady=30)

                course5 = Button(courses_selection1, image=cpplooping, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=jsloopingc)
                course5.image = cpplooping
                course5.grid(row=0, column=3, columnspan=1, padx=50, pady=30)

                diff_title = Label(courses, image=intermediate, bg="#162334", fg="#7FFFD4", font=("Arial", 24, "bold"))
                diff_title.image = intermediate
                diff_title.pack(anchor="w", padx=100, pady=50)

                courses_selection2 = Frame(courses, bg="#162334")
                courses_selection2.pack(fill="both", padx=200)

                course1 = Button(courses_selection2, image=pythonfunctions, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=jsfunctionsc)
                course1.image = pythonfunctions
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                diff2_title = Label(courses, image=advanced, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"))
                diff2_title.image = advanced
                diff2_title.pack(anchor="w", padx=100, pady=50)

                courses_selection3 = Frame(courses, bg="#162334")
                courses_selection3.pack(fill="both", padx=200)

                course1 = Button(courses_selection3, image=cppdatastructures, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=jsdatastructuresc)
                course1.image = cppdatastructures
                course1.grid(row=0, column=0, columnspan=1, padx=50, pady=30)

                course2 = Button(courses_selection3, image=cppalgorithms, bg="#162334", fg="#00E69A", font=("Arial", 24, "bold"), bd=0, activebackground="#2A4160", command=jsalgorithmsc)
                course2.image = cppalgorithms
                course2.grid(row=0, column=1, columnspan=1, padx=50, pady=30)

                # Change the image of course1 in courses_selection1
                course_window.create_window((0, 0), window=courses, anchor="nw")

                course_window.update_idletasks()
                course_window.config(scrollregion=course_window.bbox("all"))

            def courses_clicked():
                menuc.pack_forget()
                loginc.pack_forget()
                python_icon = ImageTk.PhotoImage(file="images/python logo.png")
                cpp_icon = ImageTk.PhotoImage(file="images/cpp_logo.png")
                java_icon = ImageTk.PhotoImage(file="images/java.png")
                js_icon = ImageTk.PhotoImage(file="images/js_logo.png")
                algo_icon = ImageTk.PhotoImage(file="images/algorithmimg.png")
                courses_icon = ImageTk.PhotoImage(file="images/coursestitle.png")
                back_buttonimg = ImageTk.PhotoImage(file="images/backb.png")

                def python():
                    self.window.destroy()
                    subprocess.call(['python', 'pythoncl.py'])
                def back():
                    courses.pack_forget()
                    menu()
                courses = Frame(self.window, bg="#162334")
                courses.pack(fill=BOTH, expand=True)
                title = Label(courses, image=courses_icon, font=("Arial", 24, "bold"), bg="#162334", fg="#FFBD59")

                title.image = courses_icon
                title.pack(anchor="w",padx=30, pady=30)

                courses_frames = Frame(courses, bg="#1D3350")
                courses_frames.pack(padx=0, pady=20)

                python_button = Button(courses_frames, image=python_icon, bg="#1D3350", bd=0, activebackground="#1D2734", command=python)
                python_button.image = python_icon
                python_label = Label(courses_frames, text="Python", font=("Arial", 24, "bold"), bg="#1D3350", padx=20, pady=10, fg="#FFBD59", bd=0)

                cpp_button = Button(courses_frames, image=cpp_icon, bg="#1D3350", bd=0, activebackground="#1D2734")
                cpp_button.image = cpp_icon
                cpp_label = Label(courses_frames, text="C++", font=("Arial", 24, "bold"), bg="#1D3350", padx=20, pady=10, fg="#FFBD59", bd=0)

                java_button = Button(courses_frames, image=java_icon, bg="#1D3350", bd=0, activebackground="#1D2734")
                java_button.image = java_icon
                java_label = Label(courses_frames, text="Java", font=("Arial", 24, "bold"), bg="#1D3350", padx=20, pady=10, fg="#FFBD59", bd=0)

                js_button = Button(courses_frames, image=js_icon, bg="#1D3350", bd=0, activebackground="#1D2734")
                js_button.image = js_icon
                js_label = Label(courses_frames, text="JavaScript", font=("Arial", 24, "bold"), bg="#1D3350", padx=20, pady=10, fg="#FFBD59", bd=0)

                algo_button = Button(courses_frames, image=algo_icon, bg="#1D3350", bd=0, activebackground="#1D2734")
                algo_button.image = algo_icon
                algo_label = Label(courses_frames, text="Algorithm", font=("Arial", 24, "bold"), bg="#1D3350", padx=20, pady=10, fg="#FFBD59", bd=0)

                back_button = Button(courses, image=back_buttonimg, bg="#162334", bd=0, command=back, activebackground="#2f4460")
                back_button.image = back_buttonimg
                back_button.place(relx=0.9, rely=0.97, anchor="se")

                python_button.grid(row=0, column=0, padx=30, pady=10)
                python_label.grid(row=1, column=0, padx=30)

                cpp_button.grid(row=0, column=1, padx=30, pady=10)
                cpp_label.grid(row=1, column=1, padx=30)

                java_button.grid(row=0, column=2, padx=30, pady=10)
                java_label.grid(row=1, column=2, padx=30)

                js_button.grid(row=0, column=3, padx=30, pady=10)
                js_label.grid(row=1, column=3, padx=30)

                algo_button.grid(row=2, column=2, padx=30, pady=10)
                algo_label.grid(row=3, column=2, padx=30)

            def projects_clicked(self):
                cd = os.getcwd()
                print(cd)
                project3img = ImageTk.PhotoImage(file="images/itrim.png")
                def back():
                    nav_bar.pack_forget()
                    menu()
                def get_solved_problem_set(user_id):   
                    query = "SELECT solved_psets FROM users WHERE id = %s"
                    self.c.execute(query, (user_id,))
                    result = self.c.fetchone()
                    if result:
                        problem_sets = result[0].split(',')
                        return problem_sets
                    else:
                        return []
                problem_sets = get_solved_problem_set(self.logged_in_user_id)

                menuc.pack_forget()
                
                nav_bar = Frame(self.window, bg="#162334")
                nav_bar.pack(fill=X)

                nav_bar.grid_columnconfigure(0, weight=1)
                nav_bar.grid_columnconfigure(2, weight=1)

                title = Label(nav_bar, text=f"Hello, {username}", font=("Arial", 24, "bold"), bg="#162334", pady=10, fg="#FFBD59", bd=0)
                title.grid(row=0, column=1, pady=20)
                back_button = Button(nav_bar, text="Back", font=("Arial", 24, "bold"), bg="#162334", pady=10, fg="#FFBD59", bd=0, activebackground="#1D3350", activeforeground="white", command=back)
                back_button.grid(row=0, column=0, pady=20,padx=0)

                projects_frame = Frame(self.window, bg="#1D3350")
                projects_frame.pack(fill=BOTH, expand=TRUE)

                if '0wordcap' in problem_sets:
                    project1 = Label(projects_frame, image=self.project1img, bg="#1D3350", bd=0)
                    project1_label = Label(projects_frame, text="Word Capitalization", font=("Arial", 16, "bold"), bg="#1D3350", padx=20, pady=10, fg="#FFBD59", bd=0)
                    project1.grid(row=0, column=0, padx=70, pady=40)
                    project1_label.grid(row=1, column=0, padx=70, pady=0)

                if 'CTT' in problem_sets:
                    project2 = Label(projects_frame, image=self.project2img, bg="#1D3350", bd=0)
                    project2_label = Label(projects_frame, text="Complete the Triplets", font=("Arial", 16, "bold"), bg="#1D3350", padx=20, pady=10, fg="#FFBD59", bd=0)
                    project2.grid(row=0, column=1, padx=70, pady=40)
                    project2_label.grid(row=1, column=1, padx=70, pady=0)

                if 'ITR' in problem_sets:
                    project3 = Label(projects_frame, image=project3img, bg="#1D3350", bd=0)
                    project3.image = project3img
                    project3_label = Label(projects_frame, text="Integer to Roman", font=("Arial", 16, "bold"), bg="#1D3350", padx=20, pady=10, fg="#FFBD59", bd=0)
                    project3.grid(row=0, column=1, padx=70, pady=40)
                    project3_label.grid(row=1, column=1, padx=70, pady=0)

            def settings_clicked():
                menuc.master.destroy()
                subprocess.call(['python','settings.py'])
            def leaderboards_clicked():
                def back():
                    lb_canvas.pack_forget()
                    menu()
                menuc.pack_forget()
                loginc.pack_forget()
                
                lb_canvas = Canvas(self.window, bg="#162334", highlightthickness=0)
                bg_image_item = lb_canvas.create_image(0, 0, anchor=tk.NW, image=self.menu_bg_image)
                lb_canvas.place(relwidth=1, relheight=1)

                lbs = Frame(lb_canvas, bg="#162334")
                lbs.place(x=551, y=309, anchor=CENTER)

                query = "SELECT username, scores FROM users ORDER BY scores DESC"
                self.c.execute(query)
                leaderboard_data = self.c.fetchall()

                for i, entry in enumerate(leaderboard_data):
                    username = entry[0]
                    score = entry[1] * 30

                    leaderboard_entry = "{:<5} {:<20} {:>20}".format(str(i+1), username, str(score))
                    leaderboard_label = Label(lbs, text=leaderboard_entry, bg="#162334", font=("Courier New", 20, "bold"))
                    leaderboard_label.grid(row=i, column=0, padx=(20, 0), pady=5, sticky="w")
                    leaderboard_label['foreground'] = "#FFBD59"

                    back_button = Button(lbs, image=self.back_image2, borderwidth=0, padx=0, pady=0,
                                        bg="#162334", activebackground="#162334", command=back)
                    back_button.grid(row=len(leaderboard_data) + 1, column=0)

            def exit_clicked():
                confirm = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
                if confirm:
                    menuc.quit()

            loginc.pack_forget()
            menuc = tk.Canvas(self.window, bg="#162334", highlightthickness=0)
            bg_image_item = menuc.create_image(0, 0, anchor=tk.NW, image=self.menu_bg_image)
            menuc.place(relwidth=1, relheight=1)

            python_icon = ImageTk.PhotoImage(file="images/python logo.png")
            cpp_icon = ImageTk.PhotoImage(file="images/cpp_logo.png")
            java_icon = ImageTk.PhotoImage(file="images/java.png")
            js_icon = ImageTk.PhotoImage(file="images/js_logo.png")
            label_img = ImageTk.PhotoImage(file="images/learn_now.png")
            
            user_iconimg = ImageTk.PhotoImage(file="images/usericon.png")
            lb_icon = ImageTk.PhotoImage(file="images/leaderboardsb.png")
            courses_icon = ImageTk.PhotoImage(file="images/courses.png")
            projects_icon = ImageTk.PhotoImage(file="images/projects.png")
            settings_icon = ImageTk.PhotoImage(file="images/settings.png")
            pset_icon = ImageTk.PhotoImage(file="images/problemsets.png")
            exit_icon = ImageTk.PhotoImage(file="images/exit2.png")
    
            user_label_context = f"{username}"
            scores_context = scores * 30

            user_icon = tk.Label(menuc, image=user_iconimg, bg="#162334")
            user_icon.image = user_iconimg
            user_icon.place(x=50, y=10)
            user_label = tk.Label(menuc, text=user_label_context, bg="#162334", font=("Arial", 17, "bold"), fg="#FFBD59")
            user_label.place(x=120, y=20)
            scores = tk.Label(menuc, text=scores_context, bg="#162334", font=("Arial", 17), fg="#FFBD59")
            scores.place(x=120, y=67)

            prepare_label = tk.Label(menuc, image=label_img, bg="#162334")
            prepare_label.image = label_img
            prepare_label.place(x=40, y=120)

            python_button = tk.Button(menuc, image=python_icon, bg="#162334", bd=0, command=python_clicked, activebackground="#1D2734")
            python_label = tk.Label(menuc, text="Python", font=("Arial", 24, "bold"), bg="#162334", padx=20, pady=10, fg="#FFBD59", bd=0)
            python_button.image = python_icon
            python_label.place(x=110,y=410)
            python_button.place(x=120, y=260)

            cpp_button = tk.Button(menuc, image=cpp_icon, bg="#162334", bd=0, command=cpp_clicked, activebackground="#1D2734")
            cpp_label = tk.Label(menuc, text="C++", font=("Arial", 24, "bold"), bg="#162334", padx=20, pady=10, fg="#FFBD59", bd=0)
            cpp_button.image = cpp_icon
            cpp_label.place(x=375,y=410)
            cpp_button.place(x=370, y=260)
            

            java_button = tk.Button(menuc, image=java_icon, bg="#162334", bd=0, command=java_clicked, activebackground="#1D2734")
            java_label = tk.Label(menuc, text="Java", font=("Arial", 24, "bold"), bg="#162334", padx=20, pady=10, fg="#FFBD59", bd=0)
            java_button.image = java_icon
            java_label.place(x=610,y=410)
            java_button.place(x=620, y=260)

            js_button = tk.Button(menuc, image=js_icon, bg="#162334", bd=0, command=js_clicked, activebackground="#1D2734")
            js_label = tk.Label(menuc, text="JavaScript", font=("Arial", 24, "bold"), bg="#162334", padx=20, pady=10, fg="#FFBD59", bd=0)
            js_button.image = js_icon
            js_label.place(x=800,y=410)
            js_button.place(x=840, y=260)

            ##Buttons Below
            courses_button = tk.Button(menuc, image=courses_icon, bg="#162334", bd=0, command=courses_clicked, activebackground="#1D2734")
            courses_button.image = courses_icon
            courses_button.place(x=40+130, y=530)

            projects_button = tk.Button(menuc, image=projects_icon, bg="#162334", bd=0, command=lambda: projects_clicked(self), activebackground="#1D2734")
            projects_button.image = projects_icon
            projects_button.place(x=40, y=530)

            settings_button = tk.Button(menuc, image=settings_icon, bg="#162334", bd=0, command=settings_clicked, activebackground="#1D2734")
            settings_button.image = settings_icon
            settings_button.place(x=40+140*4, y=530)

            lb_button = tk.Button(menuc, image=lb_icon, bg="#162334", bd=0, command=leaderboards_clicked, activebackground="#1D2734")
            lb_button.image = lb_icon
            lb_button.place(x=40+130*3, y=530)

            psets_button = tk.Button(menuc, image=pset_icon, bg="#162334", bd=0, command=psets_clicked, activebackground="#1D2734")
            pset_icon.image = pset_icon
            psets_button.place(x=40+130*2, y=530)

            exit_button = tk.Button(menuc, image=exit_icon, bg="#162334", bd=0, command=exit_clicked, activebackground="#1D2734")
            exit_button.image = exit_icon
            exit_button.place(x=950, y=530)
        # Menu --------------------------------------------------------
        self.canvas.pack_forget()
        loginc = tk.Canvas(self.window, bg="#162334", highlightthickness=0)
        bg_image_item = loginc.create_image(0, 0, anchor=tk.NW, image=self.canvas.bg_image)
        loginc.place(relwidth=1, relheight=1)

        def on_enter(e):
            userlogin.delete(0, 'end')

        def on_leave():
            name = userlogin.get()
            if name == '':
                userlogin.insert(0, 'Enter Username')

        userlogin = tk.Entry(loginc, width=25, fg="#162334", border=2, bg="#4E7896",
                             font=("Bebas Neue", 18, 'bold'), relief=tk.SOLID, bd=1,
                             highlightthickness=1, highlightbackground="#4E7896")
        userlogin.insert(0, 'Username')
        userlogin.bind("<FocusIn>", on_enter)
        userlogin.bind("<FocusOut>", on_leave)

        def on_enter(e):
            passlogin.delete(0, 'end')

        def on_leave():
            name = passlogin.get()
            if name == '':
                passlogin.insert(0, 'Enter Username')

        passlogin = tk.Entry(loginc, width=25, fg="#162334", border=2, bg="#4E7896",
                             font=("Bebas Neue", 18, 'bold'), relief=tk.SOLID, bd=1,
                             highlightthickness=1, highlightbackground="#4E7896")

        passlogin.insert(0, 'Password')
        passlogin.bind("<FocusIn>", on_enter)
        passlogin.bind("<FocusOut>", on_leave)
        passlogin.config(show="*")

        def login():
            username = userlogin.get()
            password = passlogin.get()

            query = "SELECT id FROM users WHERE username = %s AND password = %s"
            self.c.execute(query,(username, password))
            result = self.c.fetchone()
            login_manager.login(username, password)

            if login_manager.logged_in:
                self.logged_in_user_id = result[0]
                with open('login_status.txt', 'w') as file:
                    file.write('Logged in')
                messagebox.showinfo("Login Successful", "You have successfully logged in!")
                menu()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")
        userlogin.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        passlogin.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        login_button = tk.Button(loginc, image=self.login_image, borderwidth=0, padx=0, pady=0,
                                 bg="#162334", activebackground="#162334", command=login)
        login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        back_button = Button(loginc, image=self.back_image2, borderwidth=0, padx=0, pady=0,
                                 bg="#162334", activebackground="#162334", command=back)
        back_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        loginc.pack(fill=tk.BOTH, expand=True)

    def option(self):
        def on_resize(event):
            window_width = event.width
            window_height = event.height
            settings_x = int(window_width * 0.3)
            settings_y = int(window_height * 0.3)
            settings_width = int(window_width * 0.6)
            settings_height = int(window_height * 0.4)

            optionc.config(width=window_width, height=window_height)

            resized_bg_image = self.option_bg_image.resize((window_width, window_height), Image.ANTIALIAS)
            bg_photo = ImageTk.PhotoImage(resized_bg_image)
            bg_image_item = optionc.create_image(0, 0, anchor=tk.NW, image=bg_photo)
            optionc.image = bg_photo

            audiob.place(x=165, y=220, anchor=tk.CENTER)
            languageb.place(x=165, y=290, anchor=tk.CENTER)
            infob.place(x=165, y=360, anchor=tk.CENTER)
            backb.place(x=165, y=450, anchor=tk.CENTER)

            settings_frame.place(x=settings_x, y=settings_y, width=settings_width, height=settings_height)

        def show_audio_settings():
            clear_settings_frame()

            audio_label = tk.Label(settings_frame, text="Audio Settings", font=("Arial", 18, "bold"), bg="#4E7896", fg="#FFBD59")
            audio_label.pack()

            overall_volume_label = tk.Label(settings_frame, text="Overall Volume", font=("Arial", 18, "bold"), bg="#4E7896", fg="white")
            overall_volume_label.pack()

        def show_language_settings():
            clear_settings_frame()

            language_label = tk.Label(settings_frame, text="Language Settings", font=("Arial", 18, "bold"), bg="#4E7896", fg="#FFBD59")
            language_label.pack()

            tagalog_disabled_var = tk.BooleanVar()
            tagalog_label_checkbutton = tk.Checkbutton(settings_frame, text="Tagalog", font=("Arial", 18, "bold"), bg="#4E7896", fg="white", variable=tagalog_disabled_var)
            tagalog_label_checkbutton.pack()

        def show_info_settings():
            clear_settings_frame()

            info_label = tk.Label(settings_frame, text="Info Settings", font=("Arial", 18, "bold"), bg="#4E7896", fg="#FFBD59")
            info_label.pack()

            infobg_label = tk.Label(settings_frame, text="A group of three people, Jim Hernandez, Carl Villanueva,\nand Denelle Ocsena, created the game CodeQuest.\nOne of the most challenging subjects to take, according to some,\n is programming. Therefore, our aim was to develop an educational \ngame that teaches programming while allowing players\n to have fun and be delighted.", font=("Arial", 15), bg="#4E7896", fg="#FFBD59")
            infobg_label.pack()

        def clear_settings_frame():
            for widget in settings_frame.winfo_children():
                widget.destroy()

        def back():
            optionc.forget()
            self.home()

        self.canvas.forget()

        optionc = tk.Canvas(self.window, width=1102, height=618, highlightthickness=0, bg="#162334")
        optionc.pack(fill=tk.BOTH, expand=True)
        audiob = tk.Button(optionc, image=self.audio_image, borderwidth=0, padx=0, pady=0, bg="#162334", activebackground="#162334", command=show_audio_settings)
        languageb = tk.Button(optionc, image=self.language_image, borderwidth=0, padx=0, pady=0, bg="#162334", activebackground="#162334", command=show_language_settings)
        optionc.bind("<Configure>", on_resize)
        infob = tk.Button(optionc, image=self.info_image, borderwidth=0, padx=0, pady=0, bg="#162334", activebackground="#162334", command=show_info_settings)
        backb = tk.Button(optionc, image=self.back_image2, borderwidth=0, padx=0, pady=0, bg="#162334", activebackground="#162334", command=back)
        settings_frame = tk.Frame(optionc, bg="#4E7896")

    def registerpage(self):
        def back():
            register_frame.pack_forget()
            self.home()
        self.canvas.pack_forget()

        register_frame = tk.Canvas(self.window, bg="#162334", highlightthickness=0)
        bg_image_item = register_frame.create_image(0, 0, anchor=tk.NW, image=self.canvas.bg_image)
        register_frame.place(relwidth=1, relheight=1)

        def on_enter(e):
            username_entry.delete(0, 'end')

        def on_leave():
            name = username_entry.get()
            if name == '':
                username_entry.insert(0, 'Enter Username')

        username_entry = tk.Entry(register_frame, width=25, fg="#162334", border=2, bg="#4E7896",
                                font=("Bebas Neue", 18, 'bold'), relief=tk.SOLID, bd=1,
                                highlightthickness=1, highlightbackground="#4E7896")
        username_entry.insert(0, 'Username')
        username_entry.bind("<FocusIn>", on_enter)
        username_entry.bind("<FocusOut>", on_leave)

        def on_enter(e):
            password_entry.delete(0, 'end')

        def on_leave():
            name = password_entry.get()
            if name == '':
                password_entry.insert(0, 'Enter Password')

        password_entry = tk.Entry(register_frame, width=25, fg="#162334", border=2, bg="#4E7896",
                                font=("Bebas Neue", 18, 'bold'), relief=tk.SOLID, bd=1,
                                highlightthickness=1, highlightbackground="#4E7896")
        password_entry.insert(0, 'Password')
        password_entry.bind("<FocusIn>", on_enter)
        password_entry.bind("<FocusOut>", on_leave)
        password_entry.config(show="*")

        back_button = Button(register_frame, image=self.back_image2, bg="#162334", bd=0, activebackground="#162334", command=back)
        back_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        def register():
            username = username_entry.get()
            password = password_entry.get()

            select_query = "SELECT * FROM `users` WHERE `username` = %s"
            values = (username,)
            self.c.execute(select_query, values)
            result = self.c.fetchone()

            if result:
                messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")
            else:
                insert_query = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"
                insert_values = (username, password)
                self.c.execute(insert_query, insert_values)
                self.connection.commit()

                messagebox.showinfo("Registration Successful", "You have successfully registered!")
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')

        username_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        register_button = tk.Button(register_frame, image=self.signup_image, borderwidth=0, padx=0, pady=0,
                                    bg="#162334", activebackground="#162334", command=register)
        register_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def exit(self):
        self.window.destroy()




if __name__ == "__main__":
    shared_data = type('', (), {})()
    shared_data.logged_in = False
    shared_data.username = ""
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()
