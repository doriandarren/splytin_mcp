import os
from gen.helpers.helper_file import HelperFile


class DjGenerateCoreModels:
    
    
    def invoke(self, full_path):
        self.create_file_init(full_path)
        self.create_file_models(full_path)



    def create_file_init(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "core", "models")

        content = ""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="__init__.py",
            content=content
        )
        
        
        
        
    def create_file_models(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "core", "models")

        content = r'''from django.db import models
from django.conf import settings
from django.utils import timezone


# QuerySet personalizado para eliminaciones lógicas y físicas
class SoftDeleteQuerySet(models.QuerySet):

    def delete(self):
        now = timezone.now()

        count = self.update(
            deleted_at=now,
            updated_at=now
        )

        return count, {
            self.model._meta.label: count
        }

    def hard_delete(self):
        return super().delete()


# Manager: solo registros activos
class ActiveManager(models.Manager.from_queryset(SoftDeleteQuerySet)):

    def get_queryset(self):
        return super().get_queryset().filter(
            deleted_at__isnull=True
        )


# Manager: todos los registros, incluidos los eliminados
class AllObjectsManager(models.Manager.from_queryset(SoftDeleteQuerySet)):
    pass


# Modelo base abstracto
class BaseModel(models.Model):

    # Fechas de auditoría
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Usuarios de auditoría
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created"
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated"
    )

    # Managers
    objects = ActiveManager()
    all_objects = AllObjectsManager()

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    # Eliminación lógica
    def soft_delete(self, user=None):
        self.deleted_at = timezone.now()

        if user is not None:
            self.updated_by = user

        self.save(update_fields=[
            "deleted_at",
            "updated_by",
            "updated_at"
        ])

    # Restaurar registro eliminado
    def restore(self, user=None):
        self.deleted_at = None

        if user is not None:
            self.updated_by = user

        self.save(update_fields=[
            "deleted_at",
            "updated_by",
            "updated_at"
        ])

    # Sobrescribir eliminación normal
    def delete(self, using=None, keep_parents=False):
        self.soft_delete()
        return 1, {self._meta.label: 1}

    # Eliminación física
    def hard_delete(self, using=None, keep_parents=False):
        return super().delete(
            using=using,
            keep_parents=keep_parents
        )
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="models.py",
            content=content
        )