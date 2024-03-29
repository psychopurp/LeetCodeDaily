from bitarray import bitarray
import math
import mmh3


class BloomFilter:
    """
    Class for Bloom filter, using murmur3 hash function
    """

    def __init__(self, items_count: int, fp_prob: float) -> None:
        """
        items_count : int
            Number of items expected to be stored in bloom filter
        fp_prob : float
            False Positive probability in decimal. False Positive means all of the hash digest were in the bit array, but it actually doesn't exist.
        """

        # False possible probability in decimal
        self.fp_prob = fp_prob

        # Size of bit array to use
        self.size = self.get_size(items_count, fp_prob)

        # number of hash functions to use
        self.hash_count = self.get_hash_count(self.size, items_count)

        # Bit array of given size
        self.bit_arrat = bitarray(self.size)

        # initialize all bits as 0
        self.bit_arrat.setall(0)

    def add(self, item: str):
        """
        Add an item in the filter
        """

        digests = []
        for i in range(self.hash_count):
            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)

            # set the bit True in bit_array
            self.bit_arrat[digest] = True

    def check(self, item: str) -> bool:
        """
        Check for existence of an item in filter
        """

        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if not self.bit_arrat[digest]:
                # if any of bit is False then,its not present
                # in filter
                # else there is probability that it exist
                return False

        return True

    @classmethod
    def get_size(self, n: int, p: float) -> int:
        """
        Return the size of bit array(m) to used using
        following formula
        m = -(n * lg(p)) / (lg(2)^2)
        n : int
            number of items expected to be stored in filter
        p : float
            False Positive probability in decimal
        """
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @classmethod
    def get_hash_count(self, m: int, n: int) -> int:
        """
        Return the hash function(k) to be used using
        following formula
        k = (m/n) * lg(2)

        m : int
            size of bit array
        n : int
            number of items expected to be stored in filter
        """
        k = (m / n) * math.log(2)
        return int(k)


def run_test():
    from random import shuffle

    n = 20  # no of items to add
    p = 0.05  # false positive probability

    bloomf = BloomFilter(n, p)
    print("Size of bit array:{}".format(bloomf.size))
    print("False positive Probability:{}".format(bloomf.fp_prob))
    print("Number of hash functions:{}".format(bloomf.hash_count))

    # words to be added
    word_present = [
        "abound",
        "abounds",
        "abundance",
        "abundant",
        "accessible",
        "bloom",
        "blossom",
        "bolster",
        "bonny",
        "bonus",
        "bonuses",
        "coherent",
        "cohesive",
        "colorful",
        "comely",
        "comfort",
        "gems",
        "generosity",
        "generous",
        "generously",
        "genial",
    ]

    # word not added
    word_absent = [
        "bluff",
        "cheater",
        "hate",
        "war",
        "humanity",
        "racism",
        "hurt",
        "nuke",
        "gloomy",
        "facebook",
        "geeksforgeeks",
        "twitter",
    ]

    for item in word_present:
        bloomf.add(item)

    shuffle(word_present)
    shuffle(word_absent)

    test_words = word_present[:10] + word_absent
    shuffle(test_words)
    for word in test_words:
        if bloomf.check(word):
            if word in word_absent:
                print("'{}' is a false positive!".format(word))
            else:
                print("'{}' is probably present!".format(word))
        else:
            print("'{}' is definitely not present!".format(word))


run_test()
