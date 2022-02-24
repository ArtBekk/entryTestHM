def reverse_sort_by_magnitude(obj_list, key='absolute_magnitude_h'):
    less = []
    equal = []
    greater = []

    if len(obj_list) > 1:
        pivot = obj_list[0][key]
        for obj in obj_list:
            if obj[key] > pivot:
                less.append(obj)
            elif obj[key] == pivot:
                equal.append(obj)
            elif obj[key] < pivot:
                greater.append(obj)
        return reverse_sort_by_magnitude(less) + equal + reverse_sort_by_magnitude(greater)
    else:
        return obj_list
