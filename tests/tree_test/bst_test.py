import unittest
from trees.bst import BST
from trees.bst import Node
import random
import math

def black_height(curr):
    if curr is None:
        return 1
    left_bh = black_height(curr.left)
    right_bh = black_height(curr.right)
    if left_bh == -1 or right_bh == -1 or left_bh != right_bh:
        return -1
    return left_bh + int(not curr._Node__red)

def consec_red(curr):
    if curr is None:
        return False, False
    one_red_l, two_red_l = consec_red(curr.left)
    one_red_g, two_red_g = consec_red(curr.right)
    curr_red = curr._Node__red
    return curr_red, (two_red_l or two_red_g) or (curr_red and (one_red_l or one_red_g))



class TestRedBlack(unittest.TestCase):
    def setUp(self):
        random.seed(1957)

        largest_size = 2500
        # create trees by inserting random values
        self.insert_trees = []
        for n in range(1, largest_size, 5):
            bst = BST()
            for _ in range(n):
                bst.insert(random.randint(0,1000))
            self.insert_trees.append(bst)






        # TODO: delete random items from each tree
        """
        self.delete_trees = self.insert_trees.copy()
        for dbst in self.delete_trees:
            dels = 0
            while dels < random.randint(0,bst.len()):
                dels += int(dbst.delete(random.randint(0,1000)))
        """

    def test_black_heights_insertion(self):
        bh_rule = True
        trees = self.insert_trees
        for bst in trees:
            if black_height(bst.root) == -1:
                bh_rule = False
                break
        self.assertTrue(bh_rule)

    def test_consec_reds_insertion(self):
        red_rule = True
        trees = self.insert_trees
        for bst in trees:
            _, has_consec_red = consec_red(bst.root)
            if has_consec_red:
                red_rule = False
                break
        self.assertTrue(red_rule)

    def test_consec_red_fail(self):
        """
        # violate tree's red property
        consec_red_tree = self.insert_trees[-1].copy()
        consec_red_tree.insert_no_rebalance(random.randint(0,1000))
        self.assertTrue(consec_red(consec_red_tree.root))
        """
    """
    def test_black_heights_deletion(self):
        bh_rule = True
        trees = self.delete_trees
        for bst in trees:
            if black_height(bst.root) == -1:
                bh_rule = False
        self.assertTrue(bh_rule)
    """

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestRedBlack('test_black_heights_insertion'))
    suite.addTest(TestRedBlack('test_consec_reds_insertion'))
    suite.addTest(TestRedBlack('test_consec_red_fail'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())