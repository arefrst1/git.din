class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# تابع برای گسترش درخت دودویی
def expand_tree(root):
    if root is None:
        return None


    #testttttttttt
    # استفاده از یک صف برای جستجو در سطح به سطح
    queue = [root]  # صف برای پیمایش درخت

    while queue:
        current_node = queue.pop(0)  # گره جاری را از صف بردارید
        
        # اگر گره چپ ندارد، یک گره جدید اضافه کن
        if current_node.left is None:
            current_node.left = Node(-1)  # گره جدید با مقدار دلخواه، در اینجا -1

        # اگر گره راست ندارد، یک گره جدید اضافه کن
        if current_node.right is None:
            current_node.right = Node(-1)  # گره جدید با مقدار دلخواه، در اینجا -1

        # گره‌های چپ و راست جدید را به صف اضافه کن
        queue.append(current_node.left)
        queue.append(current_node.right)
        
    return root 

# تابع برای نمایش درخت به صورت پیش‌سفارش (Pre-order)
def pre_order_traversal(root):
    if root is None:
        return
    print(root.value, end=" ")
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)

# ایجاد درخت دودویی اولیه
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

print("درخت اولیه:")
pre_order_traversal(root)  # پیمایش پیش‌سفارش (چاپ مقادیر گره‌ها)
# گسترش درخت
expand_tree(root)
print("\nدرخت گسترش‌یافته:")
pre_order_traversal(root)  # پیمایش پیش‌سفارش بعد از گسترش
