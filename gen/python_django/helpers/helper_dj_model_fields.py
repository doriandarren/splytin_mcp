class HelperDjModelFields:

    @staticmethod
    def map_column_type(column, plural_name_snake):
        """
        Convierte el tipo de columna en un campo Django.
        """

        column_type = column.get("type")
        field_name = column["name"]

        if column.get("is_fk"):
            related_table = column.get("related_table", "")
            related_model = column.get("related_model", "")
            field_name = column.get("relationship_name") or field_name.removesuffix("_id")

            return field_name, f'''models.ForeignKey(
        "{related_table}.{related_model}",
        on_delete=models.CASCADE,
        related_name="{plural_name_snake}"
    )'''

        if column_type == "string":
            size = column.get("size") or 255
            return field_name, f"models.CharField(max_length={size})"

        elif column_type == "integer":
            return field_name, "models.IntegerField()"

        elif column_type == "text":
            return field_name, "models.TextField()"

        elif column_type == "boolean":
            return field_name, "models.BooleanField(default=False)"

        elif column_type == "float":
            return field_name, "models.FloatField()"

        elif column_type == "decimal":
            precision = column.get("precision") or 10
            scale = column.get("scale")
            if scale is None:
                scale = 2

            return field_name, (
                f"models.DecimalField(max_digits={precision}, "
                f"decimal_places={scale})"
            )

        elif column_type == "date":
            return field_name, "models.DateField()"

        elif column_type == "datetime":
            return field_name, "models.DateTimeField()"

        return field_name, "models.CharField(max_length=255)"
