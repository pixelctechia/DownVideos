import os
import subprocess
import sys

def menu():
    print("="*40)
    print("      DownVideos - SELETOR DE INTERFACE")
    print("="*40)
    print("[1] Abrir Interface de Desktop (Tkinter)")
    print("[2] Abrir Interface Web Moderna (Streamlit)")
    print("[0] Sair")
    print("-"*40)

    escolha = input("Escolha o número da opção desejada: ")

    if escolha == '1':
        print("\nIniciando Tkinter...")
        # Executa o app.py original (que agora vamos renomear ou manter como padrão)
        subprocess.run([sys.executable, "app.py"])
    
    elif escolha == '2':
        print("\nVerificando se o Streamlit está instalado...")
        try:
            import streamlit
            print("Iniciando Streamlit no seu navegador...")
            subprocess.run(["streamlit", "run", "app_web.py"])
        except ImportError:
            print("\n[ERRO] Streamlit não encontrado!")
            print("Por favor, instale com: pip install streamlit")
    
    elif escolha == '0':
        print("Saindo...")
        sys.exit()
    
    else:
        print("Opção inválida!")
        menu()

if __name__ == "__main__":
    menu()
