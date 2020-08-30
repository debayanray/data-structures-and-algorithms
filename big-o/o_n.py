from common import utils


nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel',
            'squirt', 'darla']
large = ['nemo' for i in range(10000)]


@utils.time_it
def find_nemo(collection):
    for item in collection:
        if item == 'nemo':
            print("Found NEMO!")


# find_nemo(nemo)
# find_nemo(everyone)
find_nemo(large)
