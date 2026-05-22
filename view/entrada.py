


_impl = None


def _registrar(impl):
    global _impl
    _impl = impl


def _limpiar():
    global _impl
    _impl = None


def pedir_varios(campos, contexto=None):
    if _impl is None:
        raise RuntimeError(
            
        )
    return _impl(campos, contexto)
