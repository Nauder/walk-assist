def validate_usuario(usuario: dict[str, str]) -> bool:
    return all(k in usuario for k in ('nome', 'registro', 'email', 'senha', 'tipo_usuario'))
