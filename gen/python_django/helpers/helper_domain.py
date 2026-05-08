


def helper_domain_name(value):
    """
    Devuelve el dominio de un URL
    Ex. api.splytin.com -> splytin.com
    """
    
    parts = value.lower().split(".")
    
    if len(parts) < 2:
        return value.lower()
    
    return ".".join(parts[-2:])