# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SalesPickupStock(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.selling.doctype.sales_pickup_stock_item.sales_pickup_stock_item import SalesPickupStockItem
		from frappe.types import DF

		amended_from: DF.Link | None
		end_date: DF.Date | None
		items: DF.Table[SalesPickupStockItem]
		naming_series: DF.Literal["PS-.MM.YYYY.-"]
		posting_date: DF.Date | None
		start_date: DF.Date | None
		target_warehouse: DF.Link | None
	# end: auto-generated types
	pass
