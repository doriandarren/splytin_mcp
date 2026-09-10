import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_trait_tracks_users(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Traits")
    file_path = os.path.join(folder_path, "TracksUsers.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""<?php

namespace App\Traits;

use App\Models\User;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

trait TracksUsers
{
    protected static function bootTracksUsers(): void
    {
        static::creating(function ($model) {
            if (auth()->check()) {
                $model->created_by = auth()->id();
                $model->updated_by = auth()->id();
            }
        });

        static::updating(function ($model) {
            if (auth()->check()) {
                $model->updated_by = auth()->id();
            }
        });

        static::deleting(function ($model) {
            if (
                auth()->check() &&
                method_exists($model, 'isForceDeleting') &&
                ! $model->isForceDeleting()
            ) {
                $model->deleted_by = auth()->id();
                $model->saveQuietly();
            }
        });
    }

    public function createdBy(): BelongsTo
    {
        return $this->belongsTo(User::class, 'created_by');
    }

    public function updatedBy(): BelongsTo
    {
        return $this->belongsTo(User::class, 'updated_by');
    }

    public function deletedBy(): BelongsTo
    {
        return $this->belongsTo(User::class, 'deleted_by');
    }
}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
