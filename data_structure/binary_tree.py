class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class BinaryTree:

	def __init__(self):
		self.root = None

	def insert_node(self, data):
		new_node = Node(data)
		if self.root is None:
			self.root = new_node
			return True
		else:
			q = []
			q.append(self.root)
			while q:
				node = q.pop(0)
				if node.left is None:
					node.left = new_node
					return True
				elif node.left:
					q.append(node.left)

				if node.right is None:
					node.right = new_node
					return True
				elif node.right:
					q.append(node.right)

	def preorder_traversal(self, root):
		res = []
		if root:
			res.append(root.data)
			res += self.preorder_traversal(root.left)
			res += self.preorder_traversal(root.right)
		return res

	def inorder_traversal(self, root):
		res = []
		if root:
			res += self.inorder_traversal(root.left)
			res.append(root.data)
			res += self.inorder_traversal(root.right)
		return res

	def postorder_traversal(self, root):
		res = []
		if root:
			res += self.postorder_traversal(root.left)
			res.append(root.data)
			res += self.postorder_traversal(root.right)
		return res

	def levelorder_traversal(self, root):
		res = []
		q = []
		q.append(root)
		while q:
			node = q.pop(0)
			res.append(node.data)
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)

		return res

	def height(self, root):
		if root is None:
			return 0
		return max(self.height(root.left), self.height(root.right)) + 1

	def convert_mirror_tree(self, root):
		if root is None:
			return root
		self.convert_mirror_tree(root.left)
		self.convert_mirror_tree(root.right)
		root.left, root.right = root.right, root.left
		return root

	def symmetric_tree(self, root):
		if root is None:
			return True
		if root.data != root.data:
			return False

		def helper(root1, root2):
			if root1 is None and root2 is None:
				return True
			if root1 is None or root2 is None:
				return False
			if root1.data != root2.data:
				return False
			l = helper(root1.left, root2.right)
			r = helper(root1.right, root2.left)
			return all([l, r])
		l = root.left
		r = root.right
		return helper(l, r)


if __name__ == '__main__':
	root = BinaryTree()
	root.insert_node(7)
	root.insert_node(3)
	root.insert_node(6)
	root.insert_node(9)
	root.insert_node(11)
	root.insert_node(15)
	root.insert_node(2)

	print(root.levelorder_traversal(root.root))

	root_3 = root.convert_mirror_tree(root.root)
	print(root.levelorder_traversal(root_3))
