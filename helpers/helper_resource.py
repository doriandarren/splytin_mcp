from pathlib import Path


class HelperResource:
    """
    Helper genérico para localizar y acceder a recursos compartidos
    (imágenes, fuentes, plantillas, etc.) desde cualquier generador.
    """

    # Ruta absoluta a la carpeta resources del proyecto
    BASE_PATH = Path(__file__).resolve().parents[1] / "resources"


    @classmethod
    def image(cls, filename):
        """
        Devuelve la ruta absoluta de una imagen dentro de resources/images.
        """
        return cls.BASE_PATH / "images" / filename