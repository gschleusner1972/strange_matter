import tkinter as tk
import json
import os
from tkinter import filedialog

class SchemaCreator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.config(bg="dark blue")

        self.schema_name_label = tk.Label(self, text="Schema Name", bg="dark blue", fg="pink")
        self.schema_name_label.pack(pady=10)

        self.schema_name = tk.Entry(self)
        self.schema_name.pack(pady=5)

        # Add primary class dropdown
        self.primary_class_label = tk.Label(self, text="Primary Class", bg="dark blue", fg="pink")
        self.primary_class_label.pack(pady=10)

        self.primary_class = tk.StringVar()
        self.primary_class.set("Component")
        self.primary_class_combobox = tk.OptionMenu(self, self.primary_class, "Component", "Relationship")
        self.primary_class_combobox.config(bg="dark blue", fg="pink")
        self.primary_class_combobox["menu"].config(bg="dark blue", fg="pink")
        self.primary_class_combobox.pack(pady=5)

        self.schema_data_label = tk.Label(self, text="Data Format", bg="dark blue", fg="pink")
        self.schema_data_label.pack(pady=10)

        self.schema_data = tk.Entry(self)
        self.schema_data.pack(pady=5)

        self.schema_folder_label = tk.Label(self, text="Schema Folder", bg="dark blue", fg="pink")
        self.schema_folder_label.pack(pady=10)

        self.schema_folder = tk.Entry(self)
        self.schema_folder.pack(pady=5)

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_folder, bg="dark blue", fg="pink")
        self.browse_button.pack(pady=10)

        self.enums_data_label = tk.Label(self, text="Enums", bg="dark blue", fg="pink")
        self.enums_data_label.pack(pady=10)

        self.enums_data = tk.Entry(self)
        self.enums_data.pack(pady=5)

        self.fields = []
        for i in range(0, 10):
            field = tk.Frame(self, bg="dark blue")
            field.pack(pady=5)

            field_name_label = tk.Label(field, text="Field Name", bg="dark blue", fg="pink")
            field_name_label.pack(side="left", padx=5)

            field_name = tk.Entry(field)
            field_name.pack(side="left", padx=5)

            field_type_label = tk.Label(field, text="Field Type", bg="dark blue", fg="pink")
            field_type_label.pack(side="left", padx=5)

            field_type = tk.StringVar()
            field_type.set("string")
            field_type_combobox = tk.OptionMenu(field, field_type, "string", "integer", "float", "boolean", "array")
            field_type_combobox.config(bg="dark blue", fg="pink")
            field_type_combobox["menu"].config(bg="dark blue", fg="pink")
            field_type_combobox.pack(side="left", padx=5)

            self.fields.append((field_name, field_type))

        self.array_type_label = tk.Label(self, text="Array Type", bg="dark blue", fg="pink")
        self.array_type_label.pack(pady=10)

        self.array_type = tk.StringVar()
        self.array_type.set("string")
        self.array_type_combobox = tk.OptionMenu(self, self.array_type, "string", "integer", "float", "boolean")
        self.array_type_combobox.config(bg="dark blue", fg="pink")
        self.array_type_combobox["menu"].config(bg="dark blue", fg="pink")
        self.array_type_combobox.pack(pady=5)

        self.array_values_label = tk.Label(self, text="Array Values", bg="dark blue", fg="pink")
        self.array_values_label.pack(pady=10)

        self.array_values = tk.Text(self, height=5)
        self.array_values.pack(pady=5)

        self.create_button = tk.Button(self, text="Create", command=self.create_schema, bg="dark blue", fg="pink")
        self.create_button.pack(pady=20)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.schema_folder.delete(0, tk.END)
        self.schema_folder.insert(0, folder_path)

    def create_schema(self):
        schema_name = self.schema_name.get()
        schema_folder = self.schema_folder.get()
        schema_data = self.schema_data.get()
        myenum_data = self.enums_data.get()

        with open(os.path.join(schema_folder, schema_name + ".json"), "w") as f:
            valid_fields = []
            for field_name, field_type in self.fields:
                if field_name.get():
                    if field_type.get() == "array":
                        valid_fields.append({
                                "name": field_name.get(),
                                "type": "array",
                                "items": {
                                    "type": self.array_type.get(),
                            }
                        })

                    if field_name.get() == "compound":
                        valid_fields.append({  
                                "dimensions": {
                                    "type": "object",
                                    "properties": {
                                        "length": {
                                        "type": "number"
                                        },
                                        "width": {
                                        "type": "number"
                                        },
                                        "height": {
                                        "type": "number"
                                        }
                                    },
                                    }
                        })
      
                    else:
                        valid_fields.append({
                            "name": field_name.get(),
                            "type": field_type.get()
                        })


            json.dump({
                "$schema":"http://json-schema.org/schema#",
                "title": schema_name,
                "data_format": schema_data,
                "primary_class": self.primary_class.get(),
                "schema_version": "00",
                "type": "object",
                "properties": valid_fields
            }, f, indent=4)

        print("Schema created successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="dark blue")
    schema_creator = SchemaCreator(root)
    schema_creator.pack(padx=20, pady=20)
    root.mainloop()

