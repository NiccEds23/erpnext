# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SalesPickupStockItem(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		final_qty: DF.Float
		item_code: DF.Link | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		reserve_qty: DF.Float
		source_final_qty: DF.Float
		source_warehouse: DF.Link | None
		stock_qty: DF.Float
		target_warehouse: DF.Link | None
	# end: auto-generated types
	pass
