import tkinter as tk
import json
import os


class SchemaCreator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.schema_name_label = tk.Label(self, text="Schema Name")
        self.schema_name_label.pack()

        self.schema_name = tk.Entry(self)
        self.schema_name.pack()

        self.schema_data = tk.Label(self, text="Data Format")
        self.schema_data.pack()

        self.schema_data = tk.Entry(self)
        self.schema_data.pack()

        self.schema_folder_label = tk.Label(self, text="Schema Folder")
        self.schema_folder_label.pack()

        self.schema_folder = tk.Entry(self)
        self.schema_folder.pack()

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_folder)
        self.browse_button.pack()

        self.fields = []
        for i in range(0, 10):
            field = tk.Frame(self)
            field.pack()

            field_name_label = tk.Label(field, text="Field Name")
            field_name_label.pack(side="left")

            field_name = tk.Entry(field)
            field_name.pack(side="left")

            field_type_label = tk.Label(field, text="Field Type")
            field_type_label.pack(side="left")

            field_type = tk.StringVar()
            field_type.set("string")
            field_type_combobox = tk.OptionMenu(field, field_type, "string", "integer", "float", "boolean", "array")
            field_type_combobox.pack(side="left")

            self.fields.append((field_name, field_type))

        self.array_type_label = tk.Label(self, text="Array Type")
        self.array_type_label.pack()

        self.array_type = tk.StringVar()
        self.array_type.set("string")
        self.array_type_combobox = tk.OptionMenu(self, self.array_type, "string", "integer", "float", "boolean")
        self.array_type_combobox.pack()

        self.array_values_label = tk.Label(self, text="Array Values")
        self.array_values_label.pack()

        self.array_values = tk.Text(self, height=5)
        self.array_values.pack()

        self.create_button = tk.Button(self, text="Create", command=self.create_schema)
        self.create_button.pack()

    def browse_folder(self):
        folder_path = tk.filedialog.askdirectory()
        self.schema_folder.delete(0, tk.END)
        self.schema_folder.insert(0, folder_path)

    def create_schema(self):
        schema_name = self.schema_name.get()
        schema_folder = self.schema_folder.get()
        schema_data = self.schema_data.get()

        with open(os.path.join(schema_folder, schema_name + ".json"), "w") as f:
            valid_fields = []
            for field_name, field_type in self.fields:
                if field_name.get():
                    if field_type.get() == "array":
                        valid_fields.append({
                            "name": field_name.get(),
                            "type": "array",
                            "items": {
                                "type": self.array_type.get()
                            }
                        })
                    else:
                        valid_fields.append({
                            "name": field_name.get(),
                            "type": field_type.get()
                        })

            json.dump({
                "$schema": "http://json-schema.org/schema#",
                "title": schema_name,
                "data format": schema_data,
                "parentclass":"WIP",
                "schema version":"00",
                "type": "ojbect",
                "properties": valid_fields
                
            }, f, indent=4)

        print("Schema created successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    schema_creator = SchemaCreator(root)
    schema_creator.pack()
    root.mainloop()