import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules import data_manager
from werkzeug.security import generate_password_hash

def seed_users():
    # Users from Organogram
    users_to_seed = [
        # Presidência / Conselho (Global Access)
        {"username": "presidente", "password": "admin123", "role": "presidente"},
        {"username": "conselho", "password": "admin123", "role": "conselho"},
        
        # Diretoria Operacional (Produção + Estoque)
        {"username": "dir_operacional", "password": "123456", "role": "diretor_operacional"},
        {"username": "ger_montagem", "password": "123456", "role": "gerente_montagem"},
        {"username": "func_producao", "password": "123456", "role": "func_producao"},
        
        # Gerencia Insumos / Estoque
        {"username": "ger_insumos", "password": "123456", "role": "gerente_insumos"},
        {"username": "func_estoque", "password": "123456", "role": "func_estoque"},
        
        # Diretoria Financeira
        {"username": "dir_financeira", "password": "123456", "role": "diretor_financeiro"},
        {"username": "ger_financeira", "password": "123456", "role": "gerente_financeiro"},
        {"username": "func_financeiro", "password": "123456", "role": "func_financeiro"},
        
        # Diretoria RH
        {"username": "dir_rh", "password": "123456", "role": "diretor_rh"},
        {"username": "ger_rh", "password": "123456", "role": "gerente_rh"},
        {"username": "func_rh", "password": "123456", "role": "func_rh"},
        
        # Admin
        {"username": "admin", "password": "admin123", "role": "admin"}
    ]
    
    print("--- Seeding Users to JSON ---")
    
    current_users = data_manager.load_data('users.json')
    
    for u in users_to_seed:
        # Check if exists
        if any(existing['username'] == u['username'] for existing in current_users):
            print(f"[SKIP] User already exists: {u['username']}")
            continue
            
        hashed_pw = generate_password_hash(u['password'])
        new_user = {
            "username": u['username'],
            "password": hashed_pw,
            "role": u['role']
        }
        current_users.append(new_user)
        print(f"[OK] Created user: {u['username']} ({u['role']})")
            
    data_manager.save_data('users.json', current_users)
    print("--- Seeding Complete ---")

if __name__ == "__main__":
    seed_users()
