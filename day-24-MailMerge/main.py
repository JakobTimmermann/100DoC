names = []
with open("/home/daisy/data/100DoC/day24-MailMerge/Input/Names/invited_names.txt") as name_file:
    names = name_file.read().splitlines()

with open("/home/daisy/data/100DoC/day24-MailMerge/Input/Letters/starting_letter.txt") as file:
    letter_template = file.read()
    for name in names:
        new_letter = letter_template.replace('[name]', name)
        with open(f"/home/daisy/data/100DoC/day24-MailMerge/Output/ReadyToSend/{name}.txt","w") as final_mail:
            final_mail.write(new_letter)
