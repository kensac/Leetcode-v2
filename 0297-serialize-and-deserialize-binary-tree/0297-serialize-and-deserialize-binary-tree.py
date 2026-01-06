# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def serializer(root, string=""):
            if not root:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = serializer(root.left, string)
                string = serializer(root.right, string)

            return string

        print(serializer(root))
        return serializer(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def deserializer(string_list):
            if string_list[0] == "None":
                string_list.pop(0)
                return None

            root = TreeNode(string_list.pop(0))
            root.left = deserializer(string_list)
            root.right = deserializer(string_list)

            return root

        data_list = data.split(",")
        return deserializer(data_list)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
