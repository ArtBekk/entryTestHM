def filter_data(objects, key_list):
    for date, obj_list_by_date in objects.items():
        filtered_objects = []
        for obj in obj_list_by_date:
            temp_obj = {key: obj[key] for key in key_list}
            filtered_objects.append(temp_obj)
        objects[date] = filtered_objects
    return objects
