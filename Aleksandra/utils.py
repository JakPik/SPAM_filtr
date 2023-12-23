def read_classification_from_file(file_path):
    classification_dict={}
    with open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                email_name, classification = parts
                classification_dict[email_name] = classification
    return classification_dict