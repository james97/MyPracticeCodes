from collections import defaultdict
from typing import Union, List

coupons = [
    {"Coupon Name": "50% off", "Category Name": "Bedding"},
    {"Coupon Name": "BOGO", "Category Name": "Kitchen"},
    {"Coupon Name": "BOGO only for Garden", "Category Name": "Garden"},
    {"Coupon Name": "BOGO only for Garden1", "Category Name": "Garden"}
]
categories = [
    {"Category Name": "Comforter", "Parent category Name": "Bedding"},
    {"Category Name": "Kitchen", "Parent category Name": None},
    {"Category Name": "Patio", "Parent category Name": "Garden"}
]


def build_category_tree():
    category_tree = defaultdict(dict)
    for c in categories:
        category_tree[c["Category Name"]]["parent"] = c["Parent category Name"]
        category_tree[c["Category Name"]]["coupons"] = []
    for c in coupons:
        category_name = c["Category Name"]
        if category_name not in category_tree:
            category_tree[category_name] = {"parent": None, "coupons": []}
        category_tree[category_name]["coupons"].append(c["Coupon Name"])
    return category_tree


def get_coupon(category_name: str) -> Union[List[str], None]:
    category_tree = build_category_tree()
    while category_name:
        if category_name not in category_tree:
            return None
        coupons = category_tree[category_name].get("coupons")
        if coupons:
            return coupons
        else:
            category_name = category_tree[category_name].get("parent")

    return None


if __name__ == "__main__":
    category_name = "Patio"
    print(get_coupon(category_name))
