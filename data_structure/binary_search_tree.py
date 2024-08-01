class BinarySearchTree:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def insert_node(self, data):
		if self.data is None:
			self.data = data
		else:
			if self.data < data:
				if self.right is None:
					self.right = BinarySearchTree(data)
				else:
					self.right.insert_node(data)
			else:
				if self.left is None:
					self.left = BinarySearchTree(data)
				else:
					self.left.insert_node(data)

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
			res += self.postorder_traversal(root.right)
			res.append(root.data)

		return res

	def height(self, root):
		if root is None:
			return 0
		return max(self.height(root.left), self.height(root.right)) + 1

	def is_same_tree(self, root1, root2):
		if root1 is None and root2 is None:
			return True
		if root1 is None or root2 is None:
			return False
		if root1.data != root2.data:
			return False
		return all([self.is_same_tree(root1.left, root2.left), self.is_same_tree(root1.right, root2.right)])



if __name__ == '__main__':
	root = BinarySearchTree(23)
	root.insert_node(22)
	root.insert_node(17)
	root.insert_node(35)
	root.insert_node(11)
	root.insert_node(7)
	root.insert_node(45)

	root_2 = BinarySearchTree(23)
	root_2.insert_node(22)
	root_2.insert_node(17)
	root_2.insert_node(35)
	root_2.insert_node(11)
	root_2.insert_node(7)
	root_2.insert_node(45)

	print(root.is_same_tree(root, root_2))
