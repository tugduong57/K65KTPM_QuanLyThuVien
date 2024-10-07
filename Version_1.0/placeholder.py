## Các hàm để tạo Dòng chữ mờ tại Entry  - placeholder
def set_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text); entry.config(fg='grey')

def on_entry_click(event, entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end"); entry.config(fg='#145da0')

def on_focusout(event, entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text); entry.config(fg='grey')

def apply_placeholder(entry, placeholder_text):
    # Áp dụng placeholder cho một Entry.
    set_placeholder(entry, placeholder_text) 
    entry.bind("<FocusIn>", lambda event: on_entry_click(event, entry, placeholder_text))
    entry.bind("<FocusOut>", lambda event: on_focusout(event, entry, placeholder_text))
