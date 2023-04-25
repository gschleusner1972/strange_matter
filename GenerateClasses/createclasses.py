import csv

# Define the output file name
OUTPUT_FILE_NAME = "classes.py"

# Function to remove data types from arguments for "self.<arg> = <arg>" statements
def remove_data_type(arg):
    return arg.split(':')[0].strip()

# Read the CSV file
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Get the parent class details from the first row
    parent_class_row = next(csv_reader)
    parent_class_name = parent_class_row[1]
    parent_class_args = parent_class_row[2:]
    parent_class_args_str = ", ".join(parent_class_args)
    parent_class_args_no_type = [remove_data_type(arg) for arg in parent_class_args]
    # Generate the subclasses
    sub_classes = []
    for row in csv_reader:
        sub_class_name = row[1]
        sub_class_args = [arg for arg in row[2:] if arg]  # Filter out blank values
        sub_class_args_str = ", ".join(sub_class_args)
        sub_class_args_no_type = [remove_data_type(arg) for arg in sub_class_args]
        sub_class_code = f"class {sub_class_name}({parent_class_name}):\n\tdef __init__(self, {parent_class_args_str}, {sub_class_args_str}):\n\t\tsuper().__init__({', '.join(parent_class_args_no_type)})\n\t\t{'; '.join([f'self.{arg} = {arg}' for arg in sub_class_args_no_type])}\n\n"
        sub_classes.append(sub_class_code)

# Write the output file
with open(OUTPUT_FILE_NAME, "w") as output_file:
    output_file.write(f"class {parent_class_name}:\n\tdef __init__(self, {parent_class_args_str}):\n\t\t{'; '.join([f'self.{arg} = {arg}' for arg in parent_class_args_no_type])}\n\n")
    output_file.write("".join(sub_classes))
