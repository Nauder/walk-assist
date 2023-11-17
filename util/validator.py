def verify_keys(data: dict[str, str], keys: tuple) -> bool:
    return all(k in data for k in keys) and all(v != "" for v in [data[k] for k in keys])


def validate_usuario(usuario: dict[str, str]) -> bool:
    return verify_keys(usuario, ('nome', 'registro', 'email', 'senha', 'tipo_usuario'))


def validate_put_usuario(usuario: dict[str, str]) -> bool:
    return verify_keys(usuario, ('nome', 'email', 'senha'))


def validate_login(login: dict[str, str]) -> bool:
    return verify_keys(login, ('registro', 'senha'))


def validate_ponto(ponto: dict[str, str]) -> bool:
    return verify_keys(ponto, ('nome',))


def validate_segmento(segmento: dict[str, str]) -> bool:
    return verify_keys(segmento, ('ponto_inicial', 'ponto_final', 'status', 'distancia', 'direcao'))
