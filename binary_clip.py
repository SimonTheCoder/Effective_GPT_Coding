import tkinter as tk
from tkinter import filedialog
import os

def extract_data():
    file_path = file_entry.get()
    start_point = start_entry.get()
    end_point = end_entry.get()

    if not file_path or not start_point or not end_point:
        result_label.config(text="请填写所有字段")
        return

    try:
        start_point = int(start_point, 0)
        end_point = int(end_point, 0)
    except ValueError:
        result_label.config(text="起始点和结束点必须是整数")
        return

    if start_point >= end_point:
        result_label.config(text="起始点必须小于结束点")
        return

    with open(file_path, 'rb') as f:
        f.seek(start_point)
        data = f.read(end_point - start_point)

    base_name = os.path.basename(file_path)
    file_name, file_ext = os.path.splitext(base_name)
    new_file_name = f"{file_name}_{start_point}_{end_point}{file_ext}"
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

    with open(new_file_path, 'wb') as f:
        f.write(data)

    result_label.config(text="文件提取完成")

def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

root = tk.Tk()
root.title("二进制文件提取")
root.geometry("400x200")

file_label = tk.Label(root, text="文件路径:")
file_label.pack()

file_entry = tk.Entry(root, width=50)
file_entry.pack()

browse_button = tk.Button(root, text="浏览", command=browse_file)
browse_button.pack()

start_label = tk.Label(root, text="起始点:")
start_label.pack()

start_entry = tk.Entry(root, width=20)
start_entry.pack()

end_label = tk.Label(root, text="结束点:")
end_label.pack()

end_entry = tk.Entry(root, width=20)
end_entry.pack()

extract_button = tk.Button(root, text="开始处理", command=extract_data)
extract_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
