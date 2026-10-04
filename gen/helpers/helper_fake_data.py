"""
TO USE / IMPLEMENTS: 

if __name__ == '__main__':
    fake = HelperFakeData()
    generate_postman_file(
        base_ruta=fake.project,
        singular_name=fake.singular_name,
        plural_name=fake.plural_name,
        singular_name_kebab=fake.singular_name_kebab,
        plural_name_kebab=fake.plural_name_kebab,
        columns=fake.get_data(),
    )
"""

class HelperFakeData():
    
    def __init__(self):
       
        
        self.project = "/Users/dorian/PHPProjects/api.app1.com"
        self.namespace = "API"
        self.version_api = "V1"
        self.folder_group = ""

        self.singular_name = "AgendaUnloading"
        self.plural_name = "AgendaUnloadings"

        self.singular_name_kebab = "agenda-unloading"
        self.plural_name_kebab = "agenda-unloadings"

        self.singular_name_snake = "agenda_unloading"
        self.plural_name_snake = "agenda_unloadings"
        
        self.data = []
        self.start()
        
    
    def get_data(self):
        return self.data



    def start(self):
        
        self.set_data(
            is_fk=True,
            is_index=False,
            is_nullable=False,
            is_unique=False,
            is_unsigned=False,
            name="user_id",
            options=["fk"],
            precision=None,
            raw_type="fk",
            related_model="User",
            related_table="users",
            relationship_column="user_id",
            relationship_name="user",
            scale=None,
            size=None,
            type="fk",
        )
        
        self.set_data(
            is_fk=True,
            is_index=False,
            is_nullable=False,
            is_unique=False,
            is_unsigned=False,
            name="ablity_group_id",
            options=["fk"],
            precision=None,
            raw_type="fk",
            related_model="AblityGroup",
            related_table="ablity_groups",
            relationship_column="ablity_group_id",
            relationship_name="ablity_group",
            scale=None,
            size=None,
            type="fk",
        )

        self.set_data(
            is_fk=False,
            is_index=False,
            is_nullable=False,
            is_unique=True,
            is_unsigned=False,
            name="name",
            options=["string(30)", "unique"],
            precision=None,
            raw_type="string(30)",
            related_model=None,
            related_table=None,
            relationship_column=None,
            relationship_name=None,
            scale=None,
            size=30,
            type="string",
        )

        self.set_data(
            is_fk=False,
            is_index=False,
            is_nullable=False,
            is_unique=False,
            is_unsigned=False,
            name="amount",
            options=["decimal(10,2)"],
            precision=10,
            raw_type="decimal(10,2)",
            related_model=None,
            related_table=None,
            relationship_column=None,
            relationship_name=None,
            scale=2,
            size=None,
            type="decimal",
        )

        self.set_data(
            is_fk=False,
            is_index=False,
            is_nullable=False,
            is_unique=False,
            is_unsigned=False,
            name="amount_with_tax",
            options=["float"],
            precision=None,
            raw_type="float",
            related_model=None,
            related_table=None,
            relationship_column=None,
            relationship_name=None,
            scale=None,
            size=None,
            type="float",
        )

        self.set_data(
            is_fk=False,
            is_index=False,
            is_nullable=False,
            is_unique=False,
            is_unsigned=False,
            name="description",
            options=["varchar(10)"],
            precision=None,
            raw_type="varchar(10)",
            related_model=None,
            related_table=None,
            relationship_column=None,
            relationship_name=None,
            scale=None,
            size=10,
            type="string",
        )

        self.set_data(
            is_fk=False,
            is_index=False,
            is_nullable=False,
            is_unique=False,
            is_unsigned=False,
            name="note",
            options=["string"],
            precision=None,
            raw_type="string",
            related_model=None,
            related_table=None,
            relationship_column=None,
            relationship_name=None,
            scale=None,
            size=255,
            type="string",
        )

        self.set_data(
            is_fk=False,
            is_index=False,
            is_nullable=False,
            is_unique=False,
            is_unsigned=False,
            name="has_active",
            options=["boolean"],
            precision=None,
            raw_type="boolean",
            related_model=None,
            related_table=None,
            relationship_column=None,
            relationship_name=None,
            scale=None,
            size=None,
            type="boolean",
        )







    
    def set_data(
        self, 
        is_fk,
        is_index,
        is_nullable,
        is_unique,
        is_unsigned,
        name,
        options,
        precision,
        raw_type,
        related_model,
        related_table,
        relationship_column,
        relationship_name,
        scale,
        size,
        type
    ):
        
        obj = {}
        obj['is_fk'] = is_fk
        obj['is_index'] = is_index
        obj['is_nullable'] = is_nullable
        obj['is_unique'] = is_unique
        obj['is_unsigned'] = is_unsigned
        obj['name'] = name
        obj['options'] = options
        obj['precision'] = precision
        obj['raw_type'] = raw_type
        obj['related_model'] = related_model
        obj['related_table'] = related_table
        obj['relationship_column'] = relationship_column
        obj['relationship_name'] = relationship_name
        obj['scale'] = scale
        obj['size'] = size
        obj['type'] = type
        
        self.data.append(obj)


    