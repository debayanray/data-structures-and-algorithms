from common import utils


@utils.time_it
def has_common_item(collection1, collection2):
    len1 = len(collection1)
    len2 = len(collection2)
    lookup_set = set()
    primary_collection, secondary_collection = (
        (collection1, collection2) if len1 > len2
        else (collection2, collection1))

    for index, val in enumerate(primary_collection):

        val_to_check = primary_collection[index]
        if val_to_check in lookup_set:
            return True

        if index < len(secondary_collection):

            val_to_check_against = secondary_collection[index]
            if val_to_check == val_to_check_against:
                return True

            lookup_set.add(val_to_check_against)

    return False


arr1 = ['a', 'b', 'c', 'x']
arr1 = [1 for _ in range(1000000)]

arr2 = ['z', 'y', 'i']
arr2 = []
arr2 = ['z', 'y', 'x', 'b', 'c', 'a']

print(has_common_item(arr1, arr2))
