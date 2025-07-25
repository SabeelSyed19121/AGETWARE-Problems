import json
def overlap_fraction(pos1, pos2):
    left1, right1 = pos1
    left2, right2 = pos2

    overlap_left = max(left1, left2)
    overlap_right = min(right1, right2)
    overlap = max(0, overlap_right - overlap_left)

    length1 = right1 - left1
    length2 = right2 - left2

    frac1 = overlap / length1 if length1 > 0 else 0
    frac2 = overlap / length2 if length2 > 0 else 0

    return frac1, frac2

def combine_lists(list1, list2):
    combined = []
    used_in_list2 = set()

    for idx1, item1 in enumerate(list1):
        pos1 = item1['positions']
        values1 = item1['values']
        merged = False

        for idx2, item2 in enumerate(list2):
            if idx2 in used_in_list2:
                continue

            pos2 = item2['positions']
            values2 = item2['values']

            frac1, frac2 = overlap_fraction(pos1, pos2)

            if frac1 > 0.5 or frac2 > 0.5:
                if pos1[0] <= pos2[0]:
                    new_pos = pos1
                else:
                    new_pos = pos2

                new_values = values1 + values2
                combined.append({"positions": new_pos, "values": new_values})
                used_in_list2.add(idx2)
                merged = True
                break

        if not merged:
            combined.append(item1)

    for idx2, item2 in enumerate(list2):
        if idx2 not in used_in_list2:
            combined.append(item2)

    combined.sort(key=lambda x: x['positions'][0])
    return combined
if _name_ == "_main_":
    print("Enter list1 JSON:")
    list1 = json.loads(input())

    print("Enter list2 JSON:")
    list2 = json.loads(input())

    result = combine_lists(list1, list2)

    print("Combined result:")
    print(json.dumps(result, indent=2))
