from common import utils


# items = [1, 2, 3, 4, 5]
items = [i for i in range(100)]


@utils.time_it
def log_all_pairs(collection):
    for counter, value in enumerate(collection):
        for counter2, value2 in enumerate(collection):
            # if counter2 == counter:
            #     continue

            print("[{0} {1}]".format(value, value2))


log_all_pairs(items)
