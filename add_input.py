username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки (дд-мм-гггг): ")
issue_date = input("Введите дату истечения заметки (дд-мм-гггг): ")
temp_created_date = created_date[:-5]
temp_issue_date = issue_date[:-5]

print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
print("Дата создания заметки :", temp_created_date)
print("Дата истечения заметки :", temp_issue_date)
