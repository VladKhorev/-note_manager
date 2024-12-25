username = "Владислав"
title = "Заметка о проекте"
content = "Описание проекта, который нужно завершить к дедлайну."
status = "В процессе"
created_date = "23-12-2024"
issue_date = "23-12-2024"
temp_created_date = created_date[:-5]
temp_issue_date = issue_date[:-5]

print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
print("Дата создания заметки:", temp_created_date)
print("Дата истечения заметки:", temp_issue_date)
