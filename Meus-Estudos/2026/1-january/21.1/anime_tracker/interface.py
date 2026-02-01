import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import logica

class AnimeTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎌 Anime Tracker")
        self.root.geometry("900x700")
        self.root.configure(bg='#1a1a2e')

        #estilo moderno
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Title.TLabel', font=('Arial', 18, 'bold'), foreground='#00d4ff')
        style.configure('Anime.TButton', font=('Arial', 10, 'bold'), padding=10)

        self.animes = logica.carregar_animes()

        self.criar_interface()

    
    def criar_interface(self):

        # Frame principal
        main_frame = tk.Frame(self.root, bg='#1a1a2e')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Botões (Esquerda (30%))
        left_frame = tk.Frame(main_frame, bg='#16213e', width=250)
        left_frame.pack(side='left', fill='y', padx=(0,10))
        left_frame.pack_propagate(False) #fixa largura 250px

        # Título
        titulo = tk.Label(left_frame, text="🎌 ANIME TRACKER", font=('Arial', 20, 'bold'), fg='#00d4ff', bg='#16213e')
        titulo.pack(pady=(20, 30))

        botoes = [
            ("📊 Listar Animes", self.listar_animes),
            ("➕ Novo Anime", self.adicionar_anime),
            ("❌ Excluir Anime", self.excluir_animes),
            ("💔 Dropado", self.add_dropado),
            ("⏳ Planejar", self.add_planejado),
            ("📈 Estatísticas", self.mostrar_stats),
            ("💾 Salvar", self.salvar_animes)
        ]

        for texto, comando in botoes:
            btn = tk.Button(left_frame, text=texto, command=comando, bg='#0f3460', fg='white', font=('Arial', 10, 'bold'), relief='flat', bd=0, padx=15, pady=8, cursor='hand2', height=2, activebackground='#00d4ff')
            btn.pack(pady=3, padx=10, fill='x')
        
        # Área de texto (lista + stats)
        # === direita: output (70%)
        
        right_frame = tk.Frame(main_frame, bg='#16213e')
        right_frame.pack(side='right', fill='both', expand=True, padx=(10,0))
        
        # Título output

        output_title = tk.Label(right_frame, text="📋 OUTPUT", font=('Arial', 14, 'bold'), fg='#00d4ff', bg='#16213e')
        output_title.pack(pady=(20,10))

        self.text_area = scrolledtext.ScrolledText(right_frame, height=30, width=70, bg='#0f0f23', fg='#e0e0e0', font=('Consolas', 11), insertbackground='white')
        self.text_area.pack(fill='both', expand=True, pady=(0,20))

        # Status bar

        self.status_var = tk.StringVar()
        self.status_var.set("🔥 Pronto! Clique em Listar Animes")
        status_bar = tk.Label(right_frame, textvariable=self.status_var, bg='#16213e', fg='#00d4ff', font=('Arial', 10), relief='sunken', anchor='w')
        status_bar.pack(fill='x', side='bottom')


    def atualizar_status(self, msg):
        self.status_var.set(msg)
        self.root.update()
    

    def limpar_area(self):
        self.text_area.delete(1.0, tk.END)
    

    def listar_animes(self):
        self.limpar_area()
        self.text_area.insert(tk.END, "📋 SEUS ANIMES:\n")
        self.text_area.insert(tk.END, "="*80+"\n")

        # captura saída do print e coloca na GUI
        import sys
        import io

        old_stdout = sys.stdout
        output_buffer = io.StringIO()

        sys.stdout = output_buffer
        logica.listar_animes()
        sys_stdout = old_stdout

        # pega o texto capturado e coloca na GUI
        texto_capturado = output_buffer.getvalue()
        self.text_area.insert(tk.END, texto_capturado)
        self.text_area.see(tk.END) # Auto-scroll
        self.atualizar_status("✅ Animes listados!")
    

    def adicionar_anime(self):
        janela = tk.Toplevel(self.root)
        janela.title("➕ Novo Anime")
        janela.geometry("400x300")
        janela.configure(bg='#1a1a2e')
        janela.transient(self.root)
        janela.grab_set()

        tk.Label(janela, text="Novo Anime", font=('Arial', 16, 'bold'), fg='#00d4ff', bg='#1a1a2e').pack(pady=20)
        tk.Label(janela, text="Nome:", fg='white', bg='#1a1a2e').pack()
        nome_entry = tk.Entry(janela, font=('Arial', 12), width=30)
        nome_entry.pack(pady=5)

        tk.Label(janela, text="Nota (0-10):", fg='white', bg='#1a1a2e').pack(pady=5)
        nota_entry = tk.Entry(janela, font=('Arial', 12), width=30)
        nota_entry.pack(pady=5)

        tk.Label(janela, text="Status:", fg='white', bg='#1a1a2e').pack()
        status_var = tk.StringVar(value="completo")
        status_combo = ttk.Combobox(janela, textvariable=status_var, values=["assistindo", "completo", "planejado", "dropado"])
        status_combo.pack(pady=5)


        def salvar_novo():
            try:
                logica.adicionar_anime(nome_entry.get(), float(nota_entry.get()), status_var.get())
                messagebox.showinfo("Sucesso", "Anime adicionado! 🎉")
                janela.destroy()
                self.atualizar_status("➕ Anime adicionado!")
            except ValueError:
                messagebox.showerror("Erro", "Nota deve ser número!")
        tk.Button(janela, text="Adicionar", command=salvar_novo, bg='#00d4ff', fg='black', font=('Arial', 12, 'bold')).pack(pady=20)


    def mostrar_stats(self):
        self.limpar_area()

        import sys
        import io

        old_stdout = sys.stdout
        output_buffer = io.StringIO()

        sys_stdout = output_buffer
        logica.mostrar_estatisticas()           
        sys_stdout = old_stdout

        texto_capturado = output_buffer.getvalue()
        self.text_area.insert(tk.END, texto_capturado)
        self.text_area.see(tk.END)
        self.atualizar_status("📈 Estatísticas atualizadas!")

    
    def salvar_animes(self):
        logica.salvar_lista(logica.carregar_animes())
        self.atualizar_status("💾 Salvo com sucesso!")
    
    
    def excluir_animes(self):
        janela = tk.Toplevel(self.root)
        janela.title("❌ Excluir Anime")
        janela.geometry("700x500")
        janela.configure(bg='#1a1a2e')
        janela.transient(self.root)
        janela.grab_set()

        #lista atual
        tk.Label(janela, text='Selecione anime para excluir:', font=('Arial', 14, ' bold'), fg='#ff6b6b', bg='#1a1a2e').pack(pady=10)

        lista_frame = tk.Frame(janela,bg='#1a1a2e')
        lista_frame.pack(pady=10, padx=20, fill='both', expand=True)

        self.animes = logica.carregar_animes()
        self.listbox = tk.Listbox(lista_frame, height=12, font=('Consolas', 11), bg='#0f0f23', fg='#e0e0e0', selectbackground='#ff4757')
        scrollbar = tk.Scrollbar(lista_frame, orient='vertical')
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.listbox.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Preenche lista
        for i, anime in enumerate(self.animes, 1):
            nome = anime["nome"][:40] + "..." if len(anime["nome"]) > 40 else anime["nome"]
            self.listbox.insert(tk.END, f'{i:2}. {nome:<35} | {anime["nota"]:<4} | {anime["status"]}')


        def confirmar_exclusao():
            selecao = self.listbox.curselection()
            if not selecao:
                messagebox.showwarning("Atenção", "Selecione um anime!")
                return
            
            idx = selecao[0]
            anime_excluido = self.animes[idx]

            if messagebox.askyesno("Confirmar", f"Excluir '{anime_excluido['nome']}'\nNota:{anime_excluido['nota']} | Status: {anime_excluido['status']}?"):
                logica.excluir_anime(idx)
                messagebox.showinfo("Sucesso", f"❌ '{anime_excluido['nome']}' excluído!")
                janela.destroy()
                self.atualizar_status(f"🗑️ Excluído: {anime_excluido['nome']}")
            tk.Button(janela, text="🗑️ EXCLUIR SELECIONADO", command=confirmar_exclusao, bg='#ff4757', fg='white', font=('Arial', 12, 'bold'), relief='flat', pady=10).pack(pady=20)


    def add_dropado(self):
        #interface para marcar como dropado.
        janela = tk.Toplevel(self.root)
        janela.title("💔 Anime Dropado")
        janela.geometry("450x350")
        janela.configure(bg='#1a1a2e')
        janela.transient(self.root)
        janela.grab_set()

        tk.Label(janela, text="💔 Marcar como DROPPED", font=("Arial", 16, 'bold'), fg='#ff6b6b', bg='#1a1a2e').pack(pady=20)

        tk.Label(janela, text="Nome do anime:", fg='white', bg='#1a1a2e').pack(pady=(0,5))
        nome_entry = tk.Entry(janela, font=('Arial', 12), width=35)
        nome_entry.pack(pady=5)
        nome_entry.focus() #cursor já no campo

        tk.Label(janela, text="Nota (0-10):", fg='white', bg='#1a1a2e').pack(pady=(10,5))
        nota_entry = tk.Entry(janela, font=('Arial', 12), width=35)
        nota_entry.pack(pady=5)


        def salvar_dropado():
            try:
                nome = nome_entry.get().strip()
                if not nome:
                    messagebox.showerror("Erro", "Nome é obrigatório!")
                    return
                nota = float(nota_entry.get() or 0)
                
                logica.add_dropado(nome, nota)
                messagebox.showinfo("Dropado", f"💔 '{nome}' marcado como dropado!\n")
                janela.destroy()
                self.atualizar_status(f"💔 Dropado: {nome}")
            except ValueError:
                messagebox.showerror("Erro", "Nota deve ser um número")
            tk.Button(janela, text="💔 CONFIRMAR DROP", command=salvar_dropado, bg='#ff4757', fg='white', font=('Arial', 12, 'bold'), relief='flat', pady=12, padx=30).pack(pady=25)
    
    
    def add_planejado(self):
        #interface para planejar anime
        janela = tk.Toplevel(self.root)
        janela.title("⏳ Planejar Anime")
        janela.geometry("450x350")
        janela.configure(bg='#1a1a2e')
        janela.transient(self.root)
        janela.grab_set()

        tk.Label(janela, text="⏳ Adicionar aos PLANEJADOS", font=('Arial', 16, 'bold'), fg='#ffa726', bg='#1a1a2e').pack(pady=20)

        tk.Label(janela, text="Nome do anime:", fg='white', bg='#1a1a2e').pack(pady=(0,5))
        nome_entry = tk.Entry(janela, font=('Arial', 12), width=35)
        nome_entry.pack(pady=5)
        nome_entry.focus() #cursor já no campo

        tk.Label(janela, text="Nota esperada (0-10):", fg='white', bg='#1a1a2e').pack(pady=(10,5))
        nota_entry = tk.Entry(janela, font=('Arial', 12), width=35)
        nota_entry.pack(pady=5)
        nota_entry.insert(0, "9.0") # nota padrão pra planejados

        def salvar_planejado():
            try:
                nome = nome_entry.get().strip()
                if not nome:
                    messagebox.showerror("Erro", "Nome é obrigatório!")
                    return
                nota = float(nota_entry.get() or 9.0)

                # Chama logica com status fixo "planejado"
                logica.adicionar_anime(nome, nota, "planejado")
                messagebox.showinfo("Planejado", f"⏳ '{nome}' adicionado aos planejados!")
                janela.destroy()
                self.atualizar_status(f"⏳ Planejado: {nome}")
            except ValueError:
                messagebox.showerror("Erro","Nota deve ser um número!")
        tk.Button(janela, text="⏳ ADICIONAR AOS PLANEJADOS", command=salvar_planejado, bg='#ffa726', fg='black', font=('Arial', 12, 'bold'), relief='flat', pady=12, padx=20).pack(pady=25)


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimeTrackerGUI(root)
    root.mainloop()