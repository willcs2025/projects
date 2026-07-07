@@ -0,0 +1,28 @@
+   from tkinter import *
+
+   from tkinter.tkk import *
+
+   window = Tk()
+
+   window.title("Turtle Code")
+
+   window.geometry("350x200")
+
+   combo = Combobox(window)
+
+   combo['values'] = (1, 2, 3, 4, 5, "Text")
+
+   combo.current(2)
+
+   combo.grid(column = 0, row = 0)
+
+   lbl = Label(window, text= " Hello ")
+   lbl.grid(column= 1, row= 4)
+
+   def clicked
+       lbl.configure(text = combo.get())
+
+   btn = Button(window, text= "Click me", command = clicked)
+   btn.grid(column=2, row= 0)
+
+   window.mainloop()
\ No newline at end of file

 
