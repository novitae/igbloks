from pydantic import BaseModel, Field
from collections import deque
from typing import Dict, Any

def create_dataclasses(data: Dict[str, Dict[str, Any]]):
    created_dataclasses = set()
    queue = deque(data.keys())

    while queue:
        name = queue.popleft()
        fields = data[name]

        # Vérifie si toutes les dépendances sont créées
        dependencies_created = True
        for field_info in fields.values():
            if field_info["types"][0] == "dict":
                referenced_dataclass = field_info["values"][0]
                if referenced_dataclass not in created_dataclasses:
                    dependencies_created = False
                    break

        # Si toutes les dépendances sont créées, créez la dataclass
        if dependencies_created:
            print(f"""class {name.replace(".", "_").replace('|', '__or__')}(BaseModel):""")

            for field, field_info in fields.items():
                readable_field, compressed_field = field.split("|")
                field_type = field_info["types"][0]
                if field_type == "dict":
                    field_type = field_info["values"][0].replace(".", "_").replace('|', '__or__') + "__container"

                compressed_field_repr = repr(compressed_field)[1:-1]  # Utilisez repr() et retirez les guillemets
                readable_field = readable_field.replace(".", "").replace("|", "")
                print(f"    {readable_field}: {field_type} = Field(None, alias='{compressed_field_repr}')")

            container_class_name = name.replace(".", "_").replace('|', '__or__') + "__container"
            container_name, container_alias = name.replace(".", "").split("|")
            print(f"""\nclass {container_class_name}(BaseModel):""")
            print(f"    {container_name}: {name.replace('.', '_').replace('|', '__or__')} = Field(None, alias='{container_alias}')\n")

            created_dataclasses.add(name)
            print()
        else:
            # Remet l'objet en attente pour un traitement ultérieur
            queue.append(name)

import json
# Charge les données structurées précédemment sauvegardées
with open("bloks_structure.json", "r") as f:
    bloks_data = json.load(f)

# Génère le code des dataclasses
create_dataclasses(bloks_data)
