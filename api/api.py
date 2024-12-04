
from ninja import NinjaAPI
from .supabase_client import supabase

api = NinjaAPI()

# Rota para listar usuários
@api.get("/users")
def list_users(request):
    response = supabase.table("users").select("*").execute()
    return {"users": response.data}

# Rota para criar um usuário
@api.post("/users")
def create_user(request, name: str, email: str):
    response = supabase.table("users").insert({"name": name, "email": email}).execute()
    return {"message": "User created", "user": response.data}
