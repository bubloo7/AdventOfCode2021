import json
import copy
arr = [json.loads(x) for x in open('Day 18/input').read().split('\n')]


class Node:
    def __init__(self, value, temp):
        self.value = value
        self.left = None
        self.right = None
        self.temp = temp
        self.parent = None

    def __str__(self):
        return str(self.value)

    __repr__ = __str__

    def levels(self):
        q = [self]
        lq = []
        ans = [[self]]
        while len(q) > 0:
            node = q.pop(0)
            if node.left is not None:
                lq.append(node.left)
            if node.right is not None:
                lq.append(node.right)
            if len(q) == 0:
                ans.append(lq)
                temp = []
                for t in lq:
                    temp.append(t)
                lq = []
                q = temp
        return ans

    def height(self):
        if self.left is None and self.right is None:
            return 0
        return 1 + max(self.left.height(), self.right.height())

    def inorder(self, L):
        if self.left is not None:
            self.left.inorder(L)
        if not self.temp:
            L.append(self)
        if self.right is not None:
            self.right.inorder(L)
        return L

    def predeccessor(self):
        if self.left is not None:
            return self.left.max()
        else:
            return self.parent


def makeTree(a):
    if type(a) == int:
        return Node(a, False)
    else:
        temp = Node('x', True)
        temp.left = makeTree(a[0])
        temp.left.parent = temp
        temp.right = makeTree(a[1])
        temp.right.parent = temp
        return temp


def breakTree(a):
    if type(a.value) == int:
        return a.value
    else:
        ans = [breakTree(a.left), breakTree(a.right)]
        return ans


def explode(node):
    l = None
    r = None

    if node.height() == 5:
        lvls = node.levels()
        iorder = node.inorder([])

        for i in range(len(lvls[4])):
            if lvls[4][i].temp:
                lvls[4][i].temp = False
                l = lvls[4][i].left
                r = lvls[4][i].right
                lvls[4][i].left = None
                lvls[4][i].right = None
                lvls[4][i].value = 0

                break

        for i in range(len(iorder)):
            if iorder[i] is l:
                if i - 1 >= 0:
                    iorder[i - 1].value += l.value
                if i + 2 < len(iorder):
                    iorder[i + 2].value += r.value
        return True
    return False


def split(node):
    iorder = node.inorder([])

    for i in range(len(iorder)):
        curr = iorder[i]
        if curr.value >= 10:
            val = curr.value
            par = curr.parent
            if par.left is curr:
                par.left = Node('y', True)
                par.left.left = Node(val // 2, False)
                par.left.right = Node(val // 2 + val % 2, False)
                par.left.parent = par
                node.left.left.parent = node.left
                node.left.right.parent = node.left
                return True
            if par.right is curr:
                par.right = Node('y', True)
                par.right.left = Node(val // 2, False)
                par.right.right = Node(val // 2 + val % 2, False)
                par.right.parent = par
                node.right.left.parent = node.right
                node.right.right.parent = node.right
                return True

    return False


def reduce(node):
    cont = True
    while cont:
        cont = False
        if explode(node):
            node = makeTree(breakTree(node))
            cont = True
            continue
        if split(node):
            node = makeTree(breakTree(node))
            cont = True
            continue
    return node


def magnitude(num):
    if type(num) == list:
        return magnitude(num[0])*3 + magnitude(num[1])*2
    else:
        return num


ans = -1
for i in range(len(arr)):
    for j in range(len(arr)):
        ans = max(ans, magnitude(
            breakTree(reduce(makeTree([arr[i], arr[j]])))))

print(ans)  # answer is 4347
