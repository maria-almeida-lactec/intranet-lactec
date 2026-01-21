from lactec.intranet import logger

import os


def log_event(event: object):
    """Escreve no log todos os eventos disparados pelo processo do backend.

    Apenas funciona se a variável de ambiente DEBUG estiver definida.
    exemplo: DEBUG=1 make backend-start
    """
    if not os.environ.get("DEBUG"):
        return

    module_name = event.__class__.__module__
    class_name = event.__class__.__name__
    dotted_name = f"{module_name}.{class_name}"
    logger.info(f"- Evento disparado: {dotted_name} ({event})")
