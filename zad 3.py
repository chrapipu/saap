def read_subjects(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def extract_numbers(s):
    return sum([int(num) for num in s if num.isdigit()])

def process_subjects(subject_lines):
    subjects_dict = {}
    for line in subject_lines:
        parts = line.split(':')
        subject = parts[0].strip()
        if len(parts) > 1:
            num_classes = extract_numbers(parts[1])
            subjects_dict[subject] = num_classes
    return subjects_dict

def main():
    file_path = 'предметы.txt'
    subject_lines = read_subjects(file_path)
    subjects_dict = process_subjects(subject_lines)

    print(subjects_dict)

if __name__ == "__main__":
    main()
