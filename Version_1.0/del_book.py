import Version0_5, connectSQL

def del_book(root,bookOfID):
    connectSQL.delete_sach(bookOfID)
    Version0_5.quanlykhosach(root)
    
