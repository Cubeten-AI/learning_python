
import tkinter as tk
from tkinter import ttk, messagebox

class StudentManager:
    def __init__(self):
        self.students=[]
        self.root=tk.Tk()
        self.root.title("Ben's Student Management Program")
        self.root.geometry("900x600")
        self.root.configure(bg="#183a66")
        tk.Label(self.root,text="🎓 Ben's Student Management Program",font=("Arial",20,"bold"),bg="#183a66",fg="white").pack(pady=10)
        f=tk.Frame(self.root,bg="#183a66"); f.pack()
        self.vars={}
        for i,l in enumerate(["ID","Name","Age","Course","Marks"]):
            tk.Label(f,text=("🆔","👤","🎂","📚","📝")[i]+" "+l,bg="#183a66",fg="white").grid(row=i,column=0,sticky="e",padx=5,pady=3)
            v=tk.StringVar(); self.vars[l]=v
            tk.Entry(f,textvariable=v).grid(row=i,column=1,padx=5,pady=3)
        bf=tk.Frame(self.root,bg="#183a66"); bf.pack(pady=8)
        for t,c in [("➕ Add",self.add),("🔍 Search",self.search),("✏️ Update",self.update),("🗑 Delete",self.delete),("📊 Average",self.avg),("🏆 Topper",self.topper),("💾 Save",self.save)]:
            tk.Button(bf,text=t,command=c).pack(side="left",padx=3)
        self.tree=ttk.Treeview(self.root,columns=("ID","Name","Age","Course","Marks"),show="headings")
        for c in ("ID","Name","Age","Course","Marks"):
            self.tree.heading(c,text=c)
        self.tree.pack(fill="both",expand=True,padx=10,pady=10)
        self.root.mainloop()
    def refresh(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        for s in self.students: self.tree.insert("",'end',values=(s["ID"],s["Name"],s["Age"],s["Course"],s["Marks"]))
    def get(self):
        return {"ID":int(self.vars["ID"].get()),"Name":self.vars["Name"].get(),"Age":int(self.vars["Age"].get()),"Course":self.vars["Course"].get(),"Marks":float(self.vars["Marks"].get())}
    def add(self):
        try:self.students.append(self.get());self.refresh()
        except Exception as e: messagebox.showerror("Error",str(e))
    def search(self):
        sid=self.vars["ID"].get()
        for s in self.students:
            if str(s["ID"])==sid:
                messagebox.showinfo("Found",str(s));return
        messagebox.showinfo("Search","Not found")
    def update(self):
        try:
            d=self.get()
            for i,s in enumerate(self.students):
                if s["ID"]==d["ID"]:
                    self.students[i]=d;self.refresh();return
            messagebox.showinfo("Update","Not found")
        except Exception as e: messagebox.showerror("Error",str(e))
    def delete(self):
        sid=self.vars["ID"].get()
        self.students=[s for s in self.students if str(s["ID"])!=sid]
        self.refresh()
    def avg(self):
        if not self.students:return
        a=sum(s["Marks"] for s in self.students)/len(self.students)
        messagebox.showinfo("Average",f"{a:.2f}")
    def topper(self):
        if not self.students:return
        t=max(self.students,key=lambda x:x["Marks"])
        messagebox.showinfo("Topper",str(t))
    def save(self):
        with open("student_list.txt","w") as f:
            for s in self.students:
                f.write(f"ID: {s['ID']}\nName: {s['Name']}\nAge: {s['Age']}\nCourse: {s['Course']}\nMarks: {s['Marks']}\n-----------------\n")
        messagebox.showinfo("Saved","Saved to student_list.txt")
StudentManager()
