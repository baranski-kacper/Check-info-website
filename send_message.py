import win32com.client as win32
outlook=win32.Dispatch('outlook.application')s
mail=outlook.CreateItem(0)
mail.To='baranski.kacper94@gmail.com'
mail.Subject='Message subject'
mail.Body='Message body'
mail.HTMLBody='<h2>HTML Message body</h2>' #this field is optional

mail.Send()
