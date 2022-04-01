# Helper method to update attribute of class
def update_attrs(update_obj, update_with_obj):
    # vars() will convert class <attr, val> to dict <key, val>
    update_obj = vars(update_obj)
    update_with_obj = vars(update_with_obj)
    
    # Iterating over two dicts at a time to update
    for (_, _), (update_with_obj_key, update_with_obj_val) \
        in zip(update_obj.items(), update_with_obj.items()):
            if update_with_obj[update_with_obj_key] is not None:
                update_obj.update({update_with_obj_key: update_with_obj_val})
    return