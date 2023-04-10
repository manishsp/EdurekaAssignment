#
#
# class Order(CustomerNotAllowedException):
#
#     def __init__(self):
#         self.value = self
#
#     def __str__(self):
#         pass
#
#     def createOrder(self, customerfname, blacklistvalue, productname, productcode):
#         self.customerfname = customerfname
#         self.blacklistvalue = blacklistvalue
#         self.productname = productname
#         self.productcode = productcode
#
#         if blacklistvalue == 1:
#             raise Merger.CustomerNotAllowedException
#         else:
#             print(f"{customerfname} is allowed")
