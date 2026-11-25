def sort_parcels(parcels):
    """Merge sort: higher priority first; for ties, earlier deadline first."""
    if len(parcels) <= 1:
        return parcels[:]

    mid = len(parcels) // 2
    left = sort_parcels(parcels[:mid])
    right = sort_parcels(parcels[mid:])
    return _merge(left, right)


def _key(parcel):
    return (-parcel["priority"], parcel["deadline"])


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if _key(left[i]) <= _key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
